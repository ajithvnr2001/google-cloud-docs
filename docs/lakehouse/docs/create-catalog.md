---
url: https://docs.cloud.google.com/lakehouse/docs/create-catalog/
title: Create a catalog \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:25.369052+00:00
---

# Create a catalog  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/create-catalog/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Create a catalog Stay organized with collections  Save and categorize content based on your preferences. 

The Lakehouse runtime catalog lets you create [catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs#configuration) in borderless Lakehouse.

A catalog endpoint points to an underlying Cloud Storage bucket and provides a metadata layer that lets query engines and open source workloads interact directly with your tables. When you create a catalog endpoint, you can choose between end-user credentials and credential vending mode for storage access delegation.

## Before you begin

  1. Read [About the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs) to understand how the Lakehouse runtime catalog works and the limitations for the service.

Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)




### Required roles

To get the permissions that you need to create a catalog and register tables, ask your administrator to grant you the following IAM roles: 

  * Create a catalog: 
    * [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on your project
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on your project
  * Create (register) tables: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on your project. Registering tables requires the specific table registration permission (`biglake.tables.register`), which is included in the BigLake Admin role. 
  * Use the auto-provisioned catalog service account in credential vending mode: [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the target Cloud Storage buckets. After creating the catalog, explicitly grant the Storage Object User role (`roles/storage.objectUser`) on your storage buckets to the auto-provisioned service account. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** Creation of the auto-provisioned catalog service account is [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency), which means that it takes time for the service account to propagate through the system. If you try to grant roles to the service account immediately after creation, the request might fail. To learn how long it takes, on average, for access changes to propagate, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Create a catalog

Follow these steps to create a catalog based on your preferred credential mode and bucket type. For more information about the different catalog types, see [About the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#warehouse-storage-locations).

**Note:** When creating or managing a multiple-bucket catalog in Google Cloud, specify Cloud Storage paths (`gs://`) for the default and restricted storage locations. The `bl://projects/PROJECT_ID/catalogs/CATALOG_ID` URI format is used exclusively during client configuration to identify the catalog warehouse when connecting from query engines (such as Apache Spark or Trino).

###  Console 

**Create a multiple-bucket catalog (recommended)**

This configuration lets your catalog associate multiple buckets and lets you name your catalog independently of any bucket name.

  1. Open the **Lakehouse** page in the Google Cloud console.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click **Create catalog** , and then select **Lakehouse runtime catalog**.

  3. For **Catalog type** , select **Iceberg Rest Catalog**.

  4. For **Lakehouse catalog bucket options** , select **Multiple bucket catalog**.

  5. For **Default Catalog Cloud Storage path** , enter or browse for the Cloud Storage path to use with your catalog.

  6. For **Catalog ID** , enter a custom name for your catalog.

  7. For **Primary location** , select a location. The location must be near the regions of the main bucket.

  8. Click **Continue**.

  9. In the **Data paths** step, if you want to add additional Cloud Storage paths, click **Add path** and enter or browse for a path.

  10. Click **Continue**.

  11. For **Authentication method** , select **End-user credentials** or **Credential vending mode**.

  12. Click **Create**.

Your catalog is created, and the **Catalog details** page opens.

  13. If you selected **Credential vending mode** , perform the following additional steps:

     1. Under **Authentication method** , click **Set bucket permissions** (or **Set permissions for buckets** if your catalog uses more than one bucket).
     2. In the dialog, click **Confirm**.



### Create a single-bucket catalog

**Caution:** Avoid using the single-bucket configuration for new projects. This configuration restricts your catalog to a single bucket and locks the catalog name to the bucket name. 

  1. On the **Lakehouse** page, click **Create catalog** , and then select **Lakehouse runtime catalog**.
  2. For **Catalog type** , select **Iceberg Rest Catalog** or **Hive Metastore**.
  3. If you selected **Iceberg Rest Catalog** , for **Lakehouse catalog bucket options** , select **Single bucket catalog**.
  4. For **Default Catalog Cloud Storage bucket** (or **Default Catalog Cloud Storage path** for an Apache Hive catalog endpoint), enter or browse for the Cloud Storage bucket to use with your catalog. For a single-bucket catalog, you can only have one catalog per bucket, and the catalog name matches the bucket name.
  5. Click **Continue**.
  6. For **Authentication method** , select **End-user credentials** or **Credential vending mode**.
  7. Click **Create**.
  8. If you selected **Credential vending mode** , perform the following additional steps: 
     1. Under **Authentication method** , click **Set bucket permissions**.
     2. In the dialog, click **Confirm**.



###  gcloud 

**Create a multiple-bucket catalog (recommended)**

This configuration lets your catalog associate multiple buckets and lets you name your catalog independently of any bucket name.

To create a multiple-bucket catalog (recommended), run the [`gcloud biglake iceberg catalogs create`](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/create) command:
    
    
    gcloud biglake iceberg catalogs create \
        CATALOG_NAME \
        --project PROJECT_ID \
        --catalog-type biglake \
        --default-location DEFAULT_LOCATION \
        --credential-mode CREDENTIAL_MODE \
        [--restricted-locations RESTRICTED_LOCATIONS] \
        [--primary-location LOCATION]

Replace the following:

  * `CATALOG_NAME`: a name for your catalog. For multiple-bucket catalogs (recommended), this is your custom catalog name.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `DEFAULT_LOCATION`: the default storage location for the catalog. You can specify a bucket (`gs://my-bucket`) or a subpath (`gs://my-bucket/path`). All namespaces and tables in the catalog must reside under the specified path. For example, if you specify `gs://my-bucket/path`, you can't create namespaces or tables under `gs://my-bucket/another/path`.
  * `CREDENTIAL_MODE`: the authentication method. Use `end-user` for end-user credentials or `vended-credentials` for credential vending mode.

**Note** : If you use credential vending mode, you must explicitly grant the Storage Object User role (`roles/storage.objectUser`) on all associated storage buckets to your catalog's auto-provisioned Lakehouse runtime catalog service account.

  * `RESTRICTED_LOCATIONS`: optional: a comma-separated list of additional allowed storage locations, in the format `gs://my-bucket-1/...,gs://my-bucket-2/...`. If you specify a path (such as `gs://my-bucket/path`), any namespaces or tables within that bucket must be under that path. All configured Cloud Storage locations across the default location and restricted locations must be in the same geographic region group or jurisdiction (such as the United States, Europe, Canada, or Asia). For example, you can't mix a bucket in the US with a bucket in Europe. For a list of supported locations, see [Lakehouse locations](https://docs.cloud.google.com/lakehouse/docs/locations).

**Warning** : Avoid configuring overlapping paths with other catalogs to prevent unauthorized credential exposure. For more information, see [Storage across multiple buckets](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#storage-multiple-buckets).

  * `LOCATION`: optional: the primary region for the catalog to ensure interoperability with BigQuery. For Cloud Storage buckets in the US region (for example, `US` or `us-central1`) or the EU region (for example, `EU` or `europe-west4`), specify `US` or `EU` respectively to ensure the catalog is accessible and available for querying from the corresponding BigQuery multi-regions. For more information, see [Bucket and catalog regions](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#bucket_and_catalog_regions).




### Create a single-bucket catalog

**Caution:** Avoid using the single-bucket configuration for new projects. This configuration restricts your catalog to a single bucket and locks the catalog name to the bucket name. 

To create a single-bucket catalog, run the following command:
    
    
    gcloud biglake iceberg catalogs create \
        CATALOG_NAME \
        --project PROJECT_ID \
        --catalog-type gcs-bucket \
        --credential-mode CREDENTIAL_MODE

Replace the following:

  * `CATALOG_NAME`: a name for your catalog. For single-bucket catalogs, this matches the Cloud Storage bucket ID used with the catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CREDENTIAL_MODE`: the authentication method. Use `end-user` for end-user credentials or `vended-credentials` for credential vending mode.



###  REST 

**Create an Iceberg REST catalog**

To create a catalog management endpoint using the REST API, make a `POST` request to the [`CreateIcebergCatalog`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs/create) endpoint:
    
    
    POST /iceberg/v1/restcatalog/extensions/projects/PROJECT_ID/catalogs?iceberg-catalog-id=CATALOG_ID
    

The request body must contain an `IcebergCatalog` JSON payload defining the catalog configuration, such as the underlying Cloud Storage bucket warehouse and authentication mode.

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your Lakehouse runtime catalog.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
