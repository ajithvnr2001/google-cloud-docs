---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-commute/
title: Commute search (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:35.159315+00:00
---

# Commute search (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-commute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Commute search (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Job search requests can include a commute time filter that restricts returned jobs to those within a specified travel time from a start point. Results include the estimated commute time in seconds for matched jobs.

## Specific commute time search

To return jobs within a specific commute time, send a [`jobs.search`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs/search) request and include a `CommuteFilter` object in the `JobQuery.commuteFilter` field. Cloud Talent Solution uses the job's [address](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs#Job.FIELDS.addresses) to calculate the commute time to that job. When a detailed address is not provided Cloud Talent Solution attempts to infer the actual street address of the job.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
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
    
    

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
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
    

### Ruby

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
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

## Required fields

  * `commuteMethod`: The method of transportation for which to calculate the commute time. Options are `DRIVING` and `TRANSIT`. All versions since V3p1beta1 will also include `WALKING` and `CYCLING` transit modes. **Walking and cycling routes may not reflect real-world conditions such as construction or include clear walking or cycling paths. These responses will include`warnings` in the returned result which you must display to your users.**

  * `travelDuration`: The maximum travel time in seconds. The maximum allowed value is `3600s` (one hour). Format is `123s`.

  * `startCoordinates`: The latitude and longitude of the location from which to calculate the commute time. Accepts a [`LatLng`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/Shared.Types/LatLng) object.




## Optional fields

  * `allowImpreciseAddresses`: "Precise" addresses are defined as either street level addresses or GPS coordinates. If `allowImpreciseAddresses` is set to `true`, jobs with "imprecise" addresses (city, state, or country only) may also be returned. For city level and coarser level addresses, text matching is used. If this field is set to `false` or is not specified, only jobs that include precise addresses are returned by commute search.

**Note:** If `allowImpreciseAddresses` is set to `true`, Commute Search is not able to calculate accurate commute times to jobs with city level and coarser address information. Jobs with imprecise addresses return a `travelDuration` time of 0 regardless of the distance from the job seeker.

  * `roadTraffic`: Specifies the traffic density to use when calculating commute time. Options are `TRAFFIC_FREE` or `BUSY_HOUR`. Must not be present if `departureHourLocal` is specified.

  * `departureTime`: The departure hour to use to calculate traffic impact. Accepts an integer between 0 and 23, representing the hour in the timezone of the `startLocation`. Must not be present if `roadTraffic` is specified.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
