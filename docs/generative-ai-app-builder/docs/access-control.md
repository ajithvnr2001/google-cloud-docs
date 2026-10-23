---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:29.255822+00:00
---

# Access control with IAM  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can control Discovery Engine API access and permissions for Agent Search resources using Identity and Access Management (IAM).

## Overview

Google Cloud offers IAM, which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. This page describes the Agent Search IAM roles and permissions. For a detailed description of Google Cloud IAM, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

Agent Search provides a set of predefined roles designed to help you control access to your Agent Search resources. You can also create your own [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), if the predefined roles don't provide the sets of permissions you need. In addition, the older basic roles (Editor, Viewer, and Owner) are also still available to you, although they don't provide the same fine-grained control as the Agent Search roles. In particular, the basic roles provide access to resources across Google Cloud rather than just for Agent Search. See the [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) documentation for more information.

## Predefined roles

Agent Search provides some predefined roles that you can use to provide finer-grained permissions to principals. The role you grant to a principal controls what actions the principal can take. Principals can be individuals, groups, or service accounts.

You can grant multiple roles to the same principal, and you can change the roles granted to a principal at any time, provided you have the permissions to do so.

**Note:** To create an app and view its monitoring data, you might need permissions that are not included in the predefined Discovery Engine roles. For example, the `monitoring.timeSeries.list` permission is required. To get this permission, consider asking your project administrator to grant you the [Monitoring Viewer (`roles/monitoring.viewer`)](https://docs.cloud.google.com/monitoring/access-control#permissions-and-roles) role in addition to one of the roles listed below.

The broader roles include the more narrowly defined roles. For example, the Discovery Engine Editor role includes all of the permissions of the Discovery Engine Viewer role, along with the addition permissions of the Discovery Engine Editor role. Likewise, the Discovery Engine Admin role includes all of the permissions of the Discovery Engine Editor role, along with its additional permissions.

The basic roles (Owner, Editor, Viewer) provide permissions across Google Cloud. The roles specific to Agent Search provide only Agent Search permissions, except for the following Google Cloud permissions, which are needed for general Google Cloud usage:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `serviceusage.services.list`
  * `serviceusage.services.get`



The following table lists the Agent Search IAM roles with a corresponding list of all the permissions for each role.

Role | Permissions  
---|---  
  
#### Discovery Engine Admin 

(`roles/discoveryengine.admin`) Grants full access to all discoveryengine resources.  |  `cloudaicompanion.aiDevToolsSettings.*`

  * `cloudaicompanion.aiDevToolsSettings.create`
  * `cloudaicompanion.aiDevToolsSettings.delete`
  * `cloudaicompanion.aiDevToolsSettings.get`
  * `cloudaicompanion.aiDevToolsSettings.list`
  * `cloudaicompanion.aiDevToolsSettings.update`

`cloudaicompanion.codeRepositoryIndexes.*`

  * `cloudaicompanion.codeRepositoryIndexes.create`
  * `cloudaicompanion.codeRepositoryIndexes.delete`
  * `cloudaicompanion.codeRepositoryIndexes.get`
  * `cloudaicompanion.codeRepositoryIndexes.list`
  * `cloudaicompanion.codeRepositoryIndexes.update`

`cloudaicompanion.codeToolsSettings.*`

  * `cloudaicompanion.codeToolsSettings.create`
  * `cloudaicompanion.codeToolsSettings.delete`
  * `cloudaicompanion.codeToolsSettings.get`
  * `cloudaicompanion.codeToolsSettings.list`
  * `cloudaicompanion.codeToolsSettings.update`

`cloudaicompanion.dataSharingWithGoogleSettings.*`

  * `cloudaicompanion.dataSharingWithGoogleSettings.create`
  * `cloudaicompanion.dataSharingWithGoogleSettings.delete`
  * `cloudaicompanion.dataSharingWithGoogleSettings.get`
  * `cloudaicompanion.dataSharingWithGoogleSettings.list`
  * `cloudaicompanion.dataSharingWithGoogleSettings.update`

`cloudaicompanion.geminiGcpEnablementSettings.*`

  * `cloudaicompanion.geminiGcpEnablementSettings.create`
  * `cloudaicompanion.geminiGcpEnablementSettings.delete`
  * `cloudaicompanion.geminiGcpEnablementSettings.get`
  * `cloudaicompanion.geminiGcpEnablementSettings.list`
  * `cloudaicompanion.geminiGcpEnablementSettings.update`

`cloudaicompanion.gibqObservabilitySettings.*`

  * `cloudaicompanion.gibqObservabilitySettings.create`
  * `cloudaicompanion.gibqObservabilitySettings.delete`
  * `cloudaicompanion.gibqObservabilitySettings.get`
  * `cloudaicompanion.gibqObservabilitySettings.list`
  * `cloudaicompanion.gibqObservabilitySettings.update`

`cloudaicompanion.instances.queryEffectiveSetting` `cloudaicompanion.instances.queryEffectiveSettingBindings` `cloudaicompanion.loggingSettings.*`

  * `cloudaicompanion.loggingSettings.create`
  * `cloudaicompanion.loggingSettings.delete`
  * `cloudaicompanion.loggingSettings.get`
  * `cloudaicompanion.loggingSettings.list`
  * `cloudaicompanion.loggingSettings.update`

`cloudaicompanion.operations.*`

  * `cloudaicompanion.operations.cancel`
  * `cloudaicompanion.operations.delete`
  * `cloudaicompanion.operations.get`
  * `cloudaicompanion.operations.list`

`cloudaicompanion.releaseChannelSettings.*`

  * `cloudaicompanion.releaseChannelSettings.create`
  * `cloudaicompanion.releaseChannelSettings.delete`
  * `cloudaicompanion.releaseChannelSettings.get`
  * `cloudaicompanion.releaseChannelSettings.list`
  * `cloudaicompanion.releaseChannelSettings.update`

`cloudaicompanion.repositoryGroups.create` `cloudaicompanion.repositoryGroups.delete` `cloudaicompanion.repositoryGroups.get` `cloudaicompanion.repositoryGroups.getIamPolicy` `cloudaicompanion.repositoryGroups.list` `cloudaicompanion.repositoryGroups.setIamPolicy` `cloudaicompanion.repositoryGroups.update` `cloudaicompanion.settingBindings.*`

  * `cloudaicompanion.settingBindings.aiDevToolsSettingsCreate`
  * `cloudaicompanion.settingBindings.aiDevToolsSettingsDelete`
  * `cloudaicompanion.settingBindings.aiDevToolsSettingsGet`
  * `cloudaicompanion.settingBindings.aiDevToolsSettingsList`
  * `cloudaicompanion.settingBindings.aiDevToolsSettingsUpdate`
  * `cloudaicompanion.settingBindings.aiDevToolsSettingsUse`
  * `cloudaicompanion.settingBindings.codeToolsSettingsCreate`
  * `cloudaicompanion.settingBindings.codeToolsSettingsDelete`
  * `cloudaicompanion.settingBindings.codeToolsSettingsGet`
  * `cloudaicompanion.settingBindings.codeToolsSettingsList`
  * `cloudaicompanion.settingBindings.codeToolsSettingsUpdate`
  * `cloudaicompanion.settingBindings.codeToolsSettingsUse`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsCreate`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsDelete`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsGet`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsList`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsUpdate`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsUse`
  * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsCreate`
  * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsDelete`
  * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsGet`
  * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsList`
  * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsUpdate`
  * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsUse`
  * `cloudaicompanion.settingBindings.gibqObservabilitySettingsCreate`
  * `cloudaicompanion.settingBindings.gibqObservabilitySettingsDelete`
  * `cloudaicompanion.settingBindings.gibqObservabilitySettingsGet`
  * `cloudaicompanion.settingBindings.gibqObservabilitySettingsList`
  * `cloudaicompanion.settingBindings.gibqObservabilitySettingsUpdate`
  * `cloudaicompanion.settingBindings.gibqObservabilitySettingsUse`
  * `cloudaicompanion.settingBindings.loggingSettingsCreate`
  * `cloudaicompanion.settingBindings.loggingSettingsDelete`
  * `cloudaicompanion.settingBindings.loggingSettingsGet`
  * `cloudaicompanion.settingBindings.loggingSettingsList`
  * `cloudaicompanion.settingBindings.loggingSettingsUpdate`
  * `cloudaicompanion.settingBindings.loggingSettingsUse`
  * `cloudaicompanion.settingBindings.releaseChannelSettingsCreate`
  * `cloudaicompanion.settingBindings.releaseChannelSettingsDelete`
  * `cloudaicompanion.settingBindings.releaseChannelSettingsGet`
  * `cloudaicompanion.settingBindings.releaseChannelSettingsList`
  * `cloudaicompanion.settingBindings.releaseChannelSettingsUpdate`
  * `cloudaicompanion.settingBindings.releaseChannelSettingsUse`

`cloudnotifications.activities.list` `cloudtrace.insights.*`

  * `cloudtrace.insights.get`
  * `cloudtrace.insights.list`

`cloudtrace.stats.get` `cloudtrace.tasks.*`

  * `cloudtrace.tasks.create`
  * `cloudtrace.tasks.delete`
  * `cloudtrace.tasks.get`
  * `cloudtrace.tasks.list`

`cloudtrace.traceScopes.*`

  * `cloudtrace.traceScopes.create`
  * `cloudtrace.traceScopes.delete`
  * `cloudtrace.traceScopes.get`
  * `cloudtrace.traceScopes.list`
  * `cloudtrace.traceScopes.update`

`cloudtrace.traces.get` `cloudtrace.traces.list` `consumerprocurement.entitlements.*`

  * `consumerprocurement.entitlements.get`
  * `consumerprocurement.entitlements.list`

`discoveryengine.accounts.create` `discoveryengine.aclConfigs.*`

  * `discoveryengine.aclConfigs.get`
  * `discoveryengine.aclConfigs.update`

`discoveryengine.agentFiles.*`

  * `discoveryengine.agentFiles.delete`
  * `discoveryengine.agentFiles.download`
  * `discoveryengine.agentFiles.import`
  * `discoveryengine.agentFiles.list`
  * `discoveryengine.agentFiles.upload`

`discoveryengine.agentIamProposals.*`

  * `discoveryengine.agentIamProposals.create`
  * `discoveryengine.agentIamProposals.delete`
  * `discoveryengine.agentIamProposals.get`
  * `discoveryengine.agentIamProposals.list`

`discoveryengine.agents.create` `discoveryengine.agents.delete` `discoveryengine.agents.get` `discoveryengine.agents.getAgentView` `discoveryengine.agents.getIamPolicy` `discoveryengine.agents.list` `discoveryengine.agents.listAvailableAgentViews` `discoveryengine.agents.manage` `discoveryengine.agents.setIamPolicy` `discoveryengine.agents.update` `discoveryengine.alertPolicies.*`

  * `discoveryengine.alertPolicies.create`
  * `discoveryengine.alertPolicies.get`
  * `discoveryengine.alertPolicies.update`

`discoveryengine.analytics.*`

  * `discoveryengine.analytics.acquireDashboardSession`
  * `discoveryengine.analytics.refreshDashboardSessionTokens`

`discoveryengine.answers.get` `discoveryengine.assistAnswers.get` `discoveryengine.assistants.*`

  * `discoveryengine.assistants.assist`
  * `discoveryengine.assistants.create`
  * `discoveryengine.assistants.delete`
  * `discoveryengine.assistants.get`
  * `discoveryengine.assistants.list`
  * `discoveryengine.assistants.update`

`discoveryengine.audioOverviews.*`

  * `discoveryengine.audioOverviews.create`
  * `discoveryengine.audioOverviews.delete`
  * `discoveryengine.audioOverviews.get`
  * `discoveryengine.audioOverviews.getIceConfig`
  * `discoveryengine.audioOverviews.sendSdpOffer`

`discoveryengine.authorizations.*`

  * `discoveryengine.authorizations.create`
  * `discoveryengine.authorizations.delete`
  * `discoveryengine.authorizations.get`
  * `discoveryengine.authorizations.list`
  * `discoveryengine.authorizations.storeUserAuthorization`
  * `discoveryengine.authorizations.update`

`discoveryengine.billingAccountLicenseConfigs.*`

  * `discoveryengine.billingAccountLicenseConfigs.distribute`
  * `discoveryengine.billingAccountLicenseConfigs.get`
  * `discoveryengine.billingAccountLicenseConfigs.list`
  * `discoveryengine.billingAccountLicenseConfigs.retract`

`discoveryengine.branches.*`

  * `discoveryengine.branches.get`
  * `discoveryengine.branches.list`

`discoveryengine.cannedQueries.*`

  * `discoveryengine.cannedQueries.create`
  * `discoveryengine.cannedQueries.delete`
  * `discoveryengine.cannedQueries.get`
  * `discoveryengine.cannedQueries.list`
  * `discoveryengine.cannedQueries.listActiveCannedQueryUserViews`
  * `discoveryengine.cannedQueries.update`

`discoveryengine.cmekConfigs.*`

  * `discoveryengine.cmekConfigs.delete`
  * `discoveryengine.cmekConfigs.get`
  * `discoveryengine.cmekConfigs.list`
  * `discoveryengine.cmekConfigs.update`

`discoveryengine.collections.*`

  * `discoveryengine.collections.delete`
  * `discoveryengine.collections.get`
  * `discoveryengine.collections.getIamPolicy`
  * `discoveryengine.collections.list`
  * `discoveryengine.collections.setIamPolicy`

`discoveryengine.completionConfigs.*`

  * `discoveryengine.completionConfigs.completeQuery`
  * `discoveryengine.completionConfigs.get`
  * `discoveryengine.completionConfigs.removeSuggestion`
  * `discoveryengine.completionConfigs.update`

`discoveryengine.completionSuggestions.*`

  * `discoveryengine.completionSuggestions.import`
  * `discoveryengine.completionSuggestions.purge`

`discoveryengine.connectorRuns.*`

  * `discoveryengine.connectorRuns.cancel`
  * `discoveryengine.connectorRuns.list`

`discoveryengine.controls.*`

  * `discoveryengine.controls.create`
  * `discoveryengine.controls.delete`
  * `discoveryengine.controls.get`
  * `discoveryengine.controls.list`
  * `discoveryengine.controls.update`

`discoveryengine.conversations.*`

  * `discoveryengine.conversations.converse`
  * `discoveryengine.conversations.create`
  * `discoveryengine.conversations.delete`
  * `discoveryengine.conversations.get`
  * `discoveryengine.conversations.list`
  * `discoveryengine.conversations.update`

`discoveryengine.dataConnectors.*`

  * `discoveryengine.dataConnectors.acquireAccessToken`
  * `discoveryengine.dataConnectors.acquireAndStoreRefreshToken`
  * `discoveryengine.dataConnectors.buildActionInvocation`
  * `discoveryengine.dataConnectors.checkRefreshToken`
  * `discoveryengine.dataConnectors.executeAction`
  * `discoveryengine.dataConnectors.get`
  * `discoveryengine.dataConnectors.queryAvailableActions`
  * `discoveryengine.dataConnectors.startConnectorRun`
  * `discoveryengine.dataConnectors.update`

`discoveryengine.dataStores.*`

  * `discoveryengine.dataStores.completeQuery`
  * `discoveryengine.dataStores.create`
  * `discoveryengine.dataStores.delete`
  * `discoveryengine.dataStores.enrollSolutions`
  * `discoveryengine.dataStores.get`
  * `discoveryengine.dataStores.getIamPolicy`
  * `discoveryengine.dataStores.list`
  * `discoveryengine.dataStores.listCustomModels`
  * `discoveryengine.dataStores.setIamPolicy`
  * `discoveryengine.dataStores.trainCustomModel`
  * `discoveryengine.dataStores.update`

`discoveryengine.devToolsConfigs.*`

  * `discoveryengine.devToolsConfigs.get`
  * `discoveryengine.devToolsConfigs.update`

`discoveryengine.documentProcessingConfigs.*`

  * `discoveryengine.documentProcessingConfigs.get`
  * `discoveryengine.documentProcessingConfigs.update`

`discoveryengine.documents.*`

  * `discoveryengine.documents.batchGetDocumentsMetadata`
  * `discoveryengine.documents.create`
  * `discoveryengine.documents.delete`
  * `discoveryengine.documents.get`
  * `discoveryengine.documents.import`
  * `discoveryengine.documents.list`
  * `discoveryengine.documents.purge`
  * `discoveryengine.documents.update`

`discoveryengine.engines.*`

  * `discoveryengine.engines.create`
  * `discoveryengine.engines.createEngineUserData`
  * `discoveryengine.engines.delete`
  * `discoveryengine.engines.generateMemories`
  * `discoveryengine.engines.generatePersonalContext`
  * `discoveryengine.engines.get`
  * `discoveryengine.engines.getEngineUserData`
  * `discoveryengine.engines.getIamPolicy`
  * `discoveryengine.engines.getPersonalContext`
  * `discoveryengine.engines.list`
  * `discoveryengine.engines.pause`
  * `discoveryengine.engines.resume`
  * `discoveryengine.engines.setIamPolicy`
  * `discoveryengine.engines.tune`
  * `discoveryengine.engines.update`
  * `discoveryengine.engines.updateEngineUserData`

`discoveryengine.evaluations.*`

  * `discoveryengine.evaluations.create`
  * `discoveryengine.evaluations.get`
  * `discoveryengine.evaluations.list`

`discoveryengine.groundingConfigs.check` `discoveryengine.homepageDataConfigs.fetchDocuments` `discoveryengine.ideaForgeIdeas.*`

  * `discoveryengine.ideaForgeIdeas.create`
  * `discoveryengine.ideaForgeIdeas.get`

`discoveryengine.ideaForgeInstances.*`

  * `discoveryengine.ideaForgeInstances.get`
  * `discoveryengine.ideaForgeInstances.start`
  * `discoveryengine.ideaForgeInstances.stop`

`discoveryengine.identityMappingStores.*`

  * `discoveryengine.identityMappingStores.create`
  * `discoveryengine.identityMappingStores.delete`
  * `discoveryengine.identityMappingStores.get`
  * `discoveryengine.identityMappingStores.importIdentityMappings`
  * `discoveryengine.identityMappingStores.list`
  * `discoveryengine.identityMappingStores.listIdentityMappings`
  * `discoveryengine.identityMappingStores.purgeIdentityMappings`

`discoveryengine.immersiveArtifacts.*`

  * `discoveryengine.immersiveArtifacts.create`
  * `discoveryengine.immersiveArtifacts.delete`
  * `discoveryengine.immersiveArtifacts.export`
  * `discoveryengine.immersiveArtifacts.get`
  * `discoveryengine.immersiveArtifacts.list`
  * `discoveryengine.immersiveArtifacts.navigate`
  * `discoveryengine.immersiveArtifacts.update`

`discoveryengine.licenseConfigs.*`

  * `discoveryengine.licenseConfigs.create`
  * `discoveryengine.licenseConfigs.get`
  * `discoveryengine.licenseConfigs.list`
  * `discoveryengine.licenseConfigs.update`

`discoveryengine.locations.*`

  * `discoveryengine.locations.buildAuthorizationUrl`
  * `discoveryengine.locations.completeExternalIdentities`
  * `discoveryengine.locations.estimateDataSize`
  * `discoveryengine.locations.exchangeAuthCredentials`
  * `discoveryengine.locations.fetchAgentCards`
  * `discoveryengine.locations.getConnectorSource`
  * `discoveryengine.locations.listConnectorSources`
  * `discoveryengine.locations.setUpDataConnector`

`discoveryengine.memories.*`

  * `discoveryengine.memories.delete`
  * `discoveryengine.memories.list`
  * `discoveryengine.memories.retrieve`
  * `discoveryengine.memories.update`

`discoveryengine.models.*`

  * `discoveryengine.models.create`
  * `discoveryengine.models.delete`
  * `discoveryengine.models.get`
  * `discoveryengine.models.list`
  * `discoveryengine.models.pause`
  * `discoveryengine.models.resume`
  * `discoveryengine.models.tune`
  * `discoveryengine.models.update`

`discoveryengine.notebooks.*`

  * `discoveryengine.notebooks.create`
  * `discoveryengine.notebooks.generateGuide`
  * `discoveryengine.notebooks.get`
  * `discoveryengine.notebooks.getAnalytics`
  * `discoveryengine.notebooks.getIamPolicy`
  * `discoveryengine.notebooks.interactSources`
  * `discoveryengine.notebooks.list`
  * `discoveryengine.notebooks.removeSelf`
  * `discoveryengine.notebooks.setIamPolicy`
  * `discoveryengine.notebooks.update`

`discoveryengine.notes.*`

  * `discoveryengine.notes.create`
  * `discoveryengine.notes.delete`
  * `discoveryengine.notes.get`
  * `discoveryengine.notes.update`

`discoveryengine.notificationMessages.*`

  * `discoveryengine.notificationMessages.ackAll`
  * `discoveryengine.notificationMessages.list`
  * `discoveryengine.notificationMessages.update`

`discoveryengine.operations.*`

  * `discoveryengine.operations.get`
  * `discoveryengine.operations.list`

`discoveryengine.podcasts.create` `discoveryengine.projectOverageConfigs.get` `discoveryengine.projects.*`

  * `discoveryengine.projects.get`
  * `discoveryengine.projects.provision`
  * `discoveryengine.projects.reportConsentChange`
  * `discoveryengine.projects.update`

`discoveryengine.rankingConfigs.rank` `discoveryengine.sampleQueries.*`

  * `discoveryengine.sampleQueries.create`
  * `discoveryengine.sampleQueries.delete`
  * `discoveryengine.sampleQueries.get`
  * `discoveryengine.sampleQueries.import`
  * `discoveryengine.sampleQueries.list`
  * `discoveryengine.sampleQueries.update`

`discoveryengine.sampleQuerySets.*`

  * `discoveryengine.sampleQuerySets.create`
  * `discoveryengine.sampleQuerySets.delete`
  * `discoveryengine.sampleQuerySets.get`
  * `discoveryengine.sampleQuerySets.list`
  * `discoveryengine.sampleQuerySets.update`

`discoveryengine.schemas.*`

  * `discoveryengine.schemas.create`
  * `discoveryengine.schemas.delete`
  * `discoveryengine.schemas.get`
  * `discoveryengine.schemas.list`
  * `discoveryengine.schemas.preview`
  * `discoveryengine.schemas.update`
  * `discoveryengine.schemas.validate`

`discoveryengine.servingConfigs.*`

  * `discoveryengine.servingConfigs.answer`
  * `discoveryengine.servingConfigs.create`
  * `discoveryengine.servingConfigs.delete`
  * `discoveryengine.servingConfigs.get`
  * `discoveryengine.servingConfigs.list`
  * `discoveryengine.servingConfigs.recommend`
  * `discoveryengine.servingConfigs.search`
  * `discoveryengine.servingConfigs.update`

`discoveryengine.sessions.*`

  * `discoveryengine.sessions.addContextFile`
  * `discoveryengine.sessions.create`
  * `discoveryengine.sessions.delete`
  * `discoveryengine.sessions.downloadFile`
  * `discoveryengine.sessions.generateSummary`
  * `discoveryengine.sessions.get`
  * `discoveryengine.sessions.list`
  * `discoveryengine.sessions.listSessionFileMetadata`
  * `discoveryengine.sessions.recommendQuestions`
  * `discoveryengine.sessions.removeContextFile`
  * `discoveryengine.sessions.search`
  * `discoveryengine.sessions.selectContextFiles`
  * `discoveryengine.sessions.update`
  * `discoveryengine.sessions.uploadFile`

`discoveryengine.sharedContents.*`

  * `discoveryengine.sharedContents.create`
  * `discoveryengine.sharedContents.delete`
  * `discoveryengine.sharedContents.get`
  * `discoveryengine.sharedContents.list`

`discoveryengine.siteSearchEngines.*`

  * `discoveryengine.siteSearchEngines.batchVerifyTargetSites`
  * `discoveryengine.siteSearchEngines.disableAdvancedSiteSearch`
  * `discoveryengine.siteSearchEngines.enableAdvancedSiteSearch`
  * `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus`
  * `discoveryengine.siteSearchEngines.get`
  * `discoveryengine.siteSearchEngines.recrawlUris`

`discoveryengine.sitemaps.*`

  * `discoveryengine.sitemaps.create`
  * `discoveryengine.sitemaps.delete`
  * `discoveryengine.sitemaps.fetch`

`discoveryengine.sources.*`

  * `discoveryengine.sources.checkFreshness`
  * `discoveryengine.sources.create`
  * `discoveryengine.sources.delete`
  * `discoveryengine.sources.generateDocumentGuide`
  * `discoveryengine.sources.get`
  * `discoveryengine.sources.refresh`
  * `discoveryengine.sources.update`

`discoveryengine.suggestionDenyListEntries.*`

  * `discoveryengine.suggestionDenyListEntries.import`
  * `discoveryengine.suggestionDenyListEntries.purge`

`discoveryengine.targetSites.*`

  * `discoveryengine.targetSites.batchCreate`
  * `discoveryengine.targetSites.create`
  * `discoveryengine.targetSites.delete`
  * `discoveryengine.targetSites.get`
  * `discoveryengine.targetSites.list`
  * `discoveryengine.targetSites.update`

`discoveryengine.userEvents.*`

  * `discoveryengine.userEvents.create`
  * `discoveryengine.userEvents.fetchStats`
  * `discoveryengine.userEvents.import`
  * `discoveryengine.userEvents.purge`

`discoveryengine.userStores.*`

  * `discoveryengine.userStores.batchUpdateUserLicenses`
  * `discoveryengine.userStores.get`
  * `discoveryengine.userStores.listUserLicenses`
  * `discoveryengine.userStores.update`

`discoveryengine.users.*`

  * `discoveryengine.users.get`
  * `discoveryengine.users.update`

`discoveryengine.widgetConfigs.*`

  * `discoveryengine.widgetConfigs.get`
  * `discoveryengine.widgetConfigs.update`

`logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.exclusions.get` `logging.exclusions.list` `logging.links.get` `logging.links.list` `logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.list` `logging.logMetrics.get` `logging.logMetrics.list` `logging.logScopes.get` `logging.logScopes.list` `logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.get` `logging.notificationRules.list` `logging.operations.get` `logging.operations.list` `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `logging.settings.get` `logging.sinks.get` `logging.sinks.list` `logging.usage.get` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.list` `monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `observability.scopes.get` `observability.traceScopes.*`

  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`

`opsconfigmonitoring.resourceMetadata.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get` `stackdriver.resourceMetadata.list`  
  
#### Discovery Engine Editor 

(`roles/discoveryengine.editor`) Grants read and write access to all discovery engine resources.  |  `discoveryengine.accounts.create` `discoveryengine.aclConfigs.get` `discoveryengine.agentFiles.*`

  * `discoveryengine.agentFiles.delete`
  * `discoveryengine.agentFiles.download`
  * `discoveryengine.agentFiles.import`
  * `discoveryengine.agentFiles.list`
  * `discoveryengine.agentFiles.upload`

`discoveryengine.agents.create` `discoveryengine.agents.delete` `discoveryengine.agents.get` `discoveryengine.agents.getAgentView` `discoveryengine.agents.getIamPolicy` `discoveryengine.agents.list` `discoveryengine.agents.listAvailableAgentViews` `discoveryengine.agents.manage` `discoveryengine.agents.update` `discoveryengine.alertPolicies.*`

  * `discoveryengine.alertPolicies.create`
  * `discoveryengine.alertPolicies.get`
  * `discoveryengine.alertPolicies.update`

`discoveryengine.analytics.*`

  * `discoveryengine.analytics.acquireDashboardSession`
  * `discoveryengine.analytics.refreshDashboardSessionTokens`

`discoveryengine.answers.get` `discoveryengine.assistAnswers.get` `discoveryengine.assistants.*`

  * `discoveryengine.assistants.assist`
  * `discoveryengine.assistants.create`
  * `discoveryengine.assistants.delete`
  * `discoveryengine.assistants.get`
  * `discoveryengine.assistants.list`
  * `discoveryengine.assistants.update`

`discoveryengine.authorizations.storeUserAuthorization` `discoveryengine.branches.*`

  * `discoveryengine.branches.get`
  * `discoveryengine.branches.list`

`discoveryengine.cannedQueries.get` `discoveryengine.cannedQueries.list` `discoveryengine.cannedQueries.listActiveCannedQueryUserViews` `discoveryengine.cmekConfigs.get` `discoveryengine.cmekConfigs.list` `discoveryengine.collections.get` `discoveryengine.collections.list` `discoveryengine.completionConfigs.*`

  * `discoveryengine.completionConfigs.completeQuery`
  * `discoveryengine.completionConfigs.get`
  * `discoveryengine.completionConfigs.removeSuggestion`
  * `discoveryengine.completionConfigs.update`

`discoveryengine.connectorRuns.list` `discoveryengine.controls.*`

  * `discoveryengine.controls.create`
  * `discoveryengine.controls.delete`
  * `discoveryengine.controls.get`
  * `discoveryengine.controls.list`
  * `discoveryengine.controls.update`

`discoveryengine.conversations.*`

  * `discoveryengine.conversations.converse`
  * `discoveryengine.conversations.create`
  * `discoveryengine.conversations.delete`
  * `discoveryengine.conversations.get`
  * `discoveryengine.conversations.list`
  * `discoveryengine.conversations.update`

`discoveryengine.dataConnectors.*`

  * `discoveryengine.dataConnectors.acquireAccessToken`
  * `discoveryengine.dataConnectors.acquireAndStoreRefreshToken`
  * `discoveryengine.dataConnectors.buildActionInvocation`
  * `discoveryengine.dataConnectors.checkRefreshToken`
  * `discoveryengine.dataConnectors.executeAction`
  * `discoveryengine.dataConnectors.get`
  * `discoveryengine.dataConnectors.queryAvailableActions`
  * `discoveryengine.dataConnectors.startConnectorRun`
  * `discoveryengine.dataConnectors.update`

`discoveryengine.dataStores.completeQuery` `discoveryengine.dataStores.create` `discoveryengine.dataStores.delete` `discoveryengine.dataStores.enrollSolutions` `discoveryengine.dataStores.get` `discoveryengine.dataStores.list` `discoveryengine.dataStores.listCustomModels` `discoveryengine.dataStores.trainCustomModel` `discoveryengine.dataStores.update` `discoveryengine.devToolsConfigs.get` `discoveryengine.documentProcessingConfigs.*`

  * `discoveryengine.documentProcessingConfigs.get`
  * `discoveryengine.documentProcessingConfigs.update`

`discoveryengine.documents.*`

  * `discoveryengine.documents.batchGetDocumentsMetadata`
  * `discoveryengine.documents.create`
  * `discoveryengine.documents.delete`
  * `discoveryengine.documents.get`
  * `discoveryengine.documents.import`
  * `discoveryengine.documents.list`
  * `discoveryengine.documents.purge`
  * `discoveryengine.documents.update`

`discoveryengine.engines.create` `discoveryengine.engines.createEngineUserData` `discoveryengine.engines.delete` `discoveryengine.engines.generateMemories` `discoveryengine.engines.generatePersonalContext` `discoveryengine.engines.get` `discoveryengine.engines.getEngineUserData` `discoveryengine.engines.getIamPolicy` `discoveryengine.engines.getPersonalContext` `discoveryengine.engines.list` `discoveryengine.engines.pause` `discoveryengine.engines.resume` `discoveryengine.engines.tune` `discoveryengine.engines.update` `discoveryengine.engines.updateEngineUserData` `discoveryengine.evaluations.*`

  * `discoveryengine.evaluations.create`
  * `discoveryengine.evaluations.get`
  * `discoveryengine.evaluations.list`

`discoveryengine.groundingConfigs.check` `discoveryengine.homepageDataConfigs.fetchDocuments` `discoveryengine.ideaForgeIdeas.*`

  * `discoveryengine.ideaForgeIdeas.create`
  * `discoveryengine.ideaForgeIdeas.get`

`discoveryengine.ideaForgeInstances.*`

  * `discoveryengine.ideaForgeInstances.get`
  * `discoveryengine.ideaForgeInstances.start`
  * `discoveryengine.ideaForgeInstances.stop`

`discoveryengine.identityMappingStores.*`

  * `discoveryengine.identityMappingStores.create`
  * `discoveryengine.identityMappingStores.delete`
  * `discoveryengine.identityMappingStores.get`
  * `discoveryengine.identityMappingStores.importIdentityMappings`
  * `discoveryengine.identityMappingStores.list`
  * `discoveryengine.identityMappingStores.listIdentityMappings`
  * `discoveryengine.identityMappingStores.purgeIdentityMappings`

`discoveryengine.immersiveArtifacts.*`

  * `discoveryengine.immersiveArtifacts.create`
  * `discoveryengine.immersiveArtifacts.delete`
  * `discoveryengine.immersiveArtifacts.export`
  * `discoveryengine.immersiveArtifacts.get`
  * `discoveryengine.immersiveArtifacts.list`
  * `discoveryengine.immersiveArtifacts.navigate`
  * `discoveryengine.immersiveArtifacts.update`

`discoveryengine.licenseConfigs.*`

  * `discoveryengine.licenseConfigs.create`
  * `discoveryengine.licenseConfigs.get`
  * `discoveryengine.licenseConfigs.list`
  * `discoveryengine.licenseConfigs.update`

`discoveryengine.locations.completeExternalIdentities` `discoveryengine.locations.estimateDataSize` `discoveryengine.locations.exchangeAuthCredentials` `discoveryengine.locations.fetchAgentCards` `discoveryengine.locations.getConnectorSource` `discoveryengine.locations.listConnectorSources` `discoveryengine.locations.setUpDataConnector` `discoveryengine.memories.*`

  * `discoveryengine.memories.delete`
  * `discoveryengine.memories.list`
  * `discoveryengine.memories.retrieve`
  * `discoveryengine.memories.update`

`discoveryengine.models.*`

  * `discoveryengine.models.create`
  * `discoveryengine.models.delete`
  * `discoveryengine.models.get`
  * `discoveryengine.models.list`
  * `discoveryengine.models.pause`
  * `discoveryengine.models.resume`
  * `discoveryengine.models.tune`
  * `discoveryengine.models.update`

`discoveryengine.notebooks.create` `discoveryengine.notebooks.list` `discoveryengine.notificationMessages.*`

  * `discoveryengine.notificationMessages.ackAll`
  * `discoveryengine.notificationMessages.list`
  * `discoveryengine.notificationMessages.update`

`discoveryengine.operations.*`

  * `discoveryengine.operations.get`
  * `discoveryengine.operations.list`

`discoveryengine.podcasts.create` `discoveryengine.projectOverageConfigs.get` `discoveryengine.projects.get` `discoveryengine.projects.provision` `discoveryengine.projects.reportConsentChange` `discoveryengine.rankingConfigs.rank` `discoveryengine.sampleQueries.*`

  * `discoveryengine.sampleQueries.create`
  * `discoveryengine.sampleQueries.delete`
  * `discoveryengine.sampleQueries.get`
  * `discoveryengine.sampleQueries.import`
  * `discoveryengine.sampleQueries.list`
  * `discoveryengine.sampleQueries.update`

`discoveryengine.sampleQuerySets.*`

  * `discoveryengine.sampleQuerySets.create`
  * `discoveryengine.sampleQuerySets.delete`
  * `discoveryengine.sampleQuerySets.get`
  * `discoveryengine.sampleQuerySets.list`
  * `discoveryengine.sampleQuerySets.update`

`discoveryengine.schemas.*`

  * `discoveryengine.schemas.create`
  * `discoveryengine.schemas.delete`
  * `discoveryengine.schemas.get`
  * `discoveryengine.schemas.list`
  * `discoveryengine.schemas.preview`
  * `discoveryengine.schemas.update`
  * `discoveryengine.schemas.validate`

`discoveryengine.servingConfigs.*`

  * `discoveryengine.servingConfigs.answer`
  * `discoveryengine.servingConfigs.create`
  * `discoveryengine.servingConfigs.delete`
  * `discoveryengine.servingConfigs.get`
  * `discoveryengine.servingConfigs.list`
  * `discoveryengine.servingConfigs.recommend`
  * `discoveryengine.servingConfigs.search`
  * `discoveryengine.servingConfigs.update`

`discoveryengine.sessions.*`

  * `discoveryengine.sessions.addContextFile`
  * `discoveryengine.sessions.create`
  * `discoveryengine.sessions.delete`
  * `discoveryengine.sessions.downloadFile`
  * `discoveryengine.sessions.generateSummary`
  * `discoveryengine.sessions.get`
  * `discoveryengine.sessions.list`
  * `discoveryengine.sessions.listSessionFileMetadata`
  * `discoveryengine.sessions.recommendQuestions`
  * `discoveryengine.sessions.removeContextFile`
  * `discoveryengine.sessions.search`
  * `discoveryengine.sessions.selectContextFiles`
  * `discoveryengine.sessions.update`
  * `discoveryengine.sessions.uploadFile`

`discoveryengine.sharedContents.*`

  * `discoveryengine.sharedContents.create`
  * `discoveryengine.sharedContents.delete`
  * `discoveryengine.sharedContents.get`
  * `discoveryengine.sharedContents.list`

`discoveryengine.siteSearchEngines.*`

  * `discoveryengine.siteSearchEngines.batchVerifyTargetSites`
  * `discoveryengine.siteSearchEngines.disableAdvancedSiteSearch`
  * `discoveryengine.siteSearchEngines.enableAdvancedSiteSearch`
  * `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus`
  * `discoveryengine.siteSearchEngines.get`
  * `discoveryengine.siteSearchEngines.recrawlUris`

`discoveryengine.sitemaps.*`

  * `discoveryengine.sitemaps.create`
  * `discoveryengine.sitemaps.delete`
  * `discoveryengine.sitemaps.fetch`

`discoveryengine.suggestionDenyListEntries.*`

  * `discoveryengine.suggestionDenyListEntries.import`
  * `discoveryengine.suggestionDenyListEntries.purge`

`discoveryengine.targetSites.create` `discoveryengine.targetSites.delete` `discoveryengine.targetSites.get` `discoveryengine.targetSites.list` `discoveryengine.targetSites.update` `discoveryengine.userEvents.*`

  * `discoveryengine.userEvents.create`
  * `discoveryengine.userEvents.fetchStats`
  * `discoveryengine.userEvents.import`
  * `discoveryengine.userEvents.purge`

`discoveryengine.userStores.batchUpdateUserLicenses` `discoveryengine.userStores.get` `discoveryengine.userStores.listUserLicenses` `discoveryengine.widgetConfigs.*`

  * `discoveryengine.widgetConfigs.get`
  * `discoveryengine.widgetConfigs.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Discovery Engine User 

(`roles/discoveryengine.user`) Grants user-level access to Discovery Engine resources.  |  `businessaicode.*`

  * `businessaicode.locations.fetchQuotaStatus`
  * `businessaicode.locations.generateContent`
  * `businessaicode.locations.queryConfiguration`
  * `businessaicode.locations.selfAssignLicense`
  * `businessaicode.locations.sendTelemetry`

`cloudaicompanion.companions.*`

  * `cloudaicompanion.companions.generateChat`
  * `cloudaicompanion.companions.generateCode`

`cloudaicompanion.entitlements.get` `cloudaicompanion.instances.*`

  * `cloudaicompanion.instances.completeCode`
  * `cloudaicompanion.instances.completeTask`
  * `cloudaicompanion.instances.exportMetrics`
  * `cloudaicompanion.instances.generateCode`
  * `cloudaicompanion.instances.generateText`
  * `cloudaicompanion.instances.queryEffectiveSetting`
  * `cloudaicompanion.instances.queryEffectiveSettingBindings`

`cloudaicompanion.licenses.selfAssign` `cloudaicompanion.operations.get` `cloudaicompanion.topics.create` `discoveryengine.accounts.create` `discoveryengine.agentFiles.*`

  * `discoveryengine.agentFiles.delete`
  * `discoveryengine.agentFiles.download`
  * `discoveryengine.agentFiles.import`
  * `discoveryengine.agentFiles.list`
  * `discoveryengine.agentFiles.upload`

`discoveryengine.agentIamProposals.*`

  * `discoveryengine.agentIamProposals.create`
  * `discoveryengine.agentIamProposals.delete`
  * `discoveryengine.agentIamProposals.get`
  * `discoveryengine.agentIamProposals.list`

`discoveryengine.agents.create` `discoveryengine.agents.delete` `discoveryengine.agents.get` `discoveryengine.agents.getAgentView` `discoveryengine.agents.list` `discoveryengine.agents.listAvailableAgentViews` `discoveryengine.agents.requestReview` `discoveryengine.agents.update` `discoveryengine.answers.get` `discoveryengine.assistAnswers.get` `discoveryengine.assistants.assist` `discoveryengine.authorizations.storeUserAuthorization` `discoveryengine.cannedQueries.listActiveCannedQueryUserViews` `discoveryengine.collections.get` `discoveryengine.completionConfigs.completeQuery` `discoveryengine.completionConfigs.removeSuggestion` `discoveryengine.dataConnectors.acquireAccessToken` `discoveryengine.dataConnectors.acquireAndStoreRefreshToken` `discoveryengine.dataConnectors.buildActionInvocation` `discoveryengine.dataConnectors.checkRefreshToken` `discoveryengine.dataConnectors.executeAction` `discoveryengine.dataConnectors.queryAvailableActions` `discoveryengine.dataStores.get` `discoveryengine.devToolsConfigs.get` `discoveryengine.engines.createEngineUserData` `discoveryengine.engines.generateMemories` `discoveryengine.engines.generatePersonalContext` `discoveryengine.engines.get` `discoveryengine.engines.getEngineUserData` `discoveryengine.engines.getPersonalContext` `discoveryengine.engines.updateEngineUserData` `discoveryengine.homepageDataConfigs.fetchDocuments` `discoveryengine.ideaForgeIdeas.*`

  * `discoveryengine.ideaForgeIdeas.create`
  * `discoveryengine.ideaForgeIdeas.get`

`discoveryengine.ideaForgeInstances.*`

  * `discoveryengine.ideaForgeInstances.get`
  * `discoveryengine.ideaForgeInstances.start`
  * `discoveryengine.ideaForgeInstances.stop`

`discoveryengine.immersiveArtifacts.*`

  * `discoveryengine.immersiveArtifacts.create`
  * `discoveryengine.immersiveArtifacts.delete`
  * `discoveryengine.immersiveArtifacts.export`
  * `discoveryengine.immersiveArtifacts.get`
  * `discoveryengine.immersiveArtifacts.list`
  * `discoveryengine.immersiveArtifacts.navigate`
  * `discoveryengine.immersiveArtifacts.update`

`discoveryengine.locations.buildAuthorizationUrl` `discoveryengine.locations.completeExternalIdentities` `discoveryengine.locations.fetchAgentCards` `discoveryengine.memories.*`

  * `discoveryengine.memories.delete`
  * `discoveryengine.memories.list`
  * `discoveryengine.memories.retrieve`
  * `discoveryengine.memories.update`

`discoveryengine.notebooks.create` `discoveryengine.notebooks.list` `discoveryengine.notificationMessages.*`

  * `discoveryengine.notificationMessages.ackAll`
  * `discoveryengine.notificationMessages.list`
  * `discoveryengine.notificationMessages.update`

`discoveryengine.servingConfigs.answer` `discoveryengine.servingConfigs.recommend` `discoveryengine.servingConfigs.search` `discoveryengine.sessions.*`

  * `discoveryengine.sessions.addContextFile`
  * `discoveryengine.sessions.create`
  * `discoveryengine.sessions.delete`
  * `discoveryengine.sessions.downloadFile`
  * `discoveryengine.sessions.generateSummary`
  * `discoveryengine.sessions.get`
  * `discoveryengine.sessions.list`
  * `discoveryengine.sessions.listSessionFileMetadata`
  * `discoveryengine.sessions.recommendQuestions`
  * `discoveryengine.sessions.removeContextFile`
  * `discoveryengine.sessions.search`
  * `discoveryengine.sessions.selectContextFiles`
  * `discoveryengine.sessions.update`
  * `discoveryengine.sessions.uploadFile`

`discoveryengine.sharedContents.*`

  * `discoveryengine.sharedContents.create`
  * `discoveryengine.sharedContents.delete`
  * `discoveryengine.sharedContents.get`
  * `discoveryengine.sharedContents.list`

`discoveryengine.userEvents.create` `discoveryengine.users.*`

  * `discoveryengine.users.get`
  * `discoveryengine.users.update`

`discoveryengine.widgetConfigs.get` `geminicloudassist.agents.invoke` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test`  
  
#### Discovery Engine Viewer 

(`roles/discoveryengine.viewer`) Grants read access to all discovery engine resources.  |  `discoveryengine.aclConfigs.get` `discoveryengine.agentFiles.list` `discoveryengine.agents.get` `discoveryengine.agents.getAgentView` `discoveryengine.agents.getIamPolicy` `discoveryengine.agents.list` `discoveryengine.agents.listAvailableAgentViews` `discoveryengine.alertPolicies.get` `discoveryengine.analytics.*`

  * `discoveryengine.analytics.acquireDashboardSession`
  * `discoveryengine.analytics.refreshDashboardSessionTokens`

`discoveryengine.answers.get` `discoveryengine.assistAnswers.get` `discoveryengine.assistants.get` `discoveryengine.assistants.list` `discoveryengine.branches.*`

  * `discoveryengine.branches.get`
  * `discoveryengine.branches.list`

`discoveryengine.cannedQueries.get` `discoveryengine.cannedQueries.list` `discoveryengine.cannedQueries.listActiveCannedQueryUserViews` `discoveryengine.cmekConfigs.get` `discoveryengine.cmekConfigs.list` `discoveryengine.collections.get` `discoveryengine.collections.list` `discoveryengine.completionConfigs.completeQuery` `discoveryengine.completionConfigs.get` `discoveryengine.connectorRuns.list` `discoveryengine.controls.get` `discoveryengine.controls.list` `discoveryengine.conversations.converse` `discoveryengine.conversations.get` `discoveryengine.conversations.list` `discoveryengine.dataConnectors.buildActionInvocation` `discoveryengine.dataConnectors.checkRefreshToken` `discoveryengine.dataConnectors.get` `discoveryengine.dataConnectors.queryAvailableActions` `discoveryengine.dataStores.completeQuery` `discoveryengine.dataStores.get` `discoveryengine.dataStores.list` `discoveryengine.dataStores.listCustomModels` `discoveryengine.devToolsConfigs.get` `discoveryengine.documentProcessingConfigs.get` `discoveryengine.documents.batchGetDocumentsMetadata` `discoveryengine.documents.get` `discoveryengine.documents.list` `discoveryengine.engines.get` `discoveryengine.engines.getIamPolicy` `discoveryengine.engines.getPersonalContext` `discoveryengine.engines.list` `discoveryengine.evaluations.get` `discoveryengine.evaluations.list` `discoveryengine.groundingConfigs.check` `discoveryengine.homepageDataConfigs.fetchDocuments` `discoveryengine.ideaForgeIdeas.get` `discoveryengine.ideaForgeInstances.get` `discoveryengine.identityMappingStores.get` `discoveryengine.identityMappingStores.list` `discoveryengine.identityMappingStores.listIdentityMappings` `discoveryengine.immersiveArtifacts.export` `discoveryengine.immersiveArtifacts.get` `discoveryengine.immersiveArtifacts.list` `discoveryengine.locations.completeExternalIdentities` `discoveryengine.locations.fetchAgentCards` `discoveryengine.locations.getConnectorSource` `discoveryengine.locations.listConnectorSources` `discoveryengine.memories.list` `discoveryengine.memories.retrieve` `discoveryengine.models.get` `discoveryengine.models.list` `discoveryengine.notebooks.list` `discoveryengine.notificationMessages.list` `discoveryengine.operations.*`

  * `discoveryengine.operations.get`
  * `discoveryengine.operations.list`

`discoveryengine.projectOverageConfigs.get` `discoveryengine.projects.get` `discoveryengine.rankingConfigs.rank` `discoveryengine.sampleQueries.get` `discoveryengine.sampleQueries.list` `discoveryengine.sampleQuerySets.get` `discoveryengine.sampleQuerySets.list` `discoveryengine.schemas.get` `discoveryengine.schemas.list` `discoveryengine.schemas.preview` `discoveryengine.schemas.validate` `discoveryengine.servingConfigs.answer` `discoveryengine.servingConfigs.get` `discoveryengine.servingConfigs.list` `discoveryengine.servingConfigs.recommend` `discoveryengine.servingConfigs.search` `discoveryengine.sessions.downloadFile` `discoveryengine.sessions.generateSummary` `discoveryengine.sessions.get` `discoveryengine.sessions.list` `discoveryengine.sessions.listSessionFileMetadata` `discoveryengine.sessions.recommendQuestions` `discoveryengine.sharedContents.get` `discoveryengine.sharedContents.list` `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus` `discoveryengine.siteSearchEngines.get` `discoveryengine.sitemaps.fetch` `discoveryengine.targetSites.get` `discoveryengine.targetSites.list` `discoveryengine.userEvents.fetchStats` `discoveryengine.userStores.get` `discoveryengine.widgetConfigs.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Manage Agent Search IAM

You can get and set IAM allow policies and IAM roles using the Google Cloud Console. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## What's next

  * Learn how to [manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).
  * Learn more about [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
