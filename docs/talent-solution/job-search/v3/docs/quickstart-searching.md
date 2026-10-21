---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/quickstart-searching/
title: Quickstart: Search (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:42.609616+00:00
---

# Quickstart: Search (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/quickstart-searching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Quickstart: Search (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution allows you to search for jobs you have posted to our system in Google Cloud Talent Solution that are currently active. This tutorial provides a simple search call for the job created in the [Creating companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/create-company-job).

Once you are able to make search requests, be sure to implement the Jobs analytics framework (see [Improve pre-trained model](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/events). This is core to the value of Cloud Talent Solution and directly impacts improved search results.

## Search for the job posting

Search for the job created in the tutorial - [Creating companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/create-company-job#create_a_job_in_your_company). Cloud Talent Solution also uses the `RequestMetadata` to actively ensure that job seekers get a consistent user experience as they search through jobs. It's imperative to ensure that this field is set correctly. Reference the [`RequestMetadata`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/RequestMetadata) documentation.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Simple search jobs with keyword. */
    public static void basicSearcJobs(String companyName, String query)
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
    
      // Perform a search for analyst  related jobs
      JobQuery jobQuery = new JobQuery().setQuery(query);
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
      System.out.printf("Simple search jobs results: %s\n", searchJobsResponse);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def basic_keyword_search(client_service, company_name, keyword):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        job_query = {"query": keyword}
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
    
    
    // basicJobSearch searches for jobs with query.
    func basicJobSearch(w io.Writer, projectID, companyName, query string) (*talent.SearchJobsResponse, error) {
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
    		Query: query,
    	}
    	if companyName != "" {
    		jobQuery.CompanyNames = []string{companyName}
    	}
    
    	parent := "projects/" + projectID
    	req := &talent.SearchJobsRequest{
    		// Make sure to set the requestMetadata the same as the associated
    		// search request.
    		RequestMetadata: &talent.RequestMetadata{
    			// Make sure to hash your userID
    			UserId: "HashedUsrId",
    			// Make sure to hash the sessionID
    			SessionId: "HashedSessionId",
    			// Domain of the website where the search is conducted
    			Domain: "www.googlesample.com",
    		},
    		// Set the actual search term as defined in the jobQuery
    		JobQuery: jobQuery,
    		// Set the search mode to a regular search
    		SearchMode: "JOB_SEARCH",
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with query %q: %w", query, err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

## Get a histogram of the number of jobs by a certain field

The search API also returns a histogram of all relevant jobs indexed in Cloud Talent Solution that match the filters of the search query. Now that you've gotten the search results, you can get a count of the jobs by different facets. Leverage the histogram API to get the count of jobs by certain facets.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Histogram search */
    public static void histogramSearch(String companyName) throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash your userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
    
      HistogramFacets histogramFacets =
          new HistogramFacets()
              .setSimpleHistogramFacets(Arrays.asList("COMPANY_ID"))
              .setCustomAttributeHistogramFacets(
                  Arrays.asList(
                      new CustomAttributeHistogramRequest()
                          .setKey("someFieldName1")
                          .setStringValueHistogram(true)));
    
      // conducted.
      SearchJobsRequest searchJobsRequest =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setSearchMode("JOB_SEARCH")
              .setHistogramFacets(histogramFacets);
      if (companyName != null) {
        searchJobsRequest.setJobQuery(new JobQuery().setCompanyNames(Arrays.asList(companyName)));
      }
    
      SearchJobsResponse searchJobsResponse =
          talentSolutionClient
              .projects()
              .jobs()
              .search(DEFAULT_PROJECT_ID, searchJobsRequest)
              .execute();
      Thread.sleep(1000);
    
      System.out.printf("Histogram search results: %s\n", searchJobsResponse);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def histogram_search(client_service, company_name):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        custom_attribute_histogram_facet = {
            "key": "someFieldName1",
            "string_value_histogram": True,
        }
        histogram_facets = {
            "simple_histogram_facets": ["COMPANY_ID"],
            "custom_attribute_histogram_facets": [custom_attribute_histogram_facet],
        }
        request = {
            "search_mode": "JOB_SEARCH",
            "request_metadata": request_metadata,
            "histogram_facets": histogram_facets,
        }
        if company_name is not None:
            request.update({"job_query": {"company_names": [company_name]}})
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // histogramSearch searches for jobs with histogram facets.
    func histogramSearch(w io.Writer, projectID, companyName string) (*talent.SearchJobsResponse, error) {
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
    		HistogramFacets: &talent.HistogramFacets{
    			SimpleHistogramFacets: []string{"COMPANY_ID"},
    			CustomAttributeHistogramFacets: []*talent.CustomAttributeHistogramRequest{
    				{
    					Key:                  "someFieldString",
    					StringValueHistogram: true,
    				},
    			},
    		},
    		// Set the search mode to a regular search.
    		SearchMode:               "JOB_SEARCH",
    		RequirePreciseResultSize: true,
    	}
    	if companyName != "" {
    		req.JobQuery = &talent.JobQuery{
    			CompanyNames: []string{companyName},
    		}
    	}
    
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with Historgram Facets: %w", err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

In this case, we're getting the count of all jobs in the system, that are accepted by the filters specified, across the various facets - CATEGORY and CITY.

The complete API suggests job titles or company titles that the job seeker might be interested in based on what they've already typed. Use this to autocomplete potential results in the search bar of your UI.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Auto completes job titles within given companyName. */
    public static void jobTitleAutoComplete(String companyName, String query) throws IOException {
    
      Complete complete =
          talentSolutionClient
              .projects()
              .complete(DEFAULT_PROJECT_ID)
              .setQuery(query)
              .setLanguageCode("en-US")
              .setType("JOB_TITLE")
              .setPageSize(10);
      if (companyName != null) {
        complete.setCompanyName(companyName);
      }
    
      CompleteQueryResponse results = complete.execute();
    
      System.out.println(results);
    }
    

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def job_title_auto_complete(client_service, query, company_name):
        complete = client_service.projects().complete(
            name=name, query=query, languageCode="en-US", type="JOB_TITLE", pageSize=10
        )
        if company_name is not None:
            complete.companyName = company_name
    
        results = complete.execute()
        print(results)
    
    

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // jobTitleAutoComplete suggests the job titles of the given companyName based
    // on query.
    func jobTitleAutoComplete(w io.Writer, projectID, companyName, query string) (*talent.CompleteQueryResponse, error) {
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
    
    	parent := "projects/" + projectID
    	complete := service.Projects.Complete(parent).Query(query).LanguageCode("en-US").Type("JOB_TITLE").PageSize(10)
    	if companyName != "" {
    		complete.CompanyName(companyName)
    	}
    	resp, err := complete.Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to auto complete with query %s in company %s: %w", query, companyName, err)
    	}
    
    	fmt.Fprintf(w, "Auto complete results:")
    	for _, c := range resp.CompletionResults {
    		fmt.Fprintf(w, "\t%v", c.Suggestion)
    	}
    
    	return resp, nil
    }
    

## Set up the jobs analytics framework to tune Cloud Talent Solution with client events

You're now ready to optimize search results to your site (see [Improve search results using client events](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/improve-job-search-results-ml)). This is a critical step in improving results for job seekers by optimizing search results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
