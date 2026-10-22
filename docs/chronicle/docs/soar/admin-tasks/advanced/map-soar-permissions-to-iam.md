---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/map-soar-permissions-to-iam/
title: Map SOAR permissions to IAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:18.595942+00:00
---

# Map SOAR permissions to IAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/map-soar-permissions-to-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Map SOAR permissions to IAM

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

## Map SOAR legacy permissions to IAM permissions

This document maps legacy Google Security Operations SOAR permissions to Google Cloud IAM permissions. Use this mapping to manage access and capabilities in Google SecOps SOAR when migrating from legacy SOAR permission models.

The following sections list each SOAR legacy permission name (action) and show the required Cloud IAM permissions mapped to that action.

> **Important:** Always grant the full list of IAM permissions for a SOAR legacy permission name (action).
> 
> The lists of Google Cloud IAM permissions in this document are the **minimum required sets** needed to make each action work. To ensure that an action functions correctly and its related console elements (such as tabs or buttons) display as expected, you must grant all the permissions listed for that action.

## Required permissions for every role

Every user in the environment needs the following Cloud IAM permissions for platform accessibility and system functionality. These permissions let you render the interface, manage preferences, and generate authentication tokens:
    
    
    "chronicle.dataAccessScopes.list",
    "chronicle.preferenceSets.get",
    "chronicle.preferenceSets.update",
    "chronicle.instances.get",
    "chronicle.socRoles.get",
    "chronicle.userNotifications.get",
    "chronicle.userLocalizations.get",
    "chronicle.moduleSettings.rebranding",
    "chronicle.integrations.get",
    "chronicle.legacySoarAdvancedReports.get",
    "chronicle.environmentGroups.get",
    "chronicle.moduleSettingsProperties.get",
    "chronicle.legacySoarUsers.get"
    

## Permissions to view playbooks

To view playbooks, you need the following permissions:
    
    
    "chronicle.soarNetworks.get",
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarDashboards.get",
    "chronicle.involvedEntities.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.integrationLogicalOperatorRevisions.get",
    "chronicle.integrationLogicalOperators.get"
    

### Permissions to edit playbooks

To allow editing playbooks, you need the following permissions:
    
    
    "chronicle.soarNetworks.get",
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarDashboards.get",
    "chronicle.involvedEntities.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.emailTemplates.get",
    "chronicle.legacyPlaybooks.update",
    "chronicle.legacyPlaybooks.delete",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.import",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarSettings.update"
    

#### Permissions to manage folders

To allow managing folders, you need the following permissions:
    
    
    "chronicle.soarNetworks.get",
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarDashboards.get",
    "chronicle.involvedEntities.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.emailTemplates.get",
    "chronicle.legacyPlaybooks.import",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarSettings.update",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.update",
    "chronicle.legacyPlaybooks.delete"
    

## Permissions to view response integrations

To view response integrations, you need the following permissions:
    
    
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySoarSettings.get",
    "chronicle.marketplaceIntegrations.get",
    "chronicle.contentPacks.get",
    "chronicle.contentPacks.export",
    "chronicle.integrations.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get"
    

### Permissions to manage integrations, power-ups, and their instances

To manage integrations, power-ups, and their instances, including installing, deleting, configuring, and editing, you need the following permissions:
    
    
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySoarSettings.get",
    "chronicle.marketplaceIntegrations.get",
    "chronicle.contentPacks.export",
    "chronicle.integrations.get",
    "chronicle.integrationActions.get",
    "chronicle.contentPacks.get",
    "chronicle.contentPacks.delete",
    "chronicle.contentPacks.create",
    "chronicle.contentPacks.install",
    "chronicle.integrationInstances.get",
    "chronicle.integrationInstances.update",
    "chronicle.integrationInstances.delete"
    

## Permissions to view jobs

To view jobs, you need the following permissions:
    
    
    "chronicle.jobInstances.get",
    "chronicle.jobInstanceLogs.get",
    "chronicle.remoteAgents.get",
    "chronicle.jobs.get"
    

### Permissions to edit jobs

To allow editing jobs, you need the following permissions:
    
    
    "chronicle.jobInstanceLogs.get",
    "chronicle.remoteAgents.get",
    "chronicle.jobInstances.get",
    "chronicle.jobInstances.update",
    "chronicle.jobInstances.delete",
    "chronicle.jobInstances.run"
    

## Permissions to view settings

To view settings, you need the following permissions:
    
    
    "chronicle.slaDefinitions.get",
    "chronicle.requestTemplates.get",
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.soarNetworks.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.soarDomains.get",
    "chronicle.customLists.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.alertGroupingRules.get",
    "chronicle.legacySystem.getSystemVersion",
    "chronicle.legacySystem.getMaximumDataRetentionValue",
    "chronicle.legacyConfiguration.getMaximumAlertsGroupingConfiguration",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarAudits.legacySoarAudit",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFields.get",
    "chronicle.legacySoarIdpMappingGroups.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.views.get",
    "chronicle.moduleSettingsProperties.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.entitiesBlocklists.get",
    "chronicle.visualFamilies.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.remoteAgents.get",
    "chronicle.legacyPublisher.get",
    "chronicle.calculatedFieldDefinitions.get",
    "chronicle.enrichmentAgent.get",
    "chronicle.legacySdk.get",
    "chronicle.legacySoarPermissionGroups.get",
    "chronicle.legacySystemMetadata.get",
    "chronicle.legacySystemMetadata.placeholders",
    "chronicle.moduleSettings.get",
    "chronicle.notificationSettings.get",
    "chronicle.systemNotifications.get"
    

### Permissions to edit settings

To allow editing settings, you need the following permissions:
    
    
    "chronicle.legacySystem.getSystemVersion",
    "chronicle.legacySystem.getMaximumDataRetentionValue",
    "chronicle.legacyConfiguration.getMaximumAlertsGroupingConfiguration",
    "chronicle.legacySoarAudits.legacySoarAudit",
    "chronicle.views.get",
    "chronicle.moduleSettingsProperties.get",
    "chronicle.visualFamilies.get",
    "chronicle.integrationInstances.get",
    "chronicle.remoteAgents.get",
    "chronicle.legacyPublisher.get",
    "chronicle.socRoles.get",
    "chronicle.socRoles.update",
    "chronicle.socRoles.delete",
    "chronicle.slaDefinitions.get",
    "chronicle.slaDefinitions.update",
    "chronicle.slaDefinitions.delete",
    "chronicle.requestTemplates.get",
    "chronicle.requestTemplates.update",
    "chronicle.requestTemplates.delete",
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.propertySchemaDefinitions.update",
    "chronicle.propertySchemaDefinitions.delete",
    "chronicle.soarNetworks.get",
    "chronicle.soarNetworks.update",
    "chronicle.soarNetworks.delete",
    "chronicle.emailTemplates.get",
    "chronicle.emailTemplates.update",
    "chronicle.emailTemplates.delete",
    "chronicle.soarDomains.get",
    "chronicle.soarDomains.update",
    "chronicle.soarDomains.delete",
    "chronicle.customLists.get",
    "chronicle.customLists.update",
    "chronicle.customLists.delete",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseStageDefinitions.update",
    "chronicle.caseStageDefinitions.delete",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.caseCloseDefinitions.update",
    "chronicle.caseCloseDefinitions.delete",
    "chronicle.alertGroupingRules.get",
    "chronicle.alertGroupingRules.update",
    "chronicle.alertGroupingRules.delete",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarSettings.update",
    "chronicle.formDynamicParameters.get",
    "chronicle.formDynamicParameters.update",
    "chronicle.customFields.get",
    "chronicle.customFields.update",
    "chronicle.customFields.delete",
    "chronicle.legacySoarUsers.get",
    "chronicle.legacySoarUsers.delete",
    "chronicle.environments.get",
    "chronicle.environments.update",
    "chronicle.legacySoarIdpMappingGroups.get",
    "chronicle.legacySoarIdpMappingGroups.update",
    "chronicle.legacySoarIdpMappingGroups.delete",
    "chronicle.caseTagDefinitions.get",
    "chronicle.caseTagDefinitions.update",
    "chronicle.caseTagDefinitions.delete",
    "chronicle.entitiesBlocklists.get",
    "chronicle.entitiesBlocklists.update",
    "chronicle.entitiesBlocklists.delete",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyCaseFederationPlatforms.update",
    "chronicle.legacyCaseFederationPlatforms.delete",
    "chronicle.calculatedFieldDefinitions.delete",
    "chronicle.calculatedFieldDefinitions.update",
    "chronicle.legacySdk.update",
    "chronicle.moduleSettingsProperties.testSettings",
    "chronicle.moduleSettingsProperties.update",
    "chronicle.notificationSettings.update",
    "chronicle.systemNotifications.update",
    "chronicle.userLocalizations.update",
    "chronicle.userNotifications.update"
    

#### Permissions to edit environments

To allow editing environments, you need the following permissions:
    
    
    "chronicle.slaDefinitions.get",
    "chronicle.requestTemplates.get",
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.soarNetworks.get",
    "chronicle.emailTemplates.get",
    "chronicle.soarDomains.get",
    "chronicle.customLists.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.alertGroupingRules.get",
    "chronicle.legacySystem.getSystemVersion",
    "chronicle.legacySystem.getMaximumDataRetentionValue",
    "chronicle.legacyConfiguration.getMaximumAlertsGroupingConfiguration",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarAudits.legacySoarAudit",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFields.get",
    "chronicle.legacySoarIdpMappingGroups.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.views.get",
    "chronicle.moduleSettingsProperties.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.entitiesBlocklists.get",
    "chronicle.visualFamilies.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.remoteAgents.get",
    "chronicle.legacyPublisher.get",
    "chronicle.environments.get",
    "chronicle.environments.update",
    "chronicle.environments.delete",
    "chronicle.environmentGroups.get",
    "chronicle.environmentGroups.update",
    "chronicle.environmentGroups.delete"
    

## Permissions to view remote agents

To view remote agents, you need the following permissions:
    
    
    "chronicle.remoteAgents.get",
    "chronicle.legacyPublisher.get"
    

### Permissions to edit agents

To allow editing agents, you need the following permissions:
    
    
    "chronicle.remoteAgents.get",
    "chronicle.remoteAgents.update",
    "chronicle.remoteAgents.delete",
    "chronicle.legacyPublisher.get",
    "chronicle.legacyPublisher.update"
    

## Permissions for views

To manage views, you need the following permissions:
    
    
    "chronicle.views.get",
    "chronicle.views.update"
    

## Permissions to view connectors

To view connectors, you need the following permissions:
    
    
    "chronicle.connectorInstances.get",
    "chronicle.connectorInstanceLogs.get",
    "chronicle.remoteAgents.get"
    

### Permissions to edit connectors

To allow editing connectors, you need the following permissions:
    
    
    "chronicle.connectorInstanceLogs.get",
    "chronicle.remoteAgents.get",
    "chronicle.legacyCases.get",
    "chronicle.legacyCases.ingest",
    "chronicle.connectorInstances.update",
    "chronicle.connectorInstances.delete",
    "chronicle.connectorInstances.get"
    

## Permissions to view webhooks

To view webhooks, you need the following permissions:
    
    
    "chronicle.webhooks.get"
    

### Permissions to edit webhooks

To allow editing webhooks, you need the following permissions:
    
    
    "chronicle.webhooks.get",
    "chronicle.webhooks.update",
    "chronicle.webhooks.delete"
    

## Permissions to view dashboards

To view dashboards, you need the following permissions:
    
    
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarDashboards.update",
    "chronicle.legacySoarDashboards.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get"
    

### Permissions to edit dashboards

To allow editing dashboards, you need the following permissions:
    
    
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacySoarDashboards.update",
    "chronicle.legacySoarDashboards.get",
    "chronicle.legacySoarDashboards.delete"
    

## Permissions to view SOAR search

To view SOAR search, you need the following permissions:
    
    
    "chronicle.caseStageDefinitions.get",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySearches.searchCases",
    "chronicle.caseTagDefinitions.get"
    

### Permissions to view case search

To view case search, you need the following permissions:
    
    
    "chronicle.caseTagDefinitions.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities"
    

#### Permissions to allow search actions

To allow search actions, you need the following permissions:
    
    
    "chronicle.caseTagDefinitions.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.cases.get",
    "chronicle.cases.close",
    "chronicle.cases.reopen",
    "chronicle.cases.update"
    

## Permissions to view cases

To view cases, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.cases.countPriorities",
    "chronicle.cases.generateReport",
    "chronicle.legacyFederatedCases.fetchCasesToSync",
    "chronicle.legacySystemMetadata.placeholders"
    

### Permissions to view cases 2.0

To view cases 2.0, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.caseDetections.get",
    "chronicle.caseEvents.get",
    "chronicle.views.get",
    "chronicle.caseEvidenceDatas.get",
    "chronicle.cases.countPriorities",
    "chronicle.cases.generateReport",
    "chronicle.enrichmentAgent.get",
    "chronicle.legacyFederatedCases.fetchCasesToSync",
    "chronicle.legacySystemMetadata.placeholders"
    

### Permissions to allow case management actions

To allow case management actions, you need the following permissions:
    
    
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFields.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.propertySchemaDefinitions.update",
    "chronicle.propertySchemaDefinitions.delete",
    "chronicle.legacyCases.get",
    "chronicle.legacyCases.ingest",
    "chronicle.customFieldValues.get",
    "chronicle.customFieldValues.update",
    "chronicle.contextProperties.get",
    "chronicle.contextProperties.update",
    "chronicle.contextProperties.delete",
    "chronicle.involvedEntities.get",
    "chronicle.involvedEntities.update",
    "chronicle.cases.get",
    "chronicle.cases.update",
    "chronicle.cases.updateTag",
    "chronicle.cases.removeTag",
    "chronicle.cases.close",
    "chronicle.cases.reopen",
    "chronicle.caseAlerts.get",
    "chronicle.caseAlerts.metadataUpdate",
    "chronicle.caseAlerts.move",
    "chronicle.caseAlerts.removeTag",
    "chronicle.caseAlerts.updateTag",
    "chronicle.enrichmentAgent.execute",
    "chronicle.legacyFederatedCases.batchPatchFederatedCases",
    "chronicle.legacySystemMetadata.placeholders"
    

### Permissions to view case playbooks tab

To view the case playbooks tab, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyPlaybooks.get"
    

#### Permissions to attach playbooks manually

To allow attaching playbooks manually, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyPlaybooks.update",
    "chronicle.legacyPlaybooks.get"
    

#### Permissions to respond to actions

To allow responding to actions, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.update"
    

#### Permissions to rerun attached playbooks

To allow rerunning attached playbooks, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.update"
    

### Permissions to view case wall tab

To view the case wall tab, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyCases.get",
    "chronicle.caseComments.get",
    "chronicle.caseWallRecords.get",
    "chronicle.caseWallRecords.update"
    

#### Permissions to add and edit comments and attachments

To allow adding and editing comments and attachments, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyCases.get",
    "chronicle.caseWallRecords.get",
    "chronicle.caseWallRecords.update",
    "chronicle.caseComments.get",
    "chronicle.caseComments.update",
    "chronicle.caseComments.delete"
    

#### Permissions to pin case chat messages to the case wall

To allow pinning case chat messages to the case wall, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyCases.get",
    "chronicle.caseComments.get",
    "chronicle.caseWallRecords.get",
    "chronicle.caseWallRecords.update",
    "chronicle.chatMessages.pin",
    "chronicle.chatMessages.get"
    

### Permissions to allow case simulation

To allow case simulation, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyCases.importJson",
    "chronicle.legacyCases.deleteSimulated",
    "chronicle.legacyCases.simulate",
    "chronicle.legacyCases.get",
    "chronicle.legacyCases.exportJson",
    "chronicle.legacyCases.createSimulated",
    "chronicle.legacyCases.getSimulated"
    

### Permissions to ingest alerts as test cases

To allow ingesting alerts as test cases, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyCases.get",
    "chronicle.legacyCases.ingestAlertTestCase"
    

### Permissions to perform manual actions

To allow performing manual actions, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyCases.get",
    "chronicle.legacyCases.runManualAction"
    

### Permissions to create manual cases

To allow creating manual cases, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyCases.get",
    "chronicle.legacyCases.createManual",
    "chronicle.legacyPlaybooks.get"
    

### Permissions to respond to actions

To allow responding to actions, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.update"
    

### Permissions to allow case chat

To allow case chat, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.chatMessages.get",
    "chronicle.chatMessages.create",
    "chronicle.chatMessageAttachments.get",
    "chronicle.instances.generateSoarChatMessage"
    

### Permissions to add and edit entity properties

To allow adding and editing entity properties, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.involvedEntities.get",
    "chronicle.involvedEntities.update"
    

### Permissions to share case queue filters

To allow sharing case queue filters, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.environments.get",
    "chronicle.emailTemplates.get",
    "chronicle.caseStageDefinitions.get",
    "chronicle.caseCloseDefinitions.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.export",
    "chronicle.legacySoarSettings.get",
    "chronicle.formDynamicParameters.get",
    "chronicle.customFieldValues.get",
    "chronicle.customFields.get",
    "chronicle.contextProperties.get",
    "chronicle.legacySoarUsers.get",
    "chronicle.connectorEvents.get",
    "chronicle.involvedEntities.get",
    "chronicle.cases.get",
    "chronicle.caseAlerts.get",
    "chronicle.tasks.get",
    "chronicle.views.get",
    "chronicle.caseTagDefinitions.get",
    "chronicle.integrationInstances.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacyFederatedCases.get",
    "chronicle.caseQueueFilters.update",
    "chronicle.caseQueueFilters.get",
    "chronicle.caseQueueFilters.delete",
    "chronicle.shareConfigs.update"
    

## Permissions for entity explorer

To view the entity explorer, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.uniqueEntities.get"
    

### Permissions to add comments

To allow adding comments in the entity explorer, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.uniqueEntities.get",
    "chronicle.uniqueEntities.update"
    

### Permissions to add and edit entity properties in entity explorer

To allow adding and editing entity properties in the entity explorer, you need the following permissions:
    
    
    "chronicle.propertySchemaDefinitions.get",
    "chronicle.uniqueEntities.get",
    "chronicle.uniqueEntities.update"
    

## Permissions for Your Workdesk

To view Your Workdesk, you need the following permissions:
    
    
    "chronicle.requestTemplates.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarUsers.get"
    

### Permissions for My tasks

To view "My tasks" on Your Workdesk, you need the following permissions:
    
    
    "chronicle.requestTemplates.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarUsers.get",
    "chronicle.tasks.get"
    

#### Permissions to create and edit tasks

To allow creating and editing tasks, you need the following permissions:
    
    
    "chronicle.requestTemplates.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarUsers.get",
    "chronicle.tasks.get",
    "chronicle.tasks.update",
    "chronicle.tasks.delete"
    

### Permissions for Announcements

To view announcements on Your Workdesk, you need the following permissions:
    
    
    "chronicle.requestTemplates.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarUsers.get",
    "chronicle.announcements.get"
    

#### Permissions to create and edit announcements

To allow creating and editing announcements, you need the following permissions:
    
    
    "chronicle.requestTemplates.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarUsers.get",
    "chronicle.announcements.get",
    "chronicle.announcements.update",
    "chronicle.announcements.delete"
    

### Permissions for Requests

To view requests on Your Workdesk, you need the following permissions:
    
    
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarUsers.get",
    "chronicle.requestTemplates.get"
    

### Permissions for Pending actions

To view pending actions on Your Workdesk, you need the following permissions:
    
    
    "chronicle.requestTemplates.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarUsers.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacyPlaybooks.update"
    

### Permissions for Workspace

To use the workspace feature on Your Workdesk, you need the following permissions:
    
    
    "chronicle.requestTemplates.get",
    "chronicle.legacySearches.searchCases",
    "chronicle.legacySearches.searchEntities",
    "chronicle.legacySoarUsers.get",
    "chronicle.workdeskNotes.update",
    "chronicle.workdeskNotes.get",
    "chronicle.workdeskNotes.delete",
    "chronicle.workdeskLinks.update",
    "chronicle.workdeskLinks.get",
    "chronicle.workdeskLinks.delete",
    "chronicle.workdeskContacts.update",
    "chronicle.workdeskContacts.get",
    "chronicle.workdeskContacts.delete",
    "chronicle.attachments.update",
    "chronicle.attachments.get",
    "chronicle.attachments.delete"
    

## Permissions for Investigation

This section covers permissions related to investigation tasks.

### Permissions to perform manual actions

To allow performing manual actions during an investigation, you need the following permissions:
    
    
    "chronicle.legacyCases.get",
    "chronicle.legacyCases.runManualAction"
    

### Permissions to add and edit entity properties in investigation

To allow adding and editing entity properties during an investigation, you need the following permissions:
    
    
    "chronicle.involvedEntities.get",
    "chronicle.involvedEntities.update"
    

## Permissions for reports

To view reports, you need the following permissions:
    
    
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarReports.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get"
    

### Permissions to edit reports

To allow editing reports, you need the following permissions:
    
    
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySoarSettings.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacySoarDashboards.get",
    "chronicle.legacySoarDashboards.update",
    "chronicle.legacySoarReports.get",
    "chronicle.legacySoarReports.update",
    "chronicle.legacySoarReports.delete"
    

### Permissions to view advanced reports

To view advanced reports, you need the following permissions:
    
    
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySoarSettings.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacySoarAdvancedReports.get",
    "chronicle.legacySoarReports.get"
    

#### Permissions to edit advanced reports

To allow editing advanced reports, you need the following permissions:
    
    
    "chronicle.environments.get",
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySoarSettings.get",
    "chronicle.integrationInstances.get",
    "chronicle.integrationActions.get",
    "chronicle.legacyCaseFederationPlatforms.get",
    "chronicle.legacySoarAdvancedReports.update",
    "chronicle.legacySoarAdvancedReports.share",
    "chronicle.legacySoarAdvancedReports.get",
    "chronicle.legacySoarAdvancedReports.delete",
    "chronicle.legacySoarReports.get",
    "chronicle.legacySoarReports.update"
    

## Permissions for ontology

To view the ontology, you need the following permissions:
    
    
    "chronicle.mappingRules.get",
    "chronicle.ontologyRecords.get",
    "chronicle.visualFamilies.get"
    

### Permissions to allow event configuration screen

To access the event configuration screen in the ontology, you need the following permissions:
    
    
    "chronicle.mappingRules.get",
    "chronicle.mappingRules.update",
    "chronicle.mappingRules.delete",
    "chronicle.ontologyRecords.get",
    "chronicle.ontologyRecords.update",
    "chronicle.visualFamilies.get",
    "chronicle.visualFamilies.update",
    "chronicle.visualFamilies.delete"
    

## Permissions for IDE

To use the IDE, you need the following permissions:
    
    
    "chronicle.legacyPlaybooks.get",
    "chronicle.legacySoarSettings.get",
    "chronicle.legacySoarSettings.update",
    "chronicle.marketplaceIntegrations.get",
    "chronicle.marketplaceIntegrations.uninstall",
    "chronicle.marketplaceIntegrations.install",
    "chronicle.contentPacks.get",
    "chronicle.contentPacks.delete",
    "chronicle.contentPacks.create",
    "chronicle.contentPacks.install",
    "chronicle.contentPacks.export",
    "chronicle.managers.update",
    "chronicle.managers.get",
    "chronicle.managers.delete",
    "chronicle.managerRevisions.update",
    "chronicle.managerRevisions.get",
    "chronicle.managerRevisions.delete",
    "chronicle.jobs.update",
    "chronicle.jobs.get",
    "chronicle.jobs.delete",
    "chronicle.jobRevisions.get",
    "chronicle.jobRevisions.update",
    "chronicle.jobRevisions.delete",
    "chronicle.integrations.update",
    "chronicle.integrations.get",
    "chronicle.integrations.delete",
    "chronicle.integrationInstances.update",
    "chronicle.integrationInstances.get",
    "chronicle.integrationInstances.delete",
    "chronicle.connectors.get",
    "chronicle.connectors.update",
    "chronicle.connectors.delete",
    "chronicle.connectorRevisions.update",
    "chronicle.connectorRevisions.delete",
    "chronicle.connectorRevisions.get",
    "chronicle.integrationActions.get",
    "chronicle.integrationActions.update",
    "chronicle.integrationActions.delete",
    "chronicle.integrationActions.run",
    "chronicle.integrationActionRevisions.update",
    "chronicle.integrationActionRevisions.delete",
    "chronicle.integrationActionRevisions.get",
    "chronicle.integrationLogicalOperatorRevisions.delete",
    "chronicle.integrationLogicalOperatorRevisions.get",
    "chronicle.integrationLogicalOperatorRevisions.update",
    "chronicle.integrationLogicalOperators.delete",
    "chronicle.integrationLogicalOperators.execute",
    "chronicle.integrationLogicalOperators.get",
    "chronicle.integrationLogicalOperators.update",
    "chronicle.transformerDefinitions.create",
    "chronicle.transformerDefinitions.delete",
    "chronicle.transformerDefinitions.execute",
    "chronicle.transformerDefinitions.get",
    "chronicle.transformerDefinitions.list",
    "chronicle.transformerDefinitions.update",
    "chronicle.transformerRevisions.delete",
    "chronicle.transformerRevisions.get",
    "chronicle.transformerRevisions.update"
    

## Permissions for all environments

To manage all environments, you need the following permissions:
    
    
    "chronicle.environments.get",
    "chronicle.environments.update",
    "chronicle.environmentGroups.get",
    "chronicle.environmentGroups.update",
    "chronicle.environmentGroups.delete"
    

## Permissions for SLA

This section covers permissions related to Service Level Agreements (SLAs).

### Permissions to pause and resume SLAs

To allow pausing and resuming SLAs, you need the following permissions:
    
    
    "chronicle.cases.get",
    "chronicle.cases.update",
    "chronicle.caseAlerts.get",
    "chronicle.caseAlerts.updateSla"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
