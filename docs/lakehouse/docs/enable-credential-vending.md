---
url: https://docs.cloud.google.com/lakehouse/docs/enable-credential-vending/
title: Enable credential vending \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:06.792902+00:00
---

# Enable credential vending  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/enable-credential-vending/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Enable credential vending Stay organized with collections  Save and categorize content based on your preferences. 

The Lakehouse runtime catalog lets you enable credential vending mode for [catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs#configuration) in borderless Lakehouse.

Credential vending mode vends short-lived, downscoped storage tokens to authorized query engines and workloads. This authentication method eliminates the need for you or query runtimes to hold direct read and write permissions on the underlying Cloud Storage bucket.

**Note:** You can enable credential vending mode only for Apache Iceberg REST catalog endpoints; it isn't supported for Apache Hive catalog endpoints.

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

To get the permissions that you need to enable credential vending, ask your administrator to grant you the following IAM roles: 

  * All: 
    * [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on your project
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on your project
  * Auto-provisioned Apache Iceberg REST catalog service account: [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on all associated Cloud Storage buckets. After enabling credential vending, explicitly grant the Storage Object User role (`roles/storage.objectUser`) on all associated storage buckets to your catalog's auto-provisioned Apache Iceberg REST catalog service account. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** Creation of the auto-provisioned catalog service account is [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency). This means that it takes time for the service account to propagate through the system. If you try to grant roles to the service account immediately after creation, the request might fail. To learn how long it takes, on average, for access changes to propagate, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Enable credential vending

If the authentication method for your Apache Iceberg REST catalog is set to end-user credentials, you can switch it to [credential vending mode](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#credential-vending-mode).

###  Console 

  1. In the Google Cloud console, open the **Lakehouse** page.



[Go to Lakehouse](https://console.cloud.google.com/biglake)

  1. In the row of the catalog that you're updating, select more_vert **More catalog actions > Edit authentication**.

  2. In the authentication dialog, select **Credential vending mode**. The auto-provisioned Apache Iceberg REST catalog service account requires the explicit **Storage Object User** role (`roles/storage.objectUser`) on all associated Cloud Storage buckets. By default, it has no access. Without this role, vended credentials don't have sufficient scope to perform storage writes.

  3. Select **Save**.
         
         Your catalog is updated and the **Catalog details** page opens.
         

  4. Under **Authentication method** , select **Set bucket permissions**.

  5. In the dialog, select **Confirm**.




This verifies that your catalog's service account has the Storage Object User role (`roles/storage.objectUser`) on all associated storage buckets.

###  gcloud 

Use the [`gcloud biglake iceberg catalogs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/create).
    
    
    gcloud biglake iceberg catalogs update \
        CATALOG_NAME \
        --project PROJECT_ID \
        --credential-mode vended-credentials

Replace the following:

  * `CATALOG_NAME`: a name for your catalog. For Lakehouse catalogs, this is your custom catalog name. For Cloud Storage bucket catalogs, this matches the Cloud Storage bucket ID used with the REST catalog. This name is also used as the catalog identifier when [querying these tables from BigQuery](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/create).
  * `PROJECT_ID`: your Google Cloud project ID.

After enabling credential vending, explicitly grant the **Storage Object User** role (`roles/storage.objectUser`) on all associated storage buckets to your catalog's auto-provisioned Apache Iceberg REST catalog service account.




###  REST 

To enable credential vending mode using the REST API, make a `PATCH` request to the [`UpdateIcebergCatalog`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs/patch) endpoint:
    
    
    PATCH /iceberg/v1/restcatalog/extensions/projects/PROJECT_ID/catalogs/CATALOG_ID?updateMask=icebergCatalog.credential_mode
    

The request body must contain an `IcebergCatalog` JSON payload with `credential_mode` set to `VENDED_CREDENTIALS`.

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your Lakehouse runtime catalog.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
