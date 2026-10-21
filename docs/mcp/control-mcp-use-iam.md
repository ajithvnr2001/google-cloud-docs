---
url: https://docs.cloud.google.com/mcp/control-mcp-use-iam/
title: Control MCP use with Identity and Access Management \u00a0|\u00a0 Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:56.818326+00:00
---

# Control MCP use with Identity and Access Management  |  Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/control-mcp-use-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Control MCP use with Identity and Access Management Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) and [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies) let you secure Google Cloud Model Context Protocol (MCP) servers. You can configure these policies to grant or restrict MCP tool calls based on the service, tool name, OAuth client ID, or whether a tool is read-only. You can't use IAM to control access to [non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers).

## Understand IAM permission checks for MCP

When you use Google Cloud services through MCP servers, the principal making the tool call must have the following permissions:

  * The `mcp.tools.call` permission on the Google Cloud project.
  * The required permissions to access the underlying Google Cloud resources.



For example, if an MCP tool call is sent to get a BigQuery Dataset's metadata, and the caller has the `mcp.tools.call` permission but lacks the `bigquery.datasets.get` permission, the tool call fails. Similarly, if the caller has the `bigquery.datasets.get` permission, but lacks the `mcp.tools.call` permission, the call fails.

## IAM deny policy attributes

The following attributes can be used in your Identity and Access Management deny policies:

  * `tool.isReadOnly`: a resource attribute that indicates whether the invoked tool only reads data.
  * `request.auth.oauth.client_id`: the OAuth client ID.
  * `resource.service`: the name of service—for example, `bigquery.googleapis.com`.
  * `tool.name`: the name of the MCP tool, for example, `list_agents`.



## IAM allow policy attributes

The following attributes can be used in your Identity and Access Management allow policies:

  * `resource.service`: the name of service—for example, `bigquery.googleapis.com`.
  * `tool.name`: the name of the MCP tool, for example, `list_agents`.



## Limitations

Control of MCP use with IAM has the following limitations:

  * The `request.auth.oauth.client_id` attribute is only supported for IAM deny policies. IAM allow policies don't support this attribute.
  * These IAM attributes are only checked and enforced for the `mcp.tools.call` permission. These attributes cannot be combined with any other permissions in IAM deny policies.
  * Tags can't be mixed with the `resource.service` attribute or any MCP attributes in IAM conditions.
  * The `resource.service` and `tool.name` attributes aren't available in the Google Cloud console. IAM policies that use these attributes must be managed with Google Cloud CLI.
  * Because the `mcp.tools.call` permission is checked at the project level, MCP IAM attributes can't be used to control access to resourceless APIs such as the Resource Manager MCP server. For more information, see [Resource Manager overview](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview) and [Use the Resource Manager remote MCP server](https://docs.cloud.google.com/resource-manager/docs/use-resourcemanager-mcp).



## Example IAM deny policies

The following sections give examples of Identity and Access Management deny policies that can be used to control MCP use.

### Deny all MCP tool use

The following IAM deny policy prevents use of Google and Google Cloud MCP server tools by all users.
    
    
    {
      "displayName": "Deny access to MCP tools for all users",
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principalSet://goog/public:all"
            ],
            "deniedPermissions": [
              "mcp.googleapis.com/tools.call"
            ]
          }
        }
      ]
    }
    

After the policy is applied to a Google Cloud project, when a client calls `tools/call`, the request fails and an HTTP client error is returned.

**Note:** When an MCP client calls `tools/list`, a list of all tools is returned.

### Deny read-write MCP tool use

The following IAM deny policy prevents use of any tool that isn't read-only. Tools that create, modify, or delete resources aren't permitted.
    
    
    {
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principalSet://goog/public:all"
            ],
            "deniedPermissions": [
              "mcp.googleapis.com/tools.call"
            ],
            "denialCondition": {
              "title":  "Deny read-write tools",
              "expression": "api.getAttribute('mcp.googleapis.com/tool.isReadOnly', false) == false",
            }
          }
        }
      ]
    }
    

After the policy is applied to a Google Cloud project, when an MCP client makes a tool call to a tool that isn't annotated as `read-only`, the request fails and an HTTP client error is returned.

**Note:** When an MCP client calls `tools/list`, a list of all tools is returned, including read-write tools.

### Deny MCP use by service

The following IAM deny policy prevents use of MCP tools from a specific service for all users.
    
    
    {
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principalSet://goog/public:all"
            ],
            "deniedPermissions": [
              "mcp.googleapis.com/tools.call"
            ],
            "denialCondition": {
              "title": "Deny all MCP tool use from this service",
              "expression": "resource.service == 'SERVICE_NAME'"
            }
          }
        }
      ]
    }
    

Replace SERVICE_NAME with the service name—for example, `bigquery.googleapis.com`.

### Allow MCP use by service

You can use a deny policy to deny MCP use for all services except ones that you specify.

The following IAM deny policy prevents use of MCP tools from all services except one service for all users.
    
    
    {
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principalSet://goog/public:all"
            ],
            "deniedPermissions": [
              "mcp.googleapis.com/tools.call"
            ],
            "denialCondition": {
              "title": "Only Allow access to the following service's MCP tools",
              "expression": "!(resource.service == 'SERVICE_NAME')"
            }
          }
        }
      ]
    }
    

Replace SERVICE_NAME with the name of the service that you want to allow—for example, `compute.googleapis.com`.

### Allow MCP use by Client ID

The following IAM deny policy prevents use of MCP tools by all principals except for a specific client ID.
    
    
    {
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principalSet://goog/public:all"
            ],
            "deniedPermissions": [
              "mcp.googleapis.com/tools.call"
            ],
            "denialCondition": {
              "title": "Allow MCP tool use by the following client ID.",
              "expression": "!(request.auth.oauth.client_id == 'CLIENT_ID')"
            }
          }
        }
      ]
    }
    

Replace CLIENT_ID with the client ID—for example, `12345678910-0abcdef0ghi.apps.googleusercontent.com`. To view existing client IDs, in the Google Cloud console, go to **Google Auth Platform** > **Clients**.

[Go to Clients](https://console.cloud.google.com/auth/clients)

## Apply a deny policy

To apply a deny policy to a Google Cloud project, add the policy to a file named `policy.json`, and then run the following command:
    
    
    gcloud iam policies create mcp-deny-policy \
      --attachment-point=cloudresourcemanager.googleapis.com/projects/PROJECT_ID \
      --kind=denypolicies \
      --policy-file=policy.json
    

For more information, see [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview). For information on how to attach a deny policy to an organization or folder, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).

## Example IAM allow policies

The following sections give examples of Identity and Access Management allow policies that can be used to control MCP use. In addition to the MCP-specific permissions, principals must have permissions on any services they access through MCP calls.

### Grant principals MCP access to specific services

You can use an allow policy to grant principals MCP access to specific servers.

The following Use IAM allow policy grants the principal `user@example.com` access to the BigQuery and Cloud Storage MCP servers.
    
    
    {
      "bindings": [
        {
          "role": "roles/mcp.toolUser",
          "members": [
            "user:user@example.com",
          ],
          "condition": {
            "title": "Allow MCP calls for BigQuery and Cloud Storage MCP servers",
            "expression": "resource.service == 'bigquery.googleapis.com' || resource.service == 'storage.googleapis.com'"
          }
        }
      ]
    }
    

### Grant principals access to a specific MCP tool

You can use an allow policy to grant principals access to a specific MCP tool.

The following Use IAM allow policy grants the principal `user@example.com` access to the Compute Engine tool `list_instances`.
    
    
    {
      "bindings": [
        {
          "role": "roles/mcp.toolUser",
          "members": [
            "user:user@example.com"
          ],
          "condition": {
            "title": "Grant access to list_instances tool in the Compute Engine MCP server",
            "expression": "resource.service == 'compute.googleapis.com' && api.getAttribute('mcp.googleapis.com/tool.name', '') == 'list_instances'"
          }
        }
      ]
    }
    

## Apply an allow policy

To apply an allow policy to a Google Cloud resource, follow the read, modify, write process outlined in [Configure resource-based access](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access).

For more information, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

## What's next

  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).
  * Learn more about IAM [deny](https://docs.cloud.google.com/iam/docs/deny-access) policies and [allow](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) policies.
  * [Troubleshoot IAM policies](https://docs.cloud.google.com/iam/docs/troubleshoot-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
