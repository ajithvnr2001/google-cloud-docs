---
url: https://docs.cloud.google.com/datastream/docs/quickstart-replication-to-bigquery/
title: Replicate data to BigQuery in near real-time with Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:24.678294+00:00
---

# Replicate data to BigQuery in near real-time with Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/quickstart-replication-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Replicate data to BigQuery in near real-time with Datastream

Learn how to replicate data from a source database to BigQuery datasets using Datastream.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=datastream--quickstart-replicate-to-bigquery)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Datastream API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datastream.googleapis.com)

  5. Make sure that you have the following role or roles on the project: Support User, Datastream Admin, Monitoring Metrics Scopes Viewer, Gemini for Google Cloud Settings Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Datastream API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datastream.googleapis.com)

  9. Make sure that you have the following role or roles on the project: Support User, Datastream Admin, Monitoring Metrics Scopes Viewer, Gemini for Google Cloud Settings Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 




If you want to create a [private connectivity configuration](https://docs.cloud.google.com/datastream/docs/private-connectivity) for a standard or shared VPC network, you need to complete additional prerequisites. For more information, see [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration#before-you-begin).

## Requirements

Datastream offers a variety of source options, destination options, and networking connectivity methods.

In this quickstart, we assume that you're replicating data from a Cloud SQL for PostgreSQL database to BigQuery. For the source database, you should be able to configure your database instance to accept connections from Datastream public IP addresses.

Because we can't know the specifics of your environment, we can't provide detailed steps when it comes to your networking configuration.

For this quickstart, you'll select **IP allowlisting** as the network connectivity method. IP allowlisting is a security feature often used for limiting and controlling access to the data in your source database to trusted users. You can use IP allowlists to create lists of trusted IP addresses or IP ranges from which your users and other Cloud services such as Datastream can access this data. To use IP allowlists, you must open the source Cloud SQL database to incoming connections from Datastream.

## Create connection profiles

By creating connection profiles, you're storing some basic information about the source and the destination in Datastream. You can then re-use this information in multiple streams.

In this quickstart, you'll select **PostgreSQL** as the profile type for your source connection profile, and **BigQuery** as the profile type for your destination connection profile. Datastream uses the information in the connection profiles to connect to the source database and to BigQuery.

### Create a source connection profile for PostgreSQL database

  1. Go to the **Connection profiles** page for Datastream in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **PostgreSQL** profile type (because you want to create a source connection profile for PostgreSQL database).

  4. Supply the following information in the **Define connection settings** section of the **Create PostgreSQL profile** page:

     * Enter `My Source Connection Profile` as the **Connection profile name** for your source database.
     * Keep the auto-generated **Connection profile ID**.
     * Select the **Region** where the connection profile will be stored.
Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.
     * Enter **Connection details** :
     * In the **Hostname or IP** field, enter a hostname or public IP address that Datastream can use to connect to the source PostgreSQL database. You're providing a public IP address because **IP allowlist** will be used as the network connectivity method for this quickstart.
     * In the **Port** field, enter the port number that's reserved for the source database. For a PostgreSQL database, the default port is typically `5432`.
     * Enter a **Username** and **Password** to authenticate to your source database.
     * In the **Database** field, enter the name that identifies the database instance. For PostgreSQL databases, this is typically `postgres`.
  5. In the **Define connection settings** section, click **CONTINUE**. The **Define connectivity method** section of the **Create PostgreSQL profile** page is active.

  6. Choose the networking method that you'd like to use to establish connectivity between the source database and Datastream. For this quickstart, use the **Connectivity method** drop-down menu to select **IP allowlisting** as the networking method.

  7. Configure your source database to allow incoming connections from the Datastream public IP addresses that appear.

  8. In the **Define connectivity method** section, click **CONTINUE**. The **Test connection profile** section of the **Create PostgreSQL profile** page is active.

  9. Click **RUN TEST** to verify that the source PostgreSQL database and Datastream can communicate with each other.

  10. Verify that the "Test passed" status appears.

  11. If the test fails, you can address the problem in the appropriate part of the flow, and then return to re-test. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps.

  12. Click **CREATE**.




### Create a destination connection profile for BigQuery

  1. Go to the **Connection profiles** page for Datastream in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **BigQuery** profile type (because you want to create a destination connection profile for BigQuery).

  4. Supply the following information in the **Create BigQuery profile** page:

     * Enter `My Destination Connection Profile` as the **Connection profile name** for your destination BigQuery service.
     * Keep the auto-generated **Connection profile ID**.
     * Select the **Region** where the connection profile will be stored.
  5. Click **CREATE**.




After creating a source connection profile for PostgreSQL database and a destination connection profile for BigQuery, you can use them to create a stream.

## Create a stream

In this section, you create a stream to replicate data from a source PostgreSQL database to BigQuery.

Creating a stream includes:

  * Defining settings for the stream.
  * Selecting the connection profile that you created for your source database (the source connection profile). For this quickstart, this is **My Source Connection Profile**.
  * Configuring information about the source database for the stream by specifying the replication properties, and the tables and schemas in the source database that Datastream: 
    * Can transfer into the destination.
    * Is restricted from transferring into the destination.
  * Determining whether Datastream will backfill historical data, as well as stream ongoing changes into the destination, or stream only changes to the data.
  * Selecting the connection profile that you created for BigQuery (the destination connection profile). For this quickstart, this is **My Destination Connection Profile**.
  * Configuring information about the destination for the stream, such as configuring the BigQuery datasets.
  * Validating the stream.



Datastream comes equipped with a wizard to help you create a stream. This wizard consists of six panels: **Get started** , **Define & test source**, **Configure source** , **Define destination** , **Configure destination** , and **Review & create**. Information on how to populate each panel is provided in the various sections of this page.

### Define settings for the stream

  1. Go to the **Streams** page for Datastream in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click **CREATE STREAM**.

  3. Supply the following information in the **Define stream details** panel of the **Create stream** page:

     * Enter `My Stream` as the **Stream name**.
     * Keep the auto-generated **Stream ID**.
     * From the **Region** menu, select the region where you created your source connection profile.
     * From the **Source type** menu, select the **PostgreSQL** profile type.
     * From the **Destination type** menu, select the **BigQuery** profile type.
  4. Review the required prerequisites that are generated automatically to reflect how your environment must be prepared for a stream. These prerequisites include how to configure the source database and how to configure BigQuery.

For more information about these prerequisites, see [Configure your source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).
  5. Click **CONTINUE**. The **Define PostgreSQL connection profile** panel of the **Create stream** page appears.




### Specify information about the source connection profile

  1. From the **Source connection profile** menu, select your source connection profile for PostgreSQL database.

  2. Click **RUN TEST** to verify that the source database and Datastream can communicate with each other.

If the test fails, then the issue associated with the connection profile appears. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. Make the necessary changes to correct the issue, and then retest.

  3. Click **CONTINUE**. The **Configure stream source** panel of the **Create stream** page appears.




### Configure information about the source database for the stream

  1. Provide the **Replication slot** and **Publication** names for your source database. The replication slot and publication were created when [configuring your PostgreSQL](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database) database.

  2. Use the **Objects to include** menu to specify the tables and schemas in your source database that Datastream will replicate into BigQuery. The menu only loads if your database has up to 5,000 objects.

For this quickstart, you want Datastream to transfer all tables and schemas. Therefore, select **All tables from all schemas** from the menu.

For this quickstart, make sure that the **Select objects to exclude** panel is set to "None.". You don't want to restrict Datastream from transferring any tables and schemas in your source database into BigQuery.

Also, make sure that the **Choose backfill mode for historical data** panel is set to "Automatic." Datastream will stream all existing data, in addition to changes to the data, from the source into the destination. 

  3. Click **CONTINUE**. The **Define BigQuery connection profile** panel of the **Create stream** page appears.




### Select a destination connection profile

  1. From the **Destination connection profile** menu, select your destination connection profile for BigQuery.

  2. Click **CONTINUE**. The **Configure stream destination** panel of the **Create stream** page appears.




### Configure information about the destination for the stream

  1. Choose the **Dataset for each schema** option, so that Datastream automatically creates a dataset in BigQuery for every schema in the source database.

  2. Select the **Location type** where the datasets will be created in BigQuery. Although this location doesn't have to be the same as the region where the Datastream stream is created, we recommend to keep all resources, as well as datasets, in the same region for cost and performance optimization.

  3. Set the **Prefix** to `quickstart-`. Datastream will add this string to the beginning of every dataset that it creates in BigQuery.

  4. Leave the value in the **Stream write mode** set to **Merge**. This way, the tables in BigQuery stay synchronized with the source.

  5. Leave the value in the **Specify the limit of data staleness** drop-down list set to 15 minutes. BigQuery uses this value to decide how stale your data may be when queried.

  6. Click **CONTINUE**. The **Review stream details and create** panel of the **Create stream** page appears.




### Create the stream

  1. Verify details about the stream as well as the source and destination connection profiles that the stream will use to transfer data from a source PostgreSQL database to BigQuery.

  2. Click **RUN VALIDATION** to validate the stream. By validating a stream, Datastream checks that the source is configured properly, validates that the stream can connect to both the source and the destination, and verifies the end-to-end configuration of the stream.

If a validation check passes, then a check mark icon appears to the left of the validation check. 

If a validation check doesn't pass, then an exclamation point icon appears to the left of the check, and a **SEE ERROR DETAILS** button appears below the check. Click the button, and a dialog appears, explaining why the check didn't pass and information about what to do to rectify the problem. After making the appropriate corrections, click **REVALIDATE**.

For more information about troubleshooting validation checks that don't pass, see [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues).

  3. After all validation checks pass, click **CREATE**.

  4. In the **Create stream?** dialog, click **CREATE**.




## Start the stream

In the previous section of the quickstart, you created a stream, but you didn't start it. You can do this now.

For this quickstart, you create and start a stream separately in case the stream creation process incurs an increased load on your source database. To put off that load, you create the stream without starting it, and then start the stream when the load can be incurred.

By starting the stream, Datastream can transfer data, schemas, and tables from the source database to the destination.

  1. Go to the **Streams** page for Datastream in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Select the checkbox to the left of the stream that you want to start. For this quickstart, this is **My Stream**.

  3. Click **START**.

  4. In the dialog, click **START**. The status of the stream changes from `Not started` to `Starting` to `Running`.

It takes about 30 seconds for background resources to start before the stream status changes to `Running`.

After starting a stream, you can verify that Datastream transferred data from the source database to the destination.




## Verify the stream

In this section, you confirm that Datastream transfers the data from all tables of your source PostgreSQL database into BigQuery.

  1. Go to the **Streams** page for Datastream in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you created. For this quickstart, this is **My Stream**.

  3. In the **Stream details** page, click the link that appears below the **Destination write path** field. BigQuery Studio opens in a separate tab.

  4. Verify that you see datasets and tables that represent schemas and tables of your source PostgreSQL database.

  5. Click one of the tables to see a preview of your data.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Use the Google Cloud console to delete your project, Datastream stream and connection profiles, and BigQuery datasets.



By cleaning up the resources that you created on Datastream, they won't take up quota and you won't be billed for them in the future. The following sections describe how to delete or turn off these resources.

### Delete your project

The easiest way to eliminate billing is to delete the project that you created for this quickstart.

Deleting a project has the following effects:

  * **Everything in the project is deleted.** If you used an existing project for this quickstart, then when you delete it, you also delete any other work you've done in the project.
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as `**appspot.com**`, delete selected resources inside the project instead of deleting the whole project.



If you plan to explore multiple tutorials and quickstarts, then reusing projects can help you avoid exceeding project quota limits.

  1. In the the Google Cloud console, go to the **Manage resources** page.

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

  2. Select the checkbox for each connection profile that you want to delete. For this quickstart, select the checkboxes for **My Source Connection Profile** and **My Destination Connection Profile**.

  3. Click **DELETE**.

  4. In the dialog, click **DELETE**.




### Delete your BigQuery datasets

  1. Go to the **BigQuery Studio** page in the Google Cloud Console.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

  2. Expand the project node where you created this quickstart.

  3. For each dataset that you want to delete, click the **View actions** menu and then click **Delete**.

  4. In the dialog, enter `delete` in the text field, and then click **DELETE**.




## What's next

  * Learn more about [Datastream](https://docs.cloud.google.com/datastream/docs).
  * Try out other Google Cloud features for yourself. Have a look at our [quickstarts](https://cloud.google.com/docs/tutorials).
  * Learn how to [work with change data capture tables in BigQuery](https://docs.cloud.google.com/bigquery/docs/change-data-capture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
