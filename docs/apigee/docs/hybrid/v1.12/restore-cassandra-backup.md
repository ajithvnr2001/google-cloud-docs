---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-backup/
title: Cassandra restore overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:49:50.680034+00:00
---

# Cassandra restore overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Cassandra restore overview Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/restore-cassandra-backup.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/restore-cassandra-backup.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/restore-cassandra-backup.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/restore-cassandra-backup.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/restore-cassandra-backup.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-backup.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/restore-cassandra-backup.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/restore-cassandra-backup.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/restore-cassandra-backup.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/restore-cassandra-backup.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/restore-cassandra-backup.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/restore-cassandra-backup.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/restore-cassandra-backup.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/restore-cassandra-backup.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/restore-cassandra-backup.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/restore-cassandra-backup.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/restore-cassandra-backup.html)



This page provides an overview of restoring Cassandra in Apigee hybrid.

## Why use restore?

You can use [backups](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-backup-overview) to restore Apigee infrastructure from the ground up in the event of catastrophic failures, such as irrecoverable data loss in your Apigee hybrid instance from a disaster. Restoration takes your data from the backup location and restores the data into a new Cassandra cluster with the same number of nodes. No cluster data is taken from the old Cassandra cluster. The goal of the restoration process is to bring an Apigee hybrid installation back to a previously operational state using backup data from a snapshot.

The use of backups to restore is not recommended for the following scenarios: 

  * Cassandra node failures.
  * Accidental deletion of data like `apps`, `developers`, and `api_credentials`.
  * One or more regions going down in a multi-region hybrid deployment.



Apigee Cassandra deployments and operational architecture take care of redundancy and fault tolerance for a single region. In most cases, the recommended multi-region production implementation of hybrid means that a region failure can be recovered from another live region using [region decommissioning and expansion procedures](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-backup/) instead of restoring from a backup.

Before you begin implementing a restore from a Cassandra backup, be aware of the following: 

  * **Downtime:** There will be downtime for the duration of the restoration. 
  * **Data loss:** There will be data loss between the last valid backup and the time the restoration is complete. 
  * **Restoration time:** Restoration time depends on the size of the data and cluster. 
  * **Cherry-picking data:** You cannot select only specific data to restore. Restoration restores the entire backup you select. 

**Note:** When restoring an Apigee hybrid installation from backup, ensure that the backup file is created from the same hybrid version as the installation. For example, if you have a backup file created from Apigee hybrid 1.5.x, use it to restore only an Apigee hybrid 1.5.x installation. If there is a version mismatch between the backup file and the hybrid installation, the restoration might not work and Apigee does not support any issues that arise because of such restoration. 

## Multi-region restores

If you installed Apigee hybrid into multiple regions, you must check the overrides file for the region you are restoring to make sure the `cassandra:hostNetwork` is set to `false` before you perform the restoration. For more information, see [Restoring in multiple regions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-multi-region).

## Prerequisites

Check all the following prerequisites are successful. Investigate any prerequisite failures before proceeding with restoration. 

  1. Verify all Cassandra pods are up and running with the following command. 
         
         kubectl get pods -n apigee -l app=apigee-cassandra

Your output should look something like the following example: 
         
         NAME                         READY   STATUS    RESTARTS   AGE
         apigee-cassandra-default-0   1/1     Running   0          14m
         apigee-cassandra-default-1   1/1     Running   0          13m
         apigee-cassandra-default-2   1/1     Running   0          11m
         exampleuser@example hybrid-files %
               

  2. Verify the Cassandra statefulset shows all pods are running with the following command. 
         
         kubectl get sts -n apigee -l app=apigee-cassandra

Your output should look something like the following example: 
         
         NAME                       READY   AGE
         apigee-cassandra-default   3/3     15m
             

  3. Verify the ApigeeDatastore resource is in a _running_ state with the following command. 
         
         kubectl get apigeeds -n apigee

Your output should look something like the following example: 
         
         NAME      STATE     AGE
         default   running   16m
             

  4. Verify all Cassandra PVCs are in _Bound_ status with the following command. 
         
         kubectl get pvc -n apigee -l app=apigee-cassandra

Your output should look something like the following example: 
         
         NAME                                        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
         cassandra-data-apigee-cassandra-default-0   Bound    pvc-a14184e7-8745-4b30-8069-9d50642efe04   10Gi       RWO            standard-rwo   17m
         cassandra-data-apigee-cassandra-default-1   Bound    pvc-ed129dcb-4706-4bad-a692-ac7c78bad64d   10Gi       RWO            standard-rwo   15m
         cassandra-data-apigee-cassandra-default-2   Bound    pvc-faed0ad1-9019-4def-adcd-05e7e8bb8279   10Gi       RWO            standard-rwo   13m
             

  5. Verify all Cassandra PVs are in Bound status with the following command. 
         
         kubectl get pv -n apigee

Your output should look something like the following example: 
         
         NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                              STORAGECLASS   REASON   AGE
         pvc-a14184e7-8745-4b30-8069-9d50642efe04   10Gi       RWO            Delete           Bound    apigee/cassandra-data-apigee-cassandra-default-0   standard-rwo            17m
         pvc-ed129dcb-4706-4bad-a692-ac7c78bad64d   10Gi       RWO            Delete           Bound    apigee/cassandra-data-apigee-cassandra-default-1   standard-rwo            16m
         pvc-faed0ad1-9019-4def-adcd-05e7e8bb8279   10Gi       RWO            Delete           Bound    apigee/cassandra-data-apigee-cassandra-default-2   standard-rwo            14m
             

  6. Verify the Apigee Controller resource is in Running status with the following command. 
         
         kubectl get pods -n apigee-system -l app=apigee-controller

Your output should look something like the following example: 
         
         NAME                                         READY   STATUS    RESTARTS   AGE
         apigee-controller-manager-856d9bb7cb-cfvd7   2/2     Running   0          20m
             




## How to restore?

Cassandra's restoration steps differ slightly depending on whether your Apigee hybrid is deployed in a single region or multiple regions. For the detailed restoration steps, see the following documentation:

  * [Restoring in a single region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-single-region)
  * [Restoring in a multi-region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-multi-region)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
