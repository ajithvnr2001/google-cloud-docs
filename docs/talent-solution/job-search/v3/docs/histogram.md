---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/histogram/
title: Histogram (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:37.690575+00:00
---

# Histogram (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/histogram/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Histogram (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution allows you to get a histogram representation of the number of jobs associated to a given search. A histogram search returns a count of all jobs that match a particular query, broken down by the requested [`searchType`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/SearchType). For example, a histogram search could return the number of jobs per employment type (full-time, part-time, etc) that exist in Mountain View, CA. To define the dimensions and parameters of the histogram, follow this guide.

Histograms are generally run in parallel with a search call, using the same [`JobQuery`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/JobQuery) and the same [`requestMetadata`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/RequestMetadata).

## Request

The histogram can be obtained from the underlying `search` API. This is achieved by setting the `histogramFacets` on the `search` API and defining the filters of the request. **Note that the histogram observes all the filters as defined in the search query**. The following example illustrates the mechanism of retrieving a histogram,

## Required fields

  * `searchTypes` is a list of categories for which to return counts. For example, specify `EMPLOYMENT_TYPE` to return a count of employment types, such as full-time or part-time. See [`SearchType`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/SearchType) for a detailed list of enums.



## Optional fields

  * `jobQuery` is the job query to perform in this search. See [Search Filters](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-filters) for more details. In this example, no query is applied.

  * `requestMetadata` contains information about the user initiating the search. See the [`RequestMetadata`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search#requestmetadata) section of the job search page for more information.

  * `enableBroadening` loosens the restrictions on location and job category of the search request, in order to return more results. For example, if a request specified jobs within a 20 mile radius of a location, setting this flag to `true` may return jobs from outside of that radius. The following example does not include broadened results.




## Examples

The following example returns the list of job counts across the `COMPANY_ID` and the customAttribute `someFieldName1`:

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
    

## Relevance thresholding

Histogram requests do not use relevance thresholding. To ensure that the counts are consistent between a histogram search and an identical job search, `disableKeywordMatch` in the job search must be `false`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
