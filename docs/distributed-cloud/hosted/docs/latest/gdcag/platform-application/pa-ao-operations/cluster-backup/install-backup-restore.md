---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/install-backup-restore/
title: Install backup and restore components \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:13.759650+00:00
---

# Install backup and restore components  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/install-backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Install backup and restore components Stay organized with collections  Save and categorize content based on your preferences. 

This document contains the steps you must follow to install and configure the components that are necessary to backup and restore your workloads in Google Distributed Cloud (GDC) air-gapped.

## Before you begin

Ensure you have the following items pre-configured:

  * An S3 endpoint and bucket on GDC object storage with an S3 access key ID and secret access key.
  * A working cluster. ### Request IAM roles



To verify and work with backup and restore components, ask your IAM Org Admin or IAM Project Admin to grant you one of the following roles:

  * **User Cluster Backup Admin** (`user-cluster-backup-admin`): creates, gets, lists, watches, updates, patches, and deletes backup resources such as backup plans, restore plans, and backup repositories in user clusters. Contact your IAM Org Admin to request this role.

  * **Backup Creator** (`backup-creator`): creates, gets, lists, watches, updates, patches, and deletes manual backup requests and manual restore requests. Contact your IAM Project Admin to request this role.




## Verify backup and restore installation

Verify that the `gpcbackup` control plane and agent are both running for the cluster you want to back up:
    
    
    kubectl get pods -n gpc-backup-system
    

After running the command, the output looks like the following example. There should be two pods running, a control plane pod and an agent pod:
    
    
    NAME                                                READY   STATUS    RESTARTS   AGE
    gpcbackup-agent-0                                   1/1     Running   2          64m
    gpcbackup-controlplane-controller-6fc9485ff-jdk95   1/1     Running   0          64m
    

## What's next

  * [Add a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/add-backup-repository)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
