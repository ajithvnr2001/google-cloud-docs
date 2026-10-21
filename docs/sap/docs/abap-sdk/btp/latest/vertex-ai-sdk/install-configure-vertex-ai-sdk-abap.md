---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap/
title: Install and configure the Agent Platform SDK for ABAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:34.024636+00:00
---

# Install and configure the Agent Platform SDK for ABAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install and configure the Agent Platform SDK for ABAP Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap)



This document describes how to install and configure the Agent Platform SDK for ABAP in your [SAP BTP, ABAP environment](https://www.sap.com/india/products/technology-platform/abap.html#overview).

## Installation

When you install the latest version of the SAP BTP edition of ABAP SDK for Google Cloud, the Agent Platform SDK for ABAP is installed for you. For information about the installation steps, see [Install and configure the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config).

We understand that access to Agent Platform and cloud resources might be limited for some developers. To enable prototyping and experimentation with minimal setup, see [Quick prototyping with Gemini](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/quick-prototyping-with-gemini).

## Enable the Agent Platform API

  * Enable the Agent Platform API in your Google Cloud project.

[Agent Platform API](https://console.cloud.google.com/project/_/apis/library/aiplatform.googleapis.com)

For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/docs/getting-started#enabling_apis).




## Authentication

Once you set up authentication to access Google Cloud APIs in your SAP BTP edition of ABAP SDK for Google Cloud, the Agent Platform SDK for ABAP utilizes the same authentication method to access the Agent Platform API. For information about how to set up authentication in the SAP BTP edition of ABAP SDK for Google Cloud, see [Authentication overview](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication).

Make a note of the client key that you've created as part of the authentication setup. You use this client key when configuring AI model generation parameters and search parameters.

### IAM permissions

Ensure that the dedicated service account for API access that you've configured in the client key table has access to the Agent Platform resources.

#### Agent Platform

To use the Agent Platform resources, you must grant the [Agent Platform User (`roles/aiplatform.user`)](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user) role to the dedicated service account to which you have granted permissions to access the Agent Platform API.

If you need to provide specific permissions to create, modify, deploy artifacts, then grant specific [Agent Platform IAM permissions](https://docs.cloud.google.com/vertex-ai/docs/general/iam-permissions) as appropriate.

#### Agent Platform Feature Store

To use the Agent Platform Feature Store, you must grant the following roles to the service account:

**AI capability** | **Required IAM roles**  
---|---  
Agent Platform Feature Store | 

  * [Agent Platform Feature Store Admin (`roles/aiplatform.featurestoreAdmin`)](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.featurestoreAdmin)
  * [Agent Platform Feature Store Data Viewer (`roles/aiplatform.featurestoreDataViewer`)](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.featurestoreDataViewer)

  
  
## Verify the addition of Fiori apps to the launchpad

To let your administrators and developers configure the model generation parameters and the Vector Search parameters, the SAP BTP edition of ABAP SDK for Google Cloud provides SAP Fiori apps. The SDK also provides display-only Fiori apps for viewing the maintained parameters.

You add these Fiori apps to your launchpad while you're installing the SAP BTP edition of ABAP SDK for Google Cloud. Verify that these apps are available in your launchpad. For more information, see [Add Fiori apps to the launchpad](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config#add_fiori_apps_to_the_launchpad).

## Configure the model generation parameters

Large language models (LLMs) are deep learning models trained on massive amounts of text data. A model includes parameter values that control how the model generates a response. You can get different results from the model by changing the parameter values.

To define the generation parameters for a model, the Agent Platform SDK for ABAP uses the table `/GOOG/AI_CONFIG`.

**Note:** To configure the model generation parameters for embeddings models, you need to populate only the following fields: **Model Key** , **Model ID** , **Google Cloud Key Name** , **Google Cloud Region Location ID** and **Publisher ID of the LLM**. Leave all the other fields blank.

To configure the generation parameters for a model, perform the following steps:

  1. Access the SAP Fiori launchpad.

  2. Go to the [space](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config#assign_space_to_the_business_role) that contains the Fiori apps for SDK configuration.

  3. Open the **Vertex AI SDK: Configure Model Generation Parameters** app.

  4. Click **Create**.

  5. In the **Create** dialog that appears, enter a value for the **Model Key** field, and then click **Continue**.

  6. Enter values for the fields that appear.

The following table describes the fields and how they correspond to the model generation parameters:

Field | Data type | Description  
---|---|---  
**Model Key** | String | A unique name that you specify to identify the model configuration, such as `Gemini`. You use this model key while instantiating the generative model class or the embeddings class to specify the generation configuration to take effect.  
**Model ID** | String | Model ID of the LLM that you want to use. For the list of Gemini and embedding models that are available on Google Cloud's Agent Platform and their model IDs, see [Model versions and lifecycle](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions).  
**Google Cloud Key Name** | String | The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication).  
**Google Cloud Region Location ID** | String | The location ID of the Google Cloud region where the Agent Platform features that you want to use are available. Typically, you use the region closest to your physical location or the physical location of your intended users. For more information, see [Agent Platform locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations).  
**Publisher ID of the LLM** | String | Optional. The publisher of the LLM, such as `google`.  
**Response MIME type** | String | Optional. Output response MIME type of the generated candidate text. Supported MIME type: 
     * `text/plain`: (default) Text output.
     * `application/json`: JSON response in the candidates.
The model needs to be prompted to output the appropriate response type, otherwise the behavior is undefined.   
**Randomness temperature** | String | Optional. Controls the randomness of predictions. For more information, see [Temperature](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#temperature). Range: [0.0, 1.0]  
**Top-K Sampling** | Float | Optional. Top-K changes how the model selects tokens for output. Specify a lower value for less random responses and a higher value for more random responses. For more information, see [Top-K](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#top-k). Range: [1, 40]  
**Top-P Sampling** | Float | Optional. Top-P changes how the model selects tokens for output. Specify a lower value for less random responses and a higher value for more random responses. For more information, see [Top-P](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#top-p). Range: [0.0, 1.0]  
**Maximum number of output tokens per msg** | Integer | Optional. Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. Specify a lower value for shorter responses and a higher value for potentially longer responses.  
**Positive Penalties** | Float | Optional. Positive values penalize tokens that have appeared in the generated text, thus increasing the possibility of generating more diverse topics. Range: [-2.0, 2.0]  
**Frequency Penalties** | Float | Optional. Positive values penalize tokens that repeatedly appear in the generated text, thus decreasing the possibility of repeating the same content. Range: [-2.0, 2.0]  
  
If you don't provide a value for an optional parameter, then the SDK uses the default value of the parameter specific to the model version configured in `Model ID`.

  7. Click **Create** to save the entry.




## Configure the Vector Search parameters

To define Vector Search configurations, the Agent Platform SDK for ABAP uses the table `/GOOG/SEARCHCONF`.

To configure the Vector Search parameters, perform the following steps:

  1. Access the SAP Fiori launchpad.

  2. Go to the [space](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config#assign_space_to_the_business_role) that contains the Fiori apps for SDK configuration.

  3. Open the **Vertex AI SDK: Vector Search Configuration** app.

  4. Click **Create**.

  5. In the **Create** dialog that appears, enter a value for the **Model Key** field, and then click **Continue**.

  6. Enter values for the fields that appear.

The following table describes the fields and how they correspond to the Vector Search parameters:

Field | Data type | Description  
---|---|---  
**Search Key** | String | A unique name that you specify to identify the search configuration.  
**Google Cloud Key Name** | String | The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication).  
**Google Cloud Region Location ID** | String | The location ID of the Google Cloud region where the Agent Platform features that you want to use are available. Typically, you use the region closest to your physical location or the physical location of your intended users. For more information, see [Agent Platform locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations).  
**Deployment ID of Vector Index** | String | The deployment ID of an index. When you deploy an index to an endpoint, you assign it a unique deployment ID. For information about index deployment, see [Deploy a vector index to an index endpoint](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-vector-search#deploy-index).  
**Vector Index Endpoint ID** | String | The ID of the index endpoint to which the index is deployed to. For information about index endpoint, see [Create a vector index endpoint](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-vector-search#create-index-endpoint).  
  7. Click **Create** to save the entry.




## What's next

  * Learn about [Generative AI on Agent Platform for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/vertex-ai-for-sap-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
