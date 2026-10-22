---
url: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent/
title: Register and manage ADK agents hosted on Agent Runtime \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:44.927372+00:00
---

# Register and manage ADK agents hosted on Agent Runtime  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Register and manage ADK agents hosted on Agent Runtime Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how administrators register ADK agents from Agent Runtime for use in the Gemini Enterprise web app.

For ADK agents that are deployed on [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview), you can use a single [Agents CLI in Agent Platform](https://google.github.io/agents-cli) command to register the agents with Gemini Enterprise.

When you register ADK agents hosted on Agent Runtime with a Gemini Enterprise app and make these agents available to end users on the Gemini Enterprise web app:

  * The Agent Runtime service processes the agent queries.

  * The Agent Runtime ML processing terms apply. For more information, see [Agent Runtime limitations](https://docs.cloud.google.com/gemini/enterprise/docs/locations#agent_engine_limitations).




The following table describes how ADK agents are governed to ensure secure and controlled deployment and usage.

**Agent governance** | **Description**  
---|---  
**Secure communication** | The connection between Agent Runtime and Gemini Enterprise is compliant with VPC Service Controls (VPC-SC), ensuring secure data exchange.  
**Cross-project agent support** |  You can connect ADK agents hosted in a different Google Cloud. Gemini Enterprise uses Google Cloud's secure private networking for these cross-project connections. For more information, see [Configure cross-project ADK agent access](https://docs.cloud.google.com/gemini/enterprise/docs/configure-cross-project-adk-agents).   
**Personalized interactions** | ADK agents receive the user's email address from Gemini Enterprise. This allows agents to recognize individual users and provide personalized responses based on their identity and permissions.  
**Note:** To secure ADK agents, developers must configure Model Armor using the REST API within their agent's application code. The Model Armor settings in the Google Cloud console for Gemini Enterprise don't automatically protect ADK agents.

## Before you begin

Make sure you have the following:

  * The [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

  * Enable the Discovery Engine API. To enable the Discovery Engine API for the Google Cloud project, in the Google Cloud console, go to the **Discovery Engine API** page.

[Go to Discovery Engine API](https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics)

  * An existing Gemini Enterprise app. To create an app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * An ADK agent that is hosted on the Agent Runtime. For more information, see [Overview of Agent Development Kit](https://docs.cloud.google.com/agent-builder/agent-development-kit/overview).

    * If you don't have an agent, follow the steps in the [`adk-samples` GitHub Repository](https://github.com/google/adk-samples/tree/main/python/agents/fun-facts) to deploy a `fun_facts` agent to Agent Runtime. You can then register the agent with Gemini Enterprise.
**Tip:** You must host and maintain your ADK agents on Agent Runtime for them to function within Gemini Enterprise.
  * If your ADK agent is hosted in a different Google Cloud project than your Gemini Enterprise app, you must grant necessary permissions. For more information, see [Grant permissions for cross-project ADK agent access](https://docs.cloud.google.com/gemini/enterprise/docs/configure-cross-project-adk-agents).




## Configure authorization details (optional)

**Tip:** If the agent must access Google Cloud resources on behalf of a user, then you must configure the authorization details.

Follow these steps to obtain the authorization details.

  1. In the Google Cloud console, on the **APIs & Services** page, go to the **Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Select the Google Cloud project, which has the data source that you want the agent to access. For example, select the project that contains the BigQuery dataset that you want the agent to query.

  3. Click **Create credentials** and select **OAuth client ID**.

  4. In **Application type** , select **Web application**.

  5. In the **Authorized redirect URIs** section, add the following URIs:

     * `https://vertexaisearch.cloud.google.com/oauth-redirect`
     * `https://vertexaisearch.cloud.google.com/static/oauth/oauth.html`
  6. Click **Create**.

  7. In the **OAuth client created** panel, click **Download JSON**. The downloaded JSON includes the `Client ID`, `Authorization URI`, `Token URI`, and `Client secret` for the selected Google Cloud project. You need these details to create an authorization resource.




## Register an ADK agent with Gemini Enterprise

You can register your ADK agent with Gemini Enterprise using either the Google Cloud console or the REST API. This makes the agent available to users within a Gemini Enterprise app.

**Agent registration quota and licensing:** Registering an agent with an app consumes one unit of your project's pooled daily agent creation quota (`discoveryengine.googleapis.com/agents_tier_enterprise_regional`). Quota is determined by the number of Gemini Enterprise Standard licenses (1 creation per user per day, pooled) or Plus licenses (10 per user per day, pooled) distributed to the project. Frontline licenses provide 0 creation quota.

If you register a backend agent across multiple Gemini Enterprise apps or engines in the same project, each registration API call (`agents.create`) counts as an agent creation against this daily quota. Automated deployment scripts or CI/CD pipelines registering an agent across many apps can encounter `HTTP 429 RESOURCE_EXHAUSTED: Agent creation quota exceeded` if the number of registration calls in a day exceeds the number of distributed Standard licenses. Ensure your project has sufficient Standard licenses distributed before executing multi-app rollouts. For more details, see [Daily creation quotas](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits#creation-quotas).

### Console

To register an ADK agent using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to register the agent with.

  3. Click **Agents**. The **Agents** page displays.

  4. Click **add Add agent**. The **Add an agent** panel displays.

  5. Click **Add** for **Custom agent via Agent Runtime**. The **Authorizations** page displays.

  6. If you want the agent to access Google Cloud resources on your behalf, then each resource needs an authorization. To set up an authorization for a single resource, follow these steps:

     1. Click **Add authorization**.

     2. Enter a unique value for **Authorization name**. An ID is generated based on the name, and it can't be changed later.

     3. Enter the values that you generated in Configure authorization details (optional) in the following fields:

        1. Enter the value in the **Client ID** field.

        2. Enter the value in the **Client secret** field.

        3. Enter the value in the **Token URI** field.

        4. Enter the value in the **Authorization URI** field. Construct the Authorization URI using the details from your OAuth credentials JSON file. Copy the following template, and replace the placeholders with your specific values.
               
               https://accounts.google.com/o/oauth2/v2/auth?client_id=YOUR_CLIENT_ID&redirect_uri=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fstatic%2Foauth%2Foauth.html&scope=YOUR_CUSTOM_SCOPES&include_granted_scopes=true&response_type=code&access_type=offline&prompt=consent
               

        5. Click **Done**.

  7. Click **Next**.

  8. To configure your agent, follow these steps:

     1. Enter a name in the **Agent name** field. This value appears in the Gemini Enterprise web app as the display name of your agent.

     2. Enter a description in the **Describe your agent** field. This value is used by an LLM to determine whether to invoke your agent in response to a user query.

     3. Enter the **Agent Runtime** resource path. The resource path has the following format:
            
            projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID
             

For more information on how to list the agents hosted on Agent Runtime and get the resource path, see [List deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents#list).

     4. Click **Create**.




### REST

To register an ADK agent using the REST API, follow these steps:

  * Add an authorization resource to Gemini Enterprise (optional)
  * Register your ADK agent



### Add the authorization resource to Gemini Enterprise (optional)

If the agent must access Google Cloud resources on behalf of a user, run the following command to register the authorization resource you created in the Configure authorization details (optional) section with Gemini Enterprise:
    
    
    curl -X POST \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -H "Content-Type: application/json" \
       -H "X-Goog-User-Project: PROJECT_ID" \
       "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/authorizations?authorizationId=AUTH_ID" \
       -d '{
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/authorizations/AUTH_ID",
          "serverSideOauth2": {
             "clientId": "OAUTH_CLIENT_ID",
             "clientSecret": "OAUTH_CLIENT_SECRET",
             "authorizationUri": "OAUTH_AUTH_URI",
             "tokenUri": "OAUTH_TOKEN_URI"
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
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
  * `AUTH_ID`: the ID of the authorization resource. This is an arbitrary alphanumeric ID that you define. You need to reference this ID later when registering an Agent that requires OAuth support.
  * `OAUTH_CLIENT_ID`: the OAuth 2.0 client identifier you obtained when you created the OAuth credentials.
  * `OAUTH_CLIENT_SECRET`: the OAuth 2.0 client secret you obtained when you created the OAuth credentials.
  * `OAUTH_AUTH_URI`: the Authorization URI. To authorize your app, construct a specific Authorization URI using the details from your OAuth credentials JSON file. Copy the following template, and replace the placeholders with your specific values.
        
        https://accounts.google.com/o/oauth2/v2/auth?client_id=OAUTH_CLIENT_ID&redirect_uri=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fstatic%2Foauth%2Foauth.html&scope=YOUR_CUSTOM_SCOPES&include_granted_scopes=true&response_type=code&access_type=offline&prompt=consent
        

    * `YOUR_CUSTOM_SCOPES`: you can add the scopes you need. For example, the following OAuth scope string requests read-only access to your Google Drive and Google Docs.
          
          scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdocuments.readonly
          

  * `OAUTH_TOKEN_URI`: the token URI you obtained when you created the OAuth credentials.




#### More information about Authorization URI parameters.

To help ensure that the URI works correctly, verify the following fields:

**Parameter** | **Value or action**  
---|---  
`client_id` | Replace with the `client_id` that's found in your downloaded JSON.  
`redirect_uri` | Don't change. Must be `https://vertexaisearch.cloud.google.com/static/oauth/oauth.html`.  
`scope` |  List the Google API scopes that your app needs to access on behalf of the user. For example, to grant access to BigQuery, use the scope `https://www.googleapis.com/auth/bigquery` and for read-only access to Google Docs, use `https://www.googleapis.com/auth/documents.readonly`. If you're using multiple scopes, separate them with a space, which becomes `%20` in the URL.  
`include_granted_scopes` | Must be `true`.  
`response_type` | Must be `code` to receive an authorization code.  
`access_type` | Set to `offline` to help ensure that you receive a refresh token.  
`prompt` | Set to `consent` to help ensure that the user is always shown a consent screen.  
  
### Register your ADK agent

This code sample demonstrates how you can register your ADK agents.
    
    
       curl -X POST \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -H "X-Goog-User-Project: PROJECT_ID" \
          "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents" \
          -d '{
             "displayName": "DISPLAY_NAME",
             "description": "DESCRIPTION",
             "icon": {
                "uri": "ICON_URI"
             },
             "adkAgentDefinition": {
                "provisionedReasoningEngine": {
                   "reasoningEngine": "projects/PROJECT_ID/locations/RESOURCE_LOCATION/reasoningEngines/RESOURCE_ID"
                }
             },
             "authorizationConfig": {
                "toolAuthorizations": [
                   "projects/PROJECT_NUMBER/locations/global/authorizations/AUTH_ID"
                ]
             }
          }'
    

Replace the variables with values:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 

    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.

  * PROJECT_NUMBER: the number of your Google Cloud project.

  * APP_ID: the unique identifier for the Gemini Enterprise app.

  * DESCRIPTION: the description of the agent that's displayed in Gemini Enterprise.

  * ICON_URI: the public URI of the icon to display near the name of the agent. Alternatively, you can pass Base64-encoded image file contents, and in that case, use `icon.content`.

    * RESOURCE_ID: the ID of the Agent Runtime endpoint where the ADK agent is deployed. For more information on how to list the agents hosted on Agent Runtime and get the resource ID, see [List deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents#list).

    * RESOURCE_LOCATION: the cloud location of the Agent Runtime endpoint. For more information, see Agent Runtime location.

    * `authorization_config`: If you obtained the authorization details and want the agent to access Google Cloud resources on behalf of the user, add the `authorization_config` field to your JSON resource.

      * `AUTH_ID`: the value that you used for AUTH_ID in the Configure authorization details section.



## Share agents with users

To allow users to access an agent using the Gemini Enterprise web app, see [Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents#share_an_agent).

## List agents connected to an app

The following code sample demonstrates how you can get the details of all the agents connected to your app:

###  REST 
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents"
    

Replace the variables with values:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.
  * LOCATION: the multi-region of your app: `global`, `us`, or `eu`.
  * APP_ID: the ID of your Gemini Enterprise app.



If your agent isn't prebuilt by Google, the response includes a `name` field in the first few lines. The value of this field contains the Agent ID at the end of the path. For example, in the following response, the Agent ID is `12345678901234567890`:
    
    
    {
    "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890",
    ...
    }
    

## View the details of an ADK agent

The following code sample demonstrates how you can retrieve the details of an agent that was registered with Gemini Enterprise:

###  REST 
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
    

Replace the variables with values:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.
  * LOCATION: the multi-region of your app: `global`, `us`, or `eu`.
  * APP_ID: the ID of your Gemini Enterprise app.
  * AGENT_ID: the ID of the agent. You can find the agent ID by listing the agents connected to your app.



## Update an ADK agent

You can modify the details of an existing agent registered with Gemini Enterprise using either the Google Cloud console or the REST API.

### Console

To update the agent using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that includes the agent you want to update.

  3. Click **Agents**.

  4. Click the name of the **Agent Runtime** agent that you want to update, and then click **Edit**.

  5. Update the **Display name** , **Description** , or the **Agent Runtime reasoning engine**.

The resource path has the following format:
         
         projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID
         

For more information on how to list the agents hosted on Agent Runtime and get the resource path, see [List deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents#list).

  6. Click **Save**.




### REST

You can update all fields during the agent registration. However, the following fields must be updated:

  * `displayName`
  * `description`
  * `reasoningEngine`

This code sample demonstrates how you can update the registration of an existing ADK agent:
        
        curl -X PATCH \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -H "X-Goog-User-Project: PROJECT_ID" \
           "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/AGENT_RESOURCE_NAME" \
           -d '{
                 "displayName": "DISPLAY_NAME",
                 "description": "DESCRIPTION",
                 "adkAgentDefinition": {
                 "provisionedReasoningEngine": {
                    "reasoningEngine":
                    "projects/PROJECT_ID/locations/RESOURCE_LOCATION/reasoningEngine
                    s/RESOURCE_ID"
                 },
              }
           }'
        

Replace the variables with values:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 

    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.

  * AGENT_RESOURCE_NAME: the resource name of the agent registration to be updated.

  * DISPLAY_NAME: required. the user-friendly name for your agent that displays in Gemini Enterprise.

  * DESCRIPTION: required. A brief explanation of what your agent does that's visible to users in Gemini Enterprise.

  * RESOURCE_LOCATION: the cloud location of the Agent Runtime endpoint. For more information, see Agent Runtime location.

  * RESOURCE_ID: the ID of the Agent Runtime endpoint where the ADK agent is deployed. For more information on how to list the agents hosted on Agent Runtime and get the resource ID, see [List deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents#list).




## Delete an ADK agent

The following code sample demonstrates how you can delete an agent that is connected to your app:

###  REST 
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
    

Replace the variables with values:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.
  * LOCATION: the multi-region of your app: `global`, `us`, or `eu`
  * APP_ID: the ID of your Gemini Enterprise app.
  * AGENT_ID: the ID of the agent. You can find the agent ID by listing the agents connected to your app.



#### Example command and result
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890"
    
    
    * * *
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890/operations/delete-agent-12345678901234567890",
      "done": true
    }
    

## Agent Runtime location

When registering or updating an agent, the Agent Runtime location must be compatible with the location of your Gemini Enterprise app. Mismatched locations result in an error.

Refer to the following table for compatibility requirements:

**Gemini Enterprise app location** | **Allowed Agent Runtime location(s)**  
---|---  
`global` | Any supported Google Cloud region  
`us` | Any region starting with `us-`, such as `us-central1` or `us-east4`  
`eu` | Any region starting with `europe-`, such as `europe-west1` or `europe-west3`  
  
## Best practices for performance and reliability

To minimize response latency and prevent request timeouts when running ADK agents hosted on Agent Runtime in Gemini Enterprise, follow these best practices:

  * **Minimize sequential multi-agent hops and redundant summarization** : Each additional sub-agent handoff or tool round-trip adds model inference latency to the turn. Avoid deep sequential agent chains, and wrap sub-agents with `AgentTool(..., skip_summarization=True)` when the parent agent doesn't need to run an extra model pass to re-summarize a sub-agent's output.
  * **Configure runtime scaling and concurrency for multi-user workloads** : To prevent cold-start delays, request queuing, and out-of-memory (`OOM`) crashes when multiple users query your agent concurrently, configure `min_instances`, `resource_limits` (`cpu` and `memory`), and `container_concurrency` when deploying to Agent Runtime. For more information, see [Optimize and scale Agent Runtime performance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/optimize-and-scale).
  * **Pin matching package versions between local build and cloud runtime** : When deploying an agent to Agent Runtime, pin the exact same versions of `google-adk`, `google-cloud-aiplatform`, and `cloudpickle` in your deployment `requirements` list that you use in your local build environment to avoid deserialization overhead and initialization delays.
  * **Use the`global` endpoint for model calls and bound tool retries**: When your ADK agent invokes Gemini models on Vertex AI, use the `global` endpoint (or Provisioned Throughput) to reduce regional capacity contention, and configure explicit connection timeouts and bounded retry limits on external tool calls so slow downstream dependencies don't cause cascading turn timeouts.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
