---
url: https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2/
title: Authenticate using API key with auth manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:23.351729+00:00
---

# Authenticate using API key with auth manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Authenticate using API key with auth manager Stay organized with collections  Save and categorize content based on your preferences. 

To let your agents authenticate to external tools like Google Maps or Weather APIs, configure outbound authentication using API key auth providers in Agent Identity auth manager.

API key auth providers manage your cryptographic keys for you. This capability removes the need to hardcode keys in your agent's code or manage them manually.

**Important:** This document shows how to authenticate by using the Agent Identity API. We recommend using the Agent Identity API because the [IAM Connectors API](https://docs.cloud.google.com/iam/docs/auth-with-api-key) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) will not be [generally available](https://docs.cloud.google.com/products#product-launch-stages). If you are using the IAM Connectors API, then [migrate to the Agent Identity API](https://docs.cloud.google.com/iam/docs/migrate-to-agent-identity-api).

## API key workflow

API key auth providers use the agent's identity and don't require user consent. Google takes measures to help secure the API key during storage. When you use the Agent Development Kit (ADK), it automatically retrieves and injects the API key into the tool invocation headers.

## Before you begin

  1. [Verify that you have chosen the correct authentication method](https://docs.cloud.google.com/iam/docs/agent-identity-overview#auth-models).
  2. Enable the Agent Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=agentidentity.googleapis.com)

  3. [Create and deploy an agent](https://docs.cloud.google.com/iam/docs/create-and-deploy-agent).

  4. Obtain an API key from the third-party service that you want to connect to.

  5. Verify that you have the roles required to complete this task.




### Required roles

To get the permissions that you need to create and use an API key auth provider, ask your administrator to grant you the following IAM roles on the project: 

  * To create auth providers: 
    * [Agent Identity Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)
    * [Agent Identity Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)
  * To use auth providers: 
    * [Agent Identity User ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.user) (`roles/agentidentity.user`)
    * [Vertex AI User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`)
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and use an API key auth provider. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and use an API key auth provider:

  * To create auth providers: `agentidentity.authProviders.create`
  * To use auth providers: 
    * `agentidentity.authProviders.retrieveCredentials`
    * `aiplatform.endpoints.predict`
    * `aiplatform.sessions.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Obtain an API key from the third-party service

Before you create an auth provider, obtain an API key from the third-party service that you want your agent to connect to.

If you are connecting to a third-party service outside of Google Cloud, obtain the API key from that service's developer portal and skip the steps in this section.

If you are connecting to Google Cloud services (such as Cloud Translation or Google Maps), you can generate and configure an API key by performing the following steps:

  1. In the Google Cloud console, enable the required API services for your project:

     1. In the Google Cloud console, go to the **APIs & Services >Library** page. 

[Go to APIs & Services >Library](https://console.cloud.google.com/apis/library)

     2. Search for and enable the APIs that your agent uses, such as the Cloud Translation API or the Google Maps Weather API.
     3. Copy your generated API key string.
  2. Configure your API key:

     1. In the Google Cloud console, go to the **APIs & Services >Credentials** page. 

[Go to APIs & Services >Credentials](https://console.cloud.google.com/apis/credentials)

     2. Click **Create credentials >API Key**.
     3. In the **Create API key** dialog, do the following: 
        1. Enter a unique name for your API key.
        2. To restrict the key to the specific APIs that you enabled, select those APIs from the **Select API restrictions** list.
        3. Optional: In the **Restrict your key to reduce security risks** section, select an application type to restrict access.
        4. Click **Create**.
  3. Validate your API key by sending a test request to the service endpoint.

     * To verify a Cloud Translation API key, run the following command:
           
           curl -X POST \
             -H "Content-Type: application/json" \
             -H "X-goog-api-key: YOUR_API_KEY" \
             -d '{"q": "Hello world", "target": "es"}' \
             "https://translation.googleapis.com/language/translate/v2"

Replace `YOUR_API_KEY` with the API key that you generated.

     * To verify a Google Maps Weather API key, run the following command:
           
           curl -X GET \
             "https://weather.googleapis.com/v1/currentConditions:lookup?key=YOUR_API_KEY&location.latitude=37.4220&location.longitude=-122.0841"

Replace `YOUR_API_KEY` with the API key that you generated.

If the API key is valid and configured correctly, the service returns the requested data.




## Create an API key auth provider

Create an auth provider to define the configuration and credentials for third-party applications.

To create an API key auth provider, use the Google Cloud console or the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Agent Registry** page. 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry/)

  2. Click the name of the agent that you want to create an auth provider for.
  3. Click **Identity**.
  4. In the **Auth Providers** section, click ** add  Add auth provider**.
  5. In the **Add auth provider** pane, enter a name and description.

The name can contain only lowercase letters, numbers, or hyphens, cannot end with a hyphen, and must start with a lowercase letter.

  6. From the **OAuth Type** list, select **API key** . 
  7. Click **Create and continue**.
  8. To grant your agent identity permission to use the auth provider, click **Grant access**. 

This process automatically assigns the **Agent Identity User** (`roles/agentidentity.user`) role to the agent identity on the auth provider resource.

  9. In the **Auth provider credentials** section, enter the **API key**.
  10. Click **Add provider config**.



The newly created auth provider appears in the **Auth Providers** list.

### gcloud CLI

  1. Create the auth provider:
         
         gcloud agent-identity auth-providers create AUTH_PROVIDER_NAME \
             --project="PROJECT_ID" \
             --location="LOCATION" \
             --api-key="API_KEY"

  2. Verify that your auth provider appears in the list and its state is `ENABLED`: 
         
         gcloud agent-identity auth-providers list \
            --project="PROJECT_ID" \
            --location="LOCATION"

  3. Grant access permissions to allow your agent and local development environment to retrieve credentials from the auth provider. To allow your deployed agent and your personal user account to access the auth provider, grant the **Agent Identity User** (`roles/agentidentity.user`) role on the auth provider resource:

     1. Grant access to your deployed agent's SPIFFE ID (Agent Identity):
            
            gcloud agent-identity auth-providers add-iam-policy-binding AUTH_PROVIDER_NAME \
                --project="PROJECT_ID" \
                --location="LOCATION" \
                --role="roles/agentidentity.user" \
                --member="principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/ENGINE_ID"

     2. Grant access to your personal user account for local development and testing (`adk web`):
            
            gcloud agent-identity auth-providers add-iam-policy-binding AUTH_PROVIDER_NAME \
                --project="PROJECT_ID" \
                --location="LOCATION" \
                --role="roles/agentidentity.user" \
                --member="user:USER_EMAIL"




Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location where your auth provider and agent are deployed (for example, `us-west1`).
  * `AUTH_PROVIDER_NAME`: The name for your auth provider (for example, `maps-api-key-authprovider`).
  * `API_KEY`: The API key you generated from the third-party service.
  * `ORGANIZATION_ID`: Your Google Cloud organization ID.
  * `PROJECT_NUMBER`: Your Google Cloud project number.
  * `ENGINE_ID`: The ID of your deployed reasoning engine agent.
  * `USER_EMAIL`: Your personal user account email address.



## Authenticate in your agent code

To authenticate your agent, you can use the ADK.

**Note:** The following samples register the auth provider at the module level, which works when you run the agent locally or deploy it with the Agent CLI. If you deploy with the Vertex AI Python SDK, register the auth provider in `set_up()` instead so that it runs in the deployed container. For more information, see Deploy the agent. 

### ADK

Reference the auth provider in your agent's code using the MCP toolset in the ADK.
    
    
    from google.adk.agents import Agent
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider, GcpAuthProviderScheme
    from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
    from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
    from google.adk.auth.auth_tool import AuthConfig
    
    # Register Google Cloud auth provider
    CredentialManager.register_auth_provider(GcpAuthProvider())
    
    # Create Google Cloud auth provider scheme
    # Note: If using the legacy V1 API, the resource name uses 'connectors'
    # instead of 'authProviders': projects/.../connectors/...
    auth_scheme = GcpAuthProviderScheme(
        name="projects/PROJECT_ID/locations/LOCATION/authProviders/AUTH_PROVIDER_NAME"
    )
    
    # Configure an MCP tool with the authentication scheme.
    toolset = McpToolset(
        connection_params=StreamableHTTPConnectionParams(url="https://YOUR_MCP_SERVER_URL"),
        auth_scheme=auth_scheme,
    )
    
    # Initialize the agent with the authenticated tools.
    agent = Agent(
        name="AGENT_NAME",
        model="gemini-2.5-flash",
        instruction="AGENT_INSTRUCTIONS",
        tools=[toolset],
    )

#### Example: Connecting to Google Maps MCP

The following example demonstrates an `agent.py` configuration that connects an agent to a Google Maps MCP server:
    
    
    import os
    from google.adk.agents import Agent
    from google.adk.apps import App
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider, GcpAuthProviderScheme
    from google.adk.models import Gemini
    from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
    from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
    
    os.environ["GOOGLE_CLOUD_PROJECT"] = "PROJECT_ID"
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
    os.environ["GOOGLE_API_USE_CLIENT_CERTIFICATE"] = "false"
    
    # Register Google Cloud auth provider for Agent Identity Credentials service
    CredentialManager.register_auth_provider(GcpAuthProvider())
    
    maps_auth_scheme = GcpAuthProviderScheme(
        name="projects/PROJECT_ID/locations/LOCATION/authProviders/AUTH_PROVIDER_NAME"
    )
    
    maps_tools = McpToolset(
        connection_params=StreamableHTTPConnectionParams(url="https://mapstools.googleapis.com/mcp"),
        auth_scheme=maps_auth_scheme,
        errlog=None,
    )
    
    root_agent = Agent(
        name="root_agent",
        model=Gemini(model="gemini-2.5-flash"),
        instruction=(
            "You are a helpful AI assistant designed to provide accurate and useful "
            "information. You can also use your Google Maps tools to look up "
            "locations and directions."
        ),
        tools=[maps_tools],
    )
    
    app = App(
        root_agent=root_agent,
        name="AGENT_NAME",
    )

### ADK

Reference the auth provider in your agent's code using an authenticated function tool in the ADK.
    
    
    import httpx
    from google.adk.agents import Agent
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider
    from google.adk.integrations.agent_identity import GcpAuthProviderScheme
    from google.adk.apps import App
    from google.adk.auth.auth_credential import AuthCredential
    from google.adk.auth.auth_tool import AuthConfig
    from google.adk.tools.authenticated_function_tool import AuthenticatedFunctionTool
    from vertexai import agent_engines
    
    # First, register Google Cloud auth provider
    CredentialManager.register_auth_provider(GcpAuthProvider())
    
    # Create Auth Config
    # Note: If using the legacy V1 API, the resource name uses 'connectors'
    # instead of 'authProviders': projects/.../connectors/...
    spotify_auth_config = AuthConfig(
        auth_scheme=GcpAuthProviderScheme(
            name="projects/PROJECT_ID/locations/LOCATION/authProviders/AUTH_PROVIDER_NAME"
        )
    )
    
    # Use the Auth Config in Authenticated Function Tool
    spotify_search_track_tool = AuthenticatedFunctionTool(
        func=spotify_search_track, auth_config=spotify_auth_config
    )
    
    # Sample function tool
    async def spotify_search_track(credential: AuthCredential, query: str) -> str | list:
        token = None
        if credential.http and credential.http.credentials:
            token = credential.http.credentials.token
    
        if not token:
            return "Error: No authentication token available."
    
        async with httpx.AsyncClient() as client:
            response = await client.[get](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(
                "https://api.spotify.com/v1/search",
                headers={"Authorization": f"Bearer {token}"},
                params={"q": query, "type": "track", "limit": 1},
            )
            # Add your own logic here
    
    agent = Agent(
        name="AGENT_NAME",
        model="gemini-2.5-flash",
        instruction="AGENT_INSTRUCTIONS",
        tools=[spotify_search_track_tool],
    )
    
    app = App(
        name="APP_NAME",
        root_agent=agent,
    )
    
    vertex_app = agent_engines.AdkApp(app_name=app)

#### Example: Connecting to Google Maps Weather API

The following example demonstrates an `agent.py` configuration that connects an agent to the Google Maps Weather API using an authenticated function tool:
    
    
    import os
    import httpx
    from google.adk.agents import Agent
    from google.adk.apps import App
    from google.adk.auth.auth_credential import AuthCredential
    from google.adk.auth.auth_tool import AuthConfig
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider, GcpAuthProviderScheme
    from google.adk.models import Gemini
    from google.adk.tools.authenticated_function_tool import AuthenticatedFunctionTool
    
    os.environ["GOOGLE_CLOUD_PROJECT"] = "PROJECT_ID"
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
    os.environ["GOOGLE_API_USE_CLIENT_CERTIFICATE"] = "false"
    
    # Register Google Cloud auth provider for Agent Identity Credentials service
    CredentialManager.register_auth_provider(GcpAuthProvider())
    
    weather_auth_config = AuthConfig(
        auth_scheme=GcpAuthProviderScheme(
            name="projects/PROJECT_ID/locations/LOCATION/authProviders/AUTH_PROVIDER_NAME"
        )
    )
    
    async def get_weather(credential: AuthCredential, latitude: float, longitude: float) -> str | dict:
        """Gets current weather conditions for a location."""
        api_key = None
        if http := credential.http:
            if http.additional_headers and "X-GOOG-API-KEY" in http.additional_headers:
                api_key = http.additional_headers["X-GOOG-API-KEY"]
            elif http.credentials and http.credentials.token:
                api_key = http.credentials.token
    
        if not api_key:
            return "Error: No API key available from the auth provider."
    
        params = {"location.latitude": latitude, "location.longitude": longitude, "key": api_key}
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://weather.googleapis.com/v1/currentConditions:lookup",
                params=params,
            )
            if response.status_code != 200:
                return f"Error from Weather API: {response.status_code} - {response.text}"
            return response.json()
    
    get_weather_tool = AuthenticatedFunctionTool(
        func=get_weather, auth_config=weather_auth_config
    )
    
    root_agent = Agent(
        name="root_agent",
        model=Gemini(model="gemini-2.5-flash"),
        instruction=(
            "You are a helpful AI assistant. You will use your weather tool to "
            "look up current conditions."
        ),
        tools=[get_weather_tool],
    )
    
    app = App(
        root_agent=root_agent,
        name="AGENT_NAME",
    )

### ADK

Reference the auth provider in your agent's code using the Agent Registry MCP toolset in the ADK.

You don't construct an auth scheme for this flow. The MCP server's outbound binding already records which auth provider to use.

**Caution:** Use the same region for the auth provider, the MCP server, and the Agent Registry client. Auth providers aren't available in the `global` location, so if you set `location="global"`, creating the outbound binding fails with the error `Location of auth provider does not match location of binding`. 
    
    
    from google.adk.agents import Agent
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider
    from google.adk.integrations.agent_registry import AgentRegistry
    
    # First, register Google Cloud auth provider
    CredentialManager.register_auth_provider(GcpAuthProvider())
    
    # Set Agent Registry. LOCATION must be the same region as the auth provider.
    registry = AgentRegistry(project_id="PROJECT_ID", location="LOCATION")
    
    # The auth provider is resolved from the MCP server's outbound binding.
    toolset = registry.get_mcp_toolset(
        mcp_server_name=(
            "projects/PROJECT_ID/locations/"
            "LOCATION/mcpServers/"
            "agentregistry-00000000-0000-0000-0000-000000000000"
        ),
    )
    
    agent = Agent(
        name="AGENT_NAME",
        model="MODEL_NAME",
        instruction="AGENT_INSTRUCTIONS",
        tools=[toolset],
    )
    
      

## Deploy the agent

When you deploy your agent to Google Cloud, ensure that Agent Identity is enabled.

### Agent CLI

If you're using the Agent Development Kit (ADK) and the Agent CLI, do the following to deploy your agent with Agent Identity enabled:

  1. In your agent application folder, create a configuration file named `.agent_engine_config.json` to enable Agent Identity:
         
         echo '{ "identity_type": "AGENT_IDENTITY" }' > AGENT_NAME/.agent_engine_config.json

  2. Deploy your agent to Agent Runtime on Gemini Enterprise Agent Platform :
         
         uv run adk deploy agent_engine AGENT_NAME \
             --project="PROJECT_ID" \
             --region="LOCATION"

Replace the following:

     * `AGENT_NAME`: The name of your agent application folder (for example, `maps_agent`).
     * `PROJECT_ID`: Your Google Cloud project ID.
     * `LOCATION`: The supported region where you want to deploy the agent (for example, `us-west1`).



### Python SDK

If you're deploying programmatically using the Vertex AI Python SDK, use the `identity_type=AGENT_IDENTITY` flag:

**Caution:** The SDK serializes your app object, so the `CredentialManager.register_auth_provider()` call that your local script runs at import time doesn't run in the deployed container. Instead, register the auth provider in your app's `set_up()` method, which the runtime calls when the container starts. Otherwise, the agent fails at query time with `No auth provider registered for custom auth scheme 'gcpAuthProviderScheme'`. For more information, see [Deployment considerations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-a-custom-agent#deployment-considerations). 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai import [types](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.html)
    from vertexai.agent_engines import [AdkApp](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.AdkApp.html)
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider
    
    # Initialize the Vertex AI client with v1beta1 API for Agent Identity support
    client = [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).Client(
        project="PROJECT_ID",
        location="LOCATION",
        http_options=dict(api_version="v1beta1")
    )
    
    # Register the auth provider in set_up() so that it runs in the deployed
    # container. Use the proper wrapper class for your Agent Framework (for example, AdkApp).
    class AuthenticatedAdkApp(AdkApp):
        def set_up(self):
            CredentialManager.register_auth_provider(GcpAuthProvider())
            super().set_up()
    
    app = AuthenticatedAdkApp(agent=agent)
    
    # Deploy the agent with Agent Identity enabled
    remote_app = client.[agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).create(
        agent=app,
        config={
            "identity_type": [types](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.html).[IdentityType](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.IdentityType.html).[AGENT_IDENTITY](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.IdentityType.html#vertexai__genai_types_IdentityType_AGENT_IDENTITY),
            "requirements": [
                "google-cloud-aiplatform[agent_engines,adk]",
                "google-adk[agent-identity,mcp]>=2.7.1",
            ],
        },
    )

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The supported region where you want to deploy the agent (for example, `us-west1`).



## What's next

  * [Troubleshoot Agent Identity authentication issues](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager)
  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
  * [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)
  * [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2)
  * [Manage Agent Identity auth providers](https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
