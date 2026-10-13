---
url: https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc/
title: Publish Data Products to SAP BDC \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:49.405487+00:00
---

# Publish Data Products to SAP BDC  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Publish Data Products to SAP BDC Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure Google Cloud to let SAP Business Data Cloud (BDC) access BigQuery data without copying it. You do this by setting up the Apache Iceberg REST catalog endpoint in the Lakehouse runtime catalog or a [Knowledge Catalog Data Product](https://docs.cloud.google.com/dataplex/docs/data-products-overview) to share with SAP.

For an overview of this integration and its use cases, see [About SAP BDC integration](https://docs.cloud.google.com/lakehouse/docs/sap-bdc-overview).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the BigLake and Dataplex APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,dataplex.googleapis.com)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the BigLake and Dataplex APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,dataplex.googleapis.com)

  6. **Cloud Storage bucket** : Create a Cloud Storage bucket to store your Iceberg metadata and data files. For instructions, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets). All resources, including the backend bucket, must exist in the same region to avoid configuration pipeline failures.
  7. **Apache Iceberg REST catalog** : Set up an Apache Iceberg REST catalog endpoint in the Lakehouse runtime catalog with credential vending enabled, containing the namespaces and tables you want to share. This catalog uses the Cloud Storage bucket as its warehouse. For instructions, see [Set up the Iceberg REST catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog).
  8. **Delta Sharing connection catalog** : Prepare an enrolled Delta Sharing connection catalog for your SAP BDC connection. This is the same catalog created during your initial setup for sharing data from SAP BDC to BigQuery; you don't need to create a new one. For instructions, see [Set up cross-cloud connection for SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc).
  9. **Workload Identity Federation (WIF)** : Prepare to configure WIF to trust the SAP BDC authentication issuer. You set this up in the following section.



### Required roles

To get the permissions that you need to configure Workload Identity Federation and publish data, ask your administrator to grant you the following IAM roles on your project: 

  * Manage Workload Identity Federation: [Identity and Access Management (IAM) Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`) 
  * Publish data products: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) 
  * View catalog metadata (granted to the WIF principal): [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) 
  * Consume service quota (granted to the WIF principal): [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## General workflow

**Note:** Specific VPC configuration or allowlisting might be required to make the publish-back work.

To publish data to SAP BDC, follow these steps:

  1. **Configure Workload Identity Federation:** Create a Workload Identity Federation pool and provider to establish trust with the SAP BDC OIDC issuer.
  2. **Grant roles to the federated principal:** Grant the federated identity permissions to view catalog metadata and consume service quota.
  3. **Publish data:** Publish your Apache Iceberg REST catalog or a Knowledge Catalog Data Product to SAP BDC using the `gcloud` CLI.



## Configure Workload Identity Federation

To let SAP BDC access your borderless Lakehouse resources without requiring exported service account keys, configure Workload Identity Federation (WIF). This establishes trust between Google Cloud and the SAP BDC OIDC issuer.

Follow these steps to set up the WIF pool and provider:

### Get the issuer URI

Retrieve the OIDC issuer URI from your Delta Sharing connection catalog. You need this URI to configure the WIF provider.
    
    
    gcloud biglake delta-sharing catalogs describe CONNECTION_CATALOG_ID \
        --project="PROJECT_ID"

In the command output, locate the `federatedIdentityIssuer` field, which contains the issuer URI.

### Create the workload identity pool

Create a workload identity pool to group external identities.
    
    
    gcloud iam workload-identity-pools create POOL_ID \
        --location="global" \
        --display-name="POOL_DISPLAY_NAME" \
        --project="PROJECT_ID"

### Create the OIDC provider

Create an OIDC provider within the pool to define trust and map token claims.
    
    
    gcloud iam workload-identity-pools providers create-oidc PROVIDER_ID \
        --location="global" \
        --workload-identity-pool="POOL_ID" \
        --issuer-uri="ISSUER_URI" \
        --attribute-mapping="google.subject=assertion.sub.split('://')[1].split('.')[0]" \
        --project="PROJECT_ID"

**Note:** The specific `--attribute-mapping` shown is required to correctly extract the subject from the SAP BDC token.

### Grant roles to the federated principal

Authorize the federated identity from the trusted pool to call required Google APIs. You can authorize a specific subject UUID or the entire pool.

To authorize a specific subject (recommended):
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="roles/biglake.viewer" \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/WIF_SUBJECT"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="roles/serviceusage.serviceUsageConsumer" \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/WIF_SUBJECT"

Replace `WIF_SUBJECT` with the UUID issued by the SAP-side issuer for the workload.

To authorize every identity in the pool (less restrictive, suitable for test environments):
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="roles/biglake.viewer" \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="roles/serviceusage.serviceUsageConsumer" \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*"

## Publish data to SAP BDC

You can publish an Apache Iceberg REST catalog or a Knowledge Catalog Data Product containing Iceberg tables using Google Cloud console or Google Cloud CLI.

###  Iceberg REST catalog 

Before publishing, verify your Iceberg tables have primary keys defined using `identifier-field-ids` in their Iceberg table metadata and at least one row, because SAP BDC requires both for queries. Any column referenced in `identifier-field-ids` must be set to `required: true` (non-nullable) in the Iceberg schema. If your table does not have primary keys or contains nullable key fields, see [Update Iceberg table schema for primary keys](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-sap-bdc-access#primary-key-required) to update them using the BigLake REST API.

###  Console 

  1. In the Google Cloud console, go to the **Lakehouse Runtime Catalog** page.

[Go to Lakehouse Runtime Catalog](https://console.cloud.google.com/biglake)

  2. In the navigation panel, expand your project and select the **Delta Catalog** (connection catalog) to use for publishing.

  3. Click **Publish Data Product**.

  4. Enter the required share details, including selecting the Iceberg REST catalog to publish.

  5. Click **Publish**.




###  gcloud 

  1. Verify the Apache Iceberg REST catalog endpoint exists and get its details:
         
         gcloud biglake iceberg catalogs describe ICEBERG_CATALOG_ID \
             --project="PROJECT_ID"

  2. Publish the Apache Iceberg REST catalog to SAP BDC. Note that the connection catalog, Iceberg catalog, and underlying Cloud Storage bucket must all reside in the same region.
         
         gcloud biglake data-product-sharing publish \
             --connection-catalog="projects/PROJECT_ID/catalogs/CONNECTION_CATALOG_ID" \
             --share="SAP_SHARE_NAME" \
             --sap-federated-identity-provider="projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID" \
             --iceberg-catalog="projects/PROJECT_ID/catalogs/ICEBERG_CATALOG_ID" \
             --title="TITLE_TEXT" \
             --short-description="SHORT_DESCRIPTION_TEXT" \
             --description="DETAILED_DESCRIPTION_TEXT" \
             --project="PROJECT_ID"

The published Apache Iceberg REST catalog is discoverable in SAP BDC and can be installed in SAP Datasphere as a [remote table](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/ea7cb802cbea47b39a441888873c3a49.html?locale=en-US&version=LATEST).

Replace the following:

     * `CONNECTION_CATALOG_ID`: the enrolled Delta Sharing connection catalog that was created during the initial setup for sharing data from SAP BDC to BigQuery. It is the same as the Delta Sharing catalog mentioned in the setup instructions; you don't need to create another one for publishing back.
     * `PROJECT_NUMBER`: your Google Cloud project number. The `--sap-federated-identity-provider` flag must use the project number, not the project ID.
     * `POOL_ID`: the WIF pool ID.
     * `PROVIDER_ID`: the WIF provider ID.
     * `TITLE_TEXT` and `SHORT_DESCRIPTION_TEXT`: required display values for the share in SAP BDC.
     * `DETAILED_DESCRIPTION_TEXT`: an optional detailed description. Don't enter the same text for the short description and the detailed description, because this is rejected by SAP. The publish operation is also rejected if the detailed description contains the exact short description as a substring. For example, if the short description is `Sales Data`, a detailed description of `Longer Sales Data details` is rejected because it contains `Sales Data`. However, a detailed description of "Longer Sales Information" is accepted.



###  Knowledge Catalog Data Product 

Alternatively, you can publish a [Knowledge Catalog Data Product](https://docs.cloud.google.com/dataplex/docs/data-products-overview). A Data Product is a curated, logical grouping of data assets (like tables or views) packaged together to solve specific business problems. Instead of publishing a full catalog, you can select specific Apache Iceberg tables, group them into a Data Product, and publish that curated collection to SAP BDC.

###  Console 

  1. In the Google Cloud console, go to the **Knowledge Catalog** page.

[Go to Knowledge Catalog](https://console.cloud.google.com/dataplex/govern/data-products)

  2. In the navigation menu, select **Data products**.

  3. Click the Data Product that you want to publish to open its details page.

  4. Click **Share** arrow_drop_down and select **Publish to SAP**.

  5. In the **Publish Data Product to SAP** pane, configure the following fields:

     * **Share name** : Enter the name for the share in SAP BDC.
     * **Delta catalog** : Select your enrolled Delta Sharing connection catalog.
     * **Workload identity** : Select or enter your Workload Identity Pool Provider.
  6. Click **Publish**.




###  gcloud 

  1. Create the Data Product:
         
         gcloud alpha dataplex data-products create DATA_PRODUCT_ID \
             --location="LOCATION" \
             --display-name="TITLE_TEXT" \
             --description="SHORT_DESCRIPTION_TEXT" \
             --owner-emails="OWNER_EMAIL" \
             --project="PROJECT_ID"

The `--display-name` maps to the `title` in SAP BDC, and `--description` maps to the `short_description`.

  2. Link an Apache Iceberg table asset managed by Lakehouse to the Data Product:
         
         gcloud alpha dataplex data-products data-assets create DATA_ASSET_ID \
             --data_product="DATA_PRODUCT_ID" \
             --location="LOCATION" \
             --resource="//biglake.googleapis.com/projects/PROJECT_ID/catalogs/ICEBERG_CATALOG_ID/namespaces/NAMESPACE_NAME/tables/TABLE_NAME" \
             --project="PROJECT_ID"

When configuring assets in a Data Product, table assets must have primary keys defined using `identifier-field-ids` in their Iceberg table metadata (with all identifier columns marked as `required: true`) and at least one row. If your table does not have primary keys or contains nullable key fields, see [Update Iceberg table schema for primary keys](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-sap-bdc-access#primary-key-required) to update them using the BigLake REST API. All data assets in a single Data Product must belong to the same Apache Iceberg REST catalog. A Data Product can have a maximum of 50 tables, and must contain at least one valid data asset to publish. Iceberg tables might not appear in the Google Cloud console immediately.

  3. Optional: Verify the assets in your Data Product:
         
         gcloud alpha dataplex data-products data-assets list \
             --data_product="DATA_PRODUCT_ID" \
             --location="LOCATION" \
             --project="PROJECT_ID"

  4. Publish the Data Product to SAP BDC. Ensure that the connection catalog, Data Product, and underlying resources are in the same region.
         
         gcloud biglake data-product-sharing publish \
             --connection-catalog="projects/PROJECT_ID/catalogs/CONNECTION_CATALOG_ID" \
             --share="SAP_SHARE_NAME" \
             --sap-federated-identity-provider="projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID" \
             --data-product="projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID" \
             --project="PROJECT_ID"

The published Data Product is discoverable in SAP BDC and can be installed in SAP Datasphere as a [remote table](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/ea7cb802cbea47b39a441888873c3a49.html?locale=en-US&version=LATEST). In SAP BDC, the published Data Product inherits the title and short description set when creating the Knowledge Catalog Data Product.

Replace the following:

     * `CONNECTION_CATALOG_ID`: the enrolled Delta Sharing connection catalog that was created during the initial setup for sharing data from SAP BDC to BigQuery. It is the same as the Delta Sharing catalog mentioned in the setup instructions; you don't need to create another one for publishing back.
     * `PROJECT_NUMBER`: your Google Cloud project number. The `sap-federated-identity-provider` must use the project number, not the project ID.
     * `POOL_ID`: The WIF pool ID.
     * `PROVIDER_ID`: the WIF provider ID.
     * `DATA_PRODUCT_ID`: the ID of your Knowledge Catalog Data Product.
     * `LOCATION`: the location of your Knowledge Catalog Data Product.
     * `SAP_SHARE_NAME`: the name of the share in SAP BDC.



## Access Google Cloud data in SAP BDC

After you publish your data to SAP BDC, you can access Google Cloud data natively in the SAP environment. For more information about installing and consuming Data Products in SAP as remote tables, see [Installing Data Products](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/ea7cb802cbea47b39a441888873c3a49.html?locale=en-US&version=LATEST) in the SAP documentation.

## What's next

  * [Troubleshoot SAP BDC access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-sap-bdc-access).
  * [Installing Data Products](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/ea7cb802cbea47b39a441888873c3a49.html?locale=en-US&version=LATEST) in the SAP documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
