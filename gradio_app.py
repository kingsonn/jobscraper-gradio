import gradio as gr
import pandas as pd
import numpy as np
import os
import time
from jobscraper import search_jobs

def format_job_results(df):
    """Format job results for display in Gradio."""
    if df.empty:
        return "No jobs found."
    
    # Create a formatted HTML table for better display
    html = "<div style='max-height: 600px; overflow-y: auto;'>"
    html += "<table style='width: 100%; border-collapse: collapse;'>"
    
    # Table header with updated color for better visibility
    html += "<tr style='background-color: #2c3e50; color: white; position: sticky; top: 0;'>"
    for col in ['Title', 'Company', 'Location', 'Date Posted', 'Site', 'Apply']:
        html += f"<th style='padding: 12px; text-align: left; border-bottom: 1px solid #ddd;'>{col}</th>"
    html += "</tr>"
    
    # Table rows with blue hover color for better text visibility
    for _, row in df.iterrows():
        html += "<tr style='border-bottom: 1px solid #eee; transition: background-color 0.3s;' onmouseover=\"this.style.backgroundColor='#e3f2fd'\" onmouseout=\"this.style.backgroundColor='transparent'\">"
        
        # Title
        title = row.get('title', 'N/A')
        html += f"<td style='padding: 12px;'><strong>{title}</strong></td>"
        
        # Company
        company = row.get('company', 'N/A')
        html += f"<td style='padding: 12px;'>{company}</td>"
        
        # Location
        location = row.get('location', 'N/A')
        html += f"<td style='padding: 12px;'>{location}</td>"
        
        # Date Posted
        date_posted = row.get('date_posted', 'N/A')
        html += f"<td style='padding: 12px;'>{date_posted}</td>"
        
        # Site
        site = row.get('site', 'N/A')
        html += f"<td style='padding: 12px;'>{site}</td>"
        
        # Apply Link
        job_url = row.get('job_url', '#')
        if job_url and job_url != '#' and not pd.isna(job_url):
            html += f"<td style='padding: 12px;'><a href='{job_url}' target='_blank' style='color: #2196F3; text-decoration: none;'>Apply</a></td>"
        else:
            html += "<td style='padding: 12px;'>No link</td>"
        
        html += "</tr>"
    
    html += "</table></div>"
    return html

def search_and_display_jobs(role, location, indeed, linkedin, glassdoor, google, naukri, 
                           results_per_site, hours_old, country, use_proxies, use_google_search):
    """Search for jobs and return formatted results."""
    # Create site list based on selections
    site_list = []
    if indeed:
        site_list.append("indeed")
    if linkedin:
        site_list.append("linkedin")
    if glassdoor:
        site_list.append("glassdoor")
    if google:
        site_list.append("google")
    if naukri:
        site_list.append("naukri")
    
    if not site_list:
        return "Please select at least one job site.", None
    
    try:
        # Start time for performance tracking
        start_time = time.time()
        
        # Use the search_jobs function from jobscraper.py
        jobs_df = search_jobs(
            role=role,
            location=location,
            site_names=site_list,
            results_wanted=results_per_site,
            hours_old=hours_old,
            country_indeed=country,
            use_proxies=use_proxies,
            include_google_search=use_google_search
        )
        
        # Calculate search time
        search_time = time.time() - start_time
        
        # Save to CSV
        csv_path = "jobs.csv"
        if not jobs_df.empty:
            jobs_df.to_csv(csv_path, index=False)
            
            # Create summary
            summary = f"Found {len(jobs_df)} jobs in {search_time:.2f} seconds!\n\n"
            
            # Add job count by site
            if 'site' in jobs_df.columns:
                summary += "Jobs by site:\n"
                site_counts = jobs_df['site'].value_counts()
                for site, count in site_counts.items():
                    summary += f"- {site.capitalize()}: {count} jobs\n"
            
            # Format results for display
            formatted_results = format_job_results(jobs_df)
            
            return summary, formatted_results, csv_path if os.path.exists(csv_path) else None
        else:
            return "No jobs found matching your criteria. Try adjusting your search parameters.", None, None
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return error_message, None, None

# Create the Gradio interface
with gr.Blocks(title="Job Scraper", theme=gr.themes.Soft(primary_hue="blue")) as demo:
    # Simple HTML header with the title and logo
    gr.HTML(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');
        .upleveling-brand {
            display: inline-flex;
            align-items: center;
            background-color: #2563eb;
            padding: 5px 15px;
            border-radius: 20px;
            margin-left: 10px;
        }
        .upleveling-brand span {
            font-family: 'Libre Baskerville', serif;
            color: white;
            font-weight: 500;
            font-size: 16px;
            vertical-align: middle;
        }
        .upleveling-logo {
            height: 32px;
            width: 32px;
            margin-right: 10px;
            border-radius: 4px;
            object-fit: contain;
            vertical-align: middle;
        }
        </style>
        <div style="margin-bottom: 20px; display: flex; align-items: center;">
            <h1 style="margin: 0;">🔍 Job Scraper by</h1>
            <div class="upleveling-brand">
                <img src="https://uzufwojpgyxicaypshtj.supabase.co/storage/v1/object/public/blogimg/meow/7a01ef21-37c5-4169-8ae8-7b2455a2f376.jpg" alt="UpLeveling Logo" class="upleveling-logo">
                <span>UpLeveling</span>
            </div>
        </div>
        """
    )
    
    gr.Markdown(
        """
        Search for jobs across multiple platforms including Indeed, LinkedIn, Glassdoor, Google, and Naukri.
        
        Enter your job search criteria below and click 'Search Jobs' to begin.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=2):
            # Main search parameters
            role_input = gr.Textbox(label="Job Role/Title", placeholder="e.g. Software Engineer", value="Software Engineer")
            location_input = gr.Textbox(label="Location", placeholder="e.g. Bangalore, India", value="Bangalore, India")
            
            # Job site selection
            gr.Markdown("### Job Sites")
            with gr.Row():
                indeed_checkbox = gr.Checkbox(label="Indeed", value=True)
                linkedin_checkbox = gr.Checkbox(label="LinkedIn", value=True)
                glassdoor_checkbox = gr.Checkbox(label="Glassdoor", value=True)
                google_checkbox = gr.Checkbox(label="Google", value=True)
                naukri_checkbox = gr.Checkbox(label="Naukri", value=False)
            
            # Search button
            search_button = gr.Button("Search Jobs", variant="primary")
        
        with gr.Column(scale=1):
            # Advanced options
            gr.Markdown("### Advanced Options")
            results_slider = gr.Slider(minimum=5, maximum=50, value=10, step=5, label="Results per site")
            hours_slider = gr.Slider(minimum=24, maximum=168, value=72, step=24, label="Posted within (hours)")
            country_input = gr.Textbox(label="Indeed Country", value="India")
            use_proxies = gr.Checkbox(label="Use proxies (recommended for multiple sites)", value=True)
            use_google_search = gr.Checkbox(label="Use Google search for better results", value=True)
    
    # Results section
    with gr.Row():
        with gr.Column():
            summary_output = gr.Textbox(label="Search Summary", lines=5)
            results_output = gr.HTML(label="Job Listings")
            file_output = gr.File(label="Download Results")
    
    # Set up the search function
    search_button.click(
        fn=search_and_display_jobs,
        inputs=[
            role_input, location_input, 
            indeed_checkbox, linkedin_checkbox, glassdoor_checkbox, google_checkbox, naukri_checkbox,
            results_slider, hours_slider, country_input, use_proxies, use_google_search
        ],
        outputs=[summary_output, results_output, file_output]
    )
    
    # Footer
    gr.Markdown(
        """
        ### About
        
        Job Scraper v1.0.0 - Powered by UpLeveling
        
        This tool searches multiple job sites and aggregates the results. Results are also saved to a CSV file for further analysis.
        """
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)
