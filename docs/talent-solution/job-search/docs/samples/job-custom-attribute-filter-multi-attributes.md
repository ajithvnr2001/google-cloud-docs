---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-custom-attribute-filter-multi-attributes/
title: Custom Attribute Filter Multiple Attributes \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:18.364546+00:00
---

# Custom Attribute Filter Multiple Attributes  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-custom-attribute-filter-multi-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Custom Attribute Filter Multiple Attributes Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to use custom attribute filters with multiple attributes to search for jobs.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Custom attributes (v3)](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/custom-attributes)



## Code sample

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // filterOnLongValueCustomAttribute searches for jobs on multiple custom
    // atrributes.
    func filterOnMultiCustomAttributes(w io.Writer, projectID string) (*talent.SearchJobsResponse, error) {
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
    		JobQuery: &talent.JobQuery{
    			CustomAttributeFilter: "(someFieldString = \"someStrVal\") AND (someFieldLong < 1000)",
    		},
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
    		JobView: "JOB_VIEW_FULL",
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with multiple custom attributes: %w", err)
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
    
    
    /** CustomAttributeFilter on multiple CustomAttributes */
    public static void filtersOnMultiCustomAttributes() throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash your userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
    
      String customAttributeFilter =
          "(someFieldName1 = \"value1\") "
              + "AND ((255 <= someFieldName2) OR (someFieldName2 <= 213))";
      JobQuery jobQuery = new JobQuery().setCustomAttributeFilter(customAttributeFilter);
    
      SearchJobsRequest searchJobsRequest =
          new SearchJobsRequest()
              .setJobQuery(jobQuery)
              .setRequestMetadata(requestMetadata)
              .setJobView("JOB_VIEW_FULL");
      SearchJobsResponse response =
          talentSolutionClient
              .projects()
              .jobs()
              .search(DEFAULT_PROJECT_ID, searchJobsRequest)
              .execute();
      Thread.sleep(1000);
      System.out.printf("Custom search job results (multiple value): %s\n", response);
    }

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def custom_attribute_filter_multi_attributes(client_service):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
    
        custom_attribute_filter = (
            '(someFieldName1 = "value1") AND ((255 <= someFieldName2) OR '
            "(someFieldName2 <= 213))"
        )
        job_query = {"custom_attribute_filter": custom_attribute_filter}
        request = {
            "request_metadata": request_metadata,
            "job_query": job_query,
            "job_view": "JOB_VIEW_FULL",
        }
    
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
