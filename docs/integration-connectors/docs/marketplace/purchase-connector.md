---
url: https://docs.cloud.google.com/integration-connectors/docs/marketplace/purchase-connector/
title: Purchase and use a Marketplace connector \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:01.193917+00:00
---

# Purchase and use a Marketplace connector  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/marketplace/purchase-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Purchase and use a Marketplace connector

This page describes how to purchase, deploy, and use a Marketplace connector.

  1. Navigate to the Marketplace connector page from either Integration Connectors or Application Integration. 
     * Navigate from Integration Connectors: In the [Google Cloud console](https://console.cloud.google.com/), go to the **Integration Connectors > Marketplace connectors** page.
     * Navigate from Application Integration: In the [Google Cloud console](https://console.cloud.google.com/), go to the **Application** **Integration > Marketplace connectors** page.
  2. Search for the Marketplace connector that you want to purchase or select the Marketplace connector from the existing list of connectors in the **Marketplace connectors** page.
  3. Click on the Marketplace connector to read the description and pricing information.
  4. Click **Launch**.



### Deploy a connector

After you purchase a Marketplace connector, do the following:

  1. Specify the deployment configuration. For information, see [Deploy products](https://docs.cloud.google.com/integration-connectors/docs/marketplace/h/marketplace/docs/deploy-products).
  2. Click **Deploy**.



### Set up private connectivity

After you deploy the connector, set up private connectivity for the connector. For information, see [Configure private connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-managed-services#configure-private-connectivity). When you create a connection, in the **Destination** section, you will specify the host address or the endpoint attachment. 

### Use the Marketplace connector to create a connection

After you deploy a Marketplace connector, you can create a connection using the connector.

#### Create a connection in Integration Connectors

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Connector** section, select the Marketplace connector that you want to use. If you haven't purchased the Marketplace connector, a message appears indicating that you need to purchase the connector. 
  4. Specify the required connection details and then click **Create**.



#### Create a connection in Application Integration

  1. In the Google Cloud console, go to the **Application Integration** page.
  2. In your existing integration or new integration, click the **Connectors** task element on the designer to view the **Connectors** task configuration pane.
  3. Click **Configure connector**.
  4. In the **Connection** field, click **Create connection**.
  5. In the **Select connection** section, select the region of the connection.
  6. In the **Connector** field, select the Marketplace connector that you want to use. If you haven't purchased the Marketplace connector, a message appears indicating that you need to purchase the connector. 
  7. Specify the required connection details and then click **Create**.



### System limitations

The Marketplace connector can process 100 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
