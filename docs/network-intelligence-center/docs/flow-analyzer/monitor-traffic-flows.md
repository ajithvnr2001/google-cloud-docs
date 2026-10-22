---
url: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/monitor-traffic-flows/
title: Monitor your traffic flows \u00a0|\u00a0 Network Intelligence Center - Flow Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:11.983579+00:00
---

# Monitor your traffic flows  |  Network Intelligence Center - Flow Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/monitor-traffic-flows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Flow Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)



#  Monitor your traffic flows Stay organized with collections  Save and categorize content based on your preferences. 

The following sections describe various ways that Flow Analyzer can help you.

## Scenario: Understand client-server traffic

As a network administrator, you want to understand who initiated the connection and visualize the traffic flow data in the form of client-server dependency.

### Access Flow Analyzer

You access Google Cloud console and go to Flow Analyzer. If Observability Analytics isn't enabled on the subnet, you'll see no data.

VPC Flow Logs must be enabled on the relevant subnet. The logs must be stored in the log bucket that you're using to view Flow Analyzer. Also note that this log bucket must be upgraded to use Observability Analytics.

Follow the instructions on the Flow Analyzer page to enable Observability Analytics.

### Build and run the query using the selected properties

  1. On the Flow Analyzer page, select the traffic aggregation and the time range for which you need to view the data.
  2. Because you want to know who initiated the connection, in the **Source** pane, select the following fields in the **Organize Flows by** box: **VPC subnetwork, IP, and Port**.



The **Highest data flows** chart and the **All data flows** table display the query results.

### View the details to understand the client-server traffic

The chart displays the top five highest traffic flows over time, when compared with the rest of the traffic. Spot trends such as traffic spikes using this chart.

You can use the time selector to specify the required time range. Decrease the value of the alignment period to get the required details.

If there are specific spikes in the traffic, learn more about any specific flow using the **Flow details** page.

### View specific traffic flow details

In the **All data flows** or **All latency flows** table, click **Details** for the flow that you want to investigate. The **Flow details** page that appears shows all the resources matching the selected filters and the traffic of these resources.

You can further drill down the query results using the remaining fields or properties available in VPC Flow Logs. On the **Flow details** page, the **drill down** panel provides details about the selected traffic flow including information such as the source, destination, traffic, and possible drill down options.

You can drill down further by splitting a selected traffic flow using any available extra field.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
