---
url: https://docs.cloud.google.com/logging/docs/regionalized-logs/
title: Regionalize your logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:08.056809+00:00
---

# Regionalize your logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/regionalized-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Regionalize your logs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use the `_Default` sink to route your log entries to a Cloud Logging bucket that is in a specific region. For a list of supported regions, see [Locations](https://docs.cloud.google.com/logging/docs/region-support).

You can also set a default storage location for new `_Default` and `_Required` buckets by configuring default settings for your organization or folder. For more information, see [Set the default storage location](https://docs.cloud.google.com/logging/docs/default-settings#specify-region).

This guide walks through this process using the example of redirecting all logs to one region. This process involves the following steps:

  1. Create a log bucket in the designated region for storing the logs.

  2. Redirect the `_Default` sink to route the logs to the new log bucket.

  3. Search for logs in the Logs Explorer.




## Overview

In Logging, [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries#about_log_buckets) are regional resources: the infrastructure that stores, indexes, and searches your logs is located in a specific geographical location. With the exception of log buckets in the `global`, `eu`, or `us` regions, Google Cloud manages the infrastructure so that your applications are available redundantly across the zones within the region of the log bucket.

Your organization might be required to store its logs data in specific regions. The primary factors in selecting the region where your logs are stored include meeting your organization's latency, availability, or compliance requirements. When selecting a region for logs storage, consider the locations of the other Google Cloud products and services that your application uses.

If you have data residency requirements, then don't enable services that can query log data and then store the query result in a `global` location. An example of such a service is [Gemini Cloud Assist](https://docs.cloud.google.com/gemini/docs/discover/certifications#cloud-assist-security).

## Key concepts

The following key concepts apply to data regionality for Logging.

### Log Router locations

The [Log Router](https://docs.cloud.google.com/logging/docs/routing/overview) processes all log entries written to the Cloud Logging API. It checks each log entry against existing rules to determine which log entries to store in Logging buckets and which log entries to route to supported destinations using [sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks). To reliably route logs, the Log Router also stores the logs temporarily, which buffers against temporary disruptions on any sink.

The Log Router processes logs in the region in which they are received. The Log Router might send logs to a different region based on a sink's definition or if you've opted to share log data with another Google Cloud service such as the [Security Command Center Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-event-threat-detection). Sinks apply to logs equally and regardless of region. 

### Log bucket locations

[Log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries) are the containers in your Google Cloud project, billing account, folder, and organization that store and organize your logs data.

For each Google Cloud project, billing account, folder, and organization, Logging automatically creates two log buckets: `_Required` and `_Default`, which are in the `global` location. You can't change the location of existing buckets. However, your organization can create a policy that sets a different default location for these buckets. For more information, see [Configure default settings for organizations and folders](https://docs.cloud.google.com/logging/docs/default-settings).

You can also [create user-defined log buckets](https://docs.cloud.google.com/logging/docs/buckets) for any Google Cloud project. When you create a user-defined log bucket, you can specify the location of the log bucket. After you create the log bucket, the location can't be changed, but you can create a new bucket and then direct log entries to the new log bucket by using sinks. To learn how to set the location for your buckets, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).

**Note:** Log buckets in the `global` region or in multi-regions don't offer added resiliency compared to log buckets created in single regions like `us-west1`.

Logging supports querying logs from multiple regions together, in which case queries are processed in the same locations as the buckets being queried and then aggregated in the region the query was received from to return the results.

The region of a log bucket is shown on the **Logs Storage** page and on some dialogs. For example, when you to the Logs Explorer page and use the **Refine scope** selector to list log views, region information is also displayed. For this selector, when the region is `global`, both the region and the current storage location are displayed in a format similar to `GLOBAL (US-WEST4)`.

## Before you begin

  1. Identify the Google Cloud project that will store your log entries.
  2. Identify the name and location of the log bucket that will store your log entries.
  3. Determine the log entries that you want to route to your log bucket. In this guide, we include all logs routed by the `_Default` sink.
  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 




## Supported regions

When you create your log bucket, you can choose where to store your logs. For a list of supported regions, see [Locations](https://docs.cloud.google.com/logging/docs/region-support).

## Create the log bucket

**Note:** Error Reporting evaluates log entries only when certain criteria are true. For more information, see [When Error Reporting analyzes log entries](https://docs.cloud.google.com/error-reporting/docs/grouping-errors#when-analyze). 

Log buckets store log entries. Projects, folders, and organizations contain log sinks that route log entries to log buckets or to other destinations. When the destination of a sink is a log bucket, that log bucket can be in the same resource as the log sink, or in a different resource. For more information, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets).

  1. Open a shell.

For example, to use the Cloud Shell, do the following:

     1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/)

     2. In the toolbar, click _terminal_ **Activate Cloud Shell**.
  2. To create a log bucket, run the [`gcloud logging buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/create) command in the shell. Before running the example command, make the following replacements:

     * BUCKET_ID: The name or ID of the log bucket.
     * LOCATION: The location of the log bucket.
     * PROJECT_ID: The identifier of the project.

Example command:
    
    gcloud logging buckets create BUCKET_ID \
      --location=LOCATION \
      --project=PROJECT_ID
    

**Note:** After you create your bucket, you can't change your bucket's location.
  3. Verify that the bucket was created:
         
         gcloud logging buckets list --project=PROJECT_ID
         




After you create your log bucket, you can change some properties, such as the description and the data retention period. To make these changes use the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command.

## Redirect the `_Default` logs sink

You route logs to a log bucket by creating a sink. A sink includes a filter, which selects which log entries to export through the sink, and a destination. In this guide, we update the existing `_Default` sink to route log entries to the log bucket created in the previous step.

**Note:** Redirecting the `_Default` sink ensures that all future logs go into the regionalized log bucket rather than the `_Default` bucket, which is **global**. You can't change the `_Required` sink, with the logs going into a different global bucket.

To update a sink, run the [`gcloud logging sinks update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) command. Before running the example command, make the following replacements, make the following replacement:

  * _Default: This example updates the destination for the sink named `_Default`. If you want to update a different sink, then change the name of this variable.
  * BUCKET_ID: The name or ID of the log bucket.
  * LOCATION: The location of the log bucket.
  * PROJECT_ID: The identifier of the project.



Example command:
    
    
    gcloud logging sinks update _Default \
      logging.googleapis.com/projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID \
      --log-filter='NOT LOG_ID("cloudaudit.googleapis.com/activity") AND NOT
        LOG_ID("externalaudit.googleapis.com/activity") AND NOT
        LOG_ID("cloudaudit.googleapis.com/system_event") AND NOT
        LOG_ID("externalaudit.googleapis.com/system_event") AND NOT
        LOG_ID("cloudaudit.googleapis.com/access_transparency") AND NOT
        LOG_ID("externalaudit.googleapis.com/access_transparency")' \
      --description="Updated the _Default sink to route logs to the LOCATION region"
    

**Note:** When you create a project, the filter for the `_Default` sink is as shown in the previous command. This filter, which excludes log entries that are routed by the `_Required` sink to the `_Required` log bucket, ensures that log entries are routed to the `_Default` log bucket or to the `_Required` log bucket, but not to both log buckets.

## Create a log entry to test your sink

To verify that you updated the sink properly, complete the following steps:

  1. Send a test log message to your regionalized bucket by using the [`gcloud logging write`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/write) command. Before running the example command, make the following replacements:

     * LOG_NAME: The name of your log.
     * BUCKET_ID: The name or ID of the log bucket.
     * PROJECT_ID: The identifier of the project.

Example command:
    
    gcloud logging write LOG_NAME "Test to route logs to BUCKET_ID" \
    --project=PROJECT_ID
    

**Note:** It might take several minutes for the test message to be sent.
  2. View your log entry:

     1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. In the toolbar, click **Refine scope** , and then select **Current project**.

The Logs Explorer is configured to display log entries that originate in your project.

     3. In the **Log field** pane, select the **Global** resource type.

     4. Your test log entry displays in the **Query results** panel.




## Search logs in the Google Cloud console

To view the log entries in your log bucket, go to the Google Cloud console and complete the following steps:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select **Refine Scope**.

  3. On the **Refine scope** panel, select **Log view**.

  4. Select the `_AllLogs` view associated with your **BUCKET_NAME**.

  5. Click **Apply**.

The **Logs Explorer** refreshes to show logs from your bucket.

For information on using the Logs Explorer, refer to [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).




## Next steps

  * [View all the Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations#region).

  * [Explore additional location-based concepts](https://docs.cloud.google.com/docs/geography-and-regions), such as zones, that apply to other Google Cloud services.

  * Read the following whitepapers that provide best practices for data governance:

    * [Logs data: A step by step guide for overcoming common compliance challenges](https://services.google.com/fh/files/misc/whitepaper_data_governance_logs_how_to.pdf)

    * [Data governance: Principles for securing and managing logs](https://cloud.google.com/resources/data-governance-logs-best-practices-whitepaper)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
