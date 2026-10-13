---
url: https://docs.cloud.google.com/lakehouse/docs/create-namespace/
title: Create a namespace \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:44.621570+00:00
---

# Create a namespace  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/create-namespace/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Create a namespace Stay organized with collections  Save and categorize content based on your preferences. 

The Lakehouse runtime catalog lets you create namespaces in borderless Lakehouse [catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs#configuration) to group and organize related tables.

When you create a namespace, you can optionally associate it with a custom Cloud Storage bucket or path, or inherit the catalog's default storage location.

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

To get the permissions that you need to create a namespace, ask your administrator to grant you the following IAM roles on your project: 

  * All: 
    * [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a namespace

Create a namespace within a catalog.

**Considerations**

When you create a namespace, you can optionally specify a Cloud Storage bucket or path to associate with the namespace:

  * **Multiple-bucket catalog** (recommended): You can set any custom location as long as it is under a location allowed by the catalog (`default_location` or `restricted_locations`). If you do not specify a location, the namespace is created under the catalog's default location (for example, `gs://{default_location}/{namespace_name}`).
  * **Single-bucket catalog** : The namespace location is automatically inherited from the catalog's single bucket.




###  Console 

  1. In the Google Cloud console, open the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you don't have one.

  3. In the menu bar, click **\+ Create namespace**.

  4. For **Namespace name** , enter a unique name for your namespace.

  5. For **Location** , optionally specify a Cloud Storage bucket or path to associate with your namespace. The location matches the warehouse bucket.

  6. Click **Create**.

Your namespace is created and appears in your catalog details list.




###  gcloud 

**Create a namespace in a multiple-bucket catalog (recommended)**

To create a namespace in a multiple-bucket catalog (where you can optionally specify a custom location), run the [`gcloud biglake iceberg namespaces create` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/namespaces/create) with the `--properties` flag:
    
    
    gcloud biglake iceberg namespaces create NAMESPACE_NAME \
        --project="PROJECT_ID" \
        --catalog="CATALOG_ID" \
        [--properties="location=LOCATION"]

Replace the following:

  * `NAMESPACE_NAME`: a name for your namespace.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `LOCATION`: (Optional) a custom Cloud Storage bucket or path to associate with the namespace (for example, `gs://my-bucket/my-path`).



**Create a namespace in a single-bucket catalog**

To create a namespace in a single-bucket catalog, omit the `--properties` flag. The namespace location is automatically inherited from the catalog's single bucket.
    
    
    gcloud biglake iceberg namespaces create NAMESPACE_NAME \
        --project="PROJECT_ID" \
        --catalog="CATALOG_ID"

###  REST 

To create a namespace using the REST API, make a `POST` request to the [`CreateIcebergNamespace`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces/create) endpoint:
    
    
    POST /iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/namespaces
    

The request body must contain a valid Iceberg `CreateNamespaceRequest` JSON payload defining the namespace identifier and properties:
    
    
    {
      "namespace": [
        "NAMESPACE_NAME"
      ],
      "properties": {
        "location": "LOCATION"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: a name for your namespace.
  * `LOCATION`: (Optional) a custom Cloud Storage bucket or path to associate with the namespace (for example, `gs://my-bucket/my-path`).



## What's next

  * Learn how to [manage namespace ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl#apply-acl-namespaces).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
