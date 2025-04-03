import csv
from jobspy import scrape_jobs
import pandas as pd
import requests
import time

# Default fallback proxies if API fails
default_proxies_list = [
    "154.213.204.37:3128",
    "localhost"
]

# Fetch proxies from proxyscrape API
def get_proxies():
    try:
        url = "https://api.proxyscrape.com/v2/account/datacenter_shared/proxy-list?auth=syxfulrs4twdkuq6l81q&type=getproxies&country[]=all&protocol=http&format=normal&status=all"
        response = requests.get(url)
        print(response.text)
        # if response.status_code == 200:
        #     # Parse the response text into a list of proxies
        #     proxies = response.text.strip().split('\n')
            
        #     # Filter out empty lines and add to the list
        #     proxies_list = [proxy.strip() for proxy in proxies if proxy.strip()]
            
        #     if proxies_list:
        #         print(f"Successfully fetched {len(proxies_list)} proxies from API")
        #         return proxies_list
        #     else:
        #         print("No proxies returned from API, using default proxies")
        #         return default_proxies_list
        # else:
        #     print(f"Failed to fetch proxies: HTTP {response.status_code}")
        #     return default_proxies_list
    except Exception as e:
        print(f"Error fetching proxies: {str(e)}")
        return default_proxies_list

# Get the proxies
proxies_list = get_proxies()

def search_jobs(role, location, site_names=None, results_wanted=20, hours_old=72, country_indeed='India', use_proxies=True, include_google_search=True):
    """
    Search for jobs across multiple platforms.
    
    Args:
        role (str): Job role or title to search for
        location (str): Location to search for jobs
        site_names (list): List of job sites to search (default: ["indeed", "linkedin", "glassdoor", "google"])
        results_wanted (int): Number of results to return per site
        hours_old (int): Only return jobs posted within this many hours
        country_indeed (str): Country code for Indeed searches
        use_proxies (bool): Whether to use proxies for scraping
        include_google_search (bool): Whether to use Google search terms for better results
        
    Returns:
        pd.DataFrame: DataFrame containing job search results
    """
    if site_names is None:
        site_names = ["indeed", "linkedin", "glassdoor", "google"]
    
    # Separate Google from other sites to handle differently
    google_site = None
    other_sites = site_names.copy()
    
    if "google" in other_sites:
        other_sites.remove("google")
        google_site = "google"
    
    all_jobs = pd.DataFrame()
    
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
                if all_jobs.empty:
                    all_jobs = site_jobs
                else:
                    all_jobs = pd.concat([all_jobs, site_jobs], ignore_index=True)
        except Exception as e:
            print(f"Error scraping {site}: {str(e)}")
    
    return all_jobs

# Example usage when run directly
if __name__ == "__main__":
    jobs = search_jobs(
        role="fullstack developer",
        location="Mumbai, Maharashtra, India",
        site_names=["glassdoor"],
        results_wanted=20,
        hours_old=72,
        country_indeed='India',
        use_proxies=True
    )
    
    # Save to CSV
    if not jobs.empty:
        jobs.to_csv("jobs.csv", index=False)
        print(f"Saved {len(jobs)} jobs to jobs.csv")
    else:
        print("No jobs found.")