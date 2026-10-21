---
url: https://docs.cloud.google.com/workload-manager/docs/access-control/roles-permissions/
title: IAM roles and permissions \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:35.197649+00:00
---

# IAM roles and permissions  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/access-control/roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  IAM roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Workload Manager, including the permissions required to create and run evaluations.

## Workload Manager roles

The following table lists all Workload Manager IAM roles and the permissions granted by those roles:

Role | Permissions  
---|---  
  
#### Workload Manager Admin Beta

(`roles/workloadmanager.admin`) Full access to Workload Manager all resources.  |  `compute.acceleratorTypes.list` `compute.diskTypes.list` `compute.machineTypes.list` `compute.networks.list` `compute.projects.get` `compute.regions.list` `compute.subnetworks.list` `compute.zones.list` `dns.managedZones.list` `iam.serviceAccounts.list` `monitoring.timeSeries.list` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.list` `storage.objects.list` `workloadmanager.*`

  * `workloadmanager.actuations.create`
  * `workloadmanager.actuations.delete`
  * `workloadmanager.actuations.get`
  * `workloadmanager.actuations.list`
  * `workloadmanager.deployments.create`
  * `workloadmanager.deployments.delete`
  * `workloadmanager.deployments.get`
  * `workloadmanager.deployments.list`
  * `workloadmanager.discoveredprofiles.get`
  * `workloadmanager.discoveredprofiles.getHealth`
  * `workloadmanager.discoveredprofiles.list`
  * `workloadmanager.evaluations.create`
  * `workloadmanager.evaluations.delete`
  * `workloadmanager.evaluations.get`
  * `workloadmanager.evaluations.list`
  * `workloadmanager.evaluations.run`
  * `workloadmanager.evaluations.update`
  * `workloadmanager.executions.delete`
  * `workloadmanager.executions.get`
  * `workloadmanager.executions.list`
  * `workloadmanager.findings.create`
  * `workloadmanager.findings.list`
  * `workloadmanager.insights.delete`
  * `workloadmanager.insights.export`
  * `workloadmanager.insights.listSapSystems`
  * `workloadmanager.insights.write`
  * `workloadmanager.locations.get`
  * `workloadmanager.locations.list`
  * `workloadmanager.operations.cancel`
  * `workloadmanager.operations.delete`
  * `workloadmanager.operations.get`
  * `workloadmanager.operations.list`
  * `workloadmanager.results.list`
  * `workloadmanager.rules.list`
  * `workloadmanager.workloads.get`
  * `workloadmanager.workloads.list`

  
  
#### Workload Manager Viewer Beta

(`roles/workloadmanager.viewer`) Read-only access to Workload Manager all resources.  |  `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadmanager.actuations.get` `workloadmanager.actuations.list` `workloadmanager.deployments.get` `workloadmanager.deployments.list` `workloadmanager.discoveredprofiles.*`

  * `workloadmanager.discoveredprofiles.get`
  * `workloadmanager.discoveredprofiles.getHealth`
  * `workloadmanager.discoveredprofiles.list`

`workloadmanager.evaluations.get` `workloadmanager.evaluations.list` `workloadmanager.executions.get` `workloadmanager.executions.list` `workloadmanager.findings.list` `workloadmanager.results.list` `workloadmanager.rules.list`  
  
#### Workload Manager Deployment Admin Beta

(`roles/workloadmanager.deploymentAdmin`) Full access to Workload Manager deployment resources.  |  `compute.acceleratorTypes.list` `compute.diskTypes.list` `compute.machineTypes.list` `compute.networks.list` `compute.projects.get` `compute.regions.list` `compute.subnetworks.list` `compute.zones.list` `dns.managedZones.list` `iam.serviceAccounts.list` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.list` `storage.objects.list` `workloadmanager.actuations.*`

  * `workloadmanager.actuations.create`
  * `workloadmanager.actuations.delete`
  * `workloadmanager.actuations.get`
  * `workloadmanager.actuations.list`

`workloadmanager.deployments.*`

  * `workloadmanager.deployments.create`
  * `workloadmanager.deployments.delete`
  * `workloadmanager.deployments.get`
  * `workloadmanager.deployments.list`

`workloadmanager.locations.*`

  * `workloadmanager.locations.get`
  * `workloadmanager.locations.list`

`workloadmanager.operations.*`

  * `workloadmanager.operations.cancel`
  * `workloadmanager.operations.delete`
  * `workloadmanager.operations.get`
  * `workloadmanager.operations.list`

  
  
#### Workload Manager Deployment Viewer Beta

(`roles/workloadmanager.deploymentViewer`) Read-only access to Workload Manager deployment resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadmanager.actuations.get` `workloadmanager.actuations.list` `workloadmanager.deployments.get` `workloadmanager.deployments.list`  
  
#### Workload Manager Evaluation Admin Beta

(`roles/workloadmanager.evaluationAdmin`) Full access to Workload Manager evaluation resources.  |  `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadmanager.evaluations.*`

  * `workloadmanager.evaluations.create`
  * `workloadmanager.evaluations.delete`
  * `workloadmanager.evaluations.get`
  * `workloadmanager.evaluations.list`
  * `workloadmanager.evaluations.run`
  * `workloadmanager.evaluations.update`

`workloadmanager.executions.*`

  * `workloadmanager.executions.delete`
  * `workloadmanager.executions.get`
  * `workloadmanager.executions.list`

`workloadmanager.findings.*`

  * `workloadmanager.findings.create`
  * `workloadmanager.findings.list`

`workloadmanager.locations.*`

  * `workloadmanager.locations.get`
  * `workloadmanager.locations.list`

`workloadmanager.operations.*`

  * `workloadmanager.operations.cancel`
  * `workloadmanager.operations.delete`
  * `workloadmanager.operations.get`
  * `workloadmanager.operations.list`

`workloadmanager.results.list` `workloadmanager.rules.list`  
  
#### Workload Manager Evaluation Viewer Beta

(`roles/workloadmanager.evaluationViewer`) Read-only access to Workload Manager evaluation resources.  |  `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadmanager.evaluations.get` `workloadmanager.evaluations.list` `workloadmanager.executions.get` `workloadmanager.executions.list` `workloadmanager.results.list` `workloadmanager.rules.list`  
  
#### Workload Manager Insights Writer Beta

(`roles/workloadmanager.insightWriter`) The role used to write data to WLM data warehouse.  |  `workloadmanager.insights.delete` `workloadmanager.insights.write`  
  
#### Workload Manager Worker Beta

(`roles/workloadmanager.worker`) The role used by Workload Manager application runners to read and update workloads.  |  `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadmanager.actuations.*`

  * `workloadmanager.actuations.create`
  * `workloadmanager.actuations.delete`
  * `workloadmanager.actuations.get`
  * `workloadmanager.actuations.list`

`workloadmanager.deployments.*`

  * `workloadmanager.deployments.create`
  * `workloadmanager.deployments.delete`
  * `workloadmanager.deployments.get`
  * `workloadmanager.deployments.list`

`workloadmanager.discoveredprofiles.*`

  * `workloadmanager.discoveredprofiles.get`
  * `workloadmanager.discoveredprofiles.getHealth`
  * `workloadmanager.discoveredprofiles.list`

`workloadmanager.evaluations.*`

  * `workloadmanager.evaluations.create`
  * `workloadmanager.evaluations.delete`
  * `workloadmanager.evaluations.get`
  * `workloadmanager.evaluations.list`
  * `workloadmanager.evaluations.run`
  * `workloadmanager.evaluations.update`

`workloadmanager.executions.*`

  * `workloadmanager.executions.delete`
  * `workloadmanager.executions.get`
  * `workloadmanager.executions.list`

`workloadmanager.findings.*`

  * `workloadmanager.findings.create`
  * `workloadmanager.findings.list`

`workloadmanager.insights.write` `workloadmanager.results.list` `workloadmanager.rules.list`  
  
#### Workload Manager Workload Viewer Beta

(`roles/workloadmanager.workloadViewer`) The role used to view the workload related data.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `workloadmanager.discoveredprofiles.*`

  * `workloadmanager.discoveredprofiles.get`
  * `workloadmanager.discoveredprofiles.getHealth`
  * `workloadmanager.discoveredprofiles.list`

`workloadmanager.workloads.*`

  * `workloadmanager.workloads.get`
  * `workloadmanager.workloads.list`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Workload Manager Service Agent 

(`roles/workloadmanager.serviceAgent`) Gives Workload Manager Service Agent access to CAI export functions and Cloud Monitoring.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudasset.assets.exportAccessPolicy` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportOrgPolicy` `cloudasset.assets.exportResource` `cloudasset.assets.listAccessPolicy` `cloudasset.assets.listIamPolicy` `cloudasset.assets.listOSInventories` `cloudasset.assets.listOrgPolicy` `cloudasset.assets.listResource` `cloudasset.assets.searchAllResources` `config.deployments.create` `config.deployments.delete` `config.deployments.get` `config.deployments.list` `config.deployments.update` `config.locations.*`

  * `config.locations.get`
  * `config.locations.list`

`config.operations.*`

  * `config.operations.cancel`
  * `config.operations.delete`
  * `config.operations.get`
  * `config.operations.list`

`config.resources.list` `config.revisions.get` `config.revisions.list` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.list` `serviceusage.services.use` `workloadmanager.insights.export` `workloadmanager.insights.listSapSystems`  
  
## Workload Manager permissions

The following table lists the permissions supported by Workload Manager:

Permission | Included in roles  
---|---  
  
#### `workloadmanager.actuations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.actuations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.actuations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentViewer) (`roles/workloadmanager.deploymentViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.actuations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentViewer) (`roles/workloadmanager.deploymentViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.deployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.deployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.deployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentViewer) (`roles/workloadmanager.deploymentViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.deployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentViewer) (`roles/workloadmanager.deploymentViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.discoveredprofiles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)  [Workload Manager Workload Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.workloadViewer) (`roles/workloadmanager.workloadViewer`)   
  
#### `workloadmanager.discoveredprofiles.getHealth`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)  [Workload Manager Workload Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.workloadViewer) (`roles/workloadmanager.workloadViewer`)   
  
#### `workloadmanager.discoveredprofiles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)  [Workload Manager Workload Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.workloadViewer) (`roles/workloadmanager.workloadViewer`)   
  
#### `workloadmanager.evaluations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.evaluations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.evaluations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Evaluation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationViewer) (`roles/workloadmanager.evaluationViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.evaluations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Evaluation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationViewer) (`roles/workloadmanager.evaluationViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.evaluations.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.evaluations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.executions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.executions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Evaluation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationViewer) (`roles/workloadmanager.evaluationViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.executions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Evaluation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationViewer) (`roles/workloadmanager.evaluationViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.findings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.findings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.insights.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Insights Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`)   
  
#### `workloadmanager.insights.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Workload Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.serviceAgent) (`roles/workloadmanager.serviceAgent`) 

  
  
#### `workloadmanager.insights.listSapSystems`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Workload Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.serviceAgent) (`roles/workloadmanager.serviceAgent`) 

  
  
#### `workloadmanager.insights.write`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Insights Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)   
  
#### `workloadmanager.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)   
  
#### `workloadmanager.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)   
  
#### `workloadmanager.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)   
  
#### `workloadmanager.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)   
  
#### `workloadmanager.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.deploymentAdmin) (`roles/workloadmanager.deploymentAdmin`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)   
  
#### `workloadmanager.results.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Evaluation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationViewer) (`roles/workloadmanager.evaluationViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.rules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Workload Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.viewer) (`roles/workloadmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Evaluation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`)  [Workload Manager Evaluation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationViewer) (`roles/workloadmanager.evaluationViewer`)  [Workload Manager Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.worker) (`roles/workloadmanager.worker`)   
  
#### `workloadmanager.workloads.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Workload Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.workloadViewer) (`roles/workloadmanager.workloadViewer`)   
  
#### `workloadmanager.workloads.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.admin) (`roles/workloadmanager.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Manager Workload Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.workloadViewer) (`roles/workloadmanager.workloadViewer`)   
  
## IAM roles in consumer and target projects for evaluations

To evaluate workloads using Workload Manager, you run evaluations from a consumer project against target projects.

To learn about consumer and target projects and view the summary table of required permissions to create, run, and view evaluations, see [IAM roles in consumer and target projects for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).

## What's next

  * Learn about [Workload Manager service agents](https://docs.cloud.google.com/workload-manager/docs/access-control/service-accounts)
  * [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
