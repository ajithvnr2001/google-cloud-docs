---
url: https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor/
title: Enable Model Armor in Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:12.616525+00:00
---

# Enable Model Armor in Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Enable Model Armor in Gemini Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) for Gemini Enterprise. Model Armor is a Google Cloud service that enhances the security and safety of your AI applications by proactively screening the prompts and responses given by the Gemini Enterprise assistant. This helps protect against various risks and ensures responsible AI practices. Model Armor is supported on all Gemini Enterprise editions at no additional cost.

Model Armor does not remove or alter personally identifiable information (PII) or mask sensitive data. However, Gemini Enterprise blocks any response from the Gemini Enterprise assistant that triggers Sensitive Data Protection detectors.

**Note:** Enabling Model Armor in Gemini Enterprise can increase latency.

Model Armor's response to potential issues in user queries or responses from the Gemini Enterprise assistant is governed by the template's enforcement type. For more information, see [Define the enforcement type](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview#define-enforcement-type).

  * If the enforcement type is **Inspect and block** , Gemini Enterprise blocks the request and displays an error message. This is the default enforcement type when you create a Model Armor template using the console.

  * If the enforcement type is **Inspect only** , Gemini Enterprise does not block the requests or responses.




When the Model Armor screening service is unavailable, you can configure Gemini Enterprise to behave in one of the following ways:

Mode | Description  
---|---  
**Allow user interactions** |  In this mode, Gemini Enterprise allows requests and responses to pass through without proactive screening when the Model Armor screening service is unavailable, ensuring continuous communication with the end-user. However, this can occasionally expose unscreened messages or provide answers to unscreened queries.   
**Block all user interactions** |  In this mode, when the Model Armor screening service is unavailable, Gemini Enterprise blocks all requests and responses, including legitimate ones.   
  
## Before you begin

  * Make sure you have the required roles assigned to you and the service account:

    * To enable Model Armor in Gemini Enterprise, you need the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) role.

    * To create the Model Armor templates, you need the [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) role (`roles/modelarmor.admin`).

    * To call the Model Armor APIs, you need the [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) role (`roles/modelarmor.user`).

**Note:** To grant multiple IAM roles to a service account, see [Grant or revoke multiple IAM roles using the Google Cloud console](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#multiple-roles-console).
    * If your Model Armor template is in a different project than your Gemini Enterprise app, the template's project must grant the [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) role (`roles/modelarmor.user`) to the Gemini Enterprise app's [service account](https://docs.cloud.google.com/iam/docs/service-agents#discovery-engine-service-account). The service account ID is `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`, where `PROJECT_NUMBER` is the project number of your Gemini Enterprise app.
  * Ensure you have created a Gemini Enterprise app. To create one, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).




## Create a Model Armor template

We recommend that you configure two separate Model Armor templates: one for user prompts and one for responses. User prompts and responses have different risk profiles and objectives:

  * **Template for user prompts** : Focuses on preventing malicious inputs, prompt injections, jailbreak attempts, and sensitive data from being sent or uploaded. Although harmful content is also a concern for user inputs, you can disable responsible AI filters on the user prompt template because Gemini includes built-in safety checks for user prompts.
  * **Template for response outputs** : Focuses on preventing responses from returning or leaking sensitive data, generating harmful or off-brand content, or returning malicious URLs.



For more information about creating templates, see [Create a Model Armor template](https://docs.cloud.google.com/security-command-center/docs/manage-model-armor-templates).

### Configuration considerations

When creating a Model Armor template for Gemini Enterprise apps, consider these configurations:

  * You can create Model Armor templates centrally in one project and reuse them across different projects. If you use a cross-project template, ensure that the cross-project permissions are configured as described in Before you begin.

  * Select **Multi-region** in the **Regions** field. The following table shows you how to map Model Armor template regions to Gemini Enterprise app regions:

**Note:** After a Model Armor template or a Gemini Enterprise app is created, the regions can't be changed.Gemini Enterprise app multi-region | Model Armor multi-region  
---|---  
Global | 
    * US (multiple regions in United States)
    * EU (multiple regions in the Europe Union)  
US (multiple regions in United States) | US (multiple regions in United States)  
EU (multiple regions in the Europe Union) | EU (multiple regions in the Europe Union)  
  * Google does not recommend configuring cloud logging in the Model Armor template for Gemini Enterprise apps. This configuration can expose sensitive data to users with the Private Logs Viewer (`roles/logging.privateLogViewer`) IAM role. Instead, consider the following options:

    * If you need to log the data that goes through the Model Armor template, you can reroute logs to a secure storage like BigQuery, which offers stricter access controls. For more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

    * You can configure Data Access audit logs to analyze and report on the request and response screening verdicts generated by Model Armor. For more information, see Configure audit logs.

  * Avoid turning on the prompt injection and jailbreak detection filter for responses. Prompt injection and jailbreak attacks are more commonly used in user prompts. Enabling this filter on responses can increase false positives and add unnecessary latency.




## Configure the Gemini Enterprise app with the Model Armor templates

The following steps describe how to add the Model Armor templates to your Gemini Enterprise app.

### Console

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations** > **Assistant**.

  4. To turn on Model Armor, click **Enable Model Armor**.

  5. For **Model Armor template for user prompts** and **Model Armor templates for response outputs** , enter the **Resource name** of the Model Armor templates you created.

**Note:** To get the **Resource name** , follow the steps in the [View a Model Armor template](https://docs.cloud.google.com/security-command-center/docs/manage-model-armor-templates#view-ma-template) documentation, and copy the **Resource name** value. You can use Model Armor templates created in the same project as the Gemini Enterprise app or use Model Armor templates from a different project. If you use a template from a different project, ensure the cross-project permissions are configured as described in Before you begin.
  6. If you want to block user interactions during Model Armor processing failures, click the **Allow user interactions during Model Armor processing failure** toggle to the off position. For more information, see the two modes supported by Gemini Enterprise when Model Armor is unavailable.

  7. Click **Save and publish**.




### REST

To add the Model Armor templates to your Gemini Enterprise app, run the following command :

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant?update_mask=customerPolicy" \
    -d '{
      "customerPolicy": {
        "modelArmorConfig": {
          "userPromptTemplate": "QUERY_PROMPT_TEMPLATE",
          "responseTemplate": "RESPONSE_PROMPT_TEMPLATE",
          "failureMode": "FAIL_MODE"
        }
      }
    }'
    
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
  * `APP_ID`: the ID of the app that you want to configure.
  * `QUERY_PROMPT_TEMPLATE`: the **Resource name** of the Model Armor templates you created.   
To get the **Resource name** , follow the steps in the [View a Model Armor template](https://docs.cloud.google.com/security-command-center/docs/manage-model-armor-templates#view-ma-template) documentation, and copy the **Resource name** value.

**Note:** You can use Model Armor templates created in the same project as the Gemini Enterprise app or use Model Armor templates from a different project. If you use a template from a different project, ensure the cross-project permissions are configured as described in Before you begin.
  * `RESPONSE_PROMPT_TEMPLATE`: the **Resource name** of the Model Armor templates you created. You can use Model Armor templates created in the same project or from a different project.

  * `FAIL_MODE`: the operation mode when Model Armor is not available: `FAIL_CLOSED` or `FAIL_OPEN`.   
If the `FAIL_MODE` is not defined, `FAIL_CLOSED` is the default mode where all the interactions with the Gemini Enterprise assistant are blocked when there are Model Armor processing failures. For more information, see the two modes supported by Gemini Enterprise when Model Armor is unavailable




#### Example command and result
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant?update_mask=customerPolicy" \
    -d '{
      "customerPolicy": {
        "modelArmorConfig": {
          "userPromptTemplate": "projects/my-project-123/locations/global/templates/123456789",
          "responseTemplate": "projects/my-project-123/locations/global/templates/123456789",
          "failureMode": "FAIL_OPEN"
        }
      }
    }'
    
    
    * * *
    
    
    {
      "name": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant",
      "displayName": "Default Assistant",
      "webGroundingType": "WEB_GROUNDING_TYPE_GOOGLE_SEARCH",
      "googleSearchGroundingEnabled": true,
      "customerPolicy": {
        "modelArmorConfig": {
          "userPromptTemplate": "projects/my-project-123/locations/global/templates/123456789",
          "responseTemplate": "projects/my-project-123/locations/global/templates/123456789",
          "failureMode": "FAIL_OPEN"
        }
      }
    }
    

## Test if the Model Armor template is enabled

After configuring the Model Armor template, test if your Gemini Enterprise app proactively screens and blocks user prompts and responses from the Gemini Enterprise assistant, according to the confidence levels set in the Model Armor filters.

When the Model Armor template is configured to **Inspect and block** requests that violate the policy, the following policy violation message is shown:

### Console

For example, you see the policy violation message: ![Shows the message a user gets when it violates the model-armor template that is enabled for the app.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/model-armor/model-armor-policy-violation-message.png)Model Armor policy violation message

### REST

A JSON response which includes the following:
    
    
    answer.state = SKIPPED
    answer.assist_skipped_reasons: [CUSTOMER_POLICY_VIOLATION]
    

## Remove the Model Armor templates from a Gemini Enterprise app

To remove the Model Armor templates from a Gemini Enterprise app, use the Google Cloud console or the REST API.

### Console

To remove the Model Armor templates from your Gemini Enterprise app, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations** > **Assistant**.

  4. To turn off Model Armor, click the **Enable Model Armor** toggle to the off position.

  5. Click **Save and publish**.




### REST

To remove the Model Armor templates from your Gemini Enterprise app, run the following command:

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant?update_mask=customerPolicy" \
    -d '{
      "customerPolicy": {
        "modelArmorConfig": {
        }
      }
    }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`.
  * `APP_ID`: the ID of the app that you want to configure.



#### Example command and result
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant?update_mask=customerPolicy" \
    -d '{
      "customerPolicy": {
        "modelArmorConfig": {
        }
      }
    }'
    
    
    * * *
    
    
    {
      "name": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant",
      "displayName": "Default Assistant",
      "webGroundingType": "WEB_GROUNDING_TYPE_GOOGLE_SEARCH",
      "googleSearchGroundingEnabled": true,
      "customerPolicy": {
        "modelArmorConfig": {}
      },
      "generationConfig": {
        "systemInstruction": {}
      }
    }
    

## Configure audit logs

Model Armor can write [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access), which you can use to analyze and report on the request and response screening verdicts generated by Model Armor. These logs don't contain the user queries or responses from the Gemini Enterprise assistant, so they are safe for reporting and analytics. For more information, see [Audit logging for Model Armor](https://docs.cloud.google.com/security-command-center/docs/audit-logging-model-armor).

To access these logs, you need to have the [Private Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) (`roles/logging.privateLogViewer`) IAM role.

### Enable Data Access audit logs

To enable the Data Access audit logs, follow these steps:

  1. In the Google Cloud console, go to **IAM & Admin** > **Audit Logs**.

  2. Select the **Model Armor API**.

  3. In the **Permission type** section, select the **Data read** permission type.

  4. Click **Save**.




### Examine Data Access audit logs

To examine the Data Access audit logs, follow these steps:

  1. In the Google Cloud console, go to **Logs Explorer**.

  2. Search the logs for the following method names:

     * `methodName: "google.cloud.modelarmor.v1.ModelArmor.SanitizeUserPrompt"` to view the user requests that were screened.

     * `google.cloud.modelarmor.v1.ModelArmor.SanitizeModelResponse` to view the responses that were screened.




## Considerations when using Model Armor

When using Model Armor with Gemini Enterprise, consider the following:

**De-identification and masking** |  When Model Armor uses a Sensitive Data Protection template for scanning prompts or responses, Model Armor checks if the content matches the detector criteria defined in the template. Although Sensitive Data Protection supports de-identification based on the template configuration, Model Armor does not pass de-identified or masked data back to Gemini Enterprise. If the content triggers any detectors from Sensitive Data Protection and the enforcement type is `INSPECT_AND_BLOCK`, Gemini Enterprise blocks the request or response rather than de-identifying it.   
---|---  
**Token limits and quotas** |  There are no token limits when you use Model Armor with Gemini Enterprise. However, the total throughput of your Model Armor evaluations is still indirectly governed by [Gemini Enterprise system quotas](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages) and [Model Armor API rate limits](https://docs.cloud.google.com/model-armor/quotas#quotas).   
**Service Level Agreement** |  Gemini Enterprise provides a [Service Level Agreement](https://cloud.google.com/terms/gemini/enterprise/sla). When Gemini Enterprise is configured to use Model Armor, blocked queries don't count as SLA violations, regardless of whether the **fail-open** or **fail-closed** mode is used.   
**Compliance** |  Both Gemini Enterprise and Model Armor offer various compliance certifications. When used together, the effective compliance certifications are the common subset of both products. Google recommends reviewing the compliance certifications for both products to ensure that they meet your regulatory requirements.   
**Document and image screening** |  In addition to text prompts, the Model Armor integration supports documents (such as PDFs) and images. The Model Armor integration screens the following files only when you upload them to the Gemini Enterprise assistant: 

  * Documents (such as PDFs, CSVs, and text files).
  * Images that you upload directly.
  * Images contained inside other files and documents that you upload directly. 

If a file or an image inside a document violates your configured policies, the entire file or document is discarded and excluded from the request. For the list of supported document types, see [Document screening](https://docs.cloud.google.com/model-armor/overview#ma-support-screening-pdfs).   
**Screened interactions and agents** |  If a Model Armor template is configured to screen user requests, only interactions with the following agents are screened in Gemini Enterprise: 

  * The Gemini Enterprise assistant
  * [ Employee-made agents](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview#types-of-agents), which are created in Gemini Enterprise app using the Workflow Builder.
  * [Google-made agents](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview#types-of-agents)

Interactions with custom agents from your organization, such as ADK, A2A, and Dialogflow, are not screened.   
  
## What's next

  * [Correlate Model Armor logs with Gemini Enterprise logs](https://docs.cloud.google.com/gemini/enterprise/docs/correlate-model-armor-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
