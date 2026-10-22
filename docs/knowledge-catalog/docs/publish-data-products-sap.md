---
url: https://docs.cloud.google.com/knowledge-catalog/docs/publish-data-products-sap/
title: Publish data products to SAP \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:28.569462+00:00
---

# Publish data products to SAP  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/publish-data-products-sap/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Publish data products to SAP Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you publish data products to SAP Business Data Cloud (BDC) by using BigLake Delta Sharing. Users in the SAP ecosystem can then discover and consume your Google Cloud data assets as read-only federated tables without moving or replicating data.

## Overview

The integration between Knowledge Catalog and SAP BDC relies on an open-protocol approach using Delta Sharing. When you publish a data product to SAP, Knowledge Catalog facilitates the creation of a secure sharing link.

Key technical aspects of this integration include the following:

  * **Federated access** : Underlying data assets, such as Apache Iceberg REST catalog tables, are presented in SAP as read-only federated tables and queried in real-time from Google Cloud storage.
  * **Delta Sharing** : Knowledge Catalog acts as a Delta Sharing server, providing a standard interface for external clients like SAP to access BigLake and Iceberg tables.
  * **No data movement** : Your data stays in its original location in Google Cloud without replication, which helps lower latency and maintain a single source of truth. Only the metadata and secure access protocols are shared with the SAP environment.
  * **Security** : Authentication and authorization are handled using Workload Identity Federation, ensuring that only authorized SAP users can access the data based on the permissions granted in Google Cloud.



## Before you begin

Before you publish a data product to SAP BDC, complete the following prerequisites:

### Enable APIs

Enable the BigLake API on your Google Cloud project.

[Enable the BigLake API](https://console.cloud.google.com/apis/library/biglake.googleapis.com)

### Delta Sharing and catalog requirements

Ensure that your environment meets the following requirements:

Requirement | Details | Reference  
---|---|---  
**Delta Sharing catalog** | You must have a BigLake Delta Sharing catalog created and enrolled with your SAP BDC environment in the same project and region as your data product. | See [Set up cross-cloud connection for SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse-sap-bdc).  
**Workload Identity Federation** | You must configure a Workload Identity Pool and Provider to trust the SAP BDC OIDC issuer. | See [Configure Workload Identity Federation](https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc#configure-wif).  
**Data product assets** |  The data product must contain at least one supported data asset (such as an Apache Iceberg REST catalog table) and a maximum of 50 tables. All Iceberg tables in the data product must meet the following constraints: 

  * Belong to the same Iceberg REST catalog
  * Have primary keys defined
  * Contain at least one row of data

| See [About data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).  
  
### Required roles

To get the permissions that you need to manage and publish a data product to SAP BDC, ask your administrator to grant you the following IAM roles on the Google Cloud project: 

  * Manage data products in the Google Cloud console: [Dataplex Data Products Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`) 
  * Publish data products to SAP BDC: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Publish a data product to SAP BDC

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the name of the data product that you want to publish.

  3. On the data product details page, click **Share** , and then select **Publish to SAP**.

**Note:** The **Share** button and the **Publish to SAP** option are only visible if the feature is enabled for your project and there is at least one enrolled Delta Sharing catalog in your project and region. If these options are missing, verify that you have fulfilled the prerequisites.
  4. In the **Publish data product to SAP** pane, specify the following:

     * **Share name** : Enter a unique name for the share to be created in SAP.
     * **Delta catalog** : Select the enrolled Delta Sharing catalog from the list.
     * **Workload identity** : Enter the full resource name of the Workload Identity Provider configured for SAP BDC. Use the following format:
    
    projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID
    

Replace the following:

     * `PROJECT_NUMBER`: your Google Cloud project number
     * `POOL_ID`: the ID of your Workload Identity Pool
     * `PROVIDER_ID`: the ID of your Workload Identity Provider.
  5. Click **Publish**.




Knowledge Catalog initiates the publishing process using the BigLake API. Once successful, the data product is discoverable as federated tables within SAP BDC.

###  gcloud 

See [Publish data to SAP BDC](https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc#knowledge-catalog-data-product).

## What's next

  * Learn more about [managing Knowledge Catalog data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).
  * Learn how to [set up cross-cloud connection for SAP BDC](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse-sap-bdc).
  * Learn more about [configuring Workload Identity Federation](https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc#configure-wif).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
