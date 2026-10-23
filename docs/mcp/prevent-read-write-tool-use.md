---
url: https://docs.cloud.google.com/mcp/prevent-read-write-tool-use/
title: Prevent read-write MCP tool use \u00a0|\u00a0 Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:37.747697+00:00
---

# Prevent read-write MCP tool use  |  Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/prevent-read-write-tool-use/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Prevent read-write MCP tool use Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) deny policies let you restrict Model Context Protocol (MCP) tools to read-only actions, preventing AI applications from modifying or deleting resources. You can enforce these guardrails at the Google Cloud organization, folder, or project level to protect workloads from unintended or unauthorized changes.

You can't use IAM deny policies to control access to MCP tools provided by [non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers).

## Control MCP use with IAM attributes

The following attributes can be used in your Identity and Access Management deny policies:

  * `tool.isReadOnly`: a resource attribute that indicates whether the invoked tool only reads data.
  * `request.auth.oauth.client_id`: the OAuth client ID.
  * `resource.service`: the name of service—for example, `bigquery.googleapis.com`.
  * `tool.name`: the name of the MCP tool, for example, `list_agents`.



## Limitations

Control of MCP use with IAM has the following limitations:

  * The `request.auth.oauth.client_id` attribute is only supported for IAM deny policies. IAM allow policies don't support this attribute.
  * These IAM attributes are only checked and enforced for the `mcp.tools.call` permission. These attributes cannot be combined with any other permissions in IAM deny policies.
  * Tags can't be mixed with the `resource.service` attribute or any MCP attributes in IAM conditions.
  * The `resource.service` and `tool.name` attributes aren't available in the Google Cloud console. IAM policies that use these attributes must be managed with Google Cloud CLI.
  * Because the `mcp.tools.call` permission is checked at the project level, MCP IAM attributes can't be used to control access to resourceless APIs such as the Resource Manager MCP server. For more information, see [Resource Manager overview](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview) and [Use the Resource Manager remote MCP server](https://docs.cloud.google.com/resource-manager/docs/use-resourcemanager-mcp).



## Prevent read-write tool use

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

## Apply a deny policy

To apply a deny policy to a Google Cloud project, add the policy to a file named `policy.json`, and then run the following command:
    
    
    gcloud iam policies create mcp-deny-policy \
      --attachment-point=cloudresourcemanager.googleapis.com/projects/PROJECT_ID \
      --kind=denypolicies \
      --policy-file=policy.json
    

For more information, see [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview). For information on how to attach a deny policy to an organization or folder, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).

## What's next

  * [Audit logging](https://docs.cloud.google.com/logging/docs/audit/application-audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
