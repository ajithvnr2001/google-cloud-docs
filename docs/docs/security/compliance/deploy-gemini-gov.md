---
url: https://docs.cloud.google.com/docs/security/compliance/deploy-gemini-gov/
title: Deployment guidance for Gemini for Government \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:59.719888+00:00
---

# Deployment guidance for Gemini for Government  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/deploy-gemini-gov/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Deployment guidance for Gemini for Government Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-24 UTC

This document provides technical guidance for US Federal agencies and DoD departments on deploying and using Gemini for Government in compliance with FedRAMP High and DoD Impact Level 4 (IL4) requirements. This document describes which services and features are included in the authorization boundaries and the steps to help you meet your compliance obligations.

Gemini for Government uses [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) to help with compliance requirements. You must deploy all Gemini for Government resources within an Assured Workloads folder that's configured for your specific compliance regime (FedRAMP High or IL4).

## Core product dependencies

Gemini for Government relies on several Google Cloud services. The following table lists the compliance status for each service.

Google Cloud service | FedRAMP High status | IL4 status  
---|---|---  
Gemini Enterprise | Authorized | Authorized  
Generative AI on Gemini Enterprise Agent Platform (formerly Generative AI on Vertex AI) | Authorized | Authorized  
BigQuery | Authorized | Authorized  
Cloud Storage | Authorized | Authorized  
Looker (Google Cloud core) | Authorized | Submitted  
**Note:** Because Looker (Google Cloud core) isn't yet IL4 authorized, dependent features like Gemini in Looker aren't authorized for IL4, as described in Unauthorized features that you should disable manually.

## Authorized services and features

The following table lists the services and features that you can use within Gemini for Government for FedRAMP High and IL4 deployments.

Feature | FedRAMP High | IL4  
---|---|---  
[Autocomplete](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete) | Authorized | Authorized  
[Serving controls](https://docs.cloud.google.com/gemini/enterprise/docs/configure-serving-controls) | Authorized | Authorized  
Authorized data stores such as [Cloud Storage](https://docs.cloud.google.com/gemini/enterprise/docs/connect-cloud-storage) and [BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connect-bigquery) | Authorized | Authorized  
[Web Grounding for Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/web-grounding-enterprise) | Authorized | Authorized  
[Uploading documents](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#upload_and_chat_about_files) from local machines | Authorized | Authorized  
Ability for end users to [select models](https://docs.cloud.google.com/gemini/enterprise/docs/answer-generation-models) | Authorized | Authorized  
[Deep Research agent](https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant) | Authorized | DISA review  
No-code agent creation using [Agent Designer](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer) | Authorized | DISA review  
[Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery) | Authorized | DISA review  
[Image generation using Nano Banana](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#generate_an_image) | Authorized | DISA review  
[Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview) (excludes Audio Overview, Infographic, Slide Deck, and Video Overview | Authorized | DISA review  
[Model Armor](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor) | Authorized | DISA review  
Google Workspace federated connectors (includes [Gmail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail), [Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive), and [Google Calendar](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal)) | Authorized | DISA review  
Third-party federated connectors (such as Microsoft Office 365 Government Community Cloud (GCC), Office GCC High and DoD, and [Salesforce](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce)) | Authorized | DISA review  
[Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas) | Authorized | DISA review  
[Projects](https://docs.cloud.google.com/gemini/enterprise/docs/projects) | Authorized | DISA review  
[Skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) | Authorized | DISA review  
  
## Model support

This section describes support for Google and third-party models.

### Google model support

Only [Google models that support US multi-regional endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency#ml-processing-google-models), including most Gemini models that are Generally Available, offer data residency (DRZ) commitments and can support FedRAMP High and DoD IL4 and IL5 requirements without requiring you to configure additional settings.

If you require DRZ commitments, it is your responsibility to restrict access to Google models that only support global endpoints. See [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage) for more information on how to restrict access to these models.

### Third-party model support

Google Cloud is responsible for maintaining authorizations for its serving infrastructure and custom-built containers so that you can deploy third-party models for FedRAMP High and DoD IL4 and IL5.

Although Google doesn't validate the compliance status of third-party model deployments or usage of these third-party models, you can use authorized services (such as Generative AI on Gemini Enterprise Agent Platform and Gemini Enterprise Agent Platform Inference: Batch and Online) to interact with more than 200 first-party, third-party, and open-source large language models (LLMs) available in Model Garden. It is your responsibility to ensure third-party models are deployed, configured, and secured in compliance with your FedRAMP and DoD IL4 and IL5 compliance requirements. For more information, see [Overview of self-deployed models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models) and [Control access to Model Garden models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access).

## Connector support

Connectors retrieve data from Google or third-party data sources into Gemini Enterprise. The two types of available connectors are federated connectors and ingestion connectors.

Federated connectors retrieve data from supported Google or third-party data sources. When a user runs a query, Gemini Enterprise federates the request to the connected data source, retrieves matching results in real time, and returns them in the query response. Data from the connected data source is not persisted in the Gemini Enterprise index.

Ingestion connectors copy and index data from the source system into Google Cloud. When a user runs a query, Gemini Enterprise retrieves results from this persisted index to deliver the response. The ingested data remains in the index until explicitly [removed or updated](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/create-manage-index).

You can enable and configure connectors from the Gemini Enterprise console. To restrict which data sources and egress destinations are permitted, you can use organization policy constraints.

### Third-party connector support

[Third-party federated connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source) (available at GA or Public Preview) are in-scope for Google's FedRAMP High authorization. IL5 authorization for federated connectors using Gemini Enterprise is pending.

### Google connector support

The Google federated connector for Google Workspace (which includes Gmail, Google Drive, and Google Calendar) is in-scope for Google's FedRAMP High authorization. IL5 authorization is pending.

Additionally, you can use the following Google ingestion connectors to comply with FedRAMP High and IL5 requirements:

  * [BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery)
  * [Cloud Storage](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage)



To ensure compliance, create a connection that uses regional endpoints and that is within the same organization and VPC Service Controls boundary.

For more information about connectors, see [Introduction to connectors and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores).

## Unauthorized features that you should disable manually

The following services and features aren't authorized for FedRAMP High or IL4. However, they aren't blocked by the Assured Workloads control packages and are available in your project. As part of your risk assessment, you might need to evaluate service usage relative to sensitive data and any mitigating controls available to you. You may need to manually disable the features on this list in your Gemini Enterprise app configuration based on your assessment.

Agents and galleries | 

  * [Prompt gallery](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/prompt-gallery)

  
---|---  
Grounding | 

  * [Grounding with Google Maps Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps)
  * [Grounding with Google Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-search)
  * Grounding using Google Drive uploads (for IL4 use cases)
  * Grounding using Microsoft OneDrive uploads (for IL4 use cases)

  
Generative features | 

  * [Generate images using Imagen](https://ai.google.dev/gemini-api/docs/imagen)
  * [Generate video with Veo](https://ai.google.dev/gemini-api/docs/video)

  
User, session, and UI features | 

  * [User events for Gemini Enterprise apps](https://docs.cloud.google.com/gemini/enterprise/docs/user-events)
  * [Personalization and memory in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization)
  * [Gemini Notebook Enterprise (for IL4 and IL5 use cases)](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview)
  * [Standalone Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#notebooklm-availability)

  
Other features | 

  * [Private Knowledge Graph in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search)
  * [Model Armor (for IL4 and IL5 use cases)](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor)
  * [Implicit context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)

  
  
For more information about implicit context caching, see [ Gemini Enterprise Agent Platform and zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention).

## Unauthorized features that you can't disable

The following services and features are available in the Assured Workloads control package. You can't disable them. If you use these features, we recommend that you conduct a proper risk assessment prior to granting your authorization to make sure service usage is appropriate for your FedRAMP High or IL4 deployment. For example, you can assess service usage relative to data sensitivity. You can also evaluate if any mitigating controls based on data encryption are available to you to establish sole control over data access.

Analytics and dependent features | 

  * [View analytics data](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics)
  * [Data agent context for Looker data sources](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/data-agent-authored-context-looker)
  * [Data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/data-agent-authored-context-bq)
  * [Data agents that you create](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview#build-and-interact-with-a-data-agent) using the Conversational Analytics API
  * [Gemini in BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-overview)
  * [Gemini in Looker](https://docs.cloud.google.com/gemini/docs/looker/overview)

  
---|---  
Data connectors and stores | 

  * Google Cloud data stores such as Cloud SQL and Firestore

  
User, session, and UI features | 

  * [Prompt chips](https://docs.cloud.google.com/gemini/enterprise/docs/configure-prompt-chips)

  
Other features | 

  * [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview)

  
  
## Deploy your environment

Follow these steps for assistance with deploying an environment that meets your compliance obligations:

  1. Deploy Assured Workloads: 
     1. [Create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder) that uses Data Boundary for FedRAMP High or Data Boundary for IL4.
     2. [Create your Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) inside this folder.
     3. [Verify that all users and service accounts](https://docs.cloud.google.com/resource-manager/docs/access-control-proj) have the required Identity and Access Management (IAM) permissions.
  2. Configure your FedRAMP High or IL4 network. For more information, see [Configure network for FedRAMP and DoD on Google Cloud](https://docs.cloud.google.com/architecture/configure-networks-fedramp-dod-google-cloud). 
     1. Create a [Gemini Enterprise app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app). Select **US Multi-region** as the location. The Assured Workloads data residency policy enforces this option.
  3. Connect to a [Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store) that's located within your Assured Workloads folder. The authorized data stores for FedRAMP High and IL4 are Cloud Storage buckets and BigQuery datasets.

**Note:** Don't connect to an unauthorized data source (for example, Cloud SQL or Google Drive) or a resource that's outside your Assured Workloads folder.
  4. Configure authorized compliance features.

  5. Turn off the unauthorized features that are described in unauthorized features that you should disable manually.

  6. Train your personnel not to use unauthorized features that you can't disable.




## Turn off unauthorized features

Complete the tasks in this section to turn off unauthorized features that you can disable manually.

### Disable the prompt gallery

Complete this task for each app that you deploy in Gemini Enterprise.

Ensure that you have one of the following roles:

  * **Discovery Engine Admin** (`roles/discoveryengine.admin`)
  * **Gemini Enterprise Admin** (`roles/discoveryengine.agentspaceAdmin`)
  * A custom role with the `discoveryengine.engines.update` permission




###  Console 

  1. In the Google Cloud console, go to the **Gemini Enterprise apps** page.



[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

  1. Select the app.
  2. In the navigation menu, click **Configurations** and then select the **Feature Management** tab.
  3. Turn off **Enable prompt gallery**.
  4. Click **Save**.



###  REST 

To update the feature control map of your app, use the `engines.patch` method on the `discoveryengine.googleapis.com` API endpoint.

Set the `prompt-gallery` key to `FEATURE_STATE_OFF` in your engine's [`features` configuration](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines).

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project
  * `APP_ID`: the ID of your app



HTTP method and URL: 
    
    
    PATCH https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features

Request JSON body: 
    
    
    {
      "features": {
        "prompt-gallery": "FEATURE_STATE_OFF"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID",
      "features": {
        "prompt-gallery": "FEATURE_STATE_OFF"
      }
    }
    

### Turn off grounding with Google Maps Platform

To turn off grounding with Google Maps Platform for all requests, you can disable the **Maps Grounding API** (`mapsgrounding.googleapis.com`) using one of the following methods:

  * In the **APIs & Services** page on the console, locate the **Map Grounding API** (`mapsgrounding.googleapis.com`), and select **Disable API**. For more information, see [Enable and disable services](https://docs.cloud.google.com/service-usage/docs/enable-disable#before).

  * In the Google Cloud CLI, run:
        
        gcloud services disable mapsgrounding.googleapis.com
        




### Turn off grounding with Google Search

To turn off grounding with Google Search for all requests, set the `constraints/vertexai.disableGenAIGoogleSearchGrounding` organization policy boolean constraint to `true` at the Assured Workloads folder level. For more information, see [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).

### Turn off grounding using Google Drive uploads (IL4 only)

This section applies to DoD IL4 customers only.

Grounding with Google Drive is only enabled when you connect a Google Drive data store to your app. To disable grounding with Google Drive uploads, complete the following:

  * Ensure that no Google Drive data stores are configured in your Gemini Enterprise apps. If an app is already connected to a Google Drive data store, remove it from the app's settings in the console, or delete the data store using the [`dataStores.delete` method](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores/delete) in the Discovery Engine API.

  * Disable Workspace data-sharing capabilities in the Google Admin console, or disable [**Smart features and personalization**](https://knowledge.workspace.google.com/admin/security/manage-google-workspace-smart-features-for-your-users) in Google Workspace to block the connector from accessing user documents in Google Drive.




### Turn off grounding using Microsoft OneDrive uploads (IL4 only)

This section applies to DoD IL4 customers only.

Grounding with Microsoft OneDrive is only enabled when you connect a Microsoft OneDrive data store to your app. To disable grounding with Microsoft OneDrive uploads, complete the following:

  * Ensure that no Microsoft OneDrive data stores are configured in your Gemini Enterprise apps. If an app is already connected to a Microsoft OneDrive data store, remove it from the [app's settings in the console](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-existing-data-store), or delete the data store using the [`dataStores.delete` method](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores/delete) in the Discovery Engine API.
  * To block the connector's access, revoke the credentials or delete the registered OAuth 2.0 application client ID and credentials in Microsoft Entra ID (Azure AD) that is used for Microsoft OneDrive connectivity.



### Turn off Imagen and Veo

To turn off image generation using Imagen and video generation using Veo, complete the following:

  * Set the `constraints/vertexai.allowedModels` or `constraints/vertexai.allowedGenAIModels` organization policy list constraint at the folder or organization level to deny the `imagen` and `veo` models (for example, `publishers/google/models/imagen-4.0-ultra-generate-001`) or to permit only approved models. For more information, see [Control access to Model Garden models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access).
  * To restrict prediction access on Imagen or Veo models, configure an [ IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) that denies the `aiplatform.endpoints.predict` IAM permission on the resource path for the model. The model resource path is `projects/PROJECT_ID/locations/LOCATION/publishers/google/models/MODEL_NAME`.

Replace the following:

    * PROJECT_ID: the ID of your project
    * LOCATION: the location of the app
    * MODEL_NAME: the name of the model to allow or deny



### Turn off user events for Gemini Enterprise apps

User events are sent by client-side event trackers or imported in bulk. To disable user events collection, complete one of the following:

  * When configuring the search widget for your application, disable event logging by setting the `disableUserEventsCollection` property to `true` inside the [`uiSettings` configuration namespace](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.widgetConfigs#uisettings). For example:
        
        "uiSettings": {
        "disableUserEventsCollection": true
        }
        

  * Don't call the event injection endpoints (specifically the [`userEvents.collect` method](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/collect) and the [`userEvents.write` method](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write)) and ensure that search pixel scripts (such as `v1beta_event.js`) are not active on your client pages.

  * Update the setting at the application level, as follows:

    1. In the Google Cloud console, go to the **Gemini Enterprise apps** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

    1. Select the app.
    2. In the navigation menu, click **Configurations**.
    3. Turn off **Enable user event collection**.
    4. Click **Save**.



### Turn off personalization and memory in Gemini Enterprise

Complete this task for each app that you deploy in Gemini Enterprise.

Ensure that you have one of the following roles:

  * **Discovery Engine Admin** (`roles/discoveryengine.admin`)
  * **Gemini Enterprise Admin** (`roles/discoveryengine.agentspaceAdmin`)
  * A custom role with the `discoveryengine.engines.update` permission




###  Console 

For instructions, see [Turn off personalization and memory](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization#disable-personalization-and-memory).

###  REST 

To update the feature control map of your app, use the `engines.patch` method on the `discoveryengine.googleapis.com` API endpoint.

Set the `personalization-memory` and `personalization-suggested-highlights` keys to `FEATURE_STATE_OFF` in your engine's [`features` configuration](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#engine).

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project
  * `APP_ID`: the ID of your app



HTTP method and URL: 
    
    
    PATCH https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features

Request JSON body: 
    
    
    {
      "features": {
        "personalization-memory": "FEATURE_STATE_OFF",
        "personalization-suggested-highlights": "FEATURE_STATE_OFF"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID",
      "features": {
        "prompt-gallery": "FEATURE_STATE_OFF",
        "personalization-memory": "FEATURE_STATE_OFF",
        "personalization-suggested-highlights": "FEATURE_STATE_OFF"
      }
    }
    

### Turn off Private Knowledge Graph

To turn off the Private Knowledge Graph, you can use the console or the API.

Ensure that you have one of the following roles:

  * **Discovery Engine Admin** (`roles/discoveryengine.admin`)
  * **Gemini Enterprise Admin** (`roles/discoveryengine.agentspaceAdmin`)
  * A custom role with the `discoveryengine.engines.update` permission




###  Console 

For instructions, see [Manage Knowledge Graph configuration](https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search#manage-kg-config).

###  REST 

To update your app configuration, use the `engines.patch` method on the `discoveryengine.googleapis.com` API endpoint.

Set `enablePrivateKnowledgeGraph` and `enableCloudKnowledgeGraph` to `false` inside the [`knowledgeGraphConfig` parameter](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#knowledgegraphconfig).

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project
  * `APP_ID`: the ID of your app



HTTP method and URL: 
    
    
    PATCH https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=knowledgeGraphConfig

Request JSON body: 
    
    
    {
      "knowledgeGraphConfig": {
        "enableCloudKnowledgeGraph": false,
        "enablePrivateKnowledgeGraph": false
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=knowledgeGraphConfig"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=knowledgeGraphConfig" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID",
      "knowledgeGraphConfig": {
        "enableCloudKnowledgeGraph": false,
        "enablePrivateKnowledgeGraph": false
      }
    }
    

### Turn off Model Armor (IL4 only)

This section applies to DoD IL4 customers only.

To turn off Model Armor for DOD IL4 environments, remove its templates from your apps and then disable the API.

To remove the templates, see [Remove the Model Armor templates from a Gemini Enterprise app](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor#remove-model-armor-templates).

To disable the **Model Armor API** (`modelarmor.googleapis.com`), use one of the following methods:

  * In the **APIs & Services** page on the console, locate **Model Armor API** (`modelarmor.googleapis.com`), and select **Disable API**. For more information, see [Enable and disable services](https://docs.cloud.google.com/service-usage/docs/enable-disable#before).

  * In Google Cloud CLI, run:
        
        gcloud services disable modelarmor.googleapis.com
        




### Turn off implicit context caching

To turn off implicit context caching, see [Enabling and disabling data caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention#enabling-disabling-caching).

### Turn off Gemini Notebook Enterprise (IL4 and IL5 only)

This section applies to DoD IL4 and IL5 customers only.

Complete this task for each app that you deploy in Gemini Enterprise.

Ensure that you have one of the following roles:

  * **Discovery Engine Admin** (`roles/discoveryengine.admin`)
  * **Gemini Enterprise Admin** (`roles/discoveryengine.agentspaceAdmin`)
  * A custom role with the `discoveryengine.engines.update` permission




###  Console 

  1. In the Google Cloud console, go to the **Gemini Enterprise apps** page.



[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

  1. Select the app.
  2. In the navigation menu, click **Configurations** and then select the **Feature Management** tab.
  3. Turn off **Notebook**.
  4. Click **Save**.



###  REST 

To update the feature control map of your app, use the `engines.patch` method on the `discoveryengine.googleapis.com` API endpoint. Set the `notebook-lm` key to `FEATURE_STATE_OFF` in your engine's [`features` configuration](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines).

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project
  * `APP_ID`: the ID of your app



HTTP method and URL: 
    
    
    PATCH https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features

Request JSON body: 
    
    
    {
      "features": {
        "notebook-lm": "FEATURE_STATE_OFF"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID?updateMask=features" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID",
      "features": {
        "prompt-gallery": "FEATURE_STATE_OFF",
        "notebook-lm": "FEATURE_STATE_OFF"
      }
    }
    

### Remove access to the standalone Gemini Notebook Enterprise

To remove access to the standalone Gemini Notebook Enterprise (`https://notebooklm.cloud.google.com/`), revoke the following IAM roles from all users and groups:

  * **Cloud NotebookLM User** (`roles/discoveryengine.notebookLmUser`)
  * **Cloud NotebookLM Admin** (`roles/discoveryengine.notebookLmOwner`)



For instructions on revoking roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Optionally, if your organization purchased a separate standalone Gemini Notebook Enterprise subscription (rather than a Gemini Enterprise subscription), turn off auto-renewal:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Manage subscriptions** page.

[Go to Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click the name of your standalone subscription.

  3. Click **Edit**.

  4. Clear the **Auto renew subscription** checkbox.

  5. Click **Submit**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
