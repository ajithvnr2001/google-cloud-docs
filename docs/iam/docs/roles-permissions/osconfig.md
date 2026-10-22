---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig/
title: Cloud OS Config roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:58.625598+00:00
---

# Cloud OS Config roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud OS Config roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud OS Config. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud OS Config roles

Role | Permissions  
---|---  
  
#### OS Config Admin 

(`roles/osconfig.admin`) Full access to OS Config resources  |  `osconfig.*`

  * `osconfig.guestPolicies.create`
  * `osconfig.guestPolicies.delete`
  * `osconfig.guestPolicies.get`
  * `osconfig.guestPolicies.list`
  * `osconfig.guestPolicies.update`
  * `osconfig.instanceOSPoliciesCompliances.get`
  * `osconfig.instanceOSPoliciesCompliances.list`
  * `osconfig.inventories.get`
  * `osconfig.inventories.list`
  * `osconfig.locations.get`
  * `osconfig.locations.list`
  * `osconfig.operations.cancel`
  * `osconfig.operations.delete`
  * `osconfig.operations.get`
  * `osconfig.operations.list`
  * `osconfig.osPolicyAssignmentReports.get`
  * `osconfig.osPolicyAssignmentReports.list`
  * `osconfig.osPolicyAssignmentReports.searchSummaries`
  * `osconfig.osPolicyAssignments.create`
  * `osconfig.osPolicyAssignments.delete`
  * `osconfig.osPolicyAssignments.get`
  * `osconfig.osPolicyAssignments.list`
  * `osconfig.osPolicyAssignments.searchPolicies`
  * `osconfig.osPolicyAssignments.update`
  * `osconfig.patchDeployments.create`
  * `osconfig.patchDeployments.delete`
  * `osconfig.patchDeployments.execute`
  * `osconfig.patchDeployments.get`
  * `osconfig.patchDeployments.list`
  * `osconfig.patchDeployments.pause`
  * `osconfig.patchDeployments.resume`
  * `osconfig.patchDeployments.update`
  * `osconfig.patchJobs.exec`
  * `osconfig.patchJobs.get`
  * `osconfig.patchJobs.list`
  * `osconfig.policyOrchestrators.create`
  * `osconfig.policyOrchestrators.delete`
  * `osconfig.policyOrchestrators.get`
  * `osconfig.policyOrchestrators.list`
  * `osconfig.policyOrchestrators.update`
  * `osconfig.projectFeatureSettings.get`
  * `osconfig.projectFeatureSettings.update`
  * `osconfig.upgradeReports.get`
  * `osconfig.upgradeReports.getSummary`
  * `osconfig.upgradeReports.list`
  * `osconfig.upgradeReports.searchSummaries`
  * `osconfig.vulnerabilityReports.get`
  * `osconfig.vulnerabilityReports.list`

  
  
#### OS Config Viewer 

(`roles/osconfig.viewer`) Readonly access to OS Config resources  |  `osconfig.guestPolicies.get` `osconfig.guestPolicies.list` `osconfig.instanceOSPoliciesCompliances.*`

  * `osconfig.instanceOSPoliciesCompliances.get`
  * `osconfig.instanceOSPoliciesCompliances.list`

`osconfig.inventories.*`

  * `osconfig.inventories.get`
  * `osconfig.inventories.list`

`osconfig.locations.*`

  * `osconfig.locations.get`
  * `osconfig.locations.list`

`osconfig.operations.get` `osconfig.operations.list` `osconfig.osPolicyAssignmentReports.*`

  * `osconfig.osPolicyAssignmentReports.get`
  * `osconfig.osPolicyAssignmentReports.list`
  * `osconfig.osPolicyAssignmentReports.searchSummaries`

`osconfig.osPolicyAssignments.get` `osconfig.osPolicyAssignments.list` `osconfig.osPolicyAssignments.searchPolicies` `osconfig.patchDeployments.get` `osconfig.patchDeployments.list` `osconfig.patchJobs.get` `osconfig.patchJobs.list` `osconfig.policyOrchestrators.get` `osconfig.policyOrchestrators.list` `osconfig.projectFeatureSettings.get` `osconfig.upgradeReports.*`

  * `osconfig.upgradeReports.get`
  * `osconfig.upgradeReports.getSummary`
  * `osconfig.upgradeReports.list`
  * `osconfig.upgradeReports.searchSummaries`

`osconfig.vulnerabilityReports.*`

  * `osconfig.vulnerabilityReports.get`
  * `osconfig.vulnerabilityReports.list`

  
  
#### GuestPolicy Admin Beta

(`roles/osconfig.guestPolicyAdmin`) Full admin access to GuestPolicies  |  `osconfig.guestPolicies.*`

  * `osconfig.guestPolicies.create`
  * `osconfig.guestPolicies.delete`
  * `osconfig.guestPolicies.get`
  * `osconfig.guestPolicies.list`
  * `osconfig.guestPolicies.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GuestPolicy Editor Beta

(`roles/osconfig.guestPolicyEditor`) Editor of GuestPolicy resources  |  `osconfig.guestPolicies.get` `osconfig.guestPolicies.list` `osconfig.guestPolicies.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GuestPolicy Viewer Beta

(`roles/osconfig.guestPolicyViewer`) Viewer of GuestPolicy resources  |  `osconfig.guestPolicies.get` `osconfig.guestPolicies.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### InstanceOSPoliciesCompliance Viewer Beta

(`roles/osconfig.instanceOSPoliciesComplianceViewer`) Viewer of OS Policies Compliance of VM instances  |  `osconfig.instanceOSPoliciesCompliances.*`

  * `osconfig.instanceOSPoliciesCompliances.get`
  * `osconfig.instanceOSPoliciesCompliances.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### OS Inventory Viewer 

(`roles/osconfig.inventoryViewer`) Viewer of OS Inventories  |  `osconfig.inventories.*`

  * `osconfig.inventories.get`
  * `osconfig.inventories.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### OSPolicyAssignment Admin 

(`roles/osconfig.osPolicyAssignmentAdmin`) Full admin access to OS Policy Assignments  |  `osconfig.osPolicyAssignments.*`

  * `osconfig.osPolicyAssignments.create`
  * `osconfig.osPolicyAssignments.delete`
  * `osconfig.osPolicyAssignments.get`
  * `osconfig.osPolicyAssignments.list`
  * `osconfig.osPolicyAssignments.searchPolicies`
  * `osconfig.osPolicyAssignments.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### OSPolicyAssignment Editor 

(`roles/osconfig.osPolicyAssignmentEditor`) Editor of OS Policy Assignments  |  `osconfig.osPolicyAssignments.get` `osconfig.osPolicyAssignments.list` `osconfig.osPolicyAssignments.searchPolicies` `osconfig.osPolicyAssignments.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### OSPolicyAssignmentReport Viewer 

(`roles/osconfig.osPolicyAssignmentReportViewer`) Viewer of OS policy assignment reports for VM instances  |  `osconfig.osPolicyAssignmentReports.*`

  * `osconfig.osPolicyAssignmentReports.get`
  * `osconfig.osPolicyAssignmentReports.list`
  * `osconfig.osPolicyAssignmentReports.searchSummaries`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### OSPolicyAssignment Viewer 

(`roles/osconfig.osPolicyAssignmentViewer`) Viewer of OS Policy Assignments  |  `osconfig.osPolicyAssignments.get` `osconfig.osPolicyAssignments.list` `osconfig.osPolicyAssignments.searchPolicies` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### PatchDeployment Admin 

(`roles/osconfig.patchDeploymentAdmin`) Full admin access to PatchDeployments  |  `osconfig.patchDeployments.*`

  * `osconfig.patchDeployments.create`
  * `osconfig.patchDeployments.delete`
  * `osconfig.patchDeployments.execute`
  * `osconfig.patchDeployments.get`
  * `osconfig.patchDeployments.list`
  * `osconfig.patchDeployments.pause`
  * `osconfig.patchDeployments.resume`
  * `osconfig.patchDeployments.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### PatchDeployment Viewer 

(`roles/osconfig.patchDeploymentViewer`) Viewer of PatchDeployment resources  |  `osconfig.patchDeployments.get` `osconfig.patchDeployments.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Patch Job Executor 

(`roles/osconfig.patchJobExecutor`) Access to execute Patch Jobs.  |  `osconfig.patchJobs.*`

  * `osconfig.patchJobs.exec`
  * `osconfig.patchJobs.get`
  * `osconfig.patchJobs.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Patch Job Viewer 

(`roles/osconfig.patchJobViewer`) Get and list Patch Jobs.  |  `osconfig.patchJobs.get` `osconfig.patchJobs.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### PolicyOrchestrator Admin Beta

(`roles/osconfig.policyOrchestratorAdmin`) Admin of PolicyOrchestrator resources  |  `osconfig.locations.*`

  * `osconfig.locations.get`
  * `osconfig.locations.list`

`osconfig.operations.get` `osconfig.policyOrchestrators.*`

  * `osconfig.policyOrchestrators.create`
  * `osconfig.policyOrchestrators.delete`
  * `osconfig.policyOrchestrators.get`
  * `osconfig.policyOrchestrators.list`
  * `osconfig.policyOrchestrators.update`

  
  
#### PolicyOrchestrator Viewer Beta

(`roles/osconfig.policyOrchestratorViewer`) Viewer of PolicyOrchestrator resources  |  `osconfig.locations.*`

  * `osconfig.locations.get`
  * `osconfig.locations.list`

`osconfig.operations.get` `osconfig.policyOrchestrators.get` `osconfig.policyOrchestrators.list`  
  
#### Project Feature Settings Editor 

(`roles/osconfig.projectFeatureSettingsEditor`) Read/write access to project feature settings  |  `osconfig.projectFeatureSettings.*`

  * `osconfig.projectFeatureSettings.get`
  * `osconfig.projectFeatureSettings.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Project Feature Settings Viewer 

(`roles/osconfig.projectFeatureSettingsViewer`) Read access to project feature settings  |  `osconfig.projectFeatureSettings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Upgrade Report Viewer Beta

(`roles/osconfig.upgradeReportViewer`) Provides read-only access to VM Manager Upgrade Reports  |  `osconfig.upgradeReports.*`

  * `osconfig.upgradeReports.get`
  * `osconfig.upgradeReports.getSummary`
  * `osconfig.upgradeReports.list`
  * `osconfig.upgradeReports.searchSummaries`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### OS VulnerabilityReport Viewer 

(`roles/osconfig.vulnerabilityReportViewer`) Viewer of OS VulnerabilityReports  |  `osconfig.vulnerabilityReports.*`

  * `osconfig.vulnerabilityReports.get`
  * `osconfig.vulnerabilityReports.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud OS Config Rollout Service Agent 

(`roles/osconfig.rolloutServiceAgent`) Grants OS Config Rollout Service Account access to zonal OS Config resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `osconfig.operations.get` `osconfig.osPolicyAssignments.delete` `osconfig.osPolicyAssignments.get` `osconfig.osPolicyAssignments.update`  
  
#### Cloud OS Config Service Agent 

(`roles/osconfig.serviceAgent`) Grants OS Config Service Account access to Google Compute Engine instances.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudasset.assets.listOSConfigOSPolicyAssignments` `cloudasset.assets.listPatchDeployments` `compute.globalOperations.get` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.list` `compute.instances.setMetadata` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`containeranalysis.notes.attachOccurrence` `containeranalysis.notes.create` `containeranalysis.notes.delete` `containeranalysis.notes.get` `containeranalysis.notes.list` `containeranalysis.notes.update` `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `iam.serviceAccounts.actAs` `osconfig.projectFeatureSettings.*`

  * `osconfig.projectFeatureSettings.get`
  * `osconfig.projectFeatureSettings.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Cloud OS Config permissions

Permission | Included in roles  
---|---  
  
#### `osconfig.guestPolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [GuestPolicy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyAdmin) (`roles/osconfig.guestPolicyAdmin`)   
  
#### `osconfig.guestPolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [GuestPolicy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyAdmin) (`roles/osconfig.guestPolicyAdmin`)   
  
#### `osconfig.guestPolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GuestPolicy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyAdmin) (`roles/osconfig.guestPolicyAdmin`)  [GuestPolicy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyEditor) (`roles/osconfig.guestPolicyEditor`)  [GuestPolicy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyViewer) (`roles/osconfig.guestPolicyViewer`)   
  
#### `osconfig.guestPolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GuestPolicy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyAdmin) (`roles/osconfig.guestPolicyAdmin`)  [GuestPolicy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyEditor) (`roles/osconfig.guestPolicyEditor`)  [GuestPolicy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyViewer) (`roles/osconfig.guestPolicyViewer`)   
  
#### `osconfig.guestPolicies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [GuestPolicy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyAdmin) (`roles/osconfig.guestPolicyAdmin`)  [GuestPolicy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.guestPolicyEditor) (`roles/osconfig.guestPolicyEditor`)   
  
#### `osconfig.instanceOSPoliciesCompliances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [InstanceOSPoliciesCompliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.instanceOSPoliciesComplianceViewer) (`roles/osconfig.instanceOSPoliciesComplianceViewer`)   
  
#### `osconfig.instanceOSPoliciesCompliances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [InstanceOSPoliciesCompliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.instanceOSPoliciesComplianceViewer) (`roles/osconfig.instanceOSPoliciesComplianceViewer`)   
  
#### `osconfig.inventories.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OS Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.inventoryViewer) (`roles/osconfig.inventoryViewer`)   
  
#### `osconfig.inventories.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OS Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.inventoryViewer) (`roles/osconfig.inventoryViewer`)   
  
#### `osconfig.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [PolicyOrchestrator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorAdmin) (`roles/osconfig.policyOrchestratorAdmin`)  [PolicyOrchestrator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorViewer) (`roles/osconfig.policyOrchestratorViewer`)   
  
#### `osconfig.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [PolicyOrchestrator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorAdmin) (`roles/osconfig.policyOrchestratorAdmin`)  [PolicyOrchestrator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorViewer) (`roles/osconfig.policyOrchestratorViewer`)   
  
#### `osconfig.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)   
  
#### `osconfig.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)   
  
#### `osconfig.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [PolicyOrchestrator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorAdmin) (`roles/osconfig.policyOrchestratorAdmin`)  [PolicyOrchestrator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorViewer) (`roles/osconfig.policyOrchestratorViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud OS Config Rollout Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.rolloutServiceAgent) (`roles/osconfig.rolloutServiceAgent`) 

  
  
#### `osconfig.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `osconfig.osPolicyAssignmentReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OSPolicyAssignmentReport Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentReportViewer) (`roles/osconfig.osPolicyAssignmentReportViewer`)   
  
#### `osconfig.osPolicyAssignmentReports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OSPolicyAssignmentReport Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentReportViewer) (`roles/osconfig.osPolicyAssignmentReportViewer`)   
  
#### `osconfig.osPolicyAssignmentReports.searchSummaries`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OSPolicyAssignmentReport Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentReportViewer) (`roles/osconfig.osPolicyAssignmentReportViewer`)   
  
#### `osconfig.osPolicyAssignments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OSPolicyAssignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin) (`roles/osconfig.osPolicyAssignmentAdmin`)   
  
#### `osconfig.osPolicyAssignments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OSPolicyAssignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin) (`roles/osconfig.osPolicyAssignmentAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud OS Config Rollout Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.rolloutServiceAgent) (`roles/osconfig.rolloutServiceAgent`) 

  
  
#### `osconfig.osPolicyAssignments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OSPolicyAssignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin) (`roles/osconfig.osPolicyAssignmentAdmin`)  [OSPolicyAssignment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentEditor) (`roles/osconfig.osPolicyAssignmentEditor`)  [OSPolicyAssignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentViewer) (`roles/osconfig.osPolicyAssignmentViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud OS Config Rollout Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.rolloutServiceAgent) (`roles/osconfig.rolloutServiceAgent`) 

  
  
#### `osconfig.osPolicyAssignments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OSPolicyAssignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin) (`roles/osconfig.osPolicyAssignmentAdmin`)  [OSPolicyAssignment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentEditor) (`roles/osconfig.osPolicyAssignmentEditor`)  [OSPolicyAssignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentViewer) (`roles/osconfig.osPolicyAssignmentViewer`)   
  
#### `osconfig.osPolicyAssignments.searchPolicies`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OSPolicyAssignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin) (`roles/osconfig.osPolicyAssignmentAdmin`)  [OSPolicyAssignment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentEditor) (`roles/osconfig.osPolicyAssignmentEditor`)  [OSPolicyAssignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentViewer) (`roles/osconfig.osPolicyAssignmentViewer`)   
  
#### `osconfig.osPolicyAssignments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OSPolicyAssignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin) (`roles/osconfig.osPolicyAssignmentAdmin`)  [OSPolicyAssignment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentEditor) (`roles/osconfig.osPolicyAssignmentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud OS Config Rollout Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.rolloutServiceAgent) (`roles/osconfig.rolloutServiceAgent`) 

  
  
#### `osconfig.patchDeployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PatchDeployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentAdmin) (`roles/osconfig.patchDeploymentAdmin`)   
  
#### `osconfig.patchDeployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PatchDeployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentAdmin) (`roles/osconfig.patchDeploymentAdmin`)   
  
#### `osconfig.patchDeployments.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PatchDeployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentAdmin) (`roles/osconfig.patchDeploymentAdmin`)   
  
#### `osconfig.patchDeployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [PatchDeployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentAdmin) (`roles/osconfig.patchDeploymentAdmin`)  [PatchDeployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentViewer) (`roles/osconfig.patchDeploymentViewer`)   
  
#### `osconfig.patchDeployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [PatchDeployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentAdmin) (`roles/osconfig.patchDeploymentAdmin`)  [PatchDeployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentViewer) (`roles/osconfig.patchDeploymentViewer`)   
  
#### `osconfig.patchDeployments.pause`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PatchDeployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentAdmin) (`roles/osconfig.patchDeploymentAdmin`)   
  
#### `osconfig.patchDeployments.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PatchDeployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentAdmin) (`roles/osconfig.patchDeploymentAdmin`)   
  
#### `osconfig.patchDeployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PatchDeployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchDeploymentAdmin) (`roles/osconfig.patchDeploymentAdmin`)   
  
#### `osconfig.patchJobs.exec`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [Patch Job Executor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchJobExecutor) (`roles/osconfig.patchJobExecutor`)   
  
#### `osconfig.patchJobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Patch Job Executor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchJobExecutor) (`roles/osconfig.patchJobExecutor`)  [Patch Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchJobViewer) (`roles/osconfig.patchJobViewer`)   
  
#### `osconfig.patchJobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Patch Job Executor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchJobExecutor) (`roles/osconfig.patchJobExecutor`)  [Patch Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.patchJobViewer) (`roles/osconfig.patchJobViewer`)   
  
#### `osconfig.policyOrchestrators.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PolicyOrchestrator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorAdmin) (`roles/osconfig.policyOrchestratorAdmin`)   
  
#### `osconfig.policyOrchestrators.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PolicyOrchestrator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorAdmin) (`roles/osconfig.policyOrchestratorAdmin`)   
  
#### `osconfig.policyOrchestrators.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [PolicyOrchestrator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorAdmin) (`roles/osconfig.policyOrchestratorAdmin`)  [PolicyOrchestrator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorViewer) (`roles/osconfig.policyOrchestratorViewer`)   
  
#### `osconfig.policyOrchestrators.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [PolicyOrchestrator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorAdmin) (`roles/osconfig.policyOrchestratorAdmin`)  [PolicyOrchestrator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorViewer) (`roles/osconfig.policyOrchestratorViewer`)   
  
#### `osconfig.policyOrchestrators.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [PolicyOrchestrator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.policyOrchestratorAdmin) (`roles/osconfig.policyOrchestratorAdmin`)   
  
#### `osconfig.projectFeatureSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Project Feature Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.projectFeatureSettingsEditor) (`roles/osconfig.projectFeatureSettingsEditor`)  [Project Feature Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.projectFeatureSettingsViewer) (`roles/osconfig.projectFeatureSettingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `osconfig.projectFeatureSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [Project Feature Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.projectFeatureSettingsEditor) (`roles/osconfig.projectFeatureSettingsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `osconfig.upgradeReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Upgrade Report Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.upgradeReportViewer) (`roles/osconfig.upgradeReportViewer`)   
  
#### `osconfig.upgradeReports.getSummary`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Upgrade Report Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.upgradeReportViewer) (`roles/osconfig.upgradeReportViewer`)   
  
#### `osconfig.upgradeReports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Upgrade Report Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.upgradeReportViewer) (`roles/osconfig.upgradeReportViewer`)   
  
#### `osconfig.upgradeReports.searchSummaries`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Upgrade Report Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.upgradeReportViewer) (`roles/osconfig.upgradeReportViewer`)   
  
#### `osconfig.vulnerabilityReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OS VulnerabilityReport Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.vulnerabilityReportViewer) (`roles/osconfig.vulnerabilityReportViewer`)   
  
#### `osconfig.vulnerabilityReports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [OS Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.admin) (`roles/osconfig.admin`)  [OS Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.viewer) (`roles/osconfig.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [OS VulnerabilityReport Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.vulnerabilityReportViewer) (`roles/osconfig.vulnerabilityReportViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
