---
url: https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs/
title: View audit logs for GKE \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:15.664289+00:00
---

# View audit logs for GKE  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  View audit logs for GKE Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to view information about deployment status and policy enforcement in [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

To learn more about Cloud Audit Logs user interface terminology used in this page, see [Viewing logs](https://docs.cloud.google.com/logging/docs/view/basic-queries).

You can assess your application security posture, including Binary Authorization policy enforcement across interdependent Google Cloud products in a single dashboard. To learn more, see [Security monitoring](https://docs.cloud.google.com/anthos/docs/concepts/security-monitoring).

## Overview

When you use Binary Authorization to deploy a container image to Google Kubernetes Engine (GKE), GKE writes details about the deployment to the audit logs in Google Cloud Observability. These audit log entries include **enforcement status messages**. You can view these log entries in the Google Cloud console or at the command line using the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command.

For the searches later in this guide, you access Cloud Audit Logs and select the project with the events you want to view.

For _general access_ to Cloud Audit Logs, do the following:

  1. Go to the **Google Cloud Observability Logging > Logs** (Logs Explorer) page in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Choose the Google Cloud project for which you want to view Cloud Audit Logs.




## Enforcement status messages

GKE writes messages to the audit log for the following enforcement conditions:

  * **Blocked deployment** : Deployment was blocked due to Binary Authorization policy.
  * **Breakglass event** : Deployment bypassed policy check using breakglass mechanism. For more information, see [Using breakglass](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass).
  * **Fail open** : Deployment was allowed because Binary Authorization backend was unavailable.
  * **Dry run** : Deployment allowed with policy violations because dry run mode was set in the Binary Authorization policy.



## Blocked deployment events in Cloud Audit Logs

When a container image is blocked because it violates a Binary Authorization policy, you can find the blocked-deployment events in Cloud Audit Logs.

### Query Cloud Audit Logs for blocked deployment events

This section describes how to query Cloud Audit Logs for blocked deployment events.

###  Logs Explorer 

To view blocked deployment events in the Cloud Audit Logs Logs Explorer, do the following:

  1. Go to the [Logs Explorer page](https://console.cloud.google.com/logs/query).

  2. Enter the following query in the _search-query_ box:
         
         resource.type="k8s_cluster"
         logName:"cloudaudit.googleapis.com%2Factivity"
         (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
          protoPayload.methodName="io.k8s.core.v1.pods.update")
         protoPayload.response.status="Failure"
         (protoPayload.response.reason="VIOLATES_POLICY" OR
         protoPayload.response.reason="Forbidden")
         

  3. Select the time range in the _time-range selector_.




###  gcloud 

To view policy violation events from the past week in Cloud Audit Logs using the Google Cloud CLI, run the following command:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'resource.type="k8s_cluster"
       logName:"cloudaudit.googleapis.com%2Factivity"
       (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
        protoPayload.methodName="io.k8s.core.v1.pods.update")
       protoPayload.response.status="Failure"
       (protoPayload.response.reason="VIOLATES_POLICY" OR
       protoPayload.response.reason="Forbidden")'
    

**Note:** For Kubernetes master versions 1.18.15 and later, 1.19.7 and later, and 1.20.2 and later, `protoPayload.response.reason` is set to `VIOLATES_POLICY`.

## Breakglass events in Cloud Audit Logs

Binary Authorization enables you to override the policy using a [_breakglass_](https://docs.cloud.google.com/binary-authorization/docs/deploying-containers#override_a_policy) label in the Pod specification. When images are deployed with breakglass, Binary Authorization logs breakglass events in Cloud Audit Logs. The following section describes how you can query for these events.

### Query Cloud Audit Logs for pods with breakglass specified

###  Logs Explorer 

To view breakglass events in the Cloud Audit Logs Logs Explorer, do the following:

  1. Go to the [Logs Explorer page](https://console.cloud.google.com/logs/query).

  2. Enter the following in the _search-query_ box:
         
         resource.type="k8s_cluster"
         logName:"cloudaudit.googleapis.com%2Factivity"
         (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
         protoPayload.methodName="io.k8s.core.v1.pods.update")
         "image-policy.k8s.io/break-glass"
         

  3. Select the time range in the _time-range selector_.




###  gcloud 

To view breakglass events from the past week in Cloud Audit Logs using the the gcloud CLI, run the following command:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'resource.type="k8s_cluster" AND
      logName:"cloudaudit.googleapis.com%2Factivity" AND
      (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
        protoPayload.methodName="io.k8s.core.v1.pods.update") AND
      "image-policy.k8s.io/break-glass"'
    

## Fail open events in Cloud Audit Logs

Fail open occurs when a container image deployment is attempted, Binary Authorization enforcement is unavailable or times out, and the container image is allowed to deploy.

In this case, the verification result is unknown and a log entry is recorded.

### Query Cloud Audit Logs fail open events

###  Logs Explorer 

To view fail open events in the Cloud Audit Logs Logs Explorer, do the following:

  1. Go to the [Logs Explorer page](https://console.cloud.google.com/logs/query).

  2. Enter the following in the _search-query_ box:
         
         resource.type="k8s_cluster"
         logName:"cloudaudit.googleapis.com%2Factivity"
         (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
          protoPayload.methodName="io.k8s.core.v1.pods.update")
         ("image-policy.k8s.io/failed-open" OR
          "imagepolicywebhook.image-policy.k8s.io/failed-open" OR
          "failed-open.validating.webhook.admission.k8s.io")
         

  3. Select the time range in the _time-range selector_.




###  gcloud 

To view fail open events from the past week in Cloud Audit Logs using the gcloud CLI, run the following command:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'resource.type="k8s_cluster"
       logName:"cloudaudit.googleapis.com%2Factivity"
       (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
        protoPayload.methodName="io.k8s.core.v1.pods.update")
       ("image-policy.k8s.io/failed-open" OR
        "imagepolicywebhook.image-policy.k8s.io/failed-open" OR
        "failed-open.validating.webhook.admission.k8s.io")'
    

## Dry run events in Cloud Audit Logs

[Dry run mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#enforcement_modes) is an enforcement mode in a policy that enables non-conformant images to be deployed, but writes details about the deployment to the audit log. Dry run mode allows you to test a policy in your production environment before it goes into effect.

When a container image fails to pass the required checks in a policy, but is permitted to be deployed by dry run mode, Cloud Audit Logs contains `imagepolicywebhook.image-policy.k8s.io/dry-run: "true"`.

### Query Cloud Audit Logs for dry run events

###  Logs Explorer 

To view dry run events in the Cloud Audit Logs Logs Explorer, do the following:

  1. Go to the [Logs Explorer page](https://console.cloud.google.com/logs/query).

  2. Enter the following in the _search-query_ box:
         
         resource.type="k8s_cluster"
         logName:"cloudaudit.googleapis.com%2Factivity"
         (protoPayload.methodName="io.k8s.core.v1.pods.create" OR
          protoPayload.methodName="io.k8s.core.v1.pods.update")
         labels."imagepolicywebhook.image-policy.k8s.io/dry-run"="true"
         

  3. Select the time range in the _time-range selector_.




###  gcloud 

To view dry run deployment events from the past week in Cloud Audit Logs using the gcloud CLI, run the following command:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'labels."imagepolicywebhook.image-policy.k8s.io/dry-run"="true"'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
