---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging/
title: Audit logging \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:01.854832+00:00
---

# Audit logging  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/audit-logging)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/audit-logging)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



## Overview

Google Distributed Cloud supports audit logging at both the Cloud API and Kubernetes cluster level. This document provides information about Kubernetes cluster audit logging. For information about Cloud API audit logging, see [Cloud API audit logging information](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging-api).

Google Distributed Cloud makes use of [Kubernetes Audit Logging](https://kubernetes.io/docs/tasks/debug-application-cluster/audit/), which keeps a chronological record of calls made to a cluster's Kubernetes API server. Audit logs are useful for investigating suspicious API requests and for collecting statistics.

You can configure a cluster to write audit logs to disk or to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) in a Google Cloud project. Writing to Cloud Audit Logs has several benefits over writing to disk, or even capturing logs in an on-premises logging system:

  * Audit logs for all GKE clusters can be centralized.
  * Log entries written to Cloud Audit Logs are immutable.
  * Cloud Audit Logs entries are retained for 400 days.
  * Cloud Audit Logs is included in the price of Anthos.



### Disk-based audit logging

By default, audit logs are written to a persistent disk so that VM restarts and upgrades don't cause the logs to disappear. Google Distributed Cloud retains up to 12 GB of audit log entries.

### Cloud Audit Logs

If you enable Cloud Audit Logs for a cluster, then Admin Activity audit log entries from the cluster's Kubernetes API server are sent to Google Cloud, using the Google Cloud project that you specify in the `cloudAuditLogging.projectID` field of your cluster configuration file. This Google Cloud project is called your [audit logging project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multiple-gcp-projects#audit_logging_project).

Your audit logging project must be the same as your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multiple-gcp-projects#fleet_host_project).

When you enable Cloud Audit Logs, Google Distributed Cloud disables disk-based audit logging.

To buffer and write log entries to Cloud Audit Logs, Google Distributed Cloud deploys an `audit-proxy` Pod to the admin cluster. This component is also available as a sidecar container on user clusters.

#### Limitations

The current version of Cloud Audit Logs for Google Distributed Cloud has several limitations:

  * Data access (get, list, watch requests) logging is not supported.

  * Modifying the Kubernetes audit policy is not supported.

  * Cloud Audit Logs is not resilient to extended network outages. If the log entries cannot be exported to Google Cloud, they are cached in a 10G disk buffer. If that buffer fills, then subsequent entries are dropped.




## Enable the Anthos Audit API

Enable the Anthos Audit API in your audit logging project.

[Enable the Anthos Audit API](https://console.cloud.google.com/apis/library/anthosaudit.googleapis.com)

## Create a service account for Cloud Audit Logs

You already have one or more [service accounts](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts) that you created to use with Google Distributed Cloud. For this feature, you need to create an additional service account called the [audit logging service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#audit_logging_service_account).

  1. Create your audit logging service account:
         
         gcloud iam service-accounts create audit-logging-service-account

  2. Create a JSON key file for your Cloud Audit Logs service account:
         
         gcloud iam service-accounts keys create audit-logging-key.json \
            --iam-account AUDIT_LOGGING_SERVICE_ACCOUNT_EMAIL
         

where AUDIT_LOGGING_SERVICE_ACCOUNT_EMAIL is the email address of your service account.

  3. Save `audit-logging-key.json` on the admin workstation in the same location as your other service account keys.




## Create an admin cluster with Cloud Audit Logs enabled

You can enable Cloud Audit Logs for an admin cluster only when you first create the admin cluster. You cannot modify an existing admin cluster to enable Cloud Audit Logs.

  1. Refer to [Creating an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-cluster).

  2. In your admin cluster configuration file, fill in the `cloudAuditLogging` section.

  3. Set `cloudAuditLogging.projectID` to the ID of your audit logging project.

  4. Set `cloudAuditLogging.clusterLocation` to a Google Cloud region where you want to store audit logs. For improved latency, choose a region that is near your on-premises data center.

  5. Set `cloudAuditLogging.serviceAccountKeyPath` to the path of the JSON key file for your audit logging service account.




For example:
    
    
    cloudAuditLogging:
      projectID: "my-project"
      clusterLocation: "us-west1"
      serviceAccountKeyPath: "/my-key-folder/audit-logging-key.json"
    

Continue the cluster creation as usual.

## Create a user cluster with Cloud Audit Logs enabled

  1. Refer to [Creating a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster).

  2. In your user cluster configuration file, fill in the `cloudAuditLogging` section.

  3. Set `cloudAuditLogging.projectID` to the ID of your audit logging project.

  4. Set `cloudAuditLogging.clusterLocation` to a Google Cloud region where you want to store audit logs. For improved latency, choose a region that is near your on-premises data center.

  5. Set `cloudAuditLogging.serviceAccounKeyPath` to the path of the JSON key file for your Cloud Audit Logs service account.

  6. Ensure that the `gkeConnect` section is filled in and `gkeConnect.projectID` is the same as `cloudAuditLogging.projectID`.




For example:
    
    
    gkeConnect:
      projectID: "my-project"
      registerServiceAccountKeyPath: "/my-key-fokder/connect-register-key.json"
    
    cloudAuditLogging:
      projectID: "my-project"
      clusterLocation: "us-west1"
      serviceAccountKeyPath: "/my-key-folder/audit-logging-key.json"
    

Continue the cluster creation as usual.

## Enable Cloud Audit Logs for an existing user cluster

Cloud Audit Logs can be enabled only in the Google Cloud project where the user cluster is registered.

If an existing user cluster is not registered, register it by following these steps before you enable Cloud Audit Logs:

  1. Add a `gkeConnect` section to the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#gkeconnect-section). For example:
         
         gkeConnect:
           projectID: "my-project"
           registerServiceAccountKeyPath: "/my-key-fokder/connect-register-key.json"
         

  2. Update the cluster:
         
         gkectl update cluster --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




After the user cluster is registered, follow these steps to enable Cloud Audit Logs:

  1. Fill in the `cloudAuditLogging` section of your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#cloudauditlogging-section). See Create a user cluster with Cloud Audit Logs enabled for details on the individual fields. The `projectID` in the `cloudAuditLogging` section must be the same as that in the `gkeConnect` section.

  2. Update the cluster:
         
         gkectl update cluster --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




## Disable Cloud Audit Logs for an existing user cluster

  1. In the user cluster configuration file, delete the `cloudAuditLogging` section.

  2. Update the user cluster:



    
    
    gkectl update cluster --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] --config [USER_CLUSTER_CONFIG] 
    

## Access audit logs

### Disk-based audit logging

You can find the audit logs for the admin cluster on the control-plane nodes under `/var/log/kube-audit/kube-apiserver-audit.log`. The audit logs for the user cluster are in the `PersistentVolumeClaim` named `kube-audit-kube-apiserver-0`. You can access this data within your own Pods via `volumes` entries:

Add this entry for the **admin cluster** : 
    
    
        volumes:
        - name: kube-audit
          hostPath:
            path: /var/log/kube-audit
            type: ""
    

Add this entry for the **user cluster** : 
    
    
        volumes:
        - name: kube-audit
          persistentVolumeClaim:
            claimName: kube-audit-kube-apiserver-0
    

To schedule your Pod on the appropriate **admin cluster** node (and only this node) you will need to add `nodeSelector` and `tolerations` sections to your Pod spec, like this:
    
    
        spec:
          nodeSelector:
            node-role.kubernetes.io/master: ''
          tolerations:
          - key: node-role.kubernetes.io/master
            value: ""
            effect: NoSchedule
    

For the **user cluster** , set `namespace` as the user cluster name, then set `nodeName` to the same as `kube-apiserver-0`:
    
    
       spec:
         nodeName: NODE_NAME
    

To point out the `nodeName` of `kube-apiserver-0`, run the following command:
    
    
    kubectl get pod kube-apiserver-0 -n USER_CLUSTER_NAME --kubeconfig kubeconfig -o jsonpath='{.spec.nodeName}'
    

Each audit log's filename has a timestamp that indicates when the file was rotated. A file contains audit logs up to that time and date.

### Cloud Audit Logs

### Console

  1. In the Google Cloud console, go to the **Logs** page in the **Logging** menu.

[Go to the Logs page](https://console.cloud.google.com/logs/viewer)

  2. In the **Filter by label or text search** box, just above the drop-down menus discussed above, click the down arrow to open the drop-down menu. From the menu, choose **Convert to advanced filter**.

  3. Fill the text box with the following filter:
         
         resource.type="k8s_cluster"
         logName="projects/PROJECT_ID/logs/externalaudit.googleapis.com%2Factivity"
         protoPayload.serviceName="anthosgke.googleapis.com"
         

  4. Click **Submit Filter** to display all audit logs from Google Distributed Cloud clusters that were configured to log in to this project.




### gcloud

List the first two log entries in your project's Admin Activity log that apply to the `k8s_cluster` resource type:
    
    
    gcloud logging read \
        'logName="projects/PROJECT_ID/logs/externalaudit.googleapis.com%2Factivity" \
        AND resource.type="k8s_cluster" \
        AND protoPayload.serviceName="anthosgke.googleapis.com" ' \
        --limit 2 \
        --freshness 300d
    

where PROJECT_ID is your project ID.

The output shows two log entries. Notice that for each log entry, the `logName` field has the value `projects/PROJECT_ID/logs/externalaudit.googleapis.com%2Factivity` and `protoPayload.serviceName` is equal to `anthosgke.googleapis.com`.

## Audit policy

Cloud Audit Logs behavior is determined by a statically-configured Kubernetes audit logging policy. Changing this policy is currently not supported, but will be available in a future release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
