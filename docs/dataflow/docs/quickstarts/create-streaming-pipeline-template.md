---
url: https://docs.cloud.google.com/dataflow/docs/quickstarts/create-streaming-pipeline-template/
title: Quickstart: Create a streaming pipeline using a Dataflow template \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:36.602930+00:00
---

# Quickstart: Create a streaming pipeline using a Dataflow template  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/quickstarts/create-streaming-pipeline-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a streaming pipeline using a Dataflow template

This quickstart shows you how to create a streaming pipeline using a Google-provided Dataflow template. Specifically, this quickstart uses the **Pub/Sub to BigQuery** template as an example.

The Pub/Sub to BigQuery template is a streaming pipeline that can read JSON-formatted messages from a Pub/Sub topic and write them to a BigQuery table.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/home/dashboard?tutorial=dataflow--quickstart-templates)

* * *

## Before you begin

Complete the following steps before running your pipeline.

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataflow, Compute Engine, Cloud Logging, Cloud Storage, Google Cloud Storage JSON, BigQuery, Pub/Sub, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow,compute_component,logging,storage_component,storage_api,bigquery,pubsub,cloudresourcemanager.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataflow, Compute Engine, Cloud Logging, Cloud Storage, Google Cloud Storage JSON, BigQuery, Pub/Sub, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow,compute_component,logging,storage_component,storage_api,bigquery,pubsub,cloudresourcemanager.googleapis.com)




### Required roles

To complete this quickstart, you need the following Identity and Access Management (IAM) roles.

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [BigQuery User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`)
  * [Dataflow Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To ensure that the Compute Engine default service account has the necessary permissions to run the Dataflow job, ask your administrator to grant the following IAM roles to the Compute Engine default service account on your project: 

**Important:** You must grant these roles to the Compute Engine default service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
  * [Dataflow Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker) (`roles/dataflow.worker`)
  * [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)
  * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)
  * [Viewer ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Compute Engine default service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create a Cloud Storage bucket

Before you can run a pipeline, you must create a Cloud Storage bucket.

  1. Create a Cloud Storage bucket:

     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click add_box **Create**. 
     3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
        1. For **Name your bucket** , enter a unique bucket name. Don't include sensitive information in the bucket name, because the bucket namespace is global and publicly visible. 
        2. In the **Choose where to store your data** section, do the following: 
           1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
           2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
              * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
           3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

              1. In the **Bucket** menu, select a bucket.
              2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

                 * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
                 * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
                 * Click **Done**.

        3. In the **Choose how to store your data** section, do the following: 
           1. In the **Set a default class** section, select the following: **Standard**. 
           2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
        4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
        5. In the **Choose how to protect object data** section, do the following: 
           * Select any of the options under **Data protection** that you want to set for your bucket. 
             * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
             * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
             * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
               * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
               * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
           * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
     4. Click **Create**. 
  2. Copy the following, as you need them in a later section:

     * Your Cloud Storage bucket name.
     * Your Google Cloud project ID.

To find this ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




### VPC network

By default, each new project starts with a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network). If the default network for your project is [disabled](https://docs.cloud.google.com/vpc/docs/vpc#org-policies) or was deleted, you need to have a network in your project for which your user account has the [Compute Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`).

## Create a BigQuery dataset and table

Create a BigQuery dataset and table with the appropriate schema for your Pub/Sub topic using the Google Cloud console.

In this example, the name of the dataset is `taxirides` and the name of the table is `realtime`. To create this dataset and table, follow these steps:

  1. Go to the **BigQuery** page.   
[Go to BigQuery](https://console.cloud.google.com/bigquery)
  2. In the **Explorer** panel, next to the project where you want to create the dataset, click more_vert **View actions** , and then click **Create dataset**. **Note:** The default experience is the [Preview](https://cloud.google.com/products#product-launch-stages) Google Cloud console. If you clicked **Hide preview features** to go to the Google Cloud console, then perform the following step instead: In the navigation panel, in the **Resources** section, select your project. 
  3. On the **Create dataset** panel, follow these steps:
     1. For **Dataset ID** , enter `taxirides`. Dataset IDs are unique for each Google Cloud project.
     2. For **Location type** , choose **Multi-region** , and then select **US (multiple regions in United States)**. Public datasets are stored in the `US` multi-region [location](https://docs.cloud.google.com/bigquery/docs/dataset-locations). For simplicity, place your dataset in the same location. 
     3. Leave the other default settings, and then click **Create dataset**
  4. In the **Explorer** panel, expand your project.
  5. Next to your `taxirides` dataset, click more_vert **View actions** , and then click **Create table**. **Note:** The default experience is the [Preview](https://cloud.google.com/products#product-launch-stages) Google Cloud console. If you clicked **Hide preview features** to go to the Google Cloud console, then perform the following step instead: In the navigation panel, in the **Resources** section, select the `taxirides` dataset you created. 
  6. On the **Create table** panel, follow these steps:
     1. In the **Source** section, for **Create table from** , select **Empty table**.
     2. In the **Destination** section, for **Table** , enter `realtime`.
     3. In the **Schema** section, click the **Edit as text** toggle and paste the following schema definition into the box:   

            
            ride_id:string,point_idx:integer,latitude:float,longitude:float,timestamp:timestamp,
            meter_reading:float,meter_increment:float,ride_status:string,passenger_count:integer

     4. In the **Partition and cluster settings** section, for **Partitioning** , select the **timestamp** field.
  7. Leave the other default settings in place and click **Create table**.



## Run the pipeline

Run a streaming pipeline using the Google-provided [Pub/Sub to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery) template. The pipeline gets incoming data from the input topic. 

  1. Go to the Dataflow **Jobs** page.  
[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)
  2. Click **Create job from template**.
  3. Enter `taxi-data` as the **Job name** for your Dataflow job.
  4. For **Dataflow template** , select the **Pub/Sub to BigQuery** template.
  5. For **BigQuery output table** , enter the following: 
         
         PROJECT_ID:taxirides.realtime

Replace `PROJECT_ID` with the project ID of the project where you created your BigQuery dataset.

  6. In the section **Optional source parameters** , in the **Input Pub/Sub topic** field, click **Enter topic manually**.
  7. In the dialog, for **Topic name** enter the following, and then click **Save** : 
         
         projects/pubsub-public-data/topics/taxirides-realtime

This publicly available Pub/Sub topic is based on the [NYC Taxi & Limousine Commission's open dataset](https://data.cityofnewyork.us/). The following is a sample message from this topic, in the JSON format:
         
         {
           "ride_id": "19c41fc4-e362-4be5-9d06-435a7dc9ba8e",
           "point_idx": 217,
           "latitude": 40.75399,
           "longitude": -73.96302,
           "timestamp": "2021-03-08T02:29:09.66644-05:00",
           "meter_reading": 6.293821,
           "meter_increment": 0.029003782,
           "ride_status": "enroute",
           "passenger_count": 1
         }

  8. For **Temp location** , enter the following: 
         
         gs://BUCKET_NAME/temp/

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket. The `temp` folder stores temporary files, like the staged pipeline job.

  9. If your project does not have a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network), enter a **Network** and a **Subnetwork**. For more information, see [Specify a network and subnetwork](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks#specifying_a_network_and_a_subnetwork). **Note:** Unless specified through the `network` option, the Dataflow runner runs jobs in the `default` Virtual Private Cloud network. If your project does not have a default network and you don't specify a network, an error occurs. You might not have a default network if the default network was deleted or if [an organization policy constraint](https://docs.cloud.google.com/vpc/docs/vpc#org-policies) prevents the creation of the default network. 
  10. Click **Run job**.



## View your results

To view the data written to your `realtime` table, follow these steps: 

  1. Go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Click add_box **Compose a new query**. A new **Editor** tab opens.
         
         SELECT * FROM `PROJECT_ID.taxirides.realtime`
         WHERE `timestamp` > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY)
         LIMIT 1000

Replace `PROJECT_ID` with the project ID of the project where you created your BigQuery dataset. It can take up to five minutes for data to start appearing in your table.

  3. Click **Run**.

The query returns rows that have been added to your table in the past 24 hours. You can also run queries using standard SQL.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the project

The easiest way to eliminate billing is to delete the Google Cloud project that you created for the quickstart. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

If you want to keep the Google Cloud project that you used in this quickstart, then delete the individual resources:

  1. Go to the Dataflow **Jobs** page.  
[ Go to Jobs](https://console.cloud.google.com/dataflow/jobs)
  2. Select your streaming job from the job list.
  3. In the navigation, click **Stop**.
  4. In the **Stop job** dialog, either [cancel](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel) or [drain](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain) your pipeline, and then click **Stop job**.
  5. Go to the **BigQuery** page.  
[Go to BigQuery](https://console.cloud.google.com/bigquery)
  6. In the **Explorer** panel, expand your project.
  7. Next to the dataset you want to delete, click more_vert**View actions** , and then click **Open**. 
  8. In the details panel, click **Delete dataset** , and then follow the instructions.
  9. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  10. Click the checkbox for the bucket that you want to delete. 
  11. To delete the bucket, click delete **Delete** , and then follow the instructions. 



## What's next

  * [Dataflow templates overview](https://docs.cloud.google.com/dataflow/docs/templates/overview)
  * [Creating classic templates](https://docs.cloud.google.com/dataflow/docs/templates/creating-templates)
  * [Running classic templates](https://docs.cloud.google.com/dataflow/docs/templates/running-templates)
  * [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
