---
url: https://docs.cloud.google.com/binary-authorization/docs/viewing-on-prem-logs/
title: View audit logs for Google Distributed Cloud \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:14.693948+00:00
---

# View audit logs for Google Distributed Cloud  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/viewing-on-prem-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  View audit logs for Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view log entries produced by Binary Authorization for Google Distributed Cloud software. These entries can be used to troubleshoot the system setup and use.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To use this document, you must configure your Distributed Cloud user cluster to forward log entries to Cloud Audit Logs.

To enable Cloud Audit Logs, you must [configure the `cloudAuditLogging` section](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-configuration-file) of your user cluster configuration file to properly forward log events. If your GKE clusters on GDC are not configured to forward log entries, you can [view local audit logs](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/audit-logging) by using keyword searches. Entries in local logs are formatted as described in this document.

This document describes how to use Cloud Audit Logs to query for log entries. You can also query log entries through the [Cloud Audit Logs API](https://docs.cloud.google.com/logging/docs/apis).

## View Cloud Audit Logs entries

  1. In the Google Cloud console, go to the **Cloud Audit Logs** page.

[Go to Cloud Audit Logs](https://console.cloud.google.com/logs)

  2. Select the Google Cloud project you configured in the `cloudAuditLogging` section of your user cluster configuration file.

  3. Enter a filter. You can find example filters for Binary Authorization for Distributed Cloud log entries in the following sections.

  4. Select the activity log:

     1. Select the **Log name** combo box.

     2. Enter `externalaudit.googleapis.com` in the text field.

     3. Select the log named `externalaudit.googleapis.com`.

     4. Click **Add**.

     5. Make sure you select the time period when the events would have occurred.

  5. Click **Run Query**.




## View rejected Deployment log entries

To find Cloud Audit Logs entries for rejected Deployments, use the following query:
    
    
    resource.type="k8s_cluster"
    (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
     protoPayload.methodName="io.k8s.core.v1.pods.update")
    protoPayload.response.status="Failure"
    

## View dry run log entries

To find Cloud Audit Logs entries related to Pod create or update with dry run enabled, use the following query:
    
    
    resource.type="k8s_cluster"
    (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
     protoPayload.methodName="io.k8s.core.v1.pods.update")
    labels."binaryauthorization.googleapis.com/dry-run"="true"
    

## View breakglass log entries

To find Cloud Audit Logs entries related to Pod create or update with breakglass enabled, use the following query:
    
    
    resource.type="k8s_cluster"
    (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
      protoPayload.methodName="io.k8s.core.v1.pods.update")
    (labels."binaryauthorization.googleapis.com/break-glass"="true" OR
      protoPayload.request.metadata.labels."image-policy.k8s.io/break-glass"="true")
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
