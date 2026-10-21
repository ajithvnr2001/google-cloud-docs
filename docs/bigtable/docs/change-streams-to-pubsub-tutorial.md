---
url: https://docs.cloud.google.com/bigtable/docs/change-streams-to-pubsub-tutorial/
title: Stream changes to Pub/Sub using optional Cloud Run function trigger \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:26.183073+00:00
---

# Stream changes to Pub/Sub using optional Cloud Run function trigger  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/change-streams-to-pubsub-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback 

#  Stream changes to Pub/Sub using optional Cloud Run function trigger Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to use the **Bigtable change streams to Pub/Sub** template, including how to set up a topic and configure the template. You can optionally create a Cloud Run function, in the programming language of your choice, that is triggered by the event stream.

This tutorial is intended for technical users who are familiar with Bigtable, writing code, and event streaming services.

## Objectives

This tutorial shows you how to do the following:

  * Create a Bigtable table with a change stream enabled.
  * Create a Pub/Sub topic with the Bigtable change stream schema.
  * Deploy a Bigtable change stream to a Pub/Sub pipeline on Dataflow using the template.
  * View the event stream in Pub/Sub directly or in the logs of a Cloud Run function.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Bigtable](https://docs.cloud.google.com/bigtable/pricing)
  * [ Compute Engine](https://cloud.google.com/products/compute/pricing)
  * [ Dataflow](https://docs.cloud.google.com/dataflow/pricing)
  * [ Cloud Run functions](https://docs.cloud.google.com/functions/pricing)
  * [ Pub/Sub](https://docs.cloud.google.com/pubsub/pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the Dataflow, Cloud Bigtable API, Cloud Bigtable Admin API, Pub/Sub, Cloud Run functions, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow.googleapis.com,bigtable.googleapis.com,bigtableadmin.googleapis.com,pubsub.googleapis.com,cloudfunctions.googleapis.com,storage.googleapis.com)

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the Dataflow, Cloud Bigtable API, Cloud Bigtable Admin API, Pub/Sub, Cloud Run functions, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow.googleapis.com,bigtable.googleapis.com,bigtableadmin.googleapis.com,pubsub.googleapis.com,cloudfunctions.googleapis.com,storage.googleapis.com)

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  1. Update and install the `cbt` CLI . 
         
         gcloud components update
         gcloud components install cbt




## Create a Pub/Sub topic

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click **Create topic**.

  3. Set the ID to `bigtable-change-stream-topic`.

  4. Select **Use a schema**.

  5. In the **Select a Pub/Sub schema** drop-down, click **Create new schema**. This opens a new tab where you define the schema.

     1. Set the schema ID to `bigtable-change-stream-schema`.
     2. Set the schema type to _Avro_.
     3. Paste the following as the schema definition. More information about the schema can be found on the [template documentation page](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-pubsub).
    
    {
          "name" : "ChangelogEntryMessage",
          "type" : "record",
          "namespace" : "com.google.cloud.teleport.bigtable",
          "fields" : [
            { "name" : "rowKey", "type" : "bytes"},
            {
              "name" : "modType",
              "type" : {
                "name": "ModType",
                "type": "enum",
                "symbols": ["SET_CELL", "DELETE_FAMILY", "DELETE_CELLS", "UNKNOWN"]}
            },
            { "name": "isGC", "type": "boolean" },
            { "name": "tieBreaker", "type": "int"},
            { "name": "columnFamily", "type": "string"},
            { "name": "commitTimestamp", "type" : "long"},
            { "name" : "sourceInstance", "type" : "string"},
            { "name" : "sourceCluster", "type" : "string"},
            { "name" : "sourceTable", "type" : "string"},
            { "name": "column", "type" : ["null", "bytes"]},
            { "name": "timestamp", "type" : ["null", "long"]},
            { "name": "timestampFrom", "type" : ["null", "long"]},
            { "name": "timestampTo", "type" : ["null", "long"]},
            { "name" : "value", "type" : ["null", "bytes"]}
        ]
      }
    

     1. Click **Create** to create the schema.
  6. Close the **Create schema** tab, refresh the schema list, and select your newly defined schema.

  7. Click **Create** to create the topic.




### Optional: Create a Cloud Run function

You might want to process the Pub/Sub stream with a Cloud Run function.

  1. On the **Details** page for the `bigtable-change-stream-topic` topic, click **Trigger Cloud Function** .
  2. In the **Function name** field, enter the name `bt-ps-tutorial-function`.
  3. In the **Source Code** section, click the **Runtime** drop-down, and then select the runtime and programming language of your choice. A `hello world` is generated that prints out the change stream as it comes in. See the documentation to learn more about [writing Cloud Run functions](https://docs.cloud.google.com/functions).
  4. Use the default values for all other fields.
  5. Click **Deploy function**.



## Create a table with a change stream enabled

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Go to Instances](https://console.cloud.google.com/bigtable/instances)

  2. Click the ID of the instance that you are using for this tutorial.

If you don't have an instance available, [create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) with the default configurations in a region near you.

  3. In the left navigation pane, click **Tables**.

  4. Click **Create a table**.

  5. Name the table `change-streams-pubsub-tutorial`.

  6. Add a column family named `cf`.

  7. Select **Enable change stream**.

  8. Click **Create**.




## Initialize a data pipeline to capture the change stream

  1. On the Bigtable **Tables** page, find your table `change-streams-pubsub-tutorial`.
  2. In the **Change stream** column, click **Connect**.
  3. In the dialog, select **Pub/Sub**.
  4. Click **Create Dataflow job**.
  5. On the Dataflow **Create job** page, set the output Pub/Sub topic name to: `bigtable-change-stream-topic`.
  6. Set the Bigtable application profile ID to `default`.
  7. Click **Run job**.
  8. Wait until the job status is **Starting** or **Running** before proceeding. It takes around 5 minutes once the job is queued.



## Write some data to Bigtable

  1. In the Cloud Shell, write a few rows to Bigtable so the change log can write some data to the Pub/Sub stream. As long as you write the data after the job is created, the changes appear. You don't have to wait for the job status to become `running`.
         
         cbt -instance=BIGTABLE_INSTANCE_ID -project=YOUR_PROJECT_ID \
             set change-streams-pubsub-tutorial user123 cf:col1=abc
         cbt -instance=BIGTABLE_INSTANCE_ID -project=YOUR_PROJECT_ID \
             set change-streams-pubsub-tutorial user546 cf:col1=def
         cbt -instance=BIGTABLE_INSTANCE_ID -project=YOUR_PROJECT_ID \
             set change-streams-pubsub-tutorial user789 cf:col1=ghi
         




## View the change logs in Pub/Sub

  1. In the Google Cloud console, go to the Pub/Sub **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click the automatically created subscription for your topic `bigtable-change-stream-topic`. It should be named `bigtable-change-stream-topic-sub`.

  3. Go to to the **Messages** tab.

  4. Click **Pull**.

  5. Explore the list of messages and view the data that you wrote.

![Change log messages in
Pub/Sub](https://docs.cloud.google.com/bigtable/img/pubsub-change-log-tutorial.png)




## Optional: View the changes in the Cloud Run functions logs

If you created a Cloud Run functions function, you can view the changes in the logs.

  1. In the Google Cloud console, go to **Cloud Run functions**.

[Go to Cloud Run functions](https://console.cloud.google.com/functions)

  2. Click your function `bt-ps-tutorial-function`.

  3. Go to the **Logs** tab.

  4. Ensure that **Severity** is set to at least **Info** so you can see the logs.

  5. Explore the logs and view the data that you wrote.




The output looks similar to the following:
    
    
    Pub/Sub message: {"rowKey":"user789","modType":"SET_CELL","isGC":false,"tieBreaker":0,"columnFamily":"cf","commitTimestamp":1695653833064548,"sourceInstance":"YOUR-INSTANCE","sourceCluster":"YOUR-INSTANCE-c1","sourceTable":"change-streams-pubsub-tutorial","column":{"bytes":"col1"},"timestamp":{"long":1695653832278000},"timestampFrom":null,"timestampTo":null,"value":{"bytes":"ghi"}}
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

## Delete the Bigtable table

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Go to Instances](https://console.cloud.google.com/bigtable/instances)

  2. Click the ID of the instance that you are using for this tutorial.

  3. In the left navigation pane, click **Tables**.

  4. Find the `change-streams-pubsub-tutorial` table.

  5. Click **Edit**.

  6. Clear **Enable change stream**.

  7. Click **Save**.

  8. Open the overflow menu for the table.

  9. Click **Delete** and input the table name to confirm.




## Stop the change stream pipeline

  1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[ Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Select your streaming job from the job list.

  3. In the navigation, click **Stop**.

  4. In the **Stop job** dialog, cancel your pipeline, and then click **Stop job**.




## Delete the Pub/Sub topic and subcription

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Select the `bigtable-change-stream-topic` topic.

  3. Click **Delete** and confirm.

  4. Click **Subscriptions** in the sidebar.

  5. Select the `bigtable-change-stream-topic-sub` subscription.

  6. Click **Delete** and confirm.




## Delete the Cloud Run function

  1. In the Google Cloud console, go to **Cloud Run functions**.

[Go to Cloud Run functions](https://console.cloud.google.com/functions)

  2. Select the `bt-ps-tutorial-function` function.

  3. Click **Delete** and confirm.




## What's next

  * [Read through the change streams documentation.](https://docs.cloud.google.com/bigtable/docs/change-streams-overview)
  * [Learn more about writing event driven functions with Cloud Run functions.](https://docs.cloud.google.com/functions/docs/writing/write-event-driven-functions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
