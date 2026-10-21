---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-autocomplete-job-title/
title: Automatically complete job title (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:12.245873+00:00
---

# Automatically complete job title (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-autocomplete-job-title/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Automatically complete job title (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Automatically complete a job title query.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Autocomplete](https://docs.cloud.google.com/talent-solution/job-search/docs/autocomplete)
  * [Autocomplete (v3)](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/autocomplete)
  * [Autocomplete (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/autocomplete)
  * [Quickstart: Search](https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-searching)
  * [Quickstart: Search (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-searching)



## Code sample

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
    
    
    import com.google.cloud.talent.v4beta1.CompleteQueryRequest;
    import com.google.cloud.talent.v4beta1.CompleteQueryResponse;
    import com.google.cloud.talent.v4beta1.CompletionClient;
    import com.google.cloud.talent.v4beta1.TenantName;
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
        try (CompletionClient completionClient = CompletionClient.create()) {
          TenantName parent = TenantName.of(projectId, tenantId);
          CompleteQueryRequest request =
              CompleteQueryRequest.newBuilder()
                  .setParent(parent.toString())
                  .setQuery(query)
                  .setPageSize(5) // limit for number of results
                  .addLanguageCodes("en-US") // language code
                  .build();
          CompleteQueryResponse response = completionClient.completeQuery(request);
          for (CompleteQueryResponse.CompletionResult result : response.getCompletionResultsList()) {
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
