---
url: https://docs.cloud.google.com/lakehouse/docs/sap-bdc-overview/
title: About SAP Business Data Cloud integration \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:48.767327+00:00
---

# About SAP Business Data Cloud integration  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/sap-bdc-overview/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  About SAP Business Data Cloud integration Stay organized with collections  Save and categorize content based on your preferences. 

Borderless Lakehouse lets you connect Google Cloud analytics with your SAP environment. This integration unifies your data analytics by connecting external data sources with your existing Google Cloud environment.

This integration lets you use BigQuery's analytical power directly on your SAP data without moving it. The SAP Business Data Cloud (BDC) instance acts as the central system that governs and provides data from all SAP applications, including finance, supply chain, and HR.

You can manage access to your federated data for several use cases:

  * **Unified analytics:** Analyze SAP data alongside other data in BigQuery.
  * **No data copies:** Reduce complexity and cost by querying data in place.
  * **Use the BigQuery ecosystem:** Use BigQuery ML, Looker, and other tools with your SAP data.
  * **Fresh data:** Access the most current data available in SAP BDC.



## Integration workflows

The integration between Lakehouse and SAP BDC supports two workflows:

### SAP to Google Cloud (Federation)

In this workflow, you query data residing in SAP BDC directly from BigQuery. This is handled using a Federated Delta Lake Catalog that communicates with SAP BDC using the Delta Sharing protocol.

  * Discover available tables and schemas live.
  * Run queries against live SAP data without moving it into Google Cloud.



For more information, see [Set up cross-cloud connection for SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc) and [Query SAP Business Data Cloud data](https://docs.cloud.google.com/lakehouse/docs/query-sap-data). For information on the SAP configuration, see [Provisioning SAP Business Data Cloud Connect](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provisioning-sap-bdc-connect?locale=en-US&version=LATEST) and [Working with Data Products in SAP Business Data Cloud Connect](https://help.sap.com/docs/business-data-cloud/sap-business-data-cloud-connect/working-with-data-products-in-sap-business-data-cloud-connect?locale=en-US&version=LATEST) in the SAP documentation.

### Google Cloud to SAP (Publishing)

In this workflow, you can publish or share data managed by Lakehouse or BigQuery to SAP BDC. This lets SAP users and applications consume Google Cloud data natively.

  * Publish an Iceberg REST Catalog or a Knowledge Catalog Data Product to SAP.



Published assets are discoverable in SAP BDC and can be installed in SAP Datasphere as [remote tables](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/ea7cb802cbea47b39a441888873c3a49.html?locale=en-US&version=LATEST).

For more information, see [Publish BigQuery data to SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc). For information on installing these products in SAP, see [Installing Data Products](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/ea7cb802cbea47b39a441888873c3a49.html?locale=en-US&version=LATEST) in the SAP documentation.

## How SAP BDC connects to Lakehouse

SAP BDC connects to Lakehouse using the Delta Sharing protocol to expose data to BigQuery without moving it.

### Core concepts

  * **Federated Delta Lake Catalog:** A Lakehouse catalog type that connects to SAP BDC using the Delta Sharing protocol.
  * **Catalog ID:** A unique identifier for the Lakehouse catalog resource in your Google Cloud project.
  * **Federated Catalog:** A mechanism where BigQuery continuously queries the remote SAP BDC catalog for a current list of shares, schemas, and tables. This prevents stale or manually copied metadata.
  * **Connection:** The mechanism in the Lakehouse catalog that links and authenticates BigQuery and SAP BDC.



### Data hierarchy

SAP BDC data is organized into a five-level hierarchy in BigQuery: `PROJECT_ID.CATALOG_ID.SHARE_NAME.SCHEMA_NAME.TABLE_NAME`. This maps to the Delta Sharing protocol used by SAP BDC.

  * **Catalog ID** (Lakehouse): The connection resource in Google Cloud that acts as the top-level container for all shared data from a single SAP BDC Connector.
  * **Share** (or _SAP Data Product_): A logical grouping of tables shared for consumption. This maps to a Delta Sharing _Share_ , the first namespace level under the Catalog in BigQuery.
  * **Schema** (Delta Schema): The second namespace level contained within a _Share_.
  * **Table** (SAP Table): The granular data object inside a Schema that contains the SAP BDC data.
  * **SAP BDC Connector:** An SAP BDC configuration that authorizes access from a specific Google Cloud project.



## What's next

  * [Set up cross-cloud connection for SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc).
  * [Query SAP Business Data Cloud data](https://docs.cloud.google.com/lakehouse/docs/query-sap-data).
  * [Publish Data Products to SAP BDC](https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
