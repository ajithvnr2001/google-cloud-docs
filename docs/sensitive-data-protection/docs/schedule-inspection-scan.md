---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/schedule-inspection-scan/
title: Quickstart: Schedule a Sensitive Data Protection inspection scan \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:36.769965+00:00
---

# Quickstart: Schedule a Sensitive Data Protection inspection scan  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/schedule-inspection-scan/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Schedule a Sensitive Data Protection inspection scan

Learn how to create a new job trigger using Sensitive Data Protection in the Google Cloud console.

Job triggers are events that automate running Sensitive Data Protection jobs to scan Google Cloud storage repositories (Cloud Storage, BigQuery, and Firestore in Datastore mode (Datastore)).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=dlp--quickstart-create-job-trigger)

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

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Sensitive Data Protection API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)




## Create a job trigger

In the following sections, you configure and create a job trigger for a [BigQuery public dataset](https://docs.cloud.google.com/bigquery/public-data) that contains the street addresses of bike share stations in a city.

When this job trigger runs, Sensitive Data Protection scans around 700 bytes of data. You can inspect up to 1 GB of storage data per month free of charge. For more information about pricing, see [Storage inspection job pricing](https://cloud.google.com/sensitive-data-protection/pricing#storage-pricing).

### Choose input data

  1. In the Sensitive Data Protection section of the Google Cloud console, go to the **Create job or job trigger** page.

[Go to Create job or job trigger](https://console.cloud.google.com/security/sensitive-data-protection/create/job;source=7)

  2. To configure input data, do the following:

     1. In the **Name** section, define the following options:

        * For **Job ID** , enter `quickstart-job-trigger`.

        * Keep **Resource location** set to **Global (any region)**.

     2. In the **Storage type** list, select **BigQuery** , and then define the following options:

        * For **Project ID** , enter `bigquery-public-data`.

        * For **Dataset ID** , enter `austin_bikeshare`.

        * For **Table ID** , enter `bikeshare_stations`.

     3. In the **Maximum number of rows** field, enter `10`.

  3. Click **Continue**.




### Configure detection parameters

  1. To configure detection, do the following:

     1. In the **InfoTypes** section, click **Manage infoTypes**.

     2. In the **InfoTypes** pane, select **STREET_ADDRESS**.

     3. To close the **infoTypes** pane, click **Done**.

     4. In the **Confidence threshold** section, select **Possible** from the **Likelihood** list.

The value **Possible** is sufficient for most purposes. If you routinely get matches that are too broad when you use this job trigger, select a higher confidence threshold value. If you get too few matches, select a lower confidence threshold value.

  2. Click **Continue**.




### Add post-scan actions

  1. Click the **Notify by email** toggle.

  2. Click **Continue**.




### Set a schedule

  1. In the **Time span or schedule** list, select **Create a trigger to run the job on a periodic schedule**.

**Important:** Selecting **Create a trigger to run the job on a periodic schedule** is what makes a job into a job trigger. If you don't specify a schedule, you create a single job that runs only once.
  2. In the **Trigger scan repeats** list, select **Weekly**.

  3. Click **Continue**.




### Review and create the job trigger

After you review the JSON-formatted summary of the job settings you just specified, do the following:

  1. Click **Create**.

  2. In the **Confirm job or job trigger create** dialog, click **Confirm create**.

Allow a minute for Sensitive Data Protection to create the job trigger.




## Run the job trigger and view results

To trigger a job immediately, do the following:

  1. On the **Trigger details** page, click **Run now**.

This operation might take some time to complete.

  2. After the job that you created runs once, do the following:

     1. In the **Triggered jobs** section, select the job ID of the triggered job in the **Job ID** column.

     2. On the **Job details** page, view the job results.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

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



### Delete the job trigger

If you created the job trigger in an existing project and you no longer need the job trigger, follow these steps:

  1. In the Google Cloud console, go to the Sensitive Data Protection page.

[Go to Sensitive Data Protection](https://console.cloud.google.com/security/sensitive-data-protection;source=7)

  2. If necessary, select the project in which you created a job trigger from the Google Cloud console toolbar.

  3. Click the **Inspection** tab, and then click the **Job triggers** tab. The Google Cloud console displays a list of all the job triggers for the current project.

  4. In the **Actions** column for the job trigger you want to delete, click the trigger actions menu (more_vert), click **Delete** , and then click **Confirm**.




## What's next

  * Learn more about [creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers).

  * Learn more about [creating Sensitive Data Protection inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect).

  * To add actions you want Sensitive Data Protection to take after a trigger job completes, see [Add actions](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#add-actions).

  * To specify the types of sensitive data you want to scan for, see [Configure detection](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#configure-detection).

  * To create a BigQuery dataset in a project, see [Creating datasets](https://docs.cloud.google.com/bigquery/docs/datasets).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
