---
url: https://docs.cloud.google.com/agent-registry/troubleshooting/
title: Troubleshoot Agent Registry issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:13.777131+00:00
---

# Troubleshoot Agent Registry issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Troubleshoot Agent Registry issues Stay organized with collections  Save and categorize content based on your preferences. 

When you register, discover, or connect components in Agent Registry, you can diagnose and resolve common issues such as quota limits, payload and skill validation errors, location mismatches, synchronization delays, and permission errors.

## API rate quota exceeded

The following error occurs if you exceed the request rate limit when interacting with the Agent Registry API or rapidly navigating through Agent Registry in the Google Cloud console:
    
    
    429 Too Many Requests

To resolve this issue, implement exponential backoff in your API clients to manage request rates. Agent Registry API has a default [rate quota](https://docs.cloud.google.com/agent-registry/quotas#rate-quotas) of 1,200 requests per minute, or 20 queries per second, globally and per region.

If you encounter throttling when switching tabs in Google Cloud console, wait a few moments and try again. If your programmatic use case requires higher limits, [request a quota increase](https://docs.cloud.google.com/agent-registry/quotas#request-a-quota-adjustment) for the `RequestsPerMinute` metric.

## Payload size error during manual registration

The following error occurs when you manually register an agent or MCP server with a specification file that exceeds the size limit:

The API rejects the request with an error stating that the payload is too large.

To resolve this issue, verify that your `agent-card.json` or `toolspec.json` file is less than 10 KB. The `AgentSpec` and `McpServerSpec` content sizes are limited to 10 KB. Minify your JSON files, remove unnecessary whitespace, or condense tool descriptions to adhere to this limit. For more information, see [JSON schemas](https://docs.cloud.google.com/agent-registry/json-schemas).

## Missing agents or MCP servers after creation

The following error occurs after you create an agent or MCP server in a supported Google Cloud product, such as Google Workspace or Gemini Enterprise:

The resource doesn't appear in the output when you call the `ListAgents` or `ListMcpServers` APIs.

To resolve this issue, wait for the background synchronization to complete. Your resources update in real time, but periodic offline batch jobs populate other integrations. If your resource doesn't appear after several hours, verify your project's [Service Usage](https://docs.cloud.google.com/service-usage/docs/overview) settings and ensure that the relevant API is enabled.

## Long-running operations appear stuck

The following error occurs when you deploy agents or configure complex bindings:

The operation takes a significant amount of time and appears stuck.

To resolve this issue, use the `get_operation` MCP tool or the `google.longrunning.Operations.GetOperation` API endpoint to poll the operation's status. Some agent and MCP backend creations require significant infrastructure provisioning, which can lead to long-running operation (LRO) times that might take up to 30 minutes. Configure your client timeout settings as a result and poll the `done` boolean flag to verify completion.

## Empty results when fetching available bindings

The following error occurs if you fetch available bindings for an [auth provider](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#auth-providers) without sufficient permissions on the target `AuthProvider` resource:

The API returns an empty array or an access error, even if the binding exists.

To resolve this issue, verify that your principal has the correct Identity and Access Management (IAM) permissions on the target `AuthProvider` resource. The API applies strict IAM checks and removes `Binding` objects that reference auth providers the caller doesn't have access to. Ensure that your principal has the required access on the auth provider and the `roles/agentregistry.viewer` role on the project.

## Skill revision download fails with `302` error

The following error occurs if you try to download a skill revision payload using the `GetSkillRevision` API with the `?alt=media` query parameter and your HTTP client doesn't follow redirects:
    
    
    {
      "error": {
        "code": 302,
        "message": "Unknown Error.",
        "status": "UNKNOWN"
      }
    }
    

To resolve this issue, verify that your HTTP client is configured to automatically follow redirects. The `?alt=media` endpoint requires a `302` redirect to successfully download the skill's archive. For example, if you are using `curl`, add the `-L` or `--location` flag to your command.

## Skill revision validation fails or shows `FAILED` state

The following error occurs when you create a new skill revision with an invalid ZIP archive:

The revision transitions to a `FAILED` state and can't be loaded by agents.

To resolve this issue, check the validation logs or inspect the ZIP payload contents:

  * Ensure that the ZIP archive contains a `SKILL.md` file at its root.
  * Verify that the `SKILL.md` file has a valid YAML front matter block with both `name` and `description` defined.
  * Confirm that the ZIP payload doesn't exceed the size limits: compressed size must be less than 500 KB, total uncompressed size less than 10 MB, and individual file size less than 1 MB.
  * Verify that the archive doesn't contain symbolic links, directory traversal elements such as `..`, or absolute paths.



## Standalone skills don't appear in service or agent resource lists

The following error occurs if you query the agent or service lists for standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture), such as by running `gcloud agent-registry services list` or `gcloud agent-registry agents list`:

The standalone skill doesn't appear in the output.

To resolve this issue, query the `skills` collection instead:

  * Unlike manually registered agents, MCP servers, and endpoints, standalone skills don't use writable `Service` resources or `Agent`, `McpServer`, or `Endpoint` discovery resources. Instead, Agent Registry represents standalone skills directly as top-level `Skill` resources and versioned `SkillRevision` resources.
  * To list, search, or inspect standalone skills, use the **Skills** tab in the Google Cloud console, run `gcloud alpha agent-registry skills list` or `gcloud alpha agent-registry skills search`, or call the [`skills`](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills) REST API methods. For instructions, see [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills) and [Search for standalone skills](https://docs.cloud.google.com/agent-registry/search-agents-and-tools#search-skills).
  * If you are looking for inline [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a) declared in an agent's Agent Card, inspect the `skills` field on the `Agent` discovery resource using `gcloud agent-registry agents describe` or `gcloud agent-registry agents search`.



## Resource entity not found error when managing IAP policies

The following error occurs when you use `gcloud iap web` commands to manage Identity-Aware Proxy (IAP) egress policies on Agent Registry resources:
    
    
    NOT_FOUND: Requested entity was not found

To resolve this issue, verify the following:

  * **Registration status** : confirm that the target component is registered in Agent Registry in the expected location.
  * **Identifier format** : confirm that your command or policy binding specifies the standard [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) rather than a [registry identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers) URN.
  * **Resource flag** : verify that the resource flag you pass to `gcloud iap web` matches the underlying Agent Registry child resource type: 
    * For endpoints, such as external APIs or Google API egress points, use the `--endpoint` flag.
    * For Model Context Protocol servers, use the `--mcp-server` flag.
    * For registered agents, use the `--agent` flag.



Check the [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) returned by `gcloud agent-registry endpoints list`, `gcloud agent-registry mcp-servers list`, or `gcloud agent-registry agents list` to confirm whether the resource name contains `/endpoints/`, `/mcpServers/`, or `/agents/`. Passing the wrong resource flag, for example, passing `--endpoint` for an MCP server ID, causes a `NOT_FOUND` error.

## Permission denied when applying IAP web IAM policies

The following error occurs when you apply or modify IAP web IAM policies for Agent Registry resources without the required administrative roles:
    
    
    ERROR: (gcloud.iap.web.set-iam-policy) PERMISSION_DENIED

To resolve this issue, verify that your active user or service account has the required permissions on the project hosting the registry and gateway:

  * Ensure that the caller has the IAP Policy Admin (`roles/iap.admin`) or Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) role on the central [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project).
  * Confirm that the caller has the `iap.web.setIamPolicy` and `resourcemanager.projects.setIamPolicy` permissions.



## Remote MCP server not found in a regional location

The following error occurs if you query for an automatically registered [Google or Google Cloud remote MCP server](https://docs.cloud.google.com/mcp/supported-products), or apply an IAP egress policy to it, in a regional location such as `us-central1`:

The request returns a `NOT_FOUND` error or an empty list, even when the service provides regional endpoints (REPs) or when traffic is routed through a regional Agent Gateway.

When Agent Registry automatically registers a Google or Google Cloud remote MCP server for an enabled API, it creates the `McpServer` resource only in the `global` location, not in individual regions such as `us-central1`. If the service provides regional endpoints, such as `https://SERVICE.REGION.rep.googleapis.com/mcp`, Agent Registry lists those regional URLs in the `interfaces` field of that single `global` `McpServer` resource.

To resolve this issue, do one of the following:

  * **Use`global` for automatically registered servers**: specify the `global` location when you query the server in Agent Registry with `--location=global` or apply IAP egress policies to it with `--region=global`, even when the calling agent routes traffic through a regional gateway.
  * **Register in a region for data residency** : if you need to keep registry metadata in a specific region, deploy custom MCP servers to regional [Cloud Run](https://docs.cloud.google.com/agent-registry/register-mcp-servers#cloud-run-mcp) or [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/agent-registry/register-mcp-servers#gke-mcp) runtimes, or [manually register](https://docs.cloud.google.com/agent-registry/register-mcp-servers#register-external-servers) the MCP server and its regional endpoint URL in that region, and then apply your IAP policy in that same region. When Agent Gateway resolves a target URL, regional registry entries take precedence over `global` entries.



## Region mismatch errors when configuring Model Armor on Agent Gateway

The following error occurs when you configure [Model Armor policy filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor) on Agent Gateway across mismatched regions:

Creating the authorization policy fails with a region mismatch error, or traffic routed through the gateway to an MCP server fails policy evaluation.

To resolve this issue, verify the regional alignment of your gateway resources and target policy bindings:

  * **Align gateway and Model Armor regions** : ensure that the Agent Gateway, the Model Armor templates, and the authorization extension and policy all reside in the same region, such as `us-central1`.
  * **Route to`global` or regional MCP servers**: you don't need to re-register `global` MCP servers in a region solely to use Model Armor. Because Model Armor inspects request and response payloads at the regional gateway, a regional gateway can inspect and govern traffic routed to MCP servers registered in the `global` location as well as regional destinations.
  * **Match IAP egress bindings to the target's registration location** : apply the IAP egress authorization binding in the location where the target `McpServer` resource is registered. Use `global` for automatically registered remote MCP servers, or use the specific region for regionally registered MCP servers.



## Manual registration or binding creation fails in a multi-region location

The following error occurs if you attempt to manually register an agent, an MCP server, or an endpoint, or create a binding, in a multi-region location such as `us` or `eu`:

The API rejects the request with an unsupported location or invalid argument error.

To resolve this issue, specify a supported regional location, such as `us-central1` or `europe-west1`, or the `global` location instead. The `us` and `eu` multi-region locations only support discovering automatically registered components and registering or discovering standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture). For the list of supported locations, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations).

## Failures when accessing Agent Registry with Workforce Identity Federation

The following errors occur if you access Agent Registry in the Google Cloud console or use the Google Cloud CLI when authenticated with Workforce Identity Federation:

Google Cloud console displays generic loading errors, such as the following:

  * "There was an error while loading..."
  * "The server was not able to fulfill your request"
  * "Failed to load"



Additionally, `gcloud` commands might return an internal error, such as `error 13: an internal error has occurred`.

To resolve this issue, authenticate with a standard Google Account managed through Cloud Identity or Google Workspace. Ensure that the account has the required permissions, such as `roles/agentregistry.admin` or `roles/agentregistry.viewer`.

Gemini Enterprise Agent Platform governance services have limited support for federated identities. Granting broader IAM roles to a federated principal doesn't resolve the issue.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
