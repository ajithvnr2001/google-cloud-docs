---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/dspm/
title: Data Security Posture Management roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:21.060692+00:00
---

# Data Security Posture Management roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/dspm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Data Security Posture Management roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Data Security Posture Management. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Data Security Posture Management roles

Role | Permissions  
---|---  
  
#### Data Security Posture Management Admin 

(`roles/dspm.admin`) Full access to Data Security Posture Management resources.  |  `dspm.*`

  * `dspm.locations.computeAggregation`
  * `dspm.locations.fetchDataGovernanceAnalytics`
  * `dspm.locations.fetchDspmGovernedProjects`
  * `dspm.locations.fetchGovernedResourceMetrics`
  * `dspm.locations.fetchLineageConnections`
  * `dspm.locations.get`
  * `dspm.locations.list`
  * `dspm.operations.cancel`
  * `dspm.operations.delete`
  * `dspm.operations.get`
  * `dspm.operations.list`

`resourcemanager.organizations.get`  
  
#### Data Security Posture Management Viewer 

(`roles/dspm.viewer`) Readonly access to Data Security Posture Management resources.  |  `dspm.locations.*`

  * `dspm.locations.computeAggregation`
  * `dspm.locations.fetchDataGovernanceAnalytics`
  * `dspm.locations.fetchDspmGovernedProjects`
  * `dspm.locations.fetchGovernedResourceMetrics`
  * `dspm.locations.fetchLineageConnections`
  * `dspm.locations.get`
  * `dspm.locations.list`

`dspm.operations.get` `dspm.operations.list` `resourcemanager.organizations.get`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### DSPM Service Agent 

(`roles/dspm.serviceAgent`) Gives DSPM Service Account access to consumer resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.artifacts.list` `aiplatform.contexts.list` `aiplatform.dataItems.list` `aiplatform.datasets.get` `aiplatform.datasets.list` `aiplatform.endpoints.list` `aiplatform.entityTypes.list` `aiplatform.executions.list` `aiplatform.metadataSchemas.list` `aiplatform.modelEvaluations.list` `aiplatform.models.list` `aiplatform.trainingPipelines.list` `aiplatform.tuningJobs.list` `bigquery.datasets.createTagBinding` `bigquery.datasets.deleteTagBinding` `bigquery.datasets.listEffectiveTags` `bigquery.datasets.listTagBindings` `bigquery.jobs.create` `bigquery.tables.createTagBinding` `bigquery.tables.deleteTagBinding` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.listEffectiveTags` `bigquery.tables.listTagBindings` `cloudasset.assets.exportResource` `cloudasset.assets.listResource` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllResources` `cloudasset.feeds.create` `cloudasset.feeds.delete` `cloudasset.feeds.get` `cloudasset.feeds.update` `cloudsecuritycompliance.cloudControlDeployments.create` `cloudsecuritycompliance.cloudControlDeployments.delete` `cloudsecuritycompliance.cloudControlDeployments.get` `cloudsecuritycompliance.cloudControlDeployments.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.frameworkDeployments.create` `cloudsecuritycompliance.frameworkDeployments.delete` `cloudsecuritycompliance.frameworkDeployments.get` `cloudsecuritycompliance.frameworkDeployments.list` `cloudsecuritycompliance.frameworks.get` `resourcemanager.folders.getIamPolicy` `resourcemanager.hierarchyNodes.*`

  * `resourcemanager.hierarchyNodes.createTagBinding`
  * `resourcemanager.hierarchyNodes.deleteTagBinding`
  * `resourcemanager.hierarchyNodes.listEffectiveTags`
  * `resourcemanager.hierarchyNodes.listTagBindings`

`resourcemanager.organizations.getIamPolicy` `resourcemanager.projects.getIamPolicy` `resourcemanager.tagKeys.create` `resourcemanager.tagKeys.delete` `resourcemanager.tagKeys.get` `resourcemanager.tagKeys.getIamPolicy` `resourcemanager.tagKeys.list` `resourcemanager.tagKeys.update` `resourcemanager.tagValueBindings.*`

  * `resourcemanager.tagValueBindings.create`
  * `resourcemanager.tagValueBindings.delete`

`resourcemanager.tagValues.create` `resourcemanager.tagValues.delete` `resourcemanager.tagValues.get` `resourcemanager.tagValues.getIamPolicy` `resourcemanager.tagValues.list` `resourcemanager.tagValues.update` `securitycenter.securityhealthanalyticssettings.*`

  * `securitycenter.securityhealthanalyticssettings.calculate`
  * `securitycenter.securityhealthanalyticssettings.get`
  * `securitycenter.securityhealthanalyticssettings.update`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityCenterServices.get` `securitycentermanagement.securityCenterServices.update` `securitycentermanagement.securityHealthAnalyticsCustomModules.create` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securityposture.operations.get` `securityposture.postureDeployments.create` `securityposture.postureDeployments.delete` `securityposture.postureDeployments.get` `securityposture.postureDeployments.list` `securityposture.postures.create` `securityposture.postures.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.createTagBinding` `storage.buckets.deleteTagBinding` `storage.buckets.listEffectiveTags` `storage.buckets.listTagBindings` `storage.intelligenceConfigs.get`  
  
## Data Security Posture Management permissions

Permission | Included in roles  
---|---  
  
#### `dspm.locations.computeAggregation`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `dspm.locations.fetchDataGovernanceAnalytics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `dspm.locations.fetchDspmGovernedProjects`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `dspm.locations.fetchGovernedResourceMetrics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `dspm.locations.fetchLineageConnections`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `dspm.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `dspm.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `dspm.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)   
  
#### `dspm.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)   
  
#### `dspm.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `dspm.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Security Posture Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)  [Data Security Posture Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
