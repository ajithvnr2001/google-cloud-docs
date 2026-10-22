---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle/
title: Google Security Operations roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:39.755669+00:00
---

# Google Security Operations roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Security Operations roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Security Operations. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Security Operations roles

Role | Permissions  
---|---  
  
#### Chronicle API Admin 

(`roles/chronicle.admin`) Full access to the Chronicle API services, including global settings.  |  `chronicle.agentSettings.*`

  * `chronicle.agentSettings.get`
  * `chronicle.agentSettings.update`

`chronicle.ais.*`

  * `chronicle.ais.createFeedback`
  * `chronicle.ais.translateUdmQuery`
  * `chronicle.ais.translateYlRule`

`chronicle.alertGroupingRules.*`

  * `chronicle.alertGroupingRules.delete`
  * `chronicle.alertGroupingRules.get`
  * `chronicle.alertGroupingRules.update`

`chronicle.analyticValues.list` `chronicle.analytics.list` `chronicle.announcements.*`

  * `chronicle.announcements.delete`
  * `chronicle.announcements.get`
  * `chronicle.announcements.update`

`chronicle.attachments.*`

  * `chronicle.attachments.delete`
  * `chronicle.attachments.get`
  * `chronicle.attachments.update`

`chronicle.bigQueryAccess.provide` `chronicle.bigQueryExport.*`

  * `chronicle.bigQueryExport.get`
  * `chronicle.bigQueryExport.provision`
  * `chronicle.bigQueryExport.update`

`chronicle.calculatedFieldDefinitions.*`

  * `chronicle.calculatedFieldDefinitions.delete`
  * `chronicle.calculatedFieldDefinitions.get`
  * `chronicle.calculatedFieldDefinitions.update`

`chronicle.caseAlerts.*`

  * `chronicle.caseAlerts.get`
  * `chronicle.caseAlerts.metadataUpdate`
  * `chronicle.caseAlerts.move`
  * `chronicle.caseAlerts.removeTag`
  * `chronicle.caseAlerts.updateSla`
  * `chronicle.caseAlerts.updateTag`

`chronicle.caseCloseDefinitions.*`

  * `chronicle.caseCloseDefinitions.delete`
  * `chronicle.caseCloseDefinitions.get`
  * `chronicle.caseCloseDefinitions.update`

`chronicle.caseComments.*`

  * `chronicle.caseComments.delete`
  * `chronicle.caseComments.get`
  * `chronicle.caseComments.update`

`chronicle.caseDetections.get` `chronicle.caseEvents.get` `chronicle.caseEvidenceDatas.get` `chronicle.caseQueueFilters.*`

  * `chronicle.caseQueueFilters.delete`
  * `chronicle.caseQueueFilters.get`
  * `chronicle.caseQueueFilters.update`

`chronicle.caseStageDefinitions.*`

  * `chronicle.caseStageDefinitions.delete`
  * `chronicle.caseStageDefinitions.get`
  * `chronicle.caseStageDefinitions.update`

`chronicle.caseTagDefinitions.*`

  * `chronicle.caseTagDefinitions.delete`
  * `chronicle.caseTagDefinitions.get`
  * `chronicle.caseTagDefinitions.update`

`chronicle.caseWallRecords.*`

  * `chronicle.caseWallRecords.get`
  * `chronicle.caseWallRecords.update`

`chronicle.cases.*`

  * `chronicle.cases.close`
  * `chronicle.cases.countPriorities`
  * `chronicle.cases.generateReport`
  * `chronicle.cases.get`
  * `chronicle.cases.removeTag`
  * `chronicle.cases.reopen`
  * `chronicle.cases.update`
  * `chronicle.cases.updateTag`

`chronicle.chatMessageAttachments.get` `chronicle.chatMessages.*`

  * `chronicle.chatMessages.create`
  * `chronicle.chatMessages.get`
  * `chronicle.chatMessages.pin`

`chronicle.chatSessionMessages.*`

  * `chronicle.chatSessionMessages.list`
  * `chronicle.chatSessionMessages.update`

`chronicle.chatSessions.*`

  * `chronicle.chatSessions.delete`
  * `chronicle.chatSessions.list`

`chronicle.collectors.*`

  * `chronicle.collectors.create`
  * `chronicle.collectors.delete`
  * `chronicle.collectors.get`
  * `chronicle.collectors.list`
  * `chronicle.collectors.update`

`chronicle.connectorEvents.get` `chronicle.connectorInstanceLogs.get` `chronicle.connectorInstances.*`

  * `chronicle.connectorInstances.delete`
  * `chronicle.connectorInstances.get`
  * `chronicle.connectorInstances.update`

`chronicle.connectorRevisions.*`

  * `chronicle.connectorRevisions.delete`
  * `chronicle.connectorRevisions.get`
  * `chronicle.connectorRevisions.update`

`chronicle.connectors.*`

  * `chronicle.connectors.delete`
  * `chronicle.connectors.get`
  * `chronicle.connectors.update`

`chronicle.contentPacks.*`

  * `chronicle.contentPacks.create`
  * `chronicle.contentPacks.delete`
  * `chronicle.contentPacks.export`
  * `chronicle.contentPacks.get`
  * `chronicle.contentPacks.install`

`chronicle.contextProperties.*`

  * `chronicle.contextProperties.delete`
  * `chronicle.contextProperties.get`
  * `chronicle.contextProperties.update`

`chronicle.conversations.*`

  * `chronicle.conversations.create`
  * `chronicle.conversations.delete`
  * `chronicle.conversations.get`
  * `chronicle.conversations.list`
  * `chronicle.conversations.update`

`chronicle.coverageDetails.*`

  * `chronicle.coverageDetails.get`
  * `chronicle.coverageDetails.list`

`chronicle.curatedRuleSetCategories.*`

  * `chronicle.curatedRuleSetCategories.countAllCuratedRuleSetDetections`
  * `chronicle.curatedRuleSetCategories.get`
  * `chronicle.curatedRuleSetCategories.list`

`chronicle.curatedRuleSetDeployments.*`

  * `chronicle.curatedRuleSetDeployments.batchUpdate`
  * `chronicle.curatedRuleSetDeployments.get`
  * `chronicle.curatedRuleSetDeployments.list`
  * `chronicle.curatedRuleSetDeployments.update`

`chronicle.curatedRuleSets.*`

  * `chronicle.curatedRuleSets.countCuratedRuleSetDetections`
  * `chronicle.curatedRuleSets.get`
  * `chronicle.curatedRuleSets.list`

`chronicle.curatedRules.*`

  * `chronicle.curatedRules.get`
  * `chronicle.curatedRules.list`

`chronicle.customFieldValues.*`

  * `chronicle.customFieldValues.get`
  * `chronicle.customFieldValues.update`

`chronicle.customFields.*`

  * `chronicle.customFields.delete`
  * `chronicle.customFields.get`
  * `chronicle.customFields.update`

`chronicle.customLists.*`

  * `chronicle.customLists.delete`
  * `chronicle.customLists.get`
  * `chronicle.customLists.update`

`chronicle.dashboardCharts.*`

  * `chronicle.dashboardCharts.get`
  * `chronicle.dashboardCharts.list`

`chronicle.dashboardQueries.*`

  * `chronicle.dashboardQueries.execute`
  * `chronicle.dashboardQueries.get`
  * `chronicle.dashboardQueries.list`

`chronicle.dashboardScheduledReports.*`

  * `chronicle.dashboardScheduledReports.create`
  * `chronicle.dashboardScheduledReports.delete`
  * `chronicle.dashboardScheduledReports.duplicate`
  * `chronicle.dashboardScheduledReports.fetchHistory`
  * `chronicle.dashboardScheduledReports.get`
  * `chronicle.dashboardScheduledReports.list`
  * `chronicle.dashboardScheduledReports.trigger`
  * `chronicle.dashboardScheduledReports.update`

`chronicle.dashboards.*`

  * `chronicle.dashboards.copy`
  * `chronicle.dashboards.create`
  * `chronicle.dashboards.delete`
  * `chronicle.dashboards.edit`
  * `chronicle.dashboards.get`
  * `chronicle.dashboards.list`
  * `chronicle.dashboards.schedule`

`chronicle.dataAccessLabels.*`

  * `chronicle.dataAccessLabels.create`
  * `chronicle.dataAccessLabels.delete`
  * `chronicle.dataAccessLabels.get`
  * `chronicle.dataAccessLabels.list`
  * `chronicle.dataAccessLabels.update`

`chronicle.dataAccessScopes.*`

  * `chronicle.dataAccessScopes.create`
  * `chronicle.dataAccessScopes.delete`
  * `chronicle.dataAccessScopes.get`
  * `chronicle.dataAccessScopes.list`
  * `chronicle.dataAccessScopes.permit`
  * `chronicle.dataAccessScopes.update`

`chronicle.dataExports.*`

  * `chronicle.dataExports.cancel`
  * `chronicle.dataExports.create`
  * `chronicle.dataExports.fetchLogTypesAvailableForExport`
  * `chronicle.dataExports.fetchServiceAccountForDataExport`
  * `chronicle.dataExports.get`
  * `chronicle.dataExports.list`
  * `chronicle.dataExports.update`

`chronicle.dataTableOperationErrors.get` `chronicle.dataTableRows.*`

  * `chronicle.dataTableRows.asyncBulkAppend`
  * `chronicle.dataTableRows.asyncBulkCreate`
  * `chronicle.dataTableRows.asyncBulkDelete`
  * `chronicle.dataTableRows.asyncBulkReplace`
  * `chronicle.dataTableRows.asyncBulkUpdate`
  * `chronicle.dataTableRows.bulkCreate`
  * `chronicle.dataTableRows.bulkDelete`
  * `chronicle.dataTableRows.bulkGet`
  * `chronicle.dataTableRows.bulkReplace`
  * `chronicle.dataTableRows.bulkUpdate`
  * `chronicle.dataTableRows.create`
  * `chronicle.dataTableRows.delete`
  * `chronicle.dataTableRows.get`
  * `chronicle.dataTableRows.list`
  * `chronicle.dataTableRows.update`

`chronicle.dataTables.*`

  * `chronicle.dataTables.bulkCreateDataTableAsync`
  * `chronicle.dataTables.create`
  * `chronicle.dataTables.delete`
  * `chronicle.dataTables.get`
  * `chronicle.dataTables.list`
  * `chronicle.dataTables.update`

`chronicle.dataTaps.*`

  * `chronicle.dataTaps.create`
  * `chronicle.dataTaps.delete`
  * `chronicle.dataTaps.get`
  * `chronicle.dataTaps.list`
  * `chronicle.dataTaps.update`

`chronicle.emailTemplates.*`

  * `chronicle.emailTemplates.delete`
  * `chronicle.emailTemplates.get`
  * `chronicle.emailTemplates.update`

`chronicle.enrichmentAgent.*`

  * `chronicle.enrichmentAgent.execute`
  * `chronicle.enrichmentAgent.get`

`chronicle.enrichmentCombination.get` `chronicle.enrichmentControls.*`

  * `chronicle.enrichmentControls.create`
  * `chronicle.enrichmentControls.delete`
  * `chronicle.enrichmentControls.disable`
  * `chronicle.enrichmentControls.get`
  * `chronicle.enrichmentControls.list`

`chronicle.entities.*`

  * `chronicle.entities.batchCreate`
  * `chronicle.entities.batchDelete`
  * `chronicle.entities.batchValidate`
  * `chronicle.entities.create`
  * `chronicle.entities.delete`
  * `chronicle.entities.find`
  * `chronicle.entities.findEntityAlerts`
  * `chronicle.entities.findRelatedEntities`
  * `chronicle.entities.get`
  * `chronicle.entities.import`
  * `chronicle.entities.list`
  * `chronicle.entities.modifyEntityRiskScore`
  * `chronicle.entities.queryEntityRiskScoreModifications`
  * `chronicle.entities.searchEntities`
  * `chronicle.entities.summarize`
  * `chronicle.entities.summarizeFromQuery`

`chronicle.entitiesBlocklists.*`

  * `chronicle.entitiesBlocklists.delete`
  * `chronicle.entitiesBlocklists.get`
  * `chronicle.entitiesBlocklists.update`

`chronicle.entityRiskScores.queryEntityRiskScores` `chronicle.environmentGroups.*`

  * `chronicle.environmentGroups.delete`
  * `chronicle.environmentGroups.get`
  * `chronicle.environmentGroups.update`

`chronicle.environments.*`

  * `chronicle.environments.delete`
  * `chronicle.environments.get`
  * `chronicle.environments.update`

`chronicle.events.*`

  * `chronicle.events.batchGet`
  * `chronicle.events.fetchEnrichedEvent`
  * `chronicle.events.findUdmFieldValues`
  * `chronicle.events.get`
  * `chronicle.events.import`
  * `chronicle.events.queryProductSourceStats`
  * `chronicle.events.searchRawLogs`
  * `chronicle.events.udmSearch`
  * `chronicle.events.validateQuery`

`chronicle.extensionValidationReports.*`

  * `chronicle.extensionValidationReports.get`
  * `chronicle.extensionValidationReports.list`

`chronicle.featuredContentNativeDashboards.*`

  * `chronicle.featuredContentNativeDashboards.get`
  * `chronicle.featuredContentNativeDashboards.install`
  * `chronicle.featuredContentNativeDashboards.list`

`chronicle.featuredContentPlaybooks.*`

  * `chronicle.featuredContentPlaybooks.get`
  * `chronicle.featuredContentPlaybooks.install`
  * `chronicle.featuredContentPlaybooks.list`

`chronicle.featuredContentRules.list` `chronicle.featuredContentSearchQueries.*`

  * `chronicle.featuredContentSearchQueries.get`
  * `chronicle.featuredContentSearchQueries.install`
  * `chronicle.featuredContentSearchQueries.list`

`chronicle.features.*`

  * `chronicle.features.disable`
  * `chronicle.features.get`
  * `chronicle.features.list`
  * `chronicle.features.update`

`chronicle.feedPacks.*`

  * `chronicle.feedPacks.get`
  * `chronicle.feedPacks.list`

`chronicle.feedServiceAccounts.fetch` `chronicle.feedSourceTypeSchemas.list` `chronicle.feeds.*`

  * `chronicle.feeds.create`
  * `chronicle.feeds.delete`
  * `chronicle.feeds.disable`
  * `chronicle.feeds.enable`
  * `chronicle.feeds.generateSecret`
  * `chronicle.feeds.get`
  * `chronicle.feeds.list`
  * `chronicle.feeds.update`

`chronicle.findingsGraphs.*`

  * `chronicle.findingsGraphs.exploreNode`
  * `chronicle.findingsGraphs.initializeGraph`

`chronicle.findingsRefinementDeployments.*`

  * `chronicle.findingsRefinementDeployments.get`
  * `chronicle.findingsRefinementDeployments.list`
  * `chronicle.findingsRefinementDeployments.update`

`chronicle.findingsRefinements.*`

  * `chronicle.findingsRefinements.computeActivity`
  * `chronicle.findingsRefinements.computeAllActivities`
  * `chronicle.findingsRefinements.create`
  * `chronicle.findingsRefinements.get`
  * `chronicle.findingsRefinements.list`
  * `chronicle.findingsRefinements.test`
  * `chronicle.findingsRefinements.update`

`chronicle.formDynamicParameters.*`

  * `chronicle.formDynamicParameters.get`
  * `chronicle.formDynamicParameters.update`

`chronicle.forwarders.*`

  * `chronicle.forwarders.create`
  * `chronicle.forwarders.delete`
  * `chronicle.forwarders.generate`
  * `chronicle.forwarders.get`
  * `chronicle.forwarders.importStatsEvents`
  * `chronicle.forwarders.list`
  * `chronicle.forwarders.update`

`chronicle.globalDataAccessScopes.permit` `chronicle.ingestionLogLabels.*`

  * `chronicle.ingestionLogLabels.get`
  * `chronicle.ingestionLogLabels.list`

`chronicle.ingestionLogNamespaces.*`

  * `chronicle.ingestionLogNamespaces.get`
  * `chronicle.ingestionLogNamespaces.list`

`chronicle.instances.generateCollectionAgentAuth` `chronicle.instances.generateSoarAuthJwt` `chronicle.instances.generateSoarChatMessage` `chronicle.instances.generateWorkspaceConnectionToken` `chronicle.instances.get` `chronicle.instances.graduatePocInstance` `chronicle.instances.logTypeClassifier` `chronicle.instances.report` `chronicle.instances.runThreatHunt` `chronicle.instances.soarAdmin` `chronicle.instances.suggestQueryFields` `chronicle.instances.update` `chronicle.instances.verifyNonce` `chronicle.integrationActionRevisions.*`

  * `chronicle.integrationActionRevisions.delete`
  * `chronicle.integrationActionRevisions.get`
  * `chronicle.integrationActionRevisions.update`

`chronicle.integrationActions.*`

  * `chronicle.integrationActions.delete`
  * `chronicle.integrationActions.get`
  * `chronicle.integrationActions.run`
  * `chronicle.integrationActions.update`

`chronicle.integrationInstances.*`

  * `chronicle.integrationInstances.delete`
  * `chronicle.integrationInstances.get`
  * `chronicle.integrationInstances.update`

`chronicle.integrationLogicalOperatorRevisions.*`

  * `chronicle.integrationLogicalOperatorRevisions.delete`
  * `chronicle.integrationLogicalOperatorRevisions.get`
  * `chronicle.integrationLogicalOperatorRevisions.update`

`chronicle.integrationLogicalOperators.*`

  * `chronicle.integrationLogicalOperators.delete`
  * `chronicle.integrationLogicalOperators.execute`
  * `chronicle.integrationLogicalOperators.get`
  * `chronicle.integrationLogicalOperators.update`

`chronicle.integrations.*`

  * `chronicle.integrations.delete`
  * `chronicle.integrations.get`
  * `chronicle.integrations.update`

`chronicle.investigationComments.*`

  * `chronicle.investigationComments.create`
  * `chronicle.investigationComments.delete`
  * `chronicle.investigationComments.get`
  * `chronicle.investigationComments.list`
  * `chronicle.investigationComments.update`

`chronicle.investigationSteps.*`

  * `chronicle.investigationSteps.get`
  * `chronicle.investigationSteps.list`

`chronicle.investigations.*`

  * `chronicle.investigations.fetchAssociated`
  * `chronicle.investigations.get`
  * `chronicle.investigations.list`
  * `chronicle.investigations.transitionReviewState`
  * `chronicle.investigations.trigger`

`chronicle.involvedEntities.*`

  * `chronicle.involvedEntities.get`
  * `chronicle.involvedEntities.update`

`chronicle.iocAssociations.*`

  * `chronicle.iocAssociations.batchGet`
  * `chronicle.iocAssociations.fetchRelated`
  * `chronicle.iocAssociations.get`

`chronicle.iocState.*`

  * `chronicle.iocState.get`
  * `chronicle.iocState.update`

`chronicle.iocs.*`

  * `chronicle.iocs.batchGet`
  * `chronicle.iocs.fetchRelated`
  * `chronicle.iocs.findFirstAndLastSeen`
  * `chronicle.iocs.findIocs`
  * `chronicle.iocs.get`
  * `chronicle.iocs.searchCuratedDetectionsForIoc`

`chronicle.jobInstanceLogs.get` `chronicle.jobInstances.*`

  * `chronicle.jobInstances.delete`
  * `chronicle.jobInstances.get`
  * `chronicle.jobInstances.run`
  * `chronicle.jobInstances.update`

`chronicle.jobRevisions.*`

  * `chronicle.jobRevisions.delete`
  * `chronicle.jobRevisions.get`
  * `chronicle.jobRevisions.update`

`chronicle.jobs.*`

  * `chronicle.jobs.delete`
  * `chronicle.jobs.get`
  * `chronicle.jobs.update`

`chronicle.labsExperimentExecutions.*`

  * `chronicle.labsExperimentExecutions.get`
  * `chronicle.labsExperimentExecutions.list`
  * `chronicle.labsExperimentExecutions.update`

`chronicle.labsExperiments.*`

  * `chronicle.labsExperiments.execute`
  * `chronicle.labsExperiments.get`
  * `chronicle.labsExperiments.list`
  * `chronicle.labsExperiments.update`

`chronicle.legacies.*`

  * `chronicle.legacies.legacyBatchGetCases`
  * `chronicle.legacies.legacyBatchGetCollections`
  * `chronicle.legacies.legacyCreateSoarAlert`
  * `chronicle.legacies.legacyFetchAlertsView`
  * `chronicle.legacies.legacyFetchUdmSearchCsv`
  * `chronicle.legacies.legacyFetchUdmSearchView`
  * `chronicle.legacies.legacyFindAssetEvents`
  * `chronicle.legacies.legacyFindRawLogs`
  * `chronicle.legacies.legacyFindUdmEvents`
  * `chronicle.legacies.legacyGetAlert`
  * `chronicle.legacies.legacyGetCuratedRulesTrends`
  * `chronicle.legacies.legacyGetDetection`
  * `chronicle.legacies.legacyGetEventForDetection`
  * `chronicle.legacies.legacyGetRuleCounts`
  * `chronicle.legacies.legacyGetRulesTrends`
  * `chronicle.legacies.legacyRunTestRule`
  * `chronicle.legacies.legacySearchArtifactEvents`
  * `chronicle.legacies.legacySearchArtifactIoCDetails`
  * `chronicle.legacies.legacySearchAssetEvents`
  * `chronicle.legacies.legacySearchCuratedDetections`
  * `chronicle.legacies.legacySearchCustomerStats`
  * `chronicle.legacies.legacySearchDetections`
  * `chronicle.legacies.legacySearchDomainsRecentlyRegistered`
  * `chronicle.legacies.legacySearchDomainsTimingStats`
  * `chronicle.legacies.legacySearchEnterpriseWideAlerts`
  * `chronicle.legacies.legacySearchEnterpriseWideIoCs`
  * `chronicle.legacies.legacySearchFindings`
  * `chronicle.legacies.legacySearchIngestionStats`
  * `chronicle.legacies.legacySearchIoCInsights`
  * `chronicle.legacies.legacySearchRawLogs`
  * `chronicle.legacies.legacySearchRuleDetectionCountBuckets`
  * `chronicle.legacies.legacySearchRuleDetectionEvents`
  * `chronicle.legacies.legacySearchRuleResults`
  * `chronicle.legacies.legacySearchRulesAlerts`
  * `chronicle.legacies.legacySearchUserEvents`
  * `chronicle.legacies.legacyStreamDetectionAlerts`
  * `chronicle.legacies.legacyTestRuleStreaming`
  * `chronicle.legacies.legacyUpdateAlert`

`chronicle.legacyCaseFederationPlatforms.*`

  * `chronicle.legacyCaseFederationPlatforms.delete`
  * `chronicle.legacyCaseFederationPlatforms.get`
  * `chronicle.legacyCaseFederationPlatforms.update`

`chronicle.legacyCases.*`

  * `chronicle.legacyCases.createManual`
  * `chronicle.legacyCases.createSimulated`
  * `chronicle.legacyCases.deleteSimulated`
  * `chronicle.legacyCases.exportJson`
  * `chronicle.legacyCases.get`
  * `chronicle.legacyCases.getSimulated`
  * `chronicle.legacyCases.importJson`
  * `chronicle.legacyCases.ingest`
  * `chronicle.legacyCases.ingestAlertTestCase`
  * `chronicle.legacyCases.runManualAction`
  * `chronicle.legacyCases.simulate`

`chronicle.legacyConfiguration.getMaximumAlertsGroupingConfiguration` `chronicle.legacyFederatedCases.*`

  * `chronicle.legacyFederatedCases.batchPatchFederatedCases`
  * `chronicle.legacyFederatedCases.fetchCasesToSync`
  * `chronicle.legacyFederatedCases.get`

`chronicle.legacyPlaybooks.*`

  * `chronicle.legacyPlaybooks.delete`
  * `chronicle.legacyPlaybooks.export`
  * `chronicle.legacyPlaybooks.get`
  * `chronicle.legacyPlaybooks.import`
  * `chronicle.legacyPlaybooks.update`

`chronicle.legacyPublisher.*`

  * `chronicle.legacyPublisher.get`
  * `chronicle.legacyPublisher.update`

`chronicle.legacySdk.*`

  * `chronicle.legacySdk.get`
  * `chronicle.legacySdk.update`

`chronicle.legacySearches.*`

  * `chronicle.legacySearches.searchCases`
  * `chronicle.legacySearches.searchEntities`

`chronicle.legacySoarAdvancedReports.*`

  * `chronicle.legacySoarAdvancedReports.delete`
  * `chronicle.legacySoarAdvancedReports.get`
  * `chronicle.legacySoarAdvancedReports.share`
  * `chronicle.legacySoarAdvancedReports.update`

`chronicle.legacySoarAudits.legacySoarAudit` `chronicle.legacySoarDashboards.*`

  * `chronicle.legacySoarDashboards.delete`
  * `chronicle.legacySoarDashboards.get`
  * `chronicle.legacySoarDashboards.update`

`chronicle.legacySoarIdpMappingGroups.*`

  * `chronicle.legacySoarIdpMappingGroups.delete`
  * `chronicle.legacySoarIdpMappingGroups.get`
  * `chronicle.legacySoarIdpMappingGroups.update`

`chronicle.legacySoarPermissionGroups.get` `chronicle.legacySoarReports.*`

  * `chronicle.legacySoarReports.delete`
  * `chronicle.legacySoarReports.get`
  * `chronicle.legacySoarReports.update`

`chronicle.legacySoarSettings.*`

  * `chronicle.legacySoarSettings.get`
  * `chronicle.legacySoarSettings.update`

`chronicle.legacySoarUsers.*`

  * `chronicle.legacySoarUsers.delete`
  * `chronicle.legacySoarUsers.get`

`chronicle.legacySystem.*`

  * `chronicle.legacySystem.getLicenseStatus`
  * `chronicle.legacySystem.getMaximumDataRetentionValue`
  * `chronicle.legacySystem.getSystemVersion`

`chronicle.legacySystemMetadata.*`

  * `chronicle.legacySystemMetadata.get`
  * `chronicle.legacySystemMetadata.placeholders`

`chronicle.logProcessingPipelines.*`

  * `chronicle.logProcessingPipelines.associateStreams`
  * `chronicle.logProcessingPipelines.create`
  * `chronicle.logProcessingPipelines.delete`
  * `chronicle.logProcessingPipelines.dissociateStreams`
  * `chronicle.logProcessingPipelines.fetchAssociatedPipeline`
  * `chronicle.logProcessingPipelines.fetchSampleLogsByStreams`
  * `chronicle.logProcessingPipelines.get`
  * `chronicle.logProcessingPipelines.list`
  * `chronicle.logProcessingPipelines.testPipeline`
  * `chronicle.logProcessingPipelines.update`

`chronicle.logTypeSchemas.list` `chronicle.logTypeSettings.*`

  * `chronicle.logTypeSettings.get`
  * `chronicle.logTypeSettings.list`
  * `chronicle.logTypeSettings.update`

`chronicle.logTypes.*`

  * `chronicle.logTypes.create`
  * `chronicle.logTypes.get`
  * `chronicle.logTypes.list`
  * `chronicle.logTypes.search`
  * `chronicle.logTypes.update`

`chronicle.logs.*`

  * `chronicle.logs.export`
  * `chronicle.logs.get`
  * `chronicle.logs.import`
  * `chronicle.logs.list`

`chronicle.managedDomainSettings.*`

  * `chronicle.managedDomainSettings.get`
  * `chronicle.managedDomainSettings.update`

`chronicle.managerRevisions.*`

  * `chronicle.managerRevisions.delete`
  * `chronicle.managerRevisions.get`
  * `chronicle.managerRevisions.update`

`chronicle.managers.*`

  * `chronicle.managers.delete`
  * `chronicle.managers.get`
  * `chronicle.managers.update`

`chronicle.mappingRules.*`

  * `chronicle.mappingRules.delete`
  * `chronicle.mappingRules.get`
  * `chronicle.mappingRules.update`

`chronicle.marketplaceIntegrations.*`

  * `chronicle.marketplaceIntegrations.get`
  * `chronicle.marketplaceIntegrations.install`
  * `chronicle.marketplaceIntegrations.uninstall`

`chronicle.messages.*`

  * `chronicle.messages.create`
  * `chronicle.messages.delete`
  * `chronicle.messages.get`
  * `chronicle.messages.list`
  * `chronicle.messages.update`

`chronicle.moduleSettings.*`

  * `chronicle.moduleSettings.get`
  * `chronicle.moduleSettings.modifyCaseList`
  * `chronicle.moduleSettings.rebranding`

`chronicle.moduleSettingsProperties.*`

  * `chronicle.moduleSettingsProperties.get`
  * `chronicle.moduleSettingsProperties.testSettings`
  * `chronicle.moduleSettingsProperties.update`

`chronicle.multitenantDirectories.get` `chronicle.nativeDashboards.*`

  * `chronicle.nativeDashboards.create`
  * `chronicle.nativeDashboards.delete`
  * `chronicle.nativeDashboards.duplicate`
  * `chronicle.nativeDashboards.get`
  * `chronicle.nativeDashboards.list`
  * `chronicle.nativeDashboards.update`

`chronicle.notebooks.*`

  * `chronicle.notebooks.get`
  * `chronicle.notebooks.list`

`chronicle.notificationSettings.*`

  * `chronicle.notificationSettings.get`
  * `chronicle.notificationSettings.update`

`chronicle.ontologyRecords.*`

  * `chronicle.ontologyRecords.get`
  * `chronicle.ontologyRecords.update`

`chronicle.operations.*`

  * `chronicle.operations.cancel`
  * `chronicle.operations.delete`
  * `chronicle.operations.get`
  * `chronicle.operations.list`
  * `chronicle.operations.streamSearch`
  * `chronicle.operations.wait`

`chronicle.parserExtensions.*`

  * `chronicle.parserExtensions.activate`
  * `chronicle.parserExtensions.create`
  * `chronicle.parserExtensions.delete`
  * `chronicle.parserExtensions.generateKeyValueMappings`
  * `chronicle.parserExtensions.get`
  * `chronicle.parserExtensions.legacySubmitParserExtension`
  * `chronicle.parserExtensions.list`
  * `chronicle.parserExtensions.removeSyslog`

`chronicle.parsers.*`

  * `chronicle.parsers.activate`
  * `chronicle.parsers.activateReleaseCandidate`
  * `chronicle.parsers.copyPrebuiltParser`
  * `chronicle.parsers.create`
  * `chronicle.parsers.deactivate`
  * `chronicle.parsers.delete`
  * `chronicle.parsers.generateEventTypesSuggestions`
  * `chronicle.parsers.get`
  * `chronicle.parsers.list`
  * `chronicle.parsers.runParser`
  * `chronicle.parsers.update`

`chronicle.parsingErrors.list` `chronicle.preferenceSets.*`

  * `chronicle.preferenceSets.get`
  * `chronicle.preferenceSets.update`

`chronicle.propertySchemaDefinitions.*`

  * `chronicle.propertySchemaDefinitions.delete`
  * `chronicle.propertySchemaDefinitions.get`
  * `chronicle.propertySchemaDefinitions.update`

`chronicle.queries.suggestSql` `chronicle.queryMetrics.*`

  * `chronicle.queryMetrics.get`
  * `chronicle.queryMetrics.list`

`chronicle.referenceLists.*`

  * `chronicle.referenceLists.create`
  * `chronicle.referenceLists.get`
  * `chronicle.referenceLists.list`
  * `chronicle.referenceLists.update`
  * `chronicle.referenceLists.verifyReferenceList`

`chronicle.remoteAgents.*`

  * `chronicle.remoteAgents.delete`
  * `chronicle.remoteAgents.get`
  * `chronicle.remoteAgents.update`

`chronicle.requestTemplates.*`

  * `chronicle.requestTemplates.delete`
  * `chronicle.requestTemplates.get`
  * `chronicle.requestTemplates.update`

`chronicle.retrohunts.*`

  * `chronicle.retrohunts.create`
  * `chronicle.retrohunts.get`
  * `chronicle.retrohunts.list`

`chronicle.riskConfigs.*`

  * `chronicle.riskConfigs.get`
  * `chronicle.riskConfigs.update`

`chronicle.ruleDeployments.*`

  * `chronicle.ruleDeployments.get`
  * `chronicle.ruleDeployments.list`
  * `chronicle.ruleDeployments.update`

`chronicle.ruleExecutionErrors.list` `chronicle.rules.*`

  * `chronicle.rules.create`
  * `chronicle.rules.delete`
  * `chronicle.rules.get`
  * `chronicle.rules.list`
  * `chronicle.rules.listRevisions`
  * `chronicle.rules.modifyRules`
  * `chronicle.rules.update`
  * `chronicle.rules.verifyRuleText`

`chronicle.savedColumnSets.*`

  * `chronicle.savedColumnSets.create`
  * `chronicle.savedColumnSets.delete`
  * `chronicle.savedColumnSets.get`
  * `chronicle.savedColumnSets.list`
  * `chronicle.savedColumnSets.update`

`chronicle.searchQueries.*`

  * `chronicle.searchQueries.create`
  * `chronicle.searchQueries.delete`
  * `chronicle.searchQueries.get`
  * `chronicle.searchQueries.list`
  * `chronicle.searchQueries.update`

`chronicle.searchSessions.search` `chronicle.searchedResults.list` `chronicle.shareConfigs.*`

  * `chronicle.shareConfigs.get`
  * `chronicle.shareConfigs.update`

`chronicle.sharedPreferenceSets.*`

  * `chronicle.sharedPreferenceSets.create`
  * `chronicle.sharedPreferenceSets.delete`
  * `chronicle.sharedPreferenceSets.get`
  * `chronicle.sharedPreferenceSets.list`
  * `chronicle.sharedPreferenceSets.update`

`chronicle.slaDefinitions.*`

  * `chronicle.slaDefinitions.delete`
  * `chronicle.slaDefinitions.get`
  * `chronicle.slaDefinitions.update`

`chronicle.soarDomains.*`

  * `chronicle.soarDomains.delete`
  * `chronicle.soarDomains.get`
  * `chronicle.soarDomains.update`

`chronicle.soarNetworks.*`

  * `chronicle.soarNetworks.delete`
  * `chronicle.soarNetworks.get`
  * `chronicle.soarNetworks.update`

`chronicle.socRoles.*`

  * `chronicle.socRoles.delete`
  * `chronicle.socRoles.get`
  * `chronicle.socRoles.update`

`chronicle.summaryTables.*`

  * `chronicle.summaryTables.create`
  * `chronicle.summaryTables.delete`
  * `chronicle.summaryTables.get`
  * `chronicle.summaryTables.list`
  * `chronicle.summaryTables.update`

`chronicle.systemNotifications.*`

  * `chronicle.systemNotifications.get`
  * `chronicle.systemNotifications.update`

`chronicle.tagSubscriptions.*`

  * `chronicle.tagSubscriptions.create`
  * `chronicle.tagSubscriptions.delete`
  * `chronicle.tagSubscriptions.get`
  * `chronicle.tagSubscriptions.list`
  * `chronicle.tagSubscriptions.update`

`chronicle.tags.*`

  * `chronicle.tags.create`
  * `chronicle.tags.delete`
  * `chronicle.tags.get`
  * `chronicle.tags.list`
  * `chronicle.tags.update`

`chronicle.tasks.*`

  * `chronicle.tasks.delete`
  * `chronicle.tasks.get`
  * `chronicle.tasks.update`

`chronicle.tenants.*`

  * `chronicle.tenants.create`
  * `chronicle.tenants.list`
  * `chronicle.tenants.update`

`chronicle.threatCollectionFilterSet.get` `chronicle.threatCollections.*`

  * `chronicle.threatCollections.fetchEntityMetadata`
  * `chronicle.threatCollections.fetchIocMatchMetadata`
  * `chronicle.threatCollections.fetchRelated`
  * `chronicle.threatCollections.get`
  * `chronicle.threatCollections.list`

`chronicle.transformerDefinitions.*`

  * `chronicle.transformerDefinitions.create`
  * `chronicle.transformerDefinitions.delete`
  * `chronicle.transformerDefinitions.execute`
  * `chronicle.transformerDefinitions.get`
  * `chronicle.transformerDefinitions.list`
  * `chronicle.transformerDefinitions.update`

`chronicle.transformerRevisions.*`

  * `chronicle.transformerRevisions.delete`
  * `chronicle.transformerRevisions.get`
  * `chronicle.transformerRevisions.update`

`chronicle.uniqueEntities.*`

  * `chronicle.uniqueEntities.get`
  * `chronicle.uniqueEntities.update`

`chronicle.userLocalizations.*`

  * `chronicle.userLocalizations.get`
  * `chronicle.userLocalizations.update`

`chronicle.userNotifications.*`

  * `chronicle.userNotifications.get`
  * `chronicle.userNotifications.update`

`chronicle.validationErrors.list` `chronicle.validationReports.get` `chronicle.views.*`

  * `chronicle.views.get`
  * `chronicle.views.update`

`chronicle.visualFamilies.*`

  * `chronicle.visualFamilies.delete`
  * `chronicle.visualFamilies.get`
  * `chronicle.visualFamilies.update`

`chronicle.watchlists.*`

  * `chronicle.watchlists.create`
  * `chronicle.watchlists.delete`
  * `chronicle.watchlists.get`
  * `chronicle.watchlists.list`
  * `chronicle.watchlists.update`

`chronicle.webhooks.*`

  * `chronicle.webhooks.delete`
  * `chronicle.webhooks.get`
  * `chronicle.webhooks.update`

`chronicle.workdeskContacts.*`

  * `chronicle.workdeskContacts.delete`
  * `chronicle.workdeskContacts.get`
  * `chronicle.workdeskContacts.update`

`chronicle.workdeskLinks.*`

  * `chronicle.workdeskLinks.delete`
  * `chronicle.workdeskLinks.get`
  * `chronicle.workdeskLinks.update`

`chronicle.workdeskNotes.*`

  * `chronicle.workdeskNotes.delete`
  * `chronicle.workdeskNotes.get`
  * `chronicle.workdeskNotes.update`

`cloudasset.assets.exportResource` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.assets.searchEnrichmentResourceOwners` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.attackpaths.list` `securitycenter.exposurepathexplan.get` `securitycenter.findings.bulkMuteUpdate` `securitycenter.findings.group` `securitycenter.findings.list` `securitycenter.findings.listFindingPropertyNames` `securitycenter.findings.setMute` `securitycenter.findings.setState` `securitycenter.findings.update` `securitycenter.findingsecuritymarks.update` `securitycenter.simulations.get` `securitycenter.userinterfacemetadata.get` `securitycenter.valuedresources.list`  
  
#### Chronicle API Editor 

(`roles/chronicle.editor`) Modify Access to Chronicle API resources.  |  `chronicle.agentSettings.*`

  * `chronicle.agentSettings.get`
  * `chronicle.agentSettings.update`

`chronicle.ais.*`

  * `chronicle.ais.createFeedback`
  * `chronicle.ais.translateUdmQuery`
  * `chronicle.ais.translateYlRule`

`chronicle.analyticValues.list` `chronicle.analytics.list` `chronicle.announcements.get` `chronicle.attachments.*`

  * `chronicle.attachments.delete`
  * `chronicle.attachments.get`
  * `chronicle.attachments.update`

`chronicle.bigQueryExport.get` `chronicle.calculatedFieldDefinitions.get` `chronicle.caseAlerts.*`

  * `chronicle.caseAlerts.get`
  * `chronicle.caseAlerts.metadataUpdate`
  * `chronicle.caseAlerts.move`
  * `chronicle.caseAlerts.removeTag`
  * `chronicle.caseAlerts.updateSla`
  * `chronicle.caseAlerts.updateTag`

`chronicle.caseCloseDefinitions.*`

  * `chronicle.caseCloseDefinitions.delete`
  * `chronicle.caseCloseDefinitions.get`
  * `chronicle.caseCloseDefinitions.update`

`chronicle.caseComments.*`

  * `chronicle.caseComments.delete`
  * `chronicle.caseComments.get`
  * `chronicle.caseComments.update`

`chronicle.caseDetections.get` `chronicle.caseEvents.get` `chronicle.caseEvidenceDatas.get` `chronicle.caseQueueFilters.*`

  * `chronicle.caseQueueFilters.delete`
  * `chronicle.caseQueueFilters.get`
  * `chronicle.caseQueueFilters.update`

`chronicle.caseStageDefinitions.get` `chronicle.caseTagDefinitions.*`

  * `chronicle.caseTagDefinitions.delete`
  * `chronicle.caseTagDefinitions.get`
  * `chronicle.caseTagDefinitions.update`

`chronicle.caseWallRecords.*`

  * `chronicle.caseWallRecords.get`
  * `chronicle.caseWallRecords.update`

`chronicle.cases.*`

  * `chronicle.cases.close`
  * `chronicle.cases.countPriorities`
  * `chronicle.cases.generateReport`
  * `chronicle.cases.get`
  * `chronicle.cases.removeTag`
  * `chronicle.cases.reopen`
  * `chronicle.cases.update`
  * `chronicle.cases.updateTag`

`chronicle.chatMessageAttachments.get` `chronicle.chatMessages.*`

  * `chronicle.chatMessages.create`
  * `chronicle.chatMessages.get`
  * `chronicle.chatMessages.pin`

`chronicle.chatSessionMessages.*`

  * `chronicle.chatSessionMessages.list`
  * `chronicle.chatSessionMessages.update`

`chronicle.chatSessions.*`

  * `chronicle.chatSessions.delete`
  * `chronicle.chatSessions.list`

`chronicle.collectors.get` `chronicle.collectors.list` `chronicle.connectorEvents.get` `chronicle.connectorInstanceLogs.get` `chronicle.connectorInstances.*`

  * `chronicle.connectorInstances.delete`
  * `chronicle.connectorInstances.get`
  * `chronicle.connectorInstances.update`

`chronicle.connectorRevisions.*`

  * `chronicle.connectorRevisions.delete`
  * `chronicle.connectorRevisions.get`
  * `chronicle.connectorRevisions.update`

`chronicle.contentPacks.*`

  * `chronicle.contentPacks.create`
  * `chronicle.contentPacks.delete`
  * `chronicle.contentPacks.export`
  * `chronicle.contentPacks.get`
  * `chronicle.contentPacks.install`

`chronicle.contextProperties.*`

  * `chronicle.contextProperties.delete`
  * `chronicle.contextProperties.get`
  * `chronicle.contextProperties.update`

`chronicle.conversations.*`

  * `chronicle.conversations.create`
  * `chronicle.conversations.delete`
  * `chronicle.conversations.get`
  * `chronicle.conversations.list`
  * `chronicle.conversations.update`

`chronicle.coverageDetails.*`

  * `chronicle.coverageDetails.get`
  * `chronicle.coverageDetails.list`

`chronicle.curatedRuleSetCategories.*`

  * `chronicle.curatedRuleSetCategories.countAllCuratedRuleSetDetections`
  * `chronicle.curatedRuleSetCategories.get`
  * `chronicle.curatedRuleSetCategories.list`

`chronicle.curatedRuleSetDeployments.*`

  * `chronicle.curatedRuleSetDeployments.batchUpdate`
  * `chronicle.curatedRuleSetDeployments.get`
  * `chronicle.curatedRuleSetDeployments.list`
  * `chronicle.curatedRuleSetDeployments.update`

`chronicle.curatedRuleSets.*`

  * `chronicle.curatedRuleSets.countCuratedRuleSetDetections`
  * `chronicle.curatedRuleSets.get`
  * `chronicle.curatedRuleSets.list`

`chronicle.curatedRules.*`

  * `chronicle.curatedRules.get`
  * `chronicle.curatedRules.list`

`chronicle.customFieldValues.*`

  * `chronicle.customFieldValues.get`
  * `chronicle.customFieldValues.update`

`chronicle.customFields.get` `chronicle.customLists.get` `chronicle.dashboardCharts.*`

  * `chronicle.dashboardCharts.get`
  * `chronicle.dashboardCharts.list`

`chronicle.dashboardQueries.*`

  * `chronicle.dashboardQueries.execute`
  * `chronicle.dashboardQueries.get`
  * `chronicle.dashboardQueries.list`

`chronicle.dashboardScheduledReports.*`

  * `chronicle.dashboardScheduledReports.create`
  * `chronicle.dashboardScheduledReports.delete`
  * `chronicle.dashboardScheduledReports.duplicate`
  * `chronicle.dashboardScheduledReports.fetchHistory`
  * `chronicle.dashboardScheduledReports.get`
  * `chronicle.dashboardScheduledReports.list`
  * `chronicle.dashboardScheduledReports.trigger`
  * `chronicle.dashboardScheduledReports.update`

`chronicle.dashboards.*`

  * `chronicle.dashboards.copy`
  * `chronicle.dashboards.create`
  * `chronicle.dashboards.delete`
  * `chronicle.dashboards.edit`
  * `chronicle.dashboards.get`
  * `chronicle.dashboards.list`
  * `chronicle.dashboards.schedule`

`chronicle.dataAccessScopes.list` `chronicle.dataExports.*`

  * `chronicle.dataExports.cancel`
  * `chronicle.dataExports.create`
  * `chronicle.dataExports.fetchLogTypesAvailableForExport`
  * `chronicle.dataExports.fetchServiceAccountForDataExport`
  * `chronicle.dataExports.get`
  * `chronicle.dataExports.list`
  * `chronicle.dataExports.update`

`chronicle.dataTableOperationErrors.get` `chronicle.dataTableRows.*`

  * `chronicle.dataTableRows.asyncBulkAppend`
  * `chronicle.dataTableRows.asyncBulkCreate`
  * `chronicle.dataTableRows.asyncBulkDelete`
  * `chronicle.dataTableRows.asyncBulkReplace`
  * `chronicle.dataTableRows.asyncBulkUpdate`
  * `chronicle.dataTableRows.bulkCreate`
  * `chronicle.dataTableRows.bulkDelete`
  * `chronicle.dataTableRows.bulkGet`
  * `chronicle.dataTableRows.bulkReplace`
  * `chronicle.dataTableRows.bulkUpdate`
  * `chronicle.dataTableRows.create`
  * `chronicle.dataTableRows.delete`
  * `chronicle.dataTableRows.get`
  * `chronicle.dataTableRows.list`
  * `chronicle.dataTableRows.update`

`chronicle.dataTables.*`

  * `chronicle.dataTables.bulkCreateDataTableAsync`
  * `chronicle.dataTables.create`
  * `chronicle.dataTables.delete`
  * `chronicle.dataTables.get`
  * `chronicle.dataTables.list`
  * `chronicle.dataTables.update`

`chronicle.dataTaps.*`

  * `chronicle.dataTaps.create`
  * `chronicle.dataTaps.delete`
  * `chronicle.dataTaps.get`
  * `chronicle.dataTaps.list`
  * `chronicle.dataTaps.update`

`chronicle.emailTemplates.get` `chronicle.enrichmentAgent.*`

  * `chronicle.enrichmentAgent.execute`
  * `chronicle.enrichmentAgent.get`

`chronicle.enrichmentCombination.get` `chronicle.enrichmentControls.create` `chronicle.enrichmentControls.disable` `chronicle.enrichmentControls.get` `chronicle.enrichmentControls.list` `chronicle.entities.*`

  * `chronicle.entities.batchCreate`
  * `chronicle.entities.batchDelete`
  * `chronicle.entities.batchValidate`
  * `chronicle.entities.create`
  * `chronicle.entities.delete`
  * `chronicle.entities.find`
  * `chronicle.entities.findEntityAlerts`
  * `chronicle.entities.findRelatedEntities`
  * `chronicle.entities.get`
  * `chronicle.entities.import`
  * `chronicle.entities.list`
  * `chronicle.entities.modifyEntityRiskScore`
  * `chronicle.entities.queryEntityRiskScoreModifications`
  * `chronicle.entities.searchEntities`
  * `chronicle.entities.summarize`
  * `chronicle.entities.summarizeFromQuery`

`chronicle.entitiesBlocklists.get` `chronicle.entityRiskScores.queryEntityRiskScores` `chronicle.environmentGroups.get` `chronicle.environments.get` `chronicle.events.*`

  * `chronicle.events.batchGet`
  * `chronicle.events.fetchEnrichedEvent`
  * `chronicle.events.findUdmFieldValues`
  * `chronicle.events.get`
  * `chronicle.events.import`
  * `chronicle.events.queryProductSourceStats`
  * `chronicle.events.searchRawLogs`
  * `chronicle.events.udmSearch`
  * `chronicle.events.validateQuery`

`chronicle.featuredContentNativeDashboards.*`

  * `chronicle.featuredContentNativeDashboards.get`
  * `chronicle.featuredContentNativeDashboards.install`
  * `chronicle.featuredContentNativeDashboards.list`

`chronicle.featuredContentPlaybooks.*`

  * `chronicle.featuredContentPlaybooks.get`
  * `chronicle.featuredContentPlaybooks.install`
  * `chronicle.featuredContentPlaybooks.list`

`chronicle.featuredContentRules.list` `chronicle.featuredContentSearchQueries.*`

  * `chronicle.featuredContentSearchQueries.get`
  * `chronicle.featuredContentSearchQueries.install`
  * `chronicle.featuredContentSearchQueries.list`

`chronicle.features.get` `chronicle.features.list` `chronicle.feedPacks.*`

  * `chronicle.feedPacks.get`
  * `chronicle.feedPacks.list`

`chronicle.findingsGraphs.*`

  * `chronicle.findingsGraphs.exploreNode`
  * `chronicle.findingsGraphs.initializeGraph`

`chronicle.findingsRefinementDeployments.*`

  * `chronicle.findingsRefinementDeployments.get`
  * `chronicle.findingsRefinementDeployments.list`
  * `chronicle.findingsRefinementDeployments.update`

`chronicle.findingsRefinements.*`

  * `chronicle.findingsRefinements.computeActivity`
  * `chronicle.findingsRefinements.computeAllActivities`
  * `chronicle.findingsRefinements.create`
  * `chronicle.findingsRefinements.get`
  * `chronicle.findingsRefinements.list`
  * `chronicle.findingsRefinements.test`
  * `chronicle.findingsRefinements.update`

`chronicle.formDynamicParameters.get` `chronicle.forwarders.generate` `chronicle.forwarders.get` `chronicle.forwarders.importStatsEvents` `chronicle.forwarders.list` `chronicle.globalDataAccessScopes.permit` `chronicle.ingestionLogLabels.*`

  * `chronicle.ingestionLogLabels.get`
  * `chronicle.ingestionLogLabels.list`

`chronicle.ingestionLogNamespaces.*`

  * `chronicle.ingestionLogNamespaces.get`
  * `chronicle.ingestionLogNamespaces.list`

`chronicle.instances.generateCollectionAgentAuth` `chronicle.instances.generateSoarAuthJwt` `chronicle.instances.generateSoarChatMessage` `chronicle.instances.get` `chronicle.instances.logTypeClassifier` `chronicle.instances.report` `chronicle.instances.runThreatHunt` `chronicle.instances.suggestQueryFields` `chronicle.integrationActionRevisions.*`

  * `chronicle.integrationActionRevisions.delete`
  * `chronicle.integrationActionRevisions.get`
  * `chronicle.integrationActionRevisions.update`

`chronicle.integrationActions.get` `chronicle.integrationActions.run` `chronicle.integrationActions.update` `chronicle.integrationInstances.*`

  * `chronicle.integrationInstances.delete`
  * `chronicle.integrationInstances.get`
  * `chronicle.integrationInstances.update`

`chronicle.integrationLogicalOperatorRevisions.*`

  * `chronicle.integrationLogicalOperatorRevisions.delete`
  * `chronicle.integrationLogicalOperatorRevisions.get`
  * `chronicle.integrationLogicalOperatorRevisions.update`

`chronicle.integrationLogicalOperators.*`

  * `chronicle.integrationLogicalOperators.delete`
  * `chronicle.integrationLogicalOperators.execute`
  * `chronicle.integrationLogicalOperators.get`
  * `chronicle.integrationLogicalOperators.update`

`chronicle.integrations.get` `chronicle.integrations.update` `chronicle.investigationComments.*`

  * `chronicle.investigationComments.create`
  * `chronicle.investigationComments.delete`
  * `chronicle.investigationComments.get`
  * `chronicle.investigationComments.list`
  * `chronicle.investigationComments.update`

`chronicle.investigationSteps.*`

  * `chronicle.investigationSteps.get`
  * `chronicle.investigationSteps.list`

`chronicle.investigations.*`

  * `chronicle.investigations.fetchAssociated`
  * `chronicle.investigations.get`
  * `chronicle.investigations.list`
  * `chronicle.investigations.transitionReviewState`
  * `chronicle.investigations.trigger`

`chronicle.involvedEntities.*`

  * `chronicle.involvedEntities.get`
  * `chronicle.involvedEntities.update`

`chronicle.iocAssociations.*`

  * `chronicle.iocAssociations.batchGet`
  * `chronicle.iocAssociations.fetchRelated`
  * `chronicle.iocAssociations.get`

`chronicle.iocState.*`

  * `chronicle.iocState.get`
  * `chronicle.iocState.update`

`chronicle.iocs.*`

  * `chronicle.iocs.batchGet`
  * `chronicle.iocs.fetchRelated`
  * `chronicle.iocs.findFirstAndLastSeen`
  * `chronicle.iocs.findIocs`
  * `chronicle.iocs.get`
  * `chronicle.iocs.searchCuratedDetectionsForIoc`

`chronicle.jobInstanceLogs.get` `chronicle.jobInstances.*`

  * `chronicle.jobInstances.delete`
  * `chronicle.jobInstances.get`
  * `chronicle.jobInstances.run`
  * `chronicle.jobInstances.update`

`chronicle.jobRevisions.*`

  * `chronicle.jobRevisions.delete`
  * `chronicle.jobRevisions.get`
  * `chronicle.jobRevisions.update`

`chronicle.jobs.get` `chronicle.jobs.update` `chronicle.labsExperimentExecutions.*`

  * `chronicle.labsExperimentExecutions.get`
  * `chronicle.labsExperimentExecutions.list`
  * `chronicle.labsExperimentExecutions.update`

`chronicle.labsExperiments.*`

  * `chronicle.labsExperiments.execute`
  * `chronicle.labsExperiments.get`
  * `chronicle.labsExperiments.list`
  * `chronicle.labsExperiments.update`

`chronicle.legacies.*`

  * `chronicle.legacies.legacyBatchGetCases`
  * `chronicle.legacies.legacyBatchGetCollections`
  * `chronicle.legacies.legacyCreateSoarAlert`
  * `chronicle.legacies.legacyFetchAlertsView`
  * `chronicle.legacies.legacyFetchUdmSearchCsv`
  * `chronicle.legacies.legacyFetchUdmSearchView`
  * `chronicle.legacies.legacyFindAssetEvents`
  * `chronicle.legacies.legacyFindRawLogs`
  * `chronicle.legacies.legacyFindUdmEvents`
  * `chronicle.legacies.legacyGetAlert`
  * `chronicle.legacies.legacyGetCuratedRulesTrends`
  * `chronicle.legacies.legacyGetDetection`
  * `chronicle.legacies.legacyGetEventForDetection`
  * `chronicle.legacies.legacyGetRuleCounts`
  * `chronicle.legacies.legacyGetRulesTrends`
  * `chronicle.legacies.legacyRunTestRule`
  * `chronicle.legacies.legacySearchArtifactEvents`
  * `chronicle.legacies.legacySearchArtifactIoCDetails`
  * `chronicle.legacies.legacySearchAssetEvents`
  * `chronicle.legacies.legacySearchCuratedDetections`
  * `chronicle.legacies.legacySearchCustomerStats`
  * `chronicle.legacies.legacySearchDetections`
  * `chronicle.legacies.legacySearchDomainsRecentlyRegistered`
  * `chronicle.legacies.legacySearchDomainsTimingStats`
  * `chronicle.legacies.legacySearchEnterpriseWideAlerts`
  * `chronicle.legacies.legacySearchEnterpriseWideIoCs`
  * `chronicle.legacies.legacySearchFindings`
  * `chronicle.legacies.legacySearchIngestionStats`
  * `chronicle.legacies.legacySearchIoCInsights`
  * `chronicle.legacies.legacySearchRawLogs`
  * `chronicle.legacies.legacySearchRuleDetectionCountBuckets`
  * `chronicle.legacies.legacySearchRuleDetectionEvents`
  * `chronicle.legacies.legacySearchRuleResults`
  * `chronicle.legacies.legacySearchRulesAlerts`
  * `chronicle.legacies.legacySearchUserEvents`
  * `chronicle.legacies.legacyStreamDetectionAlerts`
  * `chronicle.legacies.legacyTestRuleStreaming`
  * `chronicle.legacies.legacyUpdateAlert`

`chronicle.legacyCaseFederationPlatforms.get` `chronicle.legacyCases.*`

  * `chronicle.legacyCases.createManual`
  * `chronicle.legacyCases.createSimulated`
  * `chronicle.legacyCases.deleteSimulated`
  * `chronicle.legacyCases.exportJson`
  * `chronicle.legacyCases.get`
  * `chronicle.legacyCases.getSimulated`
  * `chronicle.legacyCases.importJson`
  * `chronicle.legacyCases.ingest`
  * `chronicle.legacyCases.ingestAlertTestCase`
  * `chronicle.legacyCases.runManualAction`
  * `chronicle.legacyCases.simulate`

`chronicle.legacyFederatedCases.get` `chronicle.legacyPlaybooks.*`

  * `chronicle.legacyPlaybooks.delete`
  * `chronicle.legacyPlaybooks.export`
  * `chronicle.legacyPlaybooks.get`
  * `chronicle.legacyPlaybooks.import`
  * `chronicle.legacyPlaybooks.update`

`chronicle.legacySearches.*`

  * `chronicle.legacySearches.searchCases`
  * `chronicle.legacySearches.searchEntities`

`chronicle.legacySoarAdvancedReports.*`

  * `chronicle.legacySoarAdvancedReports.delete`
  * `chronicle.legacySoarAdvancedReports.get`
  * `chronicle.legacySoarAdvancedReports.share`
  * `chronicle.legacySoarAdvancedReports.update`

`chronicle.legacySoarDashboards.*`

  * `chronicle.legacySoarDashboards.delete`
  * `chronicle.legacySoarDashboards.get`
  * `chronicle.legacySoarDashboards.update`

`chronicle.legacySoarReports.*`

  * `chronicle.legacySoarReports.delete`
  * `chronicle.legacySoarReports.get`
  * `chronicle.legacySoarReports.update`

`chronicle.legacySoarSettings.get` `chronicle.legacySoarUsers.get` `chronicle.legacySystemMetadata.*`

  * `chronicle.legacySystemMetadata.get`
  * `chronicle.legacySystemMetadata.placeholders`

`chronicle.logProcessingPipelines.fetchAssociatedPipeline` `chronicle.logProcessingPipelines.fetchSampleLogsByStreams` `chronicle.logProcessingPipelines.get` `chronicle.logProcessingPipelines.list` `chronicle.logProcessingPipelines.testPipeline` `chronicle.logTypeSchemas.list` `chronicle.logs.*`

  * `chronicle.logs.export`
  * `chronicle.logs.get`
  * `chronicle.logs.import`
  * `chronicle.logs.list`

`chronicle.managedDomainSettings.get` `chronicle.managerRevisions.*`

  * `chronicle.managerRevisions.delete`
  * `chronicle.managerRevisions.get`
  * `chronicle.managerRevisions.update`

`chronicle.managers.*`

  * `chronicle.managers.delete`
  * `chronicle.managers.get`
  * `chronicle.managers.update`

`chronicle.marketplaceIntegrations.*`

  * `chronicle.marketplaceIntegrations.get`
  * `chronicle.marketplaceIntegrations.install`
  * `chronicle.marketplaceIntegrations.uninstall`

`chronicle.messages.*`

  * `chronicle.messages.create`
  * `chronicle.messages.delete`
  * `chronicle.messages.get`
  * `chronicle.messages.list`
  * `chronicle.messages.update`

`chronicle.moduleSettings.*`

  * `chronicle.moduleSettings.get`
  * `chronicle.moduleSettings.modifyCaseList`
  * `chronicle.moduleSettings.rebranding`

`chronicle.moduleSettingsProperties.get` `chronicle.multitenantDirectories.get` `chronicle.nativeDashboards.*`

  * `chronicle.nativeDashboards.create`
  * `chronicle.nativeDashboards.delete`
  * `chronicle.nativeDashboards.duplicate`
  * `chronicle.nativeDashboards.get`
  * `chronicle.nativeDashboards.list`
  * `chronicle.nativeDashboards.update`

`chronicle.notebooks.*`

  * `chronicle.notebooks.get`
  * `chronicle.notebooks.list`

`chronicle.notificationSettings.*`

  * `chronicle.notificationSettings.get`
  * `chronicle.notificationSettings.update`

`chronicle.ontologyRecords.get` `chronicle.operations.*`

  * `chronicle.operations.cancel`
  * `chronicle.operations.delete`
  * `chronicle.operations.get`
  * `chronicle.operations.list`
  * `chronicle.operations.streamSearch`
  * `chronicle.operations.wait`

`chronicle.preferenceSets.*`

  * `chronicle.preferenceSets.get`
  * `chronicle.preferenceSets.update`

`chronicle.propertySchemaDefinitions.*`

  * `chronicle.propertySchemaDefinitions.delete`
  * `chronicle.propertySchemaDefinitions.get`
  * `chronicle.propertySchemaDefinitions.update`

`chronicle.queries.suggestSql` `chronicle.queryMetrics.*`

  * `chronicle.queryMetrics.get`
  * `chronicle.queryMetrics.list`

`chronicle.referenceLists.*`

  * `chronicle.referenceLists.create`
  * `chronicle.referenceLists.get`
  * `chronicle.referenceLists.list`
  * `chronicle.referenceLists.update`
  * `chronicle.referenceLists.verifyReferenceList`

`chronicle.remoteAgents.*`

  * `chronicle.remoteAgents.delete`
  * `chronicle.remoteAgents.get`
  * `chronicle.remoteAgents.update`

`chronicle.requestTemplates.get` `chronicle.retrohunts.*`

  * `chronicle.retrohunts.create`
  * `chronicle.retrohunts.get`
  * `chronicle.retrohunts.list`

`chronicle.riskConfigs.*`

  * `chronicle.riskConfigs.get`
  * `chronicle.riskConfigs.update`

`chronicle.ruleDeployments.*`

  * `chronicle.ruleDeployments.get`
  * `chronicle.ruleDeployments.list`
  * `chronicle.ruleDeployments.update`

`chronicle.ruleExecutionErrors.list` `chronicle.rules.create` `chronicle.rules.get` `chronicle.rules.list` `chronicle.rules.listRevisions` `chronicle.rules.modifyRules` `chronicle.rules.update` `chronicle.rules.verifyRuleText` `chronicle.savedColumnSets.*`

  * `chronicle.savedColumnSets.create`
  * `chronicle.savedColumnSets.delete`
  * `chronicle.savedColumnSets.get`
  * `chronicle.savedColumnSets.list`
  * `chronicle.savedColumnSets.update`

`chronicle.searchQueries.*`

  * `chronicle.searchQueries.create`
  * `chronicle.searchQueries.delete`
  * `chronicle.searchQueries.get`
  * `chronicle.searchQueries.list`
  * `chronicle.searchQueries.update`

`chronicle.searchSessions.search` `chronicle.searchedResults.list` `chronicle.sharedPreferenceSets.*`

  * `chronicle.sharedPreferenceSets.create`
  * `chronicle.sharedPreferenceSets.delete`
  * `chronicle.sharedPreferenceSets.get`
  * `chronicle.sharedPreferenceSets.list`
  * `chronicle.sharedPreferenceSets.update`

`chronicle.soarDomains.get` `chronicle.soarNetworks.get` `chronicle.socRoles.get` `chronicle.summaryTables.*`

  * `chronicle.summaryTables.create`
  * `chronicle.summaryTables.delete`
  * `chronicle.summaryTables.get`
  * `chronicle.summaryTables.list`
  * `chronicle.summaryTables.update`

`chronicle.tagSubscriptions.*`

  * `chronicle.tagSubscriptions.create`
  * `chronicle.tagSubscriptions.delete`
  * `chronicle.tagSubscriptions.get`
  * `chronicle.tagSubscriptions.list`
  * `chronicle.tagSubscriptions.update`

`chronicle.tags.*`

  * `chronicle.tags.create`
  * `chronicle.tags.delete`
  * `chronicle.tags.get`
  * `chronicle.tags.list`
  * `chronicle.tags.update`

`chronicle.tasks.*`

  * `chronicle.tasks.delete`
  * `chronicle.tasks.get`
  * `chronicle.tasks.update`

`chronicle.threatCollectionFilterSet.get` `chronicle.threatCollections.*`

  * `chronicle.threatCollections.fetchEntityMetadata`
  * `chronicle.threatCollections.fetchIocMatchMetadata`
  * `chronicle.threatCollections.fetchRelated`
  * `chronicle.threatCollections.get`
  * `chronicle.threatCollections.list`

`chronicle.transformerDefinitions.*`

  * `chronicle.transformerDefinitions.create`
  * `chronicle.transformerDefinitions.delete`
  * `chronicle.transformerDefinitions.execute`
  * `chronicle.transformerDefinitions.get`
  * `chronicle.transformerDefinitions.list`
  * `chronicle.transformerDefinitions.update`

`chronicle.transformerRevisions.*`

  * `chronicle.transformerRevisions.delete`
  * `chronicle.transformerRevisions.get`
  * `chronicle.transformerRevisions.update`

`chronicle.uniqueEntities.*`

  * `chronicle.uniqueEntities.get`
  * `chronicle.uniqueEntities.update`

`chronicle.userLocalizations.*`

  * `chronicle.userLocalizations.get`
  * `chronicle.userLocalizations.update`

`chronicle.userNotifications.*`

  * `chronicle.userNotifications.get`
  * `chronicle.userNotifications.update`

`chronicle.views.get` `chronicle.visualFamilies.get` `chronicle.watchlists.*`

  * `chronicle.watchlists.create`
  * `chronicle.watchlists.delete`
  * `chronicle.watchlists.get`
  * `chronicle.watchlists.list`
  * `chronicle.watchlists.update`

`chronicle.webhooks.*`

  * `chronicle.webhooks.delete`
  * `chronicle.webhooks.get`
  * `chronicle.webhooks.update`

`chronicle.workdeskContacts.*`

  * `chronicle.workdeskContacts.delete`
  * `chronicle.workdeskContacts.get`
  * `chronicle.workdeskContacts.update`

`chronicle.workdeskLinks.*`

  * `chronicle.workdeskLinks.delete`
  * `chronicle.workdeskLinks.get`
  * `chronicle.workdeskLinks.update`

`chronicle.workdeskNotes.*`

  * `chronicle.workdeskNotes.delete`
  * `chronicle.workdeskNotes.get`
  * `chronicle.workdeskNotes.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle API Viewer 

(`roles/chronicle.viewer`) Read-only access to the Chronicle API resources.  |  `chronicle.agentSettings.get` `chronicle.ais.*`

  * `chronicle.ais.createFeedback`
  * `chronicle.ais.translateUdmQuery`
  * `chronicle.ais.translateYlRule`

`chronicle.analyticValues.list` `chronicle.analytics.list` `chronicle.announcements.get` `chronicle.attachments.get` `chronicle.bigQueryExport.get` `chronicle.calculatedFieldDefinitions.get` `chronicle.caseAlerts.get` `chronicle.caseCloseDefinitions.get` `chronicle.caseComments.get` `chronicle.caseDetections.get` `chronicle.caseEvents.get` `chronicle.caseEvidenceDatas.get` `chronicle.caseQueueFilters.get` `chronicle.caseTagDefinitions.get` `chronicle.cases.countPriorities` `chronicle.cases.generateReport` `chronicle.cases.get` `chronicle.chatMessageAttachments.get` `chronicle.chatMessages.get` `chronicle.chatSessionMessages.list` `chronicle.chatSessions.list` `chronicle.collectors.get` `chronicle.collectors.list` `chronicle.connectorEvents.get` `chronicle.contentPacks.get` `chronicle.contextProperties.get` `chronicle.conversations.get` `chronicle.conversations.list` `chronicle.coverageDetails.*`

  * `chronicle.coverageDetails.get`
  * `chronicle.coverageDetails.list`

`chronicle.curatedRuleSetCategories.*`

  * `chronicle.curatedRuleSetCategories.countAllCuratedRuleSetDetections`
  * `chronicle.curatedRuleSetCategories.get`
  * `chronicle.curatedRuleSetCategories.list`

`chronicle.curatedRuleSetDeployments.get` `chronicle.curatedRuleSetDeployments.list` `chronicle.curatedRuleSets.*`

  * `chronicle.curatedRuleSets.countCuratedRuleSetDetections`
  * `chronicle.curatedRuleSets.get`
  * `chronicle.curatedRuleSets.list`

`chronicle.curatedRules.*`

  * `chronicle.curatedRules.get`
  * `chronicle.curatedRules.list`

`chronicle.customFieldValues.get` `chronicle.customFields.get` `chronicle.dashboardCharts.*`

  * `chronicle.dashboardCharts.get`
  * `chronicle.dashboardCharts.list`

`chronicle.dashboardQueries.*`

  * `chronicle.dashboardQueries.execute`
  * `chronicle.dashboardQueries.get`
  * `chronicle.dashboardQueries.list`

`chronicle.dashboardScheduledReports.fetchHistory` `chronicle.dashboardScheduledReports.get` `chronicle.dashboardScheduledReports.list` `chronicle.dashboards.get` `chronicle.dashboards.list` `chronicle.dashboards.schedule` `chronicle.dataAccessScopes.list` `chronicle.dataExports.fetchLogTypesAvailableForExport` `chronicle.dataExports.fetchServiceAccountForDataExport` `chronicle.dataExports.get` `chronicle.dataExports.list` `chronicle.dataTableOperationErrors.get` `chronicle.dataTableRows.bulkGet` `chronicle.dataTableRows.get` `chronicle.dataTableRows.list` `chronicle.dataTables.get` `chronicle.dataTables.list` `chronicle.dataTaps.get` `chronicle.dataTaps.list` `chronicle.enrichmentAgent.get` `chronicle.enrichmentCombination.get` `chronicle.enrichmentControls.get` `chronicle.enrichmentControls.list` `chronicle.entities.find` `chronicle.entities.findEntityAlerts` `chronicle.entities.findRelatedEntities` `chronicle.entities.get` `chronicle.entities.list` `chronicle.entities.queryEntityRiskScoreModifications` `chronicle.entities.searchEntities` `chronicle.entities.summarize` `chronicle.entities.summarizeFromQuery` `chronicle.entityRiskScores.queryEntityRiskScores` `chronicle.environmentGroups.get` `chronicle.environments.get` `chronicle.events.batchGet` `chronicle.events.fetchEnrichedEvent` `chronicle.events.findUdmFieldValues` `chronicle.events.get` `chronicle.events.queryProductSourceStats` `chronicle.events.searchRawLogs` `chronicle.events.udmSearch` `chronicle.events.validateQuery` `chronicle.featuredContentNativeDashboards.get` `chronicle.featuredContentNativeDashboards.list` `chronicle.featuredContentPlaybooks.get` `chronicle.featuredContentPlaybooks.list` `chronicle.featuredContentRules.list` `chronicle.featuredContentSearchQueries.get` `chronicle.featuredContentSearchQueries.list` `chronicle.features.get` `chronicle.features.list` `chronicle.feedPacks.*`

  * `chronicle.feedPacks.get`
  * `chronicle.feedPacks.list`

`chronicle.findingsGraphs.*`

  * `chronicle.findingsGraphs.exploreNode`
  * `chronicle.findingsGraphs.initializeGraph`

`chronicle.findingsRefinementDeployments.get` `chronicle.findingsRefinementDeployments.list` `chronicle.findingsRefinements.computeActivity` `chronicle.findingsRefinements.computeAllActivities` `chronicle.findingsRefinements.get` `chronicle.findingsRefinements.list` `chronicle.findingsRefinements.test` `chronicle.formDynamicParameters.get` `chronicle.forwarders.generate` `chronicle.forwarders.get` `chronicle.forwarders.list` `chronicle.globalDataAccessScopes.permit` `chronicle.ingestionLogLabels.*`

  * `chronicle.ingestionLogLabels.get`
  * `chronicle.ingestionLogLabels.list`

`chronicle.ingestionLogNamespaces.*`

  * `chronicle.ingestionLogNamespaces.get`
  * `chronicle.ingestionLogNamespaces.list`

`chronicle.instances.generateCollectionAgentAuth` `chronicle.instances.generateSoarAuthJwt` `chronicle.instances.get` `chronicle.instances.logTypeClassifier` `chronicle.instances.report` `chronicle.instances.suggestQueryFields` `chronicle.integrationActions.get` `chronicle.integrations.get` `chronicle.investigationComments.get` `chronicle.investigationComments.list` `chronicle.investigationSteps.*`

  * `chronicle.investigationSteps.get`
  * `chronicle.investigationSteps.list`

`chronicle.investigations.fetchAssociated` `chronicle.investigations.get` `chronicle.investigations.list` `chronicle.involvedEntities.get` `chronicle.iocAssociations.*`

  * `chronicle.iocAssociations.batchGet`
  * `chronicle.iocAssociations.fetchRelated`
  * `chronicle.iocAssociations.get`

`chronicle.iocState.get` `chronicle.iocs.*`

  * `chronicle.iocs.batchGet`
  * `chronicle.iocs.fetchRelated`
  * `chronicle.iocs.findFirstAndLastSeen`
  * `chronicle.iocs.findIocs`
  * `chronicle.iocs.get`
  * `chronicle.iocs.searchCuratedDetectionsForIoc`

`chronicle.labsExperimentExecutions.get` `chronicle.labsExperimentExecutions.list` `chronicle.labsExperiments.get` `chronicle.labsExperiments.list` `chronicle.legacies.legacyBatchGetCases` `chronicle.legacies.legacyBatchGetCollections` `chronicle.legacies.legacyFetchAlertsView` `chronicle.legacies.legacyFetchUdmSearchCsv` `chronicle.legacies.legacyFetchUdmSearchView` `chronicle.legacies.legacyFindAssetEvents` `chronicle.legacies.legacyFindRawLogs` `chronicle.legacies.legacyFindUdmEvents` `chronicle.legacies.legacyGetAlert` `chronicle.legacies.legacyGetCuratedRulesTrends` `chronicle.legacies.legacyGetDetection` `chronicle.legacies.legacyGetEventForDetection` `chronicle.legacies.legacyGetRuleCounts` `chronicle.legacies.legacyGetRulesTrends` `chronicle.legacies.legacyRunTestRule` `chronicle.legacies.legacySearchArtifactEvents` `chronicle.legacies.legacySearchArtifactIoCDetails` `chronicle.legacies.legacySearchAssetEvents` `chronicle.legacies.legacySearchCuratedDetections` `chronicle.legacies.legacySearchCustomerStats` `chronicle.legacies.legacySearchDetections` `chronicle.legacies.legacySearchDomainsRecentlyRegistered` `chronicle.legacies.legacySearchDomainsTimingStats` `chronicle.legacies.legacySearchEnterpriseWideAlerts` `chronicle.legacies.legacySearchEnterpriseWideIoCs` `chronicle.legacies.legacySearchFindings` `chronicle.legacies.legacySearchIngestionStats` `chronicle.legacies.legacySearchIoCInsights` `chronicle.legacies.legacySearchRawLogs` `chronicle.legacies.legacySearchRuleDetectionCountBuckets` `chronicle.legacies.legacySearchRuleDetectionEvents` `chronicle.legacies.legacySearchRuleResults` `chronicle.legacies.legacySearchRulesAlerts` `chronicle.legacies.legacySearchUserEvents` `chronicle.legacies.legacyStreamDetectionAlerts` `chronicle.legacies.legacyTestRuleStreaming` `chronicle.legacyCaseFederationPlatforms.get` `chronicle.legacyCases.get` `chronicle.legacyFederatedCases.get` `chronicle.legacySearches.*`

  * `chronicle.legacySearches.searchCases`
  * `chronicle.legacySearches.searchEntities`

`chronicle.legacySoarAdvancedReports.get` `chronicle.legacySoarDashboards.get` `chronicle.legacySoarReports.get` `chronicle.legacySoarSettings.get` `chronicle.legacySoarUsers.get` `chronicle.legacySystemMetadata.*`

  * `chronicle.legacySystemMetadata.get`
  * `chronicle.legacySystemMetadata.placeholders`

`chronicle.logProcessingPipelines.fetchAssociatedPipeline` `chronicle.logProcessingPipelines.fetchSampleLogsByStreams` `chronicle.logProcessingPipelines.get` `chronicle.logProcessingPipelines.list` `chronicle.logProcessingPipelines.testPipeline` `chronicle.logTypeSchemas.list` `chronicle.logs.export` `chronicle.logs.get` `chronicle.logs.list` `chronicle.managedDomainSettings.get` `chronicle.marketplaceIntegrations.get` `chronicle.messages.get` `chronicle.messages.list` `chronicle.moduleSettings.*`

  * `chronicle.moduleSettings.get`
  * `chronicle.moduleSettings.modifyCaseList`
  * `chronicle.moduleSettings.rebranding`

`chronicle.moduleSettingsProperties.get` `chronicle.multitenantDirectories.get` `chronicle.nativeDashboards.get` `chronicle.nativeDashboards.list` `chronicle.notebooks.*`

  * `chronicle.notebooks.get`
  * `chronicle.notebooks.list`

`chronicle.operations.get` `chronicle.operations.list` `chronicle.operations.streamSearch` `chronicle.operations.wait` `chronicle.preferenceSets.*`

  * `chronicle.preferenceSets.get`
  * `chronicle.preferenceSets.update`

`chronicle.propertySchemaDefinitions.get` `chronicle.queries.suggestSql` `chronicle.queryMetrics.*`

  * `chronicle.queryMetrics.get`
  * `chronicle.queryMetrics.list`

`chronicle.referenceLists.get` `chronicle.referenceLists.list` `chronicle.referenceLists.verifyReferenceList` `chronicle.requestTemplates.get` `chronicle.retrohunts.get` `chronicle.retrohunts.list` `chronicle.riskConfigs.get` `chronicle.ruleDeployments.get` `chronicle.ruleDeployments.list` `chronicle.ruleExecutionErrors.list` `chronicle.rules.get` `chronicle.rules.list` `chronicle.rules.listRevisions` `chronicle.rules.verifyRuleText` `chronicle.savedColumnSets.*`

  * `chronicle.savedColumnSets.create`
  * `chronicle.savedColumnSets.delete`
  * `chronicle.savedColumnSets.get`
  * `chronicle.savedColumnSets.list`
  * `chronicle.savedColumnSets.update`

`chronicle.searchQueries.*`

  * `chronicle.searchQueries.create`
  * `chronicle.searchQueries.delete`
  * `chronicle.searchQueries.get`
  * `chronicle.searchQueries.list`
  * `chronicle.searchQueries.update`

`chronicle.searchSessions.search` `chronicle.searchedResults.list` `chronicle.sharedPreferenceSets.get` `chronicle.sharedPreferenceSets.list` `chronicle.socRoles.get` `chronicle.summaryTables.get` `chronicle.summaryTables.list` `chronicle.tagSubscriptions.get` `chronicle.tagSubscriptions.list` `chronicle.tags.get` `chronicle.tags.list` `chronicle.threatCollectionFilterSet.get` `chronicle.threatCollections.*`

  * `chronicle.threatCollections.fetchEntityMetadata`
  * `chronicle.threatCollections.fetchIocMatchMetadata`
  * `chronicle.threatCollections.fetchRelated`
  * `chronicle.threatCollections.get`
  * `chronicle.threatCollections.list`

`chronicle.userLocalizations.get` `chronicle.userNotifications.get` `chronicle.views.get` `chronicle.watchlists.get` `chronicle.watchlists.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle API Data Governor Beta

(`roles/chronicle.dataGovernor`) Grants elevated access to control the lifecycle of the Chronicle instance and its data.  |  `chronicle.instances.delete` `chronicle.instances.undelete` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle API Federation Admin Beta

(`roles/chronicle.federationAdmin`) Full access to Chronicle Federation features.  |  `chronicle.federationGroups.*`

  * `chronicle.federationGroups.create`
  * `chronicle.federationGroups.delete`
  * `chronicle.federationGroups.get`
  * `chronicle.federationGroups.list`
  * `chronicle.federationGroups.update`

`chronicle.instances.permitFederationAccess` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle API Federation Viewer Beta

(`roles/chronicle.federationViewer`) Readonly access to Chronicle Federation Features.  |  `chronicle.federationGroups.get` `chronicle.federationGroups.list` `chronicle.instances.permitFederationAccess` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle API Global Data Access Beta

(`roles/chronicle.globalDataAccess`) Grants global access to data i.e. all data can be accessed.  |  `chronicle.globalDataAccessScopes.permit`  
  
#### Chronicle API Limited Viewer 

(`roles/chronicle.limitedViewer`) Grants read-only access to Chronicle API resources, excluding Rules and Retrohunts.  |  `chronicle.agentSettings.get` `chronicle.analyticValues.list` `chronicle.analytics.list` `chronicle.cases.countPriorities` `chronicle.chatSessionMessages.list` `chronicle.chatSessions.list` `chronicle.conversations.get` `chronicle.conversations.list` `chronicle.coverageDetails.*`

  * `chronicle.coverageDetails.get`
  * `chronicle.coverageDetails.list`

`chronicle.dashboardCharts.*`

  * `chronicle.dashboardCharts.get`
  * `chronicle.dashboardCharts.list`

`chronicle.dashboardQueries.*`

  * `chronicle.dashboardQueries.execute`
  * `chronicle.dashboardQueries.get`
  * `chronicle.dashboardQueries.list`

`chronicle.dashboards.get` `chronicle.dashboards.list` `chronicle.dashboards.schedule` `chronicle.dataAccessScopes.list` `chronicle.enrichmentCombination.get` `chronicle.enrichmentControls.get` `chronicle.enrichmentControls.list` `chronicle.entities.find` `chronicle.entities.findEntityAlerts` `chronicle.entities.findRelatedEntities` `chronicle.entities.get` `chronicle.entities.queryEntityRiskScoreModifications` `chronicle.entities.searchEntities` `chronicle.entities.summarize` `chronicle.entities.summarizeFromQuery` `chronicle.entityRiskScores.queryEntityRiskScores` `chronicle.events.batchGet` `chronicle.events.fetchEnrichedEvent` `chronicle.events.findUdmFieldValues` `chronicle.events.get` `chronicle.events.queryProductSourceStats` `chronicle.events.searchRawLogs` `chronicle.events.udmSearch` `chronicle.events.validateQuery` `chronicle.featuredContentNativeDashboards.get` `chronicle.featuredContentNativeDashboards.list` `chronicle.featuredContentSearchQueries.get` `chronicle.featuredContentSearchQueries.list` `chronicle.findingsGraphs.*`

  * `chronicle.findingsGraphs.exploreNode`
  * `chronicle.findingsGraphs.initializeGraph`

`chronicle.findingsRefinementDeployments.get` `chronicle.findingsRefinementDeployments.list` `chronicle.findingsRefinements.computeActivity` `chronicle.findingsRefinements.computeAllActivities` `chronicle.findingsRefinements.get` `chronicle.findingsRefinements.list` `chronicle.findingsRefinements.test` `chronicle.globalDataAccessScopes.permit` `chronicle.ingestionLogLabels.*`

  * `chronicle.ingestionLogLabels.get`
  * `chronicle.ingestionLogLabels.list`

`chronicle.ingestionLogNamespaces.*`

  * `chronicle.ingestionLogNamespaces.get`
  * `chronicle.ingestionLogNamespaces.list`

`chronicle.instances.get` `chronicle.instances.suggestQueryFields` `chronicle.investigationComments.get` `chronicle.investigationComments.list` `chronicle.investigationSteps.*`

  * `chronicle.investigationSteps.get`
  * `chronicle.investigationSteps.list`

`chronicle.iocAssociations.*`

  * `chronicle.iocAssociations.batchGet`
  * `chronicle.iocAssociations.fetchRelated`
  * `chronicle.iocAssociations.get`

`chronicle.iocs.fetchRelated` `chronicle.iocs.findIocs` `chronicle.legacies.legacyBatchGetCases` `chronicle.legacies.legacyBatchGetCollections` `chronicle.legacies.legacyFetchAlertsView` `chronicle.legacies.legacyFetchUdmSearchCsv` `chronicle.legacies.legacyFetchUdmSearchView` `chronicle.legacies.legacyFindAssetEvents` `chronicle.legacies.legacyFindRawLogs` `chronicle.legacies.legacyFindUdmEvents` `chronicle.legacies.legacyGetAlert` `chronicle.legacies.legacySearchArtifactEvents` `chronicle.legacies.legacySearchArtifactIoCDetails` `chronicle.legacies.legacySearchAssetEvents` `chronicle.legacies.legacySearchCustomerStats` `chronicle.legacies.legacySearchDomainsRecentlyRegistered` `chronicle.legacies.legacySearchDomainsTimingStats` `chronicle.legacies.legacySearchEnterpriseWideAlerts` `chronicle.legacies.legacySearchEnterpriseWideIoCs` `chronicle.legacies.legacySearchFindings` `chronicle.legacies.legacySearchIngestionStats` `chronicle.legacies.legacySearchIoCInsights` `chronicle.legacies.legacySearchRawLogs` `chronicle.legacies.legacySearchUserEvents` `chronicle.logTypeSchemas.list` `chronicle.logs.export` `chronicle.logs.get` `chronicle.logs.list` `chronicle.messages.get` `chronicle.messages.list` `chronicle.multitenantDirectories.get` `chronicle.nativeDashboards.get` `chronicle.nativeDashboards.list` `chronicle.notebooks.*`

  * `chronicle.notebooks.get`
  * `chronicle.notebooks.list`

`chronicle.operations.get` `chronicle.operations.list` `chronicle.operations.streamSearch` `chronicle.operations.wait` `chronicle.preferenceSets.*`

  * `chronicle.preferenceSets.get`
  * `chronicle.preferenceSets.update`

`chronicle.queries.suggestSql` `chronicle.queryMetrics.*`

  * `chronicle.queryMetrics.get`
  * `chronicle.queryMetrics.list`

`chronicle.searchQueries.*`

  * `chronicle.searchQueries.create`
  * `chronicle.searchQueries.delete`
  * `chronicle.searchQueries.get`
  * `chronicle.searchQueries.list`
  * `chronicle.searchQueries.update`

`chronicle.searchSessions.search` `chronicle.searchedResults.list` `chronicle.threatCollectionFilterSet.get` `chronicle.threatCollections.*`

  * `chronicle.threatCollections.fetchEntityMetadata`
  * `chronicle.threatCollections.fetchIocMatchMetadata`
  * `chronicle.threatCollections.fetchRelated`
  * `chronicle.threatCollections.get`
  * `chronicle.threatCollections.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle API Restricted Data Access Beta

(`roles/chronicle.restrictedDataAccess`) Grants access to data controlled by Data Access Scopes. Intended to be refined by IAM Conditions.  |  `chronicle.dataAccessScopes.permit`  
  
#### Chronicle API Restricted Data Access Viewer Beta

(`roles/chronicle.restrictedDataAccessViewer`) Grants readonly access to Chronicle API resources without global data access scope.  |  `chronicle.agentSettings.get` `chronicle.ais.*`

  * `chronicle.ais.createFeedback`
  * `chronicle.ais.translateUdmQuery`
  * `chronicle.ais.translateYlRule`

`chronicle.analyticValues.list` `chronicle.analytics.list` `chronicle.announcements.get` `chronicle.attachments.get` `chronicle.bigQueryExport.get` `chronicle.calculatedFieldDefinitions.get` `chronicle.caseAlerts.get` `chronicle.caseCloseDefinitions.get` `chronicle.caseComments.get` `chronicle.caseDetections.get` `chronicle.caseEvents.get` `chronicle.caseEvidenceDatas.get` `chronicle.caseQueueFilters.get` `chronicle.caseTagDefinitions.get` `chronicle.cases.countPriorities` `chronicle.cases.generateReport` `chronicle.cases.get` `chronicle.chatMessageAttachments.get` `chronicle.chatMessages.get` `chronicle.chatSessionMessages.list` `chronicle.chatSessions.list` `chronicle.collectors.get` `chronicle.collectors.list` `chronicle.connectorEvents.get` `chronicle.contentPacks.get` `chronicle.contextProperties.get` `chronicle.conversations.get` `chronicle.conversations.list` `chronicle.coverageDetails.*`

  * `chronicle.coverageDetails.get`
  * `chronicle.coverageDetails.list`

`chronicle.curatedRuleSetCategories.*`

  * `chronicle.curatedRuleSetCategories.countAllCuratedRuleSetDetections`
  * `chronicle.curatedRuleSetCategories.get`
  * `chronicle.curatedRuleSetCategories.list`

`chronicle.curatedRuleSetDeployments.get` `chronicle.curatedRuleSetDeployments.list` `chronicle.curatedRuleSets.*`

  * `chronicle.curatedRuleSets.countCuratedRuleSetDetections`
  * `chronicle.curatedRuleSets.get`
  * `chronicle.curatedRuleSets.list`

`chronicle.curatedRules.*`

  * `chronicle.curatedRules.get`
  * `chronicle.curatedRules.list`

`chronicle.customFieldValues.get` `chronicle.customFields.get` `chronicle.dashboardCharts.*`

  * `chronicle.dashboardCharts.get`
  * `chronicle.dashboardCharts.list`

`chronicle.dashboardQueries.*`

  * `chronicle.dashboardQueries.execute`
  * `chronicle.dashboardQueries.get`
  * `chronicle.dashboardQueries.list`

`chronicle.dashboardScheduledReports.fetchHistory` `chronicle.dashboardScheduledReports.get` `chronicle.dashboardScheduledReports.list` `chronicle.dashboards.get` `chronicle.dashboards.list` `chronicle.dashboards.schedule` `chronicle.dataAccessScopes.list` `chronicle.dataExports.fetchLogTypesAvailableForExport` `chronicle.dataExports.fetchServiceAccountForDataExport` `chronicle.dataExports.get` `chronicle.dataExports.list` `chronicle.dataTableOperationErrors.get` `chronicle.dataTableRows.bulkGet` `chronicle.dataTableRows.get` `chronicle.dataTableRows.list` `chronicle.dataTables.get` `chronicle.dataTables.list` `chronicle.dataTaps.get` `chronicle.dataTaps.list` `chronicle.enrichmentAgent.get` `chronicle.enrichmentCombination.get` `chronicle.enrichmentControls.get` `chronicle.enrichmentControls.list` `chronicle.entities.find` `chronicle.entities.findEntityAlerts` `chronicle.entities.findRelatedEntities` `chronicle.entities.get` `chronicle.entities.list` `chronicle.entities.queryEntityRiskScoreModifications` `chronicle.entities.searchEntities` `chronicle.entities.summarize` `chronicle.entities.summarizeFromQuery` `chronicle.entityRiskScores.queryEntityRiskScores` `chronicle.environmentGroups.get` `chronicle.environments.get` `chronicle.events.batchGet` `chronicle.events.fetchEnrichedEvent` `chronicle.events.findUdmFieldValues` `chronicle.events.get` `chronicle.events.queryProductSourceStats` `chronicle.events.searchRawLogs` `chronicle.events.udmSearch` `chronicle.events.validateQuery` `chronicle.featuredContentNativeDashboards.get` `chronicle.featuredContentNativeDashboards.list` `chronicle.featuredContentPlaybooks.get` `chronicle.featuredContentPlaybooks.list` `chronicle.featuredContentRules.list` `chronicle.featuredContentSearchQueries.get` `chronicle.featuredContentSearchQueries.list` `chronicle.features.get` `chronicle.features.list` `chronicle.feedPacks.*`

  * `chronicle.feedPacks.get`
  * `chronicle.feedPacks.list`

`chronicle.findingsGraphs.*`

  * `chronicle.findingsGraphs.exploreNode`
  * `chronicle.findingsGraphs.initializeGraph`

`chronicle.findingsRefinementDeployments.get` `chronicle.findingsRefinementDeployments.list` `chronicle.findingsRefinements.computeActivity` `chronicle.findingsRefinements.computeAllActivities` `chronicle.findingsRefinements.get` `chronicle.findingsRefinements.list` `chronicle.findingsRefinements.test` `chronicle.formDynamicParameters.get` `chronicle.forwarders.generate` `chronicle.forwarders.get` `chronicle.forwarders.list` `chronicle.ingestionLogLabels.*`

  * `chronicle.ingestionLogLabels.get`
  * `chronicle.ingestionLogLabels.list`

`chronicle.ingestionLogNamespaces.*`

  * `chronicle.ingestionLogNamespaces.get`
  * `chronicle.ingestionLogNamespaces.list`

`chronicle.instances.generateCollectionAgentAuth` `chronicle.instances.generateSoarAuthJwt` `chronicle.instances.get` `chronicle.instances.logTypeClassifier` `chronicle.instances.report` `chronicle.instances.suggestQueryFields` `chronicle.integrationActions.get` `chronicle.integrations.get` `chronicle.investigationComments.get` `chronicle.investigationComments.list` `chronicle.investigationSteps.*`

  * `chronicle.investigationSteps.get`
  * `chronicle.investigationSteps.list`

`chronicle.investigations.fetchAssociated` `chronicle.investigations.get` `chronicle.investigations.list` `chronicle.involvedEntities.get` `chronicle.iocAssociations.*`

  * `chronicle.iocAssociations.batchGet`
  * `chronicle.iocAssociations.fetchRelated`
  * `chronicle.iocAssociations.get`

`chronicle.iocState.get` `chronicle.iocs.*`

  * `chronicle.iocs.batchGet`
  * `chronicle.iocs.fetchRelated`
  * `chronicle.iocs.findFirstAndLastSeen`
  * `chronicle.iocs.findIocs`
  * `chronicle.iocs.get`
  * `chronicle.iocs.searchCuratedDetectionsForIoc`

`chronicle.labsExperimentExecutions.get` `chronicle.labsExperimentExecutions.list` `chronicle.labsExperiments.get` `chronicle.labsExperiments.list` `chronicle.legacies.legacyBatchGetCases` `chronicle.legacies.legacyBatchGetCollections` `chronicle.legacies.legacyFetchAlertsView` `chronicle.legacies.legacyFetchUdmSearchCsv` `chronicle.legacies.legacyFetchUdmSearchView` `chronicle.legacies.legacyFindAssetEvents` `chronicle.legacies.legacyFindRawLogs` `chronicle.legacies.legacyFindUdmEvents` `chronicle.legacies.legacyGetAlert` `chronicle.legacies.legacyGetCuratedRulesTrends` `chronicle.legacies.legacyGetDetection` `chronicle.legacies.legacyGetEventForDetection` `chronicle.legacies.legacyGetRuleCounts` `chronicle.legacies.legacyGetRulesTrends` `chronicle.legacies.legacyRunTestRule` `chronicle.legacies.legacySearchArtifactEvents` `chronicle.legacies.legacySearchArtifactIoCDetails` `chronicle.legacies.legacySearchAssetEvents` `chronicle.legacies.legacySearchCuratedDetections` `chronicle.legacies.legacySearchCustomerStats` `chronicle.legacies.legacySearchDetections` `chronicle.legacies.legacySearchDomainsRecentlyRegistered` `chronicle.legacies.legacySearchDomainsTimingStats` `chronicle.legacies.legacySearchEnterpriseWideAlerts` `chronicle.legacies.legacySearchEnterpriseWideIoCs` `chronicle.legacies.legacySearchFindings` `chronicle.legacies.legacySearchIngestionStats` `chronicle.legacies.legacySearchIoCInsights` `chronicle.legacies.legacySearchRawLogs` `chronicle.legacies.legacySearchRuleDetectionCountBuckets` `chronicle.legacies.legacySearchRuleDetectionEvents` `chronicle.legacies.legacySearchRuleResults` `chronicle.legacies.legacySearchRulesAlerts` `chronicle.legacies.legacySearchUserEvents` `chronicle.legacies.legacyStreamDetectionAlerts` `chronicle.legacies.legacyTestRuleStreaming` `chronicle.legacyCaseFederationPlatforms.get` `chronicle.legacyCases.get` `chronicle.legacyFederatedCases.get` `chronicle.legacySearches.*`

  * `chronicle.legacySearches.searchCases`
  * `chronicle.legacySearches.searchEntities`

`chronicle.legacySoarAdvancedReports.get` `chronicle.legacySoarDashboards.get` `chronicle.legacySoarReports.get` `chronicle.legacySoarSettings.get` `chronicle.legacySoarUsers.get` `chronicle.legacySystemMetadata.*`

  * `chronicle.legacySystemMetadata.get`
  * `chronicle.legacySystemMetadata.placeholders`

`chronicle.logProcessingPipelines.fetchAssociatedPipeline` `chronicle.logProcessingPipelines.fetchSampleLogsByStreams` `chronicle.logProcessingPipelines.get` `chronicle.logProcessingPipelines.list` `chronicle.logProcessingPipelines.testPipeline` `chronicle.logTypeSchemas.list` `chronicle.logs.export` `chronicle.logs.get` `chronicle.logs.list` `chronicle.managedDomainSettings.get` `chronicle.marketplaceIntegrations.get` `chronicle.messages.get` `chronicle.messages.list` `chronicle.moduleSettings.*`

  * `chronicle.moduleSettings.get`
  * `chronicle.moduleSettings.modifyCaseList`
  * `chronicle.moduleSettings.rebranding`

`chronicle.moduleSettingsProperties.get` `chronicle.multitenantDirectories.get` `chronicle.nativeDashboards.get` `chronicle.nativeDashboards.list` `chronicle.notebooks.*`

  * `chronicle.notebooks.get`
  * `chronicle.notebooks.list`

`chronicle.operations.get` `chronicle.operations.list` `chronicle.operations.streamSearch` `chronicle.operations.wait` `chronicle.preferenceSets.*`

  * `chronicle.preferenceSets.get`
  * `chronicle.preferenceSets.update`

`chronicle.propertySchemaDefinitions.get` `chronicle.queries.suggestSql` `chronicle.queryMetrics.*`

  * `chronicle.queryMetrics.get`
  * `chronicle.queryMetrics.list`

`chronicle.referenceLists.get` `chronicle.referenceLists.list` `chronicle.referenceLists.verifyReferenceList` `chronicle.requestTemplates.get` `chronicle.retrohunts.get` `chronicle.retrohunts.list` `chronicle.riskConfigs.get` `chronicle.ruleDeployments.get` `chronicle.ruleDeployments.list` `chronicle.ruleExecutionErrors.list` `chronicle.rules.get` `chronicle.rules.list` `chronicle.rules.listRevisions` `chronicle.rules.verifyRuleText` `chronicle.savedColumnSets.get` `chronicle.savedColumnSets.list` `chronicle.searchQueries.*`

  * `chronicle.searchQueries.create`
  * `chronicle.searchQueries.delete`
  * `chronicle.searchQueries.get`
  * `chronicle.searchQueries.list`
  * `chronicle.searchQueries.update`

`chronicle.searchSessions.search` `chronicle.searchedResults.list` `chronicle.sharedPreferenceSets.get` `chronicle.sharedPreferenceSets.list` `chronicle.socRoles.get` `chronicle.summaryTables.get` `chronicle.summaryTables.list` `chronicle.tagSubscriptions.get` `chronicle.tagSubscriptions.list` `chronicle.tags.get` `chronicle.tags.list` `chronicle.threatCollectionFilterSet.get` `chronicle.threatCollections.*`

  * `chronicle.threatCollections.fetchEntityMetadata`
  * `chronicle.threatCollections.fetchIocMatchMetadata`
  * `chronicle.threatCollections.fetchRelated`
  * `chronicle.threatCollections.get`
  * `chronicle.threatCollections.list`

`chronicle.userLocalizations.get` `chronicle.userNotifications.get` `chronicle.views.get` `chronicle.watchlists.get` `chronicle.watchlists.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle SOAR Admin 

(`roles/chronicle.soarAdmin`) Grants admin access to Chronicle SOAR.  |  `chronicle.alertGroupingRules.*`

  * `chronicle.alertGroupingRules.delete`
  * `chronicle.alertGroupingRules.get`
  * `chronicle.alertGroupingRules.update`

`chronicle.announcements.*`

  * `chronicle.announcements.delete`
  * `chronicle.announcements.get`
  * `chronicle.announcements.update`

`chronicle.attachments.*`

  * `chronicle.attachments.delete`
  * `chronicle.attachments.get`
  * `chronicle.attachments.update`

`chronicle.calculatedFieldDefinitions.*`

  * `chronicle.calculatedFieldDefinitions.delete`
  * `chronicle.calculatedFieldDefinitions.get`
  * `chronicle.calculatedFieldDefinitions.update`

`chronicle.caseAlerts.*`

  * `chronicle.caseAlerts.get`
  * `chronicle.caseAlerts.metadataUpdate`
  * `chronicle.caseAlerts.move`
  * `chronicle.caseAlerts.removeTag`
  * `chronicle.caseAlerts.updateSla`
  * `chronicle.caseAlerts.updateTag`

`chronicle.caseCloseDefinitions.*`

  * `chronicle.caseCloseDefinitions.delete`
  * `chronicle.caseCloseDefinitions.get`
  * `chronicle.caseCloseDefinitions.update`

`chronicle.caseComments.*`

  * `chronicle.caseComments.delete`
  * `chronicle.caseComments.get`
  * `chronicle.caseComments.update`

`chronicle.caseDetections.get` `chronicle.caseEvents.get` `chronicle.caseEvidenceDatas.get` `chronicle.caseQueueFilters.*`

  * `chronicle.caseQueueFilters.delete`
  * `chronicle.caseQueueFilters.get`
  * `chronicle.caseQueueFilters.update`

`chronicle.caseStageDefinitions.*`

  * `chronicle.caseStageDefinitions.delete`
  * `chronicle.caseStageDefinitions.get`
  * `chronicle.caseStageDefinitions.update`

`chronicle.caseTagDefinitions.*`

  * `chronicle.caseTagDefinitions.delete`
  * `chronicle.caseTagDefinitions.get`
  * `chronicle.caseTagDefinitions.update`

`chronicle.caseWallRecords.*`

  * `chronicle.caseWallRecords.get`
  * `chronicle.caseWallRecords.update`

`chronicle.cases.*`

  * `chronicle.cases.close`
  * `chronicle.cases.countPriorities`
  * `chronicle.cases.generateReport`
  * `chronicle.cases.get`
  * `chronicle.cases.removeTag`
  * `chronicle.cases.reopen`
  * `chronicle.cases.update`
  * `chronicle.cases.updateTag`

`chronicle.chatMessageAttachments.get` `chronicle.chatMessages.*`

  * `chronicle.chatMessages.create`
  * `chronicle.chatMessages.get`
  * `chronicle.chatMessages.pin`

`chronicle.connectorEvents.get` `chronicle.connectorInstanceLogs.get` `chronicle.connectorInstances.*`

  * `chronicle.connectorInstances.delete`
  * `chronicle.connectorInstances.get`
  * `chronicle.connectorInstances.update`

`chronicle.connectorRevisions.*`

  * `chronicle.connectorRevisions.delete`
  * `chronicle.connectorRevisions.get`
  * `chronicle.connectorRevisions.update`

`chronicle.connectors.*`

  * `chronicle.connectors.delete`
  * `chronicle.connectors.get`
  * `chronicle.connectors.update`

`chronicle.contentPacks.*`

  * `chronicle.contentPacks.create`
  * `chronicle.contentPacks.delete`
  * `chronicle.contentPacks.export`
  * `chronicle.contentPacks.get`
  * `chronicle.contentPacks.install`

`chronicle.contextProperties.*`

  * `chronicle.contextProperties.delete`
  * `chronicle.contextProperties.get`
  * `chronicle.contextProperties.update`

`chronicle.customFieldValues.*`

  * `chronicle.customFieldValues.get`
  * `chronicle.customFieldValues.update`

`chronicle.customFields.*`

  * `chronicle.customFields.delete`
  * `chronicle.customFields.get`
  * `chronicle.customFields.update`

`chronicle.customLists.*`

  * `chronicle.customLists.delete`
  * `chronicle.customLists.get`
  * `chronicle.customLists.update`

`chronicle.dataAccessScopes.list` `chronicle.emailTemplates.*`

  * `chronicle.emailTemplates.delete`
  * `chronicle.emailTemplates.get`
  * `chronicle.emailTemplates.update`

`chronicle.enrichmentAgent.*`

  * `chronicle.enrichmentAgent.execute`
  * `chronicle.enrichmentAgent.get`

`chronicle.entitiesBlocklists.*`

  * `chronicle.entitiesBlocklists.delete`
  * `chronicle.entitiesBlocklists.get`
  * `chronicle.entitiesBlocklists.update`

`chronicle.environmentGroups.*`

  * `chronicle.environmentGroups.delete`
  * `chronicle.environmentGroups.get`
  * `chronicle.environmentGroups.update`

`chronicle.environments.*`

  * `chronicle.environments.delete`
  * `chronicle.environments.get`
  * `chronicle.environments.update`

`chronicle.featuredContentPlaybooks.*`

  * `chronicle.featuredContentPlaybooks.get`
  * `chronicle.featuredContentPlaybooks.install`
  * `chronicle.featuredContentPlaybooks.list`

`chronicle.formDynamicParameters.*`

  * `chronicle.formDynamicParameters.get`
  * `chronicle.formDynamicParameters.update`

`chronicle.instances.generateSoarAuthJwt` `chronicle.instances.generateSoarChatMessage` `chronicle.instances.get` `chronicle.instances.soarAdmin` `chronicle.integrationActionRevisions.*`

  * `chronicle.integrationActionRevisions.delete`
  * `chronicle.integrationActionRevisions.get`
  * `chronicle.integrationActionRevisions.update`

`chronicle.integrationActions.*`

  * `chronicle.integrationActions.delete`
  * `chronicle.integrationActions.get`
  * `chronicle.integrationActions.run`
  * `chronicle.integrationActions.update`

`chronicle.integrationInstances.*`

  * `chronicle.integrationInstances.delete`
  * `chronicle.integrationInstances.get`
  * `chronicle.integrationInstances.update`

`chronicle.integrationLogicalOperatorRevisions.*`

  * `chronicle.integrationLogicalOperatorRevisions.delete`
  * `chronicle.integrationLogicalOperatorRevisions.get`
  * `chronicle.integrationLogicalOperatorRevisions.update`

`chronicle.integrationLogicalOperators.*`

  * `chronicle.integrationLogicalOperators.delete`
  * `chronicle.integrationLogicalOperators.execute`
  * `chronicle.integrationLogicalOperators.get`
  * `chronicle.integrationLogicalOperators.update`

`chronicle.integrations.*`

  * `chronicle.integrations.delete`
  * `chronicle.integrations.get`
  * `chronicle.integrations.update`

`chronicle.involvedEntities.*`

  * `chronicle.involvedEntities.get`
  * `chronicle.involvedEntities.update`

`chronicle.jobInstanceLogs.get` `chronicle.jobInstances.*`

  * `chronicle.jobInstances.delete`
  * `chronicle.jobInstances.get`
  * `chronicle.jobInstances.run`
  * `chronicle.jobInstances.update`

`chronicle.jobRevisions.*`

  * `chronicle.jobRevisions.delete`
  * `chronicle.jobRevisions.get`
  * `chronicle.jobRevisions.update`

`chronicle.jobs.*`

  * `chronicle.jobs.delete`
  * `chronicle.jobs.get`
  * `chronicle.jobs.update`

`chronicle.legacyCaseFederationPlatforms.*`

  * `chronicle.legacyCaseFederationPlatforms.delete`
  * `chronicle.legacyCaseFederationPlatforms.get`
  * `chronicle.legacyCaseFederationPlatforms.update`

`chronicle.legacyCases.*`

  * `chronicle.legacyCases.createManual`
  * `chronicle.legacyCases.createSimulated`
  * `chronicle.legacyCases.deleteSimulated`
  * `chronicle.legacyCases.exportJson`
  * `chronicle.legacyCases.get`
  * `chronicle.legacyCases.getSimulated`
  * `chronicle.legacyCases.importJson`
  * `chronicle.legacyCases.ingest`
  * `chronicle.legacyCases.ingestAlertTestCase`
  * `chronicle.legacyCases.runManualAction`
  * `chronicle.legacyCases.simulate`

`chronicle.legacyConfiguration.getMaximumAlertsGroupingConfiguration` `chronicle.legacyFederatedCases.*`

  * `chronicle.legacyFederatedCases.batchPatchFederatedCases`
  * `chronicle.legacyFederatedCases.fetchCasesToSync`
  * `chronicle.legacyFederatedCases.get`

`chronicle.legacyPlaybooks.*`

  * `chronicle.legacyPlaybooks.delete`
  * `chronicle.legacyPlaybooks.export`
  * `chronicle.legacyPlaybooks.get`
  * `chronicle.legacyPlaybooks.import`
  * `chronicle.legacyPlaybooks.update`

`chronicle.legacyPublisher.*`

  * `chronicle.legacyPublisher.get`
  * `chronicle.legacyPublisher.update`

`chronicle.legacySdk.*`

  * `chronicle.legacySdk.get`
  * `chronicle.legacySdk.update`

`chronicle.legacySearches.*`

  * `chronicle.legacySearches.searchCases`
  * `chronicle.legacySearches.searchEntities`

`chronicle.legacySoarAdvancedReports.*`

  * `chronicle.legacySoarAdvancedReports.delete`
  * `chronicle.legacySoarAdvancedReports.get`
  * `chronicle.legacySoarAdvancedReports.share`
  * `chronicle.legacySoarAdvancedReports.update`

`chronicle.legacySoarAudits.legacySoarAudit` `chronicle.legacySoarDashboards.*`

  * `chronicle.legacySoarDashboards.delete`
  * `chronicle.legacySoarDashboards.get`
  * `chronicle.legacySoarDashboards.update`

`chronicle.legacySoarIdpMappingGroups.*`

  * `chronicle.legacySoarIdpMappingGroups.delete`
  * `chronicle.legacySoarIdpMappingGroups.get`
  * `chronicle.legacySoarIdpMappingGroups.update`

`chronicle.legacySoarPermissionGroups.get` `chronicle.legacySoarReports.*`

  * `chronicle.legacySoarReports.delete`
  * `chronicle.legacySoarReports.get`
  * `chronicle.legacySoarReports.update`

`chronicle.legacySoarSettings.*`

  * `chronicle.legacySoarSettings.get`
  * `chronicle.legacySoarSettings.update`

`chronicle.legacySoarUsers.*`

  * `chronicle.legacySoarUsers.delete`
  * `chronicle.legacySoarUsers.get`

`chronicle.legacySystem.*`

  * `chronicle.legacySystem.getLicenseStatus`
  * `chronicle.legacySystem.getMaximumDataRetentionValue`
  * `chronicle.legacySystem.getSystemVersion`

`chronicle.legacySystemMetadata.*`

  * `chronicle.legacySystemMetadata.get`
  * `chronicle.legacySystemMetadata.placeholders`

`chronicle.managerRevisions.*`

  * `chronicle.managerRevisions.delete`
  * `chronicle.managerRevisions.get`
  * `chronicle.managerRevisions.update`

`chronicle.managers.*`

  * `chronicle.managers.delete`
  * `chronicle.managers.get`
  * `chronicle.managers.update`

`chronicle.mappingRules.*`

  * `chronicle.mappingRules.delete`
  * `chronicle.mappingRules.get`
  * `chronicle.mappingRules.update`

`chronicle.marketplaceIntegrations.*`

  * `chronicle.marketplaceIntegrations.get`
  * `chronicle.marketplaceIntegrations.install`
  * `chronicle.marketplaceIntegrations.uninstall`

`chronicle.moduleSettings.*`

  * `chronicle.moduleSettings.get`
  * `chronicle.moduleSettings.modifyCaseList`
  * `chronicle.moduleSettings.rebranding`

`chronicle.moduleSettingsProperties.*`

  * `chronicle.moduleSettingsProperties.get`
  * `chronicle.moduleSettingsProperties.testSettings`
  * `chronicle.moduleSettingsProperties.update`

`chronicle.notificationSettings.*`

  * `chronicle.notificationSettings.get`
  * `chronicle.notificationSettings.update`

`chronicle.ontologyRecords.*`

  * `chronicle.ontologyRecords.get`
  * `chronicle.ontologyRecords.update`

`chronicle.preferenceSets.*`

  * `chronicle.preferenceSets.get`
  * `chronicle.preferenceSets.update`

`chronicle.propertySchemaDefinitions.*`

  * `chronicle.propertySchemaDefinitions.delete`
  * `chronicle.propertySchemaDefinitions.get`
  * `chronicle.propertySchemaDefinitions.update`

`chronicle.remoteAgents.*`

  * `chronicle.remoteAgents.delete`
  * `chronicle.remoteAgents.get`
  * `chronicle.remoteAgents.update`

`chronicle.requestTemplates.*`

  * `chronicle.requestTemplates.delete`
  * `chronicle.requestTemplates.get`
  * `chronicle.requestTemplates.update`

`chronicle.slaDefinitions.*`

  * `chronicle.slaDefinitions.delete`
  * `chronicle.slaDefinitions.get`
  * `chronicle.slaDefinitions.update`

`chronicle.soarDomains.*`

  * `chronicle.soarDomains.delete`
  * `chronicle.soarDomains.get`
  * `chronicle.soarDomains.update`

`chronicle.soarNetworks.*`

  * `chronicle.soarNetworks.delete`
  * `chronicle.soarNetworks.get`
  * `chronicle.soarNetworks.update`

`chronicle.socRoles.*`

  * `chronicle.socRoles.delete`
  * `chronicle.socRoles.get`
  * `chronicle.socRoles.update`

`chronicle.systemNotifications.*`

  * `chronicle.systemNotifications.get`
  * `chronicle.systemNotifications.update`

`chronicle.tasks.*`

  * `chronicle.tasks.delete`
  * `chronicle.tasks.get`
  * `chronicle.tasks.update`

`chronicle.transformerDefinitions.*`

  * `chronicle.transformerDefinitions.create`
  * `chronicle.transformerDefinitions.delete`
  * `chronicle.transformerDefinitions.execute`
  * `chronicle.transformerDefinitions.get`
  * `chronicle.transformerDefinitions.list`
  * `chronicle.transformerDefinitions.update`

`chronicle.transformerRevisions.*`

  * `chronicle.transformerRevisions.delete`
  * `chronicle.transformerRevisions.get`
  * `chronicle.transformerRevisions.update`

`chronicle.uniqueEntities.*`

  * `chronicle.uniqueEntities.get`
  * `chronicle.uniqueEntities.update`

`chronicle.userLocalizations.*`

  * `chronicle.userLocalizations.get`
  * `chronicle.userLocalizations.update`

`chronicle.userNotifications.*`

  * `chronicle.userNotifications.get`
  * `chronicle.userNotifications.update`

`chronicle.views.*`

  * `chronicle.views.get`
  * `chronicle.views.update`

`chronicle.visualFamilies.*`

  * `chronicle.visualFamilies.delete`
  * `chronicle.visualFamilies.get`
  * `chronicle.visualFamilies.update`

`chronicle.webhooks.*`

  * `chronicle.webhooks.delete`
  * `chronicle.webhooks.get`
  * `chronicle.webhooks.update`

`chronicle.workdeskContacts.*`

  * `chronicle.workdeskContacts.delete`
  * `chronicle.workdeskContacts.get`
  * `chronicle.workdeskContacts.update`

`chronicle.workdeskLinks.*`

  * `chronicle.workdeskLinks.delete`
  * `chronicle.workdeskLinks.get`
  * `chronicle.workdeskLinks.update`

`chronicle.workdeskNotes.*`

  * `chronicle.workdeskNotes.delete`
  * `chronicle.workdeskNotes.get`
  * `chronicle.workdeskNotes.update`

`cloudasset.assets.exportResource` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.assets.searchEnrichmentResourceOwners` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.attackpaths.list` `securitycenter.exposurepathexplan.get` `securitycenter.findings.bulkMuteUpdate` `securitycenter.findings.group` `securitycenter.findings.list` `securitycenter.findings.listFindingPropertyNames` `securitycenter.findings.setMute` `securitycenter.findings.setState` `securitycenter.findings.update` `securitycenter.findingsecuritymarks.update` `securitycenter.simulations.get` `securitycenter.userinterfacemetadata.get` `securitycenter.valuedresources.list`  
  
#### Chronicle SOAR Remote Agent Beta

(`roles/chronicle.soarRemoteAgent`) Grants Remote Agent access to Chronicle SOAR.  |  `chronicle.legacyPublisher.*`

  * `chronicle.legacyPublisher.get`
  * `chronicle.legacyPublisher.update`

`chronicle.legacySdk.*`

  * `chronicle.legacySdk.get`
  * `chronicle.legacySdk.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle SOAR Threat Manager 

(`roles/chronicle.soarThreatManager`) Grants threat manager access to Chronicle SOAR.  |  `chronicle.dataAccessScopes.list` `chronicle.environmentGroups.get` `chronicle.instances.generateSoarChatMessage` `chronicle.instances.get` `chronicle.instances.soarThreatManager` `chronicle.integrations.get` `chronicle.legacySoarAdvancedReports.get` `chronicle.legacySoarUsers.get` `chronicle.moduleSettings.rebranding` `chronicle.moduleSettingsProperties.get` `chronicle.preferenceSets.*`

  * `chronicle.preferenceSets.get`
  * `chronicle.preferenceSets.update`

`chronicle.socRoles.get` `chronicle.userLocalizations.get` `chronicle.userNotifications.get` `cloudasset.assets.exportResource` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.assets.searchEnrichmentResourceOwners` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.attackpaths.list` `securitycenter.exposurepathexplan.get` `securitycenter.findings.bulkMuteUpdate` `securitycenter.findings.group` `securitycenter.findings.list` `securitycenter.findings.listFindingPropertyNames` `securitycenter.findings.setMute` `securitycenter.findings.setState` `securitycenter.findings.update` `securitycenter.findingsecuritymarks.update` `securitycenter.simulations.get` `securitycenter.userinterfacemetadata.get` `securitycenter.valuedresources.list`  
  
#### Chronicle SOAR Vulnerability Manager 

(`roles/chronicle.soarVulnerabilityManager`) Grants vulnerability manager access to Chronicle SOAR.  |  `chronicle.dataAccessScopes.list` `chronicle.environmentGroups.get` `chronicle.instances.get` `chronicle.instances.soarVulnerabilityManager` `chronicle.integrations.get` `chronicle.legacySoarAdvancedReports.get` `chronicle.legacySoarUsers.get` `chronicle.moduleSettings.rebranding` `chronicle.moduleSettingsProperties.get` `chronicle.preferenceSets.*`

  * `chronicle.preferenceSets.get`
  * `chronicle.preferenceSets.update`

`chronicle.socRoles.get` `chronicle.userLocalizations.get` `chronicle.userNotifications.get` `cloudasset.assets.exportResource` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.assets.searchEnrichmentResourceOwners` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.attackpaths.list` `securitycenter.exposurepathexplan.get` `securitycenter.findings.bulkMuteUpdate` `securitycenter.findings.group` `securitycenter.findings.list` `securitycenter.findings.listFindingPropertyNames` `securitycenter.findings.setMute` `securitycenter.findings.setState` `securitycenter.findings.update` `securitycenter.findingsecuritymarks.update` `securitycenter.simulations.get` `securitycenter.userinterfacemetadata.get` `securitycenter.valuedresources.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Chronicle Organization Service Agent 

(`roles/chronicle.orgServiceAgent`) Gives Secops Service Agent access to organization level resources like CAI.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudasset.assets.analyzeIamPolicy` `cloudasset.assets.listIamPolicy` `cloudasset.assets.listOSInventories` `cloudasset.assets.listOrgPolicy` `cloudasset.assets.listResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `iam.roles.get`  
  
#### Chronicle Service Agent 

(`roles/chronicle.serviceAgent`) Grants Chronicle global data access to customer project  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.connections.create` `bigquery.connections.delegate` `bigquery.connections.delete` `bigquery.connections.get` `bigquery.connections.getIamPolicy` `bigquery.connections.list` `bigquery.connections.update` `bigquery.connections.updateTag` `bigquery.connections.use` `bigquery.datasets.create` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.tables.create` `bigquery.tables.delete` `bigquery.tables.get` `bigquery.tables.update` `bigquery.tables.updateData` `chronicle.caseAlerts.get` `chronicle.caseComments.update` `chronicle.conversations.create` `chronicle.dashboards.copy` `chronicle.dashboards.create` `chronicle.dashboards.get` `chronicle.dashboards.list` `chronicle.dataTableRows.bulkCreate` `chronicle.dataTableRows.delete` `chronicle.dataTableRows.list` `chronicle.dataTables.get` `chronicle.dataTables.list` `chronicle.enrichmentAgent.*`

  * `chronicle.enrichmentAgent.execute`
  * `chronicle.enrichmentAgent.get`

`chronicle.entities.findRelatedEntities` `chronicle.entities.summarize` `chronicle.entities.summarizeFromQuery` `chronicle.events.udmSearch` `chronicle.globalDataAccessScopes.permit` `chronicle.instances.get` `chronicle.integrationInstances.get` `chronicle.integrations.get` `chronicle.investigations.get` `chronicle.investigations.list` `chronicle.investigations.trigger` `chronicle.legacies.legacyCreateSoarAlert` `chronicle.legacies.legacyGetDetection` `chronicle.legacies.legacySearchArtifactIoCDetails` `chronicle.legacies.legacySearchAssetEvents` `chronicle.legacies.legacySearchCuratedDetections` `chronicle.legacies.legacySearchDetections` `chronicle.legacies.legacySearchEnterpriseWideIoCs` `chronicle.legacies.legacyStreamDetectionAlerts` `chronicle.legacies.legacyUpdateAlert` `chronicle.legacyCases.runManualAction` `chronicle.legacySdk.*`

  * `chronicle.legacySdk.get`
  * `chronicle.legacySdk.update`

`chronicle.messages.create` `chronicle.messages.delete` `chronicle.moduleSettings.get` `chronicle.moduleSettingsProperties.get` `chronicle.preferenceSets.update` `chronicle.referenceLists.get` `chronicle.referenceLists.list` `chronicle.referenceLists.update` `chronicle.retrohunts.create` `chronicle.rules.get` `cloudaicompanion.geminiGcpEnablementSettings.get` `cloudaicompanion.geminiGcpEnablementSettings.list` `geminicloudassist.agents.invoke` `geminicloudassist.locations.*`

  * `geminicloudassist.locations.get`
  * `geminicloudassist.locations.list`

`logging.logEntries.create` `logging.logEntries.route` `mcp.tools.call` `monitoring.alertPolicies.create` `monitoring.alertPolicies.delete` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.update` `resourcemanager.projects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `storage.buckets.create` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.setIamPolicy` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list`  
  
#### Chronicle SOAR Service Agent 

(`roles/chronicle.soarServiceAgent`) Gives Chronicle SOAR the ability to perform remediation on Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudasset.assets.analyzeIamPolicy` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `compute.firewalls.get` `compute.firewalls.update` `compute.globalOperations.get` `compute.instances.deleteAccessConfig` `compute.instances.get` `compute.instances.list` `compute.instances.stop` `compute.instances.updateNetworkInterface` `compute.networks.updatePolicy` `compute.regionOperations.get` `compute.zoneOperations.get` `compute.zones.list` `iam.serviceAccounts.disable` `iam.serviceAccounts.list` `recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`resourcemanager.organizations.getIamPolicy` `securitycenter.findingexternalsystems.update` `securitycenter.findings.list` `securitycenter.findings.setMute` `securitycenter.findings.setState` `securitycenter.findings.update` `securitycenter.notificationconfig.create` `securitycenter.notificationconfig.delete` `securitycenter.notificationconfig.get` `securitycenter.notificationconfig.update` `securitycenter.sources.list` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list` `storage.buckets.update`  
  
## Google Security Operations permissions

Permission | Included in roles  
---|---  
  
#### `chronicle.agentSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.agentSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.ais.createFeedback`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.ais.translateUdmQuery`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.ais.translateYlRule`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.alertGroupingRules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.alertGroupingRules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.alertGroupingRules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.analyticValues.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.analytics.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.announcements.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.announcements.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.announcements.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.attachments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.attachments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.attachments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.bigQueryAccess.provide`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.bigQueryExport.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.bigQueryExport.provision`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.bigQueryExport.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.calculatedFieldDefinitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.calculatedFieldDefinitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.calculatedFieldDefinitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseAlerts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.caseAlerts.metadataUpdate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseAlerts.move`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseAlerts.removeTag`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseAlerts.updateSla`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseAlerts.updateTag`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseCloseDefinitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseCloseDefinitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.caseCloseDefinitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseComments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseComments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.caseComments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.caseDetections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.caseEvents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.caseEvidenceDatas.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.caseQueueFilters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseQueueFilters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.caseQueueFilters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseStageDefinitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseStageDefinitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseStageDefinitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseTagDefinitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseTagDefinitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseTagDefinitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.caseWallRecords.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.caseWallRecords.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.cases.close`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.cases.countPriorities`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.cases.generateReport`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.cases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.cases.removeTag`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.cases.reopen`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.cases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.cases.updateTag`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.chatMessageAttachments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.chatMessages.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.chatMessages.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.chatMessages.pin`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.chatSessionMessages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.chatSessionMessages.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.chatSessions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.chatSessions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.collectors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.collectors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.collectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.collectors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.collectors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.connectorEvents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.connectorInstanceLogs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.connectorInstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.connectorInstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.connectorInstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.connectorRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.connectorRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.connectorRevisions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.connectors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.connectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.connectors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.contentPacks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.contentPacks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.contentPacks.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.contentPacks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.contentPacks.install`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.contextProperties.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.contextProperties.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.contextProperties.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.conversations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.conversations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.conversations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.conversations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.conversations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.coverageDetails.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.coverageDetails.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRuleSetCategories.countAllCuratedRuleSetDetections`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRuleSetCategories.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRuleSetCategories.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRuleSetDeployments.batchUpdate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.curatedRuleSetDeployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRuleSetDeployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRuleSetDeployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.curatedRuleSets.countCuratedRuleSetDetections`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRuleSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRuleSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.curatedRules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.customFieldValues.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.customFieldValues.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.customFields.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.customFields.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.customFields.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.customLists.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.customLists.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.customLists.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.dashboardCharts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dashboardCharts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dashboardQueries.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dashboardQueries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dashboardQueries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dashboardScheduledReports.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dashboardScheduledReports.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dashboardScheduledReports.duplicate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dashboardScheduledReports.fetchHistory`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dashboardScheduledReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dashboardScheduledReports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dashboardScheduledReports.trigger`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dashboardScheduledReports.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dashboards.copy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dashboards.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dashboards.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dashboards.edit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dashboards.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dashboards.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dashboards.schedule`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)   
  
#### `chronicle.dataAccessLabels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.dataAccessLabels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.dataAccessLabels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.dataAccessLabels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.dataAccessLabels.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.dataAccessScopes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.dataAccessScopes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.dataAccessScopes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.dataAccessScopes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.dataAccessScopes.permit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Restricted Data Access](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccess) (`roles/chronicle.restrictedDataAccess`)   
  
#### `chronicle.dataAccessScopes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.dataExports.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataExports.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataExports.fetchLogTypesAvailableForExport`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataExports.fetchServiceAccountForDataExport`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataExports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataExports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataExports.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableOperationErrors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataTableRows.asyncBulkAppend`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.asyncBulkCreate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.asyncBulkDelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.asyncBulkReplace`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.asyncBulkUpdate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.bulkCreate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dataTableRows.bulkDelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.bulkGet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataTableRows.bulkReplace`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.bulkUpdate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTableRows.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dataTableRows.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataTableRows.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dataTableRows.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTables.bulkCreateDataTableAsync`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTables.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTables.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTables.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dataTables.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.dataTables.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTaps.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTaps.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.dataTaps.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataTaps.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.dataTaps.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.emailTemplates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.emailTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.emailTemplates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.enrichmentAgent.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.enrichmentAgent.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.enrichmentCombination.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.enrichmentControls.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.enrichmentControls.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.enrichmentControls.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.enrichmentControls.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.enrichmentControls.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.entities.batchCreate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.entities.batchDelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.entities.batchValidate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.entities.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.entities.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.entities.find`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.entities.findEntityAlerts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.entities.findRelatedEntities`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.entities.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.entities.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.entities.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.entities.modifyEntityRiskScore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.entities.queryEntityRiskScoreModifications`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.entities.searchEntities`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.entities.summarize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.entities.summarizeFromQuery`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.entitiesBlocklists.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.entitiesBlocklists.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.entitiesBlocklists.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.entityRiskScores.queryEntityRiskScores`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.environmentGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.environmentGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.environmentGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.environments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.environments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.environments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.events.batchGet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.events.fetchEnrichedEvent`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.events.findUdmFieldValues`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.events.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.events.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.events.queryProductSourceStats`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.events.searchRawLogs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.events.udmSearch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.events.validateQuery`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.extensionValidationReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.extensionValidationReports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.featuredContentNativeDashboards.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.featuredContentNativeDashboards.install`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.featuredContentNativeDashboards.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.featuredContentPlaybooks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.featuredContentPlaybooks.install`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.featuredContentPlaybooks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.featuredContentRules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.featuredContentSearchQueries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.featuredContentSearchQueries.install`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.featuredContentSearchQueries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.features.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.features.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.features.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.features.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.federationGroups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Federation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationAdmin) (`roles/chronicle.federationAdmin`)   
  
#### `chronicle.federationGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Federation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationAdmin) (`roles/chronicle.federationAdmin`)   
  
#### `chronicle.federationGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Federation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationAdmin) (`roles/chronicle.federationAdmin`)  [Chronicle API Federation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationViewer) (`roles/chronicle.federationViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.federationGroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Federation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationAdmin) (`roles/chronicle.federationAdmin`)  [Chronicle API Federation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationViewer) (`roles/chronicle.federationViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.federationGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Federation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationAdmin) (`roles/chronicle.federationAdmin`)   
  
#### `chronicle.feedPacks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)   
  
#### `chronicle.feedPacks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.feedServiceAccounts.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.feedSourceTypeSchemas.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.feeds.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.feeds.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.feeds.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.feeds.enable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.feeds.generateSecret`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.feeds.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.feeds.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.feeds.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.findingsGraphs.exploreNode`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsGraphs.initializeGraph`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsRefinementDeployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsRefinementDeployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsRefinementDeployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.findingsRefinements.computeActivity`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsRefinements.computeAllActivities`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsRefinements.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.findingsRefinements.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsRefinements.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsRefinements.test`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.findingsRefinements.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.formDynamicParameters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.formDynamicParameters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.forwarders.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.forwarders.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.forwarders.generate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.forwarders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.forwarders.importStatsEvents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.forwarders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.forwarders.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.globalDataAccessScopes.permit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Global Data Access](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.globalDataAccess) (`roles/chronicle.globalDataAccess`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.ingestionLogLabels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.ingestionLogLabels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.ingestionLogNamespaces.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.ingestionLogNamespaces.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Data Governor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.dataGovernor) (`roles/chronicle.dataGovernor`)   
  
#### `chronicle.instances.generateCollectionAgentAuth`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.instances.generateSoarAuthJwt`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.instances.generateSoarChatMessage`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)   
  
#### `chronicle.instances.generateWorkspaceConnectionToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.instances.graduatePocInstance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.instances.logTypeClassifier`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.instances.permitFederationAccess`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Federation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationAdmin) (`roles/chronicle.federationAdmin`)  [Chronicle API Federation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.federationViewer) (`roles/chronicle.federationViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.instances.report`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.instances.runThreatHunt`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.instances.soarAdmin`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.instances.soarThreatManager`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)   
  
#### `chronicle.instances.soarVulnerabilityManager`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)   
  
#### `chronicle.instances.suggestQueryFields`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.instances.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Data Governor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.dataGovernor) (`roles/chronicle.dataGovernor`)   
  
#### `chronicle.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.instances.verifyNonce`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.integrationActionRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationActionRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.integrationActionRevisions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationActions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationActions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.integrationActions.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationActions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationInstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationInstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.integrationInstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationLogicalOperatorRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationLogicalOperatorRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.integrationLogicalOperatorRevisions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationLogicalOperators.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationLogicalOperators.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrationLogicalOperators.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.integrationLogicalOperators.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.integrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.integrations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.investigationComments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.investigationComments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.investigationComments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.investigationComments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.investigationComments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.investigationSteps.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.investigationSteps.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.investigations.fetchAssociated`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.investigations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.investigations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.investigations.transitionReviewState`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.investigations.trigger`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.involvedEntities.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.involvedEntities.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.iocAssociations.batchGet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocAssociations.fetchRelated`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocAssociations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocState.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocState.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.iocs.batchGet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocs.fetchRelated`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocs.findFirstAndLastSeen`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocs.findIocs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.iocs.searchCuratedDetectionsForIoc`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.jobInstanceLogs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.jobInstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.jobInstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.jobInstances.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.jobInstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.jobRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.jobRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.jobRevisions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.jobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.jobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.jobs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.labsExperimentExecutions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.labsExperimentExecutions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.labsExperimentExecutions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.labsExperiments.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.labsExperiments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.labsExperiments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.labsExperiments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.legacies.legacyBatchGetCases`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyBatchGetCollections`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyCreateSoarAlert`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacies.legacyFetchAlertsView`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyFetchUdmSearchCsv`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyFetchUdmSearchView`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyFindAssetEvents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyFindRawLogs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyFindUdmEvents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyGetAlert`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyGetCuratedRulesTrends`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyGetDetection`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacies.legacyGetEventForDetection`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyGetRuleCounts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyGetRulesTrends`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyRunTestRule`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchArtifactEvents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchArtifactIoCDetails`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacies.legacySearchAssetEvents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacies.legacySearchCuratedDetections`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacies.legacySearchCustomerStats`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchDetections`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacies.legacySearchDomainsRecentlyRegistered`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchDomainsTimingStats`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchEnterpriseWideAlerts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchEnterpriseWideIoCs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacies.legacySearchFindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchIngestionStats`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchIoCInsights`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchRawLogs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchRuleDetectionCountBuckets`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchRuleDetectionEvents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchRuleResults`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchRulesAlerts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacySearchUserEvents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyStreamDetectionAlerts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacies.legacyTestRuleStreaming`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacies.legacyUpdateAlert`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacyCaseFederationPlatforms.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCaseFederationPlatforms.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacyCaseFederationPlatforms.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.createManual`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.createSimulated`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.deleteSimulated`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.exportJson`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacyCases.getSimulated`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.importJson`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.ingest`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.ingestAlertTestCase`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyCases.runManualAction`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacyCases.simulate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyConfiguration.getMaximumAlertsGroupingConfiguration`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyFederatedCases.batchPatchFederatedCases`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyFederatedCases.fetchCasesToSync`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyFederatedCases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyPlaybooks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyPlaybooks.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyPlaybooks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacyPlaybooks.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyPlaybooks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacyPublisher.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Remote Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarRemoteAgent) (`roles/chronicle.soarRemoteAgent`)   
  
#### `chronicle.legacyPublisher.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Remote Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarRemoteAgent) (`roles/chronicle.soarRemoteAgent`)   
  
#### `chronicle.legacySdk.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Remote Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarRemoteAgent) (`roles/chronicle.soarRemoteAgent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacySdk.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Remote Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarRemoteAgent) (`roles/chronicle.soarRemoteAgent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.legacySearches.searchCases`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacySearches.searchEntities`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacySoarAdvancedReports.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarAdvancedReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacySoarAdvancedReports.share`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarAdvancedReports.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarAudits.legacySoarAudit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarDashboards.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarDashboards.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarDashboards.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarIdpMappingGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarIdpMappingGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarIdpMappingGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarPermissionGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarReports.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacySoarReports.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarUsers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySoarUsers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)   
  
#### `chronicle.legacySystem.getLicenseStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySystem.getMaximumDataRetentionValue`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySystem.getSystemVersion`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.legacySystemMetadata.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.legacySystemMetadata.placeholders`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.logProcessingPipelines.associateStreams`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logProcessingPipelines.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logProcessingPipelines.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logProcessingPipelines.dissociateStreams`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logProcessingPipelines.fetchAssociatedPipeline`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.logProcessingPipelines.fetchSampleLogsByStreams`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.logProcessingPipelines.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.logProcessingPipelines.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.logProcessingPipelines.testPipeline`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.logProcessingPipelines.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logTypeSchemas.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.logTypeSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logTypeSettings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.logTypeSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logTypes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.logTypes.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logTypes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.logs.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)   
  
#### `chronicle.logs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.logs.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.logs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.managedDomainSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.managedDomainSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.managerRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.managerRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.managerRevisions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.managers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.managers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.managers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.mappingRules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.mappingRules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.mappingRules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.marketplaceIntegrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.marketplaceIntegrations.install`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.marketplaceIntegrations.uninstall`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.messages.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.messages.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.messages.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.messages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.messages.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.moduleSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.moduleSettings.modifyCaseList`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.moduleSettings.rebranding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.moduleSettingsProperties.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.moduleSettingsProperties.testSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.moduleSettingsProperties.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.multitenantDirectories.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.nativeDashboards.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.nativeDashboards.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.nativeDashboards.duplicate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.nativeDashboards.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.nativeDashboards.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.nativeDashboards.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.notebooks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.notebooks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.notificationSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.notificationSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.ontologyRecords.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.ontologyRecords.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.operations.streamSearch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.operations.wait`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.parserExtensions.activate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parserExtensions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parserExtensions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parserExtensions.generateKeyValueMappings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parserExtensions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parserExtensions.legacySubmitParserExtension`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parserExtensions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.parserExtensions.removeSyslog`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.activate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.activateReleaseCandidate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.copyPrebuiltParser`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.deactivate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.generateEventTypesSuggestions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.parsers.runParser`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.parsingErrors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.preferenceSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)   
  
#### `chronicle.preferenceSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.propertySchemaDefinitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.propertySchemaDefinitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.propertySchemaDefinitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.queries.suggestSql`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.queryMetrics.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.queryMetrics.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.referenceLists.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.referenceLists.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.referenceLists.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.referenceLists.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.referenceLists.verifyReferenceList`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.remoteAgents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.remoteAgents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.remoteAgents.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.requestTemplates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.requestTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.requestTemplates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.retrohunts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.retrohunts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.retrohunts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.riskConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.riskConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.ruleDeployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.ruleDeployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.ruleDeployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.ruleExecutionErrors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.rules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.rules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.rules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
#### `chronicle.rules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.rules.listRevisions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.rules.modifyRules`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.rules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.rules.verifyRuleText`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.savedColumnSets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)   
  
#### `chronicle.savedColumnSets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)   
  
#### `chronicle.savedColumnSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.savedColumnSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.savedColumnSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)   
  
#### `chronicle.searchQueries.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)   
  
#### `chronicle.searchQueries.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)   
  
#### `chronicle.searchQueries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.searchQueries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.searchQueries.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)   
  
#### `chronicle.searchSessions.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.searchedResults.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.shareConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.shareConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.sharedPreferenceSets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.sharedPreferenceSets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.sharedPreferenceSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.sharedPreferenceSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.sharedPreferenceSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.slaDefinitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.slaDefinitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.slaDefinitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.soarDomains.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.soarDomains.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.soarDomains.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.soarNetworks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.soarNetworks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.soarNetworks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.socRoles.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.socRoles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)   
  
#### `chronicle.socRoles.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.summaryTables.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.summaryTables.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.summaryTables.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.summaryTables.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.summaryTables.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.systemNotifications.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.systemNotifications.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.tagSubscriptions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.tagSubscriptions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.tagSubscriptions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.tagSubscriptions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.tagSubscriptions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.tags.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.tags.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.tags.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.tags.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.tags.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.tasks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.tasks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.tasks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.tenants.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.tenants.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.tenants.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.threatCollectionFilterSet.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.threatCollections.fetchEntityMetadata`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.threatCollections.fetchIocMatchMetadata`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.threatCollections.fetchRelated`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.threatCollections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.threatCollections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer) (`roles/chronicle.limitedViewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.transformerDefinitions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.transformerDefinitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.transformerDefinitions.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.transformerDefinitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.transformerDefinitions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.transformerDefinitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.transformerRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.transformerRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.transformerRevisions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.uniqueEntities.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.uniqueEntities.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.userLocalizations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.userLocalizations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.userNotifications.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.userNotifications.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.validationErrors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `chronicle.validationReports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)   
  
#### `chronicle.views.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.views.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.visualFamilies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.visualFamilies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.visualFamilies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.watchlists.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.watchlists.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.watchlists.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.watchlists.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) (`roles/chronicle.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.watchlists.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)   
  
#### `chronicle.webhooks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.webhooks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.webhooks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.workdeskContacts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.workdeskContacts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.workdeskContacts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.workdeskLinks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.workdeskLinks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.workdeskLinks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.workdeskNotes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
#### `chronicle.workdeskNotes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chronicle.workdeskNotes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor) (`roles/chronicle.editor`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
