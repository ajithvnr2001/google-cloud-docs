---
url: https://docs.cloud.google.com/agent-registry/authenticate-toolsets/
title: Authenticate to tools and resources \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:23.284995+00:00
---

# Authenticate to tools and resources  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/authenticate-toolsets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Authenticate to tools and resources Stay organized with collections  Save and categorize content based on your preferences. 

When an orchestrator agent invokes a remote agent or Model Context Protocol (MCP) toolset discovered through Agent Registry, it must authenticate with the underlying Google Cloud service providing those capabilities.

This document describes how to handle authentication for Agent Registry resources.

## Before you begin

Before you authenticate to tools and resources, complete the following:

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) in your project.
  2. Install or upgrade to the latest version of the Agent Development Kit (ADK) with the A2A, Agent Identity, and MCP dependencies:

###  pip 
         
         pip install --upgrade "google-adk[a2a,agent-identity,mcp]"
         

###  uv 
         
         uv add "google-adk[a2a,agent-identity,mcp]"
         

You must upgrade to at least `google-adk>=1.29.0`.

  3. To use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for authentication, configure them:
         
         gcloud auth application-default login
         

ADC credentials must have the necessary Identity and Access Management (IAM) permissions for the underlying Google Cloud services the agents or tools interact with.

  4. To follow the examples in this guide, you must set up environment variables, for example:
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID
         export GOOGLE_CLOUD_LOCATION=LOCATION
         export API_KEY=EXTERNAL_API_KEY
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `LOCATION`: the registry region or location, such as `us-central1`
     * `EXTERNAL_API_KEY`: if using custom headers, your external API key



## Learn about authentication models

To manage credentials, Agent Registry relies on [Agent Identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview) for built-in Google Cloud authentication and [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager) for [auth providers](https://docs.cloud.google.com/agent-registry/concepts#auth-provider) and [bindings](https://docs.cloud.google.com/agent-registry/concepts#binding).

Your agents can use their own identity or use the auth manager to access tools using API keys or OAuth. The agent's own identity is provided through [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) whether you are using Agent Identity or [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

Alternatively, to send advanced context to a target agent, or if external toolsets don't support Agent Identity auth manager, you can provide custom HTTP headers directly in your ADK requests.

To determine the best approach for your use case, see [Authentication models](https://docs.cloud.google.com/iam/docs/agent-identity-overview#auth-models).

## Use Agent Identity for Google Cloud tools

For Google Cloud services, such as Agent Runtime on Gemini Enterprise Agent Platform or Cloud Storage, [your agent uses its own identity](https://docs.cloud.google.com/iam/docs/auth-agent-own-identity) to access the tools. This access is managed through [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) whether you are using [Agent Identity API](https://docs.cloud.google.com/iam/docs/agent-identity-overview) or [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

The identity associated with your agent must have the necessary IAM permissions for the underlying Google Cloud services. For example, if an MCP tool manages Compute Engine VM instances, the agent identity must have roles such as [Compute Instance Admin (v1) or higher](https://docs.cloud.google.com/compute/docs/use-compute-engine-mcp#before-you-begin), in addition to the [Agent Registry API Viewer role](https://docs.cloud.google.com/agent-registry/roles-permissions).

### Authenticate remote A2A agents

If your orchestrator agent is connecting to a remote Google Agent2Agent (A2A) agent using its own identity, you must explicitly include `httpx.AsyncClient` configured with your Google authentication headers to the `get_remote_a2a_agent()` method.

We recommend defining a custom timeout to prevent exceeding the default HTTP client timeout limits.

The following example shows how to configure the `httpx.AsyncClient` with ADC and a custom timeout:
    
    
    import os
    import httpx
    import google.auth
    from google.auth.transport.requests import Request
    from google.adk.integrations.agent_registry import AgentRegistry
    
    class GoogleAuth(httpx.Auth):
        def __init__(self):
            self.creds, _ = google.auth.default()
        def auth_flow(self, request):
            if not self.creds.valid:
                self.creds.refresh(Request())
            request.headers["Authorization"] = f"Bearer {self.creds.token}"
            yield request
    
    # Initialize the registry client
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
    
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable not set.")
    
    registry = AgentRegistry(
        project_id=project_id,
        location=location,
    )
    
    # Configure the HTTP client with GoogleAuth and a 60-second timeout
    httpx_client = httpx.AsyncClient(auth=GoogleAuth(), timeout=httpx.Timeout(60.0))
    
    # Connect to a remote A2A agent using its resource name in short or full format
    # Short formats automatically imply the client's configured project and location
    # Short format: "agents/AGENT_ID"
    # Full format: f"projects/{project_id}/locations/{location}/agents/AGENT_ID"
    agent_name = "agents/AGENT_ID"
    my_remote_agent = registry.get_remote_a2a_agent(
        agent_name=agent_name,
        httpx_client=httpx_client,
    )
    

### Authenticate MCP tools

If your orchestrator agent uses its own identity to access an MCP toolset, you can initialize the registry client using your ADC and the `get_mcp_toolset()` method:
    
    
    import os
    import httpx
    import google.auth
    from google.auth.transport.requests import Request
    from google.adk.integrations.agent_registry import AgentRegistry
    
    class GoogleAuth(httpx.Auth):
        def __init__(self):
            self.creds, _ = google.auth.default()
        def auth_flow(self, request):
            if not self.creds.valid:
                self.creds.refresh(Request())
            request.headers["Authorization"] = f"Bearer {self.creds.token}"
            yield request
    
    # Initialize the registry client
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
    
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable not set.")
    
    registry = AgentRegistry(
        project_id=project_id,
        location=location,
    )
    
    # Retrieve an MCP toolset using its resource name in short or full format
    # Short formats automatically imply the client's configured project and location
    # Short format: "mcpServers/SERVER_ID"
    # Full format: f"projects/{project_id}/locations/{location}/mcpServers/SERVER_ID"
    mcp_server_name = "mcpServers/SERVER_ID"
    my_mcp_toolset = registry.get_mcp_toolset(mcp_server_name=mcp_server_name)
    

## Use the auth manager for custom tools and delegated access

When your agent needs to connect to external APIs, custom tools, or external MCP servers, you can use [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager) to manage credentials without hardcoding them in your application.

Depending on your use case, you can configure the auth manager for the following scenarios:

  * **Access custom tools**: Authenticate the agent with [API keys](https://docs.cloud.google.com/iam/docs/auth-with-api-key) or [2-legged OAuth (2LO)](https://docs.cloud.google.com/iam/docs/auth-with-2lo) when the agent needs to access a tool using its own identity and permissions.
  * **Access tools on behalf of a user**: Authenticate the agent acting as an individual user with [3-legged OAuth (3LO)](https://docs.cloud.google.com/iam/docs/auth-with-3lo). This model is recommended when the agent must access tools on behalf of the person interacting with it, requiring user consent and delegated permission.



These models require you to create an [auth provider](https://docs.cloud.google.com/agent-registry/concepts#auth-provider). Then, you create a [binding](https://docs.cloud.google.com/agent-registry/concepts#binding) in Agent Registry to link the auth provider to your registry resources.

After configuring the auth provider, the ADK manages the authentication flow for your orchestrator. For an example, see Resolve bindings in your ADK code.

### Access custom tools

If you want your agent to connect to external or custom tools using its own credentials, you can configure Agent Identity auth manager to handle API keys or 2-legged OAuth (2LO):

  1. **Create the auth provider:** Create an auth provider in Agent Identity auth manager to store the API key or OAuth credentials. For information, see [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo) or [Authenticate using an API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key).
  2. **Bind the auth provider:** To let your orchestrator agent detect the correct auth provider for a target, you must create a [binding](https://docs.cloud.google.com/agent-registry/concepts#binding) in Agent Registry between your agent and the auth provider. With bindings, you don't have to manually define auth providers in your code.

###  gcloud 

Create a binding to explicitly link your agent to the auth provider. When specifying the `--auth-provider` resource name, you must use your project ID:
         
         gcloud agent-registry bindings create BINDING_NAME \
         --project=PROJECT_ID \
         --location=LOCATION \
         --display-name="DISPLAY_NAME" \
         --source-identifier="SOURCE_ID" \
         --target-identifier="TARGET_ID" \
         --auth-provider="projects/PROJECT_ID/locations/LOCATION/authProviders/AUTH_PROVIDER_ID"
         

###  Terraform 

Configure the `google_agent_registry_binding` resource to link your agent and target resource to the auth provider:
         
         resource "google_agent_registry_binding" "custom_tool_binding" {
           project      = "PROJECT_ID"
           location     = "LOCATION"
           binding_id   = "BINDING_NAME"
           display_name = "DISPLAY_NAME"
         
           source {
             identifier = "SOURCE_ID"
           }
         
           target {
             identifier = "TARGET_ID"
           }
         
           auth_provider_binding {
             auth_provider = "projects/PROJECT_ID/locations/LOCATION/authProviders/AUTH_PROVIDER_ID"
           }
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `LOCATION`: the registry region or location, such as `us-central1` or `global`
     * `BINDING_NAME`: the unique ID for the binding
     * `DISPLAY_NAME`: a human-readable display name for the binding
     * `SOURCE_ID`: the identifier of the source agent in URN format
     * `TARGET_ID`: the identifier of the target MCP server or endpoint in URN format
     * `AUTH_PROVIDER_ID`: the ID of your auth provider

For more information about managing these connections, see [Manage bindings](https://docs.cloud.google.com/agent-registry/manage-bindings).




### Access tools on behalf of a user

If you want your agent to authenticate to remote MCP servers or tools on behalf of an individual user, use 3-legged OAuth (3LO) through Agent Identity auth manager.

The auth manager provides a fully Google-managed service for handling OAuth tokens, user consent, and redirects. When you interact with the agent and trigger a tool that requires delegated permissions, the platform automatically prompts the user for consent, stores the credentials, and resumes the workflow:

  1. **Create the auth provider:** Create an auth provider in Agent Identity auth manager and configure your OAuth redirect URIs. For information, see [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo).
  2. **Update the client application:** Update your application client to handle the `adk_request_credential` function call and manage the user consent. For detailed instructions, see [Update your client-side application](https://docs.cloud.google.com/iam/docs/auth-with-3lo#update-client).
  3. **Bind the auth provider:** To let your orchestrator agent detect the correct auth provider for a target, you must create a [binding](https://docs.cloud.google.com/agent-registry/concepts#binding) in Agent Registry between your agent and the auth provider. With bindings, you don't have to manually define auth providers in your code.

###  gcloud 

Create a binding to explicitly link your agent to the auth provider. When specifying the `--auth-provider` resource name, you must use your project ID:
         
         gcloud agent-registry bindings create BINDING_NAME \
         --project=PROJECT_ID \
         --location=LOCATION \
         --display-name="DISPLAY_NAME" \
         --source-identifier="SOURCE_ID" \
         --target-identifier="TARGET_ID" \
         --auth-provider="projects/PROJECT_ID/locations/LOCATION/authProviders/AUTH_PROVIDER_ID"
         

###  Terraform 

Configure the `google_agent_registry_binding` resource with your OAuth scopes and continue URI:
         
         resource "google_agent_registry_binding" "user_delegated_binding" {
           project      = "PROJECT_ID"
           location     = "LOCATION"
           binding_id   = "BINDING_NAME"
           display_name = "DISPLAY_NAME"
         
           source {
             identifier = "SOURCE_ID"
           }
         
           target {
             identifier = "TARGET_ID"
           }
         
           auth_provider_binding {
             auth_provider = "projects/PROJECT_ID/locations/LOCATION/authProviders/AUTH_PROVIDER_ID"
             scopes        = [SCOPES]
             continue_uri  = "https://REDIRECT_URI"
           }
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `LOCATION`: the registry region or location, such as `us-central1` or `global`
     * `BINDING_NAME`: the unique ID for the binding
     * `DISPLAY_NAME`: a human-readable display name for the binding
     * `SOURCE_ID`: the identifier of the source agent in URN format
     * `TARGET_ID`: the identifier of the target MCP server or tool resource in URN format
     * `AUTH_PROVIDER_ID`: the ID of your auth provider
     * `SCOPES`: a comma-separated list of quoted OAuth 2.0 scopes, such as `"https://www.googleapis.com/auth/cloud-platform"`
     * `REDIRECT_URI`: the redirect URI configured for your auth provider after user consent

For more information about managing these connections, see [Manage bindings](https://docs.cloud.google.com/agent-registry/manage-bindings).




### Resolve bindings in your ADK code

After you create the auth provider binding in Agent Registry, the ADK handles the authentication flow.

When you use the `AgentRegistry` client to fetch an MCP toolset, the ADK automatically resolves any bindings associated with that server and applies the correct scheme. You don't need to manually configure credentials in your code.

The following example demonstrates how to fetch an authenticated MCP toolset and attach it to an agent:
    
    
    import os
    from google.adk.agents.llm_agent import LlmAgent
    from google.adk.auth.credential_manager import CredentialManager
    from google.adk.integrations.agent_identity import GcpAuthProvider
    from google.adk.integrations.agent_registry import AgentRegistry
    
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
    
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable not set.")
    
    # Register the auth provider
    CredentialManager.register_auth_provider(GcpAuthProvider())
    
    # Initialize the registry client
    registry = AgentRegistry(
        project_id=project_id,
        location=location,
    )
    
    # Fetch the registered MCP toolset.
    # The ADK applies the bindings configured in Agent Registry.
    mcp_server_name = "mcpServers/SERVER_ID"
    my_mcp_toolset = registry.get_mcp_toolset(mcp_server_name=mcp_server_name)
    
    # Compose the agent
    maps_agent = LlmAgent(
        name="maps_agent",
        model="gemini-1.5-flash",
        instruction=(
            "You are a local guide and navigation expert. Your goal is to provide"
            "accurate location information and directions.\n\n"
            "Rules:\n"
            "1. **Planning**: Before answering, plan how to use the tools to get"
            "the best information (e.g., search for a place first, then get details"
            "or directions).\n"
            "2. **Tool Usage**: Use the Maps MCP tools to find locations, addresses,"
            "and navigation details. Do not guess locations or distances.\n"
            "3. **Output Format**: Provide clear summaries of locations, including"
            "full addresses and key details. Use formatting to make recommendations"
            "easy to read.\n"
            "4. **Tone**: Be helpful, enthusiastic, and descriptive, with"
            "appropriate emojis to enhance the experience."
        ),
        tools=[my_mcp_toolset],
    )
    

If you set up 3LO for accessing tools on behalf of a user, you must also provide `continue_uri` to the `get_mcp_toolset` method. This URI indicates where the user is redirected after granting consent:
    
    
    [...]
    
    # Fetch the registered MCP toolset.
    # The ADK applies the bindings configured in Agent Registry.
    # For 3-legged OAuth (3LO), provide continue_uri.
    mcp_server_name = "mcpServers/SERVER_ID"
    my_mcp_toolset = registry.get_mcp_toolset(
        mcp_server_name=mcp_server_name,
        # Replace with your app's redirect URI:
        continue_uri="https://REDIRECT_URI"
    )
    
    # Compose the agent
    maps_agent = LlmAgent(
        name="maps_agent",
        model="gemini-1.5-flash",
        instruction=(
            "You are a local guide and navigation expert. Your goal is to provide"
            "accurate location information and directions.\n\n"
            "Rules:\n"
            "1. **Planning**: Before answering, plan how to use the tools to get"
            "the best information (e.g., search for a place first, then get details"
            "or directions).\n"
            "2. **Tool Usage**: Use the Maps MCP tools to find locations, addresses,"
            "and navigation details. Do not guess locations or distances.\n"
            "3. **Output Format**: Provide clear summaries of locations, including"
            "full addresses and key details. Use formatting to make recommendations"
            "easy to read.\n"
            "4. **Tone**: Be helpful, enthusiastic, and descriptive, with"
            "appropriate emojis to enhance the experience."
        ),
        tools=[my_mcp_toolset],
    )
    

## Use custom headers for external tools

To send advanced context to a target agent, or if external toolsets don't support [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager), you can provide custom HTTP headers directly in your ADK requests.

Configure custom headers by providing a `header_provider` callback when initializing your `AgentRegistry` client.

The `header_provider` callback receives the current execution context and returns a dictionary of HTTP headers. The `RemoteA2aAgent` or `McpToolset` component automatically attaches these headers to downstream requests.

Custom headers provided by the `header_provider` callback are only sent to the target Google Cloud services, which are either the agents or tools. Custom headers aren't used to authenticate against the Agent Registry API itself. The API always relies on ADC.

This example demonstrates how to provide an API key or custom bearer token for an external toolset:
    
    
    import os
    from typing import Any
    from google.adk.integrations.agent_registry import AgentRegistry
    
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
    external_api_key = os.environ.get("API_KEY")
    
    # Define the custom header provider.
    def my_auth_headers(context: Any) -> dict[str, str]:
        """Returns custom headers injected into the tool or agent requests."""
        return {
            "Authorization": f"Bearer {external_api_key}",
            "X-Custom-Context": "orchestrator-request"
        }
    
    # Initialize the registry client.
    # The header_provider is sent to the MCP server or agent during invocation.
    # The header_provider is not used to authenticate against the Agent Registry API.
    # The Agent Registry API always uses your Google ADC.
    registry = AgentRegistry(
        project_id=project_id,
        location=location,
        header_provider=my_auth_headers
    )
    
    # Fetching the toolset automatically attaches the header_provider to the MCP server.
    # Replace with the full resource name of your registered MCP server.
    mcp_server_name = f"projects/PROJECT_ID/locations/LOCATION/mcpServers/EXTERNAL_SERVER_ID"
    external_mcp_toolset = registry.get_mcp_toolset(mcp_server_name=mcp_server_name)
    

## What's next

  * Learn how to use [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) to enforce access controls and network perimeters on your authenticated tool requests.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
