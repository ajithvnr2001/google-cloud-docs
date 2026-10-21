---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/autocomplete/
title: Autocomplete \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:37.296063+00:00
---

# Autocomplete  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/autocomplete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Autocomplete Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution provides autocomplete suggestions for job titles and company names. Only active job postings and companies with at least one open job are considered eligible for suggestion results. Once a new job or company is added, it takes up to 48 hours for the information to be added to the autocomplete result set.

To use autocomplete, call the [`complete`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants/completeQuery) method when the search bar is updated.

**Note:** Language codes must be specified using the [BCP-47](https://tools.ietf.org/html/bcp47) identifier. For example: `en-US` or `zh-TW`. Do not use abbreviated language codes such as `en` or `zh`.

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
