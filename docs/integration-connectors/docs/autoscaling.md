---
url: https://docs.cloud.google.com/integration-connectors/docs/autoscaling/
title: About autoscaling in Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:52.110133+00:00
---

# About autoscaling in Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About autoscaling in Integration Connectors

This page describes autoscaling behavior in Integration Connectors. 

Integration Connectors, built on the same underlying infrastructure as some of Google Cloud's largest-scale services, offers autoscaling capabilities. This allows Integration Connectors to automatically scale the number of nodes based on the number of connections and the number of transactions that the nodes process.

## How autoscaling works in Integration Connectors

Integration Connectors automatically scales the number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) based on your usage. To reserve capacity and bypass automatic scaling, adjust the minimum number of nodes for a connection. A connection processing more transactions needs more nodes. A connection processing fewer transactions needs fewer nodes. To configure the node values:

  * If you are a pay-as-you-go customer, configure the minimum and maximum node values when you create or edit a connection.
  * If you have a subscription, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. Before increasing the minimum number of nodes to improve throughput, ensure your backend systems can handle the increased traffic.

Integration Connectors adheres to defined quotas and limits, which you can request increases for. For more details, see the [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas) documentation.

### Monitor Integration Connectors Usage

Integration Connectors automatically exports metrics to Cloud Monitoring. These metrics provide insights into connection usage, performance, and health. Use these metrics to understand and optimize autoscaling behavior. The following table lists Integration Connectors metrics for monitoring connection usage and health:

Metric name | Description  
---|---  
Connection state | The current state of your connections, such as active or inactive.  
Request count | The number of requests made through your connections.  
Active nodes | The number of active nodes for your connections.  
Connection status | The detailed status of individual connections.  
  
For more information, see [Monitor connectors](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
