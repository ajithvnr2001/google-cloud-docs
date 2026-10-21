---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-date-range-filter-search/
title: Date search (v3) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:43.991318+00:00
---

# Date search (v3)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-date-range-filter-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Date search (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Search jobs by date.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Search filters (v3)](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-filters)



## Code sample

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // /dateRangeSearch searches for jobs on date range.
    // In JSON format, the Timestamp type is encoded as a string in the
    // [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the
    // format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z"
    // e.g. "2017-01-15T01:30:15.01Z".
    func dateRangeSearch(w io.Writer, projectID, companyName, startTime, endTime string) (*talent.SearchJobsResponse, error) {
    	ctx := context.Background()
    
    	client, err := google.DefaultClient(ctx, talent.CloudPlatformScope)
    	if err != nil {
    		return nil, fmt.Errorf("google.DefaultClient: %w", err)
    	}
    	// Create the jobs service client.
    	service, err := talent.New(client)
    	if err != nil {
    		return nil, fmt.Errorf("talent.New: %w", err)
    	}
    
    	jobQuery := &talent.JobQuery{
    		PublishTimeRange: &talent.TimestampRange{
    			StartTime: startTime,
    			EndTime:   endTime,
    		},
    	}
    	if companyName != "" {
    		jobQuery.CompanyNames = []string{companyName}
    	}
    
    	parent := "projects/" + projectID
    	req := &talent.SearchJobsRequest{
    		// Make sure to set the RequestMetadata the same as the associated
    		// search request.
    		RequestMetadata: &talent.RequestMetadata{
    			// Make sure to hash your userID.
    			UserId: "HashedUsrId",
    			// Make sure to hash the sessionID.
    			SessionId: "HashedSessionId",
    			// Domain of the website where the search is conducted.
    			Domain: "www.googlesample.com",
    		},
    		// Set the actual search term as defined in the jobQuery.
    		JobQuery: jobQuery,
    		// Set the search mode to a regular search.
    		SearchMode: "JOB_SEARCH",
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with date range [%s, %s]: %w", startTime, endTime, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Search on date range. In JSON format, the Timestamp type is encoded as a string in the [RFC
     * 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the format is
     * "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" e.g. "2017-01-15T01:30:15.01Z"
     */
    public static void dateRangeSearch(String companyName, String startTime, String endTime)
        throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash your userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
    
      TimestampRange timestampRange =
          new TimestampRange().setStartTime(startTime).setEndTime(endTime);
    
      JobQuery jobQuery = new JobQuery().setPublishTimeRange(timestampRange);
      // JobQuery jobQuery = new JobQuery().setPublishTimeRange(dateRange);
    
      if (companyName != null) {
        jobQuery.setCompanyNames(Arrays.asList(companyName));
      }
    
      SearchJobsRequest searchJobsRequest =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setJobQuery(jobQuery) // Set the actual search term as defined in the jobQurey
              .setSearchMode("JOB_SEARCH"); // Set the search mode to a regular search
    
      SearchJobsResponse searchJobsResponse =
          talentSolutionClient
              .projects()
              .jobs()
              .search(DEFAULT_PROJECT_ID, searchJobsRequest)
              .execute();
      Thread.sleep(1000);
    
      System.out.printf("Search results on jobs with a date range: %s\n", searchJobsResponse);
    }

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def date_range_search(client_service, company_name, date_range):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        job_query = {"publish_time_range": date_range}
        if company_name is not None:
            job_query.update({"company_names": [company_name]})
        request = {
            "search_mode": "JOB_SEARCH",
            "request_metadata": request_metadata,
            "job_query": job_query,
        }
    
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)

### Ruby

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id      = "Id of the project"
    # company_name    = "The resource name of the company listing the job. The format is "projects/{project_id}/companies/{company_id}""
    # start_time      = "Start time of the date range we want to search on"
    # end_time        = "End time of the date range we want to search on"
    
    require "google/apis/jobs_v3"
    # Instantiate the client
    jobs = Google::Apis::JobsV3
    talent_solution_client = jobs::CloudTalentSolutionService.new
    # @see
    # https://developers.google.com/identity/protocols/application-default-credentials#callingruby
    talent_solution_client.authorization = Google::Auth.get_application_default(
      "https://www.googleapis.com/auth/jobs"
    )
    # Make sure to set the request_metadata the same as the associated search request
    request_metadata = jobs::RequestMetadata.new user_id:    "HashedUserId",
                                                 session_id: "HashedSessionId",
                                                 domain:     "http://careers.google.com"
    
    # Perform a search for analyst  related jobs
    timestamp_range = jobs::TimestampRange.new start_time: start_time,
                                               end_time:   end_time
    job_query = jobs::JobQuery.new publish_time_range: timestamp_range,
                                   company_names:      [company_name]
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
