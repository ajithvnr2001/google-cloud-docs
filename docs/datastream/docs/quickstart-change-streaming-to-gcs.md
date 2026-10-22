---
url: https://docs.cloud.google.com/datastream/docs/quickstart-change-streaming-to-gcs/
title: Stream changes to data in near real-time with Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:06.251882+00:00
---

# Stream changes to data in near real-time with Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/quickstart-change-streaming-to-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Stream changes to data in near real-time with Datastream

Learn how to replicate data from an Oracle source database to a Cloud Storage bucket using Datastream.

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

  6. Enable the Datastream API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datastream.googleapis.com)

  7. Make sure you have the Datastream Admin role assigned to your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




If you want to create a [private connectivity configuration](https://docs.cloud.google.com/datastream/docs/private-connectivity) for a standard or shared VPC network, you need to complete additional prerequisites. For more information, see [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration#before-you-begin).

## Requirements

Datastream offers a variety of source options, destination options, and networking connectivity methods.

In this quickstart, we assume that you're using a standalone Oracle database and a destination Cloud Storage service. For the source database, you should be able to configure your network to add an inbound firewall rule. The source database can be on-premises or in a cloud provider. Because the destination is Cloud Storage, it should be in Google's cloud provider.

Because we can't know the specifics of your environment, we can't provide detailed steps when it comes to your networking configuration.

For this quickstart, you'll select **IP allowlisting** as the connectivity method. IP allowlisting is a security feature often used for limiting and controlling access to the data in your source database to trusted users. You can use IP allowlists to create lists of trusted IP addresses or IP ranges from which your users and other Cloud services such as Datastream can access this data. To use IP allowlists, you must open the source database or firewall to incoming connections from Datastream.

## Create connection profiles

By creating connection profiles for a source database and a destination, you're creating records that contain information about the source and the destination.

In this quickstart, you'll select **Oracle** as the profile type for your source connection profile, and **Cloud Storage** as the profile type for your destination connection profile. Datastream uses the information in the connection profiles to migrate data from the source Oracle database into a destination bucket in Cloud Storage.

### Create a source connection profile for Oracle database

  1. Go to the **Connection profiles** page for Datastream in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **Oracle** profile type (because you want to create a source connection profile for Oracle database).

  4. Supply the following information in the **Define connection settings** section of the **Create Oracle profile** page:

     * Enter `My Source Connection Profile` as the **Connection profile name** for your source database.
     * Keep the auto-generated **Connection profile ID**.
     * Select the **Region** where the connection profile will be stored.
Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.
     * Enter **Connection details** :
     * In the **Hostname or IP** field, enter a hostname or public IP address that Datastream can use to connect to the source Oracle database. You're providing a public IP address because **IP allowlist** will be used as the network connectivity method for this quickstart.
     * In the **Port** field, enter the port number that's reserved for the source database. For an Oracle database, the default port is typically `1521`.
     * Enter a **Username** and **Password** to authenticate to your source database.
     * In the **System identifier (SID)** field, enter the SID or service name that identifies the database instance. For Oracle databases, this is typically `ORCL`.
  5. In the **Define connection settings** section, click **CONTINUE**. The **Define connectivity method** section of the **Create Oracle profile** page is active.

  6. Choose the networking method that you'd like to use to establish connectivity between Datastream and the source database. For this quickstart, use the **Connectivity method** drop-down menu to select **IP allowlisting** as the networking method.

  7. Configure your source database to allow incoming connections from the Datastream public IP addresses that appear.

  8. In the **Define connectivity method** section, click **CONTINUE**. The **Test connection profile** section of the **Create Oracle profile** page is active.




Datastream comes equipped with a wizard to help you create a stream. This wizard consists of six panels: Get started, Define & test source, Configure source, Define destination, Configure destination, and Review & create. Information on how to populate each panel is provided in the various sections of this page.

### Define settings for the stream

  1. Go to the **Streams** page for Datastream in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click **CREATE STREAM**.

  3. Supply the following information in the **Define stream details** panel of the **Create stream** page:

     * Enter `My Stream` as the **Stream name**.
     * Keep the auto-generated **Stream ID**.
     * From the **Region** menu, select the region where you created your source connection profile.
     * From the **Source type** menu, select the **Oracle** profile type.
     * From the **Destination type** menu, select the **Cloud Storage** profile type.
  4. Review the required prerequisites that are generated automatically to reflect how your environment must be prepared for a stream. These prerequisites can include how to configure the source database and how to connect Datastream to the destination bucket in Cloud Storage.

For more information about these prerequisites, see [Configure a source Oracle database](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database).
  5. Click **CONTINUE**. The **Define Oracle connection profile** panel of the **Create stream** page appears.




### Specify information about the source connection profile

  1. From the **Source connection profile** menu, select your source connection profile for Oracle database.

  2. Click **RUN TEST** to verify that the source database and Datastream can communicate with each other.

If the test fails, then the issue associated with the connection profile appears. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. Make the necessary changes to correct the issue, and then retest.

  3. Click **CONTINUE**. The **Configure stream source** panel of the **Create stream** page appears.




### Configure information about the source database for the stream

  1. Use the **Objects to include** menu to specify the tables and schemas in your source database that Datastream can transfer into a folder in the destination bucket in Cloud Storage. The menu only loads if your database has up to 5,000 objects.

For this quickstart, you want Datastream to transfer all tables and schemas. Therefore, select **All tables from all schemas** from the menu.

For this quickstart, make sure that the **Select objects to exclude** panel is set to "None." You don't want to restrict Datastream from transferring any tables and schemas in your source database into Cloud Storage.

Also, make sure that the **Choose backfill mode for historical data** panel is set to "Automatic." Datastream will stream all existing data, in addition to changes to the data, from the source into the destination. 

  2. Specify the CDC method. For this tutorial, select **Logminer**.

  3. Click **CONTINUE**. The **Define Cloud Storage connection profile** panel of the **Create stream** page appears.




### Select a destination connection profile

  1. From the **destination connection profile** menu, select your destination connection profile for Cloud Storage.

  2. Click **CONTINUE**. The **Configure stream destination** panel of the **Create stream** page appears.




### Configure information about the destination for the stream

  1. In the **Stream path prefix** field, enter the folder of the destination bucket into which Datastream will transfer schemas, tables, and data from a source Oracle database.

For this quickstart, you want Datastream to transfer data from the source database into the `/root/tutorial` folder in the destination bucket of Cloud Storage. Therefore, enter `/root/tutorial` in the **Stream path prefix** field.

  2. In the **Output format** field, select the format of files written to Cloud Storage. For this quickstart, **Avro** is the file format.

  3. Click **CONTINUE**. The **Review stream details and create** panel of the **Create stream** page appears.




### Create the stream

  1. Verify details about the stream as well as the source and destination connection profiles that the stream will use to transfer data from a source Oracle database to a destination bucket in Cloud Storage.

  2. Click **RUN VALIDATION** to validate the stream. By validating a stream, Datastream checks that the source is configured properly, validates that the stream can connect to both the source and the destination, and verifies the end-to-end configuration of the stream.

If a validation check passes, then a check mark icon appears to the left of the validation check. 

If a validation check doesn't pass, then an exclamation point icon appears to the left of the check, and a **SEE ERROR DETAILS** button appears below the check. Click the button, and a message appears, explaining why the check didn't pass and information about what to do to rectify the problem. After making the appropriate corrections, click **REVALIDATE**.

For more information about troubleshooting validation checks that don't pass, see [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues).

  3. After all validation checks pass, click **CREATE**.

  4. In the **Create stream?** dialog, click **CREATE**.




After creating a stream, you can start it.

## Start the stream

In the previous section of the quickstart, you created a stream, but you didn't start it. You can do this now.

For this quickstart, you create and start a stream separately in case the stream creation process incurs an increased load on your source database. To put off that load, you create the stream without starting it, and then start the stream when the load can be incurred.

By starting the stream, Datastream can transfer data, schemas, and tables from the source database to the destination.

  1. Go to the **Streams** page for Datastream in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Select the checkbox to the left of the stream that you want to start. For this quickstart, this is **My Stream**.

  3. Click **START**.

  4. In the dialog, click **START**. The status of the stream changes from `Not started` to `Starting` to `Running`.

It takes about 30 seconds for the stream to start running. Background resources need to start so that the stream can start.



After starting a stream, you can verify that Datastream transferred data from the source database to the destination.

## Verify the stream

In this section, you confirm that Datastream transfers the data from all tables of your source Oracle database into the `/root/tutorial` folder of your Cloud Storage destination bucket.

  1. Go to the **Streams** page for Datastream in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you created. For this quickstart, this is **My Stream**.

  3. In the **Stream details** page, click the link that appears below the **Destination write path** field. The **Bucket details** page of Cloud Storage opens in a separate tab.

**Note:** The link you click is comprised of the name of your bucket and the folder of your bucket into which Datastream transferred schemas, tables, and data from your source Oracle database. You specified this folder to be `/root/tutorial` when you configured information about the destination connection profile for your stream. So, the link should appear as BUCKET-NAME/root/tutorial**.
  4. Verify that you see folders that represent tables of your source Oracle database.

  5. Click one of the table folders and drill down until you see data that's associated with the table.

The first folder is `[schema]_[table]`, followed by folders that represent the year, month, day, hour, and minute that Datastream transferred data from the source Oracle database into a destination bucket in Cloud Storage.

A folder is created every minute (when there's new data to write).

A new file is created when the file size reaches 250 MB, or whenever a schema changes. If tables are partitioned, then files are created for each partition.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Use the Google Cloud console to delete your project, Datastream stream and connection profiles, and Cloud Storage destination bucket.



By cleaning up the resources that you created on Datastream, they won't take up quota and you won't be billed for them in the future. The following sections describe how to delete or turn off these resources.

### Delete your project

The easiest way to eliminate billing is to delete the project that you created for this quickstart.

Deleting a project has the following effects:

  * **Everything in the project is deleted.** If you used an existing project for this quickstart, then when you delete it, you also delete any other work you've done in the project.
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as `**appspot.com**`, delete selected resources inside the project instead of deleting the whole project.



If you plan to explore multiple tutorials and quickstarts, then reusing projects can help you avoid exceeding project quota limits.

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. In the project list, select the project that you want to delete, and then click **Delete**.

  3. In the dialog, type the project ID, and then click **Shut down** to delete the project.




### Delete the stream

  1. Go to the **Streams** page for Datastream in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you want to delete. For this quickstart, this is **My Stream**.

  3. Click **PAUSE**.

  4. In the dialog, click **PAUSE**.

  5. In the **Stream status** pane of the **Stream details** page, verify that the status of the stream is `Paused`.

**Note:** You pause the stream before deleting it to make sure that all "in flight" data is transferred cleanly from the source database to the destination.
  6. Click **DELETE**.

  7. In the dialog, enter `Delete` in the text field, and then click **DELETE**.




### Delete the connection profiles

  1. Go to the **Connection profiles** page for Datastream in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Select the checkbox for each connection profile that you want to delete. For this quickstart, select the check boxes for **My Source Connection Profile** and **My Destination Connection Profile**.

  3. Click **DELETE**.

  4. In the dialog, click **DELETE**.




### Delete your Cloud Storage destination bucket

  1. Go to the **Browser** page for Cloud Storage in the Google Cloud Console.

[Go to the Browser page](https://console.cloud.google.com/storage/browser)

  2. Select the checkbox to the left of your bucket, and then click **DELETE**.

  3. In the dialog, enter `DELETE` in the text field, and then click **DELETE**.




## What's next

  * Learn more about [Datastream](https://docs.cloud.google.com/datastream/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
