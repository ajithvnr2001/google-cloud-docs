---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations/
title: Storage Batch Operations roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:07:00.929070+00:00
---

# Storage Batch Operations roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Storage Batch Operations roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Storage Batch Operations. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Storage Batch Operations roles

Role | Permissions  
---|---  
  
#### Storage Batch Operations Admin 

(`roles/storagebatchoperations.admin`) Full access to Storage Batch Operations resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storagebatchoperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`
  * `storagebatchoperations.jobs.cancel`
  * `storagebatchoperations.jobs.create`
  * `storagebatchoperations.jobs.delete`
  * `storagebatchoperations.jobs.get`
  * `storagebatchoperations.jobs.list`
  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`
  * `storagebatchoperations.operations.cancel`
  * `storagebatchoperations.operations.delete`
  * `storagebatchoperations.operations.get`
  * `storagebatchoperations.operations.list`

  
  
#### Storage Batch Operations Viewer 

(`roles/storagebatchoperations.viewer`) Read-only access to Storage Batch Operations resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storagebatchoperations.bucketOperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`

`storagebatchoperations.jobs.get` `storagebatchoperations.jobs.list` `storagebatchoperations.locations.*`

  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`

`storagebatchoperations.operations.get` `storagebatchoperations.operations.list`  
  
## Storage Batch Operations permissions

Permission | Included in roles  
---|---  
  
#### `storagebatchoperations.bucketOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Storage Batch Operations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.viewer) (`roles/storagebatchoperations.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.bucketOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Storage Batch Operations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.viewer) (`roles/storagebatchoperations.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.jobs.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.jobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.jobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.jobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Storage Batch Operations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.viewer) (`roles/storagebatchoperations.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.jobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Storage Batch Operations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.viewer) (`roles/storagebatchoperations.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Storage Batch Operations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.viewer) (`roles/storagebatchoperations.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Storage Batch Operations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.viewer) (`roles/storagebatchoperations.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Storage Batch Operations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.viewer) (`roles/storagebatchoperations.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `storagebatchoperations.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Storage Batch Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.admin) (`roles/storagebatchoperations.admin`)  [Storage Batch Operations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagebatchoperations#storagebatchoperations.viewer) (`roles/storagebatchoperations.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
