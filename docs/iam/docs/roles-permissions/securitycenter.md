---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter/
title: Security Command Center roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:00.515184+00:00
---

# Security Command Center roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Security Command Center roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Security Command Center. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Security Command Center roles

Role | Permissions  
---|---  
  
#### Security Center Admin 

(`roles/securitycenter.admin`) Admin(super user) access to security center  Lowest-level resources where you can grant this role:

  * Project 

|  `aiplatform.artifacts.get` `aiplatform.artifacts.list` `aiplatform.batchPredictionJobs.get` `aiplatform.batchPredictionJobs.list` `aiplatform.customJobs.get` `aiplatform.customJobs.list` `aiplatform.datasets.get` `aiplatform.datasets.list` `aiplatform.endpoints.get` `aiplatform.endpoints.list` `aiplatform.executions.get` `aiplatform.executions.list` `aiplatform.models.get` `aiplatform.models.list` `aiplatform.tuningJobs.get` `aiplatform.tuningJobs.list` `appengine.applications.get` `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.create` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `assuredoss.*`

  * `assuredoss.config.get`
  * `assuredoss.customers.create`
  * `assuredoss.locations.get`
  * `assuredoss.locations.list`
  * `assuredoss.metadata.get`
  * `assuredoss.metadata.list`
  * `assuredoss.operations.cancel`
  * `assuredoss.operations.delete`
  * `assuredoss.operations.get`
  * `assuredoss.operations.list`

`auditmanager.auditReports.*`

  * `auditmanager.auditReports.generate`
  * `auditmanager.auditReports.get`
  * `auditmanager.auditReports.list`

`auditmanager.auditSchedules.*`

  * `auditmanager.auditSchedules.create`
  * `auditmanager.auditSchedules.get`
  * `auditmanager.auditSchedules.list`
  * `auditmanager.auditSchedules.update`

`auditmanager.auditScopeReports.generate` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

  * `auditmanager.controlReports.get`
  * `auditmanager.controlReports.list`

`auditmanager.controls.list` `auditmanager.findings.list` `auditmanager.locations.*`

  * `auditmanager.locations.enrollResource`
  * `auditmanager.locations.get`
  * `auditmanager.locations.list`

`auditmanager.operations.*`

  * `auditmanager.operations.get`
  * `auditmanager.operations.list`

`auditmanager.resourceEnrollmentStatuses.*`

  * `auditmanager.resourceEnrollmentStatuses.get`
  * `auditmanager.resourceEnrollmentStatuses.list`

`cloudasset.assets.exportAiplatformBatchPredictionJobs` `cloudasset.assets.exportAiplatformCustomJobs` `cloudasset.assets.exportAiplatformDataLabelingJobs` `cloudasset.assets.exportAiplatformDatasets` `cloudasset.assets.exportAiplatformEndpoints` `cloudasset.assets.exportAiplatformHyperparameterTuningJobs` `cloudasset.assets.exportAiplatformMetadataStores` `cloudasset.assets.exportAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.exportAiplatformModels` `cloudasset.assets.exportAiplatformPipelineJobs` `cloudasset.assets.exportAiplatformSpecialistPools` `cloudasset.assets.exportAiplatformTrainingPipelines` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportResource` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.assets.searchEnrichmentResourceOwners` `cloudasset.othercloudconnections.get` `cloudasset.othercloudconnections.list` `cloudasset.othercloudconnections.verify` `cloudnotifications.activities.list` `cloudsecuritycompliance.*`

  * `cloudsecuritycompliance.auditReports.generate`
  * `cloudsecuritycompliance.auditReports.get`
  * `cloudsecuritycompliance.auditReports.list`
  * `cloudsecuritycompliance.auditScopeReports.generate`
  * `cloudsecuritycompliance.billingSettings.get`
  * `cloudsecuritycompliance.cloudControlDeployments.create`
  * `cloudsecuritycompliance.cloudControlDeployments.delete`
  * `cloudsecuritycompliance.cloudControlDeployments.get`
  * `cloudsecuritycompliance.cloudControlDeployments.list`
  * `cloudsecuritycompliance.cloudControlDeployments.update`
  * `cloudsecuritycompliance.cloudControlPredictions.create`
  * `cloudsecuritycompliance.cloudControlPredictions.get`
  * `cloudsecuritycompliance.cloudControlPredictions.list`
  * `cloudsecuritycompliance.cloudControls.create`
  * `cloudsecuritycompliance.cloudControls.delete`
  * `cloudsecuritycompliance.cloudControls.get`
  * `cloudsecuritycompliance.cloudControls.list`
  * `cloudsecuritycompliance.cloudControls.update`
  * `cloudsecuritycompliance.cmEnrollments.get`
  * `cloudsecuritycompliance.cmEnrollments.update`
  * `cloudsecuritycompliance.controlComplianceSummaries.list`
  * `cloudsecuritycompliance.controlReports.get`
  * `cloudsecuritycompliance.controls.get`
  * `cloudsecuritycompliance.controls.list`
  * `cloudsecuritycompliance.findingSummaries.list`
  * `cloudsecuritycompliance.findings.list`
  * `cloudsecuritycompliance.frameworkAudits.create`
  * `cloudsecuritycompliance.frameworkAudits.get`
  * `cloudsecuritycompliance.frameworkAudits.list`
  * `cloudsecuritycompliance.frameworkComplianceReports.aggregate`
  * `cloudsecuritycompliance.frameworkComplianceReports.get`
  * `cloudsecuritycompliance.frameworkComplianceSummaries.list`
  * `cloudsecuritycompliance.frameworkDeployments.create`
  * `cloudsecuritycompliance.frameworkDeployments.delete`
  * `cloudsecuritycompliance.frameworkDeployments.get`
  * `cloudsecuritycompliance.frameworkDeployments.list`
  * `cloudsecuritycompliance.frameworkDeployments.update`
  * `cloudsecuritycompliance.frameworks.create`
  * `cloudsecuritycompliance.frameworks.delete`
  * `cloudsecuritycompliance.frameworks.get`
  * `cloudsecuritycompliance.frameworks.list`
  * `cloudsecuritycompliance.frameworks.update`
  * `cloudsecuritycompliance.locations.enrollResource`
  * `cloudsecuritycompliance.locations.get`
  * `cloudsecuritycompliance.locations.list`
  * `cloudsecuritycompliance.operations.cancel`
  * `cloudsecuritycompliance.operations.delete`
  * `cloudsecuritycompliance.operations.get`
  * `cloudsecuritycompliance.operations.list`
  * `cloudsecuritycompliance.resourceEnrollmentStatuses.get`
  * `cloudsecuritycompliance.resourceEnrollmentStatuses.list`

`cloudsecurityscanner.*`

  * `cloudsecurityscanner.crawledurls.list`
  * `cloudsecurityscanner.results.get`
  * `cloudsecurityscanner.results.list`
  * `cloudsecurityscanner.scanruns.get`
  * `cloudsecurityscanner.scanruns.getSummary`
  * `cloudsecurityscanner.scanruns.list`
  * `cloudsecurityscanner.scanruns.stop`
  * `cloudsecurityscanner.scans.create`
  * `cloudsecurityscanner.scans.delete`
  * `cloudsecurityscanner.scans.get`
  * `cloudsecurityscanner.scans.list`
  * `cloudsecurityscanner.scans.run`
  * `cloudsecurityscanner.scans.update`

`compute.addresses.list` `dlp.*`

  * `dlp.analyzeRiskTemplates.create`
  * `dlp.analyzeRiskTemplates.delete`
  * `dlp.analyzeRiskTemplates.get`
  * `dlp.analyzeRiskTemplates.list`
  * `dlp.analyzeRiskTemplates.update`
  * `dlp.charts.get`
  * `dlp.columnDataProfiles.get`
  * `dlp.columnDataProfiles.list`
  * `dlp.connections.create`
  * `dlp.connections.delete`
  * `dlp.connections.get`
  * `dlp.connections.list`
  * `dlp.connections.search`
  * `dlp.connections.update`
  * `dlp.contentPolicies.apply`
  * `dlp.contentPolicies.create`
  * `dlp.contentPolicies.delete`
  * `dlp.contentPolicies.get`
  * `dlp.contentPolicies.list`
  * `dlp.contentPolicies.update`
  * `dlp.deidentifyTemplates.create`
  * `dlp.deidentifyTemplates.delete`
  * `dlp.deidentifyTemplates.get`
  * `dlp.deidentifyTemplates.list`
  * `dlp.deidentifyTemplates.update`
  * `dlp.estimates.cancel`
  * `dlp.estimates.create`
  * `dlp.estimates.delete`
  * `dlp.estimates.get`
  * `dlp.estimates.list`
  * `dlp.fileStoreProfiles.delete`
  * `dlp.fileStoreProfiles.get`
  * `dlp.fileStoreProfiles.list`
  * `dlp.inspectFindings.list`
  * `dlp.inspectTemplates.create`
  * `dlp.inspectTemplates.delete`
  * `dlp.inspectTemplates.get`
  * `dlp.inspectTemplates.list`
  * `dlp.inspectTemplates.update`
  * `dlp.jobTriggers.create`
  * `dlp.jobTriggers.delete`
  * `dlp.jobTriggers.get`
  * `dlp.jobTriggers.hybridInspect`
  * `dlp.jobTriggers.list`
  * `dlp.jobTriggers.update`
  * `dlp.jobs.cancel`
  * `dlp.jobs.create`
  * `dlp.jobs.delete`
  * `dlp.jobs.get`
  * `dlp.jobs.hybridInspect`
  * `dlp.jobs.list`
  * `dlp.kms.encrypt`
  * `dlp.locations.get`
  * `dlp.locations.list`
  * `dlp.projectDataProfiles.get`
  * `dlp.projectDataProfiles.list`
  * `dlp.storedInfoTypes.create`
  * `dlp.storedInfoTypes.delete`
  * `dlp.storedInfoTypes.get`
  * `dlp.storedInfoTypes.list`
  * `dlp.storedInfoTypes.update`
  * `dlp.subscriptions.cancel`
  * `dlp.subscriptions.create`
  * `dlp.subscriptions.get`
  * `dlp.subscriptions.list`
  * `dlp.subscriptions.update`
  * `dlp.tableDataProfiles.delete`
  * `dlp.tableDataProfiles.get`
  * `dlp.tableDataProfiles.list`

`dspm.*`

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

`externalexposure.scanMetrics.get` `iam.serviceAccountKeys.create` `iam.serviceAccounts.create` `iam.serviceAccounts.get` `modelarmor.*`

  * `modelarmor.callouts.invoke`
  * `modelarmor.floorSettings.computeEffectiveFloorSetting`
  * `modelarmor.floorSettings.get`
  * `modelarmor.floorSettings.update`
  * `modelarmor.locations.get`
  * `modelarmor.locations.list`
  * `modelarmor.templates.create`
  * `modelarmor.templates.delete`
  * `modelarmor.templates.get`
  * `modelarmor.templates.list`
  * `modelarmor.templates.update`
  * `modelarmor.templates.useToSanitizeInput`
  * `modelarmor.templates.useToSanitizeModelResponse`
  * `modelarmor.templates.useToSanitizeOutput`
  * `modelarmor.templates.useToSanitizeUserPrompt`
  * `modelarmor.templates.useToStreamSanitizeModelResponse`
  * `modelarmor.templates.useToStreamSanitizeUserPrompt`

`monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.list` `monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `opsconfigmonitoring.resourceMetadata.list` `pubsub.messageTransforms.validate` `pubsub.schemas.get` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.validate` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.subscriptions.create` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.update` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `resourcemanager.tagValues.get` `securitycenter.*`

  * `securitycenter.assets.group`
  * `securitycenter.assets.list`
  * `securitycenter.assets.listAssetPropertyNames`
  * `securitycenter.assets.runDiscovery`
  * `securitycenter.assetsecuritymarks.update`
  * `securitycenter.attackpaths.list`
  * `securitycenter.bigQueryExports.create`
  * `securitycenter.bigQueryExports.delete`
  * `securitycenter.bigQueryExports.get`
  * `securitycenter.bigQueryExports.list`
  * `securitycenter.bigQueryExports.update`
  * `securitycenter.billingtier.update`
  * `securitycenter.complianceReports.aggregate`
  * `securitycenter.compliancesnapshots.list`
  * `securitycenter.containerthreatdetectionsettings.calculate`
  * `securitycenter.containerthreatdetectionsettings.get`
  * `securitycenter.containerthreatdetectionsettings.update`
  * `securitycenter.effectivesecurityhealthanalyticscustommodules.get`
  * `securitycenter.effectivesecurityhealthanalyticscustommodules.list`
  * `securitycenter.eventthreatdetectionsettings.calculate`
  * `securitycenter.eventthreatdetectionsettings.get`
  * `securitycenter.eventthreatdetectionsettings.update`
  * `securitycenter.exposurepathexplan.get`
  * `securitycenter.findingexplanations.get`
  * `securitycenter.findingexternalsystems.update`
  * `securitycenter.findings.bulkMuteUpdate`
  * `securitycenter.findings.export`
  * `securitycenter.findings.group`
  * `securitycenter.findings.list`
  * `securitycenter.findings.listFindingPropertyNames`
  * `securitycenter.findings.setMute`
  * `securitycenter.findings.setState`
  * `securitycenter.findings.setWorkflowState`
  * `securitycenter.findings.update`
  * `securitycenter.findingsecuritymarks.update`
  * `securitycenter.graphs.get`
  * `securitycenter.graphs.query`
  * `securitycenter.integratedvulnerabilityscannersettings.calculate`
  * `securitycenter.integratedvulnerabilityscannersettings.get`
  * `securitycenter.integratedvulnerabilityscannersettings.update`
  * `securitycenter.issues.get`
  * `securitycenter.issues.group`
  * `securitycenter.issues.list`
  * `securitycenter.issues.listFilterValues`
  * `securitycenter.issues.mute`
  * `securitycenter.issues.retrieve`
  * `securitycenter.issues.search`
  * `securitycenter.issues.searchImpactedResources`
  * `securitycenter.muteconfigs.create`
  * `securitycenter.muteconfigs.delete`
  * `securitycenter.muteconfigs.get`
  * `securitycenter.muteconfigs.list`
  * `securitycenter.muteconfigs.update`
  * `securitycenter.notificationconfig.create`
  * `securitycenter.notificationconfig.delete`
  * `securitycenter.notificationconfig.get`
  * `securitycenter.notificationconfig.list`
  * `securitycenter.notificationconfig.update`
  * `securitycenter.organizationsettings.get`
  * `securitycenter.organizationsettings.update`
  * `securitycenter.rapidvulnerabilitydetectionsettings.calculate`
  * `securitycenter.rapidvulnerabilitydetectionsettings.get`
  * `securitycenter.rapidvulnerabilitydetectionsettings.update`
  * `securitycenter.resourcevalueconfigs.create`
  * `securitycenter.resourcevalueconfigs.delete`
  * `securitycenter.resourcevalueconfigs.get`
  * `securitycenter.resourcevalueconfigs.list`
  * `securitycenter.resourcevalueconfigs.update`
  * `securitycenter.riskreports.get`
  * `securitycenter.riskreports.list`
  * `securitycenter.securitycentersettings.get`
  * `securitycenter.securitycentersettings.update`
  * `securitycenter.securityhealthanalyticscustommodules.create`
  * `securitycenter.securityhealthanalyticscustommodules.delete`
  * `securitycenter.securityhealthanalyticscustommodules.get`
  * `securitycenter.securityhealthanalyticscustommodules.list`
  * `securitycenter.securityhealthanalyticscustommodules.simulate`
  * `securitycenter.securityhealthanalyticscustommodules.test`
  * `securitycenter.securityhealthanalyticscustommodules.update`
  * `securitycenter.securityhealthanalyticssettings.calculate`
  * `securitycenter.securityhealthanalyticssettings.get`
  * `securitycenter.securityhealthanalyticssettings.update`
  * `securitycenter.simulations.get`
  * `securitycenter.sources.get`
  * `securitycenter.sources.getIamPolicy`
  * `securitycenter.sources.list`
  * `securitycenter.sources.setIamPolicy`
  * `securitycenter.sources.update`
  * `securitycenter.subscription.get`
  * `securitycenter.userinterfacemetadata.get`
  * `securitycenter.valuedresources.list`
  * `securitycenter.virtualmachinethreatdetectionsettings.calculate`
  * `securitycenter.virtualmachinethreatdetectionsettings.get`
  * `securitycenter.virtualmachinethreatdetectionsettings.update`
  * `securitycenter.vulnerabilitysnapshots.list`
  * `securitycenter.websecurityscannersettings.calculate`
  * `securitycenter.websecurityscannersettings.get`
  * `securitycenter.websecurityscannersettings.update`

`securitycentermanagement.*`

  * `securitycentermanagement.billingMetadata.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.create`
  * `securitycentermanagement.eventThreatDetectionCustomModules.delete`
  * `securitycentermanagement.eventThreatDetectionCustomModules.get`
  * `securitycentermanagement.eventThreatDetectionCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.update`
  * `securitycentermanagement.eventThreatDetectionCustomModules.validate`
  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`
  * `securitycentermanagement.operations.cancel`
  * `securitycentermanagement.operations.delete`
  * `securitycentermanagement.operations.get`
  * `securitycentermanagement.operations.list`
  * `securitycentermanagement.securityCenter.get`
  * `securitycentermanagement.securityCenter.migrate`
  * `securitycentermanagement.securityCenter.update`
  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`
  * `securitycentermanagement.securityCommandCenter.activate`
  * `securitycentermanagement.securityCommandCenter.checkActivationOperation`
  * `securitycentermanagement.securityCommandCenter.checkEligibility`
  * `securitycentermanagement.securityCommandCenter.checkOnboardingStatus`
  * `securitycentermanagement.securityCommandCenter.generateServiceAccounts`
  * `securitycentermanagement.securityCommandCenter.get`
  * `securitycentermanagement.securityCommandCenter.update`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.create`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.delete`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.test`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.update`

`securityposture.locations.*`

  * `securityposture.locations.get`
  * `securityposture.locations.list`

`securityposture.operations.get` `securityposture.operations.list` `securityposture.postureDeployments.get` `securityposture.postureDeployments.list` `securityposture.postureTemplates.*`

  * `securityposture.postureTemplates.get`
  * `securityposture.postureTemplates.list`

`securityposture.postures.get` `securityposture.postures.list` `securityposture.reports.get` `securityposture.reports.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list`  
  
#### Security Center Admin Editor 

(`roles/securitycenter.adminEditor`) Admin Read-write access to security center  Lowest-level resources where you can grant this role:

  * Project 

|  `aiplatform.artifacts.get` `aiplatform.artifacts.list` `aiplatform.batchPredictionJobs.get` `aiplatform.batchPredictionJobs.list` `aiplatform.customJobs.get` `aiplatform.customJobs.list` `aiplatform.datasets.get` `aiplatform.datasets.list` `aiplatform.endpoints.get` `aiplatform.endpoints.list` `aiplatform.executions.get` `aiplatform.executions.list` `aiplatform.models.get` `aiplatform.models.list` `aiplatform.tuningJobs.get` `aiplatform.tuningJobs.list` `appengine.applications.get` `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `assuredoss.config.get` `assuredoss.locations.*`

  * `assuredoss.locations.get`
  * `assuredoss.locations.list`

`assuredoss.metadata.*`

  * `assuredoss.metadata.get`
  * `assuredoss.metadata.list`

`assuredoss.operations.get` `assuredoss.operations.list` `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

  * `auditmanager.controlReports.get`
  * `auditmanager.controlReports.list`

`auditmanager.controls.list` `auditmanager.findings.list` `auditmanager.locations.get` `auditmanager.locations.list` `auditmanager.operations.*`

  * `auditmanager.operations.get`
  * `auditmanager.operations.list`

`auditmanager.resourceEnrollmentStatuses.*`

  * `auditmanager.resourceEnrollmentStatuses.get`
  * `auditmanager.resourceEnrollmentStatuses.list`

`cloudasset.assets.exportAiplatformBatchPredictionJobs` `cloudasset.assets.exportAiplatformCustomJobs` `cloudasset.assets.exportAiplatformDataLabelingJobs` `cloudasset.assets.exportAiplatformDatasets` `cloudasset.assets.exportAiplatformEndpoints` `cloudasset.assets.exportAiplatformHyperparameterTuningJobs` `cloudasset.assets.exportAiplatformMetadataStores` `cloudasset.assets.exportAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.exportAiplatformModels` `cloudasset.assets.exportAiplatformPipelineJobs` `cloudasset.assets.exportAiplatformSpecialistPools` `cloudasset.assets.exportAiplatformTrainingPipelines` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportResource` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.assets.searchEnrichmentResourceOwners` `cloudasset.othercloudconnections.get` `cloudasset.othercloudconnections.list` `cloudasset.othercloudconnections.verify` `cloudnotifications.activities.list` `cloudsecuritycompliance.auditReports.get` `cloudsecuritycompliance.auditReports.list` `cloudsecuritycompliance.billingSettings.get` `cloudsecuritycompliance.cloudControlDeployments.get` `cloudsecuritycompliance.cloudControlDeployments.list` `cloudsecuritycompliance.cloudControlPredictions.get` `cloudsecuritycompliance.cloudControlPredictions.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.cmEnrollments.get` `cloudsecuritycompliance.controlComplianceSummaries.list` `cloudsecuritycompliance.controlReports.get` `cloudsecuritycompliance.controls.*`

  * `cloudsecuritycompliance.controls.get`
  * `cloudsecuritycompliance.controls.list`

`cloudsecuritycompliance.findingSummaries.list` `cloudsecuritycompliance.findings.list` `cloudsecuritycompliance.frameworkAudits.get` `cloudsecuritycompliance.frameworkAudits.list` `cloudsecuritycompliance.frameworkComplianceReports.*`

  * `cloudsecuritycompliance.frameworkComplianceReports.aggregate`
  * `cloudsecuritycompliance.frameworkComplianceReports.get`

`cloudsecuritycompliance.frameworkComplianceSummaries.list` `cloudsecuritycompliance.frameworkDeployments.get` `cloudsecuritycompliance.frameworkDeployments.list` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `cloudsecuritycompliance.locations.get` `cloudsecuritycompliance.locations.list` `cloudsecuritycompliance.operations.get` `cloudsecuritycompliance.operations.list` `cloudsecuritycompliance.resourceEnrollmentStatuses.*`

  * `cloudsecuritycompliance.resourceEnrollmentStatuses.get`
  * `cloudsecuritycompliance.resourceEnrollmentStatuses.list`

`cloudsecurityscanner.*`

  * `cloudsecurityscanner.crawledurls.list`
  * `cloudsecurityscanner.results.get`
  * `cloudsecurityscanner.results.list`
  * `cloudsecurityscanner.scanruns.get`
  * `cloudsecurityscanner.scanruns.getSummary`
  * `cloudsecurityscanner.scanruns.list`
  * `cloudsecurityscanner.scanruns.stop`
  * `cloudsecurityscanner.scans.create`
  * `cloudsecurityscanner.scans.delete`
  * `cloudsecurityscanner.scans.get`
  * `cloudsecurityscanner.scans.list`
  * `cloudsecurityscanner.scans.run`
  * `cloudsecurityscanner.scans.update`

`compute.addresses.list` `dlp.charts.get` `dlp.columnDataProfiles.*`

  * `dlp.columnDataProfiles.get`
  * `dlp.columnDataProfiles.list`

`dlp.fileStoreProfiles.get` `dlp.fileStoreProfiles.list` `dlp.projectDataProfiles.*`

  * `dlp.projectDataProfiles.get`
  * `dlp.projectDataProfiles.list`

`dlp.tableDataProfiles.get` `dlp.tableDataProfiles.list` `dspm.locations.*`

  * `dspm.locations.computeAggregation`
  * `dspm.locations.fetchDataGovernanceAnalytics`
  * `dspm.locations.fetchDspmGovernedProjects`
  * `dspm.locations.fetchGovernedResourceMetrics`
  * `dspm.locations.fetchLineageConnections`
  * `dspm.locations.get`
  * `dspm.locations.list`

`dspm.operations.get` `dspm.operations.list` `externalexposure.scanMetrics.get` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.list` `monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `opsconfigmonitoring.resourceMetadata.list` `pubsub.messageTransforms.validate` `pubsub.schemas.get` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.validate` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `resourcemanager.tagValues.get` `securitycenter.assets.*`

  * `securitycenter.assets.group`
  * `securitycenter.assets.list`
  * `securitycenter.assets.listAssetPropertyNames`
  * `securitycenter.assets.runDiscovery`

`securitycenter.assetsecuritymarks.update` `securitycenter.attackpaths.list` `securitycenter.bigQueryExports.*`

  * `securitycenter.bigQueryExports.create`
  * `securitycenter.bigQueryExports.delete`
  * `securitycenter.bigQueryExports.get`
  * `securitycenter.bigQueryExports.list`
  * `securitycenter.bigQueryExports.update`

`securitycenter.complianceReports.aggregate` `securitycenter.compliancesnapshots.list` `securitycenter.containerthreatdetectionsettings.calculate` `securitycenter.containerthreatdetectionsettings.get` `securitycenter.effectivesecurityhealthanalyticscustommodules.*`

  * `securitycenter.effectivesecurityhealthanalyticscustommodules.get`
  * `securitycenter.effectivesecurityhealthanalyticscustommodules.list`

`securitycenter.eventthreatdetectionsettings.calculate` `securitycenter.eventthreatdetectionsettings.get` `securitycenter.exposurepathexplan.get` `securitycenter.findingexplanations.get` `securitycenter.findingexternalsystems.update` `securitycenter.findings.*`

  * `securitycenter.findings.bulkMuteUpdate`
  * `securitycenter.findings.export`
  * `securitycenter.findings.group`
  * `securitycenter.findings.list`
  * `securitycenter.findings.listFindingPropertyNames`
  * `securitycenter.findings.setMute`
  * `securitycenter.findings.setState`
  * `securitycenter.findings.setWorkflowState`
  * `securitycenter.findings.update`

`securitycenter.findingsecuritymarks.update` `securitycenter.graphs.*`

  * `securitycenter.graphs.get`
  * `securitycenter.graphs.query`

`securitycenter.integratedvulnerabilityscannersettings.calculate` `securitycenter.integratedvulnerabilityscannersettings.get` `securitycenter.issues.*`

  * `securitycenter.issues.get`
  * `securitycenter.issues.group`
  * `securitycenter.issues.list`
  * `securitycenter.issues.listFilterValues`
  * `securitycenter.issues.mute`
  * `securitycenter.issues.retrieve`
  * `securitycenter.issues.search`
  * `securitycenter.issues.searchImpactedResources`

`securitycenter.muteconfigs.*`

  * `securitycenter.muteconfigs.create`
  * `securitycenter.muteconfigs.delete`
  * `securitycenter.muteconfigs.get`
  * `securitycenter.muteconfigs.list`
  * `securitycenter.muteconfigs.update`

`securitycenter.notificationconfig.*`

  * `securitycenter.notificationconfig.create`
  * `securitycenter.notificationconfig.delete`
  * `securitycenter.notificationconfig.get`
  * `securitycenter.notificationconfig.list`
  * `securitycenter.notificationconfig.update`

`securitycenter.organizationsettings.get` `securitycenter.rapidvulnerabilitydetectionsettings.calculate` `securitycenter.rapidvulnerabilitydetectionsettings.get` `securitycenter.resourcevalueconfigs.*`

  * `securitycenter.resourcevalueconfigs.create`
  * `securitycenter.resourcevalueconfigs.delete`
  * `securitycenter.resourcevalueconfigs.get`
  * `securitycenter.resourcevalueconfigs.list`
  * `securitycenter.resourcevalueconfigs.update`

`securitycenter.securitycentersettings.get` `securitycenter.securityhealthanalyticscustommodules.get` `securitycenter.securityhealthanalyticscustommodules.list` `securitycenter.securityhealthanalyticscustommodules.simulate` `securitycenter.securityhealthanalyticscustommodules.test` `securitycenter.securityhealthanalyticssettings.calculate` `securitycenter.securityhealthanalyticssettings.get` `securitycenter.simulations.get` `securitycenter.sources.get` `securitycenter.sources.list` `securitycenter.sources.update` `securitycenter.subscription.get` `securitycenter.userinterfacemetadata.get` `securitycenter.valuedresources.list` `securitycenter.virtualmachinethreatdetectionsettings.calculate` `securitycenter.virtualmachinethreatdetectionsettings.get` `securitycenter.vulnerabilitysnapshots.list` `securitycenter.websecurityscannersettings.calculate` `securitycenter.websecurityscannersettings.get` `securitycentermanagement.billingMetadata.get` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.get` `securitycentermanagement.eventThreatDetectionCustomModules.list` `securitycentermanagement.eventThreatDetectionCustomModules.validate` `securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.operations.get` `securitycentermanagement.operations.list` `securitycentermanagement.securityCenter.get` `securitycentermanagement.securityCenterServices.get` `securitycentermanagement.securityCenterServices.list` `securitycentermanagement.securityCommandCenter.checkActivationOperation` `securitycentermanagement.securityCommandCenter.checkEligibility` `securitycentermanagement.securityCommandCenter.checkOnboardingStatus` `securitycentermanagement.securityCommandCenter.generateServiceAccounts` `securitycentermanagement.securityCommandCenter.get` `securitycentermanagement.securityCommandCenter.update` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.test` `securityposture.locations.*`

  * `securityposture.locations.get`
  * `securityposture.locations.list`

`securityposture.operations.get` `securityposture.operations.list` `securityposture.postureDeployments.get` `securityposture.postureDeployments.list` `securityposture.postureTemplates.*`

  * `securityposture.postureTemplates.get`
  * `securityposture.postureTemplates.list`

`securityposture.postures.get` `securityposture.postures.list` `securityposture.reports.get` `securityposture.reports.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list`  
  
#### Security Center Admin Viewer 

(`roles/securitycenter.adminViewer`) Admin Read access to security center  Lowest-level resources where you can grant this role:

  * Project 

|  `aiplatform.artifacts.get` `aiplatform.artifacts.list` `aiplatform.batchPredictionJobs.get` `aiplatform.batchPredictionJobs.list` `aiplatform.customJobs.get` `aiplatform.customJobs.list` `aiplatform.datasets.get` `aiplatform.datasets.list` `aiplatform.endpoints.get` `aiplatform.endpoints.list` `aiplatform.executions.get` `aiplatform.executions.list` `aiplatform.models.get` `aiplatform.models.list` `aiplatform.tuningJobs.get` `aiplatform.tuningJobs.list` `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `assuredoss.config.get` `assuredoss.locations.*`

  * `assuredoss.locations.get`
  * `assuredoss.locations.list`

`assuredoss.metadata.*`

  * `assuredoss.metadata.get`
  * `assuredoss.metadata.list`

`assuredoss.operations.get` `assuredoss.operations.list` `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

  * `auditmanager.controlReports.get`
  * `auditmanager.controlReports.list`

`auditmanager.controls.list` `auditmanager.findings.list` `auditmanager.locations.get` `auditmanager.locations.list` `auditmanager.operations.*`

  * `auditmanager.operations.get`
  * `auditmanager.operations.list`

`auditmanager.resourceEnrollmentStatuses.*`

  * `auditmanager.resourceEnrollmentStatuses.get`
  * `auditmanager.resourceEnrollmentStatuses.list`

`cloudasset.assets.exportAiplatformBatchPredictionJobs` `cloudasset.assets.exportAiplatformCustomJobs` `cloudasset.assets.exportAiplatformDataLabelingJobs` `cloudasset.assets.exportAiplatformDatasets` `cloudasset.assets.exportAiplatformEndpoints` `cloudasset.assets.exportAiplatformHyperparameterTuningJobs` `cloudasset.assets.exportAiplatformMetadataStores` `cloudasset.assets.exportAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.exportAiplatformModels` `cloudasset.assets.exportAiplatformPipelineJobs` `cloudasset.assets.exportAiplatformSpecialistPools` `cloudasset.assets.exportAiplatformTrainingPipelines` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportResource` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.assets.searchEnrichmentResourceOwners` `cloudasset.othercloudconnections.get` `cloudasset.othercloudconnections.list` `cloudasset.othercloudconnections.verify` `cloudnotifications.activities.list` `cloudsecuritycompliance.auditReports.get` `cloudsecuritycompliance.auditReports.list` `cloudsecuritycompliance.billingSettings.get` `cloudsecuritycompliance.cloudControlDeployments.get` `cloudsecuritycompliance.cloudControlDeployments.list` `cloudsecuritycompliance.cloudControlPredictions.get` `cloudsecuritycompliance.cloudControlPredictions.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.cmEnrollments.get` `cloudsecuritycompliance.controlComplianceSummaries.list` `cloudsecuritycompliance.controlReports.get` `cloudsecuritycompliance.controls.*`

  * `cloudsecuritycompliance.controls.get`
  * `cloudsecuritycompliance.controls.list`

`cloudsecuritycompliance.findingSummaries.list` `cloudsecuritycompliance.findings.list` `cloudsecuritycompliance.frameworkAudits.get` `cloudsecuritycompliance.frameworkAudits.list` `cloudsecuritycompliance.frameworkComplianceReports.*`

  * `cloudsecuritycompliance.frameworkComplianceReports.aggregate`
  * `cloudsecuritycompliance.frameworkComplianceReports.get`

`cloudsecuritycompliance.frameworkComplianceSummaries.list` `cloudsecuritycompliance.frameworkDeployments.get` `cloudsecuritycompliance.frameworkDeployments.list` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `cloudsecuritycompliance.locations.get` `cloudsecuritycompliance.locations.list` `cloudsecuritycompliance.operations.get` `cloudsecuritycompliance.operations.list` `cloudsecuritycompliance.resourceEnrollmentStatuses.*`

  * `cloudsecuritycompliance.resourceEnrollmentStatuses.get`
  * `cloudsecuritycompliance.resourceEnrollmentStatuses.list`

`cloudsecurityscanner.crawledurls.list` `cloudsecurityscanner.results.*`

  * `cloudsecurityscanner.results.get`
  * `cloudsecurityscanner.results.list`

`cloudsecurityscanner.scanruns.get` `cloudsecurityscanner.scanruns.getSummary` `cloudsecurityscanner.scanruns.list` `cloudsecurityscanner.scans.get` `cloudsecurityscanner.scans.list` `dlp.charts.get` `dlp.columnDataProfiles.*`

  * `dlp.columnDataProfiles.get`
  * `dlp.columnDataProfiles.list`

`dlp.fileStoreProfiles.get` `dlp.fileStoreProfiles.list` `dlp.projectDataProfiles.*`

  * `dlp.projectDataProfiles.get`
  * `dlp.projectDataProfiles.list`

`dlp.tableDataProfiles.get` `dlp.tableDataProfiles.list` `dspm.locations.*`

  * `dspm.locations.computeAggregation`
  * `dspm.locations.fetchDataGovernanceAnalytics`
  * `dspm.locations.fetchDspmGovernedProjects`
  * `dspm.locations.fetchGovernedResourceMetrics`
  * `dspm.locations.fetchLineageConnections`
  * `dspm.locations.get`
  * `dspm.locations.list`

`dspm.operations.get` `dspm.operations.list` `externalexposure.scanMetrics.get` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.list` `monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `opsconfigmonitoring.resourceMetadata.list` `pubsub.messageTransforms.validate` `pubsub.schemas.get` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.validate` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `resourcemanager.tagValues.get` `securitycenter.assets.group` `securitycenter.assets.list` `securitycenter.assets.listAssetPropertyNames` `securitycenter.attackpaths.list` `securitycenter.bigQueryExports.get` `securitycenter.bigQueryExports.list` `securitycenter.complianceReports.aggregate` `securitycenter.compliancesnapshots.list` `securitycenter.containerthreatdetectionsettings.calculate` `securitycenter.containerthreatdetectionsettings.get` `securitycenter.effectivesecurityhealthanalyticscustommodules.*`

  * `securitycenter.effectivesecurityhealthanalyticscustommodules.get`
  * `securitycenter.effectivesecurityhealthanalyticscustommodules.list`

`securitycenter.eventthreatdetectionsettings.calculate` `securitycenter.eventthreatdetectionsettings.get` `securitycenter.exposurepathexplan.get` `securitycenter.findingexplanations.get` `securitycenter.findings.group` `securitycenter.findings.list` `securitycenter.findings.listFindingPropertyNames` `securitycenter.graphs.*`

  * `securitycenter.graphs.get`
  * `securitycenter.graphs.query`

`securitycenter.integratedvulnerabilityscannersettings.calculate` `securitycenter.integratedvulnerabilityscannersettings.get` `securitycenter.issues.get` `securitycenter.issues.group` `securitycenter.issues.list` `securitycenter.issues.listFilterValues` `securitycenter.issues.retrieve` `securitycenter.issues.search` `securitycenter.issues.searchImpactedResources` `securitycenter.muteconfigs.get` `securitycenter.muteconfigs.list` `securitycenter.notificationconfig.get` `securitycenter.notificationconfig.list` `securitycenter.organizationsettings.get` `securitycenter.rapidvulnerabilitydetectionsettings.calculate` `securitycenter.rapidvulnerabilitydetectionsettings.get` `securitycenter.resourcevalueconfigs.get` `securitycenter.resourcevalueconfigs.list` `securitycenter.securitycentersettings.get` `securitycenter.securityhealthanalyticscustommodules.get` `securitycenter.securityhealthanalyticscustommodules.list` `securitycenter.securityhealthanalyticscustommodules.simulate` `securitycenter.securityhealthanalyticscustommodules.test` `securitycenter.securityhealthanalyticssettings.calculate` `securitycenter.securityhealthanalyticssettings.get` `securitycenter.simulations.get` `securitycenter.sources.get` `securitycenter.sources.list` `securitycenter.subscription.get` `securitycenter.userinterfacemetadata.get` `securitycenter.valuedresources.list` `securitycenter.virtualmachinethreatdetectionsettings.calculate` `securitycenter.virtualmachinethreatdetectionsettings.get` `securitycenter.vulnerabilitysnapshots.list` `securitycenter.websecurityscannersettings.calculate` `securitycenter.websecurityscannersettings.get` `securitycentermanagement.billingMetadata.get` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.get` `securitycentermanagement.eventThreatDetectionCustomModules.list` `securitycentermanagement.eventThreatDetectionCustomModules.validate` `securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.operations.get` `securitycentermanagement.operations.list` `securitycentermanagement.securityCenter.get` `securitycentermanagement.securityCenterServices.get` `securitycentermanagement.securityCenterServices.list` `securitycentermanagement.securityCommandCenter.checkActivationOperation` `securitycentermanagement.securityCommandCenter.checkEligibility` `securitycentermanagement.securityCommandCenter.checkOnboardingStatus` `securitycentermanagement.securityCommandCenter.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.test` `securityposture.locations.*`

  * `securityposture.locations.get`
  * `securityposture.locations.list`

`securityposture.operations.get` `securityposture.operations.list` `securityposture.postureDeployments.get` `securityposture.postureDeployments.list` `securityposture.postureTemplates.*`

  * `securityposture.postureTemplates.get`
  * `securityposture.postureTemplates.list`

`securityposture.postures.get` `securityposture.postures.list` `securityposture.reports.get` `securityposture.reports.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list`  
  
#### Security Center Asset Security Marks Writer 

(`roles/securitycenter.assetSecurityMarksWriter`) Write access to asset security marks  Lowest-level resources where you can grant this role:

  * Project 

|  `securitycenter.assetsecuritymarks.update` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Assets Discovery Runner 

(`roles/securitycenter.assetsDiscoveryRunner`) Run asset discovery access to assets  Lowest-level resources where you can grant this role:

  * Organization 

|  `securitycenter.assets.runDiscovery` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Assets Viewer 

(`roles/securitycenter.assetsViewer`) Read access to assets  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportResource` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.assets.searchEnrichmentResourceOwners` `cloudasset.othercloudconnections.get` `cloudasset.othercloudconnections.list` `cloudasset.othercloudconnections.verify` `resourcemanager.folders.get` `resourcemanager.organizations.get` `resourcemanager.projects.get` `securitycenter.assets.group` `securitycenter.assets.list` `securitycenter.assets.listAssetPropertyNames` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Attack Paths Reader 

(`roles/securitycenter.attackPathsViewer`) Read access to security center attack paths  |  `securitycenter.attackpaths.list` `securitycenter.exposurepathexplan.get`  
  
#### Security Center BigQuery Exports Editor 

(`roles/securitycenter.bigQueryExportsEditor`) Read-Write access to security center BigQuery Exports  |  `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.bigQueryExports.*`

  * `securitycenter.bigQueryExports.create`
  * `securitycenter.bigQueryExports.delete`
  * `securitycenter.bigQueryExports.get`
  * `securitycenter.bigQueryExports.list`
  * `securitycenter.bigQueryExports.update`

`securitycenter.findings.export`  
  
#### Security Center BigQuery Exports Viewer 

(`roles/securitycenter.bigQueryExportsViewer`) Read access to security center BigQuery Exports  |  `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.bigQueryExports.get` `securitycenter.bigQueryExports.list`  
  
#### Security Center Compliance Reports Viewer Beta

(`roles/securitycenter.complianceReportsViewer`) Read access to security center compliance reports  |  `securitycenter.complianceReports.aggregate`  
  
#### Security Center Compliance Snapshots Viewer Beta

(`roles/securitycenter.complianceSnapshotsViewer`) Read access to security center compliance snapshots  |  `securitycenter.complianceReports.aggregate` `securitycenter.compliancesnapshots.list`  
  
#### Security Center External Systems Editor 

(`roles/securitycenter.externalSystemsEditor`) Write access to security center external systems  |  `securitycenter.findingexternalsystems.update`  
  
#### Security Center Finding Security Marks Writer 

(`roles/securitycenter.findingSecurityMarksWriter`) Write access to finding security marks  Lowest-level resources where you can grant this role:

  * Project 

|  `securitycenter.findingsecuritymarks.update` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Findings Bulk Mute Editor 

(`roles/securitycenter.findingsBulkMuteEditor`) Ability to mute findings in bulk  |  `securitycenter.findings.bulkMuteUpdate`  
  
#### Security Center Findings Editor 

(`roles/securitycenter.findingsEditor`) Read-write access to findings  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.folders.get` `resourcemanager.organizations.get` `resourcemanager.projects.get` `securitycenter.complianceReports.aggregate` `securitycenter.compliancesnapshots.list` `securitycenter.findingexplanations.get` `securitycenter.findings.bulkMuteUpdate` `securitycenter.findings.group` `securitycenter.findings.list` `securitycenter.findings.listFindingPropertyNames` `securitycenter.findings.setMute` `securitycenter.findings.setState` `securitycenter.findings.update` `securitycenter.graphs.*`

  * `securitycenter.graphs.get`
  * `securitycenter.graphs.query`

`securitycenter.issues.*`

  * `securitycenter.issues.get`
  * `securitycenter.issues.group`
  * `securitycenter.issues.list`
  * `securitycenter.issues.listFilterValues`
  * `securitycenter.issues.mute`
  * `securitycenter.issues.retrieve`
  * `securitycenter.issues.search`
  * `securitycenter.issues.searchImpactedResources`

`securitycenter.sources.get` `securitycenter.sources.list` `securitycenter.userinterfacemetadata.get` `securitycenter.vulnerabilitysnapshots.list`  
  
#### Security Center Findings Mute Setter 

(`roles/securitycenter.findingsMuteSetter`) Set mute access to findings  |  `securitycenter.findings.setMute`  
  
#### Security Center Findings State Setter 

(`roles/securitycenter.findingsStateSetter`) Set state access to findings  Lowest-level resources where you can grant this role:

  * Project 

|  `securitycenter.findings.setState` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Findings Viewer 

(`roles/securitycenter.findingsViewer`) Read access to findings  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.folders.get` `resourcemanager.organizations.get` `resourcemanager.projects.get` `securitycenter.complianceReports.aggregate` `securitycenter.compliancesnapshots.list` `securitycenter.findingexplanations.get` `securitycenter.findings.group` `securitycenter.findings.list` `securitycenter.findings.listFindingPropertyNames` `securitycenter.graphs.*`

  * `securitycenter.graphs.get`
  * `securitycenter.graphs.query`

`securitycenter.issues.get` `securitycenter.issues.group` `securitycenter.issues.list` `securitycenter.issues.listFilterValues` `securitycenter.issues.retrieve` `securitycenter.issues.search` `securitycenter.issues.searchImpactedResources` `securitycenter.sources.get` `securitycenter.sources.list` `securitycenter.userinterfacemetadata.get` `securitycenter.vulnerabilitysnapshots.list`  
  
#### Security Center Findings Workflow State Setter Beta

(`roles/securitycenter.findingsWorkflowStateSetter`) Set workflow state access to findings  Lowest-level resources where you can grant this role:

  * Project 

|  `securitycenter.findings.setWorkflowState` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Issues Editor 

(`roles/securitycenter.issuesEditor`) Write access to security center issues  |  `securitycenter.graphs.*`

  * `securitycenter.graphs.get`
  * `securitycenter.graphs.query`

`securitycenter.issues.*`

  * `securitycenter.issues.get`
  * `securitycenter.issues.group`
  * `securitycenter.issues.list`
  * `securitycenter.issues.listFilterValues`
  * `securitycenter.issues.mute`
  * `securitycenter.issues.retrieve`
  * `securitycenter.issues.search`
  * `securitycenter.issues.searchImpactedResources`

  
  
#### Security Center Issues Viewer 

(`roles/securitycenter.issuesViewer`) Read access to security center issues  |  `securitycenter.graphs.*`

  * `securitycenter.graphs.get`
  * `securitycenter.graphs.query`

`securitycenter.issues.get` `securitycenter.issues.group` `securitycenter.issues.list` `securitycenter.issues.listFilterValues` `securitycenter.issues.retrieve` `securitycenter.issues.search` `securitycenter.issues.searchImpactedResources`  
  
#### Security Center Mute Configurations Editor 

(`roles/securitycenter.muteConfigsEditor`) Read-Write access to security center mute configurations  |  `securitycenter.muteconfigs.*`

  * `securitycenter.muteconfigs.create`
  * `securitycenter.muteconfigs.delete`
  * `securitycenter.muteconfigs.get`
  * `securitycenter.muteconfigs.list`
  * `securitycenter.muteconfigs.update`

  
  
#### Security Center Mute Configurations Viewer 

(`roles/securitycenter.muteConfigsViewer`) Read access to security center mute configurations  |  `securitycenter.muteconfigs.get` `securitycenter.muteconfigs.list`  
  
#### Security Center Notification Configurations Editor 

(`roles/securitycenter.notificationConfigEditor`) Write access to notification configurations  Lowest-level resources where you can grant this role:

  * Organization 

|  `securitycenter.notificationconfig.*`

  * `securitycenter.notificationconfig.create`
  * `securitycenter.notificationconfig.delete`
  * `securitycenter.notificationconfig.get`
  * `securitycenter.notificationconfig.list`
  * `securitycenter.notificationconfig.update`

`securitycenter.userinterfacemetadata.get`  
  
#### Security Center Notification Configurations Viewer 

(`roles/securitycenter.notificationConfigViewer`) Read access to notification configurations  Lowest-level resources where you can grant this role:

  * Organization 

|  `securitycenter.notificationconfig.get` `securitycenter.notificationconfig.list` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Resource Value Configurations Editor 

(`roles/securitycenter.resourceValueConfigsEditor`) Read-Write access to security center resource value configurations  |  `resourcemanager.tagValues.get` `securitycenter.resourcevalueconfigs.*`

  * `securitycenter.resourcevalueconfigs.create`
  * `securitycenter.resourcevalueconfigs.delete`
  * `securitycenter.resourcevalueconfigs.get`
  * `securitycenter.resourcevalueconfigs.list`
  * `securitycenter.resourcevalueconfigs.update`

  
  
#### Security Center Resource Value Configurations Viewer 

(`roles/securitycenter.resourceValueConfigsViewer`) Read access to security center resource value configurations  |  `resourcemanager.tagValues.get` `securitycenter.resourcevalueconfigs.get` `securitycenter.resourcevalueconfigs.list`  
  
#### Security Center Risk Reports Viewer 

(`roles/securitycenter.riskReportsViewer`) Read access to security center risk reports  |  `securitycenter.riskreports.*`

  * `securitycenter.riskreports.get`
  * `securitycenter.riskreports.list`

`securitycenter.userinterfacemetadata.get`  
  
#### Security Health Analytics Custom Modules Tester 

(`roles/securitycenter.securityHealthAnalyticsCustomModulesTester`) Test access to Security Health Analytics Custom Modules  |  `securitycenter.securityhealthanalyticscustommodules.simulate` `securitycenter.securityhealthanalyticscustommodules.test` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.test`  
  
#### Security Center Settings Admin 

(`roles/securitycenter.settingsAdmin`) Admin(super user) access to security center settings  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.bigQueryExports.*`

  * `securitycenter.bigQueryExports.create`
  * `securitycenter.bigQueryExports.delete`
  * `securitycenter.bigQueryExports.get`
  * `securitycenter.bigQueryExports.list`
  * `securitycenter.bigQueryExports.update`

`securitycenter.billingtier.update` `securitycenter.containerthreatdetectionsettings.*`

  * `securitycenter.containerthreatdetectionsettings.calculate`
  * `securitycenter.containerthreatdetectionsettings.get`
  * `securitycenter.containerthreatdetectionsettings.update`

`securitycenter.effectivesecurityhealthanalyticscustommodules.*`

  * `securitycenter.effectivesecurityhealthanalyticscustommodules.get`
  * `securitycenter.effectivesecurityhealthanalyticscustommodules.list`

`securitycenter.eventthreatdetectionsettings.*`

  * `securitycenter.eventthreatdetectionsettings.calculate`
  * `securitycenter.eventthreatdetectionsettings.get`
  * `securitycenter.eventthreatdetectionsettings.update`

`securitycenter.findings.export` `securitycenter.integratedvulnerabilityscannersettings.*`

  * `securitycenter.integratedvulnerabilityscannersettings.calculate`
  * `securitycenter.integratedvulnerabilityscannersettings.get`
  * `securitycenter.integratedvulnerabilityscannersettings.update`

`securitycenter.muteconfigs.*`

  * `securitycenter.muteconfigs.create`
  * `securitycenter.muteconfigs.delete`
  * `securitycenter.muteconfigs.get`
  * `securitycenter.muteconfigs.list`
  * `securitycenter.muteconfigs.update`

`securitycenter.notificationconfig.*`

  * `securitycenter.notificationconfig.create`
  * `securitycenter.notificationconfig.delete`
  * `securitycenter.notificationconfig.get`
  * `securitycenter.notificationconfig.list`
  * `securitycenter.notificationconfig.update`

`securitycenter.organizationsettings.*`

  * `securitycenter.organizationsettings.get`
  * `securitycenter.organizationsettings.update`

`securitycenter.rapidvulnerabilitydetectionsettings.*`

  * `securitycenter.rapidvulnerabilitydetectionsettings.calculate`
  * `securitycenter.rapidvulnerabilitydetectionsettings.get`
  * `securitycenter.rapidvulnerabilitydetectionsettings.update`

`securitycenter.securitycentersettings.*`

  * `securitycenter.securitycentersettings.get`
  * `securitycenter.securitycentersettings.update`

`securitycenter.securityhealthanalyticscustommodules.create` `securitycenter.securityhealthanalyticscustommodules.delete` `securitycenter.securityhealthanalyticscustommodules.get` `securitycenter.securityhealthanalyticscustommodules.list` `securitycenter.securityhealthanalyticscustommodules.update` `securitycenter.securityhealthanalyticssettings.*`

  * `securitycenter.securityhealthanalyticssettings.calculate`
  * `securitycenter.securityhealthanalyticssettings.get`
  * `securitycenter.securityhealthanalyticssettings.update`

`securitycenter.subscription.get` `securitycenter.userinterfacemetadata.get` `securitycenter.virtualmachinethreatdetectionsettings.*`

  * `securitycenter.virtualmachinethreatdetectionsettings.calculate`
  * `securitycenter.virtualmachinethreatdetectionsettings.get`
  * `securitycenter.virtualmachinethreatdetectionsettings.update`

`securitycenter.websecurityscannersettings.*`

  * `securitycenter.websecurityscannersettings.calculate`
  * `securitycenter.websecurityscannersettings.get`
  * `securitycenter.websecurityscannersettings.update`

`securitycentermanagement.*`

  * `securitycentermanagement.billingMetadata.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.create`
  * `securitycentermanagement.eventThreatDetectionCustomModules.delete`
  * `securitycentermanagement.eventThreatDetectionCustomModules.get`
  * `securitycentermanagement.eventThreatDetectionCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.update`
  * `securitycentermanagement.eventThreatDetectionCustomModules.validate`
  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`
  * `securitycentermanagement.operations.cancel`
  * `securitycentermanagement.operations.delete`
  * `securitycentermanagement.operations.get`
  * `securitycentermanagement.operations.list`
  * `securitycentermanagement.securityCenter.get`
  * `securitycentermanagement.securityCenter.migrate`
  * `securitycentermanagement.securityCenter.update`
  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`
  * `securitycentermanagement.securityCommandCenter.activate`
  * `securitycentermanagement.securityCommandCenter.checkActivationOperation`
  * `securitycentermanagement.securityCommandCenter.checkEligibility`
  * `securitycentermanagement.securityCommandCenter.checkOnboardingStatus`
  * `securitycentermanagement.securityCommandCenter.generateServiceAccounts`
  * `securitycentermanagement.securityCommandCenter.get`
  * `securitycentermanagement.securityCommandCenter.update`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.create`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.delete`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.test`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.update`

  
  
#### Security Center Settings Editor 

(`roles/securitycenter.settingsEditor`) Read-Write access to security center settings  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.bigQueryExports.*`

  * `securitycenter.bigQueryExports.create`
  * `securitycenter.bigQueryExports.delete`
  * `securitycenter.bigQueryExports.get`
  * `securitycenter.bigQueryExports.list`
  * `securitycenter.bigQueryExports.update`

`securitycenter.billingtier.update` `securitycenter.containerthreatdetectionsettings.*`

  * `securitycenter.containerthreatdetectionsettings.calculate`
  * `securitycenter.containerthreatdetectionsettings.get`
  * `securitycenter.containerthreatdetectionsettings.update`

`securitycenter.effectivesecurityhealthanalyticscustommodules.*`

  * `securitycenter.effectivesecurityhealthanalyticscustommodules.get`
  * `securitycenter.effectivesecurityhealthanalyticscustommodules.list`

`securitycenter.eventthreatdetectionsettings.*`

  * `securitycenter.eventthreatdetectionsettings.calculate`
  * `securitycenter.eventthreatdetectionsettings.get`
  * `securitycenter.eventthreatdetectionsettings.update`

`securitycenter.findings.export` `securitycenter.integratedvulnerabilityscannersettings.*`

  * `securitycenter.integratedvulnerabilityscannersettings.calculate`
  * `securitycenter.integratedvulnerabilityscannersettings.get`
  * `securitycenter.integratedvulnerabilityscannersettings.update`

`securitycenter.muteconfigs.*`

  * `securitycenter.muteconfigs.create`
  * `securitycenter.muteconfigs.delete`
  * `securitycenter.muteconfigs.get`
  * `securitycenter.muteconfigs.list`
  * `securitycenter.muteconfigs.update`

`securitycenter.notificationconfig.*`

  * `securitycenter.notificationconfig.create`
  * `securitycenter.notificationconfig.delete`
  * `securitycenter.notificationconfig.get`
  * `securitycenter.notificationconfig.list`
  * `securitycenter.notificationconfig.update`

`securitycenter.organizationsettings.*`

  * `securitycenter.organizationsettings.get`
  * `securitycenter.organizationsettings.update`

`securitycenter.rapidvulnerabilitydetectionsettings.*`

  * `securitycenter.rapidvulnerabilitydetectionsettings.calculate`
  * `securitycenter.rapidvulnerabilitydetectionsettings.get`
  * `securitycenter.rapidvulnerabilitydetectionsettings.update`

`securitycenter.securitycentersettings.*`

  * `securitycenter.securitycentersettings.get`
  * `securitycenter.securitycentersettings.update`

`securitycenter.securityhealthanalyticscustommodules.create` `securitycenter.securityhealthanalyticscustommodules.delete` `securitycenter.securityhealthanalyticscustommodules.get` `securitycenter.securityhealthanalyticscustommodules.list` `securitycenter.securityhealthanalyticscustommodules.update` `securitycenter.securityhealthanalyticssettings.*`

  * `securitycenter.securityhealthanalyticssettings.calculate`
  * `securitycenter.securityhealthanalyticssettings.get`
  * `securitycenter.securityhealthanalyticssettings.update`

`securitycenter.subscription.get` `securitycenter.userinterfacemetadata.get` `securitycenter.virtualmachinethreatdetectionsettings.*`

  * `securitycenter.virtualmachinethreatdetectionsettings.calculate`
  * `securitycenter.virtualmachinethreatdetectionsettings.get`
  * `securitycenter.virtualmachinethreatdetectionsettings.update`

`securitycenter.websecurityscannersettings.*`

  * `securitycenter.websecurityscannersettings.calculate`
  * `securitycenter.websecurityscannersettings.get`
  * `securitycenter.websecurityscannersettings.update`

`securitycentermanagement.*`

  * `securitycentermanagement.billingMetadata.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.create`
  * `securitycentermanagement.eventThreatDetectionCustomModules.delete`
  * `securitycentermanagement.eventThreatDetectionCustomModules.get`
  * `securitycentermanagement.eventThreatDetectionCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.update`
  * `securitycentermanagement.eventThreatDetectionCustomModules.validate`
  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`
  * `securitycentermanagement.operations.cancel`
  * `securitycentermanagement.operations.delete`
  * `securitycentermanagement.operations.get`
  * `securitycentermanagement.operations.list`
  * `securitycentermanagement.securityCenter.get`
  * `securitycentermanagement.securityCenter.migrate`
  * `securitycentermanagement.securityCenter.update`
  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`
  * `securitycentermanagement.securityCommandCenter.activate`
  * `securitycentermanagement.securityCommandCenter.checkActivationOperation`
  * `securitycentermanagement.securityCommandCenter.checkEligibility`
  * `securitycentermanagement.securityCommandCenter.checkOnboardingStatus`
  * `securitycentermanagement.securityCommandCenter.generateServiceAccounts`
  * `securitycentermanagement.securityCommandCenter.get`
  * `securitycentermanagement.securityCommandCenter.update`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.create`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.delete`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.test`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.update`

  
  
#### Security Center Settings Viewer 

(`roles/securitycenter.settingsViewer`) Read access to security center settings  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.bigQueryExports.get` `securitycenter.bigQueryExports.list` `securitycenter.containerthreatdetectionsettings.calculate` `securitycenter.containerthreatdetectionsettings.get` `securitycenter.effectivesecurityhealthanalyticscustommodules.*`

  * `securitycenter.effectivesecurityhealthanalyticscustommodules.get`
  * `securitycenter.effectivesecurityhealthanalyticscustommodules.list`

`securitycenter.eventthreatdetectionsettings.calculate` `securitycenter.eventthreatdetectionsettings.get` `securitycenter.integratedvulnerabilityscannersettings.calculate` `securitycenter.integratedvulnerabilityscannersettings.get` `securitycenter.muteconfigs.get` `securitycenter.muteconfigs.list` `securitycenter.notificationconfig.get` `securitycenter.notificationconfig.list` `securitycenter.organizationsettings.get` `securitycenter.rapidvulnerabilitydetectionsettings.calculate` `securitycenter.rapidvulnerabilitydetectionsettings.get` `securitycenter.securitycentersettings.get` `securitycenter.securityhealthanalyticscustommodules.get` `securitycenter.securityhealthanalyticscustommodules.list` `securitycenter.securityhealthanalyticssettings.calculate` `securitycenter.securityhealthanalyticssettings.get` `securitycenter.subscription.get` `securitycenter.userinterfacemetadata.get` `securitycenter.virtualmachinethreatdetectionsettings.calculate` `securitycenter.virtualmachinethreatdetectionsettings.get` `securitycenter.websecurityscannersettings.calculate` `securitycenter.websecurityscannersettings.get` `securitycentermanagement.billingMetadata.get` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.get` `securitycentermanagement.eventThreatDetectionCustomModules.list` `securitycentermanagement.eventThreatDetectionCustomModules.validate` `securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.operations.get` `securitycentermanagement.operations.list` `securitycentermanagement.securityCenter.get` `securitycentermanagement.securityCenterServices.get` `securitycentermanagement.securityCenterServices.list` `securitycentermanagement.securityCommandCenter.checkActivationOperation` `securitycentermanagement.securityCommandCenter.checkEligibility` `securitycentermanagement.securityCommandCenter.checkOnboardingStatus` `securitycentermanagement.securityCommandCenter.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.test`  
  
#### Security Center Simulations Reader 

(`roles/securitycenter.simulationsViewer`) Read access to security center simulations  |  `securitycenter.simulations.get`  
  
#### Security Center Sources Admin 

(`roles/securitycenter.sourcesAdmin`) Admin access to sources  Lowest-level resources where you can grant this role:

  * Organization 

|  `resourcemanager.organizations.get` `securitycenter.sources.*`

  * `securitycenter.sources.get`
  * `securitycenter.sources.getIamPolicy`
  * `securitycenter.sources.list`
  * `securitycenter.sources.setIamPolicy`
  * `securitycenter.sources.update`

`securitycenter.userinterfacemetadata.get`  
  
#### Security Center Sources Editor 

(`roles/securitycenter.sourcesEditor`) Read-write access to sources  Lowest-level resources where you can grant this role:

  * Organization 

|  `resourcemanager.organizations.get` `securitycenter.sources.get` `securitycenter.sources.list` `securitycenter.sources.update` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Sources Viewer 

(`roles/securitycenter.sourcesViewer`) Read access to sources  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.organizations.get` `securitycenter.sources.get` `securitycenter.sources.list` `securitycenter.userinterfacemetadata.get`  
  
#### Security Center Valued Resources Reader 

(`roles/securitycenter.valuedResourcesViewer`) Read access to security center valued resources  |  `securitycenter.valuedresources.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Attack Surface Management Scanner Service Agent 

(`roles/securitycenter.attackSurfaceManagementScannerServiceAgent`) Gives Mandiant Attack Surface Management the ability to scan Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `apigateway.apiconfigs.get` `cloudasset.assets.listResource` `dns.managedZones.list` `dns.resourceRecordSets.list` `resourcemanager.projects.get`  
  
#### Security Center Automation Service Agent 

(`roles/securitycenter.automationServiceAgent`) Security Center automation service agent can configure GCP resources to enable security scanning.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudasset.feeds.*`

  * `cloudasset.feeds.create`
  * `cloudasset.feeds.delete`
  * `cloudasset.feeds.get`
  * `cloudasset.feeds.list`
  * `cloudasset.feeds.update`

`resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Security Center Control Service Agent 

(`roles/securitycenter.controlServiceAgent`) Security Center Control service agent can monitor and configure GCP resources and import security findings.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `accesscontextmanager.gcpUserAccessBindings.get` `accesscontextmanager.gcpUserAccessBindings.list` `aiplatform.dataItems.list` `aiplatform.datasets.list` `aiplatform.models.list` `bigquery.datasets.get` `binaryauthorization.policy.get` `cloudasset.assets.analyzeIamPolicy` `cloudasset.assets.analyzeMove` `cloudasset.assets.analyzeOrgPolicy` `cloudasset.assets.exportAccessLevel` `cloudasset.assets.exportAccessPolicy` `cloudasset.assets.exportAiplatformBatchPredictionJobs` `cloudasset.assets.exportAiplatformCustomJobs` `cloudasset.assets.exportAiplatformDataLabelingJobs` `cloudasset.assets.exportAiplatformDatasets` `cloudasset.assets.exportAiplatformEndpoints` `cloudasset.assets.exportAiplatformHyperparameterTuningJobs` `cloudasset.assets.exportAiplatformMetadataStores` `cloudasset.assets.exportAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.exportAiplatformModels` `cloudasset.assets.exportAiplatformPipelineJobs` `cloudasset.assets.exportAiplatformSpecialistPools` `cloudasset.assets.exportAiplatformTrainingPipelines` `cloudasset.assets.exportAllAccessPolicy` `cloudasset.assets.exportAnthosConnectedCluster` `cloudasset.assets.exportAnthosedgeCluster` `cloudasset.assets.exportApigatewayApi` `cloudasset.assets.exportApigatewayApiConfig` `cloudasset.assets.exportApigatewayGateway` `cloudasset.assets.exportApikeysKeys` `cloudasset.assets.exportAppengineApplications` `cloudasset.assets.exportAppengineServices` `cloudasset.assets.exportAppengineVersions` `cloudasset.assets.exportArtifactregistryDockerImages` `cloudasset.assets.exportArtifactregistryRepositories` `cloudasset.assets.exportAssuredWorkloadsWorkloads` `cloudasset.assets.exportBeyondCorpApiGateways` `cloudasset.assets.exportBeyondCorpAppConnections` `cloudasset.assets.exportBeyondCorpAppConnectors` `cloudasset.assets.exportBeyondCorpAppGateways` `cloudasset.assets.exportBeyondCorpClientConnectorServices` `cloudasset.assets.exportBeyondCorpClientGateways` `cloudasset.assets.exportBigqueryDatasets` `cloudasset.assets.exportBigqueryModels` `cloudasset.assets.exportBigqueryTables` `cloudasset.assets.exportBigtableAppProfile` `cloudasset.assets.exportBigtableBackup` `cloudasset.assets.exportBigtableCluster` `cloudasset.assets.exportBigtableInstance` `cloudasset.assets.exportBigtableTable` `cloudasset.assets.exportCloudAssetFeeds` `cloudasset.assets.exportCloudDeployDeliveryPipelines` `cloudasset.assets.exportCloudDeployReleases` `cloudasset.assets.exportCloudDeployRollouts` `cloudasset.assets.exportCloudDeployTargets` `cloudasset.assets.exportCloudDocumentAIEvaluation` `cloudasset.assets.exportCloudDocumentAIHumanReviewConfig` `cloudasset.assets.exportCloudDocumentAILabelerPool` `cloudasset.assets.exportCloudDocumentAIProcessor` `cloudasset.assets.exportCloudDocumentAIProcessorVersion` `cloudasset.assets.exportCloudbillingBillingAccounts` `cloudasset.assets.exportCloudbillingProjectBillingInfos` `cloudasset.assets.exportCloudfunctionsFunctions` `cloudasset.assets.exportCloudfunctionsGen2Functions` `cloudasset.assets.exportCloudkmsCryptoKeyVersions` `cloudasset.assets.exportCloudkmsCryptoKeys` `cloudasset.assets.exportCloudkmsEkmConnections` `cloudasset.assets.exportCloudkmsImportJobs` `cloudasset.assets.exportCloudkmsKeyRings` `cloudasset.assets.exportCloudmemcacheInstances` `cloudasset.assets.exportCloudresourcemanagerFolders` `cloudasset.assets.exportCloudresourcemanagerOrganizations` `cloudasset.assets.exportCloudresourcemanagerProjects` `cloudasset.assets.exportCloudresourcemanagerTagBindings` `cloudasset.assets.exportCloudresourcemanagerTagKeys` `cloudasset.assets.exportCloudresourcemanagerTagValues` `cloudasset.assets.exportComposerEnvironments` `cloudasset.assets.exportComputeAddress` `cloudasset.assets.exportComputeAutoscalers` `cloudasset.assets.exportComputeBackendBuckets` `cloudasset.assets.exportComputeBackendServices` `cloudasset.assets.exportComputeCommitments` `cloudasset.assets.exportComputeDisks` `cloudasset.assets.exportComputeExternalVpnGateways` `cloudasset.assets.exportComputeFirewallPolicies` `cloudasset.assets.exportComputeFirewalls` `cloudasset.assets.exportComputeForwardingRules` `cloudasset.assets.exportComputeGlobalAddress` `cloudasset.assets.exportComputeGlobalForwardingRules` `cloudasset.assets.exportComputeHealthChecks` `cloudasset.assets.exportComputeHttpHealthChecks` `cloudasset.assets.exportComputeHttpsHealthChecks` `cloudasset.assets.exportComputeImages` `cloudasset.assets.exportComputeInstanceGroupManagers` `cloudasset.assets.exportComputeInstanceGroups` `cloudasset.assets.exportComputeInstanceTemplates` `cloudasset.assets.exportComputeInstances` `cloudasset.assets.exportComputeInterconnect` `cloudasset.assets.exportComputeInterconnectAttachment` `cloudasset.assets.exportComputeLicenses` `cloudasset.assets.exportComputeNetworkEndpointGroups` `cloudasset.assets.exportComputeNetworks` `cloudasset.assets.exportComputeNodeGroups` `cloudasset.assets.exportComputeNodeTemplates` `cloudasset.assets.exportComputePacketMirrorings` `cloudasset.assets.exportComputeProjects` `cloudasset.assets.exportComputeRegionAutoscaler` `cloudasset.assets.exportComputeRegionBackendServices` `cloudasset.assets.exportComputeRegionDisk` `cloudasset.assets.exportComputeRegionInstanceGroup` `cloudasset.assets.exportComputeRegionInstanceGroupManager` `cloudasset.assets.exportComputeReservations` `cloudasset.assets.exportComputeResourcePolicies` `cloudasset.assets.exportComputeRouters` `cloudasset.assets.exportComputeRoutes` `cloudasset.assets.exportComputeSecurityPolicy` `cloudasset.assets.exportComputeServiceAttachments` `cloudasset.assets.exportComputeSnapshots` `cloudasset.assets.exportComputeSslCertificates` `cloudasset.assets.exportComputeSslPolicies` `cloudasset.assets.exportComputeSubnetworks` `cloudasset.assets.exportComputeTargetHttpProxies` `cloudasset.assets.exportComputeTargetHttpsProxies` `cloudasset.assets.exportComputeTargetInstances` `cloudasset.assets.exportComputeTargetPools` `cloudasset.assets.exportComputeTargetSslProxies` `cloudasset.assets.exportComputeTargetTcpProxies` `cloudasset.assets.exportComputeTargetVpnGateways` `cloudasset.assets.exportComputeUrlMaps` `cloudasset.assets.exportComputeVpnGateways` `cloudasset.assets.exportComputeVpnTunnels` `cloudasset.assets.exportConnectorsConnections` `cloudasset.assets.exportConnectorsConnectorVersions` `cloudasset.assets.exportConnectorsConnectors` `cloudasset.assets.exportConnectorsProviders` `cloudasset.assets.exportConnectorsRuntimeConfigs` `cloudasset.assets.exportContainerAppsDeployment` `cloudasset.assets.exportContainerAppsReplicaSets` `cloudasset.assets.exportContainerBatchJobs` `cloudasset.assets.exportContainerClusterrole` `cloudasset.assets.exportContainerClusterrolebinding` `cloudasset.assets.exportContainerClusters` `cloudasset.assets.exportContainerExtensionsIngresses` `cloudasset.assets.exportContainerJobs` `cloudasset.assets.exportContainerNamespace` `cloudasset.assets.exportContainerNetworkingIngresses` `cloudasset.assets.exportContainerNetworkingNetworkPolicies` `cloudasset.assets.exportContainerNode` `cloudasset.assets.exportContainerNodepool` `cloudasset.assets.exportContainerPod` `cloudasset.assets.exportContainerReplicaSets` `cloudasset.assets.exportContainerRole` `cloudasset.assets.exportContainerRolebinding` `cloudasset.assets.exportContainerServices` `cloudasset.assets.exportContainerregistryImage` `cloudasset.assets.exportDataMigrationConnectionProfiles` `cloudasset.assets.exportDataMigrationMigrationJobs` `cloudasset.assets.exportDataflowJobs` `cloudasset.assets.exportDatafusionInstance` `cloudasset.assets.exportDataplexAssets` `cloudasset.assets.exportDataplexLakes` `cloudasset.assets.exportDataplexTasks` `cloudasset.assets.exportDataplexZones` `cloudasset.assets.exportDataprocAutoscalingPolicies` `cloudasset.assets.exportDataprocBatches` `cloudasset.assets.exportDataprocClusters` `cloudasset.assets.exportDataprocJobs` `cloudasset.assets.exportDataprocSessions` `cloudasset.assets.exportDataprocWorkflowTemplates` `cloudasset.assets.exportDatastreamConnectionProfile` `cloudasset.assets.exportDatastreamPrivateConnection` `cloudasset.assets.exportDatastreamStream` `cloudasset.assets.exportDialogflowAgents` `cloudasset.assets.exportDialogflowConversationProfiles` `cloudasset.assets.exportDialogflowKnowledgeBases` `cloudasset.assets.exportDialogflowLocationSettings` `cloudasset.assets.exportDlpDeidentifyTemplates` `cloudasset.assets.exportDlpDlpJobs` `cloudasset.assets.exportDlpInspectTemplates` `cloudasset.assets.exportDlpJobTriggers` `cloudasset.assets.exportDlpStoredInfoTypes` `cloudasset.assets.exportDnsManagedZones` `cloudasset.assets.exportDnsPolicies` `cloudasset.assets.exportDomainsRegistrations` `cloudasset.assets.exportEventarcTriggers` `cloudasset.assets.exportFileBackups` `cloudasset.assets.exportFileInstances` `cloudasset.assets.exportFirebaseAppInfos` `cloudasset.assets.exportFirebaseProjects` `cloudasset.assets.exportFirestoreDatabases` `cloudasset.assets.exportGKEHubFeatures` `cloudasset.assets.exportGKEHubMemberships` `cloudasset.assets.exportGameservicesGameServerClusters` `cloudasset.assets.exportGameservicesGameServerConfigs` `cloudasset.assets.exportGameservicesGameServerDeployments` `cloudasset.assets.exportGameservicesRealms` `cloudasset.assets.exportGkeBackupBackupPlans` `cloudasset.assets.exportGkeBackupBackups` `cloudasset.assets.exportGkeBackupRestorePlans` `cloudasset.assets.exportGkeBackupRestores` `cloudasset.assets.exportGkeBackupVolumeBackups` `cloudasset.assets.exportGkeBackupVolumeRestores` `cloudasset.assets.exportHealthcareConsentStores` `cloudasset.assets.exportHealthcareDatasets` `cloudasset.assets.exportHealthcareDicomStores` `cloudasset.assets.exportHealthcareFhirStores` `cloudasset.assets.exportHealthcareHl7V2Stores` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportIamRoles` `cloudasset.assets.exportIamServiceAccountKeys` `cloudasset.assets.exportIamServiceAccounts` `cloudasset.assets.exportIapTunnel` `cloudasset.assets.exportIapTunnelInstances` `cloudasset.assets.exportIapTunnelZones` `cloudasset.assets.exportIapWeb` `cloudasset.assets.exportIapWebServiceVersion` `cloudasset.assets.exportIapWebServices` `cloudasset.assets.exportIapWebType` `cloudasset.assets.exportIdsEndpoints` `cloudasset.assets.exportIntegrationsAuthConfigs` `cloudasset.assets.exportIntegrationsCertificates` `cloudasset.assets.exportIntegrationsExecutions` `cloudasset.assets.exportIntegrationsIntegrationVersions` `cloudasset.assets.exportIntegrationsIntegrations` `cloudasset.assets.exportIntegrationsSfdcChannels` `cloudasset.assets.exportIntegrationsSfdcInstances` `cloudasset.assets.exportIntegrationsSuspensions` `cloudasset.assets.exportLoggingLogMetrics` `cloudasset.assets.exportLoggingLogSinks` `cloudasset.assets.exportManagedidentitiesDomain` `cloudasset.assets.exportMetastoreBackups` `cloudasset.assets.exportMetastoreMetadataImports` `cloudasset.assets.exportMetastoreServices` `cloudasset.assets.exportMonitoringAlertPolicies` `cloudasset.assets.exportNetworkConnectivityHubs` `cloudasset.assets.exportNetworkConnectivitySpokes` `cloudasset.assets.exportNetworkManagementConnectivityTests` `cloudasset.assets.exportNetworkServicesEndpointPolicies` `cloudasset.assets.exportNetworkServicesGateways` `cloudasset.assets.exportNetworkServicesGrpcRoutes` `cloudasset.assets.exportNetworkServicesHttpRoutes` `cloudasset.assets.exportNetworkServicesMeshes` `cloudasset.assets.exportNetworkServicesServiceBindings` `cloudasset.assets.exportNetworkServicesTcpRoutes` `cloudasset.assets.exportNetworkServicesTlsRoutes` `cloudasset.assets.exportOSConfigOSPolicyAssignmentReports` `cloudasset.assets.exportOSConfigOSPolicyAssignments` `cloudasset.assets.exportOSConfigVulnerabilityReports` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportOrgPolicy` `cloudasset.assets.exportPatchDeployments` `cloudasset.assets.exportPubsubSnapshots` `cloudasset.assets.exportPubsubSubscriptions` `cloudasset.assets.exportPubsubTopics` `cloudasset.assets.exportRedisInstances` `cloudasset.assets.exportResource` `cloudasset.assets.exportSecretManagerSecretVersions` `cloudasset.assets.exportSecretManagerSecrets` `cloudasset.assets.exportServiceDirectoryNamespaces` `cloudasset.assets.exportServicePerimeter` `cloudasset.assets.exportServiceconsumermanagementConsumerProperty` `cloudasset.assets.exportServiceconsumermanagementConsumerQuotaLimits` `cloudasset.assets.exportServiceconsumermanagementConsumers` `cloudasset.assets.exportServiceconsumermanagementProducerOverrides` `cloudasset.assets.exportServiceconsumermanagementTenancyUnits` `cloudasset.assets.exportServiceconsumermanagementVisibility` `cloudasset.assets.exportServicemanagementServices` `cloudasset.assets.exportServiceusageAdminOverrides` `cloudasset.assets.exportServiceusageConsumerOverrides` `cloudasset.assets.exportServiceusageServices` `cloudasset.assets.exportSpannerBackups` `cloudasset.assets.exportSpannerDatabases` `cloudasset.assets.exportSpannerInstances` `cloudasset.assets.exportSpeakerIdPhrases` `cloudasset.assets.exportSpeakerIdSettings` `cloudasset.assets.exportSpeakerIdSpeakers` `cloudasset.assets.exportSpeechCustomClasses` `cloudasset.assets.exportSpeechPhraseSets` `cloudasset.assets.exportSqladminBackupRuns` `cloudasset.assets.exportSqladminInstances` `cloudasset.assets.exportStorageBuckets` `cloudasset.assets.exportTpuNodes` `cloudasset.assets.exportVpcaccessConnector` `cloudasset.assets.listAccessLevel` `cloudasset.assets.listAccessPolicy` `cloudasset.assets.listAiplatformBatchPredictionJobs` `cloudasset.assets.listAiplatformCustomJobs` `cloudasset.assets.listAiplatformDataLabelingJobs` `cloudasset.assets.listAiplatformDatasets` `cloudasset.assets.listAiplatformEndpoints` `cloudasset.assets.listAiplatformHyperparameterTuningJobs` `cloudasset.assets.listAiplatformMetadataStores` `cloudasset.assets.listAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.listAiplatformModels` `cloudasset.assets.listAiplatformPipelineJobs` `cloudasset.assets.listAiplatformSpecialistPools` `cloudasset.assets.listAiplatformTrainingPipelines` `cloudasset.assets.listAllAccessPolicy` `cloudasset.assets.listAnthosConnectedCluster` `cloudasset.assets.listAnthosedgeCluster` `cloudasset.assets.listApigatewayApi` `cloudasset.assets.listApigatewayApiConfig` `cloudasset.assets.listApigatewayGateway` `cloudasset.assets.listApikeysKeys` `cloudasset.assets.listAppengineApplications` `cloudasset.assets.listAppengineServices` `cloudasset.assets.listAppengineVersions` `cloudasset.assets.listArtifactregistryDockerImages` `cloudasset.assets.listArtifactregistryRepositories` `cloudasset.assets.listAssuredWorkloadsWorkloads` `cloudasset.assets.listBeyondCorpApiGateways` `cloudasset.assets.listBeyondCorpAppConnections` `cloudasset.assets.listBeyondCorpAppConnectors` `cloudasset.assets.listBeyondCorpAppGateways` `cloudasset.assets.listBeyondCorpClientConnectorServices` `cloudasset.assets.listBeyondCorpClientGateways` `cloudasset.assets.listBigqueryDatasets` `cloudasset.assets.listBigqueryModels` `cloudasset.assets.listBigqueryTables` `cloudasset.assets.listBigtableAppProfile` `cloudasset.assets.listBigtableBackup` `cloudasset.assets.listBigtableCluster` `cloudasset.assets.listBigtableInstance` `cloudasset.assets.listBigtableTable` `cloudasset.assets.listCloudAssetFeeds` `cloudasset.assets.listCloudDeployDeliveryPipelines` `cloudasset.assets.listCloudDeployReleases` `cloudasset.assets.listCloudDeployRollouts` `cloudasset.assets.listCloudDeployTargets` `cloudasset.assets.listCloudDocumentAIEvaluation` `cloudasset.assets.listCloudDocumentAIHumanReviewConfig` `cloudasset.assets.listCloudDocumentAILabelerPool` `cloudasset.assets.listCloudDocumentAIProcessor` `cloudasset.assets.listCloudDocumentAIProcessorVersion` `cloudasset.assets.listCloudbillingBillingAccounts` `cloudasset.assets.listCloudbillingProjectBillingInfos` `cloudasset.assets.listCloudfunctionsFunctions` `cloudasset.assets.listCloudfunctionsGen2Functions` `cloudasset.assets.listCloudkmsCryptoKeyVersions` `cloudasset.assets.listCloudkmsCryptoKeys` `cloudasset.assets.listCloudkmsEkmConnections` `cloudasset.assets.listCloudkmsImportJobs` `cloudasset.assets.listCloudkmsKeyRings` `cloudasset.assets.listCloudmemcacheInstances` `cloudasset.assets.listCloudresourcemanagerFolders` `cloudasset.assets.listCloudresourcemanagerOrganizations` `cloudasset.assets.listCloudresourcemanagerProjects` `cloudasset.assets.listCloudresourcemanagerTagBindings` `cloudasset.assets.listCloudresourcemanagerTagKeys` `cloudasset.assets.listCloudresourcemanagerTagValues` `cloudasset.assets.listComposerEnvironments` `cloudasset.assets.listComputeAddress` `cloudasset.assets.listComputeAutoscalers` `cloudasset.assets.listComputeBackendBuckets` `cloudasset.assets.listComputeBackendServices` `cloudasset.assets.listComputeCommitments` `cloudasset.assets.listComputeDisks` `cloudasset.assets.listComputeExternalVpnGateways` `cloudasset.assets.listComputeFirewallPolicies` `cloudasset.assets.listComputeFirewalls` `cloudasset.assets.listComputeForwardingRules` `cloudasset.assets.listComputeGlobalAddress` `cloudasset.assets.listComputeGlobalForwardingRules` `cloudasset.assets.listComputeHealthChecks` `cloudasset.assets.listComputeHttpHealthChecks` `cloudasset.assets.listComputeHttpsHealthChecks` `cloudasset.assets.listComputeImages` `cloudasset.assets.listComputeInstanceGroupManagers` `cloudasset.assets.listComputeInstanceGroups` `cloudasset.assets.listComputeInstanceTemplates` `cloudasset.assets.listComputeInstances` `cloudasset.assets.listComputeInterconnect` `cloudasset.assets.listComputeInterconnectAttachment` `cloudasset.assets.listComputeLicenses` `cloudasset.assets.listComputeNetworkEndpointGroups` `cloudasset.assets.listComputeNetworks` `cloudasset.assets.listComputeNodeGroups` `cloudasset.assets.listComputeNodeTemplates` `cloudasset.assets.listComputePacketMirrorings` `cloudasset.assets.listComputeProjects` `cloudasset.assets.listComputeRegionAutoscaler` `cloudasset.assets.listComputeRegionBackendServices` `cloudasset.assets.listComputeRegionDisk` `cloudasset.assets.listComputeRegionInstanceGroup` `cloudasset.assets.listComputeRegionInstanceGroupManager` `cloudasset.assets.listComputeReservations` `cloudasset.assets.listComputeResourcePolicies` `cloudasset.assets.listComputeRouters` `cloudasset.assets.listComputeRoutes` `cloudasset.assets.listComputeSecurityPolicy` `cloudasset.assets.listComputeServiceAttachments` `cloudasset.assets.listComputeSnapshots` `cloudasset.assets.listComputeSslCertificates` `cloudasset.assets.listComputeSslPolicies` `cloudasset.assets.listComputeSubnetworks` `cloudasset.assets.listComputeTargetHttpProxies` `cloudasset.assets.listComputeTargetHttpsProxies` `cloudasset.assets.listComputeTargetInstances` `cloudasset.assets.listComputeTargetPools` `cloudasset.assets.listComputeTargetSslProxies` `cloudasset.assets.listComputeTargetTcpProxies` `cloudasset.assets.listComputeTargetVpnGateways` `cloudasset.assets.listComputeUrlMaps` `cloudasset.assets.listComputeVpnGateways` `cloudasset.assets.listComputeVpnTunnels` `cloudasset.assets.listConnectorsConnections` `cloudasset.assets.listConnectorsConnectorVersions` `cloudasset.assets.listConnectorsConnectors` `cloudasset.assets.listConnectorsProviders` `cloudasset.assets.listConnectorsRuntimeConfigs` `cloudasset.assets.listContainerAppsDeployment` `cloudasset.assets.listContainerAppsReplicaSets` `cloudasset.assets.listContainerBatchJobs` `cloudasset.assets.listContainerClusterrole` `cloudasset.assets.listContainerClusterrolebinding` `cloudasset.assets.listContainerClusters` `cloudasset.assets.listContainerExtensionsIngresses` `cloudasset.assets.listContainerJobs` `cloudasset.assets.listContainerNamespace` `cloudasset.assets.listContainerNetworkingIngresses` `cloudasset.assets.listContainerNetworkingNetworkPolicies` `cloudasset.assets.listContainerNode` `cloudasset.assets.listContainerNodepool` `cloudasset.assets.listContainerPod` `cloudasset.assets.listContainerReplicaSets` `cloudasset.assets.listContainerRole` `cloudasset.assets.listContainerRolebinding` `cloudasset.assets.listContainerServices` `cloudasset.assets.listContainerregistryImage` `cloudasset.assets.listDataMigrationConnectionProfiles` `cloudasset.assets.listDataMigrationMigrationJobs` `cloudasset.assets.listDataflowJobs` `cloudasset.assets.listDatafusionInstance` `cloudasset.assets.listDataplexAssets` `cloudasset.assets.listDataplexLakes` `cloudasset.assets.listDataplexTasks` `cloudasset.assets.listDataplexZones` `cloudasset.assets.listDataprocAutoscalingPolicies` `cloudasset.assets.listDataprocBatches` `cloudasset.assets.listDataprocClusters` `cloudasset.assets.listDataprocJobs` `cloudasset.assets.listDataprocSessions` `cloudasset.assets.listDataprocWorkflowTemplates` `cloudasset.assets.listDatastreamConnectionProfile` `cloudasset.assets.listDatastreamPrivateConnection` `cloudasset.assets.listDatastreamStream` `cloudasset.assets.listDialogflowAgents` `cloudasset.assets.listDialogflowConversationProfiles` `cloudasset.assets.listDialogflowKnowledgeBases` `cloudasset.assets.listDialogflowLocationSettings` `cloudasset.assets.listDlpDeidentifyTemplates` `cloudasset.assets.listDlpDlpJobs` `cloudasset.assets.listDlpInspectTemplates` `cloudasset.assets.listDlpJobTriggers` `cloudasset.assets.listDlpStoredInfoTypes` `cloudasset.assets.listDnsManagedZones` `cloudasset.assets.listDnsPolicies` `cloudasset.assets.listDomainsRegistrations` `cloudasset.assets.listEventarcTriggers` `cloudasset.assets.listFileBackups` `cloudasset.assets.listFileInstances` `cloudasset.assets.listFirebaseAppInfos` `cloudasset.assets.listFirebaseProjects` `cloudasset.assets.listFirestoreDatabases` `cloudasset.assets.listGKEHubFeatures` `cloudasset.assets.listGKEHubMemberships` `cloudasset.assets.listGameservicesGameServerClusters` `cloudasset.assets.listGameservicesGameServerConfigs` `cloudasset.assets.listGameservicesGameServerDeployments` `cloudasset.assets.listGameservicesRealms` `cloudasset.assets.listGkeBackupBackupPlans` `cloudasset.assets.listGkeBackupBackups` `cloudasset.assets.listGkeBackupRestorePlans` `cloudasset.assets.listGkeBackupRestores` `cloudasset.assets.listGkeBackupVolumeBackups` `cloudasset.assets.listGkeBackupVolumeRestores` `cloudasset.assets.listHealthcareConsentStores` `cloudasset.assets.listHealthcareDatasets` `cloudasset.assets.listHealthcareDicomStores` `cloudasset.assets.listHealthcareFhirStores` `cloudasset.assets.listHealthcareHl7V2Stores` `cloudasset.assets.listIamPolicy` `cloudasset.assets.listIamRoles` `cloudasset.assets.listIamServiceAccountKeys` `cloudasset.assets.listIamServiceAccounts` `cloudasset.assets.listIapTunnel` `cloudasset.assets.listIapTunnelInstances` `cloudasset.assets.listIapTunnelZones` `cloudasset.assets.listIapWeb` `cloudasset.assets.listIapWebServiceVersion` `cloudasset.assets.listIapWebServices` `cloudasset.assets.listIapWebType` `cloudasset.assets.listIdsEndpoints` `cloudasset.assets.listIntegrationsAuthConfigs` `cloudasset.assets.listIntegrationsCertificates` `cloudasset.assets.listIntegrationsExecutions` `cloudasset.assets.listIntegrationsIntegrationVersions` `cloudasset.assets.listIntegrationsIntegrations` `cloudasset.assets.listIntegrationsSfdcChannels` `cloudasset.assets.listIntegrationsSfdcInstances` `cloudasset.assets.listIntegrationsSuspensions` `cloudasset.assets.listLoggingLogMetrics` `cloudasset.assets.listLoggingLogSinks` `cloudasset.assets.listManagedidentitiesDomain` `cloudasset.assets.listMetastoreBackups` `cloudasset.assets.listMetastoreMetadataImports` `cloudasset.assets.listMetastoreServices` `cloudasset.assets.listMonitoringAlertPolicies` `cloudasset.assets.listNetworkConnectivityHubs` `cloudasset.assets.listNetworkConnectivitySpokes` `cloudasset.assets.listNetworkManagementConnectivityTests` `cloudasset.assets.listNetworkServicesEndpointPolicies` `cloudasset.assets.listNetworkServicesGateways` `cloudasset.assets.listNetworkServicesGrpcRoutes` `cloudasset.assets.listNetworkServicesHttpRoutes` `cloudasset.assets.listNetworkServicesMeshes` `cloudasset.assets.listNetworkServicesServiceBindings` `cloudasset.assets.listNetworkServicesTcpRoutes` `cloudasset.assets.listNetworkServicesTlsRoutes` `cloudasset.assets.listOSConfigOSPolicyAssignmentReports` `cloudasset.assets.listOSConfigOSPolicyAssignments` `cloudasset.assets.listOSConfigVulnerabilityReports` `cloudasset.assets.listOSInventories` `cloudasset.assets.listOrgPolicy` `cloudasset.assets.listPatchDeployments` `cloudasset.assets.listPubsubSnapshots` `cloudasset.assets.listPubsubSubscriptions` `cloudasset.assets.listPubsubTopics` `cloudasset.assets.listRedisInstances` `cloudasset.assets.listResource` `cloudasset.assets.listRunDomainMapping` `cloudasset.assets.listRunRevision` `cloudasset.assets.listRunService` `cloudasset.assets.listSecretManagerSecretVersions` `cloudasset.assets.listSecretManagerSecrets` `cloudasset.assets.listServiceDirectoryNamespaces` `cloudasset.assets.listServicePerimeter` `cloudasset.assets.listServiceconsumermanagementConsumerProperty` `cloudasset.assets.listServiceconsumermanagementConsumerQuotaLimits` `cloudasset.assets.listServiceconsumermanagementConsumers` `cloudasset.assets.listServiceconsumermanagementProducerOverrides` `cloudasset.assets.listServiceconsumermanagementTenancyUnits` `cloudasset.assets.listServiceconsumermanagementVisibility` `cloudasset.assets.listServicemanagementServices` `cloudasset.assets.listServiceusageAdminOverrides` `cloudasset.assets.listServiceusageConsumerOverrides` `cloudasset.assets.listServiceusageServices` `cloudasset.assets.listSpannerBackups` `cloudasset.assets.listSpannerDatabases` `cloudasset.assets.listSpannerInstances` `cloudasset.assets.listSpeakerIdPhrases` `cloudasset.assets.listSpeakerIdSettings` `cloudasset.assets.listSpeakerIdSpeakers` `cloudasset.assets.listSpeechCustomClasses` `cloudasset.assets.listSpeechPhraseSets` `cloudasset.assets.listSqladminBackupRuns` `cloudasset.assets.listSqladminInstances` `cloudasset.assets.listStorageBuckets` `cloudasset.assets.listTpuNodes` `cloudasset.assets.listVpcaccessConnector` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.feeds.*`

  * `cloudasset.feeds.create`
  * `cloudasset.feeds.delete`
  * `cloudasset.feeds.get`
  * `cloudasset.feeds.list`
  * `cloudasset.feeds.update`

`cloudasset.othercloudconnections.get` `cloudasset.othercloudconnections.list` `cloudasset.othercloudconnections.verify` `cloudasset.savedqueries.get` `cloudasset.savedqueries.list` `cloudsql.instances.connect` `cloudsql.users.list` `compute.disks.useReadOnly` `compute.globalOperations.get` `compute.instances.get` `compute.instances.list` `compute.networkEndpointGroups.get` `compute.projects.get` `compute.regionOperations.get` `compute.zoneOperations.get` `container.clusters.get` `iam.denypolicies.get` `iam.denypolicies.list` `iam.googleapis.com/workloadIdentityPoolProviders.list` `iam.googleapis.com/workloadIdentityPools.list` `logging.logEntries.list` `monitoring.alertPolicies.list` `monitoring.timeSeries.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `recommender.cloudAssetInsights.get` `recommender.cloudAssetInsights.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `resourcemanager.tagValues.get` `securitycenter.assets.list` `securitycenter.assetsecuritymarks.update` `securitycenter.findings.list` `securitycenter.notificationconfig.create` `securitycenter.notificationconfig.delete` `securitycenter.notificationconfig.update` `securitycenter.organizationsettings.get` `securitycenter.resourcevalueconfigs.get` `securitycenter.resourcevalueconfigs.list` `securitycenter.simulations.get` `securitycenter.sources.list` `securitycenter.valuedresources.list` `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.securityHealthAnalyticsCustomModules.create` `securitycentermanagement.securityHealthAnalyticsCustomModules.delete` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.update` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.disable` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list`  
  
#### Security Center Integration Executor Service Agent 

(`roles/securitycenter.integrationExecutorServiceAgent`) Gives Security Center access to execute Integrations.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `integrations.securityExecutions.cancel` `integrations.securityExecutions.list` `integrations.securityIntegrations.invoke`  
  
#### Security Center Notification Service Agent 

(`roles/securitycenter.notificationServiceAgent`) Security Center service agent can publish notifications to Pub/Sub topics.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `pubsub.topics.publish`  
  
#### Security Health Analytics Service Agent 

(`roles/securitycenter.securityHealthAnalyticsServiceAgent`) Security Health Analytics service agent can scan GCP resource metadata to find security vulnerabilities.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.get` `binaryauthorization.policy.get` `cloudasset.assets.analyzeIamPolicy` `cloudasset.assets.analyzeMove` `cloudasset.assets.analyzeOrgPolicy` `cloudasset.assets.exportAccessLevel` `cloudasset.assets.exportAccessPolicy` `cloudasset.assets.exportAiplatformBatchPredictionJobs` `cloudasset.assets.exportAiplatformCustomJobs` `cloudasset.assets.exportAiplatformDataLabelingJobs` `cloudasset.assets.exportAiplatformDatasets` `cloudasset.assets.exportAiplatformEndpoints` `cloudasset.assets.exportAiplatformHyperparameterTuningJobs` `cloudasset.assets.exportAiplatformMetadataStores` `cloudasset.assets.exportAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.exportAiplatformModels` `cloudasset.assets.exportAiplatformPipelineJobs` `cloudasset.assets.exportAiplatformSpecialistPools` `cloudasset.assets.exportAiplatformTrainingPipelines` `cloudasset.assets.exportAllAccessPolicy` `cloudasset.assets.exportAnthosConnectedCluster` `cloudasset.assets.exportAnthosedgeCluster` `cloudasset.assets.exportApigatewayApi` `cloudasset.assets.exportApigatewayApiConfig` `cloudasset.assets.exportApigatewayGateway` `cloudasset.assets.exportApikeysKeys` `cloudasset.assets.exportAppengineApplications` `cloudasset.assets.exportAppengineServices` `cloudasset.assets.exportAppengineVersions` `cloudasset.assets.exportArtifactregistryDockerImages` `cloudasset.assets.exportArtifactregistryRepositories` `cloudasset.assets.exportAssuredWorkloadsWorkloads` `cloudasset.assets.exportBeyondCorpApiGateways` `cloudasset.assets.exportBeyondCorpAppConnections` `cloudasset.assets.exportBeyondCorpAppConnectors` `cloudasset.assets.exportBeyondCorpAppGateways` `cloudasset.assets.exportBeyondCorpClientConnectorServices` `cloudasset.assets.exportBeyondCorpClientGateways` `cloudasset.assets.exportBigqueryDatasets` `cloudasset.assets.exportBigqueryModels` `cloudasset.assets.exportBigqueryTables` `cloudasset.assets.exportBigtableAppProfile` `cloudasset.assets.exportBigtableBackup` `cloudasset.assets.exportBigtableCluster` `cloudasset.assets.exportBigtableInstance` `cloudasset.assets.exportBigtableTable` `cloudasset.assets.exportCloudAssetFeeds` `cloudasset.assets.exportCloudDeployDeliveryPipelines` `cloudasset.assets.exportCloudDeployReleases` `cloudasset.assets.exportCloudDeployRollouts` `cloudasset.assets.exportCloudDeployTargets` `cloudasset.assets.exportCloudDocumentAIEvaluation` `cloudasset.assets.exportCloudDocumentAIHumanReviewConfig` `cloudasset.assets.exportCloudDocumentAILabelerPool` `cloudasset.assets.exportCloudDocumentAIProcessor` `cloudasset.assets.exportCloudDocumentAIProcessorVersion` `cloudasset.assets.exportCloudbillingBillingAccounts` `cloudasset.assets.exportCloudbillingProjectBillingInfos` `cloudasset.assets.exportCloudfunctionsFunctions` `cloudasset.assets.exportCloudfunctionsGen2Functions` `cloudasset.assets.exportCloudkmsCryptoKeyVersions` `cloudasset.assets.exportCloudkmsCryptoKeys` `cloudasset.assets.exportCloudkmsEkmConnections` `cloudasset.assets.exportCloudkmsImportJobs` `cloudasset.assets.exportCloudkmsKeyRings` `cloudasset.assets.exportCloudmemcacheInstances` `cloudasset.assets.exportCloudresourcemanagerFolders` `cloudasset.assets.exportCloudresourcemanagerOrganizations` `cloudasset.assets.exportCloudresourcemanagerProjects` `cloudasset.assets.exportCloudresourcemanagerTagBindings` `cloudasset.assets.exportCloudresourcemanagerTagKeys` `cloudasset.assets.exportCloudresourcemanagerTagValues` `cloudasset.assets.exportComposerEnvironments` `cloudasset.assets.exportComputeAddress` `cloudasset.assets.exportComputeAutoscalers` `cloudasset.assets.exportComputeBackendBuckets` `cloudasset.assets.exportComputeBackendServices` `cloudasset.assets.exportComputeCommitments` `cloudasset.assets.exportComputeDisks` `cloudasset.assets.exportComputeExternalVpnGateways` `cloudasset.assets.exportComputeFirewallPolicies` `cloudasset.assets.exportComputeFirewalls` `cloudasset.assets.exportComputeForwardingRules` `cloudasset.assets.exportComputeGlobalAddress` `cloudasset.assets.exportComputeGlobalForwardingRules` `cloudasset.assets.exportComputeHealthChecks` `cloudasset.assets.exportComputeHttpHealthChecks` `cloudasset.assets.exportComputeHttpsHealthChecks` `cloudasset.assets.exportComputeImages` `cloudasset.assets.exportComputeInstanceGroupManagers` `cloudasset.assets.exportComputeInstanceGroups` `cloudasset.assets.exportComputeInstanceTemplates` `cloudasset.assets.exportComputeInstances` `cloudasset.assets.exportComputeInterconnect` `cloudasset.assets.exportComputeInterconnectAttachment` `cloudasset.assets.exportComputeLicenses` `cloudasset.assets.exportComputeNetworkEndpointGroups` `cloudasset.assets.exportComputeNetworks` `cloudasset.assets.exportComputeNodeGroups` `cloudasset.assets.exportComputeNodeTemplates` `cloudasset.assets.exportComputePacketMirrorings` `cloudasset.assets.exportComputeProjects` `cloudasset.assets.exportComputeRegionAutoscaler` `cloudasset.assets.exportComputeRegionBackendServices` `cloudasset.assets.exportComputeRegionDisk` `cloudasset.assets.exportComputeRegionInstanceGroup` `cloudasset.assets.exportComputeRegionInstanceGroupManager` `cloudasset.assets.exportComputeReservations` `cloudasset.assets.exportComputeResourcePolicies` `cloudasset.assets.exportComputeRouters` `cloudasset.assets.exportComputeRoutes` `cloudasset.assets.exportComputeSecurityPolicy` `cloudasset.assets.exportComputeServiceAttachments` `cloudasset.assets.exportComputeSnapshots` `cloudasset.assets.exportComputeSslCertificates` `cloudasset.assets.exportComputeSslPolicies` `cloudasset.assets.exportComputeSubnetworks` `cloudasset.assets.exportComputeTargetHttpProxies` `cloudasset.assets.exportComputeTargetHttpsProxies` `cloudasset.assets.exportComputeTargetInstances` `cloudasset.assets.exportComputeTargetPools` `cloudasset.assets.exportComputeTargetSslProxies` `cloudasset.assets.exportComputeTargetTcpProxies` `cloudasset.assets.exportComputeTargetVpnGateways` `cloudasset.assets.exportComputeUrlMaps` `cloudasset.assets.exportComputeVpnGateways` `cloudasset.assets.exportComputeVpnTunnels` `cloudasset.assets.exportConnectorsConnections` `cloudasset.assets.exportConnectorsConnectorVersions` `cloudasset.assets.exportConnectorsConnectors` `cloudasset.assets.exportConnectorsProviders` `cloudasset.assets.exportConnectorsRuntimeConfigs` `cloudasset.assets.exportContainerAppsDeployment` `cloudasset.assets.exportContainerAppsReplicaSets` `cloudasset.assets.exportContainerBatchJobs` `cloudasset.assets.exportContainerClusterrole` `cloudasset.assets.exportContainerClusterrolebinding` `cloudasset.assets.exportContainerClusters` `cloudasset.assets.exportContainerExtensionsIngresses` `cloudasset.assets.exportContainerJobs` `cloudasset.assets.exportContainerNamespace` `cloudasset.assets.exportContainerNetworkingIngresses` `cloudasset.assets.exportContainerNetworkingNetworkPolicies` `cloudasset.assets.exportContainerNode` `cloudasset.assets.exportContainerNodepool` `cloudasset.assets.exportContainerPod` `cloudasset.assets.exportContainerReplicaSets` `cloudasset.assets.exportContainerRole` `cloudasset.assets.exportContainerRolebinding` `cloudasset.assets.exportContainerServices` `cloudasset.assets.exportContainerregistryImage` `cloudasset.assets.exportDataMigrationConnectionProfiles` `cloudasset.assets.exportDataMigrationMigrationJobs` `cloudasset.assets.exportDataflowJobs` `cloudasset.assets.exportDatafusionInstance` `cloudasset.assets.exportDataplexAssets` `cloudasset.assets.exportDataplexLakes` `cloudasset.assets.exportDataplexTasks` `cloudasset.assets.exportDataplexZones` `cloudasset.assets.exportDataprocAutoscalingPolicies` `cloudasset.assets.exportDataprocBatches` `cloudasset.assets.exportDataprocClusters` `cloudasset.assets.exportDataprocJobs` `cloudasset.assets.exportDataprocSessions` `cloudasset.assets.exportDataprocWorkflowTemplates` `cloudasset.assets.exportDatastreamConnectionProfile` `cloudasset.assets.exportDatastreamPrivateConnection` `cloudasset.assets.exportDatastreamStream` `cloudasset.assets.exportDialogflowAgents` `cloudasset.assets.exportDialogflowConversationProfiles` `cloudasset.assets.exportDialogflowKnowledgeBases` `cloudasset.assets.exportDialogflowLocationSettings` `cloudasset.assets.exportDlpDeidentifyTemplates` `cloudasset.assets.exportDlpDlpJobs` `cloudasset.assets.exportDlpInspectTemplates` `cloudasset.assets.exportDlpJobTriggers` `cloudasset.assets.exportDlpStoredInfoTypes` `cloudasset.assets.exportDnsManagedZones` `cloudasset.assets.exportDnsPolicies` `cloudasset.assets.exportDomainsRegistrations` `cloudasset.assets.exportEventarcTriggers` `cloudasset.assets.exportFileBackups` `cloudasset.assets.exportFileInstances` `cloudasset.assets.exportFirebaseAppInfos` `cloudasset.assets.exportFirebaseProjects` `cloudasset.assets.exportFirestoreDatabases` `cloudasset.assets.exportGKEHubFeatures` `cloudasset.assets.exportGKEHubMemberships` `cloudasset.assets.exportGameservicesGameServerClusters` `cloudasset.assets.exportGameservicesGameServerConfigs` `cloudasset.assets.exportGameservicesGameServerDeployments` `cloudasset.assets.exportGameservicesRealms` `cloudasset.assets.exportGkeBackupBackupPlans` `cloudasset.assets.exportGkeBackupBackups` `cloudasset.assets.exportGkeBackupRestorePlans` `cloudasset.assets.exportGkeBackupRestores` `cloudasset.assets.exportGkeBackupVolumeBackups` `cloudasset.assets.exportGkeBackupVolumeRestores` `cloudasset.assets.exportHealthcareConsentStores` `cloudasset.assets.exportHealthcareDatasets` `cloudasset.assets.exportHealthcareDicomStores` `cloudasset.assets.exportHealthcareFhirStores` `cloudasset.assets.exportHealthcareHl7V2Stores` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportIamRoles` `cloudasset.assets.exportIamServiceAccountKeys` `cloudasset.assets.exportIamServiceAccounts` `cloudasset.assets.exportIapTunnel` `cloudasset.assets.exportIapTunnelInstances` `cloudasset.assets.exportIapTunnelZones` `cloudasset.assets.exportIapWeb` `cloudasset.assets.exportIapWebServiceVersion` `cloudasset.assets.exportIapWebServices` `cloudasset.assets.exportIapWebType` `cloudasset.assets.exportIdsEndpoints` `cloudasset.assets.exportIntegrationsAuthConfigs` `cloudasset.assets.exportIntegrationsCertificates` `cloudasset.assets.exportIntegrationsExecutions` `cloudasset.assets.exportIntegrationsIntegrationVersions` `cloudasset.assets.exportIntegrationsIntegrations` `cloudasset.assets.exportIntegrationsSfdcChannels` `cloudasset.assets.exportIntegrationsSfdcInstances` `cloudasset.assets.exportIntegrationsSuspensions` `cloudasset.assets.exportLoggingLogMetrics` `cloudasset.assets.exportLoggingLogSinks` `cloudasset.assets.exportManagedidentitiesDomain` `cloudasset.assets.exportMetastoreBackups` `cloudasset.assets.exportMetastoreMetadataImports` `cloudasset.assets.exportMetastoreServices` `cloudasset.assets.exportMonitoringAlertPolicies` `cloudasset.assets.exportNetworkConnectivityHubs` `cloudasset.assets.exportNetworkConnectivitySpokes` `cloudasset.assets.exportNetworkManagementConnectivityTests` `cloudasset.assets.exportNetworkServicesEndpointPolicies` `cloudasset.assets.exportNetworkServicesGateways` `cloudasset.assets.exportNetworkServicesGrpcRoutes` `cloudasset.assets.exportNetworkServicesHttpRoutes` `cloudasset.assets.exportNetworkServicesMeshes` `cloudasset.assets.exportNetworkServicesServiceBindings` `cloudasset.assets.exportNetworkServicesTcpRoutes` `cloudasset.assets.exportNetworkServicesTlsRoutes` `cloudasset.assets.exportOSConfigOSPolicyAssignmentReports` `cloudasset.assets.exportOSConfigOSPolicyAssignments` `cloudasset.assets.exportOSConfigVulnerabilityReports` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportOrgPolicy` `cloudasset.assets.exportPatchDeployments` `cloudasset.assets.exportPubsubSnapshots` `cloudasset.assets.exportPubsubSubscriptions` `cloudasset.assets.exportPubsubTopics` `cloudasset.assets.exportRedisInstances` `cloudasset.assets.exportResource` `cloudasset.assets.exportSecretManagerSecretVersions` `cloudasset.assets.exportSecretManagerSecrets` `cloudasset.assets.exportServiceDirectoryNamespaces` `cloudasset.assets.exportServicePerimeter` `cloudasset.assets.exportServiceconsumermanagementConsumerProperty` `cloudasset.assets.exportServiceconsumermanagementConsumerQuotaLimits` `cloudasset.assets.exportServiceconsumermanagementConsumers` `cloudasset.assets.exportServiceconsumermanagementProducerOverrides` `cloudasset.assets.exportServiceconsumermanagementTenancyUnits` `cloudasset.assets.exportServiceconsumermanagementVisibility` `cloudasset.assets.exportServicemanagementServices` `cloudasset.assets.exportServiceusageAdminOverrides` `cloudasset.assets.exportServiceusageConsumerOverrides` `cloudasset.assets.exportServiceusageServices` `cloudasset.assets.exportSpannerBackups` `cloudasset.assets.exportSpannerDatabases` `cloudasset.assets.exportSpannerInstances` `cloudasset.assets.exportSpeakerIdPhrases` `cloudasset.assets.exportSpeakerIdSettings` `cloudasset.assets.exportSpeakerIdSpeakers` `cloudasset.assets.exportSpeechCustomClasses` `cloudasset.assets.exportSpeechPhraseSets` `cloudasset.assets.exportSqladminBackupRuns` `cloudasset.assets.exportSqladminInstances` `cloudasset.assets.exportStorageBuckets` `cloudasset.assets.exportTpuNodes` `cloudasset.assets.exportVpcaccessConnector` `cloudasset.assets.listAccessLevel` `cloudasset.assets.listAccessPolicy` `cloudasset.assets.listAiplatformBatchPredictionJobs` `cloudasset.assets.listAiplatformCustomJobs` `cloudasset.assets.listAiplatformDataLabelingJobs` `cloudasset.assets.listAiplatformDatasets` `cloudasset.assets.listAiplatformEndpoints` `cloudasset.assets.listAiplatformHyperparameterTuningJobs` `cloudasset.assets.listAiplatformMetadataStores` `cloudasset.assets.listAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.listAiplatformModels` `cloudasset.assets.listAiplatformPipelineJobs` `cloudasset.assets.listAiplatformSpecialistPools` `cloudasset.assets.listAiplatformTrainingPipelines` `cloudasset.assets.listAllAccessPolicy` `cloudasset.assets.listAnthosConnectedCluster` `cloudasset.assets.listAnthosedgeCluster` `cloudasset.assets.listApigatewayApi` `cloudasset.assets.listApigatewayApiConfig` `cloudasset.assets.listApigatewayGateway` `cloudasset.assets.listApikeysKeys` `cloudasset.assets.listAppengineApplications` `cloudasset.assets.listAppengineServices` `cloudasset.assets.listAppengineVersions` `cloudasset.assets.listArtifactregistryDockerImages` `cloudasset.assets.listArtifactregistryRepositories` `cloudasset.assets.listAssuredWorkloadsWorkloads` `cloudasset.assets.listBeyondCorpApiGateways` `cloudasset.assets.listBeyondCorpAppConnections` `cloudasset.assets.listBeyondCorpAppConnectors` `cloudasset.assets.listBeyondCorpAppGateways` `cloudasset.assets.listBeyondCorpClientConnectorServices` `cloudasset.assets.listBeyondCorpClientGateways` `cloudasset.assets.listBigqueryDatasets` `cloudasset.assets.listBigqueryModels` `cloudasset.assets.listBigqueryTables` `cloudasset.assets.listBigtableAppProfile` `cloudasset.assets.listBigtableBackup` `cloudasset.assets.listBigtableCluster` `cloudasset.assets.listBigtableInstance` `cloudasset.assets.listBigtableTable` `cloudasset.assets.listCloudAssetFeeds` `cloudasset.assets.listCloudDeployDeliveryPipelines` `cloudasset.assets.listCloudDeployReleases` `cloudasset.assets.listCloudDeployRollouts` `cloudasset.assets.listCloudDeployTargets` `cloudasset.assets.listCloudDocumentAIEvaluation` `cloudasset.assets.listCloudDocumentAIHumanReviewConfig` `cloudasset.assets.listCloudDocumentAILabelerPool` `cloudasset.assets.listCloudDocumentAIProcessor` `cloudasset.assets.listCloudDocumentAIProcessorVersion` `cloudasset.assets.listCloudbillingBillingAccounts` `cloudasset.assets.listCloudbillingProjectBillingInfos` `cloudasset.assets.listCloudfunctionsFunctions` `cloudasset.assets.listCloudfunctionsGen2Functions` `cloudasset.assets.listCloudkmsCryptoKeyVersions` `cloudasset.assets.listCloudkmsCryptoKeys` `cloudasset.assets.listCloudkmsEkmConnections` `cloudasset.assets.listCloudkmsImportJobs` `cloudasset.assets.listCloudkmsKeyRings` `cloudasset.assets.listCloudmemcacheInstances` `cloudasset.assets.listCloudresourcemanagerFolders` `cloudasset.assets.listCloudresourcemanagerOrganizations` `cloudasset.assets.listCloudresourcemanagerProjects` `cloudasset.assets.listCloudresourcemanagerTagBindings` `cloudasset.assets.listCloudresourcemanagerTagKeys` `cloudasset.assets.listCloudresourcemanagerTagValues` `cloudasset.assets.listComposerEnvironments` `cloudasset.assets.listComputeAddress` `cloudasset.assets.listComputeAutoscalers` `cloudasset.assets.listComputeBackendBuckets` `cloudasset.assets.listComputeBackendServices` `cloudasset.assets.listComputeCommitments` `cloudasset.assets.listComputeDisks` `cloudasset.assets.listComputeExternalVpnGateways` `cloudasset.assets.listComputeFirewallPolicies` `cloudasset.assets.listComputeFirewalls` `cloudasset.assets.listComputeForwardingRules` `cloudasset.assets.listComputeGlobalAddress` `cloudasset.assets.listComputeGlobalForwardingRules` `cloudasset.assets.listComputeHealthChecks` `cloudasset.assets.listComputeHttpHealthChecks` `cloudasset.assets.listComputeHttpsHealthChecks` `cloudasset.assets.listComputeImages` `cloudasset.assets.listComputeInstanceGroupManagers` `cloudasset.assets.listComputeInstanceGroups` `cloudasset.assets.listComputeInstanceTemplates` `cloudasset.assets.listComputeInstances` `cloudasset.assets.listComputeInterconnect` `cloudasset.assets.listComputeInterconnectAttachment` `cloudasset.assets.listComputeLicenses` `cloudasset.assets.listComputeNetworkEndpointGroups` `cloudasset.assets.listComputeNetworks` `cloudasset.assets.listComputeNodeGroups` `cloudasset.assets.listComputeNodeTemplates` `cloudasset.assets.listComputePacketMirrorings` `cloudasset.assets.listComputeProjects` `cloudasset.assets.listComputeRegionAutoscaler` `cloudasset.assets.listComputeRegionBackendServices` `cloudasset.assets.listComputeRegionDisk` `cloudasset.assets.listComputeRegionInstanceGroup` `cloudasset.assets.listComputeRegionInstanceGroupManager` `cloudasset.assets.listComputeReservations` `cloudasset.assets.listComputeResourcePolicies` `cloudasset.assets.listComputeRouters` `cloudasset.assets.listComputeRoutes` `cloudasset.assets.listComputeSecurityPolicy` `cloudasset.assets.listComputeServiceAttachments` `cloudasset.assets.listComputeSnapshots` `cloudasset.assets.listComputeSslCertificates` `cloudasset.assets.listComputeSslPolicies` `cloudasset.assets.listComputeSubnetworks` `cloudasset.assets.listComputeTargetHttpProxies` `cloudasset.assets.listComputeTargetHttpsProxies` `cloudasset.assets.listComputeTargetInstances` `cloudasset.assets.listComputeTargetPools` `cloudasset.assets.listComputeTargetSslProxies` `cloudasset.assets.listComputeTargetTcpProxies` `cloudasset.assets.listComputeTargetVpnGateways` `cloudasset.assets.listComputeUrlMaps` `cloudasset.assets.listComputeVpnGateways` `cloudasset.assets.listComputeVpnTunnels` `cloudasset.assets.listConnectorsConnections` `cloudasset.assets.listConnectorsConnectorVersions` `cloudasset.assets.listConnectorsConnectors` `cloudasset.assets.listConnectorsProviders` `cloudasset.assets.listConnectorsRuntimeConfigs` `cloudasset.assets.listContainerAppsDeployment` `cloudasset.assets.listContainerAppsReplicaSets` `cloudasset.assets.listContainerBatchJobs` `cloudasset.assets.listContainerClusterrole` `cloudasset.assets.listContainerClusterrolebinding` `cloudasset.assets.listContainerClusters` `cloudasset.assets.listContainerExtensionsIngresses` `cloudasset.assets.listContainerJobs` `cloudasset.assets.listContainerNamespace` `cloudasset.assets.listContainerNetworkingIngresses` `cloudasset.assets.listContainerNetworkingNetworkPolicies` `cloudasset.assets.listContainerNode` `cloudasset.assets.listContainerNodepool` `cloudasset.assets.listContainerPod` `cloudasset.assets.listContainerReplicaSets` `cloudasset.assets.listContainerRole` `cloudasset.assets.listContainerRolebinding` `cloudasset.assets.listContainerServices` `cloudasset.assets.listContainerregistryImage` `cloudasset.assets.listDataMigrationConnectionProfiles` `cloudasset.assets.listDataMigrationMigrationJobs` `cloudasset.assets.listDataflowJobs` `cloudasset.assets.listDatafusionInstance` `cloudasset.assets.listDataplexAssets` `cloudasset.assets.listDataplexLakes` `cloudasset.assets.listDataplexTasks` `cloudasset.assets.listDataplexZones` `cloudasset.assets.listDataprocAutoscalingPolicies` `cloudasset.assets.listDataprocBatches` `cloudasset.assets.listDataprocClusters` `cloudasset.assets.listDataprocJobs` `cloudasset.assets.listDataprocSessions` `cloudasset.assets.listDataprocWorkflowTemplates` `cloudasset.assets.listDatastreamConnectionProfile` `cloudasset.assets.listDatastreamPrivateConnection` `cloudasset.assets.listDatastreamStream` `cloudasset.assets.listDialogflowAgents` `cloudasset.assets.listDialogflowConversationProfiles` `cloudasset.assets.listDialogflowKnowledgeBases` `cloudasset.assets.listDialogflowLocationSettings` `cloudasset.assets.listDlpDeidentifyTemplates` `cloudasset.assets.listDlpDlpJobs` `cloudasset.assets.listDlpInspectTemplates` `cloudasset.assets.listDlpJobTriggers` `cloudasset.assets.listDlpStoredInfoTypes` `cloudasset.assets.listDnsManagedZones` `cloudasset.assets.listDnsPolicies` `cloudasset.assets.listDomainsRegistrations` `cloudasset.assets.listEventarcTriggers` `cloudasset.assets.listFileBackups` `cloudasset.assets.listFileInstances` `cloudasset.assets.listFirebaseAppInfos` `cloudasset.assets.listFirebaseProjects` `cloudasset.assets.listFirestoreDatabases` `cloudasset.assets.listGKEHubFeatures` `cloudasset.assets.listGKEHubMemberships` `cloudasset.assets.listGameservicesGameServerClusters` `cloudasset.assets.listGameservicesGameServerConfigs` `cloudasset.assets.listGameservicesGameServerDeployments` `cloudasset.assets.listGameservicesRealms` `cloudasset.assets.listGkeBackupBackupPlans` `cloudasset.assets.listGkeBackupBackups` `cloudasset.assets.listGkeBackupRestorePlans` `cloudasset.assets.listGkeBackupRestores` `cloudasset.assets.listGkeBackupVolumeBackups` `cloudasset.assets.listGkeBackupVolumeRestores` `cloudasset.assets.listHealthcareConsentStores` `cloudasset.assets.listHealthcareDatasets` `cloudasset.assets.listHealthcareDicomStores` `cloudasset.assets.listHealthcareFhirStores` `cloudasset.assets.listHealthcareHl7V2Stores` `cloudasset.assets.listIamPolicy` `cloudasset.assets.listIamRoles` `cloudasset.assets.listIamServiceAccountKeys` `cloudasset.assets.listIamServiceAccounts` `cloudasset.assets.listIapTunnel` `cloudasset.assets.listIapTunnelInstances` `cloudasset.assets.listIapTunnelZones` `cloudasset.assets.listIapWeb` `cloudasset.assets.listIapWebServiceVersion` `cloudasset.assets.listIapWebServices` `cloudasset.assets.listIapWebType` `cloudasset.assets.listIdsEndpoints` `cloudasset.assets.listIntegrationsAuthConfigs` `cloudasset.assets.listIntegrationsCertificates` `cloudasset.assets.listIntegrationsExecutions` `cloudasset.assets.listIntegrationsIntegrationVersions` `cloudasset.assets.listIntegrationsIntegrations` `cloudasset.assets.listIntegrationsSfdcChannels` `cloudasset.assets.listIntegrationsSfdcInstances` `cloudasset.assets.listIntegrationsSuspensions` `cloudasset.assets.listLoggingLogMetrics` `cloudasset.assets.listLoggingLogSinks` `cloudasset.assets.listManagedidentitiesDomain` `cloudasset.assets.listMetastoreBackups` `cloudasset.assets.listMetastoreMetadataImports` `cloudasset.assets.listMetastoreServices` `cloudasset.assets.listMonitoringAlertPolicies` `cloudasset.assets.listNetworkConnectivityHubs` `cloudasset.assets.listNetworkConnectivitySpokes` `cloudasset.assets.listNetworkManagementConnectivityTests` `cloudasset.assets.listNetworkServicesEndpointPolicies` `cloudasset.assets.listNetworkServicesGateways` `cloudasset.assets.listNetworkServicesGrpcRoutes` `cloudasset.assets.listNetworkServicesHttpRoutes` `cloudasset.assets.listNetworkServicesMeshes` `cloudasset.assets.listNetworkServicesServiceBindings` `cloudasset.assets.listNetworkServicesTcpRoutes` `cloudasset.assets.listNetworkServicesTlsRoutes` `cloudasset.assets.listOSConfigOSPolicyAssignmentReports` `cloudasset.assets.listOSConfigOSPolicyAssignments` `cloudasset.assets.listOSConfigVulnerabilityReports` `cloudasset.assets.listOSInventories` `cloudasset.assets.listOrgPolicy` `cloudasset.assets.listPatchDeployments` `cloudasset.assets.listPubsubSnapshots` `cloudasset.assets.listPubsubSubscriptions` `cloudasset.assets.listPubsubTopics` `cloudasset.assets.listRedisInstances` `cloudasset.assets.listResource` `cloudasset.assets.listRunDomainMapping` `cloudasset.assets.listRunRevision` `cloudasset.assets.listRunService` `cloudasset.assets.listSecretManagerSecretVersions` `cloudasset.assets.listSecretManagerSecrets` `cloudasset.assets.listServiceDirectoryNamespaces` `cloudasset.assets.listServicePerimeter` `cloudasset.assets.listServiceconsumermanagementConsumerProperty` `cloudasset.assets.listServiceconsumermanagementConsumerQuotaLimits` `cloudasset.assets.listServiceconsumermanagementConsumers` `cloudasset.assets.listServiceconsumermanagementProducerOverrides` `cloudasset.assets.listServiceconsumermanagementTenancyUnits` `cloudasset.assets.listServiceconsumermanagementVisibility` `cloudasset.assets.listServicemanagementServices` `cloudasset.assets.listServiceusageAdminOverrides` `cloudasset.assets.listServiceusageConsumerOverrides` `cloudasset.assets.listServiceusageServices` `cloudasset.assets.listSpannerBackups` `cloudasset.assets.listSpannerDatabases` `cloudasset.assets.listSpannerInstances` `cloudasset.assets.listSpeakerIdPhrases` `cloudasset.assets.listSpeakerIdSettings` `cloudasset.assets.listSpeakerIdSpeakers` `cloudasset.assets.listSpeechCustomClasses` `cloudasset.assets.listSpeechPhraseSets` `cloudasset.assets.listSqladminBackupRuns` `cloudasset.assets.listSqladminInstances` `cloudasset.assets.listStorageBuckets` `cloudasset.assets.listTpuNodes` `cloudasset.assets.listVpcaccessConnector` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.feeds.*`

  * `cloudasset.feeds.create`
  * `cloudasset.feeds.delete`
  * `cloudasset.feeds.get`
  * `cloudasset.feeds.list`
  * `cloudasset.feeds.update`

`cloudasset.othercloudconnections.get` `cloudasset.othercloudconnections.list` `cloudasset.othercloudconnections.verify` `cloudasset.savedqueries.get` `cloudasset.savedqueries.list` `cloudsql.instances.connect` `cloudsql.users.list` `compute.globalOperations.get` `compute.instances.get` `compute.instances.list` `compute.networkEndpointGroups.get` `compute.projects.get` `container.clusters.get` `monitoring.alertPolicies.list` `orgpolicy.policy.get` `recommender.cloudAssetInsights.get` `recommender.cloudAssetInsights.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.organizationsettings.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get`  
  
#### Google Cloud Security Response Service Agent 

(`roles/securitycenter.securityResponseServiceAgent`) Gives Playbook Runner permissions to execute all Google authored Playbooks. This role will keep evolving as we add more playbooks  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.globalOperations.get` `compute.instances.deleteAccessConfig` `compute.instances.get` `compute.instances.setMetadata` `compute.regionOperations.get` `compute.zoneOperations.get` `iam.serviceAccounts.actAs` `pubsub.topics.publish` `securitycenter.findings.list` `storage.buckets.get` `storage.buckets.update`  
  
#### Security Center Service Agent 

(`roles/securitycenter.serviceAgent`) Security Center service agent can scan GCP resources and import security scans.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `accesscontextmanager.gcpUserAccessBindings.get` `accesscontextmanager.gcpUserAccessBindings.list` `aiplatform.dataItems.list` `aiplatform.datasets.list` `aiplatform.models.list` `bigquery.datasets.get` `binaryauthorization.policy.get` `cloudasset.assets.analyzeIamPolicy` `cloudasset.assets.analyzeMove` `cloudasset.assets.analyzeOrgPolicy` `cloudasset.assets.exportAccessLevel` `cloudasset.assets.exportAccessPolicy` `cloudasset.assets.exportAiplatformBatchPredictionJobs` `cloudasset.assets.exportAiplatformCustomJobs` `cloudasset.assets.exportAiplatformDataLabelingJobs` `cloudasset.assets.exportAiplatformDatasets` `cloudasset.assets.exportAiplatformEndpoints` `cloudasset.assets.exportAiplatformHyperparameterTuningJobs` `cloudasset.assets.exportAiplatformMetadataStores` `cloudasset.assets.exportAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.exportAiplatformModels` `cloudasset.assets.exportAiplatformPipelineJobs` `cloudasset.assets.exportAiplatformSpecialistPools` `cloudasset.assets.exportAiplatformTrainingPipelines` `cloudasset.assets.exportAllAccessPolicy` `cloudasset.assets.exportAnthosConnectedCluster` `cloudasset.assets.exportAnthosedgeCluster` `cloudasset.assets.exportApigatewayApi` `cloudasset.assets.exportApigatewayApiConfig` `cloudasset.assets.exportApigatewayGateway` `cloudasset.assets.exportApikeysKeys` `cloudasset.assets.exportAppengineApplications` `cloudasset.assets.exportAppengineServices` `cloudasset.assets.exportAppengineVersions` `cloudasset.assets.exportArtifactregistryDockerImages` `cloudasset.assets.exportArtifactregistryRepositories` `cloudasset.assets.exportAssuredWorkloadsWorkloads` `cloudasset.assets.exportBeyondCorpApiGateways` `cloudasset.assets.exportBeyondCorpAppConnections` `cloudasset.assets.exportBeyondCorpAppConnectors` `cloudasset.assets.exportBeyondCorpAppGateways` `cloudasset.assets.exportBeyondCorpClientConnectorServices` `cloudasset.assets.exportBeyondCorpClientGateways` `cloudasset.assets.exportBigqueryDatasets` `cloudasset.assets.exportBigqueryModels` `cloudasset.assets.exportBigqueryTables` `cloudasset.assets.exportBigtableAppProfile` `cloudasset.assets.exportBigtableBackup` `cloudasset.assets.exportBigtableCluster` `cloudasset.assets.exportBigtableInstance` `cloudasset.assets.exportBigtableTable` `cloudasset.assets.exportCloudAssetFeeds` `cloudasset.assets.exportCloudDeployDeliveryPipelines` `cloudasset.assets.exportCloudDeployReleases` `cloudasset.assets.exportCloudDeployRollouts` `cloudasset.assets.exportCloudDeployTargets` `cloudasset.assets.exportCloudDocumentAIEvaluation` `cloudasset.assets.exportCloudDocumentAIHumanReviewConfig` `cloudasset.assets.exportCloudDocumentAILabelerPool` `cloudasset.assets.exportCloudDocumentAIProcessor` `cloudasset.assets.exportCloudDocumentAIProcessorVersion` `cloudasset.assets.exportCloudbillingBillingAccounts` `cloudasset.assets.exportCloudbillingProjectBillingInfos` `cloudasset.assets.exportCloudfunctionsFunctions` `cloudasset.assets.exportCloudfunctionsGen2Functions` `cloudasset.assets.exportCloudkmsCryptoKeyVersions` `cloudasset.assets.exportCloudkmsCryptoKeys` `cloudasset.assets.exportCloudkmsEkmConnections` `cloudasset.assets.exportCloudkmsImportJobs` `cloudasset.assets.exportCloudkmsKeyRings` `cloudasset.assets.exportCloudmemcacheInstances` `cloudasset.assets.exportCloudresourcemanagerFolders` `cloudasset.assets.exportCloudresourcemanagerOrganizations` `cloudasset.assets.exportCloudresourcemanagerProjects` `cloudasset.assets.exportCloudresourcemanagerTagBindings` `cloudasset.assets.exportCloudresourcemanagerTagKeys` `cloudasset.assets.exportCloudresourcemanagerTagValues` `cloudasset.assets.exportComposerEnvironments` `cloudasset.assets.exportComputeAddress` `cloudasset.assets.exportComputeAutoscalers` `cloudasset.assets.exportComputeBackendBuckets` `cloudasset.assets.exportComputeBackendServices` `cloudasset.assets.exportComputeCommitments` `cloudasset.assets.exportComputeDisks` `cloudasset.assets.exportComputeExternalVpnGateways` `cloudasset.assets.exportComputeFirewallPolicies` `cloudasset.assets.exportComputeFirewalls` `cloudasset.assets.exportComputeForwardingRules` `cloudasset.assets.exportComputeGlobalAddress` `cloudasset.assets.exportComputeGlobalForwardingRules` `cloudasset.assets.exportComputeHealthChecks` `cloudasset.assets.exportComputeHttpHealthChecks` `cloudasset.assets.exportComputeHttpsHealthChecks` `cloudasset.assets.exportComputeImages` `cloudasset.assets.exportComputeInstanceGroupManagers` `cloudasset.assets.exportComputeInstanceGroups` `cloudasset.assets.exportComputeInstanceTemplates` `cloudasset.assets.exportComputeInstances` `cloudasset.assets.exportComputeInterconnect` `cloudasset.assets.exportComputeInterconnectAttachment` `cloudasset.assets.exportComputeLicenses` `cloudasset.assets.exportComputeNetworkEndpointGroups` `cloudasset.assets.exportComputeNetworks` `cloudasset.assets.exportComputeNodeGroups` `cloudasset.assets.exportComputeNodeTemplates` `cloudasset.assets.exportComputePacketMirrorings` `cloudasset.assets.exportComputeProjects` `cloudasset.assets.exportComputeRegionAutoscaler` `cloudasset.assets.exportComputeRegionBackendServices` `cloudasset.assets.exportComputeRegionDisk` `cloudasset.assets.exportComputeRegionInstanceGroup` `cloudasset.assets.exportComputeRegionInstanceGroupManager` `cloudasset.assets.exportComputeReservations` `cloudasset.assets.exportComputeResourcePolicies` `cloudasset.assets.exportComputeRouters` `cloudasset.assets.exportComputeRoutes` `cloudasset.assets.exportComputeSecurityPolicy` `cloudasset.assets.exportComputeServiceAttachments` `cloudasset.assets.exportComputeSnapshots` `cloudasset.assets.exportComputeSslCertificates` `cloudasset.assets.exportComputeSslPolicies` `cloudasset.assets.exportComputeSubnetworks` `cloudasset.assets.exportComputeTargetHttpProxies` `cloudasset.assets.exportComputeTargetHttpsProxies` `cloudasset.assets.exportComputeTargetInstances` `cloudasset.assets.exportComputeTargetPools` `cloudasset.assets.exportComputeTargetSslProxies` `cloudasset.assets.exportComputeTargetTcpProxies` `cloudasset.assets.exportComputeTargetVpnGateways` `cloudasset.assets.exportComputeUrlMaps` `cloudasset.assets.exportComputeVpnGateways` `cloudasset.assets.exportComputeVpnTunnels` `cloudasset.assets.exportConnectorsConnections` `cloudasset.assets.exportConnectorsConnectorVersions` `cloudasset.assets.exportConnectorsConnectors` `cloudasset.assets.exportConnectorsProviders` `cloudasset.assets.exportConnectorsRuntimeConfigs` `cloudasset.assets.exportContainerAppsDeployment` `cloudasset.assets.exportContainerAppsReplicaSets` `cloudasset.assets.exportContainerBatchJobs` `cloudasset.assets.exportContainerClusterrole` `cloudasset.assets.exportContainerClusterrolebinding` `cloudasset.assets.exportContainerClusters` `cloudasset.assets.exportContainerExtensionsIngresses` `cloudasset.assets.exportContainerJobs` `cloudasset.assets.exportContainerNamespace` `cloudasset.assets.exportContainerNetworkingIngresses` `cloudasset.assets.exportContainerNetworkingNetworkPolicies` `cloudasset.assets.exportContainerNode` `cloudasset.assets.exportContainerNodepool` `cloudasset.assets.exportContainerPod` `cloudasset.assets.exportContainerReplicaSets` `cloudasset.assets.exportContainerRole` `cloudasset.assets.exportContainerRolebinding` `cloudasset.assets.exportContainerServices` `cloudasset.assets.exportContainerregistryImage` `cloudasset.assets.exportDataMigrationConnectionProfiles` `cloudasset.assets.exportDataMigrationMigrationJobs` `cloudasset.assets.exportDataflowJobs` `cloudasset.assets.exportDatafusionInstance` `cloudasset.assets.exportDataplexAssets` `cloudasset.assets.exportDataplexLakes` `cloudasset.assets.exportDataplexTasks` `cloudasset.assets.exportDataplexZones` `cloudasset.assets.exportDataprocAutoscalingPolicies` `cloudasset.assets.exportDataprocBatches` `cloudasset.assets.exportDataprocClusters` `cloudasset.assets.exportDataprocJobs` `cloudasset.assets.exportDataprocSessions` `cloudasset.assets.exportDataprocWorkflowTemplates` `cloudasset.assets.exportDatastreamConnectionProfile` `cloudasset.assets.exportDatastreamPrivateConnection` `cloudasset.assets.exportDatastreamStream` `cloudasset.assets.exportDialogflowAgents` `cloudasset.assets.exportDialogflowConversationProfiles` `cloudasset.assets.exportDialogflowKnowledgeBases` `cloudasset.assets.exportDialogflowLocationSettings` `cloudasset.assets.exportDlpDeidentifyTemplates` `cloudasset.assets.exportDlpDlpJobs` `cloudasset.assets.exportDlpInspectTemplates` `cloudasset.assets.exportDlpJobTriggers` `cloudasset.assets.exportDlpStoredInfoTypes` `cloudasset.assets.exportDnsManagedZones` `cloudasset.assets.exportDnsPolicies` `cloudasset.assets.exportDomainsRegistrations` `cloudasset.assets.exportEventarcTriggers` `cloudasset.assets.exportFileBackups` `cloudasset.assets.exportFileInstances` `cloudasset.assets.exportFirebaseAppInfos` `cloudasset.assets.exportFirebaseProjects` `cloudasset.assets.exportFirestoreDatabases` `cloudasset.assets.exportGKEHubFeatures` `cloudasset.assets.exportGKEHubMemberships` `cloudasset.assets.exportGameservicesGameServerClusters` `cloudasset.assets.exportGameservicesGameServerConfigs` `cloudasset.assets.exportGameservicesGameServerDeployments` `cloudasset.assets.exportGameservicesRealms` `cloudasset.assets.exportGkeBackupBackupPlans` `cloudasset.assets.exportGkeBackupBackups` `cloudasset.assets.exportGkeBackupRestorePlans` `cloudasset.assets.exportGkeBackupRestores` `cloudasset.assets.exportGkeBackupVolumeBackups` `cloudasset.assets.exportGkeBackupVolumeRestores` `cloudasset.assets.exportHealthcareConsentStores` `cloudasset.assets.exportHealthcareDatasets` `cloudasset.assets.exportHealthcareDicomStores` `cloudasset.assets.exportHealthcareFhirStores` `cloudasset.assets.exportHealthcareHl7V2Stores` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportIamRoles` `cloudasset.assets.exportIamServiceAccountKeys` `cloudasset.assets.exportIamServiceAccounts` `cloudasset.assets.exportIapTunnel` `cloudasset.assets.exportIapTunnelInstances` `cloudasset.assets.exportIapTunnelZones` `cloudasset.assets.exportIapWeb` `cloudasset.assets.exportIapWebServiceVersion` `cloudasset.assets.exportIapWebServices` `cloudasset.assets.exportIapWebType` `cloudasset.assets.exportIdsEndpoints` `cloudasset.assets.exportIntegrationsAuthConfigs` `cloudasset.assets.exportIntegrationsCertificates` `cloudasset.assets.exportIntegrationsExecutions` `cloudasset.assets.exportIntegrationsIntegrationVersions` `cloudasset.assets.exportIntegrationsIntegrations` `cloudasset.assets.exportIntegrationsSfdcChannels` `cloudasset.assets.exportIntegrationsSfdcInstances` `cloudasset.assets.exportIntegrationsSuspensions` `cloudasset.assets.exportLoggingLogMetrics` `cloudasset.assets.exportLoggingLogSinks` `cloudasset.assets.exportManagedidentitiesDomain` `cloudasset.assets.exportMetastoreBackups` `cloudasset.assets.exportMetastoreMetadataImports` `cloudasset.assets.exportMetastoreServices` `cloudasset.assets.exportMonitoringAlertPolicies` `cloudasset.assets.exportNetworkConnectivityHubs` `cloudasset.assets.exportNetworkConnectivitySpokes` `cloudasset.assets.exportNetworkManagementConnectivityTests` `cloudasset.assets.exportNetworkServicesEndpointPolicies` `cloudasset.assets.exportNetworkServicesGateways` `cloudasset.assets.exportNetworkServicesGrpcRoutes` `cloudasset.assets.exportNetworkServicesHttpRoutes` `cloudasset.assets.exportNetworkServicesMeshes` `cloudasset.assets.exportNetworkServicesServiceBindings` `cloudasset.assets.exportNetworkServicesTcpRoutes` `cloudasset.assets.exportNetworkServicesTlsRoutes` `cloudasset.assets.exportOSConfigOSPolicyAssignmentReports` `cloudasset.assets.exportOSConfigOSPolicyAssignments` `cloudasset.assets.exportOSConfigVulnerabilityReports` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportOrgPolicy` `cloudasset.assets.exportPatchDeployments` `cloudasset.assets.exportPubsubSnapshots` `cloudasset.assets.exportPubsubSubscriptions` `cloudasset.assets.exportPubsubTopics` `cloudasset.assets.exportRedisInstances` `cloudasset.assets.exportResource` `cloudasset.assets.exportSecretManagerSecretVersions` `cloudasset.assets.exportSecretManagerSecrets` `cloudasset.assets.exportServiceDirectoryNamespaces` `cloudasset.assets.exportServicePerimeter` `cloudasset.assets.exportServiceconsumermanagementConsumerProperty` `cloudasset.assets.exportServiceconsumermanagementConsumerQuotaLimits` `cloudasset.assets.exportServiceconsumermanagementConsumers` `cloudasset.assets.exportServiceconsumermanagementProducerOverrides` `cloudasset.assets.exportServiceconsumermanagementTenancyUnits` `cloudasset.assets.exportServiceconsumermanagementVisibility` `cloudasset.assets.exportServicemanagementServices` `cloudasset.assets.exportServiceusageAdminOverrides` `cloudasset.assets.exportServiceusageConsumerOverrides` `cloudasset.assets.exportServiceusageServices` `cloudasset.assets.exportSpannerBackups` `cloudasset.assets.exportSpannerDatabases` `cloudasset.assets.exportSpannerInstances` `cloudasset.assets.exportSpeakerIdPhrases` `cloudasset.assets.exportSpeakerIdSettings` `cloudasset.assets.exportSpeakerIdSpeakers` `cloudasset.assets.exportSpeechCustomClasses` `cloudasset.assets.exportSpeechPhraseSets` `cloudasset.assets.exportSqladminBackupRuns` `cloudasset.assets.exportSqladminInstances` `cloudasset.assets.exportStorageBuckets` `cloudasset.assets.exportTpuNodes` `cloudasset.assets.exportVpcaccessConnector` `cloudasset.assets.listAccessLevel` `cloudasset.assets.listAccessPolicy` `cloudasset.assets.listAiplatformBatchPredictionJobs` `cloudasset.assets.listAiplatformCustomJobs` `cloudasset.assets.listAiplatformDataLabelingJobs` `cloudasset.assets.listAiplatformDatasets` `cloudasset.assets.listAiplatformEndpoints` `cloudasset.assets.listAiplatformHyperparameterTuningJobs` `cloudasset.assets.listAiplatformMetadataStores` `cloudasset.assets.listAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.listAiplatformModels` `cloudasset.assets.listAiplatformPipelineJobs` `cloudasset.assets.listAiplatformSpecialistPools` `cloudasset.assets.listAiplatformTrainingPipelines` `cloudasset.assets.listAllAccessPolicy` `cloudasset.assets.listAnthosConnectedCluster` `cloudasset.assets.listAnthosedgeCluster` `cloudasset.assets.listApigatewayApi` `cloudasset.assets.listApigatewayApiConfig` `cloudasset.assets.listApigatewayGateway` `cloudasset.assets.listApikeysKeys` `cloudasset.assets.listAppengineApplications` `cloudasset.assets.listAppengineServices` `cloudasset.assets.listAppengineVersions` `cloudasset.assets.listArtifactregistryDockerImages` `cloudasset.assets.listArtifactregistryRepositories` `cloudasset.assets.listAssuredWorkloadsWorkloads` `cloudasset.assets.listBeyondCorpApiGateways` `cloudasset.assets.listBeyondCorpAppConnections` `cloudasset.assets.listBeyondCorpAppConnectors` `cloudasset.assets.listBeyondCorpAppGateways` `cloudasset.assets.listBeyondCorpClientConnectorServices` `cloudasset.assets.listBeyondCorpClientGateways` `cloudasset.assets.listBigqueryDatasets` `cloudasset.assets.listBigqueryModels` `cloudasset.assets.listBigqueryTables` `cloudasset.assets.listBigtableAppProfile` `cloudasset.assets.listBigtableBackup` `cloudasset.assets.listBigtableCluster` `cloudasset.assets.listBigtableInstance` `cloudasset.assets.listBigtableTable` `cloudasset.assets.listCloudAssetFeeds` `cloudasset.assets.listCloudDeployDeliveryPipelines` `cloudasset.assets.listCloudDeployReleases` `cloudasset.assets.listCloudDeployRollouts` `cloudasset.assets.listCloudDeployTargets` `cloudasset.assets.listCloudDocumentAIEvaluation` `cloudasset.assets.listCloudDocumentAIHumanReviewConfig` `cloudasset.assets.listCloudDocumentAILabelerPool` `cloudasset.assets.listCloudDocumentAIProcessor` `cloudasset.assets.listCloudDocumentAIProcessorVersion` `cloudasset.assets.listCloudbillingBillingAccounts` `cloudasset.assets.listCloudbillingProjectBillingInfos` `cloudasset.assets.listCloudfunctionsFunctions` `cloudasset.assets.listCloudfunctionsGen2Functions` `cloudasset.assets.listCloudkmsCryptoKeyVersions` `cloudasset.assets.listCloudkmsCryptoKeys` `cloudasset.assets.listCloudkmsEkmConnections` `cloudasset.assets.listCloudkmsImportJobs` `cloudasset.assets.listCloudkmsKeyRings` `cloudasset.assets.listCloudmemcacheInstances` `cloudasset.assets.listCloudresourcemanagerFolders` `cloudasset.assets.listCloudresourcemanagerOrganizations` `cloudasset.assets.listCloudresourcemanagerProjects` `cloudasset.assets.listCloudresourcemanagerTagBindings` `cloudasset.assets.listCloudresourcemanagerTagKeys` `cloudasset.assets.listCloudresourcemanagerTagValues` `cloudasset.assets.listComposerEnvironments` `cloudasset.assets.listComputeAddress` `cloudasset.assets.listComputeAutoscalers` `cloudasset.assets.listComputeBackendBuckets` `cloudasset.assets.listComputeBackendServices` `cloudasset.assets.listComputeCommitments` `cloudasset.assets.listComputeDisks` `cloudasset.assets.listComputeExternalVpnGateways` `cloudasset.assets.listComputeFirewallPolicies` `cloudasset.assets.listComputeFirewalls` `cloudasset.assets.listComputeForwardingRules` `cloudasset.assets.listComputeGlobalAddress` `cloudasset.assets.listComputeGlobalForwardingRules` `cloudasset.assets.listComputeHealthChecks` `cloudasset.assets.listComputeHttpHealthChecks` `cloudasset.assets.listComputeHttpsHealthChecks` `cloudasset.assets.listComputeImages` `cloudasset.assets.listComputeInstanceGroupManagers` `cloudasset.assets.listComputeInstanceGroups` `cloudasset.assets.listComputeInstanceTemplates` `cloudasset.assets.listComputeInstances` `cloudasset.assets.listComputeInterconnect` `cloudasset.assets.listComputeInterconnectAttachment` `cloudasset.assets.listComputeLicenses` `cloudasset.assets.listComputeNetworkEndpointGroups` `cloudasset.assets.listComputeNetworks` `cloudasset.assets.listComputeNodeGroups` `cloudasset.assets.listComputeNodeTemplates` `cloudasset.assets.listComputePacketMirrorings` `cloudasset.assets.listComputeProjects` `cloudasset.assets.listComputeRegionAutoscaler` `cloudasset.assets.listComputeRegionBackendServices` `cloudasset.assets.listComputeRegionDisk` `cloudasset.assets.listComputeRegionInstanceGroup` `cloudasset.assets.listComputeRegionInstanceGroupManager` `cloudasset.assets.listComputeReservations` `cloudasset.assets.listComputeResourcePolicies` `cloudasset.assets.listComputeRouters` `cloudasset.assets.listComputeRoutes` `cloudasset.assets.listComputeSecurityPolicy` `cloudasset.assets.listComputeServiceAttachments` `cloudasset.assets.listComputeSnapshots` `cloudasset.assets.listComputeSslCertificates` `cloudasset.assets.listComputeSslPolicies` `cloudasset.assets.listComputeSubnetworks` `cloudasset.assets.listComputeTargetHttpProxies` `cloudasset.assets.listComputeTargetHttpsProxies` `cloudasset.assets.listComputeTargetInstances` `cloudasset.assets.listComputeTargetPools` `cloudasset.assets.listComputeTargetSslProxies` `cloudasset.assets.listComputeTargetTcpProxies` `cloudasset.assets.listComputeTargetVpnGateways` `cloudasset.assets.listComputeUrlMaps` `cloudasset.assets.listComputeVpnGateways` `cloudasset.assets.listComputeVpnTunnels` `cloudasset.assets.listConnectorsConnections` `cloudasset.assets.listConnectorsConnectorVersions` `cloudasset.assets.listConnectorsConnectors` `cloudasset.assets.listConnectorsProviders` `cloudasset.assets.listConnectorsRuntimeConfigs` `cloudasset.assets.listContainerAppsDeployment` `cloudasset.assets.listContainerAppsReplicaSets` `cloudasset.assets.listContainerBatchJobs` `cloudasset.assets.listContainerClusterrole` `cloudasset.assets.listContainerClusterrolebinding` `cloudasset.assets.listContainerClusters` `cloudasset.assets.listContainerExtensionsIngresses` `cloudasset.assets.listContainerJobs` `cloudasset.assets.listContainerNamespace` `cloudasset.assets.listContainerNetworkingIngresses` `cloudasset.assets.listContainerNetworkingNetworkPolicies` `cloudasset.assets.listContainerNode` `cloudasset.assets.listContainerNodepool` `cloudasset.assets.listContainerPod` `cloudasset.assets.listContainerReplicaSets` `cloudasset.assets.listContainerRole` `cloudasset.assets.listContainerRolebinding` `cloudasset.assets.listContainerServices` `cloudasset.assets.listContainerregistryImage` `cloudasset.assets.listDataMigrationConnectionProfiles` `cloudasset.assets.listDataMigrationMigrationJobs` `cloudasset.assets.listDataflowJobs` `cloudasset.assets.listDatafusionInstance` `cloudasset.assets.listDataplexAssets` `cloudasset.assets.listDataplexLakes` `cloudasset.assets.listDataplexTasks` `cloudasset.assets.listDataplexZones` `cloudasset.assets.listDataprocAutoscalingPolicies` `cloudasset.assets.listDataprocBatches` `cloudasset.assets.listDataprocClusters` `cloudasset.assets.listDataprocJobs` `cloudasset.assets.listDataprocSessions` `cloudasset.assets.listDataprocWorkflowTemplates` `cloudasset.assets.listDatastreamConnectionProfile` `cloudasset.assets.listDatastreamPrivateConnection` `cloudasset.assets.listDatastreamStream` `cloudasset.assets.listDialogflowAgents` `cloudasset.assets.listDialogflowConversationProfiles` `cloudasset.assets.listDialogflowKnowledgeBases` `cloudasset.assets.listDialogflowLocationSettings` `cloudasset.assets.listDlpDeidentifyTemplates` `cloudasset.assets.listDlpDlpJobs` `cloudasset.assets.listDlpInspectTemplates` `cloudasset.assets.listDlpJobTriggers` `cloudasset.assets.listDlpStoredInfoTypes` `cloudasset.assets.listDnsManagedZones` `cloudasset.assets.listDnsPolicies` `cloudasset.assets.listDomainsRegistrations` `cloudasset.assets.listEventarcTriggers` `cloudasset.assets.listFileBackups` `cloudasset.assets.listFileInstances` `cloudasset.assets.listFirebaseAppInfos` `cloudasset.assets.listFirebaseProjects` `cloudasset.assets.listFirestoreDatabases` `cloudasset.assets.listGKEHubFeatures` `cloudasset.assets.listGKEHubMemberships` `cloudasset.assets.listGameservicesGameServerClusters` `cloudasset.assets.listGameservicesGameServerConfigs` `cloudasset.assets.listGameservicesGameServerDeployments` `cloudasset.assets.listGameservicesRealms` `cloudasset.assets.listGkeBackupBackupPlans` `cloudasset.assets.listGkeBackupBackups` `cloudasset.assets.listGkeBackupRestorePlans` `cloudasset.assets.listGkeBackupRestores` `cloudasset.assets.listGkeBackupVolumeBackups` `cloudasset.assets.listGkeBackupVolumeRestores` `cloudasset.assets.listHealthcareConsentStores` `cloudasset.assets.listHealthcareDatasets` `cloudasset.assets.listHealthcareDicomStores` `cloudasset.assets.listHealthcareFhirStores` `cloudasset.assets.listHealthcareHl7V2Stores` `cloudasset.assets.listIamPolicy` `cloudasset.assets.listIamRoles` `cloudasset.assets.listIamServiceAccountKeys` `cloudasset.assets.listIamServiceAccounts` `cloudasset.assets.listIapTunnel` `cloudasset.assets.listIapTunnelInstances` `cloudasset.assets.listIapTunnelZones` `cloudasset.assets.listIapWeb` `cloudasset.assets.listIapWebServiceVersion` `cloudasset.assets.listIapWebServices` `cloudasset.assets.listIapWebType` `cloudasset.assets.listIdsEndpoints` `cloudasset.assets.listIntegrationsAuthConfigs` `cloudasset.assets.listIntegrationsCertificates` `cloudasset.assets.listIntegrationsExecutions` `cloudasset.assets.listIntegrationsIntegrationVersions` `cloudasset.assets.listIntegrationsIntegrations` `cloudasset.assets.listIntegrationsSfdcChannels` `cloudasset.assets.listIntegrationsSfdcInstances` `cloudasset.assets.listIntegrationsSuspensions` `cloudasset.assets.listLoggingLogMetrics` `cloudasset.assets.listLoggingLogSinks` `cloudasset.assets.listManagedidentitiesDomain` `cloudasset.assets.listMetastoreBackups` `cloudasset.assets.listMetastoreMetadataImports` `cloudasset.assets.listMetastoreServices` `cloudasset.assets.listMonitoringAlertPolicies` `cloudasset.assets.listNetworkConnectivityHubs` `cloudasset.assets.listNetworkConnectivitySpokes` `cloudasset.assets.listNetworkManagementConnectivityTests` `cloudasset.assets.listNetworkServicesEndpointPolicies` `cloudasset.assets.listNetworkServicesGateways` `cloudasset.assets.listNetworkServicesGrpcRoutes` `cloudasset.assets.listNetworkServicesHttpRoutes` `cloudasset.assets.listNetworkServicesMeshes` `cloudasset.assets.listNetworkServicesServiceBindings` `cloudasset.assets.listNetworkServicesTcpRoutes` `cloudasset.assets.listNetworkServicesTlsRoutes` `cloudasset.assets.listOSConfigOSPolicyAssignmentReports` `cloudasset.assets.listOSConfigOSPolicyAssignments` `cloudasset.assets.listOSConfigVulnerabilityReports` `cloudasset.assets.listOSInventories` `cloudasset.assets.listOrgPolicy` `cloudasset.assets.listPatchDeployments` `cloudasset.assets.listPubsubSnapshots` `cloudasset.assets.listPubsubSubscriptions` `cloudasset.assets.listPubsubTopics` `cloudasset.assets.listRedisInstances` `cloudasset.assets.listResource` `cloudasset.assets.listRunDomainMapping` `cloudasset.assets.listRunRevision` `cloudasset.assets.listRunService` `cloudasset.assets.listSecretManagerSecretVersions` `cloudasset.assets.listSecretManagerSecrets` `cloudasset.assets.listServiceDirectoryNamespaces` `cloudasset.assets.listServicePerimeter` `cloudasset.assets.listServiceconsumermanagementConsumerProperty` `cloudasset.assets.listServiceconsumermanagementConsumerQuotaLimits` `cloudasset.assets.listServiceconsumermanagementConsumers` `cloudasset.assets.listServiceconsumermanagementProducerOverrides` `cloudasset.assets.listServiceconsumermanagementTenancyUnits` `cloudasset.assets.listServiceconsumermanagementVisibility` `cloudasset.assets.listServicemanagementServices` `cloudasset.assets.listServiceusageAdminOverrides` `cloudasset.assets.listServiceusageConsumerOverrides` `cloudasset.assets.listServiceusageServices` `cloudasset.assets.listSpannerBackups` `cloudasset.assets.listSpannerDatabases` `cloudasset.assets.listSpannerInstances` `cloudasset.assets.listSpeakerIdPhrases` `cloudasset.assets.listSpeakerIdSettings` `cloudasset.assets.listSpeakerIdSpeakers` `cloudasset.assets.listSpeechCustomClasses` `cloudasset.assets.listSpeechPhraseSets` `cloudasset.assets.listSqladminBackupRuns` `cloudasset.assets.listSqladminInstances` `cloudasset.assets.listStorageBuckets` `cloudasset.assets.listTpuNodes` `cloudasset.assets.listVpcaccessConnector` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.feeds.*`

  * `cloudasset.feeds.create`
  * `cloudasset.feeds.delete`
  * `cloudasset.feeds.get`
  * `cloudasset.feeds.list`
  * `cloudasset.feeds.update`

`cloudasset.othercloudconnections.get` `cloudasset.othercloudconnections.list` `cloudasset.othercloudconnections.verify` `cloudasset.savedqueries.get` `cloudasset.savedqueries.list` `cloudsql.instances.connect` `cloudsql.users.list` `compute.disks.useReadOnly` `compute.globalOperations.get` `compute.instances.get` `compute.instances.list` `compute.networkEndpointGroups.get` `compute.projects.get` `compute.regionOperations.get` `compute.zoneOperations.get` `container.clusters.get` `iam.denypolicies.get` `iam.denypolicies.list` `iam.googleapis.com/workloadIdentityPoolProviders.list` `iam.googleapis.com/workloadIdentityPools.list` `logging.logEntries.list` `monitoring.alertPolicies.list` `monitoring.timeSeries.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `recommender.cloudAssetInsights.get` `recommender.cloudAssetInsights.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `resourcemanager.tagValues.get` `securitycenter.assets.list` `securitycenter.assetsecuritymarks.update` `securitycenter.findings.list` `securitycenter.notificationconfig.create` `securitycenter.notificationconfig.delete` `securitycenter.notificationconfig.update` `securitycenter.organizationsettings.get` `securitycenter.resourcevalueconfigs.get` `securitycenter.resourcevalueconfigs.list` `securitycenter.simulations.get` `securitycenter.sources.list` `securitycenter.valuedresources.list` `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.securityHealthAnalyticsCustomModules.create` `securitycentermanagement.securityHealthAnalyticsCustomModules.delete` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.update` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.disable` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list`  
  
## Security Command Center permissions

Permission | Included in roles  
---|---  
  
#### `securitycenter.assets.group`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Assets Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsViewer) (`roles/securitycenter.assetsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.assets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Assets Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsViewer) (`roles/securitycenter.assetsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.assets.listAssetPropertyNames`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Assets Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsViewer) (`roles/securitycenter.assetsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.assets.runDiscovery`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Assets Discovery Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsDiscoveryRunner) (`roles/securitycenter.assetsDiscoveryRunner`)   
  
#### `securitycenter.assetsecuritymarks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Asset Security Marks Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetSecurityMarksWriter) (`roles/securitycenter.assetSecurityMarksWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.attackpaths.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Attack Paths Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.attackPathsViewer) (`roles/securitycenter.attackPathsViewer`)   
  
#### `securitycenter.bigQueryExports.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center BigQuery Exports Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.bigQueryExportsEditor) (`roles/securitycenter.bigQueryExportsEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.bigQueryExports.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center BigQuery Exports Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.bigQueryExportsEditor) (`roles/securitycenter.bigQueryExportsEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.bigQueryExports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center BigQuery Exports Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.bigQueryExportsEditor) (`roles/securitycenter.bigQueryExportsEditor`)  [Security Center BigQuery Exports Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.bigQueryExportsViewer) (`roles/securitycenter.bigQueryExportsViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.bigQueryExports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center BigQuery Exports Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.bigQueryExportsEditor) (`roles/securitycenter.bigQueryExportsEditor`)  [Security Center BigQuery Exports Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.bigQueryExportsViewer) (`roles/securitycenter.bigQueryExportsViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.bigQueryExports.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center BigQuery Exports Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.bigQueryExportsEditor) (`roles/securitycenter.bigQueryExportsEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.billingtier.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.complianceReports.aggregate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Compliance Reports Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.complianceReportsViewer) (`roles/securitycenter.complianceReportsViewer`)  [Security Center Compliance Snapshots Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.complianceSnapshotsViewer) (`roles/securitycenter.complianceSnapshotsViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.compliancesnapshots.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Compliance Snapshots Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.complianceSnapshotsViewer) (`roles/securitycenter.complianceSnapshotsViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.containerthreatdetectionsettings.calculate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.containerthreatdetectionsettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.containerthreatdetectionsettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.effectivesecurityhealthanalyticscustommodules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.effectivesecurityhealthanalyticscustommodules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.eventthreatdetectionsettings.calculate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.eventthreatdetectionsettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.eventthreatdetectionsettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.exposurepathexplan.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Attack Paths Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.attackPathsViewer) (`roles/securitycenter.attackPathsViewer`)   
  
#### `securitycenter.findingexplanations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.findingexternalsystems.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center External Systems Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.externalSystemsEditor) (`roles/securitycenter.externalSystemsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 

  
  
#### `securitycenter.findings.bulkMuteUpdate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Findings Bulk Mute Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsBulkMuteEditor) (`roles/securitycenter.findingsBulkMuteEditor`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)   
  
#### `securitycenter.findings.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center BigQuery Exports Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.bigQueryExportsEditor) (`roles/securitycenter.bigQueryExportsEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.findings.group`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAM Recommender Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`)  [IAM Recommender Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamViewer) (`roles/recommender.iamViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.findings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Google Cloud Security Response Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.securityResponseServiceAgent) (`roles/securitycenter.securityResponseServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.findings.listFindingPropertyNames`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.findings.setMute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Mute Setter](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsMuteSetter) (`roles/securitycenter.findingsMuteSetter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 

  
  
#### `securitycenter.findings.setState`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings State Setter](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsStateSetter) (`roles/securitycenter.findingsStateSetter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 

  
  
#### `securitycenter.findings.setWorkflowState`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Findings Workflow State Setter](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsWorkflowStateSetter) (`roles/securitycenter.findingsWorkflowStateSetter`)   
  
#### `securitycenter.findings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 

  
  
#### `securitycenter.findingsecuritymarks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Finding Security Marks Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingSecurityMarksWriter) (`roles/securitycenter.findingSecurityMarksWriter`)   
  
#### `securitycenter.graphs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.graphs.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.integratedvulnerabilityscannersettings.calculate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.integratedvulnerabilityscannersettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.integratedvulnerabilityscannersettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.issues.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.issues.group`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.issues.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.issues.listFilterValues`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.issues.mute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)   
  
#### `securitycenter.issues.retrieve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.issues.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.issues.searchImpactedResources`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Issues Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`)  [Security Center Issues Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.muteconfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Mute Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsEditor) (`roles/securitycenter.muteConfigsEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.muteconfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Mute Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsEditor) (`roles/securitycenter.muteConfigsEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.muteconfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Mute Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsEditor) (`roles/securitycenter.muteConfigsEditor`)  [Security Center Mute Configurations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsViewer) (`roles/securitycenter.muteConfigsViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.muteconfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Mute Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsEditor) (`roles/securitycenter.muteConfigsEditor`)  [Security Center Mute Configurations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsViewer) (`roles/securitycenter.muteConfigsViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.muteconfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Mute Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsEditor) (`roles/securitycenter.muteConfigsEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.notificationconfig.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Notification Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigEditor) (`roles/securitycenter.notificationConfigEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.notificationconfig.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Notification Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigEditor) (`roles/securitycenter.notificationConfigEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.notificationconfig.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Notification Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigEditor) (`roles/securitycenter.notificationConfigEditor`)  [Security Center Notification Configurations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigViewer) (`roles/securitycenter.notificationConfigViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.notificationconfig.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Notification Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigEditor) (`roles/securitycenter.notificationConfigEditor`)  [Security Center Notification Configurations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigViewer) (`roles/securitycenter.notificationConfigViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.notificationconfig.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Notification Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigEditor) (`roles/securitycenter.notificationConfigEditor`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.organizationsettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.admin) (`roles/securitycentermanagement.admin`)  [Security Center Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.editor) (`roles/securitycentermanagement.editor`)  [Security Center Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.viewer) (`roles/securitycentermanagement.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  [Security Center Management Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.settingsEditor) (`roles/securitycentermanagement.settingsEditor`)  [Security Center Management Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.settingsViewer) (`roles/securitycentermanagement.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Health Analytics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.securityHealthAnalyticsServiceAgent) (`roles/securitycenter.securityHealthAnalyticsServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.organizationsettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.admin) (`roles/securitycentermanagement.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Management Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.settingsEditor) (`roles/securitycentermanagement.settingsEditor`)   
  
#### `securitycenter.rapidvulnerabilitydetectionsettings.calculate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.rapidvulnerabilitydetectionsettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.rapidvulnerabilitydetectionsettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.resourcevalueconfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Resource Value Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigsEditor) (`roles/securitycenter.resourceValueConfigsEditor`)   
  
#### `securitycenter.resourcevalueconfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Resource Value Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigsEditor) (`roles/securitycenter.resourceValueConfigsEditor`)   
  
#### `securitycenter.resourcevalueconfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Resource Value Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigsEditor) (`roles/securitycenter.resourceValueConfigsEditor`)  [Security Center Resource Value Configurations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigsViewer) (`roles/securitycenter.resourceValueConfigsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.resourcevalueconfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Resource Value Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigsEditor) (`roles/securitycenter.resourceValueConfigsEditor`)  [Security Center Resource Value Configurations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigsViewer) (`roles/securitycenter.resourceValueConfigsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.resourcevalueconfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Resource Value Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.resourceValueConfigsEditor) (`roles/securitycenter.resourceValueConfigsEditor`)   
  
#### `securitycenter.riskreports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Risk Reports Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.riskReportsViewer) (`roles/securitycenter.riskReportsViewer`)   
  
#### `securitycenter.riskreports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Risk Reports Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.riskReportsViewer) (`roles/securitycenter.riskReportsViewer`)   
  
#### `securitycenter.securitycentersettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.admin) (`roles/securitycentermanagement.admin`)  [Security Center Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.editor) (`roles/securitycentermanagement.editor`)  [Security Center Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.viewer) (`roles/securitycentermanagement.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  [Security Center Management Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.settingsEditor) (`roles/securitycentermanagement.settingsEditor`)  [Security Center Management Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.settingsViewer) (`roles/securitycentermanagement.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.securitycentersettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.admin) (`roles/securitycentermanagement.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Management Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.settingsEditor) (`roles/securitycentermanagement.settingsEditor`)   
  
#### `securitycenter.securityhealthanalyticscustommodules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.securityhealthanalyticscustommodules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.securityhealthanalyticscustommodules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.securityhealthanalyticscustommodules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.securityhealthanalyticscustommodules.simulate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Health Analytics Custom Modules Tester](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.securityHealthAnalyticsCustomModulesTester) (`roles/securitycenter.securityHealthAnalyticsCustomModulesTester`)   
  
#### `securitycenter.securityhealthanalyticscustommodules.test`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Health Analytics Custom Modules Tester](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.securityHealthAnalyticsCustomModulesTester) (`roles/securitycenter.securityHealthAnalyticsCustomModulesTester`)   
  
#### `securitycenter.securityhealthanalyticscustommodules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.securityhealthanalyticssettings.calculate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 
  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.securityhealthanalyticssettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 
  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.securityhealthanalyticssettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Posture Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Posture Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.postureDeployer) (`roles/securityposture.postureDeployer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DSPM Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.serviceAgent) (`roles/dspm.serviceAgent`) 

  
  
#### `securitycenter.simulations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Simulations Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.simulationsViewer) (`roles/securitycenter.simulationsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.sources.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Sources Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesAdmin) (`roles/securitycenter.sourcesAdmin`)  [Security Center Sources Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesEditor) (`roles/securitycenter.sourcesEditor`)  [Security Center Sources Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesViewer) (`roles/securitycenter.sourcesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.sources.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Sources Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesAdmin) (`roles/securitycenter.sourcesAdmin`)   
  
#### `securitycenter.sources.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Sources Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesAdmin) (`roles/securitycenter.sourcesAdmin`)  [Security Center Sources Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesEditor) (`roles/securitycenter.sourcesEditor`)  [Security Center Sources Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesViewer) (`roles/securitycenter.sourcesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) 
  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.sources.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Sources Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesAdmin) (`roles/securitycenter.sourcesAdmin`)   
  
#### `securitycenter.sources.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Sources Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesAdmin) (`roles/securitycenter.sourcesAdmin`)  [Security Center Sources Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesEditor) (`roles/securitycenter.sourcesEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 

  
  
#### `securitycenter.subscription.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.userinterfacemetadata.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAM Recommender Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`)  [IAM Recommender Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamViewer) (`roles/recommender.iamViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Asset Security Marks Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetSecurityMarksWriter) (`roles/securitycenter.assetSecurityMarksWriter`)  [Security Center Assets Discovery Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsDiscoveryRunner) (`roles/securitycenter.assetsDiscoveryRunner`)  [Security Center Assets Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsViewer) (`roles/securitycenter.assetsViewer`)  [Security Center Finding Security Marks Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingSecurityMarksWriter) (`roles/securitycenter.findingSecurityMarksWriter`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings State Setter](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsStateSetter) (`roles/securitycenter.findingsStateSetter`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  [Security Center Findings Workflow State Setter](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsWorkflowStateSetter) (`roles/securitycenter.findingsWorkflowStateSetter`)  [Security Center Notification Configurations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigEditor) (`roles/securitycenter.notificationConfigEditor`)  [Security Center Notification Configurations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationConfigViewer) (`roles/securitycenter.notificationConfigViewer`)  [Security Center Risk Reports Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.riskReportsViewer) (`roles/securitycenter.riskReportsViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  [Security Center Sources Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesAdmin) (`roles/securitycenter.sourcesAdmin`)  [Security Center Sources Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesEditor) (`roles/securitycenter.sourcesEditor`)  [Security Center Sources Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.sourcesViewer) (`roles/securitycenter.sourcesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.valuedresources.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)  [Chronicle SOAR Threat Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarThreatManager) (`roles/chronicle.soarThreatManager`)  [Chronicle SOAR Vulnerability Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarVulnerabilityManager) (`roles/chronicle.soarVulnerabilityManager`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Valued Resources Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.valuedResourcesViewer) (`roles/securitycenter.valuedResourcesViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `securitycenter.virtualmachinethreatdetectionsettings.calculate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.virtualmachinethreatdetectionsettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.virtualmachinethreatdetectionsettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
#### `securitycenter.vulnerabilitysnapshots.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Findings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)  [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.websecurityscannersettings.calculate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.websecurityscannersettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)  [Security Center Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Risk Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`) 

  
  
#### `securitycenter.websecurityscannersettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Center Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`)  [Security Center Settings Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
