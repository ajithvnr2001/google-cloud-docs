---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-multi-location-search/
title: Multiple location search (v3) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:46.224884+00:00
---

# Multiple location search (v3)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-multi-location-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Multiple location search (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Search jobs with multiple locations.

## Code sample

### Ruby

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id       = "Id of the project."
    # company_name     = "The resource name of the company listing the job. The format is "projects/{project_id}/companies/{company_id}""
    # location1        = "Location of the center where the first search is based on"
    # distance1        = "The distance from the provided location in miles in which to search."
    # city             = "Name of the city where we want to do the second search."
    require "google/apis/jobs_v3"
    # Instantiate the client
    jobs = Google::Apis::JobsV3
    talent_solution_client = jobs::CloudTalentSolutionService.new
    # @see
    # https://developers.google.com/identity/protocols/application-default-credentials#callingruby
    talent_solution_client.authorization = Google::Auth.get_application_default(
      "https://www.googleapis.com/auth/jobs"
    )
    # Make sure to set the requestMetadata the same as the associated search request
    request_metadata = jobs::RequestMetadata.new user_id:    "HashedUserId",
                                                 session_id: "HashedSessionId",
                                                 domain:     "www.google.com"
    
    # Set location filter
    location_filter1 = jobs::LocationFilter.new address:           location1,
                                                distance_in_miles: distance1
    location_filter2 = jobs::LocationFilter.new address: city2
    # Perform a search for analyst  related jobs
    job_query = jobs::JobQuery.new location_filters: [location_filter1, location_filter2],
                                   company_names:    [company_name]
    
    search_jobs_request = jobs::SearchJobsRequest.new request_metadata: request_metadata,
                                                      job_query:        job_query,
                                                      search_mode:      "JOB_SEARCH"
    
    search_jobs_response = talent_solution_client.search_jobs project_id, search_jobs_request
    
    puts search_jobs_response.to_json
    search_jobs_response

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
