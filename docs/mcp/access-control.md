---
url: https://docs.cloud.google.com/mcp/access-control/
title: Access control with Identity and Access Management \u00a0|\u00a0 Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:02.631487+00:00
---

# Access control with Identity and Access Management  |  Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Access control with Identity and Access Management Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud remote MCP servers let you use Identity and Access Management (IAM) to enforce fine-grained authorization across your resource hierarchy. You can configure access at the project or individual resource level to control tool use based on resource tags and read-only or read-write permissions.

[Non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers) don't require the MCP Tool User (`roles/mcp.toolUser`) role. You also can't use IAM policies or permissions to control access to non-Google Cloud MCP servers.

For detailed information about IAM and its features, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

## Grant access

Grant a principal the MCP Tool User role on a project.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. Select your project.

  3. Click person_add **Grant access**.

  4. Enter an identifier for the principal. For example, `my-app@example.com`.

  5. From the **Select a role** drop-down menu, search for **MCP Tool User** , and then click **MCP Tool User**.

  6. Click **Save**.

  7. Verify that the principal and the corresponding role are listed in the IAM page.




You have successfully granted an IAM role to a principal.

To learn more about other management access tasks, such as revoking IAM roles or granting multiple IAM roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) in the IAM documentation.

## Identity and Access Management conditions

Google Cloud remote MCP servers support [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview). Identity and Access Management conditions let you define and enforce conditional, attribute-based access control. This means you can grant access to principals only if specified conditions are met, such as the time of the request, the resource name, the resource type, or the tags attached to the resource.

You can use IAM Conditions in the following places:

  * Allow policy role bindings, including role bindings managed by Privileged Access Manager entitlements
  * Deny policy rules
  * Policy bindings for principal access boundary policies



For more information, see the [Attribute reference for Identity and Access Management Conditions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference).

## Google Cloud MCP servers roles and permissions

The following sections describe the IAM roles required for interacting with and controlling the use of Google Cloud MCP servers.

### Roles

To use Google Cloud MCP tools, the tool caller must be granted the MCP Tool User (`roles/mcp.toolUser`) role on the Google Cloud project, as well as the required roles for any Google Cloud products or services that you access. [Non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers) don't require the MCP Tool User role.

### Permissions

The following permissions are required to access Google Cloud services through MCP:

  * `mcp.tools.call`



## What's next

  * [Prevent read-write MCP tool use](https://docs.cloud.google.com/mcp/prevent-read-write-tool-use)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
