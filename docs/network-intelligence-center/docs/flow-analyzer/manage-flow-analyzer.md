---
url: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/manage-flow-analyzer/
title: Troubleshoot data issues in Flow Analyzer \u00a0|\u00a0 Network Intelligence Center - Flow Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:02.597993+00:00
---

# Troubleshoot data issues in Flow Analyzer  |  Network Intelligence Center - Flow Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/manage-flow-analyzer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Flow Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)



#  Troubleshoot data issues in Flow Analyzer Stay organized with collections  Save and categorize content based on your preferences. 

Use the following guidance to troubleshoot common issues with Flow Analyzer. To learn more about Flow Analyzer, see the [overview](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview).

## No data is displayed

If you don't see any data in Flow Analyzer, do the following:

  1. Make sure that VPC Flow Logs is enabled for the relevant subnets. For more information, see [Enable VPC Flow Logs when you create a subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-logging-new) or [Enable VPC Flow Logs for an existing subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-logging-existing).
  2. Make sure that the timeline is correctly set. If there's no traffic flow within the selected time period, Flow Analyzer doesn't show any data. For more information, see [Time-range selector](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#time-selector).
  3. Validate the log bucket setup: 
     * Ensure that the project has a log bucket that contains VPC Flow Logs.
     * Check that VPC Flow Logs is not disabled for the log bucket in the project.
     * Verify that VPC Flow Logs is not directed to another bucket. For more information, see [Configure a central bucket](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/configure-central-bucket).
     * Confirm that the log bucket is upgraded to use Observability Analytics. For more information, see [Enable Observability Analytics](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/enable-log-analytics).
  4. Check for missing fields and filters: 
     * Make sure that there are no missing metadata fields.
     * Verify there are no filtered out fields in VPC Flow Logs.
  5. Make sure that the sampling rate is not too low.



## Missing metadata fields

There aren't any metadata fields in VPC Flow Logs due to the following reasons:

  * Metadata is disabled in VPC Flow Logs for this project.
  * The traffic flow is a part of cross-project communication.
  * Actual data is unknown because the traffic is from an external resource.
  * The metadata information is not yet available.



## Filtered out fields in VPC Flow Logs

When you enable VPC Flow Logs, you can set a filter based on both base and metadata fields that only preserves logs that match the filter. All other logs are discarded before being written to Logging, which saves you money and reduces the time needed to find the information you are looking for.

You or other users can filter on any subset of fields from the record format. Verify that the required fields are not filtered out by other users in your project. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering).

## Low sampling rate

If the sampling rate is set too low, you cannot see any data in Flow Analyzer.

For additional troubleshooting information, see [Troubleshoot VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/access-flow-logs#troubleshooting).

## Send feedback about Flow Analyzer

To send your feedback about Flow Analyzer or any issues faced while using Flow Analyzer, do the following:

  1. Click the **Send feedback** icon. The Send feedback to Google panel appears.
  2. Describe your feedback.
  3. To add a screenshot, click **Capture screenshot**. You can also mark the area of concern or hide sensitive information by using the **Edit** tool.
  4. Select the contents of the current tab.
  5. Click **Share**. The screenshot is added to the feedback.
  6. Click **Send**.



## What's next

  * [Analyze traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows)
  * [Run Connectivity Tests from Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/run-connectivity-tests)
  * [Monitor your traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/monitor-traffic-flows)



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
