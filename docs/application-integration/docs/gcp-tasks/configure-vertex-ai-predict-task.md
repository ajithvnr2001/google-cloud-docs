---
url: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/
title: Vertex AI - Predict task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:34.471221+00:00
---

# Vertex AI - Predict task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Vertex AI - Predict task

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Vertex AI - Predict** task lets you perform an online prediction. Online predictions are synchronous requests made to a model [endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints). You can use online predictions when making requests in response to application inputs or when you require timely inferences.

[Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) is a Google Cloud service that allows you to train and deploy ML models and AI applications, and customize large language models (LLMs) for use in your AI-powered applications. 

## Before you begin

Ensure that you perform the following tasks in your Google Cloud project before configuring the **Vertex AI - Predict** task:

  1. Enable the Vertex AI API (`aiplatform.googleapis.com`). 

[ Enable the Vertex AI API ](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  2. Deploy the [model](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models) resource to the [endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints).
  3. Create an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile). Application Integration uses an authentication profile to connect to an authentication endpoint for the **Vertex AI - Predict** task. **Note:** If you're creating an authentication profile of [Service account](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles#service-account) type, then ensure that the service account is assigned with the IAM role that contains the following IAM permission(s): 
     * `aiplatform.endpoints.predict`

To know about IAM permissions and the predefined IAM roles that grant them, see [IAM permissions reference](https://docs.cloud.google.com/iam/docs/roles-permissions).

For information about granting additional roles or permissions to a service account, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  4. Ensure that [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is **NOT** setup for Application Integration in your Google Cloud project. **Warning:** **Vertex AI - Predict task** will not function or will stop functioning if [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is setup for Application Integration in your Google Cloud project. 



## Configure the Vertex AI - Predict task

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
  5. Click and place the **Vertex AI - Predict** element in the integration editor.
  6. Click the **Vertex AI - Predict** element on the designer to view the **Vertex AI - Predict** task configuration pane.
  7. Go to **Authentication** , and select an existing authentication profile that you want to use. 

Optional. If you have not created an authentication profile prior to configuring the task, Click **\+ New authentication profile** and follow the steps as mentioned in [Create a new authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile).

  8. Go to **Task Input** , and configure the displayed inputs fields using the following Task input parameters table. 

Changes to the inputs fields are saved automatically.




## Task input parameters

The following table describes the input parameters of the **Vertex AI - Predict** task: 

Property | Data type | Description   
---|---|---  
Region | String | Model endpoint [location](https://docs.cloud.google.com/document-ai/docs/regions). For example: `us` \- United States.  
ProjectsId | String | Your Google Cloud project ID.  
Endpoint| String | The name of the [endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints) requested to serve the prediction.  
Request | JSON | See [request JSON structure.](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/predict#request-body)  
  
## Task output

The **Vertex AI - Predict** task returns a response containing the [prediction](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/PredictResponse). 

## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * For information about how to use the Vertex AI task with a pre-existing model, see [AI powered applications with Application Integration and Vertex AI](https://www.googlecloudcommunity.com/gc/Integration-Services/AI-powered-applications-with-Application-Integration-and-Vertex/td-p/696540).
  * To learn how to use Vertex AI in Application Integration, see [Enhancing your business integration flows with Vertex AI](https://www.googlecloudcommunity.com/gc/Integration-Services/Enhancing-your-business-integration-flows-with-GenAI-Vertex-AI/td-p/696527).
  * [Test and publish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) your integration.
  * Add a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/data-mapping-task).
  * Learn about [all supported tasks and triggers](https://docs.cloud.google.com/application-integration/docs/how-to-guides#configure-tasks-for-google-cloud-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
