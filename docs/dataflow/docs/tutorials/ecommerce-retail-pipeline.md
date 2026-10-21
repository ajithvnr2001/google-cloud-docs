---
url: https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-retail-pipeline/
title: Create an ecommerce streaming pipeline \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:26.651482+00:00
---

# Create an ecommerce streaming pipeline  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-retail-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Create an ecommerce streaming pipeline Stay organized with collections  Save and categorize content based on your preferences. 

In this tutorial, you create a Dataflow streaming pipeline that transforms ecommerce data from Pub/Sub topics and subscriptions and outputs the data to BigQuery and Bigtable. This tutorial requires [Gradle](https://gradle.org/).

The tutorial provides an end-to-end ecommerce sample application that streams data from a webstore to BigQuery and Bigtable. The sample application illustrates common use cases and best practices for implementing streaming data analytics and real-time artificial intelligence (AI). Use this tutorial to learn how to respond dynamically to customer actions in order to analyze and react to events in real-time. This tutorial describes how to store, analyze, and visualize event data to get more insight into customer behavior.

The sample application is [available on GitHub](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/tree/master/retail/retail-java-applications). To run this tutorial using Terraform, follow the steps provided with the sample application on GitHub.

## Objectives

  * Validate incoming data and apply corrections to it where possible.
  * Analyze clickstream data to keep a count of the number of views per product in a given time period. Store this information in a low-latency store. The application can then use the data to provide _number of people who viewed this product_ messages to customers on the website.
  * Use transaction data to inform inventory ordering:

    * Analyze transaction data to calculate the total number of sales for each item, both by store and globally, for a given period.
    * Analyze inventory data to calculate the incoming inventory for each item.
    * Pass this data to inventory systems on a continuous basis so it can be used for inventory purchasing decisions.
  * Validate incoming data and apply corrections to it where possible. Write any uncorrectable data to a dead-letter queue for additional analysis and processing. Make a metric that represents the percentage of incoming data that gets sent to the dead-letter queue available for monitoring and alerting.

  * Process all incoming data into a standard format and store it in a data warehouse to use for future analysis and visualization.

  * Denormalize transaction data for in-store sales so that it can include information like the latitude and longitude of the store location. Provide the store information through a slowly changing table in BigQuery, using the store ID as a key.




### Data

The application processes the following types of data:

  * Clickstream data being sent by online systems to Pub/Sub.
  * Transaction data being sent by on-premises or software as a service (SaaS) systems to Pub/Sub.
  * Stock data being sent by on-premises or SaaS systems to Pub/Sub.

**Note:** All data is sent as JSON. This format is normal for clickstream data but not necessarily for transaction or stock data.

### Task patterns

The application contains the following task patterns common to pipelines built with the Apache Beam SDK for Java:

  * [Apache Beam schemas to work with structured data](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java#structured-data)
  * [`JsonToRow` to convert JSON data](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java#json-to-row)
  * [The `AutoValue` code generator to generate plain old Java objects (POJOs)](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java#use-autovalue)
  * [Queuing unprocessable data for further analysis](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java#queue-unprocessable-data)
  * [Serial data validation transforms](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java#data-validation-transforms)
  * [`DoFn.StartBundle` to micro-batch calls to external services](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java#micro-batch-calls)
  * [Side-input patterns](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java#side-input-pattern)



## Costs

In this document, you use the following billable components of Google Cloud: 

  * BigQuery
  * Bigtable
  * Cloud Scheduler
  * Compute Engine
  * Dataflow
  * Pub/Sub



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

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

  7. Enable the Compute Engine, Dataflow, Pub/Sub, BigQuery, Bigtable, Bigtable Admin, and Cloud Scheduler APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com dataflow.googleapis.com pubsub.googleapis.com bigquery.googleapis.com bigtable.googleapis.com bigtableadmin.googleapis.com  cloudscheduler.googleapis.com

  8. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

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

  15. Enable the Compute Engine, Dataflow, Pub/Sub, BigQuery, Bigtable, Bigtable Admin, and Cloud Scheduler APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com dataflow.googleapis.com pubsub.googleapis.com bigquery.googleapis.com bigtable.googleapis.com bigtableadmin.googleapis.com  cloudscheduler.googleapis.com

  16. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. Create a user-managed worker service account for your new pipeline and grant the necessary roles to the service account.

     1. To create the service account, run the [`gcloud iam service-accounts create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) command:
            
            gcloud iam service-accounts create retailpipeline \
                --description="Retail app data pipeline worker service account" \
                --display-name="Retail app data pipeline access"

     2. Grant roles to the service account. Run the following command once for each of the following IAM roles:

        * `roles/dataflow.admin`
        * `roles/dataflow.worker`
        * `roles/pubsub.editor`
        * `roles/bigquery.dataEditor`
        * `roles/bigtable.admin`
        * `roles/bigquery.jobUser`
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:retailpipeline@PROJECT_ID.iam.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE

Replace `SERVICE_ACCOUNT_ROLE` with each individual role.

     3. Grant your Google Account a role that lets you create access tokens for the service account:
            
            gcloud iam service-accounts add-iam-policy-binding retailpipeline@PROJECT_ID.iam.gserviceaccount.com --member="user:EMAIL_ADDRESS" --role=roles/iam.serviceAccountTokenCreator

  19. If needed, download and install [Gradle](https://gradle.org/install/).



## Create the example sources and sinks

This section explains how to create the following:

  * A Cloud Storage bucket to use as a temporary storage location
  * Streaming data sources using Pub/Sub
  * Datasets to load the data into BigQuery
  * A Bigtable instance



### Create a Cloud Storage bucket

Begin by creating a Cloud Storage bucket. This bucket is used as a temporary storage location by the Dataflow pipeline.

Use the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create):
    
    
    gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION
    

Replace the following:

  * BUCKET_NAME: a name for your Cloud Storage bucket that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). Cloud Storage bucket names must be globally unique.
  * LOCATION: the [location](https://docs.cloud.google.com/storage/docs/locations#available-locations) for the bucket.



### Create Pub/Sub topics and subscriptions

Create four Pub/Sub topics and then create three subscriptions.

To create your topics, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command once for each topic. For information about how to name a subscription, see [Guidelines to name a topic or a subscription](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).
    
    
    gcloud pubsub topics create TOPIC_NAME
    

Replace TOPIC_NAME with the following values, running the command four times, once for each topic:

  * `Clickstream-inbound`
  * `Transactions-inbound`
  * `Inventory-inbound`
  * `Inventory-outbound`



To create a subscription to your topic, run the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command once for each subscription:

  1. Create a `Clickstream-inbound-sub` subscription:
         
         gcloud pubsub subscriptions create --topic Clickstream-inbound Clickstream-inbound-sub
         

  2. Create a `Transactions-inbound-sub` subscription:
         
         gcloud pubsub subscriptions create --topic Transactions-inbound Transactions-inbound-sub
         

  3. Create an `Inventory-inbound-sub` subscription:
         
         gcloud pubsub subscriptions create --topic Inventory-inbound Inventory-inbound-sub
         




### Create BigQuery datasets and table

Create a BigQuery dataset and a [partitioned table](https://docs.cloud.google.com/bigquery/docs/partitioned-tables) with the appropriate schema for your Pub/Sub topic.

  1. Use the [`bq mk`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_mk) command to create the first dataset.
         
         bq --location=US mk \
         PROJECT_ID:Retail_Store
         

  2. Create the second dataset.
         
         bq --location=US mk \
         PROJECT_ID:Retail_Store_Aggregations
         

  3. Use the [CREATE TABLE](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_statement) SQL statement to create a table with a schema and test data. The test data has one store with an ID value of `1`. The slow update side input pattern uses this table.
         
         bq query --use_legacy_sql=false \
           'CREATE TABLE
             Retail_Store.Store_Locations
             (
               id INT64,
               city STRING,
               state STRING,
               zip INT64
             );
           INSERT INTO Retail_Store.Store_Locations
           VALUES (1, "a_city", "a_state",00000);'
         




### Create a Bigtable instance and table

Create a Bigtable instance and table. For more information about creating Bigtable instances, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).

  1. If needed, run the following command to install the [`cbt` CLI](https://docs.cloud.google.com/bigtable/docs/cbt-reference):
         
         gcloud components install cbt
         

  2. Use the [`bigtable instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/create) to create an instance:
         
         gcloud bigtable instances create aggregate-tables \
             --display-name=aggregate-tables \
             --cluster-config=id=aggregate-tables-c1,zone=CLUSTER_ZONE,nodes=1
         

Replace CLUSTER_ZONE with the [zone](https://docs.cloud.google.com/bigtable/docs/locations) where the cluster runs.

  3. Use the [`cbt createtable` command](https://docs.cloud.google.com/bigtable/docs/cbt-reference) to create a table:
         
         cbt -instance=aggregate-tables createtable PageView5MinAggregates
         

  4. Use the following command to add a column family to the table:
         
         cbt -instance=aggregate-tables createfamily PageView5MinAggregates pageViewAgg
         




## Run the pipeline

Use [Gradle](https://gradle.org/) to run a streaming pipeline. To view the Java code that the pipeline is using, see [RetailDataProcessingPipeline.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/pipelines/src/main/java/com/google/dataflow/sample/retail/pipeline/RetailDataProcessingPipeline.java).

  1. Use the `git clone` command to clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/dataflow-sample-applications.git
         

  2. Switch to the application directory:
         
         cd dataflow-sample-applications/retail/retail-java-applications
         

  3. To test the pipeline, in your shell or terminal, run the following command using Gradle:
         
         ./gradlew :data-engineering-dept:pipelines:test --tests RetailDataProcessingPipelineSimpleSmokeTest --info --rerun-tasks
         

  4. To run the pipeline, run the following command using Gradle:
         
         ./gradlew tasks executeOnDataflow -Dexec.args=" \
         --project=PROJECT_ID \
         --tempLocation=gs://BUCKET_NAME/temp/ \
         --runner=DataflowRunner \
         --region=REGION \
         --clickStreamPubSubSubscription=projects/PROJECT_ID/subscriptions/Clickstream-inbound-sub \
         --transactionsPubSubSubscription=projects/PROJECT_ID/subscriptions/Transactions-inbound-sub \
         --inventoryPubSubSubscriptions=projects/PROJECT_ID/subscriptions/Inventory-inbound-sub \
         --aggregateStockPubSubOutputTopic=projects/PROJECT_ID/topics/Inventory-outbound \
         --dataWarehouseOutputProject=PROJECT_ID \
         --serviceAccount=retailpipeline.PROJECT_ID.iam.gserviceaccount.com"
         




See the [pipeline source code](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/pipelines/src/main/java/com/google/dataflow/sample/retail/pipeline/RetailDataProcessingPipeline.java) on GitHub.

## Create and run Cloud Scheduler jobs

Create and run three Cloud Scheduler jobs, one that publishes clickstream data, one for inventory data, and one for transaction data. This step generates sample data for the pipeline.

  1. To create a Cloud Scheduler job for this tutorial, use the [`gcloud scheduler jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub) command. This step creates a publisher for clickstream data that publishes one message per minute.
         
         gcloud scheduler jobs create pubsub clickstream \
           --schedule="* * * * *" \
           --location=LOCATION \
           --topic="Clickstream-inbound" \
           --message-body='{"uid":464670,"sessionId":null,"returning":false,"lat":39.669082,"lng":-80.312306,"agent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;","event":"add-to-cart","transaction":false,"timestamp":1660091197071,"ecommerce":{"items":[{"item_name":"Donut Friday Scented T-Shirt","item_id":"67890","price":33.75,"item_brand":"Google","item_category":"Apparel","item_category_2":"Mens","item_category_3":"Shirts","item_category_4":"Tshirts","item_variant":"Black","item_list_name":"Search Results","item_list_id":"SR123","index":1,"quantity":2}]},"user_id":74378,"client_id":"52393559","page_previous":"P_3","page":"P_3","event_datetime":"2022-08-10 12:26:37"}'
         

  2. To start the Cloud Scheduler job, use the [`gcloud scheduler jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/run) command.
         
         gcloud scheduler jobs run --location=LOCATION clickstream
         

  3. Create and run another similar publisher for inventory data that publishes one message every two minutes.
         
         gcloud scheduler jobs create pubsub inventory \
           --schedule="*/2 * * * *" \
           --location=LOCATION  \
           --topic="Inventory-inbound" \
           --message-body='{"count":1,"sku":0,"aisleId":0,"product_name":null,"departmentId":0,"price":null,"recipeId":null,"image":null,"timestamp":1660149636076,"store_id":1,"product_id":10050}'
         

  4. Start the second Cloud Scheduler job.
         
         gcloud scheduler jobs run --location=LOCATION inventory
         

  5. Create and run a third publisher for transaction data that publishes one message every two minutes.
         
         gcloud scheduler jobs create pubsub transactions \
           --schedule="*/2 * * * *" \
           --location=LOCATION  \
           --topic="Transactions-inbound" \
           --message-body='{"order_number":"b8be9222-990d-11ea-9c05-42010af00081","user_id":998685,"store_id":1,"returning":false,"time_of_sale":0,"department_id":0,"product_id":4,"product_count":1,"price":25.0,"order_id":0,"order_dow":0,"order_hour_of_day":0,"order_woy":0,"days_since_prior_order":null,"product_name":null,"product_sku":0,"image":null,"timestamp":1660157951000,"ecommerce":{"items":[{"item_name":"Donut Friday Scented T-Shirt","item_id":"67890","price":33.75,"item_brand":"Google","item_category":"Apparel","item_category_2":"Mens","item_category_3":"Shirts","item_category_4":"Tshirts","item_variant":"Black","item_list_name":"Search Results","item_list_id":"SR123","index":1,"quantity":2}]},"client_id":"1686224283","page_previous":null,"page":null,"event_datetime":"2022-08-10 06:59:11"}'
         

  6. Start the third Cloud Scheduler job.
         
         gcloud scheduler jobs run --location=LOCATION transactions
         




## View your results

View data written to your BigQuery tables. Check the results in BigQuery by running the following queries. While this pipeline is running, you can see new rows appended to the BigQuery tables every minute.

You might need to wait for the tables to populate with data.
    
    
    bq query --use_legacy_sql=false 'SELECT * FROM `'"PROJECT_ID.Retail_Store.clean_inventory_data"'`'
    
    
    
    bq query --use_legacy_sql=false 'SELECT * FROM `'"PROJECT_ID.Retail_Store.clean_transaction_data"'`'
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to eliminate billing is to delete the Google Cloud project that you created for the tutorial.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

If you want to reuse the project, then delete the resources that you created for the tutorial.

#### Clean up Google Cloud project resources

  1. To delete the Cloud Scheduler jobs, use the [`gcloud scheduler jobs delete`](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/delete) command.
         
         gcloud scheduler jobs delete transactions --location=LOCATION
         
         
         gcloud scheduler jobs delete inventory --location=LOCATION
         
         
         gcloud scheduler jobs delete clickstream --location=LOCATION
         

  2. To delete the Pub/Sub subscriptions and topics, use the [`gcloud pubsub subscriptions delete`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/delete) and the [`gcloud pubsub topics delete`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/delete) commands.
         
         gcloud pubsub subscriptions delete SUBSCRIPTION_NAME
         gcloud pubsub topics delete TOPIC_NAME
         

  3. To delete the BigQuery table, use the [`bq rm`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference) command.
         
         bq rm -f -t PROJECT_ID:Retail_Store.Store_Locations
         

  4. Delete the BigQuery datasets. The dataset alone does not incur any charges.

**Caution:** The following command also deletes all tables in the dataset. The tables and data cannot be recovered.
         
         bq rm -r -f -d PROJECT_ID:Retail_Store
         
         
         bq rm -r -f -d PROJECT_ID:Retail_Store_Aggregations
         

  5. To delete the Bigtable instance, use the `cbt deleteinstance` command. The bucket alone does not incur any charges.
         
         cbt deleteinstance aggregate-tables
         

  6. To delete the Cloud Storage bucket and its objects, use the [`gcloud storage rm` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm). The bucket alone does not incur any charges.
         
         gcloud storage rm gs://BUCKET_NAME --recursive
         




#### Revoke credentials

  1. Revoke the roles that you granted to the user-managed worker service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/pubsub.editor`
     * `roles/bigquery.dataEditor`
     * `roles/bigtable.admin`
     * `roles/bigquery.jobUser`
    
    gcloud projects remove-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:retailpipeline@PROJECT_ID.iam.gserviceaccount.com \
        --role=ROLE

  2. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  3. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




## What's next

  * View [the sample application on GitHub](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/tree/master/retail/retail-java-applications).
  * Read the related blog post [Learn Beam patterns with Clickstream processing of Google Tag Manager data](https://cloud.google.com/blog/products/data-analytics/learn-beam-patterns-with-clickstream-processing-of-google-tag-manager-data).
  * Read about using Pub/Sub to [create and use topics](https://docs.cloud.google.com/pubsub/docs/create-topic) and to [Use subscriptions](https://docs.cloud.google.com/pubsub/docs/subscriber).
  * Read about using BigQuery to [create datasets](https://docs.cloud.google.com/bigquery/docs/datasets).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
