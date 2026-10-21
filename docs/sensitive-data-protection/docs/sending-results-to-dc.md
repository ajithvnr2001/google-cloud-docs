---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-dc/
title: Send Sensitive Data Protection inspection results to Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:35:18.225899+00:00
---

# Send Sensitive Data Protection inspection results to Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-dc/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Send Sensitive Data Protection inspection results to Data Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** On or after September 30, 2025, you can no longer send inspection results from Sensitive Data Protection to Data Catalog. Data Catalog is deprecated and is discontinuing on June 1, 2026.

We recommend that you send the inspection findings to Knowledge Catalog instead. For more information, see [Send inspection results to Knowledge Catalog as aspects](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job). To migrate existing job triggers to the new action, see [Migrate to the Publish to Dataplex Universal Catalog action](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job#migrate-dataplex-catalog).

Tags and tag templates that Sensitive Data Protection created for you are available in Knowledge Catalog as _aspects_. For instructions on how to transition your Data Catalog content to Knowledge Catalog, see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog) in the Knowledge Catalog documentation.

This guide shows you how to use Sensitive Data Protection to inspect a BigQuery table and to send the inspection results to Data Catalog.

You can additionally perform [data profiling](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles), which is different from an inspection operation. You can also send data profiles to Knowledge Catalog. For more information, see [Tag tables in Knowledge Catalog based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-dataplex).

[Data Catalog](https://docs.cloud.google.com/data-catalog) is a scalable metadata management service that empowers you to quickly discover, manage, and understand all your data in Google Cloud.

Sensitive Data Protection has built-in integration with Data Catalog. When you use a Sensitive Data Protection [action](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) to inspect your BigQuery tables for sensitive data, it can send results directly to Data Catalog in the form of a tag template.

By completing the steps in this guide, you'll do the following:

  * Enable Data Catalog and Sensitive Data Protection.
  * Set up Sensitive Data Protection to inspect a BigQuery table.
  * Configure a Sensitive Data Protection inspection to send inspection results to Data Catalog.



For more information about Data Catalog, see the [Data Catalog documentation](https://docs.cloud.google.com/data-catalog/docs).

If you want to send the results of data profiling operations—not inspection jobs—to Knowledge Catalog, see the documentation for [profiling an organization, folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder), or [project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project) instead.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * Sensitive Data Protection
  * BigQuery



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Before you can send Sensitive Data Protection inspection results to Data Catalog, do the following:

  * Step 1: Set up billing.
  * Step 2: Create a new project and populate a new BigQuery table. (Optional.)
  * Step 3: Enable Data Catalog.
  * Step 4: Enable Sensitive Data Protection.



The following subsections cover each step in detail.

### Step 1: Set up billing

You must first set up a billing account if you don't already have one. 

[Learn how to enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

### Step 2: Create a new project and populate a new BigQuery table (Optional)

If you are setting up this feature for production work or already have a BigQuery table that you want to inspect, open the Google Cloud project that contains the table and skip to Step 3.

If you are trying out this feature and want to inspect test data, create a new project. To complete this step, you must have the IAM **Project Creator** role. Learn more about [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

  1. Go to the [New Project](https://console.cloud.google.com/projectcreate) page in the Google Cloud console. 

[New Project](https://console.cloud.google.com/projectcreate)

  2. On the **Billing account** drop-down list, select the billing account that the project should be billed to.
  3. On the **Organization** drop-down list, select the organization that you want to create the project in.
  4. On the **Location** drop-down list, select the organization or folder that you want to create the project in.
  5. Click **Create** to create the project.



Next, download and store the sample data:

  1. Go to the [Cloud Run functions tutorials repository on GitHub](https://github.com/GoogleCloudPlatform/dlp-cloud-functions-tutorials/tree/master/sample_data).
  2. Select one of the CSV files that has example data, and then download the file.
  3. Next, go to [BigQuery](https://console.cloud.google.com/bigquery/) in the Google Cloud console.
  4. Select your project.
  5. Click **Create Dataset**.
  6. Click **Create Table**.
  7. Click **Upload** , and then select the file you want to upload.
  8. Give the table a name, and then click **Create Table**.



### Step 3: Enable Data Catalog

Next, enable Data Catalog for the project that contains the BigQuery table you want to inspect using Sensitive Data Protection.

To enable Data Catalog using the Google Cloud console:

  1. [Register your application for Data Catalog](https://console.cloud.google.com/apis/enableflow?apiid=datacatalog.googleapis.com). 

[Register your application for Data Catalog](https://console.cloud.google.com/apis/enableflow?apiid=datacatalog.googleapis.com)

  2. On the registration page, from the **Create a project** drop-down list, select the project you want to use with Data Catalog.
  3. After you've selected the project, click **Continue**.



Data Catalog is now enabled for your project.

### Step 4: Enable Sensitive Data Protection

Enable Sensitive Data Protection for the same project you enabled Data Catalog for.

To enable Sensitive Data Protection using the Google Cloud console:

  1. [Register your application for Sensitive Data Protection](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com). 

[Register your application for Sensitive Data Protection](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)

  2. On the registration page, from the **Create a project** drop-down list, select the same project you chose in the previous step.
  3. After you've selected the project, click **Continue**.



Sensitive Data Protection is now enabled for your project.

## Configure and run a Sensitive Data Protection inspection job

You can configure and run a Sensitive Data Protection inspection job using either the Google Cloud console or the DLP API.

Data Catalog tag templates are stored in the same project and region as the BigQuery table. If you are inspecting a table from another project, then you must grant the Data Catalog TagTemplate Owner (`roles/datacatalog.tagTemplateOwner`) role to the Sensitive Data Protection service agent in the project where the BigQuery table exists.

###  Google Cloud console 

To set up an inspection job of a BigQuery table using Sensitive Data Protection:

  1. In the Sensitive Data Protection section of the Google Cloud console, go to the **Create job or job trigger** page.

[Go to Create job or job trigger](https://console.cloud.google.com/security/sensitive-data-protection/create/job;source=7)

  2. Enter the Sensitive Data Protection job information and click **Continue** to complete each step:

     * For **Step 1: Choose input data** , name the job by entering a value in the **Name** field. In **Location** , choose **BigQuery** from the **Storage type** menu, and then enter the information for the table to be inspected. The **Sampling** section is pre-configured to run a sample inspection against your data. You can adjust the **Limit rows by** and **Maximum number of rows** fields to save resources if you have a large amount of data. For more details, see [Choose input data](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#choose-input-data).

     * (Optional) In **Step 2: Configure detection** , you configure what types of data to look for, called "[infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes)." For the purposes of this walkthrough, keep the default infoTypes selected. For more details, see [Configure detection](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#configure-detection).

     * For **Step 3: Add actions** , enable **Save to Data Catalog**.

     * (Optional) For **Step 4: Schedule** , for the purposes of this walkthrough, leave the menu set to **None** so that the inspection runs just once. To learn more about scheduling repeating inspection jobs, see [Schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#schedule-job).

  3. Click **Create**. The job runs immediately.




### DLP API

In this section, you configure and run a Sensitive Data Protection inspection job.

**Note:** These instructions use [APIs Explorer](https://developers.google.com/apis-explorer) to send requests that contain JSON to Sensitive Data Protection. This is for learning, demonstration, and experimentation purposes only, and you should never use APIs Explorer for production work. You can use `gcloud`, `curl`, or `httplib2` to send these requests instead. You can also use one of the available Sensitive Data Protection [client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries) to access the API using Java, Python, Go, and more.

The _inspection job_ that you configure here instructs Sensitive Data Protection to inspect either the sample BigQuery data described in Step 2 above or your own BigQuery data. The job configuration that you specify is also where you instruct Sensitive Data Protection to save its inspection results to Data Catalog.

**Step 1: Note your project identifier**

  1. Go to the [Google Cloud console](https://console.cloud.google.com/projectselector2/home/dashboard/).

[Go to the Google Cloud console](https://console.cloud.google.com/projectselector2/home/dashboard/)

  2. Click **Select**.

  3. On the **Select from** drop-down list, select the organization for which you enabled Data Catalog.

  4. Under **ID** , copy the project ID for the project that contains the data you want to inspect. This is the project described in the set storage repositories step earlier on this page.

  5. Under **Name** , click the project to select it.




**Step 2: Open APIs Explorer and configure the job**

  1. Go to APIs Explorer on the reference page for the `dlpJobs.create` method. To keep these instructions available, right-click the following link and open it in a new tab or window:

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/create?apix=true)

  2. In the **parent** box, enter the following, where project-id is the project ID you noted earlier in the previous step: 
         
         projects/project-id

Next, copy the following JSON. Select the contents of the **Request body** field in APIs Explorer, and then paste the JSON to replace the contents. Be sure to replace the `project-id`, `bigquery-dataset-name`, and `bigquery-table-name` placeholders with the actual project ID and BigQuery dataset and table names, respectively.
         
         {
           "inspectJob":
           {
             "storageConfig":
             {
               "bigQueryOptions":
               {
                 "tableReference":
                 {
                   "projectId": "project-id",
                   "datasetId": "bigquery-dataset-name",
                   "tableId": "bigquery-table-name"
                 }
               }
             },
             "inspectConfig":
             {
               "infoTypes":
               [
                 {
                   "name": "EMAIL_ADDRESS"
                 },
                 {
                   "name": "PERSON_NAME"
                 },
                 {
                   "name": "US_SOCIAL_SECURITY_NUMBER"
                 },
                 {
                   "name": "PHONE_NUMBER"
                 }
               ],
               "includeQuote": true,
               "minLikelihood": "UNLIKELY",
               "limits":
               {
                 "maxFindingsPerRequest": 100
               }
             },
             "actions":
             [
               {
                 "publishFindingsToCloudDataCatalog": {}
               }
             ]
           }
         }
         




To learn more about the available inspection options, see [Inspecting storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage). For a full list of information types that Sensitive Data Protection can inspect for, see [InfoTypes reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

**Step 3: Execute the request to start the inspection job**

After you configure the job by following the preceding steps, click **Execute** to send the request. If the request is successful, a response appears with a success code and a JSON object that indicates the status of the Sensitive Data Protection job you just created.

**Important:** Keep the page open or copy the response JSON so that you have it for the remainder of the tasks in this topic.

The response to your inspection request includes the job ID of your inspection job as the `"name"` key, and the current state of the inspection job as the `"state"` key. Because you just submitted the request, the job's state at that moment is `"PENDING"`.

## Check the status of the Sensitive Data Protection inspection job

After you submit the inspection request, the inspection job begins immediately.

###  Google Cloud console 

To check the status of the inspection job:

  1. In the Google Cloud console, open Sensitive Data Protection.

[Go to Sensitive Data Protection](https://console.cloud.google.com/security/sensitive-data-protection;source=7)

  2. Click the **Jobs & job triggers** tab, and then click **All jobs**.




The job you just ran will likely be at the top of the list. Check the **State** column to be sure its status is **Done**.

You can click on the **Job ID** of the job to see its results. Each infoType detector listed on the Job details page is followed by the number of matches that were found in the content.

### DLP API

To check the status of the inspection job:

  1. Go to APIs Explorer on the reference page for the `dlpJobs.get` method by clicking the following button:

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/get?apix=true)

  2. In the **name** box, type the name of the job from the JSON response to the inspection request in the following form: 
         
         projects/project-id/dlpJobs/job-id

The job ID is in the form of `i-1234567890123456789`.
  3. To submit the request, click **Execute**.




If the response JSON object's `"state"` key indicates that the job is `"DONE"`, then the inspection job has finished.

**Note:** You can instruct Sensitive Data Protection to send you a notification when a job is done, but that's beyond the scope of this topic. To learn more, see the [Actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) conceptual page.

To view the rest of the response JSON, scroll down the page. Under `"result"` > `"infoTypeStats"`, each information type listed should have a corresponding `"count"`. If not, make sure that you entered the JSON accurately, and that the path or location to your data is correct.

After the inspection job is done, you can continue to the next section of this guide to view inspection results in Security Command Center.

## View Sensitive Data Protection inspection results in Data Catalog

Because you instructed Sensitive Data Protection to send its inspection job results to Data Catalog, you can now view the automatically created tags and tag template in the Data Catalog UI:

  1. Go to the Data Catalog page in the Google Cloud console.

[Go to Data Catalog](https://console.cloud.google.com/datacatalog/)

  2. Search for the table that you inspected.
  3. Click on the results that match your table to view the table's metadata.



The following screen shot shows the Data Catalog metadata view of an example table:

![Sensitive Data Protection findings in Data Catalog.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/sending-results-to-dc-findings.png)

### Inspection summary

Findings from Sensitive Data Protection are included in summary form for the table that you inspected. This summary includes total infoType counts, as well as summary data about the inspection job that includes dates and job resource ID.

Any `infoTypes` that were inspected for are listed. Those with findings show a count greater than zero.

## Cleaning up

To avoid incurring charges to your Google Cloud account for the resources used in this topic, do one of the following, depending on whether you used sample data or your own data:

  * Sample data: Delete the project you created.
  * Your own data: Delete the Sensitive Data Protection job you created.



### Deleting the project

The easiest way to eliminate billing is to delete the project you created while following the instructions provided in this topic.

To delete the project:

**Warning:** Deleting a project has the following consequences: 
     * If you used an existing project, you'll also delete any other work you've done in the project. 
     * You can't reuse the project ID of a deleted project. If you created a custom project ID that you plan to use in the future, delete the resources inside the project instead. This step ensures that URLs that use the project ID—for example, `project-id.region-id.r.appspot.com`— remain available. 

If you are exploring multiple how-to, tutorial, and quickstart topics, reusing projects instead of deleting them may prevent you from exceeding project quota values. 

  1. In the Google Cloud console, go to the Projects page. 

[Go to the Projects page](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project you want to delete and click **Delete project**. ![After selecting the checkbox next to the project name, click
    Delete project](https://docs.cloud.google.com/static/docs/images/delete-project-screenshot.png)
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



When you delete your project using this method, the Sensitive Data Protection job and Cloud Storage bucket you created are also deleted, and you're done. It's not necessary to follow the instructions in the following sections.

### Deleting the Sensitive Data Protection job or job trigger

If you inspected your own data, delete the inspection job or job trigger you just created.

###  Google Cloud console 

  1. In the Google Cloud console, open Sensitive Data Protection.

[Go to Sensitive Data Protection](https://console.cloud.google.com/security/sensitive-data-protection;source=7)

  2. Click the **Jobs & job triggers** tab, and then click the **Job triggers** tab.

  3. In the **Actions** column for the job trigger you want to delete, click the **more actions** menu (displayed as three dots arranged vertically) more_vert, and then click **Delete**.




Optionally, you can also delete the job details for the job that you ran. Click the **All jobs** tab, and then in the **Actions** column for the job you want to delete, click the **more actions** menu (displayed as three dots arranged vertically) more_vert, and then **Delete**.

### DLP API

  1. Go to APIs Explorer on the reference page for the `dlpJobs.delete` method by clicking the following button:

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/delete?apix=true)

  2. In the **name** box, type the name of the job from the JSON response to the inspection request, which has the following form: 
         
         projects/project-id/dlpJobs/job-id

The job ID is in the form of `i-1234567890123456789`.



If you created additional inspection jobs or if you want to make sure you've deleted the job successfully, you can list all of the existing jobs:

  1. Go to APIs Explorer on the reference page for the `dlpJobs.list` method by clicking the following button:

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/list?apix=true)

  2. In the **parent** box, type the project identifier in the following form, where project-id is your project identifier: 
         
         projects/project-id

  3. Click **Execute**.




If there are no jobs listed in the response, you've deleted all of the jobs. If jobs are listed in the response, repeat the deletion procedure above for those jobs.

## What's next

  * Learn more about the [`publishFindingsToCloudDataCatalog` action](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishFindingsToCloudDataCatalog) in Sensitive Data Protection.
  * Learn more about [creating custom tags or column-level tags in Data Catalog based on Sensitive Data Protection results](https://docs.cloud.google.com/community/tutorials/dlp-to-datacatalog-tags).
  * Learn more about [inspecting storage repositories for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) using Sensitive Data Protection.
  * Learn how to use [Data Catalog](https://docs.cloud.google.com/data-catalog/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
