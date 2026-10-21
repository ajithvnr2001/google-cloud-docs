---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-searching/
title: Quickstart: Search \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:11.875815+00:00
---

# Quickstart: Search  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-searching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Quickstart: Search Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution allows you to search for any currently active Jobs that you have posted to the Cloud Talent Solution system. Once you are able to make [search requests](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/search), be sure to implement the Jobs analytics framework and implement [client events](https://docs.cloud.google.com/talent-solution/job-search/docs/events). This is core to the value of Cloud Talent Solution and directly impacts improved search results. Video tutorials and interactive codelabs are also [available](https://docs.cloud.google.com/talent-solution/job-search/docs/video).

## Get a histogram of the number of Jobs by a certain field

The search API can return a histogram of all relevant Jobs indexed in Cloud Talent Solution that match the filters of the search query. Now that you've gotten the search results, you can get a count of the jobs by different facets. Leverage the histogram API to get the count of jobs by certain facets.

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

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.talent.v4.[HistogramQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.HistogramQuery.html);
    import com.google.cloud.talent.v4.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html);
    import com.google.cloud.talent.v4.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html);
    import com.google.cloud.talent.v4.[RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.html);
    import com.google.cloud.talent.v4.[SearchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.html);
    import com.google.cloud.talent.v4.[SearchJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsResponse.html);
    import com.google.cloud.talent.v4.[TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html);
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
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html) jobServiceClient = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html).create()) {
          [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html) parent = [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html).of(projectId, tenantId);
    
          String domain = "http://www.jobUrl.com";
          String sessionId = "Hashed session identifier";
          String userId = "Hashed user identifier";
          [RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.html) requestMetadata =
              [RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.html).newBuilder()
                  .[setDomain](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.Builder.html#com_google_cloud_talent_v4_RequestMetadata_Builder_setDomain_java_lang_String_)(domain)
                  .[setSessionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.Builder.html#com_google_cloud_talent_v4_RequestMetadata_Builder_setSessionId_java_lang_String_)(sessionId)
                  .[setUserId](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.Builder.html#com_google_cloud_talent_v4_RequestMetadata_Builder_setUserId_java_lang_String_)(userId)
                  .build();
          [HistogramQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.HistogramQuery.html) histogramQueriesElement =
              [HistogramQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.HistogramQuery.html).newBuilder().setHistogramQuery(query).build();
          [SearchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.html) request =
              [SearchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html#com_google_cloud_talent_v4_TenantName_toString__)())
                  .[setRequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.Builder.html#com_google_cloud_talent_v4_SearchJobsRequest_Builder_setRequestMetadata_com_google_cloud_talent_v4_RequestMetadata_)(requestMetadata)
                  .[addHistogramQueries](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.Builder.html#com_google_cloud_talent_v4_SearchJobsRequest_Builder_addHistogramQueries_com_google_cloud_talent_v4_HistogramQuery_)(histogramQueriesElement)
                  .build();
    
          for ([SearchJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsResponse.html).[MatchingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsResponse.MatchingJob.html) responseItem :
              jobServiceClient.searchJobs(request).getMatchingJobsList()) {
            System.out.format("Job summary: %s%n", responseItem.getJobSummary());
            System.out.format("Job title snippet: %s%n", responseItem.getJobTitleSnippet());
            [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html) job = responseItem.getJob();
            System.out.format("Job name: %s%n", job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getName__)());
            System.out.format("Job title: %s%n", job.[getTitle](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getTitle__)());
          }
        }
      }
    }

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

In this case, we're getting the count of all jobs in the system, that are accepted by the filters specified, across the various facets - CATEGORY and CITY.

## Use the autocomplete API to get suggested job titles

The complete API suggests job titles or company titles that the job seeker might be interested in based on what they've already typed. Use this to autocomplete potential results in the search bar of your UI.

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"cloud.google.com/go/talent/apiv4beta1/talentpb"
    )
    
    // jobTitleAutoComplete suggests the job titles of the given
    // company identifier on query.
    func jobTitleAutocomplete(w io.Writer, projectID, query string) (*talentpb.CompleteQueryResponse, error) {
    	ctx := context.Background()
    
    	// Initialize a completionService client.
    	c, err := talent.NewCompletionClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("talent.NewCompletionClient: %w", err)
    	}
    	defer c.Close()
    
    	// Construct a completeQuery request.
    	req := &talentpb.CompleteQueryRequest{
    		Parent:        fmt.Sprintf("projects/%s", projectID),
    		Query:         query,
    		LanguageCodes: []string{"en-US"},
    		PageSize:      5, // Number of completion results returned.
    		Scope:         talentpb.[CompleteQueryRequest_PUBLIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_CompleteQueryRequest_COMPLETION_SCOPE_UNSPECIFIED_CompleteQueryRequest_TENANT_CompleteQueryRequest_PUBLIC),
    		Type:          talentpb.[CompleteQueryRequest_JOB_TITLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_CompleteQueryRequest_COMPLETION_TYPE_UNSPECIFIED_CompleteQueryRequest_JOB_TITLE_CompleteQueryRequest_COMPANY_NAME_CompleteQueryRequest_COMBINED),
    	}
    
    	resp, err := c.CompleteQuery(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CompleteQuery(%s): %w", query, err)
    	}
    
    	fmt.Fprintf(w, "Auto complete results:")
    	for _, c := range resp.GetCompletionResults() {
    		fmt.Fprintf(w, "\t%v\n", c.Suggestion)
    	}
    
    	return resp, nil
    }
    

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.talent.v4.[CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryRequest.html);
    import com.google.cloud.talent.v4.[CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryResponse.html);
    import com.google.cloud.talent.v4.[CompletionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionClient.html);
    import com.google.cloud.talent.v4.[TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html);
    import java.io.IOException;
    
    public class JobSearchAutoCompleteJobTitle {
    
      public static void completeQuery() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String query = "your-query-for-job-title";
        completeQuery(projectId, tenantId, query);
      }
    
      // Complete job title given partial text (autocomplete).
      public static void completeQuery(String projectId, String tenantId, String query)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([CompletionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionClient.html) completionClient = [CompletionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionClient.html).create()) {
          [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html) parent = [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html).of(projectId, tenantId);
          [CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryRequest.html) request =
              [CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryRequest.html).newBuilder()
                  .setTenant(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html#com_google_cloud_talent_v4_TenantName_toString__)())
                  .setQuery(query)
                  .setPageSize(5) // limit for number of results
                  .addLanguageCodes("en-US") // language code
                  .build();
          [CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryResponse.html) response = completionClient.completeQuery(request);
          for ([CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryResponse.html).[CompletionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryResponse.CompletionResult.html) result : response.[getCompletionResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryResponse.html#com_google_cloud_talent_v4_CompleteQueryResponse_getCompletionResultsList__)()) {
            System.out.format("Suggested title: %s%n", result.getSuggestion());
            // Suggestion type is JOB_TITLE or COMPANY_TITLE
            System.out.format("Suggestion type: %s%n", result.getType());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /**
     * Complete job title given partial text (autocomplete)
     *
     * @param projectId {string} Your Google Cloud Project ID
     * @param tenantId {string} Identifier of the TenantId
     */
    function sampleCompleteQuery(
      projectId,
      tenantId,
      query,
      numResults,
      languageCode
    ) {
      const client = new talent.[CompletionClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      // const query = '[partially typed job title]';
      // const numResults = 5;
      // const languageCode = 'en-US';
      const formattedParent = client.tenantPath(projectId, tenantId);
      const languageCodes = [languageCode];
      const request = {
        parent: formattedParent,
        query: query,
        pageSize: numResults,
        languageCodes: languageCodes,
      };
      client
        .completeQuery(request)
        .then(responses => {
          const response = responses[0];
          for (const result of response.completionResults) {
            console.log(`Suggested title: ${result.suggestion}`);
            // Suggestion type is JOB_TITLE or COMPANY_TITLE
            console.log(`Suggestion type: ${[result](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.longrunning.operation.html).type}`);
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
    

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import talent_v4beta1
    
    
    def complete_query(project_id, tenant_id, query):
        """Complete job title given partial text (autocomplete)"""
    
        client = talent_v4beta1.[CompletionClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # query = '[partially typed job title]'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(query, bytes):
            query = query.decode("utf-8")
    
        parent = f"projects/{project_id}/tenants/{tenant_id}"
    
        request = talent_v4beta1.[CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryRequest.html)(
            parent=parent,
            query=query,
            page_size=5,  # limit for number of results
            language_codes=["en-US"],  # language code
        )
        response = client.[complete_query](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient.html#google_cloud_talent_v4beta1_services_completion_CompletionClient_complete_query)(request=request)
        for result in response.completion_results:
            print(f"Suggested title: {result.suggestion}")
            # Suggestion type is JOB_TITLE or COMPANY_TITLE
            print(
                f"Suggestion type: {talent_v4beta1.[CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryRequest.html).[CompletionType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryRequest.CompletionType.html)(result.type_).name}"
            )
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
