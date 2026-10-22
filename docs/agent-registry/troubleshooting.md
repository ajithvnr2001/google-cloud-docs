---
url: https://docs.cloud.google.com/agent-registry/troubleshooting/
title: Troubleshoot Agent Registry issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:00.143390+00:00
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

This page shows you how to resolve issues with Agent Registry.

## API rate quota exceeded

You might encounter this issue if you interact with Agent Registry API or rapidly navigate through Agent Registry in Google Cloud console:
    
    
    429 Too Many Requests

To resolve this issue, implement exponential backoff in your API clients to manage request rates. Agent Registry API has a default [rate quota](https://docs.cloud.google.com/agent-registry/quotas#rate_quotas) of 1,200 requests per minute globally and per region (20 queries per second).

If you encounter throttling when switching tabs in Google Cloud console, wait a few moments and try again. If your programmatic use case requires higher limits, [request a quota increase](https://docs.cloud.google.com/agent-registry/quotas#request_a_quota_adjustment) for the `RequestsPerMinute` metric.

## Payload size error during manual registration

You might encounter this issue if you manually register an agent or MCP server: the API rejects the request with an error stating that the payload is too large.

To resolve this issue, verify that your `agent-card.json` or `toolspec.json` file is less than 10 KB. The `AgentSpec` and `McpServerSpec` content sizes are limited to 10 KB. Minify your JSON files, remove unnecessary whitespace, or condense tool descriptions to adhere to this limit. For more information, see [JSON schemas](https://docs.cloud.google.com/agent-registry/json-schemas).

## Missing agents or MCP servers after creation

You might encounter this issue if you create an agent or MCP server in a supported Google Cloud product, such as Google Workspace or Gemini Enterprise: the resource doesn't appear when calling the `ListAgents` or `ListMcpServers` APIs.

To resolve this issue, wait for the background synchronization to complete. Your resources update in real-time, but other integrations are populated by offline batch jobs running periodically. If your resource doesn't appear after several hours, verify your project's [Service Usage](https://docs.cloud.google.com/service-usage/docs/overview) settings and ensure that the relevant API is enabled.

## Long-running operations appear stuck

You might encounter this issue if you deploy agents or configure complex bindings: the operation takes a significant amount of time and appears stuck.

To resolve this issue, use the `get_operation` MCP tool or the `google.longrunning.Operations.GetOperation` API endpoint to poll the operation's status. Some agent and MCP backend creations require significant infrastructure provisioning, which can lead to long-running operation (LRO) times that might take up to 30 minutes. Configure your client timeout settings as a result and poll the `done` boolean flag to verify completion.

## Empty results when fetching available bindings

You might encounter this issue if you fetch available bindings for an auth provider: the API returns an `empty array` or an access error, even if you verified the binding exists.

To resolve this issue, verify that your principal has the correct Identity and Access Management (IAM) permissions on the target `AuthProvider` resource. The API applies strict IAM checks and removes `Binding` objects that reference auth providers the caller doesn't have access to. Ensure that your principal has the required access on the auth provider and the `roles/agentregistry.viewer` role on the project.

## Skill revision download fails with `302` error

You might encounter this issue if you try to download a skill revision payload using the `GetSkillRevision` API with the `?alt=media` query parameter: the request fails and returns an error similar to the following:
    
    
    {
      "error": {
        "code": 302,
        "message": "Unknown Error.",
        "status": "UNKNOWN"
      }
    }
    

To resolve this issue, verify that your HTTP client is configured to automatically follow redirects. The `?alt=media` endpoint requires a `302` redirect to successfully download the skill's archive. For example, if you are using `curl`, add the `-L` or `--location` flag to your command.

## Skill revision validation fails or shows `FAILED` state

You might encounter this issue after creating a new skill revision: the revision transitions to a `FAILED` state and cannot be loaded by agents.

To resolve this issue, check the validation logs or inspect the ZIP payload contents:

  * Ensure that the ZIP archive contains a `SKILL.md` file at its root.
  * Verify that the `SKILL.md` file has a valid YAML frontmatter block with both `name` and `description` defined.
  * Confirm that the ZIP payload doesn't exceed the size limits: compressed size must be less than 500 KB, total uncompressed size less than 10 MB, and individual file size less than 1 MB.
  * Verify that the archive doesn't contain symbolic links, directory traversal elements such as `..`, or absolute paths.



## Resource entity not found error when managing IAP policies

You might encounter this issue if you use `gcloud iap web` commands to manage egress policies on Agent Registry resources:
    
    
    NOT_FOUND: Requested entity was not found

To resolve this issue, verify that the resource flag you pass to `gcloud iap web` matches the underlying Agent Registry child resource type:

  * For endpoints, such as external APIs or Google API egress points, use the `--endpoint` flag.
  * For Model Context Protocol servers, use the `--mcp-server` flag.
  * For registered agents, use the `--agent` flag.



Check the resource URI returned by `gcloud agent-registry [endpoints|mcp-servers|agents] list` to confirm whether the resource path contains `/endpoints/`, `/mcpServers/`, or `/agents/`. Passing the wrong resource flag, for example, passing `--endpoint` for an MCP server ID, causes a `NOT_FOUND` error.

## Permission denied when applying IAP web IAM policies

You might encounter this issue if you apply or modify Identity-Aware Proxy web IAM policies for Agent Registry resources:
    
    
    ERROR: (gcloud.iap.web.set-iam-policy) PERMISSION_DENIED

To resolve this issue, verify that your active user or service account has the required permissions on the project hosting the registry and gateway:

  * Ensure that the caller has the IAP Policy Admin (`roles/iap.admin`) or Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) role on the central governance project.
  * Confirm that the caller has the `iap.web.setIamPolicy` and `resourcemanager.projects.setIamPolicy` permissions.



## Failures when accessing Agent Registry with Workforce Identity Federation

You might encounter this issue if you access Agent Registry in the Google Cloud console or use gcloud CLI when authenticated with Workforce Identity Federation.

Google Cloud console displays generic loading errors, such as the following:

  * "There was an error while loading..."
  * "The server was not able to fulfill your request"
  * "Failed to load"



Additionally, `gcloud` commands might return an internal error, such as `error 13: an internal error has occurred`.

To resolve this issue, authenticate with a standard Google Account managed through Cloud Identity or Google Workspace. Ensure that the account has the required permissions, such as `roles/agentregistry.admin` or `roles/agentregistry.viewer`.

Agent Platform Governance services have limited support for federated identities. Granting broader IAM roles to a federated principal doesn't resolve the issue.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
