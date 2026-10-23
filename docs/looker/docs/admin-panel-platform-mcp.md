---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-mcp/
title: Admin settings - Model Context Protocol (MCP) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:00.683853+00:00
---

# Admin settings - Model Context Protocol (MCP)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Model Context Protocol (MCP) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Provide feedback or report issues with this preview feature by sending a detailed email to [looker-mcp-support-external@google.com](mailto:looker-mcp-support-external@google.com).

The **Model Context Protocol (MCP)** page in the **Platform** section of the **Admin** menu lets you enable and govern the [Looker-managed MCP server](https://docs.cloud.google.com/looker/docs/mcp). The managed MCP server allows AI agents to securely connect to your Looker instance.

## Required roles

To access the **Model Context Protocol (MCP)** page, you must have the [**Admin**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) Looker role.

## Accessing the Model Context Protocol (MCP) page

The **Model Context Protocol (MCP)** page is available for Looker-hosted Looker (original) and Looker (Google Cloud core) instances. It isn't available for customer-hosted Looker (original) instances.

To access the **Model Context Protocol (MCP)** page, follow these steps:

  1. In the **Main menu** menu, click **Admin** to open the **Admin** menu.
  2. In the **Platform** section, select **MCP**.



## Model Context Protocol (MCP) settings

The **Model Context Protocol (MCP)** page includes several settings to enable or disable the AI tools that are available to agents that are connected to the MCP server. AI tools streamline an agent's ability to interact with Looker instances. A full list of AI tools appears in the [Use AI tools](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox#ai-tools) documentation.

### Enable all tools toggle

By default, all tools are disabled. Toggle the **Enable all tools** toggle to ON to enable all tools listed on the page as well as automatically enable any new tools that are added. Toggle **Enable all tools** toggle to OFF to have granular control of which tools to enable. When you switch the toggle, your change is saved automatically.

If you switch the **Enable all tools** toggle to ON, Looker remembers the previous state of the individual tool toggles. So, if you later switch the **Enable all tools** toggle to OFF, Looker reverts each individual tool's status back to the state it was in previously.

### Tool search

Enter a tool name, a category, or an access type in the **Search** field to filter the tools on the page.

### Granular tool control

When the **Enable all tools** toggle is switched to OFF, the tools on the **Model Context Protocol (MCP)** page can be individually enabled or disabled, allowing Looker admins to control which tools are available to AI agents. By default, all tools are disabled.

Tools are categorized into sections based on their function. For each tool, the access level to the Looker instance — read or write — is also shown. Hold your pointer over the information icon by the tool's name to see a description of each tool.

To enable a tool, follow these steps:

  1. Locate the tool in the list (for example, `looker_query`, `looker_update_project_file`).
  2. Toggle the switch to **Enabled**.



When you switch a toggle, your change is saved automatically.

As a security best practice, we recommend only enabling the tools required for your specific AI use cases.

### MCP clients and tool updates

**Tip:** After you have changed the enablement status for a tool, reconnect your AI clients to Looker to update the tools in your clients.

When a tool is enabled or disabled on the **Model Context Protocol (MCP)** page, MCP clients won't automatically refresh their list of tools. You must reconnect clients to the Looker-managed MCP server in order for the clients to access a newly enabled tool. If a tool is disabled, client calls to that tool will be rejected, but you must reconnect clients to the MCP server in order to stop exposing the tool to them.

## What's next

For more information on setting up and using the server, see the [Looker-managed MCP server](https://docs.cloud.google.com/looker/docs/mcp) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
