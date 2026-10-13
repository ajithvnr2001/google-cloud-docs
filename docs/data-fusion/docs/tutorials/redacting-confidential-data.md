---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/redacting-confidential-data/
title: Redact confidential data \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:55.016994+00:00
---

# Redact confidential data  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/redacting-confidential-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Redact confidential data Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use the Cloud Data Fusion [plugin](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#plugin) for [Cloud DLP](https://docs.cloud.google.com/sensitive-data-protection/docs) to redact sensitive data.

## Scenario

Consider the following scenario, in which some sensitive customer information must be redacted:

Your support team documents the details of each support case they handle in a support ticket. All of the information in the support ticket is pulled into a CSV file. The support technicians are not supposed to document any customer information that's considered sensitive, but sometimes they mistakenly do so. You notice that in the CSV file some customers' phone numbers appear.

You want to go through the CSV file and hide all phone numbers. You create a Cloud Data Fusion pipeline that redacts the sensitive customer data by using the Cloud DLP plugin.

In this tutorial, you create a pipeline that does the following:

  * Redacts customer phone numbers by masking them with the `#` character.
  * Stores the masked sensitive data and the non-sensitive data in a Cloud Storage bucket.



## Objectives

  * Connect Cloud Data Fusion to a Cloud Storage source.
  * Deploy the Cloud DLP plugin.
  * Create a custom Cloud DLP template.
  * Use the Redact transform plugin to mask sensitive customer data.
  * Write the output data to Cloud Storage.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Cloud DLP](https://docs.cloud.google.com/sensitive-data-protection/pricing)



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

  6. Enable the Cloud Data Fusion, BigQuery, Cloud Storage, and Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,dataproc.googleapis.com)

  7. [ Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance). 



### Get Cloud DLP permissions

  1. In the Google Cloud console, go to the IAM page. 

[ Open the IAM page](https://console.cloud.google.com/project/_/iam-admin/iam)

  2. In the permissions table, in the **Principal** column, find the service account that matches the format `service-project-number@gcp-sa-datafusion.iam.gserviceaccount.com`. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/service-account.png)

  3. Click _edit_ **Edit**.

  4. Click **Add Another Role**.

  5. Use the search bar to search and then select **DLP Administrator**. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/add-role.png)

  6. Click **Save**.

  7. Check that **DLP Administrator** appears in the **Role** column.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/role-added.png)



### Navigate to the Cloud Data Fusion UI

When using Cloud Data Fusion, you use both the Google Cloud console and the separate Cloud Data Fusion UI. In the Google Cloud console, you can create a Google Cloud console project and create and delete Cloud Data Fusion instances. In the Cloud Data Fusion UI, you can use the various pages, such as **Studio** or **Wrangler** , to use Cloud Data Fusion features.

  1. In the Google Cloud console, open the **Instances** page. 

[Open the Instances page](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the **Actions** column for the instance, click the **View Instance** link. The Cloud Data Fusion UI opens in a new browser tab.




## Create the pipeline

Create a pipeline that redacts sensitive customer data. The pipeline you build does the following:

  * Reads the input data using the Cloud Storage source plugin.
  * Deploys the Cloud DLP plugin from the Hub.
  * Writes the output data using a Cloud Storage sink plugin.



### Load the customer data

This tutorial uses the input dataset, `CallCenterRecords.csv`, provided in a publicly available Cloud Storage bucket.

**Note:** To use the `CallCenterRecords.csv` dataset, you must load the data using the Cloud Data Fusion **Studio** page. If you have your own dataset in your own Cloud Storage bucket, you can load the data using either **Studio** or **Wrangler**.

  1. Open your Cloud Data Fusion instance and click _menu_ **Menu > Studio**.

  2. In the **Source** menu, click the **Cloud Storage** plugin.

![Select the plugin.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/click-gcs-source.png)

  3. On the **Cloud Storage** node, click **Properties**.

  4. In the **Reference name** field, enter a name.

  5. In the **Path** field, enter `gs://datafusion-sample-datasets/CallCenterRecords.csv`.

  6. In the **Format** field, select `CSV`.

  7. For the **Output Schema** , delete the **offset** and **body** fields. Click  add  **Add** and enter the following fields:

     * Date
     * Bank
     * State
     * Zip
     * Notes
**Note:** All data types must be set to **string**.

![Enter source properties.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/gcs-source-properties.png)

  8. Click **Validate** to check for errors.

  9. Click close **Close**.




### Redact sensitive data

The Cloud DLP Redact plugin identifies sensitive records in your input stream of data and applies transformations that you define to those records. A record of data is considered sensitive if it matches predefined Cloud DLP filters you choose or a custom template you define.

In this tutorial, you want to redact customer phone numbers that some support technicians on your team accidentally took note of. They entered the sensitive information in the **Notes** section of the support tickets, which appears as the **Notes** column in the CSV file. You create a custom Cloud DLP template, and then provide the template ID in the properties menu of the plugin.

#### Deploy the Cloud DLP plugin

  1. In your Cloud Data Fusion instance, click **Hub**.

  2. Click the **Cloud DLP** plugin.

  3. Click **Deploy**.

  4. Click **Finish**.

  5. Click close **Close** to exit the Cloud DLP dialog.

  6. Click close **Close** to exit the Hub.




#### Create a custom template

  1. In the Google Cloud console, go to the Cloud DLP page.

[Go to Cloud DLP](https://console.cloud.google.com/security/dlp)

  2. From the **Create** menu, choose **Template**. ![image](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/create-template.png)

  3. In the **Template ID** field, enter an ID for your template.

  4. Click **Continue**.

  5. In the **Configure detection** field, click **Manage infotypes**.

  6. In the **Built-in** tab, use the filter to search for "phone number".

![Filter.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/phone-number-only.png)

  7. Select **PHONE_NUMBER**.

  8. Click **Done > Create**.




Learn more about [ creating Cloud DLP templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect). 

#### Apply the Cloud DLP Redact transformation

  1. Go to the Cloud Data Fusion **Studio** page and click to expand the **Transform** menu.

  2. Click the Cloud DLP **Redact** plugin.

![Click the plugin to add it to your pipeline.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/pii-filter-transform.png)

  3. Drag a connection arrow from the **Cloud Storage** node to the **Redact** node.

![Connect the two nodes.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/gcs-to-redact.png)

  4. Hold the pointer over the **Redact** node and click **Properties**.

     1. Set **Custom Template** to `Yes`.

     2. In the **Template ID** field, enter the template ID of the custom template you created.

     3. In the **Matching** field , apply **Masking** on **Custom template** within **Notes**.

**Note:** In addition to masking, there are other Cloud DLP transformations available in the plugin. To learn more, see the **Documentation** tab in the properties menu of the Redact plugin.
     4. In the **Masking Character** field, enter `#`.

![Mask.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/redact-properties.png)

     5. Click **Validate** to check for errors.

     6. Click close **Close**.




### Store the output data

Store the results of your pipeline in a Cloud Storage file.

  1. From the **Studio** page, click to expand the **Sink** menu.

  2. Click **Cloud Storage**.

  3. Drag a connection arrow from the **Redact** node to the **Cloud Storage2** node.

![Connect the Redact node to the second Cloud Storage node.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/redact-to-gcs2.png)

  4. Hold the pointer over the **Cloud Storage2** node and click **Properties**.

     1. In the **Reference name** field, enter a name.

     2. In the **Path** field, enter the path of a Cloud Storage bucket where you'd like to store the pipeline results. Cloud Data Fusion creates the bucket for you. Be sure to follow the [bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming).

     3. In the **Format** field, select **CSV**.

     4. Click **Validate** to ensure that there are no errors.

     5. Click close **Close**.




## Run the pipeline in preview mode

Run the pipeline in preview mode before you deploy it.

  1. Click **Preview** , and then click **Run**.

![Run the pipeline.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/preview-run.png)

Clicking **Run** displays the pipeline status, which starts with **Starting** , then turns to **Stop** , and then to **Run**.

  2. When the preview run completes, on the **Redact** node, click **Preview Data** to see a side-by-side comparison of the input and output data. Check that phone numbers have been masked with the `#` character.

![Check that the phone numbers are masked.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/preview-mode-results.png)




## Redact another data type

While examining the preview run results, you notice that there's still sensitive information that appears in the **Notes** column: email addresses. You go back and edit the Cloud DLP template to redact email addresses as well.

  1. In the Google Cloud console, go to the Cloud DLP page.

[Open the Cloud DLP page](https://console.cloud.google.com/security/dlp)

  2. On the **Configuration** tab, select your template.

  3. Click **Edit**.

  4. Click **Manage infotypes**.

  5. In the **Built-in** tab, use the filter to search for "OR" "email address".

![Filter.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/phone-number-or-email.png)

  6. Select all and click **Done**.

  7. Click **Save**.

  8. Once again, run your pipeline in preview mode. Cloud Data Fusion will automatically use the updated Cloud DLP template.

  9. Check that both phone numbers _and_ email addresses have been masked with the `#` character.

![Check that data is masked.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/preview-mode-results-with-email.png)




## Deploy and run the pipeline

  1. Make sure **Preview** mode is unchecked.

  2. Click **Save**. Clicking **Save** prompts you to name your pipeline. Then, click **OK**.

  3. Click **Deploy**.

  4. When deployment completes, click **Run**. Running your pipeline can take a few minutes. While you wait, you can observe the **Status** of the pipeline transition from **Provisioning** to **Starting** to **Running** to **Deprovisioning** to **Succeeded**.




### View the results

  1. In the Google Cloud console, go to the Cloud Storage page.

[Go to Cloud Storage](https://console.cloud.google.com/storage)

  2. In the **Storage browser** , navigate to the sink Cloud Storage bucket you specified in the sink Cloud Storage plugin properties.

  3. In **Link URL** , click the link to download the CSV file with the results. Check that the phone numbers and email addresses have been masked with the `#` character.

![Check that data is masked.](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/redact-pipeline/gcs-results.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the Cloud Data Fusion instance

Follow these instructions to [ delete your Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).

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



## What's next

  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview).
  * See how to [use the Cloud Data Fusion plugin](https://docs.cloud.google.com/data-fusion/docs/how-to), which provides the Redact and Filter PII transform plugins.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
