---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads/
title: Assured Workloads roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:55.783929+00:00
---

# Assured Workloads roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Assured Workloads roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Assured Workloads. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Assured Workloads roles

Role | Permissions  
---|---  
  
#### Assured Workloads Administrator 

(`roles/assuredworkloads.admin`) Grants full access to Assured Workloads resources, CRM resources - project/folder and Organization Policy administration  |  `assuredworkloads.*`

  * `assuredworkloads.dbControlComplianceSummaries.list`
  * `assuredworkloads.dbFindingSummaries.list`
  * `assuredworkloads.dbFrameworkComplianceReports.aggregate`
  * `assuredworkloads.dbFrameworkComplianceReports.get`
  * `assuredworkloads.dbFrameworkComplianceSummaries.list`
  * `assuredworkloads.operations.get`
  * `assuredworkloads.operations.list`
  * `assuredworkloads.updates.list`
  * `assuredworkloads.updates.update`
  * `assuredworkloads.violations.get`
  * `assuredworkloads.violations.list`
  * `assuredworkloads.violations.update`
  * `assuredworkloads.workload.create`
  * `assuredworkloads.workload.delete`
  * `assuredworkloads.workload.get`
  * `assuredworkloads.workload.list`
  * `assuredworkloads.workload.update`

`axt.labels.set` `bigquery.config.update` `cloudsecuritycompliance.cloudControlPredictions.*`

  * `cloudsecuritycompliance.cloudControlPredictions.create`
  * `cloudsecuritycompliance.cloudControlPredictions.get`
  * `cloudsecuritycompliance.cloudControlPredictions.list`

`cloudsecuritycompliance.cloudControls.*`

  * `cloudsecuritycompliance.cloudControls.create`
  * `cloudsecuritycompliance.cloudControls.delete`
  * `cloudsecuritycompliance.cloudControls.get`
  * `cloudsecuritycompliance.cloudControls.list`
  * `cloudsecuritycompliance.cloudControls.update`

`cloudsecuritycompliance.frameworks.*`

  * `cloudsecuritycompliance.frameworks.create`
  * `cloudsecuritycompliance.frameworks.delete`
  * `cloudsecuritycompliance.frameworks.get`
  * `cloudsecuritycompliance.frameworks.list`
  * `cloudsecuritycompliance.frameworks.update`

`logging.settings.update` `orgpolicy.policies.*`

  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`

`orgpolicy.policy.*`

  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`

`resourcemanager.folders.create` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.create` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Assured Workloads Editor 

(`roles/assuredworkloads.editor`) Grants read, write access to Assured Workloads resources, CRM resources - project/folder and Organization Policy administration  |  `assuredworkloads.*`

  * `assuredworkloads.dbControlComplianceSummaries.list`
  * `assuredworkloads.dbFindingSummaries.list`
  * `assuredworkloads.dbFrameworkComplianceReports.aggregate`
  * `assuredworkloads.dbFrameworkComplianceReports.get`
  * `assuredworkloads.dbFrameworkComplianceSummaries.list`
  * `assuredworkloads.operations.get`
  * `assuredworkloads.operations.list`
  * `assuredworkloads.updates.list`
  * `assuredworkloads.updates.update`
  * `assuredworkloads.violations.get`
  * `assuredworkloads.violations.list`
  * `assuredworkloads.violations.update`
  * `assuredworkloads.workload.create`
  * `assuredworkloads.workload.delete`
  * `assuredworkloads.workload.get`
  * `assuredworkloads.workload.list`
  * `assuredworkloads.workload.update`

`axt.labels.set` `bigquery.config.update` `cloudsecuritycompliance.cloudControlPredictions.*`

  * `cloudsecuritycompliance.cloudControlPredictions.create`
  * `cloudsecuritycompliance.cloudControlPredictions.get`
  * `cloudsecuritycompliance.cloudControlPredictions.list`

`cloudsecuritycompliance.cloudControls.*`

  * `cloudsecuritycompliance.cloudControls.create`
  * `cloudsecuritycompliance.cloudControls.delete`
  * `cloudsecuritycompliance.cloudControls.get`
  * `cloudsecuritycompliance.cloudControls.list`
  * `cloudsecuritycompliance.cloudControls.update`

`cloudsecuritycompliance.frameworks.*`

  * `cloudsecuritycompliance.frameworks.create`
  * `cloudsecuritycompliance.frameworks.delete`
  * `cloudsecuritycompliance.frameworks.get`
  * `cloudsecuritycompliance.frameworks.list`
  * `cloudsecuritycompliance.frameworks.update`

`logging.settings.update` `orgpolicy.policies.*`

  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`

`orgpolicy.policy.*`

  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`

`resourcemanager.folders.create` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.create` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Assured Workloads Viewer 

(`roles/assuredworkloads.viewer`) Viewer role for Assured Workloads  |  `assuredworkloads.dbControlComplianceSummaries.list` `assuredworkloads.dbFindingSummaries.list` `assuredworkloads.dbFrameworkComplianceReports.*`

  * `assuredworkloads.dbFrameworkComplianceReports.aggregate`
  * `assuredworkloads.dbFrameworkComplianceReports.get`

`assuredworkloads.dbFrameworkComplianceSummaries.list` `assuredworkloads.operations.*`

  * `assuredworkloads.operations.get`
  * `assuredworkloads.operations.list`

`assuredworkloads.updates.list` `assuredworkloads.violations.get` `assuredworkloads.violations.list` `assuredworkloads.workload.get` `assuredworkloads.workload.list` `cloudsecuritycompliance.cloudControlPredictions.get` `cloudsecuritycompliance.cloudControlPredictions.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Assured Workloads Reader 

(`roles/assuredworkloads.reader`) Grants read access to all Assured Workloads resources and CRM resources - project/folder  |  `assuredworkloads.dbControlComplianceSummaries.list` `assuredworkloads.dbFindingSummaries.list` `assuredworkloads.dbFrameworkComplianceReports.*`

  * `assuredworkloads.dbFrameworkComplianceReports.aggregate`
  * `assuredworkloads.dbFrameworkComplianceReports.get`

`assuredworkloads.dbFrameworkComplianceSummaries.list` `assuredworkloads.operations.*`

  * `assuredworkloads.operations.get`
  * `assuredworkloads.operations.list`

`assuredworkloads.updates.list` `assuredworkloads.violations.get` `assuredworkloads.violations.list` `assuredworkloads.workload.get` `assuredworkloads.workload.list` `cloudsecuritycompliance.cloudControlPredictions.get` `cloudsecuritycompliance.cloudControlPredictions.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Assured Workloads Monitoring Service Agent 

(`roles/assuredworkloads.monitoringServiceAgent`) Gives the Assured Workloads service account access to create CAIS feed and monitor Assured Workloads.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudasset.assets.exportResource` `cloudasset.assets.listResource` `cloudasset.feeds.create` `cloudasset.feeds.delete` `cloudasset.feeds.get`  
  
#### Assured Workloads Service Agent 

(`roles/assuredworkloads.serviceAgent`) Gives the Assured Workloads service account access to create KMS keyrings and keys, monitor Assured Workloads and read Organization Policies.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudkms.cryptoKeys.create` `cloudkms.keyRings.create` `orgpolicy.policies.list` `orgpolicy.policy.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test`  
  
## Assured Workloads permissions

Permission | Included in roles  
---|---  
  
#### `assuredworkloads.dbControlComplianceSummaries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.dbFindingSummaries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.dbFrameworkComplianceReports.aggregate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.dbFrameworkComplianceReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.dbFrameworkComplianceSummaries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.updates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.updates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)   
  
#### `assuredworkloads.violations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Controls Partner Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringServiceAgent) (`roles/cloudcontrolspartner.monitoringServiceAgent`) 

  
  
#### `assuredworkloads.violations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Controls Partner Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.monitoringServiceAgent) (`roles/cloudcontrolspartner.monitoringServiceAgent`) 

  
  
#### `assuredworkloads.violations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)   
  
#### `assuredworkloads.workload.create`

|  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)   
  
#### `assuredworkloads.workload.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)   
  
#### `assuredworkloads.workload.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.workload.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)  [Assured Workloads Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.viewer) (`roles/assuredworkloads.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Assured Workloads Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.reader) (`roles/assuredworkloads.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `assuredworkloads.workload.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Assured Workloads Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)  [Assured Workloads Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
