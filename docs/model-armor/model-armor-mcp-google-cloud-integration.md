---
url: https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration/
title: Integrate Model Armor with Google and Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:15.184568+00:00
---

# Integrate Model Armor with Google and Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Integrate Model Armor with Google and Google Cloud MCP servers Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to configure Model Armor to help protect your data and secure content when sending requests to Google Cloud services that expose Model Context Protocol (MCP) tools and servers.

Model Armor helps secure your agentic AI applications by sanitizing MCP tool calls and responses. This process mitigates risks such as prompt injection and sensitive data disclosure.

## Supported MCP servers

For a list of supported Google and Google Cloud MCP servers, see [Products with Model Armor support](https://docs.cloud.google.com/mcp/model-armor-supported-products#products-with-ma-support).

Model Armor floor settings won't apply if you call unsupported Google and Google Cloud MCP servers.

## Filter version

For the integration with Google and Google Cloud MCP servers, Model Armor uses the `v1` filter version. You can't override this setting.

## Data residency considerations

Your data residency requirements might be impacted, depending whether the MCP-supported service uses _cross-jurisdictional routing_ or _data residency compliant routing_. For more information, see [Integration with Google and Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/data-residency#mcp-servers).

## Before you begin

  1. Enable the API that you want to access through MCP. For more information, see [Enable supported products](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers).
  2. Enable the Model Armor API in your project. For more information, see [Enable APIs](https://docs.cloud.google.com/model-armor/configure-floor-settings#enable-apis).
  3. If you have data residency requirements, you must configure a log sink to route logs to a compliant storage location before you enable Cloud Logging in the next procedure. Configuring a log sink helps ensure that Model Armor logs are stored in buckets in the appropriate jurisdiction. For more information, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).



## Supported and unsupported MCP payloads

Model Armor sanitizes only the following MCP payloads:

  * `tools/call` request and response
  * `prompts/get` request and response
  * [MCP tool execution errors](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#error-handling) (target for prompt injection by malicious MCP tools authors)



Model Armor allows the following payloads without sanitization:

  * `tools/list`
  * `resources/*`
  * `notifications/*`
  * Streamable HTTP/SSE for MCP
  * MCP protocol errors (for example, all errors other than tool execution errors)



## Configure protection for Google and Google Cloud remote MCP servers

To help protect your MCP tool calls and responses you can use Model Armor floor settings. A floor setting defines the minimum security filters that apply across the project. This configuration applies a consistent set of filters to all MCP tool calls and responses within the project.

**Tip:** Don't enable the prompt injection and jailbreak filter unless your MCP traffic carries natural language data.

Set up a Model Armor floor setting with MCP sanitization enabled. For more information, see [Configure Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings).

**Note:** If the agent and the MCP server are in different projects, you can create floor settings in both projects (the client project and the resource project). In this case, Model Armor is invoked twice, once for each project.

See the following example command:
    
    
    gcloud model-armor floorsettings update \
    --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
    --enable-floor-setting-enforcement=TRUE \
    --add-integrated-services=GOOGLE_MCP_SERVER \
    --google-mcp-server-enforcement-type=INSPECT_AND_BLOCK \
    --enable-google-mcp-server-cloud-logging \
    --malicious-uri-filter-settings-enforcement=ENABLED \
    --add-rai-settings-filters='[{"confidenceLevel": "MEDIUM_AND_ABOVE", "filterType": "DANGEROUS"}]'

Replace `PROJECT_ID` with your Google Cloud project ID.

Note the following settings:

  * `INSPECT_AND_BLOCK`: The enforcement type that inspects content for the Google MCP server and blocks prompts and responses that match the filters.
  * `ENABLED`: The setting that enables a filter or enforcement.
  * `MEDIUM_AND_ABOVE`: The confidence level for the Responsible AI - Dangerous filter settings. You can modify this setting, though lower values might result in more false positives. For more information, see [Model Armor confidence levels](https://docs.cloud.google.com/model-armor/overview#ma-confidence-levels).



## Verify Model Armor protection

After you configure Model Armor protection for MCP servers, you can verify that it's working by sending a request that contains content that should be blocked and checking that Model Armor blocks it. The following steps assume that you have enabled Logging for Model Armor as described in Configure protection for Google and Google Cloud MCP servers.

  1. In the project where you enabled Model Armor protection, call an MCP tool with a harmful value in one of its parameters. For example, if you enabled the malicious URI filter, include a phishing test URL in a parameter, such as `http://testsafebrowsing.appspot.com/s/phishing.html`.
  2. Verify that the MCP tool call is blocked. Depending on the MCP server and client, you might receive an error or an empty response, indicating that the request was blocked by a security policy.
  3. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer)

  4. In the **Query** pane, enter the following query:
         
         resource.type="model-armor_managed_service"
         logName="projects/PROJECT_ID/logs/modelarmor.googleapis.com%2Fdetection"
         

Replace `PROJECT_ID` with your project ID.

  5. Click **Run query**.

  6. Examine the results in the **Query results** section. If Model Armor blocked the request, you see a log entry detailing the detected threat, such as `MALICIOUS_URI_DETECTED`.




## Disable scanning MCP traffic with Model Armor

To stop Model Armor from automatically scanning traffic to and from Google MCP servers based on the project's floor settings, run the following command:
    
    
    gcloud model-armor floorsettings update \
      --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
      --remove-integrated-services=GOOGLE_MCP_SERVER
    

Replace `PROJECT_ID` with the Google Cloud project ID. Model Armor doesn't automatically apply the rules defined in this project's floor settings to any Google MCP server traffic.

Model Armor floor settings and general configuration can impact more than just MCP. Because Model Armor integrates with services like Gemini Enterprise Agent Platform, any changes you make to floor settings can affect traffic scanning and safety behaviors across all integrated services, not just MCP.

## What's next

  * Learn more about [Model Armor](https://docs.cloud.google.com/model-armor/overview).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
