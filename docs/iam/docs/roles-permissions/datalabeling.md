---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling/
title: AI Platform Data Labeling Service roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:26.756423+00:00
---

# AI Platform Data Labeling Service roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  AI Platform Data Labeling Service roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for AI Platform Data Labeling Service. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## AI Platform Data Labeling Service roles

Role | Permissions  
---|---  
  
#### Data Labeling Service Admin Beta

(`roles/datalabeling.admin`) Full access to all Data Labeling resources  |  `datalabeling.*`

  * `datalabeling.annotateddatasets.delete`
  * `datalabeling.annotateddatasets.get`
  * `datalabeling.annotateddatasets.label`
  * `datalabeling.annotateddatasets.list`
  * `datalabeling.annotationspecsets.create`
  * `datalabeling.annotationspecsets.delete`
  * `datalabeling.annotationspecsets.get`
  * `datalabeling.annotationspecsets.list`
  * `datalabeling.dataitems.get`
  * `datalabeling.dataitems.list`
  * `datalabeling.datasets.create`
  * `datalabeling.datasets.delete`
  * `datalabeling.datasets.export`
  * `datalabeling.datasets.get`
  * `datalabeling.datasets.import`
  * `datalabeling.datasets.list`
  * `datalabeling.examples.get`
  * `datalabeling.examples.list`
  * `datalabeling.instructions.create`
  * `datalabeling.instructions.delete`
  * `datalabeling.instructions.get`
  * `datalabeling.instructions.list`
  * `datalabeling.operations.cancel`
  * `datalabeling.operations.get`
  * `datalabeling.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Labeling Service Editor Beta

(`roles/datalabeling.editor`) Editor of all Data Labeling resources  |  `datalabeling.*`

  * `datalabeling.annotateddatasets.delete`
  * `datalabeling.annotateddatasets.get`
  * `datalabeling.annotateddatasets.label`
  * `datalabeling.annotateddatasets.list`
  * `datalabeling.annotationspecsets.create`
  * `datalabeling.annotationspecsets.delete`
  * `datalabeling.annotationspecsets.get`
  * `datalabeling.annotationspecsets.list`
  * `datalabeling.dataitems.get`
  * `datalabeling.dataitems.list`
  * `datalabeling.datasets.create`
  * `datalabeling.datasets.delete`
  * `datalabeling.datasets.export`
  * `datalabeling.datasets.get`
  * `datalabeling.datasets.import`
  * `datalabeling.datasets.list`
  * `datalabeling.examples.get`
  * `datalabeling.examples.list`
  * `datalabeling.instructions.create`
  * `datalabeling.instructions.delete`
  * `datalabeling.instructions.get`
  * `datalabeling.instructions.list`
  * `datalabeling.operations.cancel`
  * `datalabeling.operations.get`
  * `datalabeling.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Labeling Service Viewer Beta

(`roles/datalabeling.viewer`) Viewer of all Data Labeling resources  |  `datalabeling.annotateddatasets.get` `datalabeling.annotateddatasets.list` `datalabeling.annotationspecsets.get` `datalabeling.annotationspecsets.list` `datalabeling.dataitems.*`

  * `datalabeling.dataitems.get`
  * `datalabeling.dataitems.list`

`datalabeling.datasets.get` `datalabeling.datasets.list` `datalabeling.examples.*`

  * `datalabeling.examples.get`
  * `datalabeling.examples.list`

`datalabeling.instructions.get` `datalabeling.instructions.list` `datalabeling.operations.get` `datalabeling.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Data Labeling Service Agent 

(`roles/datalabeling.serviceAgent`) Gives Data Labeling service account read/write access to Cloud Storage, read/write BigQuery, update CMLE model versions, editor access to Annotation service and AutoML service.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `automl.annotationSpecs.*`

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

`bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.tables.create` `bigquery.tables.get` `bigquery.tables.getData` `ml.jobs.create` `ml.jobs.get` `ml.jobs.getIamPolicy` `ml.jobs.list` `ml.locations.*`

  * `ml.locations.get`
  * `ml.locations.list`

`ml.models.*`

  * `ml.models.create`
  * `ml.models.delete`
  * `ml.models.get`
  * `ml.models.getIamPolicy`
  * `ml.models.list`
  * `ml.models.predict`
  * `ml.models.setIamPolicy`
  * `ml.models.update`

`ml.operations.get` `ml.operations.list` `ml.projects.getConfig` `ml.studies.*`

  * `ml.studies.create`
  * `ml.studies.delete`
  * `ml.studies.get`
  * `ml.studies.getIamPolicy`
  * `ml.studies.list`
  * `ml.studies.setIamPolicy`

`ml.trials.*`

  * `ml.trials.create`
  * `ml.trials.delete`
  * `ml.trials.get`
  * `ml.trials.list`
  * `ml.trials.update`

`ml.versions.*`

  * `ml.versions.create`
  * `ml.versions.delete`
  * `ml.versions.get`
  * `ml.versions.list`
  * `ml.versions.predict`
  * `ml.versions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## AI Platform Data Labeling Service permissions

Permission | Included in roles  
---|---  
  
#### `datalabeling.annotateddatasets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)   
  
#### `datalabeling.annotateddatasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `datalabeling.annotateddatasets.label`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalabeling.annotateddatasets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalabeling.annotationspecsets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)   
  
#### `datalabeling.annotationspecsets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)   
  
#### `datalabeling.annotationspecsets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalabeling.annotationspecsets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalabeling.dataitems.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `datalabeling.dataitems.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `datalabeling.datasets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `datalabeling.datasets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `datalabeling.datasets.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `datalabeling.datasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `datalabeling.datasets.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `datalabeling.datasets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `datalabeling.examples.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalabeling.examples.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalabeling.instructions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)   
  
#### `datalabeling.instructions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)   
  
#### `datalabeling.instructions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalabeling.instructions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalabeling.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)   
  
#### `datalabeling.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `datalabeling.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin) (`roles/datalabeling.admin`)  [Data Labeling Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.editor) (`roles/datalabeling.editor`)  [Data Labeling Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.viewer) (`roles/datalabeling.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
