---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/optimize-ingestion/
title: Optimize ingestion volume \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:20.560384+00:00
---

# Optimize ingestion volume  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/optimize-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Optimize ingestion volume

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** While this document discusses various ingestion methods, note that the Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest logs into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This guide explains how to optimize ingestion volume by focusing on configuring Google Security Operations data processing pipelines. This capability provides a unified way to filter, transform, and redact data before it's fully ingested, regardless of the source. This method improves data quality and threat-detection efficiency.

The guide is aimed at security engineers, Google SecOps analysts, and cloud administrators who manage log ingestion into Google SecOps.

Ingesting massive volumes of unfiltered logs can strain your budget and resources. It leads to increased costs, slower search and analysis capabilities, and a higher chance of security analysts missing critical alerts amidst a flood of irrelevant data. Effective filtering is crucial for a cost-effective and efficient Google SecOps deployment.

## Before you begin

Make sure you have or do the following:

  * An Identity and Access Management (IAM) role: Either the predefined Chronicle API `Admin` role (`roles/chronicle.admin`) or a custom role containing one of these permissions: 
    * `chronicle.logProcessingPipelines.*`
    * `chronicle.logTypes.get`
    * `chronicle.logTypes.list`
    * `chronicle.feeds.get`
    * `chronicle.feeds.list`
    * `chronicle.logs.list`
  * Bindplane version: You need Bindplane Server console version 1.96.4 or later.
  * For Bindplane Cloud, Workload Identity Federation (WIF) is supported for authentication. Self-hosted Bindplane deployments require Service Account JSON key credentials.
  * Access to either the Bindplane Management Console or the Google SecOps Data Pipeline APIs to configure the processor nodes.
  * Identify the precise fields, log types, and conditions needed to configure Filter, Transform, and Redact processors for volume reduction.
  * Define pipeline stream inputs by matching the specific log types, collector IDs (for Bindplane sources), or feed names (for data feeds) associated with your ingestion methods.
  * If you're ingesting Google Cloud logs, define the required Logging export filters to implement upstream filtering for maximum cost savings before data reaches the SecOps pipeline.
  * Understand your log data: 
    * Identify high-volume or low-value logs: Analyze your current ingestion metrics to pinpoint which log types and sources are contributing most to volume and cost. For more information, see the [Ingestion metrics overview](https://docs.cloud.google.com/chronicle/docs/ingestion/understand-ingestion-metrics).
    * Determine filtering criteria: Determine the specific fields, values, patterns (regex), or conditions that reliably identify logs to be dropped, transformed, or redacted.
    * Know your ingestion methods: Understand how each target log source is ingested (Direct, Bindplane, Feed, API) as this affects how you configure the pipeline stream.



## Key terminology

  * **Data processing pipelines** : A capability used to filter, transform, and redact log data as it arrives, before it is stored and indexed.
  * **Filter/filtering** : The primary capability for volume optimization, which defines conditions to selectively drop events not needed for security analysis.
  * **Transform** : A capability used to modify log formats for better usability, such as stripping fully qualified domain names (FQDN) or deleting verbose fields within events.
  * **Redact** : A capability to mask or completely remove sensitive information from logs before they are stored, helping with compliance and privacy.
  * **Bindplane agent** : An ingestion method for logs collected from on-premises systems or other cloud systems.
  * **Feeds** : An ingestion method for data brought in from sources, such as Cloud Storage, Amazon S3, or third-party APIs.
  * **Ingestion APIs** : A method for sending custom log data, which allows for server-side filtering using data processing pipelines.
  * **Upstream filtering** : The recommended best practice of filtering Google Cloud logs at the source using Logging export filters for optimal cost savings.
  * **Streams** : A specific flow of data, defined by log type and ingestion source (like a feed or API), that serves as the input to a data processing pipeline.
  * **Processor node** : A component within a pipeline that contains one or more processors (filter, transform, or redact actions) that manipulate data sequentially.
  * **Destination** : The endpoint of the data processing pipeline, typically the Google SecOps instance where processed data is sent for final ingestion and analysis.



## Use data processing pipelines for optimization

Data processing pipelines in Google SecOps offer robust, pre-parsing control over your data ingestion process. They let you define rules and actions that are applied to logs as they arrive, before they are stored and indexed. For more information, see [Set up and manage data processing pipelines](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline).

**Note:** The data processing feature is available for Google SecOps Enterprise and Enterprise plus tiers only.

### Key Capabilities

  * **Filter:** This is the primary focus for volume optimization. You can define conditions, using raw log content, attributes, or regular expression, to selectively drop events that are not required for security analysis. This is key to reducing noise and costs.
  * **Transform:** Modify log formats for better usability or to remove unnecessary data within events. Examples include stripping FQDNs from hostnames, parsing and restructuring JSON payloads, or deleting verbose but irrelevant fields.
  * **Redact:** Mask or completely remove sensitive information, such as Personally Identifiable Information (PII), from logs before they are stored, helping with compliance and privacy requirements.



### Universal applicability

A key advantage of data processing pipelines is that they can be applied to data from any ingestion method. This provides a consistent filtering layer for:

  * Google Cloud built-in logs
  * Logs collected using the Bindplane agent
  * Data brought in through Feeds
  * Custom logs sent through the Ingestion APIs



For more information, see the Method-specific filtering strategies section in this guide.

## Implement filtering with data processing pipelines

### Step 1: Set up your pipeline

You can configure and manage data processing pipelines either through the Bindplane Management Console or by using the public Google SecOps Data Pipeline APIs. They let you define streams (inputs), configure processor nodes (Filter, Transform, Redact), and manage pipeline deployment.

For comprehensive setup instructions, see [Set up and manage data processing pipelines](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline).

### Step 2: Configure the processors for filtering

Within a pipeline, you can add processors to a node. To reduce volume, you should primarily use Filter processors. You can configure these processors to drop logs based on conditions or regular expressions. You configure custom pipeline conditions and statements using OTTL (OpenTelemetry Transformation Language) syntax.

  * **Conditions:** Evaluating fields or attributes in the log data.
  * **Regular expressions:** Matching patterns within the raw log message.
  * **OTTL Example:** An example statement would be `set(attributes["labels.myLabel.value"], "myValue")`.



While filtering is key, you can also consider using Transform processors to remove large, unnecessary fields from logs you do keep, and use Redact processors to nullify sensitive data.

### Step 3: Method-specific filtering strategies

The following sections explain how to approach filtering with data processing pipelines for each main ingestion type.

#### Google Cloud logs

  * **Upstream filtering (recommended best practice):** For optimal cost savings, Google recommends filtering Google Cloud logs at the source using Cloud Logging export filters. This prevents unwanted logs from being sent to Google SecOps in the first place. You can use data processing pipelines for additional filtering if needed. For more information, see the [Ingest Google Cloud data guide](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs), in particular the [Customize export filter settings](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs#export_filter_settings) section.

  * **Pipeline application:** Configure a data processing pipeline, selecting the appropriate Google Cloud log type and ingestion method, either **Direct** or **Cloud Native**. Define filter processors to drop unwanted logs based on content.




#### Bindplane Agent

Logs collected by the Bindplane agent, from on-premises systems or other cloud systems, can be filtered using a data processing pipeline. Configure the stream to match the log types and collector IDs associated with your Bindplane sources. For more information, see [Use Bindplane with Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent).

#### Data Feeds

For data ingested using Feeds (for example, from Cloud Storage, Amazon S3, or third-party APIs), you can apply data processing pipeline filters by selecting the feed name and log type when configuring the pipeline stream. For more information, see the [Work with feeds](https://docs.cloud.google.com/chronicle/docs/administration/feed-management) guide.

#### Chronicle API ingestion methods

If you send data using the Chronicle API ingestion methods, you can still leverage data processing pipelines. Configure the pipeline stream to match the log type you use in your API calls. This allows server-side filtering of your custom log streams. For more information, see the [Chronicle API ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) guide.

**Note:** For low-volume streams using the Chronicle API ingestion methods, acknowledgment times may increase from 700ms to 2 seconds due to in-memory buffering. Acknowledgment time returns to normal once data throughput exceeds 4 MB.

## Best Practices

  * **Filter upstream when possible:** As mentioned for Google Cloud, always filter logs as close to the source as possible. This is the most cost-effective approach as it reduces data transfer and processing overhead.
  * **Be specific:** Start with narrow, well-defined filters to exclude known high-volume, low-value logs. Avoid overly broad filters that might accidentally drop useful data.
  * **Iterate and refine:** Regularly review the effectiveness of your filters. Are they catching the right events? Is there new noise that needs to be filtered?
  * **Document your filters:** Keep a record of what filters are in place and why, especially for complex regular expression or conditional logic.



## Verification & testing

  * **Testing:** You should test your filters in a non-production environment or with a small subset of data first.
  * **Validate filters:** Use the testing features within the Bindplane Console's pipeline editor. This lets you input sample logs and see the output after your processors are applied, confirming your filters work as expected.
  * **Monitor ingestion:** After deploying pipelines, monitor your ingestion dashboards in Google SecOps to observe the impact on data volume and costs. For more information, see the [Ingestion metrics overview](https://docs.cloud.google.com/chronicle/docs/ingestion/understand-ingestion-metrics).
  * **View Configurations:** You can view all configurations in the Google SecOps UI under **SIEM Settings > Data Processing**.
  * **External Management:** You can search configurations and click **"Open in Bindplane"** to jump directly to the Bindplane console for advanced management.



## Limitations

  * **Service limits:** Overly complex regexes or a large number of processors per pipeline can impact performance or may be subject to limits. You should check out the Google SecOps limits in [Service limits](https://docs.cloud.google.com/chronicle/docs/reference/service-limits).
  * **Google SecOps packages:** Make sure you're aware of the features and capabilities in your Google SecOps package. For more information, see [Google SecOps packages](https://docs.cloud.google.com/chronicle/docs/secops/secops-packages).
  * **Reusability:** While powerful, a pipeline configuration for one log type or source might not be directly reusable for another without adjustments.
  * **Maximum Processors:** Define a maximum of 10 processors per pipeline.
  * **Regex Performance:** Avoid excessive regular expression matching, as it can cause pipeline creation or deployment to fail due to timeouts. Prefer parsing data to JSON and filtering by specific fields.
  * **Stream Association Constraint:** While different pipelines can be created for different feeds of the same log type, the exact same stream definition (e.g., the same feed, or the same log type catch-all) cannot be associated with more than one active pipeline. Setting a log type to **All Ingestion Methods** acts as a catch-all and prevents configuring other pipelines for specific feeds of that log type.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
