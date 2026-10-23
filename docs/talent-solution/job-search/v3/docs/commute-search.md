---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/commute-search/
title: Implementing Commute Search in your UI (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:57.831796+00:00
---

# Implementing Commute Search in your UI (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/commute-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Implementing Commute Search in your UI (v3) Stay organized with collections  Save and categorize content based on your preferences. 

You can integrate Commute Search into your UI to allow job seekers to search for jobs within a geographic area set by commute time. Commute Search estimates commute time based on a user's selected transit mode and the time of day they plan to travel.

## Implementing Commute Search

  1. Before you can implement Commute Search, Cloud Talent Solution must be hooked up to your UI. Follow the [quickstart](https://cloud.google.com/talent-solution/job-search/v3/docs/before-you-begin) guides to set up Cloud Talent Solution.

  2. Commute Search uses the address data that you uploaded with your jobs during CTS implementation to calculate commute time. To enable this feature on your existing CTS UI, send a `jobs.search` request and include a `CommuteFilter` object in the `JobQuery.commuteFilter` field. `commuteMethod`, `travelDuration`, and `startCoordinates` are required fields.

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

## Recommendations for your UI

     1. Cloud Talent Solution doesn't allow searching by both distance (using the CTS location filter) AND commute time. To allow job seekers to access both options, use a 2-tab approach or similar.

     2. Modify the front-end of your application so that when a job seeker requests a commute search, the back-end populates the relevant information in the [commute filter](https://cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/JobQuery#FIELDS.commute_filter) and calls the API as it would in a regular search request.

     3. Include these newly added items in your UI:

        * An option to choose whether this is a distance search or commute search. For example, your Search UI could look like the sample below:

![](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/search-bar.png)

        * A drop-down menu of commute method options.

        * An option to adjust traffic conditions.

        * The total travel time (the maximum supported travel time is 60 minutes).

        * Commute start time.

     4. The commute time information returned from the API is then used to display information to the job seeker. Only relevant jobs located within the designated commute time area are returned in the results list. See the Job search [Best Practices](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/best-practices) documentation for a discussion of ways to adjust the order and number of jobs returned within this area.

## Generating a map with commute information (Recommended)

You can leverage the Maps API to generate a map based on the commute time information returned from the CTS API and embed it into the results returned to a job seeker. The Maps API suite has several options for displaying the map. Some Maps API options are more effective than others. For example, the [Google Maps JavaScript Heatmap visualization](https://developers.google.com/maps/documentation/javascript/earthquakes#heatmaps) paired with [marker clustering](https://developers.google.com/maps/documentation/javascript/marker-clustering) is a great way to visualize the relevant jobs returned to a job seeker inside the area determined by their set commute preferences. Conversely, [Directions Mode](https://developers.google.com/maps/documentation/javascript/examples/directions-travel-modes) does not show all jobs returned in a search request and is not a recommended option.

**Note:** The Maps API has a number of different pricing structures. These prices are NOT covered under the usage of Cloud Talent Solution. Only the use of Cloud Talent Solution APIs to request the jobs within the specified commute times are covered as a part of Cloud Talent Solution pricing.

For more information on implementing a commute-based search, see the [Commute Search how-to guide](https://cloud.google.com/talent-solution/job-search/v3/docs/search-commute).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
