---
url: https://docs.cloud.google.com/sap/docs/sap-datasphere-replication-bigquery-overview/
title: Replicating data from SAP S/4HANA to BigQuery through SAP Datasphere \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:44.906872+00:00
---

# Replicating data from SAP S/4HANA to BigQuery through SAP Datasphere  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-datasphere-replication-bigquery-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Replicating data from SAP S/4HANA to BigQuery through SAP Datasphere Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview about how you can replicate data from SAP S/4HANA to BigQuery through [SAP Datasphere](https://www.sap.com/india/products/technology-platform/datasphere.html). SAP Datasphere offers robust data transformation capabilities and ensures the data is loaded correctly into BigQuery. It uses the [BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api) to write the data to BigQuery dataset in near-real time.

## Replication methods

To read data from the SAP S/4HANA source system, you can use one of the following replication methods:

  * **CDS-based replication** : This method uses Core Data Services (CDS) views, which are semantically rich and offer predefined models of your business data within SAP S/4HANA.

  * **SLT-based replication** : This method directly replicates underlying database tables from your SAP S/4HANA system, typically using SAP Landscape Transformation (SLT) as the replication technology. The replicated tables can then be used as a data foundation for [Google Cloud Cortex Framework](https://docs.cloud.google.com/solutions/cortex).




### Key differences and considerations

The following table summarizes the key differences between the two replication methods:

Feature | CDS-based replication | SLT-based replication  
---|---|---  
**Data representation** | Provides business-oriented data views, often combining data from multiple tables into meaningful structures. | Provides direct access to raw table structures. If you require granular control over data or need to replicate custom tables, then this replication method is appropriate for your needs.  
**Ease of use** | If you're using the pre-delivered CDS views in SAP Datasphere, then setting up the replication becomes more straightforward. | Might require more technical configurations, especially for initial setup of SLT and handling table dependencies.  
**Flexibility** | Less flexible if you need to replicate custom tables or tables not exposed through standard CDS views. | Offers greater flexibility to replicate any table, including custom-developed ones.  
**Performance** | 

  * Causes extra CPU consumption on the production database due to business logic and delta calculations. This method can require additional CPU resources for your SAP database.
  * Less data is transferred due to possible pre-aggregations in CDS view logic.

| 

  * Replicates entire tables, leading to increased network traffic, and hence this method is networking-intensive. However, it requires less consumption of the database CPU resources.
  * More data is transferred as full tables are replicated without pre-aggregations.

  
**Google Cloud Cortex Framework compatibility** | To generate extractor-enabled CDS views that are compatible with the Google Cloud Cortex Framework, you can use the community-developed utility available at [GitHub](https://github.com/GoogleCloudPlatform/professional-services/tree/main/examples/sap-bigquery-cds-generator). **Note:** You assume the responsibility for using the community resources. Google Cloud does not offer support for issues arising from the use of community resources. | Fully compatible with pre-delivered technical accelerators.  
  
### Choose your replication method

The best replication method for you depends on several factors, including the intended use case and other considerations, such as the following:

  * **Business requirements** : If you primarily need standard business data and want a quick setup, then CDS-based replication is likely a good fit. If you require more specialized data or have heavily customized tables, then consider SLT-based replication.

  * **Cortex Framework compatibility**. If you want to use Cortex Framework, then use SLT-based replication.

  * **Technical expertise** : CDS-based replication is easier to work with for people with SAP Basis or data replication expertise.

  * **Data volume and complexity** : For multi-terabyte data or complex table relationships, SLT-based replication might be more scalable.


**Note:** Irrespective of the replication method you choose, SAP Datasphere acts as a powerful tool for orchestrating the replication process, providing data transformations, and ensuring that the data is loaded correctly into BigQuery. You can set up replication using both methods, and choose to run your replication using the method that best suits your use case and requirements.

## What's next

  * For information about how to set up CDS-based replication, see [Set up CDS-based replication: SAP S/4HANA to BigQuery through SAP Datasphere](https://docs.cloud.google.com/sap/docs/sap-datasphere-cds-replication-bigquery).
  * For information about how to set up SLT-based replication, see [Set up SLT-based replication: SAP S/4HANA to BigQuery through SAP Datasphere](https://docs.cloud.google.com/sap/docs/sap-datasphere-slt-replication-bigquery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
