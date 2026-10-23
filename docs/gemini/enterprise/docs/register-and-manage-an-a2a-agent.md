---
url: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent/
title: Register and manage A2A agents \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:56.111954+00:00
---

# Register and manage A2A agents  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Register and manage A2A agents Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Agent2Agent (A2A) Protocol](https://a2a-protocol.org/) is an open communication protocol and a universal language for agents. The protocol enables agents from different builders and platforms to discover each other, collaborate, and securely delegate tasks. This document explains how Gemini Enterprise administrators can connect agents that are built using A2A and hosted on any platform to Gemini Enterprise, making them available to users in the Gemini Enterprise web app.

**Note:** To secure A2A agents, developers must configure Model Armor using the REST API within their agent's application code. The Model Armor settings in the Google Cloud console for Gemini Enterprise don't automatically protect A2A agents.

## Before you begin

Make sure you have the following:

  * The [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

  * Enable the Discovery Engine API. To enable the Discovery Engine API for the Google Cloud project, in the Google Cloud console, go to the **Discovery Engine API** page.

[Go to Discovery Engine API](https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics)

  * An existing Gemini Enterprise app. To create an app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * An agent that uses the A2A protocol.

Gemini Enterprise supports the A2A v0.3 streaming mechanism.

If you use A2A v1.0.0 or later, then use the compatibility packages provided by the SDK to make sure that your agent functions with the earlier mechanism (for example, the `a2acompat/a2av0` package for Go or the `a2a.compat.v0_3` package for Python).

**Tip:** You must host and maintain your A2A agents for them to function within Gemini Enterprise.
  * If your A2A agent is hosted on Cloud Run, uses a default `.run.app` URL directly, and requires authentication, grant the Cloud Run Invoker (`roles/run.invoker`) role to the Discovery Engine service agent (this doesn't apply when Cloud Run is behind Apigee, a load balancer, or a custom domain):
        
        gcloud projects add-iam-policy-binding <var>PROJECT_ID</var> \
           --member="serviceAccount:service-<var>PROJECT_NUMBER</var>@gcp-sa-discoveryengine.iam.gserviceaccount.com" \
           --role="roles/run.invoker"
        

Replace the following:

    * `PROJECT_ID`: the ID of your project.
    * `PROJECT_NUMBER`: the number of your Google Cloud project.



## Configure authentication and authorization

Depending on your agent hosting environment and security requirements, you can configure how Gemini Enterprise authenticates with your agent, how your agent accesses resources on behalf of the end user, and how to secure your agent endpoint.

### How Gemini Enterprise authenticates with your agent

When Gemini Enterprise invokes an A2A agent, it can send authentication and authorization data in request headers depending on your hosting and security configuration:

**Header** | **Description**  
---|---  
`X-Serverless-Authorization` |  **Service-to-service IAM authentication** (for Cloud Run). If your A2A agent is hosted on Cloud Run and your agent URL is a default `.run.app` URL, Gemini Enterprise automatically generates a Google-signed OIDC ID token for the Discovery Engine service agent (`service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`) with your agent URL as the audience, and attaches it in the `X-Serverless-Authorization` header. If your agent URL uses Apigee, a load balancer, or a custom domain, Gemini Enterprise doesn't send this header. When Gemini Enterprise calls a default `.run.app` URL directly, the Cloud Run ingress infrastructure consumes this header to verify that the service agent has the `roles/run.invoker` IAM role (see Before you begin) before forwarding the request to your application container.  
`Authorization` |  **End-user OAuth 2.0 authorization** (for user context and API access). If you configure OAuth 2.0 credentials for your A2A agent (see Configure OAuth 2.0 for end-user authorization), Gemini Enterprise acquires an OAuth 2.0 access token or ID token on behalf of the signed-in end user after they grant consent, and sends it in the standard `Authorization` header (for example, `Bearer USER_OAUTH_TOKEN`). Cloud Run forwards the `Authorization` header directly to your container, allowing your agent application code to read the user token and call downstream APIs on behalf of the user.  
**Note:** Because Cloud Run consumes `X-Serverless-Authorization` for service-level IAM authentication and leaves the standard `Authorization` header intact for your container code, you can secure your agent as a private Cloud Run service while also receiving end-user OAuth tokens without header collisions.

### Configure OAuth 2.0 for end-user authorization (optional)

For A2A agents, configure OAuth 2.0 credentials if your agent must access Google Cloud resources or perform operations on behalf of the end user. For more information about how authentication and authorization headers work, see How Gemini Enterprise authenticates with your agent.

Follow these steps to create an OAuth client ID:

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




### Secure your A2A agent endpoint

For the authentication headers that Gemini Enterprise sends to your A2A agent, see How Gemini Enterprise authenticates with your agent. When you secure your agent endpoint, or an API gateway in front of it, consider the following:

  * **Agent card security schemes** : Gemini Enterprise doesn't use the `securitySchemes` and `security` fields of your agent card to authenticate with your agent.
  * **API keys and custom headers** : Gemini Enterprise doesn't support the `apiKey` security scheme, and doesn't provide a way to add static API keys or other custom header values to the requests that it sends to your agent.
  * **Service agent ID token** : Gemini Enterprise sends the `X-Serverless-Authorization` header only when your agent URL is a default Cloud Run URL that ends in `.run.app`. If your agent URL uses a custom domain, a load balancer, or an API gateway, Gemini Enterprise doesn't send this header.
  * **End-user token** : If you configure OAuth 2.0 for your agent, Gemini Enterprise sends the end user's token from your OAuth 2.0 provider in the `Authorization` header.



#### Secure an agent endpoint with Apigee

If you expose your A2A agent through an [Apigee](https://docs.cloud.google.com/apigee/docs) API proxy, the proxy receives the end-user token in the `Authorization` header but doesn't receive the `X-Serverless-Authorization` header. To secure the proxy, do the following:

  1. Configure OAuth 2.0 for end-user authorization for your agent (using either a Google Cloud OAuth 2.0 client ID or a third-party OAuth 2.0 provider), and provide those OAuth 2.0 details when you register the agent. Configuring OAuth 2.0 is required when securing an Apigee API proxy; don't skip the authorization step during registration.
  2. In your agent card, set `url` to the URL of your Apigee API proxy.
  3. In the API proxy, validate the end-user token in the `Authorization` header before you forward the request to your agent. Choose the Apigee policy based on the token format that your OAuth 2.0 provider issues: 
     * **Third-party OAuth 2.0 providers that issue signed JWT access tokens** : Use the [VerifyJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jwt-policy) to verify the token signature against your provider's public JSON Web Key Set (JWKS) URI and validate the issuer (`iss`) and audience (`aud`) claims.
     * **Google OAuth 2.0 (`accounts.google.com`)**: Google OAuth 2.0 access tokens (`ya29...`) are opaque tokens rather than signed JWTs. Use a [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) to call `https://oauth2.googleapis.com/tokeninfo` and verify the audience (`aud`) and `scope` fields.



## Register an A2A agent with Gemini Enterprise

You can register your A2A agent with Gemini Enterprise using either the Google Cloud console or the REST API. This makes the agent available to users within a Gemini Enterprise app.

**Important:** Traffic to A2A Agents added through this method do not go through [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-ge-deploy) and Agent Gateway policies do not apply.

**Agent registration quota and licensing:** Registering an agent with an app consumes one unit of your project's pooled daily agent creation quota (`discoveryengine.googleapis.com/agents_tier_enterprise_regional`). Quota is determined by the number of Gemini Enterprise Standard licenses (1 creation per user per day, pooled) or Plus licenses (10 per user per day, pooled) distributed to the project. Frontline licenses provide 0 creation quota.

If you register a backend agent across multiple Gemini Enterprise apps or engines in the same project, each registration API call (`agents.create`) counts as an agent creation against this daily quota. Automated deployment scripts or CI/CD pipelines registering an agent across many apps can encounter `HTTP 429 RESOURCE_EXHAUSTED: Agent creation quota exceeded` if the number of registration calls in a day exceeds the number of distributed Standard licenses. Ensure your project has sufficient Standard licenses distributed before executing multi-app rollouts. For more details, see [Daily creation quotas](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits#creation-quotas).

### Console

To register an A2A agent using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to register the agent with.

  3. Click **Agents > add Add Agents**.

  4. In the **Choose an agent type** section, click **Add** for **Custom agent via A2A**.

  5. In the **Agent card JSON** field, enter the agent card details in JSON format. For a complete list of available fields, see the [Agent2Agent (A2A) Protocol Official Specification](https://a2a-protocol.org/latest/specification/). The following example only uses the required fields.

For example:
         
         {
           "protocolVersion": "0.3",
           "name": "Hello World Agent",
           "description": "Just a hello world agent",
           "url": "https://example.com/myagent",
           "iconUrl": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTkiIGhlaWdodD0iOTkiIHN0eWxlPSJiYWNrZ3JvdW5kLWNvbG9yOmdyYXk7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zMyAwaDMzdjMzSDMzeiBNMCAzM2gzM3YzM0gweiBNNjYgMzNoMzN2MzNINjZ6IE0zMyA2NmgzM3YzM0gzM3oiIGZpbGw9ImJsdWUiLz48L3N2Zz4=",
           "version": "1.0.0",
           "capabilities": {
           },
           "skills": [
             {
               "id": "data-analysis",
               "name": "Data Analysis",
               "description": "Data analysis",
               "tags": []
             }
           ],
           "defaultInputModes": [
             "text/plain"
           ],
           "defaultOutputModes": [
             "text/plain"
           ]
         }
         

  6. Click **Preview agent details > Next**.

  7. Complete the setup using one of the following methods:

     * If you want the agent to access Google Cloud resources on behalf of you, or if your agent endpoint requires an `Authorization` header (for example, when securing an Apigee API proxy), follow these steps:

       1. Enter **Client ID** , **Client secret** , **Authorization URI** , and **Token URI** that you generated in Configure OAuth 2.0 for end-user authorization (optional).

       2. Enter the **Scopes**.

       3. Click **Finish**.

     * If you don't want the agent to access Google Cloud resources on behalf of you and your agent endpoint doesn't require an `Authorization` header, click **Skip & Finish**.




### REST

To register an A2A agent using the REST API, follow these steps:

  * Add an authorization resource to Gemini Enterprise (optional)
  * Register your A2A agent



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
`scope` |  List the Google API scopes that your app needs to access on behalf of the user. For example, to grant access to BigQuery, use the scope `https://www.googleapis.com/auth/bigquery` and for read-only access to Google Docs, use `https://www.googleapis.com/auth/documents.readonly`. If you're using multiple scopes, separate them with a space, which becomes `%20` in the URL. **Note:** If your A2A agent is hosted on Agent Runtime on Gemini Enterprise Agent Platform, you must create an authorization with `cloud-platform` scope. For example, `&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform`. For more information, see [Use an Agent2Agent agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-a2a-agent).   
`include_granted_scopes` | Must be `true`.  
`response_type` | Must be `code` to receive an authorization code.  
`access_type` | Set to `offline` to help ensure that you receive a refresh token.  
`prompt` | Set to `consent` to help ensure that the user is always shown a consent screen.  
  
### Register your A2A agent

To create and register an agent with Gemini Enterprise, use the [`agents.create`](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.agents/create) method. The following command uses only the required fields. For a complete list of available fields, see the [Agent2Agent (A2A) Protocol Official Specification](https://a2a-protocol.org/latest/specification/).

Run this command to register your A2A agent with Gemini Enterprise:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents \
    -d '
    {
      "name": "AGENT_NAME",
      "displayName": "AGENT_DISPLAY_NAME",
      "description": "AGENT_DESCRIPTION",
      "a2aAgentDefinition": {
        "jsonAgentCard": "{\"protocolVersion\":\"PROTOCOLVERSION\",\"name\":\"AGENT_NAME\",\"description\":\"AGENT_DESCRIPTION\",\"url\":\"AGENT_URL\",\"version\":\"AGENT_VERSION\",\"defaultInputModes\":[\"INPUT_MODE\"],\"defaultOutputModes\":[\"OUTPUT_MODE\"],\"capabilities\":{ CAPABILITIES },\"skills\":[SKILLS]}"
      },
      "authorizationConfig": {
        "agentAuthorization": "projects/PROJECT_ID/locations/LOCATION/authorizations/AUTH_ID"
      }
    }
    '
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
  * `PROJECT_ID`: the ID of your project.
  * `APP_ID`: the ID of the app with which you want to register the agent.
  * `AGENT_NAME`: the unique identifier for the agent.
  * `AGENT_DISPLAY_NAME`: the name of the agent that is displayed on the web app.
  * `AGENT_DESCRIPTION`: the description of what the agent can do.
  * `PROTOCOLVERSION`: the version of the A2A protocol the agent supports. For more information on the supported versions, see the [A2A release notes](https://github.com/a2aproject/A2A/releases).
  * `AGENT_URL`: the endpoint URL of the agent.
  * `AGENT_VERSION`: the version of the agent.
  * `INPUT_MODE`: the default input media type. For example, `application/json` or `text/plain`.
  * `OUTPUT_MODE`: the default output media type. For example, `text/plain"` or `image/png`.
  * `CAPABILITIES`: a JSON object containing supported A2A features. For example, `\"streaming\": true` or `\"pushNotifications\": false`.
  * `SKILLS`: a list of the [`AgentSkill` object](https://a2a-protocol.org/latest/specification/#554-agentskill-object) that the agent offers.
  * `authorizationConfig`: If you obtained the authorization details and want the agent to access Google Cloud resources on behalf of the user, add the `authorization_config` field to your JSON resource. 
    * `AUTH_ID`: the value that you used for AUTH_ID in the Add an authorization resource to Gemini Enterprise section.



#### Example command and result
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://global-discoveryengine.googleapis.com/v1alpha/projects/123456/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents \
    -d '
    {
      "name": "Hello World Agent",
      "displayName": "Hello World Agent",
      "description": "Just a hello world agent",
      "a2aAgentDefinition": {
        "jsonAgentCard": "{\"protocolVersion\":\"0.3.0\",\"name\":\"Hello World Agent\",\"description\":\"Just a hello world agent\",\"url\":\"https://example.com/myagent\",\"version\":\"1.0.0\",\"defaultInputModes\":[\"text\"],\"defaultOutputModes\":[\"text\"],\"capabilities\":{},\"skills\":[{\"description\":\"Chat with the Gemini agent.\",\"examples\":[\"Hello, world!\"],\"id\":\"chat\",\"name\":\"Chat Skill\",\"tags\":[\"chat\"]}]}"
      }
    }
    '
    
    
    * * *
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890",
      "displayName": "Hello World Agent",
      "description": "Just a hello world agent",
      "createTime": "2025-10-20T20:53:35.490600996Z",
      "state": "ENABLED",
      "a2aAgentDefinition": {
        "jsonAgentCard": "{\"protocolVersion\":\"0.3.0\",\"name\":\"Hello World Agent\",\"description\":\"Just a hello world agent\",\"url\":\"https://example.com/myagent\",\"version\":\"1.0.0\",\"capabilities\":{},\"defaultInputModes\":[\"text\"],\"defaultOutputModes\":[\"text\"],\"skills\":[{\"id\":\"chat\",\"name\":\"Chat Skill\",\"description\":\"Chat with the Gemini agent.\",\"tags\":[\"chat\"],\"examples\":[\"Hello, world!\"]}]}"
      }
    }
    
    
    
    

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
    

#### Example command and result
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents"
    
    
    * * *
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890",
      "displayName": "Hello World Agent",
      "description": "Just a hello world agent",
      "createTime": "2025-10-20T20:53:35.490600996Z",
      "state": "ENABLED",
      "a2aAgentDefinition": {
        "jsonAgentCard": "{\"name\":\"Hello World Agent\",\"description\":\"Just a hello world agent\",\"url\":\"https://example.com/myagent\",\"version\":\"1.0.0\",\"capabilities\":{},\"default_input_modes\":[\"text\"],\"default_output_modes\":[\"text\"],\"skills\":[{\"id\":\"chat\",\"name\":\"Chat Skill\",\"description\":\"Chat with the Gemini agent.\",\"tags\":[\"chat\"],\"examples\":[\"Hello, world!\"]}]}"
      }
    }
    

## View the details of an A2A agent

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



#### Example command and result
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890"
    
    
    * * *
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890",
      "displayName": "Hello World Agent",
      "description": "Just a hello world agent",
      "createTime": "2025-10-20T20:53:35.490600996Z",
      "state": "ENABLED",
      "a2aAgentDefinition": {
        "jsonAgentCard": "{\"name\":\"Hello World Agent\",\"description\":\"Just a hello world agent\",\"url\":\"https://example.com/myagent\",\"version\":\"1.0.0\",\"capabilities\":{},\"default_input_modes\":[\"text\"],\"default_output_modes\":[\"text\"],\"skills\":[{\"id\":\"chat\",\"name\":\"Chat Skill\",\"description\":\"Chat with the Gemini agent.\",\"tags\":[\"chat\"],\"examples\":[\"Hello, world!\"]}]}"
      }
    }
    

## Update an A2A agent

You can modify the details of an existing A2A agent registered with Gemini Enterprise using either the Google Cloud console or the REST API.

### Console

To update an A2A agent using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that includes the agent you want to update.

  3. Click **Agents**.

  4. Click the name of the **A2A (Custom)** agent to update, and then click **Edit**.

  5. In the **Agent card JSON** field, update the agent card details in JSON format. For a complete list of available fields, see the [Agent2Agent (A2A) Protocol Official Specification](https://a2a-protocol.org/latest/specification/). The following example only uses the required fields.

For example:
         
         {
           "protocolVersion": "0.3",
           "name": "Hello World Agent",
           "description": "Just a hello world agent",
           "url": "https://example.com/myagent",
           "iconUrl": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTkiIGhlaWdodD0iOTkiIHN0eWxlPSJiYWNrZ3JvdW5kLWNvbG9yOmdyYXk7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zMyAwaDMzdjMzSDMzeiBNMCAzM2gzM3YzM0gweiBNNjYgMzNoMzN2MzNINjZ6IE0zMyA2NmgzM3YzM0gzM3oiIGZpbGw9ImJsdWUiLz48L3N2Zz4=",
           "version": "1.1.0",
           "capabilities": {
           },
           "skills": [
             {
               "id": "data-analysis",
               "name": "Data Analysis",
               "description": "Data analysis",
               "tags": []
             }
           ],
           "defaultInputModes": [
             "text/plain"
           ],
           "defaultOutputModes": [
             "text/plain"
           ]
         }
         

  6. Click **Save**.




### REST

To update details of an A2A agent that is registered with Gemini Enterprise, use the [`agents.patch`](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.agents/patch) method. The following command uses only the required fields. For a complete list of available fields, see the [Agent2Agent (A2A) Protocol Official Specification](https://a2a-protocol.org/latest/specification/).

Run this command to update your A2A agent with Gemini Enterprise:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID \
    -d '
    {
      "name": "AGENT_NAME",
      "displayName": "AGENT_DISPLAY_NAME",
      "description": "AGENT_DESCRIPTION",
      "a2aAgentDefinition": {
        "jsonAgentCard": "{\"protocolVersion\":\"PROTOCOLVERSION\",\"name\":\"AGENT_NAME\",\"description\":\"AGENT_DESCRIPTION\",\"url\":\"AGENT_URL\",\"version\":\"AGENT_VERSION\",\"defaultInputModes\":[\"INPUT_MODE\"],\"defaultOutputModes\":[\"OUTPUT_MODE\"],\"capabilities\":{ CAPABILITIES },\"skills\":[SKILLS]}"
      },
      "authorizationConfig": {
        "agentAuthorization": "projects/PROJECT_ID/locations/LOCATION/authorizations/AUTH_ID"
      }
    }
    '
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`.
  * `PROJECT_ID`: the ID of your project.
  * `APP_ID`: the ID of the app that you want to register the agent.
  * AGENT_ID: the ID of the agent. You can find the agent ID by listing the agents connected to your app.
  * `AGENT_NAME`: the unique identifier for the agent.
  * `AGENT_DISPLAY_NAME`: the name of the agent that is displayed on the web app.
  * `AGENT_DESCRIPTION`: the description of what the agent can do.
  * `PROTOCOLVERSION`: the version of the A2A protocol that the agent supports. For more information on the supported versions, see the [A2A release notes](https://github.com/a2aproject/A2A/releases).
  * `AGENT_URL`: the endpoint URL of the agent.
  * `AGENT_VERSION`: the version of the agent.
  * `INPUT_MODE`: the default input media type. For example, `application/json` or `text/plain`.
  * `OUTPUT_MODE`: the default output media type. For example, `text/plain` or `image/png`.
  * `CAPABILITIES`: a JSON object containing supported A2A features. For example, `\"streaming\": true` or `\"pushNotifications\": false`.
  * `SKILLS`: a list of the [`AgentSkill` object](https://a2a-protocol.org/latest/specification/#554-agentskill-object) that the agent offers.
  * `authorizationConfig`: If you obtained the authorization details and want the agent to access Google Cloud resources on behalf of the user, add the `authorization_config` field to your JSON resource. 
    * `AUTH_ID`: the value that you used for AUTH_ID in the Add an authorization resource to Gemini Enterprise section.



#### Example command and result
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890 \
    -d '
    {
      "name": "Hello World Agent",
      "displayName": "Hello World Agent",
      "description": "Just a hello world agent",
      "a2aAgentDefinition": {
        "jsonAgentCard": "{\"protocolVersion\":\"0.3.0\",\"name\":\"Hello World Agent\",\"description\":\"Just a hello world agent\",\"url\":\"https://example.com/myagent\",\"version\":\"1.1.0\",\"defaultInputModes\":[\"text\"],\"defaultOutputModes\":[\"text\"],\"capabilities\":{  },\"skills\":[{\"description\":\"Chat with the Gemini agent.\",\"examples\":[\"Hello, world!\"],\"id\":\"chat\",\"name\":\"Chat Skill\",\"tags\":[\"chat\"]}]}"
      }
    }
    '
    
    
    * * *
    
    
    {
      "name": "projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890",
      "displayName": "Hello World Agent",
      "description": "Just a hello world agent",
      "createTime": "2025-10-20T20:53:35.490600996Z",
      "state": "ENABLED",
      "a2aAgentDefinition": {
        "jsonAgentCard": "{\"name\":\"Hello World Agent\",\"description\":\"Just a hello world agent\",\"url\":\"https://example.com/myagent\",\"version\":\"1.0.0\",\"capabilities\":{},\"defaultInputModes\":[\"text\"],\"defaultOutputModes\":[\"text\"],\"skills\":[{\"id\":\"chat\",\"name\":\"Chat Skill\",\"description\":\"Chat with the Gemini agent.\",\"tags\":[\"chat\"],\"examples\":[\"Hello, world!\"]}]}"
      }P
    }
    
    
    
    

## Delete an A2A agent

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
    

## What's next

  * Use the agent that you registered with Gemini Enterprise on the web app.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
