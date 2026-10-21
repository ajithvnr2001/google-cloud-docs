---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-filters/
title: Search filters (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:58.613445+00:00
---

# Search filters (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Search filters (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Optionally, a job search can include one or more `JobQuery` filters that restrict the job search following different criteria, such as location, companies, compensation, and more. The `JobQuery` fields are marked in the [`JobQuery`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/JobQuery) reference.

## Location

Location search allows you to specify a geographic radius or area within which to search.

See [Location based search](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-location) for more information.

## Job Category

Return jobs belonging to a specific category as identified by Cloud Talent Solution. Categories are predefined and include, for example, `ACCOUNTING_AND_FINANCE` and `EDUCATION`. All categories are determined by the Cloud Talent Solution models and are recommended for use in terms of category-based faceting. For a full list, see the [`JobCategory`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs#jobcategory) reference page.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Search on category filter. */
    public static void categoryFilterSearch(String companyName, List<String> categories)
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
    
      JobQuery jobQuery = new JobQuery().setJobCategories(categories);
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
    
      System.out.printf("Category search jobs results: %s\n", searchJobsResponse);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def category_search(client_service, company_name, categories):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        job_query = {"job_categories": categories}
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

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // categoryFilterSearch searches for jobs on category filter.
    func categoryFilterSearch(w io.Writer, projectID, companyName string, categories []string) (*talent.SearchJobsResponse, error) {
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
    		JobCategories: categories,
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
    		return nil, fmt.Errorf("failed to search for jobs with categories %v: %w", categories, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

## Employment type

Return jobs belonging to one or more employment type definitions, such as `FULL_TIME` or `VOLUNTEER`. For a full list, see the [EmploymentType](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs#employmenttype) reference page.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Search on employment types. */
    public static void employmentTypesSearch(String companyName, List<String> employmentTypes)
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
    
      JobQuery jobQuery = new JobQuery().setEmploymentTypes(employmentTypes);
      if (companyName != null) {
        jobQuery.setCompanyNames(Arrays.asList(companyName));
      }
    
      SearchJobsRequest searchJobsRequest =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setJobQuery(jobQuery) // Set the actual search term as defined in the jobQurey
              .setSearchMode("JOB_SEARCH"); // Set the search mode to a regular searchch
    
      SearchJobsResponse searchJobsResponse =
          talentSolutionClient
              .projects()
              .jobs()
              .search(DEFAULT_PROJECT_ID, searchJobsRequest)
              .execute();
      Thread.sleep(1000);
    
      System.out.printf("Employee type search jobs results: %s\n", searchJobsResponse);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def employment_types_search(client_service, company_name, employment_types):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        job_query = {"employment_types": employment_types}
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

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // employmentTypesSearch searches for jobs on employment types.
    func employmentTypesSearch(w io.Writer, projectID, companyName string, employmentTypes []string) (*talent.SearchJobsResponse, error) {
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
    		EmploymentTypes: employmentTypes,
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
    		return nil, fmt.Errorf("failed to search for jobs with employment types %v: %w", employmentTypes, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

## Date range

Restricts the search to jobs published within the specified date range. Accepted values are listed in the [`publishTimeRange`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/JobQuery#publishTimeRange) reference page.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
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

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
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
    

## Language code

Returns jobs that match the specified language code, as determined by the jobs' `languageCode` field. This field specifies the language of the job posting, and does not refer to language fluency requirements.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Search on language codes. */
    public static void languageCodeSearch(String companyName, List<String> languageCodes)
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
    
      JobQuery jobQuery = new JobQuery().setLanguageCodes(languageCodes);
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
    
      System.out.printf("Search results on jobs with a language code: %s\n", searchJobsResponse);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def language_code_search(client_service, company_name, language_codes):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        job_query = {"language_codes": language_codes}
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

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // languageCodeSearch searches for jobs on language code.
    func languageCodeSearch(w io.Writer, projectID, companyName string, languageCodes []string) (*talent.SearchJobsResponse, error) {
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
    		LanguageCodes: languageCodes,
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
    		return nil, fmt.Errorf("failed to search for jobs with languange codes %v: %w", languageCodes, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

## Company Display Name

Returns jobs from companies whose `displayName` matches the provided text string. Note that `displayName` is the human-readable name of the company (such as "Google") as opposed to `name` which is a generated ID (such as "companies/80df2034-176e-44a8-b763-b5370f2463a5"). See [Company displayName](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.companies#Company.FIELDS.display_name) for name search.

You can increase accuracy by using [autocomplete](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/autocomplete) suggestions.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Search on company display name. */
    public static void companyDisplayNameSearch(String companyName, List<String> companyDisplayNames)
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
    
      JobQuery jobQuery = new JobQuery().setCompanyDisplayNames(companyDisplayNames);
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
    
      System.out.printf("Search results by display name of company: %s\n", searchJobsResponse);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def company_display_name_search(client_service, company_name, company_display_names):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        job_query = {"company_display_names": company_display_names}
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

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // companyDisplayNameSearch searches for job on company display names.
    func companyDisplayNameSearch(w io.Writer, projectID, companyName string, companyDisplayNames []string) (*talent.SearchJobsResponse, error) {
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
    		CompanyDisplayNames: companyDisplayNames,
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
    		return nil, fmt.Errorf("failed to search for jobs with company display names %v: %w", companyDisplayNames, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

## Commute

Commute search allows you to specify a maximum drive or transit time around which to return jobs. You can specify the time of day for which to use traffic data.

Learn more on the [Commute Search](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-commute) reference page.

## Compensation

Filters search results based on compensation amounts. The `compensationFilter` looks like:
    
    
    "compensationFilter": {
      "type": enum(FilterType),
      "units": [
        enum(CompensationUnit)
      ],
      "range": {
        object(CompensationRange)
      },
      "includeJobWithUnspecifiedCompensationRange": boolean,
    }
    

Where:

  * `type` is required and specifies the fields to search against. For example, to search for jobs that pay any amount hourly, specify `UNIT_ONLY` here and `HOURLY` in the `compensationUnits` list.

  * `units` is a list of pay frequency enums, such as `HOURLY` and `MONTHLY`. See the [CompensationUnit](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs#compensationunit) reference page for a full list.

  * `range` specifies the minimum and maximum values that should be returned, in the specified `currencyCode` which is a [3-letter currency code](https://www.iso.org/iso-4217-currency-codes.html) and at the specified pay frequency. Leave `currencyCode` empty to return all jobs regardless of currency. For example, use this filter to look for jobs that pay between 10.50 and 15 USD per hour.




### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Search on compensation. */
    public static void compensationSearch(String companyName)
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
    
      // Search jobs that pay between 10.50 and 15 USD per hour
      JobQuery jobQuery =
          new JobQuery()
              .setCompensationFilter(
                  new CompensationFilter()
                      .setType("UNIT_AND_AMOUNT")
                      .setUnits(Arrays.asList("HOURLY"))
                      .setRange(
                          new CompensationRange()
                              .setMaxCompensation(new Money().setCurrencyCode("USD").setUnits(15L))
                              .setMinCompensation(
                                  new Money()
                                      .setCurrencyCode("USD")
                                      .setUnits(10L)
                                      .setNanos(500000000))));
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
    
      System.out.printf("Search results by compensation: %s\n", searchJobsResponse);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def compensation_search(client_service, company_name):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        compensation_range = {
            "max_compensation": {"currency_code": "USD", "units": 15},
            "min_compensation": {"currency_code": "USD", "units": 10, "nanos": 500000000},
        }
        compensation_filter = {
            "type": "UNIT_AND_AMOUNT",
            "units": ["HOURLY"],
            "range": compensation_range,
        }
        job_query = {"compensation_filter": compensation_filter}
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

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // compensationSearch searches for job on compensation.
    func compensationSearch(w io.Writer, projectID, companyName string) (*talent.SearchJobsResponse, error) {
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
    		CompensationFilter: &talent.CompensationFilter{
    			Type:  "UNIT_AND_AMOUNT",
    			Units: []string{"HOURLY"},
    			Range: &talent.CompensationRange{
    				MaxCompensation: &talent.Money{
    					Units:        15,
    					CurrencyCode: "USD",
    				},
    				MinCompensation: &talent.Money{
    					Units:        10,
    					CurrencyCode: "USD",
    					Nanos:        500000000,
    				},
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
    		return nil, fmt.Errorf("failed to search for jobs with compensation: %w", err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

Note: The `nanos` field expects nano units, which are 10^-9. There are 1,000,000,000 nanos in 1 unit. 

  * `includeJobWithUnspecifiedCompensationRange` specifies whether to include jobs without compensation information. Default is false, and does not return jobs without compensation values.



## Query language code

`query_language_code` specifies the language of the query string in BCP-47 format, for example "en-US". If left blank, the default is US English. This field is not related to `languageCode`, which specifies the language of returned job listings. See the [JobQuery documentation](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rpc/google.cloud.talent.v3#jobquery) for details. Sample code:
    
    
       "jobQuery":
       {"query":"general", "query_language_code":"fr-FR"}}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
