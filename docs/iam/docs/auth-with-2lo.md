---
url: https://docs.cloud.google.com/iam/docs/auth-with-2lo/
title: Authenticate using 2-legged OAuth with auth manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:42.197310+00:00
---

# Authenticate using 2-legged OAuth with auth manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/auth-with-2lo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)



Send feedback 

#  Authenticate using 2-legged OAuth with auth manager Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To let your agents authenticate to external tools like ServiceNow or Salesforce using their own authority, configure outbound authentication using 2-legged OAuth (Client Credentials) auth providers in Agent Identity auth manager.

2-legged OAuth auth providers manage credentials and tokens for you. This removes the need to write custom code to handle authentication flows.

**Warning:** This document shows how to authenticate by using the IAM Connectors API, which will not be [generally available](https://docs.cloud.google.com/products#product-launch-stages). For new projects, we recommend using the [Agent Identity API](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2). For existing projects, [migrate to the Agent Identity API](https://docs.cloud.google.com/iam/docs/migrate-to-agent-identity-api). 

## 2-legged OAuth workflow

2-legged OAuth auth providers use the agent's identity and don't require user consent. Google manages the storage of the client credentials. When you use the Agent Development Kit (ADK), it automatically retrieves and injects the resulting access tokens into the tool invocation headers.

## Before you begin

  1. [Verify that you have chosen the correct authentication method](https://docs.cloud.google.com/iam/docs/agent-identity-overview#auth-models).
  2. Enable the Agent Identity Connector API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iamconnectors.googleapis.com)

  3. [Create and deploy an agent](https://docs.cloud.google.com/iam/docs/create-and-deploy-agent).

  4. Obtain the **client ID** and **client secret** from the third-party application that you want to connect to.

  5. Verify that you have the roles required to complete this task.




### Required roles

To get the permissions that you need to create and use a 2-legged Agent Identity auth provider, ask your administrator to grant you the following IAM roles on the project: 

  * To create auth providers: 
    * [IAM Connector Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)
    * [IAM Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)
  * To use auth providers: 
    * [IAM Connector User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.user) (`roles/iamconnectors.user`)
    * [Agent Default Access ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.agentDefaultAccess) (`roles/aiplatform.agentDefaultAccess`)
    * [Agent Context Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.agentContextEditor) (`roles/aiplatform.agentContextEditor`)
    * [Vertex AI User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`)
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and use a 2-legged Agent Identity auth provider. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and use a 2-legged Agent Identity auth provider:

  * To create auth providers: `iamconnectors.connectors.create`
  * To use auth providers: 
    * `iamconnectors.connectors.retrieveCredentials`
    * `aiplatform.endpoints.predict`
    * `aiplatform.sessions.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a 2-legged auth provider

Create an auth provider to define the configuration and credentials for third-party applications.

To create a 2-legged auth provider, use the Google Cloud console or the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Agent Registry** page. 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry/)

  2. Click the name of the agent that you want to create an auth provider for.
  3. Click **Identity**.
  4. In the **Auth Providers** section, click ** add  Add auth provider**.
  5. In the **Add auth provider** pane, enter a name and description.

The name can contain only lowercase letters, numbers, or hyphens, cannot end with a hyphen, and must start with a lowercase letter.

  6. From the **OAuth Type** list, select **OAuth (2 legged)** . 
  7. Click **Create and continue**.
  8. To grant your agent identity permission to use the auth provider, click **Grant access**. 

This automatically assigns the **Connector User** (`roles/iamconnectors.user`) role to the agent identity on the auth provider resource.

  9. In the **Auth provider credentials** section, enter the following information: 
     * **Client ID**
     * **Client Secret**
     * **Token URL**
  10. Click **Add provider config**.



The newly created auth provider appears in the **Auth Providers** list.

### gcloud CLI

  1. Create the auth provider:
         
         gcloud alpha agent-identity connectors create AUTH_PROVIDER_NAME \
             --location="LOCATION" \
             --two-legged-oauth-client-id="CLIENT_ID" \
             --two-legged-oauth-client-secret="CLIENT_SECRET" \
             --two-legged-oauth-token-endpoint="TOKEN_ENDPOINT"

  2. Verify that your auth provider appears in the list and its state is `ENABLED`: 
         
         gcloud alpha agent-identity connectors list \
            --project="PROJECT_ID" \
            --location="LOCATION"

  3. Grant access permissions to allow your agent and local development environment to retrieve credentials from the auth provider. To allow your deployed agent and your personal user account to access the auth provider, grant the **Connector User** (`roles/iamconnectors.user`) role on the auth provider resource:

     1. Grant access to your deployed agent's SPIFFE ID (Agent Identity):
            
            gcloud alpha agent-identity connectors add-iam-policy-binding AUTH_PROVIDER_NAME \
                --project="PROJECT_ID" \
                --location="LOCATION" \
                --role="roles/iamconnectors.user" \
                --member="principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/ENGINE_ID"

     2. Grant access to your personal user account for local development and testing (`adk web`):
            
            gcloud alpha agent-identity connectors add-iam-policy-binding AUTH_PROVIDER_NAME \
                --project="PROJECT_ID" \
                --location="LOCATION" \
                --role="roles/iamconnectors.user" \
                --member="user:USER_EMAIL"




Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location where your auth provider and agent are deployed (for example, `us-west1`).
  * `AUTH_PROVIDER_NAME`: The name for your auth provider (for example, `jira-mcp-2lo-authprovider`).
  * `CLIENT_ID`: The OAuth client ID you generated from the third-party service.
  * `CLIENT_SECRET`: The OAuth client secret you generated from the third-party service.
  * `TOKEN_ENDPOINT`: The token endpoint URL (for example, `https://oauth2.googleapis.com/token`).
  * `ORGANIZATION_ID`: Your Google Cloud organization ID.
  * `PROJECT_NUMBER`: Your Google Cloud project number.
  * `ENGINE_ID`: The ID of your deployed reasoning engine agent.
  * `USER_EMAIL`: Your personal user account email address.



## Authenticate in your agent code

To authenticate your agent, you can use the ADK.

### ADK

Reference the auth provider in your agent's code by using the MCP toolset in the ADK.
    
    
    from google.adk.agents.llm_agent import LlmAgent
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider, GcpAuthProviderScheme
    from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
    from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
    from google.adk.auth.auth_tool import AuthConfig
    
    # Register the Google Cloud Auth Provider so the CredentialManager can use it.
    CredentialManager.register_auth_provider(GcpAuthProvider())
    
    # Create the Google Cloud Auth Provider scheme using the auth provider's full resource name.
    auth_scheme = GcpAuthProviderScheme(
        name="projects/PROJECT_ID/locations/LOCATION/connectors/AUTH_PROVIDER_NAME"
    )
    
    # Configure an MCP tool with the authentication scheme.
    toolset = McpToolset(
        connection_params=StreamableHTTPConnectionParams(url="https://YOUR_MCP_SERVER_URL"),
        auth_scheme=auth_scheme,
    )
    
    # Initialize the agent with the authenticated tools.
    agent = LlmAgent(
        name="AGENT_NAME",
        model="gemini-2.5-flash",
        instruction="AGENT_INSTRUCTIONS",
        tools=[toolset],
    )

### ADK

Reference the auth provider in your agent's code using an authenticated function tool in the ADK.
    
    
    import httpx
    from google.adk.agents.llm_agent import LlmAgent
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
    spotify_auth_config = AuthConfig(
        auth_scheme=GcpAuthProviderScheme(
            name=(
                "projects/PROJECT_ID/locations/"
                "LOCATION/connectors/"
                "AUTH_PROVIDER_NAME"
            )
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
    
    agent = LlmAgent(
        name="AGENT_NAME",
        model="MODEL_NAME",
        instruction="AGENT_INSTRUCTIONS",
        tools=[spotify_search_track_tool],
    )
    
    app = App(
        name="APP_NAME",
        root_agent=agent,
    )
    
    vertex_app = agent_engines.AdkApp(app_name=app)

### ADK

Reference the auth provider in your agent's code using the Agent Registry MCP toolset in the ADK.
    
    
      from google.adk.agents.llm_agent import LlmAgent
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider
    from google.adk.integrations.agent_identity import GcpAuthProviderScheme
    from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
    from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
    from google.adk.auth.auth_tool import AuthConfig
    from google.adk.integrations.agent_registry import AgentRegistry
    
    # First, register Google Cloud auth provider
    CredentialManager.register_auth_provider(GcpAuthProvider())
    
    # Create Google Cloud auth provider scheme by providing Auth Provider full resource name
    auth_scheme = GcpAuthProviderScheme(
        name=(
            "projects/PROJECT_ID/locations/"
            "LOCATION/connectors/"
            "AUTH_PROVIDER_NAME"
        )
    )
    
    # Set Agent Registry
    registry = AgentRegistry(project_id="PROJECT_ID", location="global")
    
    toolset = registry.get_mcp_toolset(
        mcp_server_name=(
            "projects/PROJECT_ID/locations/"
            "global/mcpServers/"
            "agentregistry-00000000-0000-0000-0000-000000000000"
        ),
        auth_scheme=auth_scheme,
    )
    
    # Example MCP tool
    toolset = McpToolset(
        connection_params=StreamableHTTPConnectionParams(url="MCP_URL"),
        auth_scheme=auth_scheme,
    )
    
    agent = LlmAgent(
        name="AGENT_NAME",
        model="MODEL_NAME",
        instruction="AGENT_INSTRUCTIONS",
        tools=[toolset],
    )
    
      

## Install dependencies for local testing

To test your agent locally in a virtual environment, install the following necessary dependencies:

  1. Create and activate a virtual environment: 
         
         python3 -m venv env
         source env/bin/activate

  2. Install the required packages: 
         
         pip install google-cloud-aiplatform[agent_engines,adk] google-adk[agent-identity]




## Deploy the agent

When you deploy your agent to Google Cloud, make sure that Agent Identity is enabled.

If you're deploying to Agent Runtime on Gemini Enterprise Agent Platform , use the `identity_type=AGENT_IDENTITY` flag:
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai import [types](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.html)
    from vertexai.agent_engines import [AdkApp](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.AdkApp.html)
    
    # Initialize the Vertex AI client with v1beta1 API for Agent Identity support
    client = [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).Client(
        project="PROJECT_ID",
        location="LOCATION",
        http_options=dict(api_version="v1beta1")
    )
    
    # Use the proper wrapper class for your Agent Framework (e.g., AdkApp)
    app = AdkApp(agent=agent)
    
    # Deploy the agent with Agent Identity enabled
    remote_app = client.[agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).create(
        agent=app,
        config={
            "identity_type": [types](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.html).[IdentityType](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.IdentityType.html).[AGENT_IDENTITY](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.IdentityType.html#vertexai__genai_types_IdentityType_AGENT_IDENTITY),
            "requirements": ["google-cloud-aiplatform[agent_engines,adk]", "google-adk[agent-identity]"],
        },
    )
    

## What's next

  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
  * [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo)
  * [Authenticate using API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key)
  * [Manage Agent Identity auth providers](https://docs.cloud.google.com/iam/docs/manage-auth-providers)
  * [Troubleshoot Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
