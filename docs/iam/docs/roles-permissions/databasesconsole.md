---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole/
title: Studio Query roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:26:48.747324+00:00
---

# Studio Query roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Studio Query roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Studio Query. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Studio Query roles

Role | Permissions  
---|---  
  
#### Databasesconsole Editor Beta

(`roles/databasesconsole.editor`) Editor role for databasesconsole  |  `databasesconsole.databaseCenterViews.*`

  * `databasesconsole.databaseCenterViews.create`
  * `databasesconsole.databaseCenterViews.delete`
  * `databasesconsole.databaseCenterViews.search`
  * `databasesconsole.databaseCenterViews.update`

`databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.operations.*`

  * `databasesconsole.operations.cancel`
  * `databasesconsole.operations.delete`
  * `databasesconsole.operations.get`
  * `databasesconsole.operations.list`

`databasesconsole.studioQueries.create` `databasesconsole.studioQueries.delete` `databasesconsole.studioQueries.search` `databasesconsole.studioQueries.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Databasesconsole Viewer Beta

(`roles/databasesconsole.viewer`) Viewer role for databasesconsole  |  `databasesconsole.databaseCenterViews.search` `databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.operations.get` `databasesconsole.operations.list` `databasesconsole.studioQueries.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Studio Query Admin Beta

(`roles/databasesconsole.studioQueryAdmin`) Full access to Studio Query resources.  |  `databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.operations.*`

  * `databasesconsole.operations.cancel`
  * `databasesconsole.operations.delete`
  * `databasesconsole.operations.get`
  * `databasesconsole.operations.list`

`databasesconsole.studioQueries.*`

  * `databasesconsole.studioQueries.create`
  * `databasesconsole.studioQueries.delete`
  * `databasesconsole.studioQueries.get`
  * `databasesconsole.studioQueries.list`
  * `databasesconsole.studioQueries.search`
  * `databasesconsole.studioQueries.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Studio Query User Beta

(`roles/databasesconsole.studioQueryUser`) Access to create, update, search and delete studio queries.  |  `databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.operations.get` `databasesconsole.operations.list` `databasesconsole.studioQueries.create` `databasesconsole.studioQueries.delete` `databasesconsole.studioQueries.search` `databasesconsole.studioQueries.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Studio Query permissions

Permission | Included in roles  
---|---  
  
#### `databasesconsole.databaseCenterViews.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.admin) (`roles/databasecenter.admin`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)   
  
#### `databasesconsole.databaseCenterViews.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.admin) (`roles/databasecenter.admin`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)   
  
#### `databasesconsole.databaseCenterViews.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.admin) (`roles/databasecenter.admin`)  [Database Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.viewer) (`roles/databasecenter.viewer`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Databasesconsole Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.viewer) (`roles/databasesconsole.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databasesconsole.databaseCenterViews.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.admin) (`roles/databasecenter.admin`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)   
  
#### `databasesconsole.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Database Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.admin) (`roles/databasecenter.admin`)  [Database Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.viewer) (`roles/databasecenter.viewer`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Databasesconsole Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.viewer) (`roles/databasesconsole.viewer`)  [Cloud Datastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.admin) (`roles/datastore.admin`)  [Cloud Datastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.editor) (`roles/datastore.editor`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Cloud Datastore User](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.user) (`roles/datastore.user`)  [Cloud Datastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.viewer) (`roles/datastore.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [AlloyDB Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.databaseUser) (`roles/alloydb.databaseUser`)  [Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryUser) (`roles/databasesconsole.studioQueryUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `databasesconsole.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Database Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.admin) (`roles/databasecenter.admin`)  [Database Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.viewer) (`roles/databasecenter.viewer`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Databasesconsole Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.viewer) (`roles/databasesconsole.viewer`)  [Cloud Datastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.admin) (`roles/datastore.admin`)  [Cloud Datastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.editor) (`roles/datastore.editor`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Cloud Datastore User](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.user) (`roles/datastore.user`)  [Cloud Datastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.viewer) (`roles/datastore.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AlloyDB Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.databaseUser) (`roles/alloydb.databaseUser`)  [Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryUser) (`roles/databasesconsole.studioQueryUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `databasesconsole.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)   
  
#### `databasesconsole.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)   
  
#### `databasesconsole.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Databasesconsole Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.viewer) (`roles/databasesconsole.viewer`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryUser) (`roles/databasesconsole.studioQueryUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databasesconsole.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Databasesconsole Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.viewer) (`roles/databasesconsole.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryUser) (`roles/databasesconsole.studioQueryUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databasesconsole.studioQueries.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Cloud Datastore User](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.user) (`roles/datastore.user`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryUser) (`roles/databasesconsole.studioQueryUser`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `databasesconsole.studioQueries.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Cloud Datastore User](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.user) (`roles/datastore.user`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryUser) (`roles/databasesconsole.studioQueryUser`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `databasesconsole.studioQueries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `databasesconsole.studioQueries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `databasesconsole.studioQueries.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Databasesconsole Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.viewer) (`roles/databasesconsole.viewer`)  [Cloud Datastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.admin) (`roles/datastore.admin`)  [Cloud Datastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.editor) (`roles/datastore.editor`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Cloud Datastore User](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.user) (`roles/datastore.user`)  [Cloud Datastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.viewer) (`roles/datastore.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [AlloyDB Database User](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.databaseUser) (`roles/alloydb.databaseUser`)  [Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryUser) (`roles/databasesconsole.studioQueryUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `databasesconsole.studioQueries.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)  [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)  [Databasesconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.editor) (`roles/databasesconsole.editor`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Cloud Datastore User](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.user) (`roles/datastore.user`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryAdmin) (`roles/databasesconsole.studioQueryAdmin`)  [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole#databasesconsole.studioQueryUser) (`roles/databasesconsole.studioQueryUser`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
