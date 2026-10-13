---
url: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc/
title: Set up cross-cloud connection for SAP Business Data Cloud \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:48.924385+00:00
---

# Set up cross-cloud connection for SAP Business Data Cloud  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up cross-cloud connection for SAP Business Data Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up a cross-cloud connection to query data in SAP Business Data Cloud (BDC) directly within Google Cloud. This integrates external data sources with your existing Google Cloud environment.

For an overview of how Lakehouse integrates with SAP BDC, see [About SAP BDC integration](https://docs.cloud.google.com/lakehouse/docs/sap-bdc-overview).

## Before you begin

  1. Review the [Lakehouse overview](https://docs.cloud.google.com/lakehouse/docs/introduction) to understand how Lakehouse manages data access.
  2. Read [about accessing cross-cloud data](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access) to understand how it works.
  3. Review the [supported catalogs](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#supported-catalogs) to verify requirements.
  4. Ensure your SAP administrator has access to your SAP BDC environment to configure the BDC Connect application.
  5. Ensure your target Google Cloud project runs on BigQuery Enterprise Plus edition.

  6. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)




### Required roles

To get the permissions that you need to set up cross-cloud access, ask your administrator to grant you the following IAM roles on your project: 

  * Manage Lakehouse catalogs: BigLake Admin (`roles/biglake.admin`) or BigQuery Admin (`roles/bigquery.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Limitations and considerations

This section lists the limitations and considerations for accessing cross-cloud data.

  * SAP delta sharing tables don't support fine-grained access control (FGAC).
  * Specific VPC configuration or allowlisting might be required depending on your network settings. For VPC Service Controls configurations, see [VPC Service Controls configuration for SAP BDC](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-config-sap-bdc).
  * Data Products with special characters like `/` or `-` are not supported and aren't available in BigQuery even if shared from SAP BDC to BigQuery. If you share a Data Product with special characters, this could cause the refresh to break on the Google side and require re-enrollment. Known SAP systems producing these Data Products include BW sources and SuccessFactors.
  * **Read-only:** Federated catalogs in Lakehouse are read-only views of the remote catalog. Resource manipulation (such as creating, updating, or deleting resources) are not supported and must be performed directly in the remote catalog.
  * **Data freshness:** The `--refresh-interval` flag for a federated catalog determines how often metadata is synchronized. The value must be `0s` (disabled) or at least `300s` (5 minutes). A catalog's background metadata refresh may take longer the more namespace and table resources there are. If the previous refresh overruns, the current refresh will be skipped, but the next refresh will be scheduled at the following interval. 
  * **Lakehouse caching:** Lakehouse caching is enabled automatically for all cross-cloud queries to save egress costs by storing data blocks locally in Google Cloud. Customer-managed encryption keys (CMEK) are not supported for caching; cached data is encrypted using Google-owned and Google-managed encryption keys. If the `constraints/gcp.restrictNonCmekServices` organization policy constraint is enforced on any table in the query, caching is automatically disabled for that query. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching). 
  * **Data residency and compliance:** Creating a federated catalog or connection in a Google Cloud region stores cached data at rest in that target region. If your remote cloud data resides in a different jurisdiction, ensure that cross-region caching complies with your organization's data residency and regulatory compliance requirements. 



## General workflow

To set up a cross-cloud connection for SAP BDC, follow these steps:

  * **Set up Enterprise Plus edition:** Enable BigQuery Enterprise Plus when querying your SAP BDC instance.
  * **Create the Lakehouse catalog:** A BigQuery Administrator creates an empty Delta Sharing catalog to connect to SAP BDC.
  * **Configure the connector in SAP for Me:** Your SAP administrator provisions a BDC Connect application instance.
  * **Update the catalog:** Complete the handshake by adding the endpoint and invitation code to the Lakehouse catalog.
  * **Install SAP BDC data products:** Your SAP data steward requests access and installs data products to the BDC Connect instance for BigQuery.
  * **Query data:** Query your federated data using BigQuery. Lakehouse caching is enabled automatically for queries to save egress costs.
  * **Configure permissions:** Use Identity and Access Management (IAM) to manage access.



## Set up BigQuery Enterprise Plus edition

This one-time setup lets BigQuery use Enterprise Plus to query your SAP BDC instance.

### Create an Enterprise Plus reservation

  1. Go to **BigQuery**.

[Go to BigQuery](https://console.cloud.google.com/)

  2. In the navigation menu, go to **Administration** > **Workload management**.

  3. Click **Create reservation**.

  4. For **Reservation name** , enter a name (for example, `enterprise-plus-sap-res`).

  5. For **Location** , select the region where your data resides. This must match the region used for the Lakehouse runtime catalog.

  6. For **Edition** , select **Enterprise Plus**.

  7. For **Max reservation size** , select the maximum number of slots that BigQuery can scale up to.

  8. For **Baseline slots** , enter `0` to prevent charges while not querying data.

  9. Expand **Advanced settings** , and then for **How to use idle slots?** , select **Predictable performance** to let BigQuery use idle and autoscaling slots up to the maximum reservation size.

  10. Click **Save**.




### Assign your project to the reservation

  1. In the **Capacity management** page, click the **Assignments** tab.
  2. Click **Create Assignment**.
  3. For **Select a resource** , choose the project, folder, or organization that runs the BigQuery jobs.
  4. For **Reservation** , select the Enterprise Plus reservation you created.
  5. For **Job type** , select **Query**.
  6. Click **Create**.



To verify, check the **Job Information** in the BigQuery Job History for any job run within that project.

## Set up federation

To query your data, set up a Lakehouse federated catalog that connects to your remote SAP BDC catalog. This initiates a handshake that establishes a trust relationship where the BigQuery service account acts as the identity for the Google Cloud project.

### Create the Lakehouse Delta Sharing catalog

Create an empty Delta Sharing catalog using the Google Cloud console or the `gcloud` CLI.

###  Console 

  1. In the Google Cloud console, go to the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. In the navigation menu, click **Runtime catalog**.

  3. Click **Create catalog** and select **Federated catalog**.

  4. In the **Catalog configuration** section, enter the following:

     * For **Federated catalog source** , select **SAP (Business Data Cloud)**.
     * For **Catalog name (in Lakehouse)** , enter a name for your catalog.
     * For **Data location** , select the Lakehouse region.
  5. Click **Continue**.

  6. Retrieve the Google Cloud Service Account ID displayed on the page and provide this ID to your SAP administrator.




###  gcloud 

  1. Create an empty Delta Sharing catalog:
         
         gcloud biglake delta-sharing catalogs create CATALOG_ID \
           --project="PROJECT_ID" \
           --location="REGION" \
           --refresh-interval="REFRESH_INTERVAL"

Replace the following:

     * `CATALOG_ID`: a name for your catalog.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Lakehouse region.
     * `REFRESH_INTERVAL`: Optional: the interval for refreshing metadata from the catalog, specified as a duration string with units (for example, `5m` for 5 minutes, `300s` for 300 seconds, or `1h` for 1 hour). If omitted, the refresh interval defaults to 5 minutes (`5m` or `300s`).
  2. Retrieve the Google Cloud Service Account ID to provide to your SAP administrator:
         
         gcloud biglake delta-sharing catalogs describe CATALOG_ID \
             --project="PROJECT_ID"




### Configure the connector in SAP for Me

Your SAP administrator must sign in to _SAP for Me_ and provision a new instance of the BDC Connect application:

  1. Enter the **Display Name**.
  2. Select or create a **Resource Group**.
  3. Allocate **BDC Capacity Units**.
  4. Enter the Google Cloud service account ID as the **External System Instance Identifier**.
  5. Select a **Region**. This must match the BDC Core region.
  6. Click **Finish**.



After completion, go to the tenant details view. Hold the pointer over the **View Tenant Notifications** button to get the **Activation Link** , which contains the **SAP Connector Endpoint** and the **SAP Invitation Code**.

Provide these to your BigQuery administrator.

For more information, see [Provisioning SAP Business Data Cloud Connect](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provisioning-sap-bdc-connect?locale=en-US&version=LATEST) in the SAP documentation.

### Update the catalog with SAP enrollment details

Update the catalog to complete the handshake using the Google Cloud console or the `gcloud` CLI.

###  Console 

  1. If you are not already on the **Connection details** page:

     1. In the Google Cloud console, go to the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

     2. In the navigation menu, click **Runtime catalog**.

     3. Select your SAP Delta Sharing catalog to open its **Catalog details** page.

     4. In the banner, click **Enroll catalog**.

  2. In the **Connection details** section, enter the following:

     * For **Connector endpoint** , enter the URL provided by your SAP administrator.
     * For **Invitation code** , enter the code provided by your SAP administrator.
  3. Click **Save**.




###  gcloud 
    
    
    gcloud biglake delta-sharing catalogs update CATALOG_ID \
        --project="PROJECT_ID" \
        --connector-endpoint="CONNECTOR_ENDPOINT" \
        --invitation-code="INVITATION_CODE" \
        --refresh-interval="REFRESH_INTERVAL"

Replace the following:

  * `CATALOG_ID`: the name of your catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CONNECTOR_ENDPOINT`: the URL provided by the SAP administrator.
  * `INVITATION_CODE`: the code provided by the SAP administrator.
  * `REFRESH_INTERVAL`: Optional: the interval for refreshing metadata from the catalog, specified as a duration string with units (for example, `5m` for 5 minutes, `300s` for 300 seconds, or `1h` for 1 hour). If omitted, the background metadata refresh interval defaults to 5 minutes (`5m` or `300s`).



### Add the connection to the BDC formation in SAP for Me

Your SAP administrator must sign in to _SAP for Me_ , and add the connection to the BDC formation:

  1. In **Customer Landscape** , select **Formations**.
  2. Select or create a formation for the SAP BDC instance.
  3. Click **Include Systems**.
  4. Select the SAP BDC Connect System, and click **Next Step**.
  5. Confirm the selected system and click **Include**.



After completion, it is required to synchronize the BDC formation.

## Install SAP BDC Data Products

Your SAP data steward must sign in to SAP Business Data Cloud and install data products for the BDC Connect instance associated with BigQuery. After access is approved and the data product is installed in SAP, it is discoverable as a Delta Sharing share in Google BigQuery.

For step-by-step instructions on requesting access and installing data products in SAP, see [Obtaining Access to Data Products through SAP Business Data Cloud Connect](https://help.sap.com/docs/business-data-cloud/sap-business-data-cloud-connect/sharing-data-products-from-sap-business-data-cloud-trough-sap-bdc-connect?ai=true&locale=en-US&version=LATEST) in the SAP documentation.

## What's next

  * [Query SAP Business Data Cloud data in BigQuery](https://docs.cloud.google.com/lakehouse/docs/query-sap-data).
  * [Troubleshoot SAP BDC access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-sap-bdc-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
