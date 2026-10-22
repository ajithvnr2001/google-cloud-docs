---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/automl/
title: AutoML roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:54.414076+00:00
---

# AutoML roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/automl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  AutoML roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for AutoML. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## AutoML roles

Role | Permissions  
---|---  
  
#### AutoML Admin Beta

(`roles/automl.admin`) Full access to all AutoML resources  Lowest-level resources where you can grant this role:

  * Dataset 
  * Model 

|  `automl.*`

  * `automl.annotationSpecs.create`
  * `automl.annotationSpecs.delete`
  * `automl.annotationSpecs.get`
  * `automl.annotationSpecs.list`
  * `automl.annotationSpecs.update`
  * `automl.annotations.approve`
  * `automl.annotations.create`
  * `automl.annotations.list`
  * `automl.annotations.manipulate`
  * `automl.annotations.reject`
  * `automl.columnSpecs.get`
  * `automl.columnSpecs.list`
  * `automl.columnSpecs.update`
  * `automl.datasets.create`
  * `automl.datasets.delete`
  * `automl.datasets.export`
  * `automl.datasets.get`
  * `automl.datasets.getIamPolicy`
  * `automl.datasets.import`
  * `automl.datasets.list`
  * `automl.datasets.setIamPolicy`
  * `automl.datasets.update`
  * `automl.examples.delete`
  * `automl.examples.get`
  * `automl.examples.list`
  * `automl.examples.update`
  * `automl.files.delete`
  * `automl.files.list`
  * `automl.humanAnnotationTasks.create`
  * `automl.humanAnnotationTasks.delete`
  * `automl.humanAnnotationTasks.get`
  * `automl.humanAnnotationTasks.list`
  * `automl.locations.get`
  * `automl.locations.getIamPolicy`
  * `automl.locations.list`
  * `automl.locations.setIamPolicy`
  * `automl.modelEvaluations.create`
  * `automl.modelEvaluations.get`
  * `automl.modelEvaluations.list`
  * `automl.models.create`
  * `automl.models.delete`
  * `automl.models.deploy`
  * `automl.models.export`
  * `automl.models.get`
  * `automl.models.getIamPolicy`
  * `automl.models.list`
  * `automl.models.predict`
  * `automl.models.setIamPolicy`
  * `automl.models.undeploy`
  * `automl.operations.cancel`
  * `automl.operations.delete`
  * `automl.operations.get`
  * `automl.operations.list`
  * `automl.tableSpecs.get`
  * `automl.tableSpecs.list`
  * `automl.tableSpecs.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### AutoML Editor Beta

(`roles/automl.editor`) Editor of all AutoML resources  Lowest-level resources where you can grant this role:

  * Dataset 
  * Model 

|  `automl.annotationSpecs.*`

  * `automl.annotationSpecs.create`
  * `automl.annotationSpecs.delete`
  * `automl.annotationSpecs.get`
  * `automl.annotationSpecs.list`
  * `automl.annotationSpecs.update`

`automl.annotations.*`

  * `automl.annotations.approve`
  * `automl.annotations.create`
  * `automl.annotations.list`
  * `automl.annotations.manipulate`
  * `automl.annotations.reject`

`automl.columnSpecs.*`

  * `automl.columnSpecs.get`
  * `automl.columnSpecs.list`
  * `automl.columnSpecs.update`

`automl.datasets.create` `automl.datasets.delete` `automl.datasets.export` `automl.datasets.get` `automl.datasets.import` `automl.datasets.list` `automl.datasets.update` `automl.examples.*`

  * `automl.examples.delete`
  * `automl.examples.get`
  * `automl.examples.list`
  * `automl.examples.update`

`automl.files.*`

  * `automl.files.delete`
  * `automl.files.list`

`automl.humanAnnotationTasks.*`

  * `automl.humanAnnotationTasks.create`
  * `automl.humanAnnotationTasks.delete`
  * `automl.humanAnnotationTasks.get`
  * `automl.humanAnnotationTasks.list`

`automl.locations.get` `automl.locations.list` `automl.modelEvaluations.*`

  * `automl.modelEvaluations.create`
  * `automl.modelEvaluations.get`
  * `automl.modelEvaluations.list`

`automl.models.create` `automl.models.delete` `automl.models.deploy` `automl.models.export` `automl.models.get` `automl.models.list` `automl.models.predict` `automl.models.undeploy` `automl.operations.*`

  * `automl.operations.cancel`
  * `automl.operations.delete`
  * `automl.operations.get`
  * `automl.operations.list`

`automl.tableSpecs.*`

  * `automl.tableSpecs.get`
  * `automl.tableSpecs.list`
  * `automl.tableSpecs.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### AutoML Viewer Beta

(`roles/automl.viewer`) Viewer of all AutoML resources  Lowest-level resources where you can grant this role:

  * Dataset 
  * Model 

|  `automl.annotationSpecs.get` `automl.annotationSpecs.list` `automl.annotations.list` `automl.columnSpecs.get` `automl.columnSpecs.list` `automl.datasets.get` `automl.datasets.list` `automl.examples.get` `automl.examples.list` `automl.files.list` `automl.humanAnnotationTasks.get` `automl.humanAnnotationTasks.list` `automl.locations.get` `automl.locations.list` `automl.modelEvaluations.get` `automl.modelEvaluations.list` `automl.models.get` `automl.models.list` `automl.operations.get` `automl.operations.list` `automl.tableSpecs.get` `automl.tableSpecs.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### AutoML Predictor Beta

(`roles/automl.predictor`) Predict using models  Lowest-level resources where you can grant this role:

  * Model 

|  `automl.models.predict` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### AutoML Service Agent 

(`roles/automl.serviceAgent`) AutoML service agent can act as Cloud Storage admin and export BigQuery tables, which can be backed by Cloud Storage and Cloud Bigtable.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.tables.create` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.update` `bigquery.tables.updateData` `bigtable.tables.get` `bigtable.tables.list` `bigtable.tables.readRows` `serviceusage.services.use` `storage.buckets.get` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## AutoML permissions

Permission | Included in roles  
---|---  
  
#### `automl.annotationSpecs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotationSpecs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotationSpecs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotationSpecs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotationSpecs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotations.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotations.manipulate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.annotations.reject`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.columnSpecs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.columnSpecs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.columnSpecs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.datasets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.datasets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.datasets.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.datasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.datasets.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `automl.datasets.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.datasets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.datasets.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)   
  
#### `automl.datasets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.examples.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.examples.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.examples.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.examples.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.files.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.files.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.humanAnnotationTasks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.humanAnnotationTasks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.humanAnnotationTasks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.humanAnnotationTasks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.locations.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `automl.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.locations.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)   
  
#### `automl.modelEvaluations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.modelEvaluations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.modelEvaluations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.models.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.models.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.models.deploy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.models.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.models.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Cloud Translation API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.admin) (`roles/cloudtranslate.admin`)  [Cloud Translation API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.editor) (`roles/cloudtranslate.editor`)  [Cloud Translation API User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.user) (`roles/cloudtranslate.user`)  [Cloud Translation API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.viewer) (`roles/cloudtranslate.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Translation Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.admin) (`roles/translationhub.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Translation Hub Portal User](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.portalUser) (`roles/translationhub.portalUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.models.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `automl.models.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Translation Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.admin) (`roles/translationhub.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Translation Hub Portal User](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.portalUser) (`roles/translationhub.portalUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.models.predict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Cloud Translation API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.admin) (`roles/cloudtranslate.admin`)  [Cloud Translation API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.editor) (`roles/cloudtranslate.editor`)  [Cloud Translation API User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.user) (`roles/cloudtranslate.user`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Translation Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.admin) (`roles/translationhub.admin`)  [AutoML Predictor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.predictor) (`roles/automl.predictor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Translation Hub Portal User](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.portalUser) (`roles/translationhub.portalUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [DocumentAI Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent) (`roles/documentaicore.serviceAgent`) 

  
  
#### `automl.models.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)   
  
#### `automl.models.undeploy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Cloud Translation API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent) (`roles/cloudtranslate.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.tableSpecs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.tableSpecs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [AutoML Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.viewer) (`roles/automl.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `automl.tableSpecs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AutoML Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.admin) (`roles/automl.admin`)  [AutoML Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automl#automl.editor) (`roles/automl.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
