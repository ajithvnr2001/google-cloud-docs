---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/manage-infotypes-console/
title: Manage infoTypes through the Google Cloud console \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:59.128777+00:00
---

# Manage infoTypes through the Google Cloud console  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/manage-infotypes-console/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Manage infoTypes through the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add and edit infoTypes in your inspection configuration through the Google Cloud console.

When you use Sensitive Data Protection to [inspect](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) or [profile](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) data, you use an inspection configuration to specify the information types ([_infoTypes_](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes)) that you want to scan for. The following Sensitive Data Protection operations in the Google Cloud console let you set your inspection configuration:

  * [Creating or editing an inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect)
  * [Creating an inspection job or job trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)
  * [Creating a discovery scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder)
  * [Creating or updating a content policy](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies)



These operations in the Google Cloud console have an **InfoTypes** section, where you can select infoTypes, edit the settings of built-in infoTypes, and add custom infoTypes. The step that contains the **InfoTypes** section differs depending on the operation that you're performing. The following table shows the relevant workflow step for each operation.

Operation | Relevant step  
---|---  
Creating an inspection template | Configure detection  
Creating an inspection job or job trigger | Configure detection  
Creating a discovery scan configuration | Select inspection template  
Creating a content policy | Inspection configuration  
  
## Select built-in infoTypes

  1. In the **InfoTypes** section, click **Manage infoTypes**.
  2. To narrow the selection of infoTypes, apply filters in the **Filter** field. Select a property name to filter on and enter a property value. For example, to filter for all infoTypes related to Australia, set the property name to **Location**. For the property value, select or type **Australia**.

If you know the infoType name, you can also type it directly in the **Filter** field.

  3. To view all category tags for an infoType, click  expand_more **Toggle full cell content** for that infoType.

  4. To hide or unhide columns, click view_column  **Column display options** , and select the names of the columns that you want to display.

  5. Select the infoTypes that you want to include in your inspection configuration.

**Tip:** If your scan results don't need to show the specific infoTypes that were detected, then consider selecting general infoTypes in your configuration. When you select a specific infoType covered by a general infoType, Sensitive Data Protection suggests the general infoType that you can use instead. To accept the recommended replacements, click **Apply recommendations**. For information about the benefits of using general infoTypes, see [General and specific infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes#general-specific-infotypes).
  6. To use [limited-availability infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#limited-availability-infotypes) in your configuration, select **Allow limited-availability infoTypes**. These infoTypes are supported only in specific regions; using them elsewhere can cause scanning errors.

  7. Click **Done**.




## Edit the settings of a built-in infoType

As you set the infoTypes that you want to include in your inspection configuration, you can additionally edit the settings of one or more of those infoTypes. You can edit the sensitivity level and, for some infoTypes, the infoType version.

  1. Select the built-in infoTypes that you want to include in your inspection configuration, including the infoTypes that you don't need to edit. Don't click **Done**.
  2. Click **Edit selected infoTypes**.

[ ![The Edit selected infoTypes button in the console.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/edit-selected-infotypes.png)](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/edit-selected-infotypes_2x.png)
  3. For each infoType that you want to edit, use the drop-down lists to select a sensitivity level or a detector version.

  4. Click **Confirm**.

  5. Click **Done**.




## Add custom infoTypes

This section describes how to add a custom infoType based on an underlying set of data. The underlying data can be any of the following:

  * A list of words or phrases that you provide inline in the inspection configuration.
  * A list of words or phrases that you store in a text file in Cloud Storage.
  * A large list of words or phrases that you store in a large text file in Cloud Storage or a column in BigQuery.

For this type, you must first [create a stored infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes#create) that points to the large custom dictionary, before performing this task.

  * A regular expression that you provide inline in the inspection configuration.




Whether you can reuse the new custom infoType depends on which operation you were performing when you created the custom infoType:

  * If you create a custom infoType while creating an inspection job or job trigger, the custom infoType is available to only that job or job trigger.

  * If you create a custom infoType while creating an inspection template, the custom infoType is available to any operation that uses the inspection template.

  * If you create a custom infoType while configuring profiling, Sensitive Data Protection creates a new inspection template from your inspection configuration. The custom infoType is available to any operation that uses that new inspection template.




For more information about custom infoTypes, see [Custom infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes).

To add a custom infoType detector, do the following:

  1. In the **InfoTypes** section, click **Manage infoTypes**.
  2. On the **Custom** tab, click **Add custom infoType**.
  3. For **Type** , select the type of custom infoType detector that you want to create:

     * **Words or phrases:** Matches on one or more words or phrases that you enter into the field. You can enter up to 128 KB of data, which equates to thousands of entries.

When you select this type, the **List of words or phrases** field appears. Enter the word or phrase that you want Sensitive Data Protection to match on. To match on multiple words or phrases, press `Enter` after each entry. For more information, see [Creating a regular custom dictionary detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary).

     * **Dictionary path:** Matches on words or phrases that you store in a text file in Cloud Storage. Use this custom infoType when you have hundreds of thousands of words or phrases to search for. This approach is also helpful if your list contains sensitive terms that you prefer not to store inline in the inspection configuration.

When you select this type, the **Dictionary location** field appears. Enter or browse to the Cloud Storage path where the dictionary file is stored. For more information, see [Creating a regular custom dictionary detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary).

     * **Regex:** Matches content based on a regular expression.

When you select this type, the **Regex** field appears. Enter a regular expression pattern to match words and phrases. For more information, see the [supported regular expression syntax](https://github.com/google/re2/wiki/Syntax).

     * **Stored infoType:** Matches on words or phrases that you store in a large text file in Cloud Storage or a single column in BigQuery.

This option adds a large custom dictionary detector. Use this custom infoType if you have millions of words or phrases to search for.

For this type, you must have already [created a stored infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes#create) that points to the underlying large custom dictionary.

When you select this type, the **Stored infoType name** field appears. Enter the full resource name of the stored infoType.

     * **Metadata KeyValue expression:** Matches key-value pairs within metadata in files.

When you select this type, the **Key Pattern** and **Value Pattern** fields appear. Enter the regular expression patterns to match the key and value of the metadata to detect. For more information, see [Create a custom metadata label detector](https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels).

     * **File label:** Matches Google Drive labels or Microsoft sensitivity labels that are applied to files.

When you select this type, the **File label type** field appears. Depending on the label type that you select, enter one of the following:

       * For Google Drive labels, enter the label ID. Optionally, click **Add field match** to specify the field ID and field value to match.
       * For Microsoft sensitivity labels, enter the label's GUID.

For more information, see [Create a custom metadata label detector](https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels).

  4. For **InfoType** , enter a name for the custom infoType to be created.

If you're creating a custom infoType that is of type **Stored infoType** , enter a name that is different from the name of the underlying stored infoType.

  5. For **Likelihood** , select the default likelihood level that you want to assign to all findings that match this custom infoType. You can further fine-tune the likelihood level of individual findings by using [hotword rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood). If you don't specify a default value, the default likelihood level is set to `VERY_LIKELY`. For more information, see [Match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).

  6. For **Sensitivity** , select the sensitivity level that you want to assign to all findings that match this custom infoType. If you don't specify a value, the sensitivity levels of those findings are set to `HIGH`.

Sensitivity scores are used in [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles). When profiling your data, Sensitive Data Protection uses the sensitivity scores of the infoTypes to [calculate the sensitivity level](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

  7. Click **Done**.

  8. Optional: To add another custom infoType, click **Add custom infoType** again.

  9. Click **Done**.




## What's next

  * Refer to a list of [built-in infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).
  * Learn more about [custom infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes).
  * Learn how to [create a regular custom dictionary detector through the DLP API](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary).
  * Learn how to [create a large custom dictionary detector through the DLP API](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes).
  * Learn how to [create a custom regular expression detector through the DLP API](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-regex).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
