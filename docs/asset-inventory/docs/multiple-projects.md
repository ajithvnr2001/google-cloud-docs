---
url: https://docs.cloud.google.com/asset-inventory/docs/multiple-projects/
title: Work across multiple projects \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:35.259561+00:00
---

# Work across multiple projects  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/multiple-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  Work across multiple projects Stay organized with collections  Save and categorize content based on your preferences. 

Depending on your needs, you might need to design your architecture to work across multiple projects when using Cloud Asset Inventory. The following scenarios are the most common:

  * **Orchestrator projects**: When you want a single project to trigger Cloud Asset Inventory operations in other projects.

  * **Export across projects**: When you want to export resource metadata from one project to another.




Each of these scenarios requires some setup to ensure that operations complete successfully.

## Orchestrator projects

When you use a project to trigger Cloud Asset Inventory operations on resources in another project, in certain scenarios you need to specify that the default Cloud Asset Inventory service account in the other project be used to perform the operation. These scenarios include:

  * [Exporting asset metadata to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery)

  * [Exporting asset metadata to Cloud Storage buckets](https://docs.cloud.google.com/asset-inventory/docs/export-cloud-storage)

  * [Monitoring asset changes with Pub/Sub](https://docs.cloud.google.com/asset-inventory/docs/monitor-asset-changes)




To set which service account to use, you set the _billing project_ to the ID of the project that contains the resources you're operating on. If the billing project isn't specified, Cloud Asset Inventory uses the default Cloud Asset Inventory service account in the project that's making the call, which might not have the permissions required to complete the operation.

Although it isn't required for all operations, it can be good practice to always specify a billing project to minimize confusion.

###  gcloud 

For the gcloud CLI, add the `--billing-project` flag to your command to specify the project ID that contains the correct service account:
    
    
    --billing-project=BILLING_PROJECT_ID
    

Alternatively, you can set the billing project before you run commands with the gcloud CLI. First, check if the billing project is different from the core project:
    
    
    gcloud config list
    

Then if you need to, set the billing project:
    
    
    gcloud config set billing/quota_project BILLING_PROJECT_ID
    

Provide the following values:

  * `BILLING_PROJECT_ID`: A project ID that has the Cloud Asset Inventory API enabled, and a service account with permissions to manage your target Pub/Sub topic, Cloud Storage bucket, or BigQuery table.



### REST

For the REST API, add the `X-Goog-User-Project` header to specify the project ID that contains the correct service account:
    
    
    "X-Goog-User-Project: BILLING_PROJECT_ID"
    

Provide the following values:

  * `BILLING_PROJECT_ID`: A project ID that has the Cloud Asset Inventory API enabled, and a service account with permissions to manage your target Pub/Sub topic, Cloud Storage bucket, or BigQuery table.



## Export across projects

To export asset metadata from one project, `PROJECT_A`, to another, `PROJECT_B`, you must give the default Cloud Asset Inventory service account in `PROJECT_A` access to the resources in `PROJECT_B`.

This enables two things:

  * You can export asset metadata from `PROJECT_A` into a Pub/Sub topic, Cloud Storage bucket, or BigQuery table located in `PROJECT_B`.

  * You can use `PROJECT_A` to export asset metadata from `PROJECT_B` into a Pub/Sub topic, Cloud Storage bucket, or BigQuery table located in `PROJECT_B`.




To export asset metadata from one project into another, complete the following instructions:

  1. Make sure that the [Cloud Asset Inventory API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) is enabled in the project you want to run your request from, `PROJECT_A`.

  2. Make at least one call to the Cloud Asset Inventory API in `PROJECT_A` to create the default Cloud Asset Inventory service account. Alternatively, you can create it manually:
         
         gcloud beta services identity create \
             --service=cloudasset.googleapis.com \
             --project=PROJECT_A_ID
         gcloud projects add-iam-policy-binding PROJECT_A_ID \
             --member=serviceAccount:service-PROJECT_A_NUMBER@gcp-sa-cloudasset.iam.gserviceaccount.com \
             --role=roles/cloudasset.serviceAgent
         

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

     1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

     2. Click the **switcher** list box in the menu bar.
     3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

  3. Grant the correct roles to the service account in `PROJECT_A`. 

     * To publish to a feed through Pub/Sub, grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) role to the service account on the topic:
           
           gcloud pubsub topics add-iam-policy-binding projects/PROJECT_B_ID/topics/TOPIC_ID \
               --member=serviceAccount:service-PROJECT_A_NUMBER@gcp-sa-cloudasset.iam.gserviceaccount.com \
               --role=roles/pubsub.publisher
           

     * To write to a Cloud Storage bucket, grant the [Storage admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) role to the service account on the bucket:
           
           gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:service-PROJECT_A_NUMBER@gcp-sa-cloudasset.iam.gserviceaccount.com \
             --role=roles/storage.admin
           

     * To write to a BigQuery table, grant the [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) and [BigQuery user](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`) roles to the service account on the project:
           
           gcloud projects add-iam-policy-binding PROJECT_B_ID \
               --member=serviceAccount:service-PROJECT_A_NUMBER@gcp-sa-cloudasset.iam.gserviceaccount.com \
               --role=roles/bigquery.dataEditor
           gcloud projects add-iam-policy-binding PROJECT_B_ID \
               --member=serviceAccount:service-PROJECT_A_NUMBER@gcp-sa-cloudasset.iam.gserviceaccount.com \
               --role=roles/bigquery.user
           




If you make a Cloud Asset Inventory request with the gcloud CLI from `PROJECT_B` or use the REST API, make sure to specify `PROJECT_A` as the billing project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
