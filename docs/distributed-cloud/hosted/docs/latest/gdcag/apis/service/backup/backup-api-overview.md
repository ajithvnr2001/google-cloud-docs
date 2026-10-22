---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/backup/backup-api-overview/
title: Backup API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:41.196612+00:00
---

# Backup API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/backup/backup-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Backup API overview Stay organized with collections  Save and categorize content based on your preferences. 

Kubernetes was designed for extensibility. You can add new APIs such as the Backup and GKE Backup Agent APIs to a Kubernetes cluster. These APIs conform to a uniform API model, the Kubernetes Resource Model (KRM).

These APIs use Kubernetes custom resources and rely on the KRM. The APIs are used to manage the lifecycle of backups, and to create backup repositories, policies, and plans.

## Service endpoints

The following URL is the API endpoint for the Backup KRM API:
    
    
    https://MANAGEMENT_API_SERVER_ENDPOINT/apis/backup.gdc.goog/v1
    

The following URL is the API endpoint for the GKE Backup Agent API:
    
    
    https://MANAGEMENT_API_SERVER_ENDPOINT/apis/gkebackup.gke.io/v1
    

Replace `MANAGEMENT_API_SERVER_ENDPOINT` with the endpoint of the Management API server.

## Discovery document

Use the `kubectl proxy --port=8001` command to open a proxy to the API server on your local machine. From there, you can access the discovery document at one of the following URLs:

  * `http://127.0.0.1:8001/apis/backup.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/gkebackup.gke.io/v1`



## Example `ClusterBackupPlan` resource

Here is an example of a `ClusterBackupPlan` resource:
    
    
    apiVersion: backup.gdc.goog/v1
    kind: ClusterBackupPlan
    metadata:
      name: backup-plan
      namespace: project-namespace
    spec:
      targetCluster:
        targetClusterType: UserCluster
        targetClusterName:
          kind: "Cluster"
          name: "cluster-sample"
      backupSchedule:
        cronSchedule: "*/30 * * * *"
        paused: false
      clusterBackupConfig:
        backupScope:
          selectedNamespaces:
            namespaces: ["nginx"]
        clusterBackupRepositoryName: backup-repository
      retentionPolicy:
        backupDeleteLockDays: 10
        backupRetainDays: 10
    

## Example `ProtectedApplication` resource

Here is an example of a `ProtectedApplication` resource:
    
    
    apiVersion: gkebackup.gke.io/v1
    kind: ProtectedApplication
    metadata:
      name: protected-application-test
      namespace: applications
    spec:
      applicationName: protectedApplication
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: protected
      components:
        - name: protect-application-deployment
          resourceKind: Deployment
          resourceNames:
            - protected-application-deployment
          strategy:
            type: BackupAllRestoreAll
    

## Example `ClusterBackupRepository` resource

Here is an example of a `ClusterBackupRepository` resource:
    
    
    apiVersion: backup.gdc.goog/v1
    kind: ClusterBackupRepository
    metadata:
      name: user-1-user
      namespace: user-1-user-cluster
    spec:
        secretReference:
            namespace: "object-storage-secret-ns"
            name: "object-storage-secret"
        endpoint: "https://objectstorage.google.gdch.test"
        type: "S3"
        s3Options:
          bucket: "fully-qualified-bucket-name"
          region: "us-east1"
          forcePathStyle: true
        importPolicy: "ReadWrite"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
