---
url: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-documentai-batchprocess-task/
title: Doc AI - Batch Process task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:41.465496+00:00
---

# Doc AI - Batch Process task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-documentai-batchprocess-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Doc AI - Batch Process task

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Doc AI - Batch Process** task lets you send a single batch (asynchronous) request to the Document AI processor to process multiple documents. Document AI then starts a long-running operation (LRO) and stores the processed results in a Cloud Storage bucket. The [Document AI processor](https://docs.cloud.google.com/document-ai/docs/overview#dai-processors) is a Cloud Document AI component that performs varies document processing actions such as, classify, split, parse or analysis of a document.

[Cloud Document AI](https://cloud.google.com/document-ai/docs) is a Google Cloud service that allows you to parse structured information from unstructured or semi-structured documents using state-of-the-art Google AI such as natural language, computer vision, translation, and AutoML. 

## Before you begin

Ensure that you perform the following tasks in your Google Cloud project before configuring the **Doc AI - Batch Process** task:

  1. Enable the Cloud Document AI API (`documentai.googleapis.com`). 

[ Enable the Cloud Document AI API ](https://console.cloud.google.com/apis/enableflow?apiid=documentai.googleapis.com)

  2. Create an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile). Application Integration uses an authentication profile to connect to an authentication endpoint for the **Doc AI - Batch Process** task. **Note:** If you're creating an authentication profile of [Service account](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles#service-account) type, then ensure that the service account is assigned with the IAM role that contains the following IAM permission(s): 
     * `documentai.processors.processBatch`
     * `documentai.processorVersions.processBatch`

To know about IAM permissions and the predefined IAM roles that grant them, see [IAM permissions reference](https://docs.cloud.google.com/iam/docs/roles-permissions).

For information about granting additional roles or permissions to a service account, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Configure the Doc AI - Batch Process task

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**. The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Tasks** to view the list of available tasks and connectors. 
  5. Click and place the **Doc AI - Batch Process** element in the integration editor.
  6. Click the **Doc AI - Batch Process** element on the designer to view the **Doc AI - Batch Process** task configuration pane.
  7. Go to **Authentication** , and select an existing authentication profile that you want to use. 

Optional. If you have not created an authentication profile prior to configuring the task, Click **\+ New authentication profile** and follow the steps as mentioned in [Create a new authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile).

  8. Go to **Task Input** , and configure the displayed inputs fields using the following Task input parameters table. 

Changes to the inputs fields are saved automatically.




## Task input parameters

The following table describes the input parameters of the **Doc AI - Batch Process** task: 

Property | Data type | Description   
---|---|---  
Region | String | Cloud Document AI [location](https://docs.cloud.google.com/document-ai/docs/regions) for the processor. For example: `us` \- United States.  
ProjectsId | String | Your Google Cloud project ID.  
ProcessorsId| String | The ID of your custom processor.  
Request | JSON | See [request JSON structure.](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/batchProcess#request-body)  
  
## Task output

The **Doc AI - Batch Process** task returns the name of your long-running operation (LRO), similar to the following sample output: 
    
    
    {
        "name": "projects/[PROJECT_ID]/locations/[LOCATION]/operations/[OPERATION_ID]"
    }
    

## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Add [edges and edge conditions](https://docs.cloud.google.com/application-integration/docs/edge-overview).
  * [Test and publish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) your integration.
  * Configure a [trigger](https://docs.cloud.google.com/application-integration/docs/how-to-guides#configure-triggers).
  * Add a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/data-mapping-task).
  * See [all tasks for Google Cloud services](https://docs.cloud.google.com/application-integration/docs/how-to-guides#configure-tasks-for-google-cloud-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
