---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-usage-audit-logs-for-nblme/
title: Configure usage audit logging for Gemini Notebook Enterprise \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:54.332592+00:00
---

# Configure usage audit logging for Gemini Notebook Enterprise  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-usage-audit-logs-for-nblme/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview)



Send feedback 

#  Configure usage audit logging for Gemini Notebook Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how admins can turn on and monitor usage audit logging for Gemini Notebook Enterprise through the API. Usage audit logs let organizations track user operations, metadata, and core content for auditing and observability purposes.

You can manage usage auditing for Gemini Notebook Enterprise using the `ObservabilityConfig` settings at the project level. Turning on observability captures request and response data, including prompts and grounding metadata, and stores it in Cloud Logging.

**Note:** Sensitive data isn't filtered out of the audit logs.

## Before you begin

Before configuring audit logs, ensure that you have the following IAM roles:

  * To enable the audit logs, you must have the [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role (`roles/discoveryengine.agentspaceAdmin`).
  * To access Cloud Logging, you must have the [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) IAM role (`roles/logging.viewer`).



## Turn on usage audit logging

To turn on usage audit logging, run the following command:

### REST

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID?updateMask=customerProvidedConfig.notebooklmConfig.observabilityConfig" \
    -d '{
      "customerProvidedConfig": {
        "notebooklmConfig": {
          "observabilityConfig": {
            "observabilityEnabled": true,
            "sensitiveLoggingEnabled": true
          }
        }
      }
    }'
    
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_ID`: the ID of your project.



## Logged information

The following table summarizes the usage data logged by Gemini Notebook Enterprise:

Service Path | Logged data  
---|---  
`NotebookService.CreateNotebook` |  Request: 

  * `parent`
  * `notebook.name`

Response: 
  * `No response fields are logged.`

  
`NotebookService.ShareNotebook` |  Request: 

  * `name`
  * `account_and_roles`

Response: 
  * `No response fields are logged.`

  
`NotebookService.DeleteNotebook` |  Request: 

  * `parent`
  * `names`

Response: 
  * `No response fields are logged.`

  
`NotebookService.GetNotebook` |  Request: 

  * `name`

Response: 
  * `name`
  * `title`
  * `cmek_config`

  
`SourceService.BatchCreateSources` |  Request: 

  * `parent`

Response: 
  * `sources.name`
  * `sources.source_id.id`
  * `sources.title`

  
`SourceService.UploadSourceFile` |  Request: 

  * `parent`
  * `blob.filename`
  * `source_id`

Response: 
  * `source_id.id`

  
`NotebookService.InteractSources` |  Request: 

  * `name`
  * `input_sources`
  * `free_form_action`

Response: 
  * `response.response`
  * `response.empty_answer_reason`
  * `response.citations.text`
  * `response.inline_citations.answer_citation_location`
  * `response.inline_citations.citations_reference`

  
`NotebookService.GenerateFreeFormStreamed` |  Request: 

  * `name`
  * `sources`
  * `user_query`

Response: 
  * `answer.response`
  * `answer.empty_answer_reason`
  * `citations.text`
  * `inline_citations.answer_citation_location`
  * `inline_citations.citations_reference`
  * `suggested_questions`

  
  
## Access usage logs

To view the usage audit logs for Gemini Notebook Enterprise:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the Google Cloud project for which you enabled audit logging.

  3. To show only Gemini Notebook Enterprise logs, enter the following query in the query editor field, and click **Run Query** :
         
         logName="projects/<var>PROJECT_ID</var>/logs/discoveryengine.googleapis.com%2Fnotebooklm_enterprise_user_activity"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.



## Turn off usage audit logs

To turn off usage audit logging, run the following command:

### REST

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID?updateMask=customerProvidedConfig.notebooklmConfig.observabilityConfig" \
    -d '{
      "customerProvidedConfig": {
        "notebooklmConfig": {
          "observabilityConfig": {
            "observabilityEnabled": false,
            "sensitiveLoggingEnabled": false
          }
        }
      }
    }'
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_ID`: the ID of your project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
