---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor/
title: View Storage Intelligence advisor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:32.987236+00:00
---

# View Storage Intelligence advisor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  View Storage Intelligence advisor Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view Storage Intelligence advisor.

Storage Intelligence advisor helps you monitor the health of your Cloud Storage resources, optimize storage usage, and resolve performance bottlenecks. The advisor provides environment metrics, highlights anomalies that require attention, and suggests remediation steps. For more information, see [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview).

## Before you begin

To view Storage Intelligence advisor, complete the steps in the following sections.

### Configure Storage Intelligence

Before you can view Storage Intelligence advisor, [configure Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence).

### Required roles

To get the permissions that you need to view Storage Intelligence advisor, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view Storage Intelligence advisor. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view Storage Intelligence advisor:

  * View Storage Intelligence advisor, findings, finding details, findings summary, and bucket drill-down: `storage.buckets.viewIntelligenceDetails`
  * View dashboards from Cloud Monitoring: 
    * `monitoring.dashboards.get`
    * `monitoring.dashboards.list`
  * View groups from Cloud Monitoring: 
    * `monitoring.groups.get`
    * `monitoring.groups.list`
  * View metrics from Cloud Monitoring: 
    * `monitoring.metricDescriptors.list`
    * `monitoring.timeSeries.create`
    * `monitoring.timeSeries.list`
  * View resource descriptors from Cloud Monitoring: 
    * `monitoring.monitoredResourceDescriptors.get`
    * `monitoring.monitoredResourceDescriptors.list`
  * View project and resource metadata from Cloud Monitoring: 
    * `stackdriver.projects.get`
    * `stackdriver.resourceMetadata.list`
  * Use Gemini for troubleshooting: `cloudaicompanion.instances.completeTask`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View Storage Intelligence advisor

To view Storage Intelligence advisor, do the following:

  1. In the Google Cloud console, go to the Storage Intelligence **Advisor** page.

[Go to Advisor](https://console.cloud.google.com/storage/storage-intelligence/dashboards)

  2. Optional: In the resource picker, select your project, folder, or organization.

  3. Review the **At a glance** section (labeled **Project at a glance** , **Folder at a glance** , or **Organization at a glance** depending on the selected resource) to see high-level metrics, which include the following details:

     * **Total storage size** : categorized by storage class.
     * **Bucket count and object count** : the total number of buckets containing objects and the total object count.
     * **Average object size** : the average size of objects in your buckets.
  4. To investigate anomalies, navigate to the **Top findings** section.

  5. Click a specific finding, such as **Spike in Class A/B operations** , to view its details and recommended next steps. For more information, see View finding details.




## Historical data

Storage Intelligence advisor provides a historical view of your Cloud Storage environment by retaining aggregated bucket metadata and activity data for 390 days. Because Storage Intelligence advisor includes data from deleted buckets, it might show information about resources that are no longer active.

## Respond to specific findings

The following sections describe how to respond to findings.

### View finding details

The procedure for viewing finding details depends on whether you view Storage Intelligence advisor at the organization, folder, or project level.

#### View findings for an organization or folder

When you view Storage Intelligence advisor at the organization or folder level, finding cards in the **Top findings** section summarize anomalies across all projects in that scope. Each card displays the number of affected projects (for example, **5 affected projects**).

To investigate findings for an organization or folder, do the following:

  1. In the Google Cloud console, go to the Storage Intelligence **Advisor** page.

[Go to Advisor](https://console.cloud.google.com/storage/storage-intelligence/dashboards)

  2. In the resource picker, select your organization or folder.

  3. In the **Top findings** section, locate the finding you want to investigate and click **View details**.

The **View projects with ' finding-name'** side panel opens.

  4. In the **Projects with finding** table, review the list of projects where the finding is active:

     * **Project ID / Name** : The identifier for each affected project.
     * **Finding** : The metric change or percentage increase detected in that project.
     * **Last updated** : The timestamp when the finding was last refreshed.
     * **Permission indicators** : If you lack permissions to view a specific project within the organization or folder, a warning indicator displays the message `You've insufficient permission to access this project`.
  5. Click a **Project ID** to open the finding details and charts for that project in a new tab.

**Note:** When you open the finding details page for a selected project, the resource scope in the new tab changes to that project. The resource scope on the original page remains unchanged.



#### View finding details for a project

When you view Storage Intelligence advisor for a project (or navigate to a project from the organization or folder side panel), you can drill down into bucket-level and object-level details.

To view project finding details, do the following:

  1. In the Google Cloud console, go to the Storage Intelligence **Advisor** page.

[Go to Advisor](https://console.cloud.google.com/storage/storage-intelligence/dashboards)

  2. In the resource picker, select your project.

  3. In the **Top findings** section, navigate to the finding you want to investigate and click **View details**.

  4. On the **Finding details** page, review the following details:

     * **Findings category** : the type of finding (for example, Usage optimization or Performance).
     * **Last updated** : the time when the finding was last refreshed.
     * **Common factors** : general causes contributing to the finding.
     * **Overall project-wide increase** : the total impact across your project.
  5. To identify which specific buckets are causing an increase in the metric that triggers the finding, view the **Buckets with largest increases** table.

  6. To view detailed information for a bucket, select the bucket.

  7. On the bucket's **View details** page, analyze the bucket's activity to identify the root cause of the anomaly:

     * **Bucket activity** : Review the specific metrics related to the finding.
     * **Prefixes with largest increases** : Identify the specific object prefixes or directory paths where activity increased.
     * **Service accounts with largest increases** : Identify the principals or service accounts that sent the increased API requests.



### Respond to the 'Spike in Class A/B operations' finding

To respond to the **Spike in Class A/B operations on Coldline or Archive data** finding, do the following:

  1. Complete the steps in View finding details.
  2. On the bucket's **View details** page, analyze the bucket's activity by reviewing the metrics for **Class A/B operations** and **% growth**.
  3. For guidance on selecting the recommended next step, see [Strategies for responding to a spike in Class A/B operations on Coldline or Archive data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs#respond-to-a-finding).



### Respond to the 'Spike in 429 errors' finding

To respond to the **Spike in 429 errors indicating rate limited requests** finding, do the following:

  1. Complete the steps in View finding details.
  2. On the bucket's **View details** page, analyze the bucket's activity by reviewing the metrics for **Number of`429` errors** and **% increase**.
  3. For guidance on selecting the recommended next step, see [Strategies for responding to a spike in 429 errors indicating rate limited requests](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors#respond-to-a-finding).



### Respond to the 'Spike in cross-region egress' finding

To respond to the **Spike in cross-region egress** finding, do the following:

  1. Complete the steps in View finding details.
  2. On the bucket's **View details** page, analyze the bucket's activity by reviewing the metrics for **Cross-region egress volume** and **% increase**.
  3. For guidance on selecting the recommended next step, see [Strategies for responding to a spike in cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress#respond-to-a-finding).



### Respond to the 'Total bytes stored increased above trend' finding

To respond to the **Total bytes stored increased above trend over the last 30 days** finding, do the following:

  1. Complete the steps in View finding details.
  2. On the bucket's **View details** page, analyze the bucket's activity by reviewing the metrics for **Storage volume growth** and **% growth**.
  3. For guidance on selecting the recommended next step, see [Strategies for responding to an above trend storage consumption increase](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption#respond-to-a-finding).



## What's next

  * **Respond to findings** : 
    * [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors)
    * [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs)
    * [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption)
    * [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress)
    * [Review the findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog)
  * **Related concepts** : 
    * [Storage Intelligence advisor overview](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview)
  * **Troubleshooting** : 
    * [Troubleshoot Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting#advisor-issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
