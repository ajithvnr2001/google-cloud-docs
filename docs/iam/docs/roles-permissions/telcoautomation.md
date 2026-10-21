---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation/
title: Telco Automation API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:41:54.065105+00:00
---

# Telco Automation API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Telco Automation API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Telco Automation API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Telco Automation API roles

Role | Permissions  
---|---  
  
#### Telco Automation Admin Beta

(`roles/telcoautomation.admin`) Full access to Telco Automation resources.  |  `cloudquotas.*`

  * `cloudquotas.quotas.get`
  * `cloudquotas.quotas.update`

`logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.exclusions.get` `logging.exclusions.list` `logging.links.get` `logging.links.list` `logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.list` `logging.logMetrics.get` `logging.logMetrics.list` `logging.logScopes.get` `logging.logScopes.list` `logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.get` `logging.notificationRules.list` `logging.operations.get` `logging.operations.list` `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `logging.settings.get` `logging.sinks.get` `logging.sinks.list` `logging.usage.get` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `monitoring.timeSeries.list` `observability.scopes.get` `resourcemanager.projects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.contentsecuritypolicy.*`

  * `serviceusage.contentsecuritypolicy.get`
  * `serviceusage.contentsecuritypolicy.update`

`serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.*`

  * `serviceusage.mcppolicy.get`
  * `serviceusage.mcppolicy.update`

`serviceusage.operations.get` `serviceusage.quotas.*`

  * `serviceusage.quotas.get`
  * `serviceusage.quotas.update`

`serviceusage.services.*`

  * `serviceusage.services.disable`
  * `serviceusage.services.enable`
  * `serviceusage.services.get`
  * `serviceusage.services.list`
  * `serviceusage.services.listApis`
  * `serviceusage.services.listDependentServices`
  * `serviceusage.services.use`

`serviceusage.values.test` `source.repos.get` `source.repos.list` `telcoautomation.*`

  * `telcoautomation.blueprints.approve`
  * `telcoautomation.blueprints.create`
  * `telcoautomation.blueprints.delete`
  * `telcoautomation.blueprints.get`
  * `telcoautomation.blueprints.list`
  * `telcoautomation.blueprints.propose`
  * `telcoautomation.blueprints.update`
  * `telcoautomation.deployments.apply`
  * `telcoautomation.deployments.computeStatus`
  * `telcoautomation.deployments.create`
  * `telcoautomation.deployments.delete`
  * `telcoautomation.deployments.get`
  * `telcoautomation.deployments.list`
  * `telcoautomation.deployments.rollback`
  * `telcoautomation.deployments.update`
  * `telcoautomation.edgeSlms.create`
  * `telcoautomation.edgeSlms.delete`
  * `telcoautomation.edgeSlms.get`
  * `telcoautomation.edgeSlms.list`
  * `telcoautomation.hydratedDeployments.apply`
  * `telcoautomation.hydratedDeployments.get`
  * `telcoautomation.hydratedDeployments.list`
  * `telcoautomation.hydratedDeployments.update`
  * `telcoautomation.locations.get`
  * `telcoautomation.locations.list`
  * `telcoautomation.operations.cancel`
  * `telcoautomation.operations.delete`
  * `telcoautomation.operations.get`
  * `telcoautomation.operations.list`
  * `telcoautomation.orchestrationClusters.create`
  * `telcoautomation.orchestrationClusters.delete`
  * `telcoautomation.orchestrationClusters.get`
  * `telcoautomation.orchestrationClusters.list`
  * `telcoautomation.publicBlueprints.get`
  * `telcoautomation.publicBlueprints.list`

  
  
#### Telcoautomation Editor Beta

(`roles/telcoautomation.editor`) Editor role for telcoautomation  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `telcoautomation.blueprints.*`

  * `telcoautomation.blueprints.approve`
  * `telcoautomation.blueprints.create`
  * `telcoautomation.blueprints.delete`
  * `telcoautomation.blueprints.get`
  * `telcoautomation.blueprints.list`
  * `telcoautomation.blueprints.propose`
  * `telcoautomation.blueprints.update`

`telcoautomation.deployments.*`

  * `telcoautomation.deployments.apply`
  * `telcoautomation.deployments.computeStatus`
  * `telcoautomation.deployments.create`
  * `telcoautomation.deployments.delete`
  * `telcoautomation.deployments.get`
  * `telcoautomation.deployments.list`
  * `telcoautomation.deployments.rollback`
  * `telcoautomation.deployments.update`

`telcoautomation.edgeSlms.get` `telcoautomation.edgeSlms.list` `telcoautomation.hydratedDeployments.*`

  * `telcoautomation.hydratedDeployments.apply`
  * `telcoautomation.hydratedDeployments.get`
  * `telcoautomation.hydratedDeployments.list`
  * `telcoautomation.hydratedDeployments.update`

`telcoautomation.locations.*`

  * `telcoautomation.locations.get`
  * `telcoautomation.locations.list`

`telcoautomation.operations.*`

  * `telcoautomation.operations.cancel`
  * `telcoautomation.operations.delete`
  * `telcoautomation.operations.get`
  * `telcoautomation.operations.list`

`telcoautomation.orchestrationClusters.delete` `telcoautomation.orchestrationClusters.get` `telcoautomation.orchestrationClusters.list` `telcoautomation.publicBlueprints.*`

  * `telcoautomation.publicBlueprints.get`
  * `telcoautomation.publicBlueprints.list`

  
  
#### Telcoautomation Viewer Beta

(`roles/telcoautomation.viewer`) Viewer role for telcoautomation  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `telcoautomation.blueprints.get` `telcoautomation.blueprints.list` `telcoautomation.deployments.computeStatus` `telcoautomation.deployments.get` `telcoautomation.deployments.list` `telcoautomation.edgeSlms.get` `telcoautomation.edgeSlms.list` `telcoautomation.hydratedDeployments.get` `telcoautomation.hydratedDeployments.list` `telcoautomation.locations.*`

  * `telcoautomation.locations.get`
  * `telcoautomation.locations.list`

`telcoautomation.operations.get` `telcoautomation.operations.list` `telcoautomation.orchestrationClusters.get` `telcoautomation.orchestrationClusters.list` `telcoautomation.publicBlueprints.*`

  * `telcoautomation.publicBlueprints.get`
  * `telcoautomation.publicBlueprints.list`

  
  
#### Telco Automation Blueprint Designer Beta

(`roles/telcoautomation.blueprintDesigner`) Ability to manage blueprints  |  `telcoautomation.blueprints.create` `telcoautomation.blueprints.delete` `telcoautomation.blueprints.get` `telcoautomation.blueprints.list` `telcoautomation.blueprints.propose` `telcoautomation.blueprints.update` `telcoautomation.deployments.computeStatus` `telcoautomation.deployments.get` `telcoautomation.deployments.list` `telcoautomation.hydratedDeployments.get` `telcoautomation.hydratedDeployments.list` `telcoautomation.orchestrationClusters.get` `telcoautomation.orchestrationClusters.list` `telcoautomation.publicBlueprints.*`

  * `telcoautomation.publicBlueprints.get`
  * `telcoautomation.publicBlueprints.list`

  
  
#### Telco Automation Deployment Admin Beta

(`roles/telcoautomation.deploymentAdmin`) Ability to manage deployments  |  `telcoautomation.blueprints.get` `telcoautomation.blueprints.list` `telcoautomation.deployments.*`

  * `telcoautomation.deployments.apply`
  * `telcoautomation.deployments.computeStatus`
  * `telcoautomation.deployments.create`
  * `telcoautomation.deployments.delete`
  * `telcoautomation.deployments.get`
  * `telcoautomation.deployments.list`
  * `telcoautomation.deployments.rollback`
  * `telcoautomation.deployments.update`

`telcoautomation.hydratedDeployments.*`

  * `telcoautomation.hydratedDeployments.apply`
  * `telcoautomation.hydratedDeployments.get`
  * `telcoautomation.hydratedDeployments.list`
  * `telcoautomation.hydratedDeployments.update`

`telcoautomation.orchestrationClusters.get` `telcoautomation.orchestrationClusters.list`  
  
#### Telco Automation Tier 1 Operations Admin Beta

(`roles/telcoautomation.opsAdminTier1`) Ability to get status of deployments  |  `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.exclusions.get` `logging.exclusions.list` `logging.links.get` `logging.links.list` `logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.list` `logging.logMetrics.get` `logging.logMetrics.list` `logging.logScopes.get` `logging.logScopes.list` `logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.get` `logging.notificationRules.list` `logging.operations.get` `logging.operations.list` `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `logging.settings.get` `logging.sinks.get` `logging.sinks.list` `logging.usage.get` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `observability.scopes.get` `resourcemanager.projects.get` `telcoautomation.blueprints.get` `telcoautomation.blueprints.list` `telcoautomation.deployments.computeStatus` `telcoautomation.deployments.get` `telcoautomation.deployments.list` `telcoautomation.hydratedDeployments.get` `telcoautomation.hydratedDeployments.list` `telcoautomation.orchestrationClusters.get` `telcoautomation.orchestrationClusters.list`  
  
#### Telco Automation Tier 4 Operations Admin Beta

(`roles/telcoautomation.opsAdminTier4`) Ability to manage deployments and their status  |  `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.exclusions.get` `logging.exclusions.list` `logging.links.get` `logging.links.list` `logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.list` `logging.logMetrics.get` `logging.logMetrics.list` `logging.logScopes.get` `logging.logScopes.list` `logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.get` `logging.notificationRules.list` `logging.operations.get` `logging.operations.list` `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `logging.settings.get` `logging.sinks.get` `logging.sinks.list` `logging.usage.get` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `observability.scopes.get` `resourcemanager.projects.get` `telcoautomation.blueprints.get` `telcoautomation.blueprints.list` `telcoautomation.deployments.*`

  * `telcoautomation.deployments.apply`
  * `telcoautomation.deployments.computeStatus`
  * `telcoautomation.deployments.create`
  * `telcoautomation.deployments.delete`
  * `telcoautomation.deployments.get`
  * `telcoautomation.deployments.list`
  * `telcoautomation.deployments.rollback`
  * `telcoautomation.deployments.update`

`telcoautomation.hydratedDeployments.*`

  * `telcoautomation.hydratedDeployments.apply`
  * `telcoautomation.hydratedDeployments.get`
  * `telcoautomation.hydratedDeployments.list`
  * `telcoautomation.hydratedDeployments.update`

`telcoautomation.orchestrationClusters.get` `telcoautomation.orchestrationClusters.list`  
  
#### Telco Automation Service Orchestrator Beta

(`roles/telcoautomation.serviceOrchestrator`) Ability to manage deployments  |  `telcoautomation.blueprints.get` `telcoautomation.blueprints.list` `telcoautomation.deployments.*`

  * `telcoautomation.deployments.apply`
  * `telcoautomation.deployments.computeStatus`
  * `telcoautomation.deployments.create`
  * `telcoautomation.deployments.delete`
  * `telcoautomation.deployments.get`
  * `telcoautomation.deployments.list`
  * `telcoautomation.deployments.rollback`
  * `telcoautomation.deployments.update`

`telcoautomation.hydratedDeployments.*`

  * `telcoautomation.hydratedDeployments.apply`
  * `telcoautomation.hydratedDeployments.get`
  * `telcoautomation.hydratedDeployments.list`
  * `telcoautomation.hydratedDeployments.update`

`telcoautomation.orchestrationClusters.get` `telcoautomation.orchestrationClusters.list`  
  
## Telco Automation API permissions

Permission | Included in roles  
---|---  
  
#### `telcoautomation.blueprints.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)   
  
#### `telcoautomation.blueprints.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)   
  
#### `telcoautomation.blueprints.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)   
  
#### `telcoautomation.blueprints.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.blueprints.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.blueprints.propose`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)   
  
#### `telcoautomation.blueprints.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)   
  
#### `telcoautomation.deployments.apply`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.deployments.computeStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.deployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.deployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.deployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.deployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.deployments.rollback`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.deployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.edgeSlms.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)   
  
#### `telcoautomation.edgeSlms.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)   
  
#### `telcoautomation.edgeSlms.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `telcoautomation.edgeSlms.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `telcoautomation.hydratedDeployments.apply`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.hydratedDeployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.hydratedDeployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.hydratedDeployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `telcoautomation.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `telcoautomation.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)   
  
#### `telcoautomation.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)   
  
#### `telcoautomation.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `telcoautomation.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `telcoautomation.orchestrationClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)   
  
#### `telcoautomation.orchestrationClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)   
  
#### `telcoautomation.orchestrationClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.orchestrationClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)  [Telco Automation Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.deploymentAdmin) (`roles/telcoautomation.deploymentAdmin`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  [Telco Automation Service Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.serviceOrchestrator) (`roles/telcoautomation.serviceOrchestrator`)   
  
#### `telcoautomation.publicBlueprints.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)   
  
#### `telcoautomation.publicBlueprints.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Telcoautomation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.editor) (`roles/telcoautomation.editor`)  [Telcoautomation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.viewer) (`roles/telcoautomation.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Telco Automation Blueprint Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.blueprintDesigner) (`roles/telcoautomation.blueprintDesigner`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
