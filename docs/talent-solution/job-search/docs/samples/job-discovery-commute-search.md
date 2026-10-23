---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-commute-search/
title: Commute search (v3) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:10.814908+00:00
---

# Commute search (v3)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-commute-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Commute search (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Search jobs by commute attributes including commute method, coordinates, and maximum travel time.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Commute search (v3)](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-commute)
  * [Implementing Commute Search in your UI (v3)](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/commute-search)



## Code sample

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // commuteSearch searches for jobs within commute filter.
    func commuteSearch(w io.Writer, projectID, companyName string) (*talent.SearchJobsResponse, error) {
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
    		CommuteFilter: &talent.CommuteFilter{
    			RoadTraffic:    "TRAFFIC_FREE",
    			CommuteMethod:  "TRANSIT",
    			TravelDuration: "1000s",
    			StartCoordinates: &talent.LatLng{
    				Latitude:  37.422408,
    				Longitude: -122.085609,
    			},
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
    		SearchMode:               "JOB_SEARCH",
    		RequirePreciseResultSize: true,
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with commute filter: %w", err)
    	}
    	return resp, nil
    }
    

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static void commuteSearch(String companyName) throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash your userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
      JobQuery jobQuery =
          new JobQuery()
              .setCommuteFilter(
                  new CommuteFilter()
                      .setRoadTraffic("TRAFFIC_FREE")
                      .setCommuteMethod("TRANSIT")
                      .setTravelDuration("1000s")
                      .setStartCoordinates(
                          new LatLng().setLatitude(37.422408).setLongitude(-122.085609)));
      if (companyName != null) {
        jobQuery.setCompanyNames(Arrays.asList(companyName));
      }
    
      SearchJobsRequest searchJobsRequest =
          new SearchJobsRequest()
              .setJobQuery(jobQuery)
              .setRequestMetadata(requestMetadata)
              .setJobView("JOB_VIEW_FULL")
              .setRequirePreciseResultSize(true);
      SearchJobsResponse response =
          talentSolutionClient
              .projects()
              .jobs()
              .search(DEFAULT_PROJECT_ID, searchJobsRequest)
              .execute();
      Thread.sleep(1000);
      System.out.printf("Search jobs for commute results: %s\n", response);
    }

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def commute_search(client_service, company_name):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        start_location = {"latitude": 37.422408, "longitude": -122.085609}
        commute_preference = {
            "road_traffic": "TRAFFIC_FREE",
            "commute_method": "TRANSIT",
            "travel_duration": "1000s",
            "start_coordinates": start_location,
        }
        job_query = {"commute_filter": commute_preference}
        if company_name is not None:
            job_query.update({"company_names": [company_name]})
        request = {
            "job_query": job_query,
            "request_metadata": request_metadata,
            "job_view": "JOB_VIEW_FULL",
            "require_precise_result_size": True,
        }
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)
    
    

### Ruby

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id              = "Id of the project"
    # commute_method          = "The method of transportation for which to calculate the commute time"
    # travel_duration         = "The maximum travel time in seconds"
    # start_coordinates       = "The latitude and longitude of the location from which to calculate the commute time"
    
    require "google/apis/jobs_v3"
    
    jobs = Google::Apis::JobsV3
    talent_solution_client = jobs::CloudTalentSolutionService.new
    # @see https://developers.google.com/identity/protocols/application-default-credentials#callingruby
    talent_solution_client.authorization = Google::Auth.get_application_default(
      "https://www.googleapis.com/auth/jobs"
    )
    
    # Make sure to set the request_metadata the same as the associated search request
    request_metadata = jobs::RequestMetadata.new user_id:    "HashedUserId",
                                                 session_id: "HashedSessionId",
                                                 domain:     "www.google.com"
    # Set location filter
    commute_filter = jobs::CommuteFilter.new road_traffic:      "TRAFFIC_FREE",
                                             commute_method:    commute_method,
                                             travel_duration:   travel_duration,
                                             start_coordinates: start_coordinates
    # Perform a search for analyst  related jobs
    search_jobs_request =
      jobs::SearchJobsRequest.new request_metadata:            request_metadata,
                                  job_query:                   (jobs::JobQuery.new commute_filter: commute_filter),
                                  job_view:                    "JOB_VIEW_FULL",
                                  require_precise_result_size: true
    search_jobs_response = talent_solution_client.search_jobs project_id, search_jobs_request
    puts search_jobs_response.to_json
    search_jobs_response

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
