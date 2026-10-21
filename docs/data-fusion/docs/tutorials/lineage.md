---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/lineage/
title: Explore data lineage using metadata \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:31.578131+00:00
---

# Explore data lineage using metadata  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/lineage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Explore data lineage using metadata Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to use Cloud Data Fusion to explore data _lineage_ : the origins of data and its movement over time. 

## Cloud Data Fusion data lineage

You can use Cloud Data Fusion data lineage to do the following:

  * Detect the root cause of bad data events.

  * Perform an impact analysis before making data changes.




We recommend using asset lineage integration in Knowledge Catalog. For more information see, [View lineage in Knowledge Catalog](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex).

You can also view lineage at the _dataset_ and _field_ levels in the Cloud Data Fusion Studio using the **Metadata** option, which shows lineage for a selected time range.

  * Dataset level lineage shows the relationship between datasets and pipelines.

  * Field level lineage shows the operations that were performed on a set of fields in the source dataset to produce a different set of fields in the target dataset.




From Cloud Data Fusion 6.9.2.4 onwards, if you don't track lineage in Cloud Data Fusion, we recommend turning off field level lineage emission in your instance using the [`patch`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/patch) method:
    
    
    curl -X PATCH -H 'Content-Type: application/json' -H "Authorization: Bearer
    $(gcloud auth print-access-token)"
    'https://datafusion.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/instances/INSTANCE_ID?updateMask=options'
    -d '{ "options": { "metadata.messaging.field.lineage.emission.enabled": "false" } }'
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `REGION`: the location of the Google Cloud project
  * `INSTANCE_ID`: the Cloud Data Fusion instance ID



## Tutorial Scenario

In this tutorial, you work with two pipelines:

  * The `Shipment Data Cleansing` pipeline reads raw shipment data from a small sample dataset and applies transformations to clean the data.

  * The `Delayed Shipments USA` pipeline then reads the cleansed shipment data, analyzes it, and finds shipments within the USA that were delayed by more than a threshold.




These tutorial pipelines demonstrate a typical scenario in which raw data is cleaned then sent for downstream processing. This data trail from raw data to the cleaned shipment data to analytic output can be explored using the Cloud Data Fusion lineage feature.

## Objectives

  * Produce lineage by running sample pipelines
  * Explore dataset and field level lineage
  * Learn how to pass handshaking information from the upstream pipeline to the downstream pipeline



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Data Fusion
  * Cloud Storage
  * BigQuery



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Data Fusion, Cloud Storage, Dataproc, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,storage-component.googleapis.com,bigquery.googleapis.com,dataproc.googleapis.com&redirect=https%3A//console.cloud.google.com)

  7. [ Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance#creating_an_instance).
  8. Click the following links to download these small sample datasets to your local machine: 
     * [Shipment Data Cleansing](https://docs.cloud.google.com/static/data-fusion/docs/tutorials/sample_datasets/shipment-data-cleansing-cdap-data-pipeline.json)
     * [Delayed Shipments USA](https://docs.cloud.google.com/static/data-fusion/docs/tutorials/sample_datasets/delayed-shipments-us-cdap-data-pipeline.json)



## Open the Cloud Data Fusion UI

When using Cloud Data Fusion, you use both the Google Cloud console and the separate Cloud Data Fusion UI. In the Google Cloud console, you can create a Google Cloud console project, and create and delete Cloud Data Fusion instances. In the Cloud Data Fusion UI, you can use the various pages, such as **Lineage** , to access Cloud Data Fusion features.

  1. In the Google Cloud console, open the **Instances** page. 

[Open the Instances page](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the **Actions** column for the instance, click the View Instance link. The Cloud Data Fusion UI opens in a new browser tab.

  3. In the **Integrate** pane, click **Studio** to open the Cloud Data Fusion **Studio** page. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/integrate-panel.png)




## Deploy and run pipelines

  1. Import the raw Shipping Data. On the **Studio** page, click **Import** or click **+ > Pipeline > Import**, and then select and import the Shipment Data Cleansing pipeline that you downloaded in Before you begin.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/import-shipping.png)If a dialog asks you to upgrade pipeline plugins, then click **Fix All** to upgrade the plugins to the latest versions. 
  2. Deploy the pipeline. Click Deploy in the top-right of the **Studio** page. After deployment, the **Pipeline** page opens.

  3. Run the pipeline. Click Run in the top-center of the **Pipeline** page.

  4. Import, deploy, and run the Delayed Shipments data and pipeline. After the status of the Shipping Data Cleansing shows **Succeeded** , apply the preceding steps to the Delayed Shipments USA data that you downloaded in Before You Begin. Return to the **Studio** page to import the data, then deploy and run this second pipeline from the **Pipeline** page. After the second pipeline completes successfully, proceed with the remaining steps.




## Discover datasets

You must discover a dataset before exploring its lineage. Select **Metadata** from the Cloud Data Fusion UI left navigation panel to open the metadata **Search** page. Since the Shipment Data Cleansing dataset specified **Cleaned-Shipments** as the reference dataset, insert **shipment** in the Search box. The search results include this dataset.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/metadata-search.png)

### Using tags to discover datasets

A Metadata search discovers datasets that have been consumed, processed, or generated by Cloud Data Fusion pipelines. Pipelines execute on a structured framework that generates and collects technical and operational metadata. The technical metadata includes dataset name, type, schema, fields, creation time, and processing information. This technical information is used by the Cloud Data Fusion metadata search and lineage features.

Although the `Reference Name` of sources and sinks is a unique dataset identifier and an excellent search term, you can use other technical metadata as search criteria, such as a dataset description, schema, field name, or metadata prefix.

Cloud Data Fusion also supports the annotation of datasets with business metadata, such as tags and key-value properties, which can be used as search criteria. For example, to add and search for a business tag annotation on the Raw Shipping Data dataset:

  1. Click the **Properties** button of the Raw Shipping Data node on the Shipment Data Cleansing **Pipeline** page to open the **Cloud Storage Properties** page.

  2. Click **View Metadata** to open the **Search** page.

  3. Under **Business Tags** , click + then insert a tag name (alphanumeric and underscore characters are allowed) and press Enter. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/add-tag.png)You can perform a search on a tag by clicking the tag name or by entering `tags:tag_name` in the search box on the **Metadata** search page.




## Explore lineage

### Dataset level lineage

Click the Cleaned-Shipments dataset name listed on the Search page (from Discover datasets), then click the Lineage tab. The lineage graph shows that this dataset was generated by the Shipments-Data-Cleansing pipeline, which had consumed the Raw_Shipping_Data dataset.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/lineage.png)

The left and right arrows let you navigate back and forward through any previous or subsequent dataset lineage. In this example, the graph displays the full lineage for the Cleaned-Shipments dataset.

### Field level lineage

Cloud Data Fusion field level lineage shows the relationship between the fields of a dataset and the transformations that were performed on a set of fields to produce a different set of fields. Like dataset level lineage, field level lineage is time-bound, and its results change with time.

Continuing from the Dataset level lineage step, click the Field Level Lineage button in the top right of the Cleaned Shipments dataset-level lineage graph to display its field level lineage graph.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/field-lineage.png)

The field level lineage graph shows connections between fields. You can select a field to view its lineage. Select **View > Pin field** to view lineage of that field only.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/pin-field.png)

Select **View > View impact** to perform an impact analysis.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/impact-field.png)

The cause and impact links show the transformations performed on both sides of a field in a human-readable ledger format. This information can be essential for reporting and governance.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you've finished the tutorial, clean up the resources you created on Google Cloud so they won't take up quota and you won't be billed for them in the future. The following sections describe how to delete or turn off these resources.

### Delete the tutorial dataset

This tutorial creates a `logistics_demo` dataset with several tables in your project.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/lineage/logistics-demo-dataset.png)

You can delete the dataset from the [BigQuery Web UI](https://console.cloud.google.com/bigquery) in the Google Cloud console.

### Delete the Cloud Data Fusion instance

Follow the [instructions to delete your Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Read the [how-to guides](https://docs.cloud.google.com/data-fusion/docs/how-to)
  * Work through another [tutorial](https://docs.cloud.google.com/data-fusion/docs/tutorials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
