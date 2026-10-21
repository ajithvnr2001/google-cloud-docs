---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/histogram/
title: Histogram (v4beta1) \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:27.157723+00:00
---

# Histogram (v4beta1)  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/histogram/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)



Send feedback 

#  Histogram (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution allows you to get a histogram representation of the number of jobs associated with a given search. A histogram search returns a count of all jobs that match a particular query, broken down by the requested [`SearchMode`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/SearchMode). For example, a histogram search could return the number of jobs per employment type (full-time, part-time, and so on) that exist in Mountain View, CA.

Histograms are generally run in parallel with a search call, using the same [`JobQuery`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/JobQuery) and the same [`requestMetadata`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/RequestMetadata).

The histogram is defined by the `histogramQuery` field, a single string expression. For details on the functions available for histogram queries, see the `histogramQuery` [documentation](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/HistogramQuery).

## Retrieving a histogram

The following code sample returns histogram results:

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"google.golang.org/api/iterator"
    	talentpb "google.golang.org/genproto/googleapis/cloud/talent/v4beta1"
    )
    
    // histogramSearch searches for jobs with histogram queries.
    func histogramSearch(w io.Writer, projectID, companyID string) error {
    	ctx := context.Background()
    
    	// Initialize a jobService client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		fmt.Printf("talent.NewJobClient: %v\n", err)
    		return err
    	}
    
    	// Construct a searchJobs request.
    	req := &talentpb.[SearchJobsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_SearchJobsRequest){
    		Parent: fmt.Sprintf("projects/%s", projectID),
    		// Make sure to set the RequestMetadata the same as the associated
    		// search request.
    		RequestMetadata: &talentpb.[RequestMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_RequestMetadata){
    			// Make sure to hash your userId.
    			UserId: "HashedUsrID",
    			// Make sure to hash the sessionId.
    			SessionId: "HashedSessionID",
    			// Domain of the website where the search is conducted.
    			Domain: "www.googlesample.com",
    		},
    		HistogramQueries: []*talentpb.[HistogramQuery](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_HistogramQuery){
    			{
    				// More info on histogram facets, constants, and built-in functions:
    				// https://godoc.org/google.golang.org/genproto/googleapis/cloud/talent/v4beta1#SearchJobsRequest
    				HistogramQuery: "count(base_compensation, [bucket(12, 20)])",
    			},
    		},
    	}
    	if companyID != "" {
    		req.[JobQuery](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_JobQuery) = &talentpb.[JobQuery](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_JobQuery){
    			CompanyNames: []string{fmt.Sprintf("projects/%s/companies/%s", projectID, companyID)},
    		}
    	}
    
    	it := c.SearchJobs(ctx, req)
    
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			return nil
    		}
    		if err != nil {
    			fmt.Printf("it.Next: %v\n", err)
    			return err
    		}
    		fmt.Fprintf(w, "Job: %q\n", resp.[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_Job).GetName())
    	}
    }
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.HistogramQuery;
    import com.google.cloud.talent.v4beta1.Job;
    import com.google.cloud.talent.v4beta1.JobServiceClient;
    import com.google.cloud.talent.v4beta1.RequestMetadata;
    import com.google.cloud.talent.v4beta1.SearchJobsRequest;
    import com.google.cloud.talent.v4beta1.SearchJobsResponse;
    import com.google.cloud.talent.v4beta1.TenantName;
    import java.io.IOException;
    
    public class HistogramSearchJobs {
    
      public static void searchJobs() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String query = "count(base_compensation, [bucket(12, 20)])";
        searchJobs(projectId, tenantId, query);
      }
    
      // Search Jobs with histogram queries.
      public static void searchJobs(String projectId, String tenantId, String query)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
          TenantName parent = TenantName.of(projectId, tenantId);
    
          String domain = "http://www.jobUrl.com";
          String sessionId = "Hashed session identifier";
          String userId = "Hashed user identifier";
          RequestMetadata requestMetadata =
              RequestMetadata.newBuilder()
                  .setDomain(domain)
                  .setSessionId(sessionId)
                  .setUserId(userId)
                  .build();
          HistogramQuery histogramQueriesElement =
              HistogramQuery.newBuilder().setHistogramQuery(query).build();
          SearchJobsRequest request =
              SearchJobsRequest.newBuilder()
                  .setParent(parent.toString())
                  .setRequestMetadata(requestMetadata)
                  .addHistogramQueries(histogramQueriesElement)
                  .build();
    
          for (SearchJobsResponse.MatchingJob responseItem :
              jobServiceClient.searchJobs(request).iterateAll()) {
            System.out.format("Job summary: %s%n", responseItem.getJobSummary());
            System.out.format("Job title snippet: %s%n", responseItem.getJobTitleSnippet());
            Job job = responseItem.getJob();
            System.out.format("Job name: %s%n", job.getName());
            System.out.format("Job title: %s%n", job.getTitle());
          }
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    from google.cloud import talent
    
    
    def search_jobs(project_id, tenant_id, query):
        """
        Search Jobs with histogram queries
    
        Args:
          query Histogram query
          More info on histogram facets, constants, and built-in functions:
          https://godoc.org/google.golang.org/genproto/googleapis/cloud/talent/v4beta1#SearchJobsRequest
        """
    
        client = talent.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # query = 'count(base_compensation, [bucket(12, 20)])'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(query, bytes):
            query = query.decode("utf-8")
        parent = f"projects/{project_id}/tenants/{tenant_id}"
        domain = "www.example.com"
        session_id = "Hashed session identifier"
        user_id = "Hashed user identifier"
        request_metadata = {"domain": domain, "session_id": session_id, "user_id": user_id}
        histogram_queries_element = {"histogram_query": query}
        histogram_queries = [histogram_queries_element]
    
        # Iterate over all results
        results = []
        request = talent.[SearchJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.html)(
            parent=parent,
            request_metadata=request_metadata,
            histogram_queries=histogram_queries,
        )
        for response_item in client.[search_jobs](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_search_jobs)(request=request).matching_jobs:
            print("Job summary: {response_item.job_summary}")
            print("Job title snippet: {response_item.job_title_snippet}")
            job = response_item.job
            results.append(job)
            print("Job name: {job.name}")
            print("Job title: {job.title}")
        return results
    
    

## Relevance thresholding

Histogram requests do not use relevance thresholding. To ensure that the counts are consistent between a histogram search and an identical job search, `disableKeywordMatch` in the job search must be `false`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
