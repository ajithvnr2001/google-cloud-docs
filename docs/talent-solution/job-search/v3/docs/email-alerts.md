---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/email-alerts/
title: Email alerts (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:32.897086+00:00
---

# Email alerts (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/email-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Email alerts (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution also offers a search API, [`SearchJobsForAlert`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rpc/google.cloud.talent.v3#google.cloud.talent.v3.JobService.SearchJobsForAlert), that's tuned to the needs of "passive job seekers." These are individuals not necessarily actively looking for a job, but might be inclined to apply for one if the right circumstances arise. For example, a customer can leverage Cloud Talent Solution to populate the contents of an email campaign designed to offer periodic updates of jobs individuals might be interested in. The results of `SearchJobsForAlert` may be different to those from `searchJobs` and are intended for use in job alert emails and other campaigns that are targeted towards passive job seekers. Use the date posted filter when calling `SearchJobsForAlert` to restrict the set of jobs being searched to those posted since the last alert was generated. For additional information on using this feature, see the email alerts [implementation guide](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/email).

Email alert searches are made in the same way as a regular search:

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Search jobs for alert. */
    public static void searchForAlerts(String companyName) throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash your userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
    
      SearchJobsRequest request =
          new SearchJobsRequest()
              .setRequestMetadata(requestMetadata)
              .setSearchMode("JOB_SEARCH"); // Set the search mode to a regular search
      if (companyName != null) {
        request.setJobQuery(new JobQuery().setCompanyNames(Arrays.asList(companyName)));
      }
    
      SearchJobsResponse response =
          talentSolutionClient
              .projects()
              .jobs()
              .searchForAlert(DEFAULT_PROJECT_ID, request)
              .execute();
      Thread.sleep(1000);
      System.out.printf("Search jobs for alert results: %s\n", response);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def search_for_alerts(client_service, company_name):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
        request = {
            "search_mode": "JOB_SEARCH",
            "request_metadata": request_metadata,
        }
        if company_name is not None:
            request.update({"job_query": {"company_names": [company_name]}})
        response = (
            client_service.projects()
            .jobs()
            .searchForAlert(parent=parent, body=request)
            .execute()
        )
        print(response)

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // searchForAlerts searches for jobs with email alert set which could receive
    // updates later if search result updates.
    func searchForAlerts(w io.Writer, projectID, companyName string) (*talent.SearchJobsResponse, error) {
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
    		// Set the search mode to a regular search.
    		SearchMode: "JOB_SEARCH",
    	}
    	if companyName != "" {
    		req.JobQuery = &talent.JobQuery{
    			CompanyNames: []string{companyName},
    		}
    	}
    
    	resp, err := service.Projects.Jobs.SearchForAlert(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with alerts: %w", err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

For information about searching, see [Search Basics](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
