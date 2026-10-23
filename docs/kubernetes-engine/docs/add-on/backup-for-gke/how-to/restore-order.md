---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-order/
title: Specify resource restore ordering during restoration \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:27.770470+00:00
---

# Specify resource restore ordering during restoration  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Specify resource restore ordering during restoration Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to specify the order in which Backup for GKE should restore different GroupKinds during a restore operation.

## Overview

By default, Backup for GKE restores well-known GroupKinds in an order that fulfills dependency requirements among resources. However, if there are additional resources that need restoring in a specific order, you can use the restore ordering feature to specify the required order by defining dependencies between the affected resources.

During a restore plan create or update operation, you can specify a list of custom GroupKind dependencies. To represent a dependency between two custom resources, specify the following two GroupKinds:

  * Satisfying GroupKind: this GroupKind satisfies the dependencies and must be restored before the requiring GroupKind. In the Google Cloud console, this GroupKind is termed as the **First API group** and **First object kind** fields.
  * Requiring GroupKind: this GroupKind depends on the satisfying GroupKind to be restored first. In the Google Cloud console, this GroupKind is termed as the **Second API group** and **Second object kind** fields.



Backup for GKE takes a list of custom dependencies and the default dependencies and combines them to generate a GroupKind restore order.

## Default dependencies

The following table lists the default pairing dependencies between satisfying and requiring GroundKind resources. When defining a restoring order, Backup for GKE restores all satisfying GroundKinds before Requiring GroupKinds. For example, Backup for GKE always restores all `storage.k8s.io/StorageClass` before `PersistentVolumeClaims`.

The default restore ordering also handles basic cases, such as restoring namespaces before all namespaced resources and restoring `CustomResourceDefinitions` before any `CustomResources`.

**Satisfying GroundKind resource** | **Requiring GroundKind resource**  
---|---  
flowcontrol.apiserver.k8s.io/PriorityLevelConfiguration | flowcontrol.apiserver.k8s.io/FlowSchema  
storage.k8s.io/StorageClass | PersistentVolumeClaim  
PersistentVolumeClaim | 

  * Pod


  * Deployment


  * ReplicationController


  * ReplicaSet


  * StatefulSet


  * DaemonSet


  * CronJob


  * Job

  
ServiceAccount | 

  * Pod


  * Deployment


  * ReplicationController


  * ReplicaSet


  * StatefulSet


  * DaemonSet


  * CronJob


  * Job

  
  
## Define resource restore ordering

Use the following instructions to add custom GroupKind dependencies to a restore plan. Refer to the list of default dependencies for all GroupKind dependencies that are already handled by Backup for GKE and don't need to be specified.

### gcloud

  1. Create a YAML file to define restore order. You can use the following YAML example.

The following example indicates that `stable.example.com/First` must be restored before `stable.example.com/Second` and that `stable.example.com/Second` must be restored before `stable.example.com/Third`.
         
         groupKindDependencies:
           - satisfying:
               resourceGroup: stable.example.com
               resourceKind: First
             requiring:
               resourceGroup: stable.example.com
               resourceKind: Second
           - satisfying:
               resourceGroup: stable.example.com
               resourceKind: Second
             requiring:
               resourceGroup: stable.example.com
               resourceKind: Third
         

  2. Define a restore order using the restore order file you created.
         
         gcloud beta container backup-restore restore-plans update RESTORE_PLAN \
             --project=PROJECT_ID \
             --location=LOCATION \
             --restore-order-file=RESTORE_ORDER_FILE
         

Replace the following:



  * `RESTORE_PLAN`: the name of the restore plan that you want to update.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the compute region of the parent restore plan.
  * `RESTORE_ORDER_FILE`: the path to the YAML file containing the GroupKind dependencies, as shown in the earlier example.



### Console

Use the following instructions to add order to an existing restore plan in the Google Cloud console:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restore plans** tab.

  4. Click the restore plan name.

  5. Click the **Details** tab.

  6. Click **Edit** that is next to the **Restore order**.

  7. Click **Add order set**.

  8. In the Item 1 section, enter **First API group 1** and **First object kind 1** followed by **Second API group 2** and **Second object kind 2** the order in which the resources to be restored.

  9. Click **Save changes**.




## What's next

  * Learn more about [restoring a backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
