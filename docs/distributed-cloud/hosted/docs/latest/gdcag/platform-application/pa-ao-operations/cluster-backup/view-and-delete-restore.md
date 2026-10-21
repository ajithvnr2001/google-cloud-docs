---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/view-and-delete-restore/
title: View and delete a restore \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:10:23.936869+00:00
---

# View and delete a restore  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/view-and-delete-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View and delete a restore Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view and delete an existing restore in Google Distributed Cloud (GDC) air-gapped.

Delete unused restores to free up storage space and reduce clutter.

## Before you begin

Ensure you have an existing restore. For more information, see [Plan a set of restores](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-restores).

### Request IAM roles

To view and delete a restore, ask your Organization IAM Admin or Project IAM Admin to grant you one of the following roles:

  * **User Cluster Backup Admin** (`user-cluster-backup-admin`): creates, gets, lists, watches, updates, patches, and deletes backup resources such as backup and restore plans in user clusters. Contact your Organization IAM Admin to request this role.

  * **Backup Creator** (`backup-creator`): creates, gets, lists, watches, updates, patches, and deletes manual backup requests and manual restore requests. Contact your Project IAM Admin to request this role.




## View a restore

View a list of restores using the GDC console or `kubectl`.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** to select an organization or project depending on your role:
  4. Backup Admin: Select an organization to see all of the restores in an organization or select a project to see all of the restores in a project.
  5. Backup Creator: Select a project to see all of the restores in a project.
  6. Click the **Restores** tab.
  7. Click a restore in the list to view its details.



### kubectl

View the status of a restore in the default namespace:
    
    
    kubectl get clusterRestores
    

Here's an example of the output:
    
    
    NAME                   STATE
    restore-sample         Succeeded
    

View restores in all namespaces:
    
    
    kubectl get clusterRestores -A
    

View restores in a specific namespace:
    
    
    kubectl get clusterRestores -n NAMESPACE
    

Replace `NAMESPACE` with the namespace containing the restores.

## Delete a restore

Unlike backups, deleting a restore doesn't require issuing a request. Restores are deleted by deleting the resource directly from the Kubernetes API server. This action also cleans up any associated restore artifacts from object storage.

  * To delete a restore, use `kubectl`:
        
        kubectl delete clusterRestores RESTORE_NAME
        

Replace `RESTORE_NAME` with the name of the restore.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
