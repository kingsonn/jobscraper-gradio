# Job Scraper with Gradio UI

A powerful job search aggregator that scrapes multiple job sites (Indeed, LinkedIn, Glassdoor, Google, and Naukri) and presents the results in a clean, interactive web interface built with Gradio.

<iframe width="560" height="315" src="https://uzufwojpgyxicaypshtj.supabase.co/storage/v1/object/public/blogimg/meow/UpLeveling%20job%20scraper%201.mp4" frameborder="0" allowfullscreen></iframe>

## Features

- **Multi-platform Search**: Search for jobs across Indeed, LinkedIn, Glassdoor, Google, and Naukri simultaneously
- **Customizable Search**: Filter by job title, location, and posting date
- **Interactive UI**: Clean, user-friendly interface built with Gradio
- **Data Export**: Download search results as CSV files for further analysis
- **Proxy Support**: Built-in proxy rotation to avoid rate limiting
- **Advanced Options**: Control search behavior with various parameters

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone this repository or download the source code:

```bash
git clone https://github.com/yourusername/jobscraper-gradio.git
cd jobscraper-gradio
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application with:

```bash
python gradio_app.py
```

This will start a local web server and open the interface in your default web browser. If it doesn't open automatically, navigate to the URL displayed in the terminal (typically http://127.0.0.1:7860).

## Build Your Own in 15 Minutes

Want to quickly build a similar job scraper application? Follow this express tutorial to create your own version in just 15 minutes using AI assistance!

### Step 1: Create a Basic JobSpy Script (2 minutes)

Create a file named `simple_jobscraper.py` with this basic JobSpy function:

```python
import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google", "bayt", "naukri"],
    search_term="software engineer",
    google_search_term="software engineer jobs near Mumbai, India since yesterday",
    location="Mumbai, India",
    results_wanted=20,
    hours_old=72,
    country_indeed='India',
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
```

**Note**: JobSpy returns a rich dataset with many columns including:
```
id, site, job_url, job_url_direct, title, company, location, date_posted, job_type, 
salary_source, interval, min_amount, max_amount, currency, is_remote, job_level, 
job_function, listing_type, emails, description, company_industry, company_url, 
company_logo, company_url_direct, company_addresses, company_num_employees, 
company_revenue, company_description, skills, experience_range, company_rating, 
company_reviews_count, vacancy_count, work_from_home_type
```

You can choose which columns to display in your Gradio interface based on your needs.

### Step 2: Install Required Packages (1 minute)

```bash
pip install jobspy gradio pandas
```

### Step 3: Use AI to Create the Gradio Interface (10 minutes)

Copy the following prompt and paste it into ChatGPT, Claude, or your AI coding assistant:

```
I have a Python script that scrapes job listings using the JobSpy library. Here's the code:


import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google", "bayt", "naukri"],
    search_term="software engineer",
    google_search_term="software engineer jobs near Mumbai, India since yesterday",
    location="Mumbai, India",
    results_wanted=20,
    hours_old=72,
    country_indeed='India',
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)


The JobSpy response includes many columns. Here are all the available columns:
id, site, job_url, job_url_direct, title, company, location, date_posted, job_type, 
salary_source, interval, min_amount, max_amount, currency, is_remote, job_level, 
job_function, listing_type, emails, description, company_industry, company_url, 
company_logo, company_url_direct, company_addresses, company_num_employees, 
company_revenue, company_description, skills, experience_range, company_rating, 
company_reviews_count, vacancy_count, work_from_home_type

Please create a Gradio web interface for this job scraper with the following features:

1. A clean, professional UI with a blue color scheme
2. Input fields for:
   - Job title/role
   - Location
   - Checkboxes for selecting which job sites to search (Indeed, LinkedIn, Glassdoor, Google, Naukri)
   - A slider for "Results per site" (5-50, default 10)
   - A slider for "Posted within hours" (24-168, default 72)
   - A text field for "Country" (default "India")

3. A "Search Jobs" button that triggers the job search

4. Output sections for:
   - A summary of results (number of jobs found, time taken)
   - A nicely formatted HTML table showing the job listings with the following columns:
     * Title - column: title
     * Company - column: company
     * Location - column: location
     * Site (which job board it came from) - column: site
     * Apply (a link to the job posting) - column: job_url
   - Option to download results as CSV with all available columns

5. The table should have:
   - A dark blue header with white text
   - Rows that highlight in light blue when hovered
   - Clean spacing and formatting

6. Add a title at the top: "🔍 Job Scraper by UpLeveling" with a subtitle explaining what the app does

Please provide the complete code for this Gradio app, making sure it's well-structured and includes proper error handling.
```

### Step 4: Implement the AI-Generated Code (2 minutes)

The AI will provide you with a complete Gradio application. Save this code to a file named `gradio_app.py`.

### Step 5: Run Your Application (30 seconds)

```bash
python gradio_app.py
```

That's it! In just 15 minutes, you've created a professional job scraping application with a clean, interactive UI.

### Bonus: Share Your App with Friends (2 minutes)

To share your app with friends or colleagues, modify the last line of your `gradio_app.py` file to include `share=True`:

```python
# Change this line at the end of your file
if __name__ == "__main__":
    demo.launch(share=True)  # Set share=True to create a public link
```

When you run the app, Gradio will generate a public URL that you can share with anyone:

```bash
python gradio_app.py
```

You should see something like:
```
Running on local URL:  http://127.0.0.1:7860
Running on public URL: https://12345.gradio.app
```

**Troubleshooting**: If you don't get a public link, try restarting your computer and running the app again. Sometimes network configurations can prevent Gradio from establishing the tunnel needed for public sharing.

Share the link with friends and let them search for jobs without having to install anything!

## Step-by-Step Tutorial: Building the Job Scraper

This tutorial will walk you through creating this job scraper application from scratch.

### Step 1: Setting Up the Job Scraper Backend

First, we'll create the backend functionality that handles the actual job scraping. This is implemented in `jobscraper.py`.

1. Import the necessary libraries:
   ```python
   import csv
   from jobspy import scrape_jobs
   import pandas as pd
   import requests
   import time
   ```

2. Set up proxy handling to avoid rate limiting:
   ```python
   # Default fallback proxies if API fails
   default_proxies_list = [
       "154.213.204.37:3128",
       "localhost"
   ]

   # Fetch proxies from proxyscrape API
   def get_proxies():
       try:
           url = "https://api.proxyscrape.com/v2/account/datacenter_shared/proxy-list?auth=your_auth_key&type=getproxies&country[]=all&protocol=http&format=normal&status=all"
           response = requests.get(url)
           # Process response and return proxy list
           # For simplicity, we'll return default proxies
           return default_proxies_list
       except Exception as e:
           print(f"Error fetching proxies: {str(e)}")
           return default_proxies_list
   ```

3. Create the main job search function that handles scraping from multiple sites:
   ```python
   def search_jobs(role, location, site_names=None, results_wanted=20, hours_old=72, country_indeed='India', use_proxies=True, include_google_search=True):
       """
       Search for jobs across multiple platforms.
       
       Args:
           role (str): Job role or title to search for
           location (str): Location to search for jobs
           site_names (list): List of job sites to search
           results_wanted (int): Number of results to return per site
           hours_old (int): Only return jobs posted within this many hours
           country_indeed (str): Country code for Indeed searches
           use_proxies (bool): Whether to use proxies for scraping
           include_google_search (bool): Whether to use Google search terms for better results
           
       Returns:
           pd.DataFrame: DataFrame containing job search results
       """
       # Implementation details...
   ```

4. Handle Google searches separately (since they require different parameters):
   ```python
   # Process Google separately without proxies
   if google_site:
       try:
           print(f"Scraping Google for {role} jobs in {location}...")
           google_search_term = f"{role} jobs near {location} since yesterday" if include_google_search else None
           
           google_jobs = scrape_jobs(
               site_name=["google"],
               search_term=role,
               google_search_term=google_search_term,
               location=location,
               results_wanted=results_wanted,
               hours_old=hours_old,
               country_indeed=country_indeed,
               # No proxies for Google to avoid 429 errors
           )
           
           if not google_jobs.empty:
               all_jobs = pd.concat([all_jobs, google_jobs], ignore_index=True)
           
       except Exception as e:
           print(f"Error scraping Google: {str(e)}")
   ```

5. Process other job sites with proxy support:
   ```python
   # Process other sites with proxies if enabled
   for site in other_sites:
       try:
           print(f"Scraping {site.capitalize()} for {role} jobs in {location}...")
           
           google_search_term = f"{role} jobs near {location} since yesterday" if include_google_search else None
           
           # Use proxies only if specified
           proxy_param = proxies_list if use_proxies else None
           
           site_jobs = scrape_jobs(
               site_name=[site],
               search_term=role,
               google_search_term=google_search_term,
               location=location,
               results_wanted=results_wanted,
               hours_old=hours_old,
               country_indeed=country_indeed,
               proxies=proxy_param,
           )
           
           if not site_jobs.empty:
               all_jobs = pd.concat([all_jobs, site_jobs], ignore_index=True)
       except Exception as e:
           print(f"Error scraping {site}: {str(e)}")
   ```

### Step 2: Building the Gradio UI

Next, we'll create the user interface using Gradio in `gradio_app.py`.

1. Import necessary libraries:
   ```python
   import gradio as gr
   import pandas as pd
   import numpy as np
   import os
   import time
   from jobscraper import search_jobs
   ```

2. Create a function to format job results as an HTML table:
   ```python
   def format_job_results(df):
       """Format job results for display in Gradio."""
       if df.empty:
           return "No jobs found."
       
       # Create a formatted HTML table for better display
       html = "<div style='max-height: 600px; overflow-y: auto;'>"
       html += "<table style='width: 100%; border-collapse: collapse;'>"
       
       # Table header with updated color for better visibility
       html += "<tr style='background-color: #2c3e50; color: white; position: sticky; top: 0;'>"
       for col in ['Title', 'Company', 'Location', 'Date Posted', 'Job Type', 'Salary', 'Is Remote', 'Site', 'Apply']:
           html += f"<th style='padding: 12px; text-align: left; border-bottom: 1px solid #ddd;'>{col}</th>"
       html += "</tr>"
       
       # Table rows with blue hover color for better text visibility
       for _, row in df.iterrows():
           # Format each row with job details
           # ...
       
       html += "</table></div>"
       return html
   ```

3. Create a function to handle the job search and display results:
   ```python
   def search_and_display_jobs(role, location, indeed, linkedin, glassdoor, google, naukri, 
                              results_per_site, hours_old, country, use_proxies, use_google_search):
       """Search for jobs and return formatted results."""
       # Create site list based on selections
       site_list = []
       if indeed:
           site_list.append("indeed")
       # Add other sites...
       
       # Call the search_jobs function from jobscraper.py
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
       
       # Format and return results
       # ...
   ```

4. Create the Gradio interface with custom styling:
   ```python
   with gr.Blocks(title="Job Scraper", theme=gr.themes.Soft(primary_hue="blue")) as demo:
       # Custom HTML header with logo
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
           /* More styling... */
           </style>
           <div style="margin-bottom: 20px; display: flex; align-items: center;">
               <h1 style="margin: 0;">🔍 Job Scraper by</h1>
               <div class="upleveling-brand">
                   <img src="your_logo_url" alt="Logo" class="upleveling-logo">
                   <span>UpLeveling</span>
               </div>
           </div>
           """
       )
   ```

5. Add input components for job search parameters:
   ```python
   with gr.Row():
       with gr.Column(scale=2):
           # Main search parameters
           role_input = gr.Textbox(label="Job Role/Title", placeholder="e.g. Software Engineer", value="Software Engineer")
           location_input = gr.Textbox(label="Location", placeholder="e.g. Bangalore, India", value="Bangalore, India")
           
           # Job site selection
           gr.Markdown("### Job Sites")
           with gr.Row():
               indeed_checkbox = gr.Checkbox(label="Indeed", value=True)
               # Other checkboxes...
           
           # Search button
           search_button = gr.Button("Search Jobs", variant="primary")
       
       with gr.Column(scale=1):
           # Advanced options
           # ...
   ```

6. Add output components to display results:
   ```python
   # Results section
   with gr.Row():
       with gr.Column():
           summary_output = gr.Textbox(label="Search Summary", lines=5)
           results_output = gr.HTML(label="Job Listings")
           file_output = gr.File(label="Download Results")
   ```

7. Connect the interface components with the search function:
   ```python
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
   ```

8. Launch the app:
   ```python
   # Launch the app
   if __name__ == "__main__":
       demo.launch(share=True)
   ```

### Step 3: Running the Application

1. Install all required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Gradio application:
   ```bash
   python gradio_app.py
   ```

3. Open your web browser and navigate to the URL displayed in the terminal (typically http://127.0.0.1:7860).

4. Enter your job search criteria, select the job sites you want to search, and click "Search Jobs".

5. View the search results in the table and download them as a CSV file if desired.

## Customization

You can customize the application by:

- Modifying the UI colors and styling in the HTML/CSS sections
- Adding additional job sites by extending the `search_jobs` function
- Changing the default search parameters
- Adding new features like job filtering or sorting

## Troubleshooting

- If you encounter rate limiting issues, try enabling the proxy option
- If a particular job site consistently fails, try disabling it and using the others
- For Google searches, avoid using proxies as they can trigger captchas

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [JobSpy](https://github.com/ZacharyHampton/JobSpy) for the job scraping functionality
- [Gradio](https://gradio.app/) for the web interface framework
