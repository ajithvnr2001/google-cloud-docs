---
url: https://docs.cloud.google.com/integration-connectors/docs/connectorvsconnection/
title: Connector versus connection \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:59.696983+00:00
---

# Connector versus connection  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectorvsconnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connector versus connection

This page describes the difference between the terms `connector` and `connection`. Before using Integration Connectors, it is important for you to understand this difference.

A **connector** provides connectivity to a specific type of data source. And each data source has a different connector. For example, the Salesforce connector provides connectivity to a Salesforce instance and a BigQuery connector provides connectivity to a BigQuery instance. However, a connector in itself doesn't connect to any data source. To access the data source instance, you need to create a connection using the correct type of connector.

You can think of a **connection** as an instance of a connector type that actually accesses the data source. To access a data source, you must create a connection to the data source by using the corresponding connector. For example, to access a Salesforce instance, you must create a Salesforce connection. Based on your requirement, you can create multiple connections for a connector type, and each connection is uniquely identified by its name. For example, you can have `salesforce_connection_01`, `salesforce_connection_02`, and `salesforce_connection_03` connections, where each connection accesses a different Salesforce instance or uses different credentials in the same instance.

Therefore, at a fundamental level, if you are managing your connectors, it means you are in effect managing the connections.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
