---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-agent-registry-integration/
title: Manage Agent Registry integration \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:23.662391+00:00
---

# Manage Agent Registry integration  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-agent-registry-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage Agent Registry integration Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

API hub allows you to automatically synchronize Model Context Protocol (MCP) tools and server metadata with Agent Registry. This integration enables AI agents to discover and utilize the MCP-styled APIs registered in your hub.

**Note:** This feature is enabled by default and your MCP tools and server metadata are automatically synced to Agent Registry. 

## Enable Agent Registry integration

### Console

  1. In the Google Cloud console, click **API hub > Settings**.
  2. Select the **Actions** tab.
  3. In the **Agent Registry integration** section, switch the **Sync to Agent Registry** toggle to **On**.



When you enable sync, it may take some time for the process to complete and for your data to be reflected in Agent Registry.

## Disable Agent Registry integration

**Warning:** Disabling this sync stops the injection of new MCP tools and server metadata and removes all previously synced API hub-sourced content from Agent Registry. 

### Console

  1. In the Google Cloud console, click **API hub > Settings**.
  2. Select the **Actions** tab.
  3. In the **Agent Registry integration** section, switch the **Sync to Agent Registry** toggle to **Off**.
  4. In the confirmation dialog, click **Confirm** to stop the sync and remove existing data from the registry.



## Limitations

  * API hub does not sync APIs to Agent Registry whose style is manually set to MCP. Also, API hub does not remove data from Agent Registry when an API is manually converted from an MCP-style to a non-MCP style.
  * API hub will not sync data for deployments linked to multiple API versions, because Agent Registry does not support versioning. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
