---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/autocomplete/
title: Autocomplete (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:17.048133+00:00
---

# Autocomplete (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/autocomplete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Autocomplete (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution provides autocomplete suggestions for job titles and company names. Only active job postings and companies with at least one open job are considered eligible for suggestion results. Once a new job or company is added, it takes up to 48 hours for the information to be added to the autocomplete result set.

To use autocomplete, call the [`complete`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects/complete) method when the search bar is updated.

**Note:** Language codes must be specified using the [BCP-47](https://tools.ietf.org/html/bcp47) identifier. For example: `en-US` or `zh-TW`. Do not use abbreviated language codes such as `en` or `zh`.

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
    
    

### Node.js

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
