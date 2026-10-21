---
url: https://docs.cloud.google.com/knowledge-catalog/docs/build-a-data-mesh-quickstart/
title: Build a data mesh \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:49.457820+00:00
---

# Build a data mesh  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/build-a-data-mesh-quickstart/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)



Send feedback 

#  Build a data mesh Stay organized with collections  Save and categorize content based on your preferences. 

You can use Knowledge Catalog (formerly Dataplex Universal Catalog) to build a data mesh architecture. This quickstart shows you how to use Knowledge Catalog features, such as a lake, zones, and assets, to build a data mesh.

A data mesh is an organizational and technical approach that decentralizes data ownership among domain data owners. These owners provide the data as a product in a standard way and facilitate communication among different parts of the organization to distribute datasets across different locations. Learn more about [data mesh architectures](https://docs.cloud.google.com/architecture/data-mesh).

## Objectives

In this guide, you use the Knowledge Catalog entities to build a data mesh architecture:

  * Create a Knowledge Catalog lake that acts as the domain for your data mesh.
  * Add zones to your lake that represents individual teams within each domain and provide managed data contracts.
  * Attach assets that map to data stored in Cloud Storage.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Knowledge Catalog](https://docs.cloud.google.com/dataplex/pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

  4. [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).

**Note:** You can attach each Dataproc Metastore to only one Knowledge Catalog lake. Enable `gRPC` for your metastore.



### Create a Cloud Storage bucket

You need a Cloud Storage bucket to store the data assets of your data mesh.

To create a Cloud Storage bucket, follow the instructions in [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). When doing so, note the following:

  * Name your bucket.
  * For **Location type** , choose **Region** , and select **us-central1 (Iowa)** from the menu.



## Create a domain

  1. In the Google Cloud console, go to the Knowledge Catalog **Lakes** page.

[Go to Lakes](https://console.cloud.google.com/dataplex/lakes)

  2. Click **Create** to create a new lake, which acts as your data mesh.

  3. In the **Display name** field, enter `My data mesh`.

**Note:** Knowledge Catalog automatically generates a lake ID.
  4. For **Region** , select `us-central1`.

**Note:** The region you select for your data mesh determines the location of the data (not including attached assets) managed by Knowledge Catalog. The same region is used when Knowledge Catalog creates resources in other services, but not for data contained within assets.
  5. Select the Dataproc Metastore service that you created and configured earlier as the associated metastore.

  6. Click **Create**.




## Create zones in your lake

After creating a domain by creating a Knowledge Catalog lake, you can host managed data contracts and individual teams within the domain by using zones. There are two types of zones:

  * Raw zones are typically used to store data in any format from external sources in Cloud Storage. Raw zones are useful for data that requires further processing before it's ready for consumption.

  * Curated zones are used for structured data in Cloud Storage that must conform to certain file formats, and are organized in a hive-compatible directory layout. They are most useful for data that's ready for consumption and analysis.




Each domain (for example, `sales`, `customers`, `products`) should have at least a raw zone and a curated zone.

Additional zones are used to manage data contracts between teams or to provide a more granular breakdown for teams within a given domain. For example, inventory management within the product domain. Data owners are able to manage the data within their domain and access it.

  1. In the Google Cloud console, navigate to the Knowledge Catalog **Manage** view.

  2. Click the name of the lake (`My data mesh`) you want to add a zone to.

  3. In the **Zones** tab, click add **Add Zone**.

  4. In the **Display name** field, enter `My sub domain`. Knowledge Catalog automatically generates an ID for your zone.

**Note:** The zone name becomes the name of a BigQuery dataset. Therefore, all zones hosted in the same Google Cloud project must have a unique ID, even if they exist within different lakes.
  5. For **Type** , select **Raw zone**.

  6. Click **Create**.




## Attach assets to your zones

Attach data assets to your zone. A data asset, the storage resources that contain your data, can be a Cloud Storage bucket or a BigQuery dataset. This is the final step in creating your data mesh architecture.

  1. In the Knowledge Catalog **Manage** view, click the lake you created (`My data mesh`).

  2. In the **Zones** tab, click the zone (`My sub domain`) to add the asset to.

  3. In the **Assets** tab, click add **Add assets**

  4. Click **Add an Asset**.

  5. For **Type** , select **Cloud Storage bucket**.

  6. In the **Display name** field , enter `Data mesh asset`. Knowledge Catalog automatically generates an asset ID for you.

  7. In the **Bucket** field, click **Browse**.

     1. Select your bucket from the list.
     2. Click **Select**.
  8. Click **Done** and then click **Continue**.

  9. Click **Continue** to accept the default **Advanced settings**.

  10. Click **Submit**.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete your data mesh architecture

  1. In the Google Cloud console, navigate to the Knowledge Catalog **Manage** view.

  2. For the lake that you want to delete, click more_vert **View more** , and then click **Delete**.

  3. To confirm the action, enter `delete` and click **Delete lake**.




## What's next

  * Learn about [data processing tasks](https://docs.cloud.google.com/knowledge-catalog/docs/task-templates)
  * Learn about [discovering data](https://docs.cloud.google.com/knowledge-catalog/docs/discover-data)
  * Learn about [using data quality tasks](https://docs.cloud.google.com/knowledge-catalog/docs/using-data-quality-task-templates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
