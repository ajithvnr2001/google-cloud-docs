---
url: https://docs.cloud.google.com/lakehouse/docs/update-catalog/
title: Update a catalog \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:47:10.901162+00:00
---

# Update a catalog  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/update-catalog/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Update a catalog Stay organized with collections  Save and categorize content based on your preferences. 

The Lakehouse runtime catalog lets you modify the properties of existing [catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs#configuration) in borderless Lakehouse.

For Apache Iceberg REST catalog endpoints, you can update the credential mode, default warehouse location, and catalog type. For example, you can upgrade a _single-bucket catalog_ to a _multiple-bucket catalog_ (recommended) so that your catalog can span multiple storage buckets.

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

To get the permissions that you need to update a catalog, ask your administrator to grant you the following IAM roles: 

  * All: 
    * [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on your project
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on your project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Update a catalog

You can update a catalog using the Google Cloud console, `gcloud`, or the REST API.

###  Console 

  1. In the Google Cloud console, open the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. In the row of the catalog that you want to update, click more_vert **More catalog actions > Edit**.

  3. Under **Catalog configuration** , modify the settings you want to update.

  4. Select **Save**.




###  gcloud 

**Option 1: Update catalog properties**

To update catalog properties (such as description or restricted locations), run the [`gcloud biglake iceberg catalogs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/update):
    
    
    gcloud biglake iceberg catalogs update CATALOG_ID \
        --project="PROJECT_ID" \
        [--description="DESCRIPTION"] \
        [--credential-mode="CREDENTIAL_MODE"] \
        [--restricted-locations="RESTRICTED_LOCATIONS"]

Replace the following:

  * `CATALOG_ID`: the ID of your Lakehouse runtime catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `DESCRIPTION`: (Optional) a description for the catalog.
  * `CREDENTIAL_MODE`: (Optional) the authentication method. Use `end-user` for **End-user credentials** or `vended-credentials` for **Credential vending mode**.
  * `RESTRICTED_LOCATIONS`: (Optional) a comma-separated list of additional allowed storage buckets or paths. Caution: If you specify multiple overlapping paths or buckets, this can lead to metadata conflicts, accidental data overwrites, or security issues like permission leakage.



**Option 2: Upgrade a single-bucket catalog to multiple-bucket catalog (recommended)**

To upgrade an existing single-bucket catalog to a multiple-bucket catalog (recommended), run the [`gcloud biglake iceberg catalogs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/update) and set the `--catalog-type` parameter to `biglake`:
    
    
    gcloud biglake iceberg catalogs update CATALOG_ID \
        --project="PROJECT_ID" \
        --catalog-type="biglake"

**Note:** After upgrading to a multiple-bucket catalog, update your client query engine configurations (such as Spark or Trino) to specify the warehouse path using the `bl://` format: `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`.

###  REST 

**Option 1: Update catalog properties**

To modify a catalog's properties (such as its description) using the REST API, make a `PATCH` request to the [`UpdateIcebergCatalog`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs/patch) endpoint with the appropriate `updateMask`:
    
    
    PATCH /iceberg/v1/restcatalog/extensions/projects/PROJECT_ID/catalogs/CATALOG_ID?updateMask=icebergCatalog.description
    

The request body must contain an `IcebergCatalog` JSON payload with the fields to update:
    
    
    {
      "description": "Updated catalog description"
    }
    

**Option 2: Upgrade a single-bucket catalog to multiple-bucket catalog (recommended)**

To upgrade its type using the REST API, make a `PATCH` request to the [`UpdateIcebergCatalog`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs/patch) endpoint with the `catalogType` in the `updateMask`:
    
    
    PATCH /iceberg/v1/restcatalog/extensions/projects/PROJECT_ID/catalogs/CATALOG_ID?updateMask=icebergCatalog.catalogType
    

The request body must contain an `IcebergCatalog` JSON payload with the new catalog type:
    
    
    {
      "catalogType": "BIGLAKE"
    }
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your Lakehouse runtime catalog.



**Note:** After upgrading to a multiple-bucket catalog, update your client query engine configurations (such as Spark or Trino) to specify the warehouse path using the `bl://` format: `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-17 UTC."],[],[]] 
