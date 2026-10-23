---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-location/
title: Location-based search (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:44.650096+00:00
---

# Location-based search (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-location/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Location-based search (v3) Stay organized with collections  Save and categorize content based on your preferences. 

## Basic location search

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Basic location Search */
    public static void basicLocationSearch(String companyName, String location, double distance)
        throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash the userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
      LocationFilter locationFilter =
          new LocationFilter().setAddress(location).setDistanceInMiles(distance);
      JobQuery jobQuery = new JobQuery().setLocationFilters(Arrays.asList(locationFilter));
      if (companyName != null) {
        jobQuery.setCompanyNames(Arrays.asList(companyName));
      }
      SearchJobsRequest request =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setJobQuery(jobQuery)
              .setSearchMode("JOB_SEARCH");
      SearchJobsResponse response =
          talentSolutionClient.projects().jobs().search(DEFAULT_PROJECT_ID, request).execute();
      Thread.sleep(1000);
      System.out.printf("Basic location search results: %s", response);
    
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def basic_location_search(client_service, company_name, location, distance):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        location_filter = {"address": location, "distance_in_miles": distance}
        job_query = {"location_filters": [location_filter]}
        if company_name is not None:
            job_query.update({"company_names": [company_name]})
        request = {
            "job_query": job_query,
            "request_metadata": request_metadata,
            "search_mode": "JOB_SEARCH",
        }
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)
    
    

## Keyword with location search

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Keyword location Search */
    public static void keywordLocationSearch(
        String companyName, String location, double distance, String keyword)
        throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash the userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
      LocationFilter locationFilter =
          new LocationFilter().setAddress(location).setDistanceInMiles(distance);
      JobQuery jobQuery =
          new JobQuery().setQuery(keyword).setLocationFilters(Arrays.asList(locationFilter));
      if (companyName != null) {
        jobQuery.setCompanyNames(Arrays.asList(companyName));
      }
      SearchJobsRequest request =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setJobQuery(jobQuery)
              .setSearchMode("JOB_SEARCH");
      SearchJobsResponse response =
          talentSolutionClient.projects().jobs().search(DEFAULT_PROJECT_ID, request).execute();
      Thread.sleep(1000);
      System.out.printf("Keyword location search results: %s", response);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def keyword_location_search(client_service, company_name, location, distance, keyword):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        location_filter = {"address": location, "distance_in_miles": distance}
        job_query = {"location_filters": [location_filter], "query": keyword}
        if company_name is not None:
            job_query.update({"company_names": [company_name]})
        request = {
            "job_query": job_query,
            "request_metadata": request_metadata,
            "search_mode": "JOB_SEARCH",
        }
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)
    
    

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // keywordLocationSearch searches for jobs with given keyword and within the
    // distance of given location.
    func keywordLocationSearch(w io.Writer, projectID, companyName, location string, distance float64, keyword string) (*talent.SearchJobsResponse, error) {
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
    		LocationFilters: []*talent.LocationFilter{
    			{
    				Address:         location,
    				DistanceInMiles: distance,
    			},
    		},
    		Query: keyword,
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
    		return nil, fmt.Errorf("failed to search for jobs with keyword %q in location %v within %f miles: %w", keyword, location, distance, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

All fields are optional: 

  * `address` is the actual job location represented as a string. This can be a street address, or any level up to country. For example, "123 Main Street, Anytown, WA, USA" or simply "USA".

  * `distanceInMiles`: The distance from the `name` or `latLng` in miles in which to search. Default is 20. Maximum is 5000.

    * If the value of `name` is a street address, jobs within the set distanceInMiles of that singular point are returned.
    * If the value of `name` is a neighborhood or city, jobs within the set distanceInMiles of the neighborhood/city center are returned. To return all jobs within a neighborhood/city, set `distanceInMiles` to 0. If distanceInMiles is > 0, then the applied search radius is the geographical boundaries of the neighborhood/city plus the distanceInMiles set in the request. (Geographic boundaries are estimated using the Google Maps Geocoding API.)
    * If the value of `name` is a colloquial area, like "Bay Area" or "Silicon Valley", the applied search radius is the estimated geographical boundaries of the area plus the distanceInMiles set in the request.
    * If the value `name` is a state or country, the service returns jobs within the specified state or country, ignoring `distanceInMiles`.



## Basic location only with city level location and output

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** City location Search */
    public static void cityLocationSearch(String companyName, String location)
        throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash the userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
      LocationFilter locationFilter = new LocationFilter().setAddress(location);
      JobQuery jobQuery = new JobQuery().setLocationFilters(Arrays.asList(locationFilter));
      if (companyName != null) {
        jobQuery.setCompanyNames(Arrays.asList(companyName));
      }
      SearchJobsRequest request =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setJobQuery(jobQuery)
              .setSearchMode("JOB_SEARCH");
      SearchJobsResponse response =
          talentSolutionClient.projects().jobs().search(DEFAULT_PROJECT_ID, request).execute();
      Thread.sleep(1000);
      System.out.printf("City locations search results: %s", response);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def city_location_search(client_service, company_name, location):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        location_filter = {"address": location}
        job_query = {"location_filters": [location_filter]}
        if company_name is not None:
            job_query.update({"company_names": [company_name]})
        request = {
            "job_query": job_query,
            "request_metadata": request_metadata,
            "search_mode": "JOB_SEARCH",
        }
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)
    
    

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // cityLocationSearch searches for jobs in the same city of given location.
    func cityLocationSearch(w io.Writer, projectID, companyName, location string) (*talent.SearchJobsResponse, error) {
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
    		LocationFilters: []*talent.LocationFilter{
    			{
    				Address: location,
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
    		SearchMode: "JOB_SEARCH",
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with city location %s: %w", location, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

## Multiple locations

When multiple locations are passed to the search query, along with multiple radii, the maximum radius is taken into account and applied to all locations. There is a limit of 5 locations per job.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Multiple locations Search */
    public static void multiLocationsSearch(
        String companyName, String location1, double distance1, String location2)
        throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash the userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
      JobQuery jobQuery =
          new JobQuery()
              .setLocationFilters(
                  Arrays.asList(
                      new LocationFilter().setAddress(location1).setDistanceInMiles(distance1),
                      new LocationFilter().setAddress(location2)));
      if (companyName != null) {
        jobQuery.setCompanyNames(Arrays.asList(companyName));
      }
      SearchJobsRequest request =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setJobQuery(jobQuery)
              .setSearchMode("JOB_SEARCH");
      SearchJobsResponse response =
          talentSolutionClient.projects().jobs().search(DEFAULT_PROJECT_ID, request).execute();
      Thread.sleep(1000);
      System.out.printf("Multiple locations search results: %s", response);
    
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def multi_locations_search(
        client_service, company_name, location1, distance1, location2
    ):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        location_filter1 = {"address": location1, "distance_in_miles": distance1}
        location_filter2 = {"address": location2}
        job_query = {"location_filters": [location_filter1, location_filter2]}
        if company_name is not None:
            job_query.update({"company_names": [company_name]})
        request = {
            "job_query": job_query,
            "request_metadata": request_metadata,
            "search_mode": "JOB_SEARCH",
        }
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)
    
    

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // multiLocationsSearch searches for jobs that fall in the distance of any given
    // locations.
    func multiLocationsSearch(w io.Writer, projectID, companyName, location, location2 string, distance float64) (*talent.SearchJobsResponse, error) {
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
    		LocationFilters: []*talent.LocationFilter{
    			{
    				Address:         location,
    				DistanceInMiles: distance,
    			},
    			{
    				Address:         location2,
    				DistanceInMiles: distance,
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
    		SearchMode: "JOB_SEARCH",
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Failed to search for jobs with multi locations %s and %s within %f miles, Err: %w", location, location2, distance, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

## Set enableBroadening flag

The enableBroadening flag allows you to relax the restrictions on location and job categories in order to increase the number of results that are returned.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Broadening location Search */
    public static void broadeningLocationsSearch(String companyName, String location)
        throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash the userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
      JobQuery jobQuery =
          new JobQuery().setLocationFilters(Arrays.asList(new LocationFilter().setAddress(location)));
      if (companyName != null) {
        jobQuery.setCompanyNames(Arrays.asList(companyName));
      }
      SearchJobsRequest request =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setJobQuery(jobQuery)
              .setEnableBroadening(true)
              .setSearchMode("JOB_SEARCH");
      SearchJobsResponse response =
          talentSolutionClient.projects().jobs().search(DEFAULT_PROJECT_ID, request).execute();
      Thread.sleep(1000);
      System.out.printf("Broadening locations search results: %s", response);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def broadening_location_search(client_service, company_name, location):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        location_filter = {"address": location}
        job_query = {"location_filters": [location_filter]}
        if company_name is not None:
            job_query.update({"company_names": [company_name]})
        request = {
            "job_query": job_query,
            "request_metadata": request_metadata,
            "search_mode": "JOB_SEARCH",
            "enable_broadening": True,
        }
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)
    
    

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // broadeningLocationSearch searches for jobs with a broadening area of given
    // location.
    func broadeningLocationSearch(w io.Writer, projectID, companyName, location string) (*talent.SearchJobsResponse, error) {
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
    		LocationFilters: []*talent.LocationFilter{
    			{
    				Address: location,
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
    		SearchMode:       "JOB_SEARCH",
    		EnableBroadening: true,
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with broadening location %v: %w", location, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
