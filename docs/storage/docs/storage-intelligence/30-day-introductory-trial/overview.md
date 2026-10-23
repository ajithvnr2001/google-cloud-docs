---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview/
title: 30-day introductory trial for Storage Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:43.131991+00:00
---

# 30-day introductory trial for Storage Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  30-day introductory trial for Storage Intelligence Stay organized with collections  Save and categorize content based on your preferences. 

The 30-day introductory trial for Storage Intelligence lets you evaluate, organize, and manage your Cloud Storage data at scale. The trial helps you identify optimization opportunities, analyze data, relocate buckets, and automate bulk object operations.

During the trial, you can use Storage Intelligence features in the following ways:

Action | Description  
---|---  
[Get resource metadata with Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) |  Create datasets of metadata and activity data for your Cloud Storage resources.   
[Export resource metadata to BigQuery](https://docs.cloud.google.com/storage/docs/insights/configure-datasets) |  Export metadata for your Cloud Storage resources to BigQuery for analysis.   
[Analyze storage with Gemini Cloud Assist](https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist) |  Get AI-powered insights about your data storage landscape.   
[Generate inventory reports](https://docs.cloud.google.com/storage/docs/insights/inventory-reports) |  Generate lists of objects and their metadata for analysis.   
[Relocate buckets](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) |  Relocate buckets across geographic locations.   
[Automate object operations at scale](https://docs.cloud.google.com/storage/docs/batch-operations/overview) |  Perform operations on millions or billions of objects using batch operations.   
  
## Trial overview

You can use the 30-day introductory trial to explore Storage Intelligence and analyze your storage data for up to 30 days. You can enable the `TRIAL` tier using the Google Cloud console, Google Cloud CLI, or REST APIs. After activation, you can use the trial to create Storage Insights datasets, get data insights with Gemini assistance, relocate buckets, and run storage batch operations. For pricing details, see [ Storage Intelligence pricing](https://docs.cloud.google.com/storage/pricing#storage-intelligence).

The following table provides information about the 30-day introductory trial for Storage Intelligence:

Eligibility  | You're eligible to configure the `TRIAL` tier for Storage Intelligence once for every organization, folder, and project for a 30-day period. If you enable the `TRIAL` tier for an organization, then all its folders and projects inherit the `TRIAL` tier. However, if you have enabled the `STANDARD` tier at any of these nodes, then you are no longer eligible for the introductory `TRIAL` offer.  
---|---  
Storage Intelligence tiers  | A `TRIAL` tier enables the `STANDARD` tier features, such as Storage Insights datasets, bucket relocation, and storage batch operations. The `TRIAL` tier defaults to the `STANDARD` tier at the end of the 30-day period. If you don't want to use the `STANDARD` tier, you can disable the `TRIAL` tier at any time within the 30-day period.  
Initiation | You can set the Storage Intelligence configuration to the `TRIAL` tier using the Google Cloud console, Google Cloud CLI, or REST API. To initiate the `TRIAL` tier, you'll need the Storage Admin role with the following permissions:

  * `storage.intelligenceConfigs.update`
  * `storageinsights.datasetConfigs.create`

  
Duration  | Your introductory trial ends when one of the following occurs:

  * 30 days have elapsed since you initiated the trial.
  * You upgrade your `TRIAL` tier to the paid `STANDARD` tier.
  * You disable the `TRIAL` tier on the organization, project, or folder it was enabled on.

If you don't disable your `TRIAL` tier after the 30-day introductory trial period, the tier is upgraded to the `STANDARD` tier and charges are applied in the same project where the buckets and objects are stored. Existing datasets are not removed automatically and they continue to incur storage charges until you delete them. If you terminate the use of the Storage Intelligence `STANDARD` tier within 30 days of activation, you incur an early termination fee for the remaining duration.  
Service level agreement (SLA) | SLAs might be limited during the trial period. The `STANDARD` tier SLAs can be activated at any time by upgrading the tier. You can activate the `STANDARD` tier SLA by upgrading the tier at any time during the trial period.  
  
For continuous access to the Storage Intelligence features beyond the trial period, you can enable the `STANDARD` tier. For more information about the Storage Intelligence `STANDARD` tier, see [Overview of Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview).

## Dashboard template

The [Storage Intelligence dashboard](https://lookerstudio.google.com/reporting/670eee3f-ad6d-45ea-a169-853ab023dc84) is a template that provides the insights you can gain from Storage Insights datasets. You can use the template to begin building dashboards and visualizations customized for your specific needs. For setup instructions, see [Storage Intelligence dashboard connection instructions](https://lookerstudio.google.com/c/reporting/670eee3f-ad6d-45ea-a169-853ab023dc84/page/6kP1D).

**Note:** Visualizing data can consume significant BigQuery compute resources, especially when working with large datasets. To manage resource usage during evaluation, use a smaller representative dataset. A smaller dataset minimizes costs while allowing exploration of the dashboard and its insights. After exploring the smaller dataset, analyze larger datasets as needed.

## Pricing

During your trial, we don't charge you the Storage Intelligence object management fee for all objects within the trial's scope. However, the storage and query charges still apply. For full pricing details, see the [ Storage Intelligence pricing](https://docs.cloud.google.com/storage/pricing#storage-intelligence) page.

## Limitations

The 30-day introductory trial for Storage Intelligence has the following limitations:

  * You can activate this trial only once for a specific organization, folder, or project.
  * Once activated for an organization, folder, or project, the trial period lasts for 30 days.
  * SLAs might be limited during the trial period.
  * Google Cloud can discontinue the trial at any time.



## Support

For any questions or feedback, contact [storage-intelligence-customer-support@google.com](mailto:storage-intelligence-customer-support@google.com).

## What's next

  * Learn about: 
    * [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview)
    * [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets)
    * [Inventory reports](https://docs.cloud.google.com/storage/docs/insights/inventory-reports)
    * [Gemini Cloud Assist](https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist)
    * [Bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview)
    * [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview)
  * For details about Storage Intelligence pricing after the trial period, see the [Pricing page](https://docs.cloud.google.com/storage/pricing#storage-intelligence).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
