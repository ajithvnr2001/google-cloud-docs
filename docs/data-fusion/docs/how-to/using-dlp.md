---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/using-dlp/
title: Use Sensitive Data Protection with Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:41.877647+00:00
---

# Use Sensitive Data Protection with Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/using-dlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Use Sensitive Data Protection with Cloud Data Fusion Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to use [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection) with Cloud Data Fusion.

Cloud Data Fusion provides a Sensitive Data Protection [plugin](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#plugin) that provides three transforms that can filter, redact, or decrypt your sensitive data:

  * The PII Filter transform lets you _filter_ sensitive records from an input stream of data.

  * The Redact transform lets you _transform_ sensitive data, such as masking the data or encrypting it.

  * The Decrypt transform lets you _decrypt_ sensitive data that was previously encrypted using the Redact transform,


**Note:** The Sensitive Data Protection plugin available in Cloud Data Fusion is based on the Cloud Data Loss Prevention API and therefore complies with the Sensitive Data Protection [quotas and usage limits](https://docs.cloud.google.com/sensitive-data-protection/limits).

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/pricing)
  * [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. In the Google Cloud console, go to the project selector page and select or create a project.

[ Go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Cloud Data Fusion API for your project. 

[ Enable the Cloud Data Fusion API](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com)

  3. Enable the DLP API (part of Sensitive Data Protection) for your project. 

[ Enable the DLP API](https://console.cloud.google.com/marketplace/details/google/dlp.googleapis.com)

  4. [Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).

**Note:** The Sensitive Data Protection plugin is available for instances using Cloud Data Fusion version 6.1.1 or higher.



## Grant Sensitive Data Protection permissions

  1. In the Google Cloud console, go to the IAM page. 

[ Go to IAM](https://console.cloud.google.com/project/_/iam-admin/iam)

  2. In the permissions table, select one of the following service accounts in the **Principal** column:

     1. For permission to resources at runtime, select the service account that your Managed Service for Apache Spark cluster uses. The default is the Compute Engine service account, which is not recommended for security reasons

     2. For permission to resources when using Wrangler or Preview in Cloud Data Fusion (not at runtime), instead select the service account that matches the format: `service-project-number@gcp-sa-datafusion.iam.gserviceaccount.com`.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/service-account.png)
  3. Click the pencil icon to the right of the service account.

  4. Click **Add Another Role**.

  5. Click the dropdown that appears.

  6. Use the search bar to search and then select **DLP Administrator**. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/add-role.png)

  7. Click **Save**. Check that **DLP Administrator** appears in the **Role** column.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/role-added.png)



## Deploy the Sensitive Data Protection plugin

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the Cloud Data Fusion web UI, click **Hub** in the upper right.

  3. Click the **Data Loss Prevention** plugin.

  4. Click **Deploy**.

  5. Click **Finish**.

  6. Click **Create a pipeline**. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/upload-plugin-success.png)




## Use the PII Filter transform

This transform separates sensitive records from non-sensitive records. A record is considered sensitive if it matches criteria that you define in a Sensitive Data Protection template. For example, when you create your template, you can define sensitive data to be credit card information or Social Security numbers.

  1. [Create a Sensitive Data Protection inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect).

  2. Open your pipeline in Cloud Data Fusion and click **Studio** > **Transform**.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/pii-filter-transform.png)
  3. Click the **PII Filter** transform.

  4. Hold the pointer over the **PII Filter** node and click **Properties**.

  5. Under **Filter on** , choose whether you want to filter records or fields.

In compliance with [Sensitive Data Protection limits](https://docs.cloud.google.com/sensitive-data-protection/limits#content_limits), if a record exceeds 0.5 MB, your Cloud Data Fusion pipeline will fail. To avoid such a failure, filter by field instead of record.

  6. Under **Template ID** , enter the template ID of the Sensitive Data Protection template you created.

  7. Under **Error Handling** , define how to proceed when your pipeline encounters sensitive data. Choose one of the following error handling options:

     * **Stop pipeline** : Stops the pipeline as soon as an error is encountered.
     * **Skip record** : Skips the record that caused the error. The pipeline continues to run, and no error is reported.
     * **Send to error** : Sends errors to the error port. The pipeline continues to run.
  8. Click the **X** button.




## Use the Redact transform

This transform identifies sensitive records in the input stream and applies transformations that you define to those records. A record is considered sensitive if it matches predefined Sensitive Data Protection filters you chose or a custom template you defined.

  1. In the **Studio** page of the Cloud Data Fusion web UI, click to expand the **Transform** menu.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/pii-filter-transform.png)
  2. Click the **Redact** transform.

  3. Hold the pointer over the **Redact** node and click **Properties**.

  4. Choose if you want to apply transformations to predefined filters or if you'd like to create your own.

You cannot combine these two options. You can either use predefined filters OR create a custom template.

### Predefined filters

To apply transformations to predefined filters, leave the **Custom Template** set to **No** , and under **Matching** , define a rule:

     1. Following **Apply** , click the dropdown and choose a transformation. Learn more about the available transformations in the **Description** section of the plugin's **Documentation** tab.

     2. Following **on** , click the dropdown and choose a category, which is a set of predefined Sensitive Data Protection filters grouped together by type. For the full list of provided categories and what filters they contain, see the **DLP Filter Mapping** section in the plugin's **Documentation** tab.

To set multiple matching rules, click the **+** button.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/pre-defined-filters.png)

### Custom template

To apply transformations according to a custom template, set the **Custom Template** to **Yes**.

     1. [Create a custom Sensitive Data Protection template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect).

     2. Back in the Cloud Data Fusion web UI, in the Redact properties menu, under **Template ID** , enter the template ID of the custom template you created.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/custom-template.png)

  5. Click the **X** button.




## Use the Decrypt transform

This transform identifies records that were encrypted using Sensitive Data Protection in the input stream and applies decryption. Only records that were encrypted using a reversible algorithm such as _Format Preserving Encryption_ or _Deterministic Encryption_ can be decrypted.

  1. In the **Studio** page of the Cloud Data Fusion web UI, click to expand the **Transform** menu.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/pii-filter-transform.png)
  2. Click the **Decrypt** transform.

  3. Hold the pointer over the **Decrypt** node and click **Properties**.

  4. Enter the same values that were used to configure the **Redact** plugin that encrypted this data. The properties for this plugin are identical to the **Redact** plugin.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/using-dlp/decrypt-transform-properties.png)
  5. Click the **X** button.




## What's next

  * Follow a [tutorial to redact sensitive user data](https://docs.cloud.google.com/data-fusion/docs/tutorials/redacting-confidential-data).
  * Read more about [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
