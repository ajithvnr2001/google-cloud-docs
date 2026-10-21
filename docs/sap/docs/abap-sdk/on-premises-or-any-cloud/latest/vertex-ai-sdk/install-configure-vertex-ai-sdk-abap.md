---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap/
title: Install and configure the Agent Platform SDK for ABAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:21.007035+00:00
---

# Install and configure the Agent Platform SDK for ABAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install and configure the Agent Platform SDK for ABAP Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap)



To integrate Gemini Enterprise Agent Platform capabilities into your SAP applications, install and configure the Agent Platform SDK for ABAP on an SAP host system. The host system can run on Compute Engine, other cloud virtual machines, SAP RISE with S/4HANA Cloud Private Edition, or an on-premises instance. Use this SDK to create ABAP-based AI agents that automate enterprise processes.

## Installation

When you install the latest version of the on-premises or any cloud edition of ABAP SDK for Google Cloud, the Agent Platform SDK for ABAP is installed for you. For information about the installation steps, see [Install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

If you're using version 1.7 or earlier of the on-premises or any cloud edition of ABAP SDK for Google Cloud, then update your SDK to the latest version to get the Agent Platform SDK for ABAP. For more information, see [Update ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#abap-sdk-update).

We understand that access to Agent Platform and cloud resources might be limited for some developers. To enable prototyping and experimentation with minimal setup, see [Quick prototyping with Gemini](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/quick-prototyping-with-gemini).

## Enable APIs

To use the Agent Platform SDK for ABAP, you need to enable the necessary APIs in your Google Cloud project.

For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

### Agent Platform API

Enable the Agent Platform API in your Google Cloud project.

[Agent Platform API](https://console.cloud.google.com/project/_/apis/library/aiplatform.googleapis.com)

### APIs for Gemma models on Cloud Run

If you want to use Gemma models on Cloud Run, then enable the following APIs:

  * [Gemini API](https://console.cloud.google.com/project/_/apis/library/generativelanguage.googleapis.com)
  * [Cloud Run](https://console.cloud.google.com/project/_/apis/library/run.googleapis.com)



## Deploy models in Agent Platform Model Garden

If you want to use an open model or a partner model, then you need to deploy the required model in Agent Platform Model Garden.

For information about how to deploy models in Model Garden, see [Use models in Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/use-models).

### Deploy Gemma models in Agent Platform

In the Google Cloud console, go to the **Model Garden** page, find a supported Gemma model and deploy the model. For more information, see [Deploy an open model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/use-models#deploy_an_open_model).

### Deploy partner models in Agent Platform

If you want to use a partner model, then you need to deploy the required model in Agent Platform.

The Agent Platform SDK for ABAP supports Anthropic Claude models.

To enable a Claude model, go to the **Model Garden** page in the Google Cloud console, find a supported Claude model, and then click **Enable**.

For more information about available Claude models, see [Anthropic Claude models on Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude).

## Authentication

Once you set up authentication to access Google Cloud APIs in your on-premises or any cloud edition of ABAP SDK for Google Cloud, the Agent Platform SDK for ABAP utilizes the same authentication method to access the Agent Platform API.

The authentication method you use depends on the specific model and platform where you deploy the model. While most Agent Platform services use [JWTs](https://docs.cloud.google.com/docs/authentication/token-types#sa-jwts) or [Access Tokens](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens), certain models deployed on specialized platforms require a different credential.

The following table summarizes the required authentication method based on the model and its deployment platform:

Models and services | Required credential | Description  
---|---|---  
**Gemini** , **Claude** , **Gemma** (Deployed on Agent Platform Model Garden), **embeddings** , **Vector Search** , **Agent Platform Feature Store** | **JWT** or **Access Token** | Used for standard IAM authentication with Agent Platform's managed services. For more information, see [Authentication overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).  
**Gemma** (Deployed on Cloud Run) | **ID Token** | Required to authenticate with the deployed Cloud Run endpoint. For information about setting up authentication to invoke Cloud Run, see [Authenticate with ID tokens for Cloud Run](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-cloud-functions).  
**Gemma** (Accessed through Gemini API) | **API Key** | Required when using the Gemini API path for this model. For information about setting up authentication to invoke Cloud Run, see [Authenticate with API keys](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys).  
  
For general information about how to set up authentication depending on the environment where you host your SAP system, see [Authentication overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

Note the name of the client key that you create during the authentication setup. You use this client key when you configure AI model generation parameters and search parameters.

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

  
  
#### Gemma models on Cloud Run

To use Gemma models, you must grant the following roles to the service account based on the deployment platform:

**Deployment platform** | **Required IAM roles**  
---|---  
Gemma models deployed on Agent Platform Model Garden | [Agent Platform User (`roles/aiplatform.user`)](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user)  
Gemma models on Cloud Run | [Cloud Run Invoker (`roles/run.invoker`)](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker)  
  
## Configure the model generation parameters

Large language models (LLMs) are deep learning models trained on massive amounts of text data. A model includes parameter values that control how the model generates a response. You can get different results from the model by changing the parameter values.

To define the generation parameters for a model, the Agent Platform SDK for ABAP uses the table `/GOOG/AI_CONFIG`.

**Note:** To configure the model generation parameters for embeddings models, you need to populate only the following fields: **Model Key** , **Model ID** , **Google Cloud Key Name** , **Google Cloud Region Location ID** and **Publisher ID of the LLM**. Leave all the other fields blank.

To configure the generation parameters for a model, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Agent Platform SDK: Configure Model Generation Parameters**.

  3. Click **New Entries**.

  4. Choose your model family, and enter values as appropriate: 

### Gemini

Field | Data type | Description  
---|---|---  
**Model Key** | String | A unique name that you specify to identify the model configuration, such as `Gemini`. You use this model key while instantiating the generative model class or the embeddings class to specify the generation configuration to take effect.  
**Model ID** | String | Model ID of the LLM that you want to use. For the list of Gemini and embedding models that are available on Google Cloud's Agent Platform and their model IDs, see [Model versions and lifecycle](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions).  
**Google Cloud Key Name** | String | The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).  
**Google Cloud Region Location ID** | String | The location ID of the Google Cloud region where the Agent Platform features that you want to use are available. Typically, you use the region closest to your physical location or the physical location of your intended users. For more information, see [Agent Platform locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations).  
**Publisher ID of the LLM** | String | The publisher of the LLM, such as `google`.  
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
  
### Claude

Field | Data type | Description  
---|---|---  
**Model Key** | String | A unique name that you specify to identify the model configuration, such as `Claude`. You use this model key while instantiating the generative model class to specify the generation configuration to take effect.  
**Model ID** | String | Model ID of the supported Claude model, such as `claude-sonnet-4@20250514`. For a list of supported Claude models, see [Anthropic Claude models on Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude).  
**Google Cloud Key Name** | String | The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).  
**Google Cloud Region Location ID** | String | The location ID of the Google Cloud region where the Claude model that you want to use is available. Typically, you use the region closest to your physical location or the physical location of your intended users. For more information, see [Anthropic Claude quotas and region availability](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/use-claude#quotas).  
**Publisher ID of the LLM** | String | The publisher of the LLM, such as `anthropic`.  
**Response MIME type** | String | Optional. Output response MIME type of the generated candidate text. Supported MIME type: 
     * `text/plain`: (default) Text output.
     * `application/json`: JSON response in the candidates.
The model needs to be prompted to output the appropriate response type, otherwise the behavior is undefined.  
**Randomness temperature** | String | Optional. Controls the randomness of predictions. For more information, see [Temperature](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#temperature). Range: [0.0, 1.0]  
**Top-K Sampling** | Float | Optional. Top-K changes how the model selects tokens for output. Specify a lower value for less random responses and a higher value for more random responses. For more information, see [Top-K](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#top-k). Range: [1, 40]  
**Top-P Sampling** | Float | Optional. Top-P changes how the model selects tokens for output. Specify a lower value for less random responses and a higher value for more random responses. For more information, see [Top-P](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#top-p). Range: [0.0, 1.0]  
**Maximum number of output tokens per msg** | Integer | Optional. Maximum number of tokens that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. Specify a lower value for shorter responses and a higher value for potentially longer responses.  
**Positive Penalties** | Float | Not applicable  
**Frequency Penalties** | Float | Not applicable  
  
### Gemma

Field | Data type | Description  
---|---|---  
**Model Key** | String | A unique name that you specify to identify the model configuration, such as `Gemma`. You use this model key while instantiating the generative model class or the embeddings class to specify the generation configuration to take effect.  
**Model ID** | String | The version name from the Agent Platform Model Garden for your chosen model, such as `gemma-3n-e4b-it`. For information about Gemma model versions, see [Use Gemma open models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-gemma).  
**Google Cloud Key Name** | String | The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).  
**Google Cloud Region Location ID** | String | The location ID of the Google Cloud region where the Gemma model is deployed. Typically, you use the region closest to your physical location or the physical location of your intended users.  
**Publisher ID of the LLM** | String | The publisher of the LLM, such as `google`.  
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
  5. Save the new entry.




## Configure the Vector Search parameters

To define Vector Search configurations, the Agent Platform SDK for ABAP uses the table `/GOOG/SEARCHCONF`.

To configure the Vector Search parameters, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Agent Platform SDK: Configure Vector Search Parameters**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Data type | Description  
---|---|---  
**Search Key** | String | A unique name that you specify to identify the search configuration.  
**Google Cloud Key Name** | String | The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).  
**Google Cloud Region Location ID** | String | The location ID of the Google Cloud region where the Agent Platform features that you want to use are available. Typically, you use the region closest to your physical location or the physical location of your intended users. For more information, see [Agent Platform locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations).  
**Deployment ID of Vector Index** | String | The deployment ID of an index. When you deploy an index to an endpoint, you assign it a unique deployment ID. For information about index deployment, see [Deploy a vector index to an index endpoint](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-vector-search#deploy-index).  
**Vector Index Endpoint ID** | String | The ID of the index endpoint to which the index is deployed to. For information about index endpoint, see [Create a vector index endpoint](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-vector-search#create-index-endpoint).  
  5. Save the new entry.




## What's next

  * Explore the built-in [Generative AI demos for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/demos-overview).
  * Learn about [Generative AI on Agent Platform for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/vertex-ai-for-sap-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
