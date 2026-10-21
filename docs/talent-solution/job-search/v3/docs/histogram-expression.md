---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/histogram-expression/
title: Histogram (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:41.155019+00:00
---

# Histogram (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/histogram-expression/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Histogram (v3) Stay organized with collections  Save and categorize content based on your preferences. 

You can get a histogram representation of the number of jobs associated with a given search. A search request, with histogram facets set, returns the search results and a count of all the jobs that match a particular query, broken down by the requested [searchType](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/SearchType).

For example, a histogram search could return the number of jobs per employment type (full-time, part-time, and so on) from a customer's set of jobs.

The Cloud Talent Solution Beta release (v3p1beta1) allows you to define histograms in a less structured, more flexible, and more intuitive way. The histogram representations do not change.

## Benefits

The new structure of the histogram queries offers developers more intuitive ways of defining histogram requests, while also providing more clarity into the definition of buckets, ranges, etc.

## Usage

The new histogram part of the search query replaces the old structured fields for defining the histogram.

**Note:** Having both versions in the same search request causes an error with HTTP response code 400.

## Code Samples

The following code sample returns histogram results.

The `histogramQuery` field is now a single string field that is an expression that defines the histogram. For details on the functions available for histogram queries, see [`HistogramQuery`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/HistogramQuery).

### Java

For more on installing and creating a Cloud Talent Solution client, refer to [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 

### Java

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, refer to [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 

### Python

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
