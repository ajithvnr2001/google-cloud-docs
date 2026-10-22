---
url: https://docs.cloud.google.com/datastream/docs/implementing-datastream-dataflow-analytics/
title: Implement Datastream and Dataflow for analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:33.045447+00:00
---

# Implement Datastream and Dataflow for analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/implementing-datastream-dataflow-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Implement Datastream and Dataflow for analytics Stay organized with collections  Save and categorize content based on your preferences. 

Datastream

Datastream supports streaming data from Oracle, MySQL and PostgreSQL databases directly into [BigQuery](https://docs.cloud.google.com/bigquery) datasets. However, if you need more control over the stream processing logic, such as data transformation or manual setting of logical primary keys, you can integrate Datastream with Dataflow job templates.

This tutorial shows you how Datastream integrates with [Dataflow](https://docs.cloud.google.com/dataflow) by using Dataflow job templates to stream up-to-date materialized views in BigQuery for analytics.

For organizations with many isolated data sources, access to enterprise data across the organization, especially in a real-time manner, can be limited and slow. This restricts the organization's ability to introspect.

Datastream provides near real-time access to change data from various on-premises and cloud-based data sources. Datastream provides a setup experience where you don't have to do much configuration for streaming data; Datastream does this for you. Datastream also has a unified consumption API which democratizes your organization's access to the freshest available enterprise data to build integrated scenarios.

One such scenario is transferring data from a source database into a cloud-based storage service or messaging queue. After Datastream streams the data, the data is transformed into a form that other applications and services can read. In this tutorial, Dataflow is the web service that communicates with the storage service or messaging queue to capture and process data on Google Cloud.

You learn how to use Datastream to stream changes (data that's inserted, updated, or deleted) from a source MySQL database into a folder in a [Cloud Storage](https://docs.cloud.google.com/storage) bucket. Then, you configure the Cloud Storage bucket to send notifications that Dataflow uses to learn about any new files containing the data changes that Datastream streams from the source database. A Dataflow job then processes the files and transfer the changes into BigQuery.

![integration user flow diagram](https://docs.cloud.google.com/static/datastream/docs/images/integrating-datastream-and-dataflow-overview.png)

## Objectives

In this tutorial, you: 

  * Create a bucket in Cloud Storage. This is the destination bucket into which Datastream streams schemas, tables, and data from a source MySQL database.
  * Enable Pub/Sub notifications for the Cloud Storage bucket. By doing this, you're configuring the bucket to send notifications that Dataflow uses to learn about any new files that are ready for processing. These files contain changes to data that Datastream streams from the source database into the bucket.
  * Create datasets in BigQuery. BigQuery uses datasets to contain the data that it receives from Dataflow. This data represents the changes in the source database that Datastream streams into the Cloud Storage bucket.
  * Create and manage connection profiles for a source database and a destination bucket in Cloud Storage. A stream in Datastream uses the information in the connection profiles to transfer data from the source database into the bucket.
  * Create and start a stream. This stream transfers data, schemas, and tables from the source database into the bucket.
  * Verify that Datastream transfers the data and tables associated with a schema of the source database into the bucket.
  * Create a job in Dataflow. After Datastream streams data changes from the source database into the Cloud Storage bucket, notifications are sent to Dataflow about new files containing the changes. The Dataflow job processes the files and transfers the changes into BigQuery.
  * Verify that Dataflow processes the files containing changes associated with this data, and transfers the changes into BigQuery. As a result, you have an end-to-end integration between Datastream and BigQuery.
  * Clean up the resources that you created on Datastream, Cloud Storage, Pub/Sub, Dataflow, and BigQuery so they don't take up quota and you aren't billed for them in the future.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Datastream
  * Cloud Storage
  * Pub/Sub
  * Dataflow
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

  6. Enable the Datastream API. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datastream.googleapis.com)

  7. Make sure that you have the Datastream Admin role granted to your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  8. Make sure that you have a [source MySQL database](https://docs.cloud.google.com/datastream/docs/sources-mysql) that Datastream can access. Also, verify that you have data, tables, and schemas in the database.
  9. Configure your MySQL database to allow incoming connections from Datastream public IP addresses. For a list of all Datastream regions and their associated public IP addresses, see [IP allowlists and regions](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions).
  10. Set up change data capture (CDC) for the source database. For more information, see [Configure a source MySQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-mysql-database).
  11. Make sure that you meet all [prerequisites](https://docs.cloud.google.com/storage/docs/reporting-changes#prereqs) to enable Pub/Sub notifications for Cloud Storage.

In this tutorial, you create a destination bucket in Cloud Storage and enable Pub/Sub notifications for the bucket. By doing this, Dataflow can receive notifications about new files that Datastream writes to the bucket. These files contain changes to data that Datastream streams from the source database into the bucket. 




## Requirements

Datastream offers a variety of [source options](https://docs.cloud.google.com/datastream/docs/sources), [destination options](https://docs.cloud.google.com/datastream/docs/destination), and [networking connectivity methods](https://docs.cloud.google.com/datastream/docs/network-connectivity-options).

For this tutorial, we assume that you're using a standalone MySQL database and a destination Cloud Storage service. For the source database, you should be able to configure your network to add an inbound firewall rule. The source database can be on-premises or in a cloud provider. For the Cloud Storage destination, no connectivity configuration is required.

Because we can't know the specifics of your environment, we can't provide detailed steps when it comes to your networking configuration.

For this tutorial, you select **IP allowlisting** as the network connectivity method. IP allowlisting is a security feature often used for limiting and controlling access to the data in your source database to trusted users. You can use IP allowlists to create lists of trusted IP addresses or IP ranges from which your users and other Google Cloud services such as Datastream can access this data. To use IP allowlists, you must open the source database or firewall to incoming connections from Datastream.

## Create a bucket in Cloud Storage

Create a destination bucket in Cloud Storage into which Datastream streams schemas, tables, and data from a source MySQL database.

  1. In the Google Cloud console, go to the **Browser** page for Cloud Storage.

[Go to the Browser page](https://console.cloud.google.com/storage/browser)

  2. Click **Create bucket**. The **Create a bucket** page appears.

  3. In the text field of the **Name your bucket** region, enter a unique name for your bucket, and then click **Continue**.

  4. Accept the default settings for each remaining region of the page. At the end each region, click **Continue**.

  5. Click **Create**.




## Enable Pub/Sub notifications for the Cloud Storage bucket

In this section, you enable Pub/Sub notifications for the Cloud Storage bucket that you created. By doing this, you're configuring the bucket to notify Dataflow of any new files that Datastream writes to the bucket. These files contain changes to data that Datastream streams from a source MySQL database into the bucket.

Before enabling notifications for your bucket, make sure that you meet all [prerequisites](https://docs.cloud.google.com/storage/docs/reporting-changes#prereqs).

  1. Access the Cloud Storage bucket that you created. The **Bucket details** page appears.

  2. Click terminal **Activate Cloud Shell**.

  3. At the prompt, enter the following command:

`gcloud storage buckets notifications create gs://bucket-name --topic=my_integration_notifs --payload-format=json --object-prefix=integration/tutorial/`

bucket-name is a placeholder for the name of your Cloud Storage bucket.

By entering this command, you're creating the **my_integration_notifs** topic in Pub/Sub. You're also configuring the Pub/Sub notifications to only listen to the Datastream output path which you define in the Create a destination connection profile for Cloud Storage step. Later in this procedure, you configure this topic in Pub/Sub to have notifications sent to Dataflow about changes to data that Datastream streams into your Cloud Storage bucket.

The Pub/Sub topic captures any changes to this data. Any subscribers to this topic (such as Dataflow) receive this information.

  4. Optional: If an **Authorize Cloud Shell** window appears, then click **Authorize**.

  5. Verify that you see the following lines of code:
         
         Created Cloud Pub/Sub topic projects/project-name/topics/my_integration_notifs
         Created notification config projects/_/buckets/bucket-name/notificationConfigs/1
         

project-name is a placeholder for the name of your Google Cloud project.
  6. In the Google Cloud console, go to the **Topics** page for Pub/Sub.

[Go to the Topics page](https://console.cloud.google.com/cloudpubsub/topic/list)

  7. Click the **my_integration_notifs** topic that you created.

  8. On the **my_integration_notifs** page, go to the bottom of the page. Verify that the **Subscriptions** tab is active and a **No subscriptions to display** message appears.

You're going to create a subscription for the **my_integration_notifs** topic. Apps that subscribe to this subscription, such as Dataflow, can obtain the information in the topic. This information is associated with changes to data in the source database that Datastream streams into your Cloud Storage bucket.
  9. Click **Create subscription**.

  10. In the menu that appears, select **Create subscription**.

  11. In the **Add subscription to topic** page:

     1. In the **Subscription ID** field, enter `my_integration_notifs_sub`.
     2. Set the **Acknowledgement deadline** value to `120` seconds. This allows Dataflow sufficient time to acknowledge the files it has processed, and helps improve the overall performance of the Dataflow job. For more information about Pub/Sub subscription properties, see [Subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties).
     3. Leave all other default values on the page.
     4. Click **Create**.



Later in this tutorial, you create a Dataflow job. As part of creating this job, you assign Dataflow to be a subscriber to the **my_integration_notifs_sub** subscription. By doing this, Dataflow can receive notifications about new files that Datastream writes to Cloud Storage, process the files, and transfer the data changes into BigQuery.

## Create datasets in BigQuery

In this section, you create datasets in BigQuery. BigQuery uses datasets to contain the data that it receives from Dataflow. This data represents the changes in the source MySQL database that Datastream streams into your Cloud Storage bucket.

  1. Go to the **SQL workspace** page for BigQuery in the Google Cloud console.

[Go to the SQL workspace page](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, next to your Google Cloud project name, click  more_vert  **View actions**.

  3. In the menu that appears, select **Create dataset**.

  4. In the **Create dataset** window:

     1. In the **Dataset ID** field, enter an ID for the dataset. For this tutorial, enter `My_integration_dataset_log` in the field.
     2. Leave all other default values in the window.
     3. Click **Create dataset**.
Dataflow uses the **My_integration_dataset_log** dataset to stage the data changes that it receives from Datastream.
  5. In the **Explorer** pane, next to your Google Cloud project name, click  arrow_right  **Expand node** , and then verify that you see the dataset that you created.

  6. Use the steps in this procedure to create a second dataset: **My_integration_dataset_final**.

The changes that are staged in the **My_integration_dataset_log** dataset are merged into the **My_integration_dataset_final** dataset to create a one-to-one replica of the tables in the source database.
  7. Next to each dataset, expand  arrow_right  **Expand node**.

  8. Verify that each dataset is empty.




After Datastream streams data changes from the source database into your Cloud Storage bucket, a Dataflow job processes the files containing the changes and transfers the changes into the BigQuery datasets.

## Create connection profiles in Datastream

In this section, you create connection profiles in Datastream for a source database and a destination. As part of creating the connection profiles, you select **MySQL** as the profile type for your source connection profile and **Cloud Storage** as the profile type for your destination connection profile.

Datastream uses the information defined in the connection profiles to connect to both the source and the destination so that it can stream data from the source database into your destination bucket in Cloud Storage.

### Create a source connection profile for your MySQL database

  1. In the Google Cloud console, go to the **Connection profiles** page for Datastream.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **Create profile**.

  3. To create a source connection profile for your MySQL database, in the **Create a connection profile** page, click the **MySQL** profile type.

  4. In the **Define connection settings** section of the **Create MySQL profile** page, supply the following information:

     * In the **Connection profile name** field, enter `My Source Connection Profile`.
     * Keep the autogenerated **Connection profile ID**.
     * Select the **Region** where you want to store the connection profile.

Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.
     * Enter **Connection details** :

       * In the **Hostname or IP** field, enter a hostname or public IP address that Datastream can use to connect to the source database. You're providing a public IP address because you use **IP allowlisting** as the network connectivity method for this tutorial.
       * In the **Port** field, enter the port number that's reserved for the source database. For a MySQL database, the default port is typically `3306`.
       * Enter a **Username** and **Password** to authenticate to your source database. 
  5. In the **Define connection settings** section, click **Continue**. The **Secure your connection to your source** section of the **Create MySQL profile** page is active.

  6. From the **Encryption type** menu, select **None**. For more information about this menu, see [Create a connection profile for MySQL database](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4mysqldb).

  7. In the **Secure your connection to your source** section, click **Continue**. The **Define connectivity method** section of the **Create MySQL profile** page is active.

  8. In the **Connectivity method** drop-down, choose the networking method that you'd like to use to establish connectivity between Datastream and the source database. For this tutorial, select **IP allowlisting** as the connectivity method.

  9. Configure your source database to allow incoming connections from the Datastream public IP addresses that appear.

  10. In the **Define connectivity method** section, click **Continue**. The **Test connection profile** section of the **Create MySQL profile** page is active.

  11. Click **Run test** to verify that the source database and Datastream can communicate with each other.

  12. Verify that you see the **Test passed** status. If the test fails, you can address the problem in the appropriate part of the flow, and then return to re-test. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps.

  13. Click **Create**.




### Create a destination connection profile for Cloud Storage

  1. In the Google Cloud console, go to the **Connection profiles** page for Datastream.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **Create profile**.

  3. To create a destination connection profile for Cloud Storage, in the **Create a connection profile** page, click the **Cloud Storage** profile type.

  4. In the **Create Cloud Storage profile** page, supply the following information:

     * In the **Connection profile name** field, enter `My Destination Connection Profile`.
     * Keep the autogenerated **Connection profile ID**.
     * Select the **Region** where you want to store the connection profile.
     * In the **Connection details** pane, click **Browse** to select the Cloud Storage bucket that you created earlier in this tutorial. This is the bucket into which Datastream transfers data from the source database. After making your selection, click **Select**.

Your bucket appears in the **Bucket name** field of the **Connection details** pane.

     * In the **Connection profile path prefix** field, provide a prefix for the path that you want to append to the bucket name when Datastream streams data to the destination. Make sure that Datastream writes data to a path inside the bucket, not to the bucket root folder. For this tutorial, use the path that you defined when you configured your Pub/Sub notification. Enter `/integration/tutorial` in the field.

  5. Click **Create**.




After creating a source connection profile for your MySQL database and a destination connection profile for Cloud Storage, you can use them to create a stream.

## Create a stream in Datastream

In this section, you create a stream. This stream uses the information in the connection profiles to transfer data from a source MySQL database into a destination bucket in Cloud Storage.

Datastream comes equipped with a setup assistant to help you create a stream. This assistant consists of six panels: Get started, Define & test source, Configure source, Define destination, Configure destination, and Review & create. To populate each panel, complete the instructions in the following sections.

### Define settings for the stream

  1. In the Google Cloud console, go to the **Streams** page for Datastream.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click **Create stream**.

  3. Supply the following information in the **Define stream details** panel of the **Create stream** page:

     * In the **Stream name** field, enter `My Stream`.
     * Keep the autogenerated **Stream ID**.
     * From the **Region** menu, select the region where you created your source and destination connection profiles.
     * From the **Source type** menu, select the **MySQL** profile type.
     * From the **Destination type** menu, select the **Cloud Storage** profile type.
  4. Review the required prerequisites that are generated automatically to reflect how your environment must be prepared for a stream. These prerequisites can include how to configure the source database and how to connect Datastream to the destination bucket in Cloud Storage.

For more information about these prerequisites, see [Configure a source MySQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-mysql-database).
  5. Click **Continue**. The **Define MySQL connection profile** panel of the **Create stream** page appears.




### Specify information about the source connection profile

In this section, you select the connection profile that you created for your source database (the source connection profile). For this tutorial, this is **My Source Connection Profile**.

  1. From the **Source connection profile** menu, select your source connection profile for MySQL database.

  2. Click **Run test** to verify that the source database and Datastream can communicate with each other.

If the test fails, then the issue associated with the connection profile appears. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. Make the necessary changes to correct the issue, and then retest.

  3. Click **Continue**. The **Configure stream source** panel of the **Create stream** page appears.




### Configure information about the source database for the stream

In this section, you configure information about the source database for the stream by specifying the tables and schemas in the source database that Datastream:

  * Can transfer into the destination.
  * Is restricted from transferring into the destination.



You also determine whether Datastream backfills historical data, as well as stream ongoing changes into the destination, or stream only changes to the data.

  1. Use the **Objects to include** menu to specify the tables and schemas in your source database that Datastream can transfer into a folder in the destination bucket in Cloud Storage. The menu only loads if your database has up to 5,000 objects.

For this tutorial, you want Datastream to transfer all tables and schemas. Therefore, select **All tables from all schemas** from the menu.

  2. Verify that the **Select objects to exclude** panel is set to **None**. You don't want to restrict Datastream from transferring any tables and schemas in your source database into Cloud Storage.

  3. Verify that the **Choose backfill mode for historical data** panel is set to **Automatic.** Datastream streams all existing data, in addition to changes to the data, from the source into the destination.

  4. Click **Continue**. The **Define Cloud Storage connection profile** panel of the **Create stream** page appears.




### Select a destination connection profile

In this section, you select the connection profile that you created for Cloud Storage (the destination connection profile). For this tutorial, this is **My Destination Connection Profile**.

  1. From the **Destination connection profile** menu, select your destination connection profile for Cloud Storage.

  2. Click **Continue**. The **Configure stream destination** panel of the **Create stream** page appears.




### Configure information about the destination for the stream

In this section you configure information about the destination bucket for the stream. This information includes:

  * The output format of files written to Cloud Storage.
  * The folder of the destination bucket into which Datastream transfers schemas, tables, and data from the source database.


  1. In the **Output format** field, select the format of files written to Cloud Storage. Datastream supports two output formats: Avro and JSON. For this tutorial, **Avro** is the file format.

You don't have to populate the **Stream path prefix** field. In this field, you can provide a prefix for the path that's appended to your bucket name when Datastream transfers data to the destination. This is the path of your Cloud Storage bucket into which Datastream transfers schemas, tables, and data from a source MySQL database.

You already provided the path of **/integration/tutorial** when you created the destination connection profile for Cloud Storage.

  2. Click **Continue**. The **Review stream details and create** panel of the **Create stream** page appears.




### Create the stream

  1. Verify details about the stream as well as the source and destination connection profiles that the stream uses to transfer data from a source MySQL database to a destination bucket in Cloud Storage.

  2. To validate the stream, click **Run validation**. By validating a stream, Datastream checks that the source is configured properly, validates that the stream can connect to both the source and the destination, and verifies the end-to-end configuration of the stream.

If a validation check passes, then a check mark icon appears.

If a validation check doesn't pass, then an exclamation point icon and a **See error details** button appear. Click the button, and a dialog appears, explaining why the check didn't pass and information about what to do to rectify the problem. After making the appropriate corrections, click **Revalidate**.

For more information about troubleshooting validation checks that don't pass, see [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues).

  3. After all validation checks pass, click **Create**.

  4. In the **Create stream?** dialog, click **Create**.




## Start the stream

For this tutorial, you create and start a stream separately in case the stream creation process incurs an increased load on your source database. To put off that load, you create the stream without starting it, and then start the stream when your database can handle the load.

By starting the stream, Datastream can transfer data, schemas, and tables from the source database to the destination.

  1. In the Google Cloud console, go to the **Streams** page for Datastream.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Select the checkbox next to the stream that you want to start. For this tutorial, this is **My Stream**.

  3. Click **Start**.

  4. In the dialog, click **Start**. The status of the stream changes from `Not started` to `Starting` to `Running`.

It takes about 30 seconds for the stream to start running. Background resources need to start so that the stream can start.



After starting a stream, you can verify that Datastream transferred data from the source database to the destination.

## Verify the stream

In this section, you confirm that Datastream transfers the data from all tables of a source MySQL database into the **/integration/tutorial** folder of your Cloud Storage destination bucket.

  1. In the Google Cloud console, go to the **Streams** page for Datastream.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you created. For this tutorial, this is **My Stream**.

  3. In the **Stream details** page, click the **bucket-name /integration/tutorial** link, where bucket-name is the name that you gave your Cloud Storage bucket. This link appears after the **Destination write path** field. The **Bucket details** page of Cloud Storage opens in a separate tab.

The link is comprised of the name of your bucket and the folder of your bucket into which Datastream transfers schemas, tables, and data from the source database. You specified this folder to be **/integration/tutorial** when you created the destination connection profile for Cloud Storage.
  4. Verify that you see folders that represent tables of the source database.

  5. Click one of the table folders and then click each subfolder until you see data that's associated with the table.

The first folder is `[schema]_[table]`, followed by folders that represent the year, month, day, hour, and minute that Datastream transferred data from the source database into a destination bucket in Cloud Storage.

A folder is created every minute (when there's new data to write).

A new file is created when the file size reaches 250 MB, or whenever a schema changes. If tables are partitioned, then files are created for each partition.




## Create a Dataflow job

In this section, you create a job in Dataflow. After Datastream streams data changes from a source MySQL database into your Cloud Storage bucket, Pub/Sub sends notifications to Dataflow about new files containing the changes. The Dataflow job processes the files and transfers the changes into BigQuery.

  1. In the Google Cloud console, go to the **Jobs** page for Dataflow.

[Go to the Jobs page](https://console.cloud.google.com/dataflow/jobs)

  2. Click **Create job from template**.

  3. In the **Job name** field of the **Create job from template** page, enter a name for the Dataflow job that you're creating. For this tutorial, enter `my-dataflow-integration-job` in the field.

  4. From the **Regional endpoint** menu, select the region where you want to store the job. This is the same region that you selected for the source connection profile, destination connection profile, and stream that you created.

  5. From the **Dataflow template** menu, select the template that you're using to create the job. For this tutorial, select **Datastream to BigQuery**.

After making this selection, additional fields related to this template appear.

The Datastream to BigQuery template is a streaming pipeline that reads Datastream data and replicates it into BigQuery. The template reads data from Cloud Storage using Pub/Sub notifications and replicates it into a time-partitioned BigQuery staging table. Following replication, the template executes a `Merge` in BigQuery to upsert all change data capture (CDC) changes into a replica of the source table.

To minimize the cost associated with frequent `Merge` operations, we suggest starting with an initial frequency of once every 6-12 hours. After all backfills have completed and data is replicating smoothly, reduce this value to your selected frequency.

For more information about the Datastream to BigQuery template, see [Datastream to BigQuery (Stream)](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#datastream-to-bigquery).

  6. In the **File location for Datastream file output in Cloud Storage.** field, enter the name of your Cloud Storage bucket using the following format: `gs://bucket-name`.

  7. In the **Pub/Sub subscription being used in a Cloud Storage notification policy.** field, enter the path that contains the name of your Pub/Sub subscription. For this tutorial, enter `projects/project-name/subscriptions/my_integration_notifs_sub`.

project-name is a placeholder for the name of your Google Cloud project. Also, you created the **my_integration_notifs_sub** subscription in the Enabling Pub/Sub notifications for the Cloud Storage bucket section of this tutorial.
  8. In the **Datastream output file format (avro/json).** field, enter `avro` because, for this tutorial, Avro is the file format of files that Datastream writes to Cloud Storage.

  9. In the **Name or template for the dataset to contain staging tables.** field, enter `My_integration_dataset_log` because Dataflow uses this dataset to stage the data changes that it receives from Datastream.

  10. In the **Template for the dataset to contain replica tables.** field, enter `My_integration_dataset_final` because this is the dataset where the changes that are staged in the **My_integration_dataset_log** dataset merge to create a one-to-one replica of the tables in the source database.

You created the **My_integration_dataset_log** and **My_integration_dataset_final** datasets in the Create datasets in BigQuery section of this tutorial.
  11. In the **Dead letter queue directory.** field, enter the path that contains the name of a separate Cloud Storage bucket and a folder for a dead letter queue. Make sure that you don't use a path in the root folder, and that the path is different than the one to which Datastream writes data. Any data changes that Dataflow fails to transfer into BigQuery are stored in the queue. You can fix the content in the queue so that Dataflow can reprocess it.

For this tutorial, enter `gs://dlq-bucket-name/dlq` in the **Dead letter queue directory.** field (where dlq-bucket-name is the name of your Cloud Storage bucket dedicated to the dead letter queue and **dlq** is the folder for the dead letter queue).

  12. Click **Run job**.


It might take several minutes for your Dataflow job to run. Background resources need to run. Also, the job has to process the files containing the data changes that it receives from Cloud Storage before it can transfer these changes into BigQuery.

## Verify the integration

In the Verify the stream section of this tutorial, you confirmed that Datastream transferred the data from all tables of a source MySQL database into the **/integration/tutorial** folder of your Cloud Storage destination bucket.

In this section, you verify that Dataflow processes the files containing changes associated with this data, and transfers the changes into BigQuery. As a result, you have an end-to-end integration between Datastream and BigQuery.

  1. In the Google Cloud console, go to the **SQL workspace** page for BigQuery.

[Go to the SQL workspace page](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, expand the node next to the name of your Google Cloud project.

  3. Expand the nodes next to the **My_integration_dataset_log** and **My_integration_dataset_final** datasets.

  4. Verify that each dataset now contains data. This confirms that Dataflow processed the files containing changes associated with the data that Datastream streamed into Cloud Storage, and transferred these changes into BigQuery.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, use the Google Cloud console to do the following:

  * Delete your project, Datastream stream, and Datastream connection profiles.
  * Stop the Dataflow job.
  * Delete the BigQuery datasets, Pub/Sub topic and subscription, and Cloud Storage bucket.



By cleaning up the resources that you created on Datastream, Dataflow, BigQuery, Pub/Sub, and Cloud Storage, you prevent the resources from taking up quota and you aren't billed for them in the future.

### Delete your project

The easiest way to eliminate billing is to delete the project that you created for this tutorial.

Deleting a project has the following effects:

  * **Everything in the project is deleted.** If you used an existing project for this tutorial, then when you delete it, you also delete any other work you've done in the project.
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as the `**appspot.com**` URL, delete selected resources inside the project instead of deleting the whole project.



If you plan to explore multiple tutorials and quickstarts, then reusing projects can help you avoid exceeding project quota limits.

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. In the project list, select the project that you want to delete, and then click **Delete**.

  3. To delete the project, in the dialog, type the project ID, and then click **Shut down**.




### Delete the stream

  1. In the Google Cloud console, go to the **Streams** page for Datastream.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you want to delete. For this tutorial, this is **My Stream**.

  3. Click **Pause**.

  4. In the dialog, click **Pause**.

  5. In the **Stream status** pane of the **Stream details** page, verify that the status of the stream is `Paused`.

You pause the stream before deleting it to make sure that all in-flight data transfers from the source database to the destination.
  6. Click **Delete**.

  7. In the dialog, in the text field, enter `Delete`, and then click **Delete**.




### Delete the connection profiles

  1. In the Google Cloud console, go to the **Connection profiles** page for Datastream.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Select the checkbox for each connection profile that you want to delete: **My Source Connection Profile** and **My Destination Connection Profile**.

  3. Click **Delete**.

  4. In the dialog, click **Delete**.




### Stop the Dataflow job

You can't delete a job in Dataflow. However, you can stop a job so that the job no longer processes files containing data changes that stream into the Cloud Storage bucket or transfers the data changes into BigQuery.

  1. In the Google Cloud console, go to the **Jobs** page for Dataflow.

[Go to the Jobs page](https://console.cloud.google.com/dataflow/jobs)

  2. Click the job that you want to stop. For this tutorial, this is **my-dataflow-integration-job**.

  3. Click **Stop**.

  4. In the **Stop job** dialog, select the **Drain** option, and then click **Stop job**.

Dataflow finishes processing any remaining buffered data so that all in-flight" data transfers into BigQuery before the job stops.



### Delete the BigQuery datasets

  1. In the Google Cloud console, go to the **SQL workspace** page for BigQuery.

[Go to the SQL workspace page](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, expand the node next to your Google Cloud project name.

  3. Click the **View actions** button to the right of one of the datasets that you created in Create datasets in BigQuery. This button looks like a vertical ellipsis.

For this tutorial, click the **View actions** button to the right of **My_integration_dataset_log**.

  4. Select **Delete** from the drop-down menu that appears.

  5. In the **Delete dataset?** dialog, enter `delete` in the text field, and then click **Delete**.

  6. Repeat the steps in this procedure to delete the second dataset that you created: **My_integration_dataset_final**.




### Delete the Pub/Sub subscription and topic

  1. In the Google Cloud console, go to the **Subscriptions** page for Pub/Sub.

[Go to the Subscriptions page](https://console.cloud.google.com/cloudpubsub/subscription/list)

  2. Click the checkbox next to the subscription that you want to delete. For this tutorial, click the checkbox next to the **my_integration_notifs_sub** subscription.

  3. Click **Delete**.

  4. In the **Delete subscription** dialog, click **Delete**.

  5. In the Google Cloud console, go to the **Topics** page for Pub/Sub.

[Go to the Topics page](https://console.cloud.google.com/cloudpubsub/topic/list)

  6. Click the checkbox next to the **my_integration_notifs** topic.

  7. Click **Delete**.

  8. In the **Delete topic** dialog, enter `delete` in the text field, and then click **Delete**.




### Delete your Cloud Storage bucket

  1. In the Google Cloud console, go to the **Browser** page for Cloud Storage.

[Go to the Browser page](https://console.cloud.google.com/storage/browser)

  2. Select the checkbox next to your bucket.

  3. Click **Delete**.

  4. In the dialog, enter `Delete` in the text field, and then click **Delete**.




## What's next

  * Learn more about [Datastream](https://docs.cloud.google.com/datastream/docs).
  * [Use the legacy streaming API](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery) to perform advanced capabilities with streaming data into BigQuery.
  * Try out other Google Cloud features for yourself. Have a look at our [tutorials](https://cloud.google.com/docs/tutorials).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
