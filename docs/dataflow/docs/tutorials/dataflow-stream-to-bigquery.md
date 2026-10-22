---
url: https://docs.cloud.google.com/dataflow/docs/tutorials/dataflow-stream-to-bigquery/
title: Stream from Pub/Sub to BigQuery \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:49.070692+00:00
---

# Stream from Pub/Sub to BigQuery  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tutorials/dataflow-stream-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Stream from Pub/Sub to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial uses the [Pub/Sub Subscription to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-subscription-to-bigquery) template to create and run a [Dataflow template](https://docs.cloud.google.com/dataflow/docs/guides/templates/overview) job using the Google Cloud console or Google Cloud CLI. The tutorial walks you through a streaming pipeline example that reads JSON-encoded messages from [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) and writes them to a [BigQuery](https://docs.cloud.google.com/bigquery/docs) table.

Streaming analytics and data integration pipelines use Pub/Sub to ingest and distribute data. Pub/Sub enables you to create systems of event producers and consumers, called **publishers** and **subscribers**. Publishers send events to the Pub/Sub service asynchronously, and Pub/Sub delivers the events to all services that need to react to them.

Dataflow is a fully-managed service for transforming and enriching data in stream (real-time) and batch modes. It provides a simplified pipeline development environment that uses the Apache Beam SDK to transform incoming data and then output the transformed data.

The benefit of this workflow is that you can use UDFs to transform the message data before it is written to BigQuery.

Before running a Dataflow pipeline for this scenario, consider whether a [Pub/Sub BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery) with a [UDF](https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview) meets your requirements.

## Objectives

  * Create a Pub/Sub topic.
  * Create a BigQuery dataset with a table and schema.
  * Use a Google-provided streaming template to stream data from your Pub/Sub subscription to BigQuery by using Dataflow.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Dataflow
  * Pub/Sub
  * Cloud Storage
  * BigQuery



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

This section shows you how to select a project, enable APIs, and grant the appropriate roles to your user account and to the [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account).

### Console

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, Dataflow, Cloud Logging, BigQuery, Pub/Sub, Cloud Storage, Resource Manager APIs, if any are not already enabled. 

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

  7. Enable the Compute Engine, Dataflow, Cloud Logging, BigQuery, Pub/Sub, Cloud Storage, Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow,compute_component,logging,storage_component,storage_api,bigquery,pubsub,cloudresourcemanager.googleapis.com)

  8. To complete the steps in this tutorial, your user account must have the [Service Account User](https://docs.cloud.google.com/iam/docs/service-accounts-actas) role. The [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) must have the following roles: [Dataflow Worker](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#roles), [Dataflow Admin](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#roles), Pub/Sub Editor, Storage Object Admin, and BigQuery Data Editor. To add the required roles in the Google Cloud console:

     1. In the Google Cloud console, go to the **IAM** page.

[ Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)
     2. Select your project.
     3. In the row containing your user account, click edit **Edit principal** , and then click add **Add another role**. 
     4. In the drop-down list, select the role **Service Account User**.
     5. In the row containing the Compute Engine default service account, click edit **Edit principal** , and then click add **Add another role**. 
     6. In the drop-down list, select the role **Dataflow Worker**.
     7. Repeat for the **Dataflow Admin** , the **Pub/Sub Editor** , the **Storage Object Admin** , and the **BigQuery Data Editor** roles, and then click **Save**.

For more information about granting roles, see [Grant an IAM role by using the console](https://docs.cloud.google.com/iam/docs/grant-role-console).




###  gcloud 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine, Dataflow, Cloud Logging, BigQuery, Pub/Sub, Cloud Storage, Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com dataflow.googleapis.com logging.googleapis.com bigquery.googleapis.com pubsub.googleapis.com storage.googleapis.com cloudresourcemanager.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Compute Engine, Dataflow, Cloud Logging, BigQuery, Pub/Sub, Cloud Storage, Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com dataflow.googleapis.com logging.googleapis.com bigquery.googleapis.com pubsub.googleapis.com storage.googleapis.com cloudresourcemanager.googleapis.com

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. Grant roles to your Compute Engine default service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/storage.admin`
     * `roles/pubsub.editor`
     * `roles/bigquery.dataEditor`
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `PROJECT_NUMBER`: your project number. To find your project number, use the [`gcloud projects describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe).
     * `SERVICE_ACCOUNT_ROLE`: each individual role.



## Create a Cloud Storage bucket

Begin by creating a Cloud Storage bucket using the Google Cloud console or Google Cloud CLI. The Dataflow pipeline uses this bucket as a temporary storage location.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click **Create**.

  3. On the **Create a bucket** page, for **Name your bucket** , enter a name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). Cloud Storage bucket names must be globally unique. Don't select the other options.

  4. Click **Create**.




###  gcloud 

Use the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create):
    
    
    gcloud storage buckets create gs://BUCKET_NAME
    

Replace `BUCKET_NAME` with a name for your Cloud Storage bucket that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). Cloud Storage bucket names must be globally unique.

## Create a Pub/Sub topic and subscription

Create a Pub/Sub topic and then create a subscription to that topic.

### Console

To create a topic, complete the following steps.

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click **Create topic**.

  3. In the **Topic ID** field, enter an ID for your topic. For information about how to name a topic, see [Guidelines to name a topic or a subscription](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  4. Retain the option **Add a default subscription**. Don't select the other options.

  5. Click **Create**.

  6. In the topic details page, the name of the subscription that was created is listed under **Subscription ID**. Note this value for later steps. 



### gcloud

To create a topic, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command. For information about how to name a subscription, see [Guidelines to name a topic or a subscription](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).
    
    
    gcloud pubsub topics create TOPIC_ID

Replace `TOPIC_ID` with a name for your Pub/Sub topic.

To create a subscription to your topic, run the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command:
    
    
    gcloud pubsub subscriptions create --topic TOPIC_ID SUBSCRIPTION_ID

Replace `SUBSCRIPTION_ID` with a name for your Pub/Sub subscription.

## Create a BigQuery table

In this step, you create a BigQuery table with the following schema:

Column name | Data type  
---|---  
`name` | `STRING`  
`customer_id` | `INTEGER`  
  
If you don't already have a BigQuery dataset, first create one. For more information, see [Create datasets](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset). Then create a new empty table:

###  Console 

  1. Go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, expand your project, and then select a dataset.

  3. In the **Dataset** info section, click add_box **Create table**.

  4. In the **Create table from** list, select **Empty table**.

  5. In the **Table** box, enter the name of the table.

  6. In the **Schema** section, click **Edit as text**.

  7. Paste in the following schema definition:
         
         name:STRING,
         customer_id:INTEGER
         

  8. Click **Create table**.




###  gcloud 

Use the [`bq mk`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_mk) command.
    
    
    bq mk --table \
      PROJECT_ID:DATASET_NAME.TABLE_NAME \
      name:STRING,customer_id:INTEGER
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `DATASET_NAME`: the name of the dataset
  * `TABLE_NAME`: the name of the table to create



## Run the pipeline

Run a streaming pipeline using the Google-provided Pub/Sub Subscription to BigQuery template. The pipeline gets incoming data from the Pub/Sub topic and outputs the data to your BigQuery dataset.

### Console

  1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click **Create job from template**.

  3. Enter a **Job name** for your Dataflow job.

  4. For **Regional endpoint** , select a region for your Dataflow job.

  5. For **Dataflow template** , select the **Pub/Sub Subscription to BigQuery** template.

  6. For **BigQuery output table** , select **Browse** and select your BigQuery table.

  7. In the **Pub/Sub input subscription** list, select the Pub/Sub subscription.

  8. For **Temporary location** , enter the following:
         
         gs://BUCKET_NAME/temp/
         

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket. The `temp` folder stores temporary files for the Dataflow jobs.

  9. Click **Run job**.




###  gcloud 

**Note:** To use the Google Cloud CLI to run classic templates, you must have [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later.

To run the template in your shell or terminal, use the [`gcloud dataflow jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run) command.
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/latest/PubSub_Subscription_to_BigQuery \
        --region DATAFLOW_REGION \
        --staging-location gs://BUCKET_NAME/temp \
        --parameters \
    inputSubscription=projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID,\
    outputTableSpec=PROJECT_ID:DATASET_NAME.TABLE_NAME
    

Replace the following variables:

  * `JOB_NAME`. a name for the job
  * `DATAFLOW_REGION`: a [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) for the job
  * `PROJECT_ID`: the name of your Google Cloud project
  * `SUBSCRIPTION_ID`: the name of your Pub/Sub subscription
  * `DATASET_NAME`: the name of your BigQuery dataset
  * `TABLE_NAME`: the name of your BigQuery table



## Publish messages to Pub/Sub

After the Dataflow job starts, you can publish messages to Pub/Sub, and the pipeline writes them to BigQuery.

### Console

  1. In the Google Cloud console, go to the **Pub/Sub** > **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. In the topic list, click the name of your topic.

  3. Click **Messages**.

  4. Click **Publish messages**.

  5. For **Number of messages** , enter `10`.

  6. For **Message body** , enter `{"name": "Alice", "customer_id": 1}`.

  7. Click **Publish**.




###  gcloud 

To publish messages to your topic, use the [`gcloud pubsub topics publish`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish) command.
    
    
    for run in {1..10}; do
      gcloud pubsub topics publish TOPIC_ID --message='{"name": "Alice", "customer_id": 1}'
    done
    

Replace `TOPIC_ID` with the name of your topic.

## View your results

View the data written to your BigQuery table. It can take up to a minute for data to start appearing in your table.

### Console

  1. In the Google Cloud console, go to the **BigQuery** page.  
[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  2. In the query editor, run the following query:
         
         SELECT * FROM `PROJECT_ID.DATASET_NAME.TABLE_NAME`
         LIMIT 1000
         

Replace the following variables:

     * `PROJECT_ID`: the name of your Google Cloud project
     * `DATASET_NAME`: the name of your BigQuery dataset
     * `TABLE_NAME`: the name of your BigQuery table



###  gcloud 

Check the results in BigQuery by running the following query:
    
    
    bq query --use_legacy_sql=false 'SELECT * FROM `PROJECT_ID.DATASET_NAME.TABLE_NAME`'
    

Replace the following variables:

  * `PROJECT_ID`: the name of your Google Cloud project
  * `DATASET_NAME`: the name of your BigQuery dataset
  * `TABLE_NAME`: the name of your BigQuery table



## Use a UDF to transform the data

This tutorial assumes that the Pub/Sub messages are formatted as JSON, and that the BigQuery table schema matches the JSON data.

Optionally, you can provide a JavaScript user-defined function (UDF) that transforms the data before it is written to BigQuery. The UDF can perform additional processing, such as filtering, removing personal identifiable information (PII), or enriching the data with additional fields.

For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

## Use a dead-letter table

While the job is running, the pipeline might fail to write individual messages to BigQuery. Possible errors include:

  * Serialization errors, including badly-formatted JSON.
  * Type conversion errors, caused by a mismatch in the table schema and the JSON data.
  * Extra fields in the JSON data that are not present in the table schema.



The pipeline writes these errors to a _dead-letter table_ in BigQuery. By default, the pipeline automatically creates a dead-letter table named `TABLE_NAME_error_records`, where `TABLE_NAME` is the name of the output table. To use a different name, set the `outputDeadletterTable` template parameter.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to eliminate billing is to delete the Google Cloud project that you created for the tutorial.

###  Console 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



###  gcloud 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the individual resources

If you want to reuse the project later, you can keep the project but delete the resources that you created during the tutorial.

#### Stop the Dataflow pipeline

### Console

  1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click the job that you want to stop.

To stop a job, the status of the job must be **running**.

  3. In the job details page, click **Stop**.

  4. Click **Cancel**.

  5. To confirm your choice, click **Stop Job**.




###  gcloud 

To cancel your Dataflow job, use the [`gcloud dataflow jobs`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list) command.
    
    
    gcloud dataflow jobs list \
      --filter 'NAME=JOB_NAME AND STATE=Running' \
      --format 'value(JOB_ID)' \
      --region "DATAFLOW_REGION" \
      | xargs gcloud dataflow jobs cancel --region "DATAFLOW_REGION"
    

#### Clean up Google Cloud project resources

### Console

  1. Delete the Pub/Sub topic and subscription.

     1. Go to the Pub/Sub **Topics** page in the Google Cloud console.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topicList)

     2. Select the topic that you created.

     3. Click **Delete** to permanently delete the topic.

     4. Go to the Pub/Sub **Subscriptions** page in the Google Cloud console.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription/list)

     5. Select the subscription created with your topic.

     6. Click **Delete** to permanently delete the subscription.

  2. Delete the BigQuery table and dataset.

     1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

     2. In the **Explorer** panel, expand your project.

     3. Next to the dataset you want to delete, click more_vert**View actions** , and then click **delete**.

  3. Delete the Cloud Storage bucket.

     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage)

     2. Select the bucket that you want to delete, click delete **Delete** , and then follow the instructions.




###  gcloud 

  1. To delete the Pub/Sub subscription and topic, use the [`gcloud pubsub subscriptions delete`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/delete) and the [`gcloud pubsub topics delete`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/delete) commands.
         
         gcloud pubsub subscriptions delete SUBSCRIPTION_ID
         gcloud pubsub topics delete TOPIC_ID
         

  2. To delete the BigQuery table, use the [`bq rm`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference) command.
         
         bq rm -f -t PROJECT_ID:tutorial_dataset.tutorial
         

  3. Delete the BigQuery dataset. The dataset alone does not incur any charges.

**Caution:** The following command also deletes all tables in the dataset. The tables and data cannot be recovered.
         
         bq rm -r -f -d PROJECT_ID:tutorial_dataset
         

  4. To delete the Cloud Storage bucket and its objects, use the [`gcloud storage rm` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm). The bucket alone does not incur any charges.
         
         gcloud storage rm gs://BUCKET_NAME --recursive
         




#### Revoke credentials

### Console

If you keep your project, revoke the roles that you granted to the Compute Engine default service account.

  1. In the Google Cloud console, go to the **IAM** page.



[ Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  1. Select a project, folder, or organization.

  2. Find the row containing the principal whose access you want to revoke. In that row, click  edit **Edit principal**.

  3. Click the **Delete** delete button for each role you want to revoke, and then click **Save**.




###  gcloud 

  * If you keep your project, revoke the roles that you granted to the Compute Engine default service account. Run the following command one time for each of the following IAM roles: 
    * `roles/dataflow.admin`
    * `roles/dataflow.worker`
    * `roles/storage.admin`
    * `roles/pubsub.editor`
    * `roles/bigquery.dataEditor`
    
    gcloud projects remove-iam-policy-binding <var>PROJECT_ID</var> \
      --member=serviceAccount:<var>PROJECT_NUMBER</var>-compute@developer.gserviceaccount.com \
      --role=<var>ROLE</var>
    

  * Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
        
        gcloud auth application-default revoke

  * Optional: Revoke credentials from the gcloud CLI. 
        
        gcloud auth revoke




## What's next

  * [Extend your Dataflow template with UDFs](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).
  * Learn more about using [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/overview).
  * View [all the Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).
  * Read about using Pub/Sub to [create and use topics](https://docs.cloud.google.com/pubsub/docs/create-topic) and how to create a [pull subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription).
  * Read about using BigQuery to [create datasets](https://docs.cloud.google.com/bigquery/docs/datasets).
  * Learn about [Pub/Sub subscriptions](https://docs.cloud.google.com/pubsub/docs/subscriber).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
