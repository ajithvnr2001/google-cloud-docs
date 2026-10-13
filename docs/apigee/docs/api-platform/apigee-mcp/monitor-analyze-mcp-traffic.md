---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/
title: Monitor and analyze MCP traffic with Apigee API hub API insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:56.682446+00:00
---

# Monitor and analyze MCP traffic with Apigee API hub API insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Monitor and analyze MCP traffic with Apigee API hub API insights Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to monitor and analyze traffic to your MCP Discovery Proxies using the API insights dashboards in Apigee API hub.

**Note:** API insights is not available for Apigee organizations using VPC-SC or organizations with Data Residency enabled.**Note (Apigee hybrid):** The API insights dashboards described on this page show the same data on Apigee hybrid as on Apigee, because they are computed from Message Processor traffic. Access logs from the in-cluster MCP data plane are not included in these dashboards; if you need per-request logs from the MCP data plane itself, collect them from the MCP pods with your standard cluster log-shipping pipeline.

MCP in Apigee adds specific attributes (analytics fields) to API traffic. You can filter by these fields in using the **API insights** dashboards in **API hub**. 

  * **API style:** Filter by `MCP` to isolate agentic traffic from standard REST/SOAP traffic.
  * **MCP tool name:** View metrics for specific tools (such as `create_refund`, `check_order_status`) instead of viewing all requests for the general `/mcp` proxy endpoint.



The **API style** and **MCP tool name** filters are available for the following dashboards:

  * API performance
  * API error analysis
  * Latency analysis
  * Target performance



The **MCP tool name** filter is also available on the **Insights** tab of the **API proxy** details page in Google Cloud console. 

Filtering by the `API style` and `MCP tool name` fields allows you focus on agentic traffic only and to see the performance of individual tools rather than the aggregate traffic to the `/mcp` proxy endpoint.

## Accessing API insights in API hub

Before accessing API insights in API hub, confirm the following:

  * Make sure that Apigee API Analytics is enabled for your Apigee organization. For more information, see [Analytics services overview](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview#how-do-i-get-started).
  * Make sure that [API insights](https://docs.cloud.google.com/apigee/docs/apihub/configure-api-insights) is configured in API hub to view and analyze API data from your attached gateways.
  * Make sure you have the [required IAM roles](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview#iam-roles) to access API insights.



### View API insights for all proxies

To view API insights for all proxies, do the following:

  1. In the Google Cloud console, go to the **API insights** page in **Apigee API hub**.

[ Go to API insights](https://console.cloud.google.com/apigee/api-hub/api-insights)
  2. In the **Dashboards** pane, select a dashboard.
     * To filter the data in the dashboard by API style, use the **API style** filter dropdown to select **MCP**. 
     * To filter the data in the dashboard by MCP tool name, use the **MCP tool name** filter dropdown to select your MCP tool name. 



### View API insights for a specific proxy

To view API insights for a specific proxy, do the following:

  1. In the Google Cloud console, go to the **APIs** page in **Apigee API hub**. [ Go to APIs](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Select the name of the proxy for which you want to view API insights.
  3. Click the **Insights** tab.
  4. To filter the data in the dashboard by MCP tool name for the selected proxy, use the **MCP tool name** filter dropdown to select your MCP tool or tools.



For more detailed information about using API insights, see [API insights dashboards](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard#api-performance).

## What's next

Learn more about MCP in Apigee in [Apigee MCP overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview).

For Apigee hybrid, see [Enable MCP in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
