---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/audit-logging/
title: Use Kubernetes audit logging \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:36.958309+00:00
---

# Use Kubernetes audit logging  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/audit-logging/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Use Kubernetes audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/audit-logging)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/audit-logging)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document describes how to use Cloud Audit Logs for Google Distributed Cloud. Google Distributed Cloud uses [Kubernetes Audit Logging](https://kubernetes.io/docs/tasks/debug-application-cluster/audit/), which keeps a chronological record of calls made to a cluster's Kubernetes API server. Audit logs are useful for investigating suspicious API requests and for collecting statistics. For information about audit logging for the GKE On-Prem API, see [Cloud API audit logging](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/audit-logging-api).

**Note:** Starting with Google Distributed Cloud release 1.9.0, Cloud Audit Logs is enabled by default. Cloud Audit Logs is automatically enabled for 1.8.x clusters that are upgraded to 1.16.8 unless it was explicitly disabled for the 1.8.x cluster by setting `disableCloudAuditLogging` to `true`.

## About Cloud Audit Logs

Audit logs are written to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) in your Google Cloud project. Writing to Cloud Audit Logs has several benefits over writing to disk or capturing logs in an on-premises logging system:

  * Audit logs for all GKE clusters can be centralized.
  * Log entries written to Cloud Audit Logs are immutable.
  * Cloud Audit Logs entries are retained for 400 days.
  * Cloud Audit Logs feature is included in the price of Distributed Cloud.
  * You can configure Google Distributed Cloud to write logs to disk or to Cloud Audit Logs.



### Disk-based audit logging

If Cloud Audit Logs is disabled explicitly, audit logs in Google Distributed Cloud are written to a persistent disk so that cluster restarts and upgrades don't cause the logs to disappear. Google Distributed Cloud retains up to 1 GiB of audit log entries.

Access the disk-based audit logs by logging into control plane Nodes. The logs are located in the `/var/log/apiserver/` directory.

### Cloud Audit Logs

Admin Activity audit log entries from all Kubernetes API servers are sent to Google Cloud, using the project and location that you specify when you create a user cluster. To buffer and write log entries to Cloud Audit Logs, Google Distributed Cloud deploys an `audit-proxy` daemon set that runs on the control plane nodes.

### Limitations

Cloud Audit Logs for Google Distributed Cloud has the following limitations:

  * Data access logging is not supported.
  * Modifying the Kubernetes audit policy is not supported.
  * Cloud Audit Logs is not resilient to extended network outages. If the log entries cannot be exported to Google Cloud, they are cached in a 10 GiB disk buffer. If that buffer fills, then the oldest entries are dropped.



## Creating a service account for Cloud Audit Logs

Before you can use Cloud Logging and Cloud Monitoring with Google Distributed Cloud, you must first configure the following:

  1. Create a Cloud Monitoring Workspace within the Google Cloud project, if you don't have one already.

In the Google Cloud console, click the following button and follow the workflow.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Click the following buttons to enable the required APIs:

[Enable the Anthos Audit API](https://console.cloud.google.com/apis/library/anthosaudit.googleapis.com)

[Enable the Stackdriver API](https://console.cloud.google.com/apis/library/stackdriver.googleapis.com)

[Enable the Monitoring API](https://console.cloud.google.com/apis/library/monitoring.googleapis.com)

[Enable the Logging API](https://console.cloud.google.com/apis/library/logging.googleapis.com)

  3. Assign the following IAM roles to the service account used by the Stackdriver agents:

     * `logging.logWriter`
     * `monitoring.metricWriter`
     * `stackdriver.resourceMetadata.writer`
     * `monitoring.dashboardEditor`



## Accessing Cloud Audit Logs

### Console

  1. In the Google Cloud console, go to the **Logs Explorer** page in the **Logging** menu.

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

If the **Legacy Logs Viewer** page opens, choose **Upgrade to the new Logs Explorer** from the **Upgrade** drop-down menu.

  2. Click **Query** to access the field for submitting queries.

  3. Fill the field with the following query:
         
         resource.type="k8s_cluster"
         logName="projects/PROJECT_ID/logs/externalaudit.googleapis.com%2Factivity"
         protoPayload.serviceName="anthosgke.googleapis.com"
         

Replace `PROJECT_ID` with your project ID.

  4. Click **Run query** to display all audit logs from Google Distributed Cloud clusters that were configured to sign in to this project.




### gcloud

List the first two log entries in your project's Admin Activity log that apply to the `k8s_cluster` resource type:
    
    
    gcloud logging read \
        'logName="projects/PROJECT_ID/logs/externalaudit.googleapis.com%2Factivity" \
        AND resource.type="k8s_cluster" \
        AND protoPayload.serviceName="anthosgke.googleapis.com" ' \
        --limit 2 \
        --freshness 300d
    

Replace `PROJECT_ID` with your project ID.

The output shows two log entries. Notice that for each log entry, the `logName` field has the value `projects/PROJECT_ID/logs/externalaudit.googleapis.com%2Factivity` and `protoPayload.serviceName` is equal to `anthosgke.googleapis.com`.

## Audit policy

The Kubernetes audit policy defines rules for which events are recorded as log entries and specifies what data the log entries should include. Changing this policy to modify Cloud Audit Logs behavior isn't supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
