---
url: https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-a2a/
title: Call an agent using its registry A2A endpoint \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:28.132178+00:00
---

# Call an agent using its registry A2A endpoint  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-a2a/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Call an agent using its registry A2A endpoint Stay organized with collections  Save and categorize content based on your preferences. 

Agent2Agent (A2A) agents in Agent Registry advertise protocol interfaces containing an endpoint URL and a protocol binding (such as `HTTP_JSON`). You can discover an agent's URL in the registry to call its A2A methods from custom orchestrators or clients.

## At a glance

Specification | Details  
---|---  
**Discovery API** | `agentregistry.googleapis.com` (`v1`)  
**Invocation proxy host** | `LOCATION-discoveryengine.googleapis.com`  
**Protocol binding** | `HTTP_JSON`  
**URL project identifier** | Google Cloud project number (not project ID)  
**Supported A2A methods** | `GET /v1/card`, `POST /v1/message:send`, `POST /v1/message:stream`  
**Required message schema** | `message.role = "ROLE_USER"`, `content[].text`, unique `messageId`  
**Required IAM permissions** | `roles/agentregistry.viewer` (discovery) and `discoveryengine.assistants.assist` (invocation)  
  
## Before you begin

  1. Enable the **Agent Registry API** (`agentregistry.googleapis.com`) and **Discovery Engine API** (`discoveryengine.googleapis.com`) in your Google Cloud project.
  2. If the agent was not created directly in your Gemini Enterprise app, import the agent from Agent Registry and grant end users access to it. For instructions, see [Import A2A agents from Agent Registry](https://docs.cloud.google.com/gemini/enterprise/docs/import-govern-agent-registry).
  3. Grant your caller principal appropriate IAM permissions: 
     * **To read the registry** : Agent Registry Viewer (`roles/agentregistry.viewer`).
     * **To invoke the agent** : Discovery Engine Editor (`roles/discoveryengine.editor`) or a custom role including `discoveryengine.assistants.assist`.
  4. If you authenticate using Application Default Credentials (ADC), configure your client to send the quota project header: `-H "X-Goog-User-Project: PROJECT_ID"`.
  5. Optionally, install the Agent Development Kit (ADK) library if you plan to wrap remote agents as programmatic sub-agents: `pip install "google-adk[a2a]>=1.29.0"`.



## Step 1: Discover the agent and its A2A endpoint

To invoke an A2A agent, first discover its advertised `url` in Agent Registry. List the agents in your registry location (such as `us` or `eu`, passed as a path parameter on the global `agentregistry.googleapis.com` host):
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/agents?pageSize=100"
    

You can also search for an agent by display name prefix using the Google Cloud CLI:
    
    
    gcloud agent-registry agents search \
      --project=PROJECT_ID \
      --location=LOCATION \
      --search-string="displayName:My_Agent_*"
    

**Note:** If the `agent-registry` command group is unrecognized, run `gcloud components update` to update your CLI distribution.

In the returned agent resource, inspect the `protocols` array. Locate the entry where `type` equals `A2A_AGENT` and `interfaces[].protocolBinding` equals `HTTP_JSON`. Extract the corresponding `url`:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/agents/AGENT_RESOURCE_ID",
      "displayName": "My Agent",
      "protocols": [
        {
          "type": "A2A_AGENT",
          "protocolVersion": "0.3.0",
          "interfaces": [
            {
              "url": "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/collections/default_collection/engines/ENGINE_ID/assistants/default_assistant/agents/AGENT_ID/a2a",
              "protocolBinding": "HTTP_JSON"
            }
          ]
        }
      ]
    }
    

**Important:** Use the returned `url` string verbatim. For Gemini Enterprise agents, this URL routes traffic through the Discovery Engine A2A proxy and embeds your Google Cloud project **number** rather than project ID. Not all registered agents expose an A2A interface; if `protocols` is empty or omits `A2A_AGENT`, the agent cannot be invoked over A2A.

See [`projects.locations.agents` REST API reference](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.agents) for the complete agent resource schema.

## Step 2: Fetch the agent card

The agent card provides metadata describing the agent's identity, description, and input/output capabilities. To retrieve the card, send an HTTP GET request to the `/v1/card` path appended to the agent's A2A endpoint URL:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "A2A_ENDPOINT_URL/v1/card"
    

Example response payload:
    
    
    {
      "name": "My Agent",
      "description": "What the agent does.",
      "url": "A2A_ENDPOINT_URL",
      "capabilities": {},
      "defaultInputModes": ["text"],
      "defaultOutputModes": ["text"],
      "preferredTransport": "HTTP+JSON"
    }
    

**Note:** Ensure you request `/v1/card`. Alternative path variations (such as `/v1:getCard`, `/v1/getCard`, or `/.well-known/agent-card.json`) return an HTTP `404 Not Found` error on the HTTP+JSON protocol binding.

## Step 3: Send a message

To send a user query to the agent, make a POST request to `/v1/message:send`. The request body must conform to the A2A message schema, requiring `role` set to `ROLE_USER`, a `content` array containing text parts, and a uniquely generated `messageId`:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "A2A_ENDPOINT_URL/v1/message:send" \
      -d '{
        "message": {
          "role": "ROLE_USER",
          "content": [
            {
              "text": "What can you help me with?"
            }
          ],
          "messageId": "UNIQUE_UUID_STRING"
        }
      }'
    

In the response payload, the agent's reply is returned within the `message` object:
    
    
    {
      "message": {
        "contextId": "projects/PROJECT_NUMBER/locations/LOCATION/collections/default_collection/engines/ENGINE_ID/sessions/SESSION_ID",
        "role": "ROLE_AGENT",
        "content": [
          {
            "text": "I am an AI assistant..."
          }
        ]
      }
    }
    

Concatenate the text strings inside `content[].text` to display the complete response. To continue the conversation within the same session, save the returned `contextId` string and supply it as `message.contextId` in your next request.

See [A2A `message:send` REST API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants.agents.a2a.v1.message/send) for the complete message payload schema.

## Stream responses incrementally

For streaming output, send a POST request with an identical message body to `/v1/message:stream`:
    
    
    curl -N -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "A2A_ENDPOINT_URL/v1/message:stream" \
      -d '{
        "message": {
          "role": "ROLE_USER",
          "content": [
            {
              "text": "Say hello."
            }
          ],
          "messageId": "UNIQUE_UUID_STRING"
        }
      }'
    

The endpoint returns a JSON array of streamed chunk objects over HTTP. Append the `content[].text` fragments sequentially as they arrive. Streamed chunks also contain `metadata.sessionInfo` and `metadata.assistToken`.

See [A2A `message:stream` REST API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants.agents.a2a.v1.message/stream) for the streaming payload specification.

## Call an A2A endpoint using Python

This Python script resolves an A2A endpoint in Agent Registry and sends a message using raw HTTP requests:
    
    
    # Install dependencies: pip install google-auth requests
    import uuid
    import google.auth
    from google.auth.transport.requests import AuthorizedSession
    
    # TODO(developer): Replace placeholder values with your project ID and location.
    project_id = "PROJECT_ID"
    location = "LOCATION"          # Registry location (for example: "us" or "eu")
    target_display_name = "My Agent"
    query_text = "What can you help me with?"
    
    # Initialize credentials and authorized session
    creds, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    session = AuthorizedSession(creds)
    
    # Step 1: Resolve the A2A endpoint URL from the Agent Registry
    registry_url = (
        f"https://agentregistry.googleapis.com/v1/"
        f"projects/{project_id}/locations/{location}/agents"
    )
    response = session.get(registry_url)
    response.raise_for_status()
    agents = response.json().get("agents", [])
    
    def get_a2a_url(agent_resource):
        for proto in agent_resource.get("protocols") or []:
            if proto.get("type") == "A2A_AGENT":
                for iface in proto.get("interfaces", []):
                    if iface.get("protocolBinding") == "HTTP_JSON":
                        return iface.get("url")
        return None
    
    target_agent = next(
        (a for a in agents if a.get("displayName") == target_display_name),
        None
    )
    if not target_agent:
        raise SystemExit(f"Agent '{target_display_name}' not found in registry.")
    
    endpoint_url = get_a2a_url(target_agent)
    if not endpoint_url:
        raise SystemExit("Target agent does not publish an HTTP_JSON A2A endpoint.")
    
    # Step 2: Fetch and verify the agent card
    card_resp = session.get(f"{endpoint_url}/v1/card")
    card_resp.raise_for_status()
    card = card_resp.json()
    print("Resolved Agent:", card.get("name"))
    
    # Step 3: Send an A2A message
    body = {
        "message": {
            "role": "ROLE_USER",
            "content": [{"text": query_text}],
            "messageId": str(uuid.uuid4()),
        }
    }
    send_resp = session.post(f"{endpoint_url}/v1/message:send", json=body)
    send_resp.raise_for_status()
    
    reply_message = send_resp.json().get("message", {})
    full_reply_text = "".join(
        part.get("text", "") for part in reply_message.get("content", [])
    )
    print("Agent Reply:", full_reply_text)
    

## Simplify orchestration using the ADK

The Agent Development Kit (ADK) resolves registry endpoints automatically and wraps remote A2A agents as sub-agents:
    
    
    from google.adk.integrations.agent_registry import AgentRegistry
    
    # Initialize registry client
    registry = AgentRegistry(project_id="PROJECT_ID", location="LOCATION")
    
    # Resolve remote A2A agent directly by resource name
    remote_agent = registry.get_remote_a2a_agent(
        agent_name="agents/AGENT_RESOURCE_ID"
    )
    

**Note:** This integration requires `google-adk[a2a]>=1.29.0`. For more details, see [Resolve endpoints and build orchestrators](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators).

## Additional notes

A2A endpoints have the following behaviors:

  * **Strict path naming** : Only `GET {url}/v1/card`, `POST {url}/v1/message:send`, and `POST {url}/v1/message:stream` are supported for HTTP+JSON bindings.
  * **Strict schema validation** : Passing plain `"user"` as the role returns an HTTP `400 Bad Request` error. You must pass the enum string `"ROLE_USER"`. Similarly, message text must reside inside the `content` array rather than `parts`, and `messageId` is strictly required.
  * **Non-A2A agent invocation error** : If an agent lacks an `A2A_AGENT` protocol entry in the registry (such as certain prebuilt or managed agents), calling `getCard` on its proxy URL returns `501 UNIMPLEMENTED` (_"... is not supported yet"_), and calling `message:send` returns `400 INVALID_ARGUMENT` (_"Unsupported agent"_).
  * **Project number in URL** : The registry returns an A2A URL containing the project number rather than the project ID. Do not alter this numeric string when making HTTP requests.



## Troubleshooting

Use the following table to troubleshoot common A2A endpoint errors:

Symptom | Likely cause | Resolution  
---|---|---  
**HTTP 404 on`getCard` request** | Using an incorrect path alias (such as `/v1:getCard` or `/.well-known/agent-card.json`). | Send the GET request strictly to `GET {url}/v1/card`.  
**HTTP 400 *"Unknown name 'parts'"** * | Using old or generative AI client body formatting. | Place text strings inside `content`, not `parts`.  
**HTTP 400 invalid enum value for`role`** | Passing lowercase `"user"` or `"user_role"`. | Set `message.role` exactly to `"ROLE_USER"`.  
**HTTP 501 *"is not supported yet"** * | Calling `getCard` on an agent that does not publish an A2A interface. | Inspect the registry resource's `protocols` array to confirm `A2A_AGENT` support before calling.  
**HTTP 400 *"Unsupported agent"** * | Calling `message:send` on a non-A2A agent. | Choose an agent whose registry definition includes an active `A2A_AGENT` protocol binding.  
`HTTP 401` or `HTTP 403 Permission Denied` | Missing OAuth scopes, missing IAM roles, or missing quota project header. | Check caller IAM roles (`agentregistry.viewer` and `assistants.assist`); verify `cloud-platform` scope; pass `-H "X-Goog-User-Project: PROJECT_ID"` if using ADC.  
  
## Related resources

  * [Agent Registry overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry)
  * [Search for agents and tools in Agent Registry](https://docs.cloud.google.com/agent-registry/search-agents-and-tools)
  * [Resolve endpoints and build orchestrators (ADK)](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators)
  * [A2A message:send REST API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants.agents.a2a.v1.message/send)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
