---
url: https://docs.cloud.google.com/security-command-center/docs/access-control-org/
title: Control access with organization-level activations \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:45.561097+00:00
---

# Control access with organization-level activations  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/access-control-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Control access with organization-level activations Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

In an organization-level deployment of Security Command Center, Identity and Access Management (IAM) lets you manage permissions at different levels of your resource hierarchy, including projects where the Premium tier is activated. If you specifically activated at the project level, see [IAM for project-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-project) instead.

## Permissions

To control who can view, create, or update Security Command Center resources, you grant IAM roles to principals, such as users, groups, or service accounts. Each role bundles the specific permissions that are needed for common tasks.

### Required for activation

To activate Security Command Center, see one of the following based on your service tier:

  * [Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier#required-roles).

  * [Activate Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier#required-roles).

  * [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#configure-permissions).




### Required for ongoing administration and use

This section describes permissions needed to administer and use Security Command Center Premium and Standard. For information about Security Command Center Enterprise, see [Configure permissions for ongoing use of Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#permissions-management-use%7D).

To change the configuration of your organization, you need both of the following roles at the organization level:

  * [ Organization Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)
  * [ Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)



If a user doesn't require edit permissions, consider granting them viewer roles.

To view all assets, findings, and attack paths in Security Command Center, users need the [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`) role at the organization level.

To view settings, users need the [ Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`) role at the organization level.

To restrict access to individual folders and projects, don't grant all roles at the organization level. Instead, grant the following roles at the **folder** _or_ **project** level:

  * [ Security Center Assets Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsViewer) (`roles/securitycenter.assetsViewer`)
  * [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)



Each [detection service](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) may require additional permissions to enable or configure it. See the documentation specific to each service for more information.

## Organization-level roles

When IAM roles are applied at the organization level, projects and folders under that organization [inherit its role bindings](https://docs.cloud.google.com/iam/docs/policies#inheritance).

The following figure illustrates a typical Security Command Center resource hierarchy with roles granted at the organization level.

[ ![Security Command Center resource hierarchy and permission structure](https://docs.cloud.google.com/static/security-command-center/images/organization_roles_small.svg)](https://docs.cloud.google.com/static/security-command-center/images/organization_roles_small.svg) Security Command Center resource hierarchy and organization-level roles (click to enlarge)

IAM roles include permissions to view, edit, update, create, or delete resources. Roles granted at the organization level in Security Command Center let you perform prescribed actions on findings, assets, and security sources throughout your organization. For example, a user granted the [ Security Center Findings Editor role](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`) can view or edit findings attached to any resource in any project or folder in your organization. With this structure, you don't have to grant users roles in each folder or project.

For instructions on managing roles and permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Organization-level roles are not suitable for all use cases, particularly for sensitive applications or compliance standards that require strict access controls. To create fine-grained access policies, you can grant roles at the folder and project levels.

## Folder-level and project-level roles

Security Command Center lets you grant Security Command Center IAM roles for specific folders and projects, creating multiple views, or silos, within your organization. You grant users and groups different access and edit permissions to folders and projects across your organization.

With folder and project roles, users with Security Command Center roles have the ability to manage assets and findings within designated projects or folders. For example, a security engineer can be given limited access to select folders and projects while a security administrator can manage all resources at the organization level.

Folder and project roles allow Security Command Center permissions to be applied at lower levels of your organization's resource hierarchy, but do not change the hierarchy. The following figure illustrates a user with Security Command Center permissions to access findings in a specific project.

[ ![Security Command Center resource hierarchy and permission structure](https://docs.cloud.google.com/static/security-command-center/images/project_roles_small.svg)](https://docs.cloud.google.com/static/security-command-center/images/project_roles_small.svg) Security Command Center resource hierarchy and project-level roles - dashed items are inaccessible (click to enlarge)

Users with folder and project roles see a subset of an organization's resources. Any actions they take are limited to the same scope. For example, if a user has permissions for a folder, they can access resources in any project in the folder. Permissions for a project give users access to resources in that project.

For instructions on managing roles and permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Role restrictions

By granting Security Command Center roles at the folder or project level, Security Command Center administrators can do the following:

  * Limit Security Command Center view or edit permissions to specific folders and projects
  * Grant view and edit permissions for groups of assets or findings to specific users or teams
  * Restrict the ability to view or edit finding details, including updates to security marks and finding state, to individuals or groups with access to the underlying finding
  * Control access to Security Command Center settings, which can only be viewed by individuals with organization-level roles



### Security Command Center functions

Security Command Center functions are also restricted based on view and edit permissions.

In the Google Cloud console, Security Command Center lets individuals without organization-level permissions choose only resources to which they have access. Their selection updates all elements of the user interface, including assets, findings, and settings controls. Users see the privileges attached to their roles and whether they can access or edit findings at their current scope.

The Security Command Center API and [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) also restrict functions to prescribed folders and projects. If calls to list or group assets and findings are made by users granted folder or project roles, only findings or assets at those scopes are returned.

For organization-level activations of Security Command Center, calls to create or update findings and finding notifications only support the organization scope. You need organization-level roles to perform these tasks.

To view the attack paths that are generated by attack path simulations, the appropriate permissions must be granted at the organization level and the Google Cloud console view must be set to the organization.

### Parent resources for findings

Usually, a finding is attached to a resource, like a virtual machine (VM) or firewall. Security Command Center attaches findings to the most immediate container for the resource that generated the finding. For example, if a VM generates a finding, the finding is attached to the project that contains the VM. Findings that are not connected to a Google Cloud resource are attached to the organization and are visible to anyone with organization-level Security Command Center permissions.

## Security Command Center roles

The following IAM roles are available for Security Command Center. You can grant these roles at the organization, folder, or project level.

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
  
## Security Command Center Management API roles

The following IAM roles are available for the Security Command Center Management API. You can grant these roles at the organization, folder, or project level.

Role | Permissions  
---|---  
  
#### Security Center Management Admin 

(`roles/securitycentermanagement.admin`) Full access to manage Cloud Security Command Center services and custom modules configuration.  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.organizationsettings.*`

  * `securitycenter.organizationsettings.get`
  * `securitycenter.organizationsettings.update`

`securitycenter.securitycentersettings.*`

  * `securitycenter.securitycentersettings.get`
  * `securitycenter.securitycentersettings.update`

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

  
  
#### Security Center Management Editor 

(`roles/securitycentermanagement.editor`) Editor role for Security Center Management  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.organizationsettings.get` `securitycenter.securitycentersettings.get` `securitycentermanagement.billingMetadata.get` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.*`

  * `securitycentermanagement.eventThreatDetectionCustomModules.create`
  * `securitycentermanagement.eventThreatDetectionCustomModules.delete`
  * `securitycentermanagement.eventThreatDetectionCustomModules.get`
  * `securitycentermanagement.eventThreatDetectionCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.update`
  * `securitycentermanagement.eventThreatDetectionCustomModules.validate`

`securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.operations.*`

  * `securitycentermanagement.operations.cancel`
  * `securitycentermanagement.operations.delete`
  * `securitycentermanagement.operations.get`
  * `securitycentermanagement.operations.list`

`securitycentermanagement.securityCenter.get` `securitycentermanagement.securityCenter.migrate` `securitycentermanagement.securityCenterServices.*`

  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`

`securitycentermanagement.securityCommandCenter.*`

  * `securitycentermanagement.securityCommandCenter.activate`
  * `securitycentermanagement.securityCommandCenter.checkActivationOperation`
  * `securitycentermanagement.securityCommandCenter.checkEligibility`
  * `securitycentermanagement.securityCommandCenter.checkOnboardingStatus`
  * `securitycentermanagement.securityCommandCenter.generateServiceAccounts`
  * `securitycentermanagement.securityCommandCenter.get`
  * `securitycentermanagement.securityCommandCenter.update`

`securitycentermanagement.securityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.securityHealthAnalyticsCustomModules.create`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.delete`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.test`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.update`

  
  
#### Security Center Management Viewer 

(`roles/securitycentermanagement.viewer`) Readonly access to Cloud Security Command Center services and custom modules configuration.  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.organizationsettings.get` `securitycenter.securitycentersettings.get` `securitycentermanagement.billingMetadata.get` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.get` `securitycentermanagement.eventThreatDetectionCustomModules.list` `securitycentermanagement.eventThreatDetectionCustomModules.validate` `securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.operations.get` `securitycentermanagement.operations.list` `securitycentermanagement.securityCenter.get` `securitycentermanagement.securityCenterServices.get` `securitycentermanagement.securityCenterServices.list` `securitycentermanagement.securityCommandCenter.checkActivationOperation` `securitycentermanagement.securityCommandCenter.checkEligibility` `securitycentermanagement.securityCommandCenter.checkOnboardingStatus` `securitycentermanagement.securityCommandCenter.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.test`  
  
#### Security Center Management Custom Modules Editor 

(`roles/securitycentermanagement.customModulesEditor`) Full access to manage Cloud Security Command Center custom modules.  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.*`

  * `securitycentermanagement.eventThreatDetectionCustomModules.create`
  * `securitycentermanagement.eventThreatDetectionCustomModules.delete`
  * `securitycentermanagement.eventThreatDetectionCustomModules.get`
  * `securitycentermanagement.eventThreatDetectionCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.update`
  * `securitycentermanagement.eventThreatDetectionCustomModules.validate`

`securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.securityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.securityHealthAnalyticsCustomModules.create`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.delete`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.test`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.update`

  
  
#### Security Center Management Custom Modules Viewer 

(`roles/securitycentermanagement.customModulesViewer`) Readonly access to Cloud Security Command Center custom modules.  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.get` `securitycentermanagement.eventThreatDetectionCustomModules.list` `securitycentermanagement.eventThreatDetectionCustomModules.validate` `securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.test`  
  
#### Security Center Management Custom ETD Modules Editor 

(`roles/securitycentermanagement.etdCustomModulesEditor`) Full access to manage Cloud Security Command Center ETD custom modules.  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.*`

  * `securitycentermanagement.eventThreatDetectionCustomModules.create`
  * `securitycentermanagement.eventThreatDetectionCustomModules.delete`
  * `securitycentermanagement.eventThreatDetectionCustomModules.get`
  * `securitycentermanagement.eventThreatDetectionCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.update`
  * `securitycentermanagement.eventThreatDetectionCustomModules.validate`

`securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

  
  
#### Security Center Management ETD Custom Modules Viewer 

(`roles/securitycentermanagement.etdCustomModulesViewer`) Readonly access to Cloud Security Command Center ETD custom modules.  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.get` `securitycentermanagement.eventThreatDetectionCustomModules.list` `securitycentermanagement.eventThreatDetectionCustomModules.validate` `securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

  
  
#### Security Center Management Services Editor 

(`roles/securitycentermanagement.securityCenterServicesEditor`) Full access to manage Cloud Security Command Center services configuration.  |  `securitycentermanagement.securityCenterServices.*`

  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`

  
  
#### Security Center Management Services Viewer 

(`roles/securitycentermanagement.securityCenterServicesViewer`) Readonly access to Cloud Security Command Center services configuration.  |  `securitycentermanagement.securityCenterServices.get` `securitycentermanagement.securityCenterServices.list`  
  
#### Security Center Management Settings Editor 

(`roles/securitycentermanagement.settingsEditor`) Full access to manage Cloud Security Command Center settings  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.organizationsettings.*`

  * `securitycenter.organizationsettings.get`
  * `securitycenter.organizationsettings.update`

`securitycenter.securitycentersettings.*`

  * `securitycenter.securitycentersettings.get`
  * `securitycenter.securitycentersettings.update`

`securitycentermanagement.billingMetadata.get` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.*`

  * `securitycentermanagement.eventThreatDetectionCustomModules.create`
  * `securitycentermanagement.eventThreatDetectionCustomModules.delete`
  * `securitycentermanagement.eventThreatDetectionCustomModules.get`
  * `securitycentermanagement.eventThreatDetectionCustomModules.list`
  * `securitycentermanagement.eventThreatDetectionCustomModules.update`
  * `securitycentermanagement.eventThreatDetectionCustomModules.validate`

`securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.securityCenterServices.*`

  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`

`securitycentermanagement.securityCommandCenter.*`

  * `securitycentermanagement.securityCommandCenter.activate`
  * `securitycentermanagement.securityCommandCenter.checkActivationOperation`
  * `securitycentermanagement.securityCommandCenter.checkEligibility`
  * `securitycentermanagement.securityCommandCenter.checkOnboardingStatus`
  * `securitycentermanagement.securityCommandCenter.generateServiceAccounts`
  * `securitycentermanagement.securityCommandCenter.get`
  * `securitycentermanagement.securityCommandCenter.update`

`securitycentermanagement.securityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.securityHealthAnalyticsCustomModules.create`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.delete`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.test`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.update`

  
  
#### Security Center Management Settings Viewer 

(`roles/securitycentermanagement.settingsViewer`) Readonly access to Cloud Security Command Center settings  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycenter.organizationsettings.get` `securitycenter.securitycentersettings.get` `securitycentermanagement.billingMetadata.get` `securitycentermanagement.effectiveEventThreatDetectionCustomModules.*`

  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`
  * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.eventThreatDetectionCustomModules.get` `securitycentermanagement.eventThreatDetectionCustomModules.list` `securitycentermanagement.eventThreatDetectionCustomModules.validate` `securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.securityCenterServices.get` `securitycentermanagement.securityCenterServices.list` `securitycentermanagement.securityCommandCenter.checkActivationOperation` `securitycentermanagement.securityCommandCenter.checkOnboardingStatus` `securitycentermanagement.securityCommandCenter.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.test`  
  
#### Security Center Management SHA Custom Modules Editor 

(`roles/securitycentermanagement.shaCustomModulesEditor`) Full access to manage Cloud Security Command Center SHA custom modules.  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.securityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.securityHealthAnalyticsCustomModules.create`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.delete`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.list`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.test`
  * `securitycentermanagement.securityHealthAnalyticsCustomModules.update`

  
  
#### Security Center Management SHA Custom Modules Viewer 

(`roles/securitycentermanagement.shaCustomModulesViewer`) Readonly access to Cloud Security Command Center SHA custom modules.  |  `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.locations.*`

  * `securitycentermanagement.locations.get`
  * `securitycentermanagement.locations.list`

`securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate` `securitycentermanagement.securityHealthAnalyticsCustomModules.test`  
  
## IAM roles in Compliance Manager

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The following is a list of IAM roles and permissions available for the Compliance Manager service. You can grant these roles at the organization, folder, or project level.

Role | Permissions  
---|---  
  
#### Compliance Manager Admin 

(`roles/cloudsecuritycompliance.admin`) Full access to Compliance Manager resources.  |  `auditmanager.auditReports.*`

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

`cloudsecuritycompliance.*`

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

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Compliance Manager Viewer 

(`roles/cloudsecuritycompliance.viewer`) Readonly access to Compliance Manager resources.  |  `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

  * `auditmanager.controlReports.get`
  * `auditmanager.controlReports.list`

`auditmanager.controls.list` `auditmanager.findings.list` `auditmanager.locations.get` `auditmanager.locations.list` `auditmanager.operations.*`

  * `auditmanager.operations.get`
  * `auditmanager.operations.list`

`auditmanager.resourceEnrollmentStatuses.*`

  * `auditmanager.resourceEnrollmentStatuses.get`
  * `auditmanager.resourceEnrollmentStatuses.list`

`cloudsecuritycompliance.auditReports.get` `cloudsecuritycompliance.auditReports.list` `cloudsecuritycompliance.billingSettings.get` `cloudsecuritycompliance.cloudControlDeployments.get` `cloudsecuritycompliance.cloudControlDeployments.list` `cloudsecuritycompliance.cloudControlPredictions.get` `cloudsecuritycompliance.cloudControlPredictions.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.cmEnrollments.get` `cloudsecuritycompliance.controlComplianceSummaries.list` `cloudsecuritycompliance.controlReports.get` `cloudsecuritycompliance.controls.*`

  * `cloudsecuritycompliance.controls.get`
  * `cloudsecuritycompliance.controls.list`

`cloudsecuritycompliance.findingSummaries.list` `cloudsecuritycompliance.findings.list` `cloudsecuritycompliance.frameworkAudits.get` `cloudsecuritycompliance.frameworkAudits.list` `cloudsecuritycompliance.frameworkComplianceReports.*`

  * `cloudsecuritycompliance.frameworkComplianceReports.aggregate`
  * `cloudsecuritycompliance.frameworkComplianceReports.get`

`cloudsecuritycompliance.frameworkComplianceSummaries.list` `cloudsecuritycompliance.frameworkDeployments.get` `cloudsecuritycompliance.frameworkDeployments.list` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `cloudsecuritycompliance.locations.get` `cloudsecuritycompliance.locations.list` `cloudsecuritycompliance.operations.get` `cloudsecuritycompliance.operations.list` `cloudsecuritycompliance.resourceEnrollmentStatuses.*`

  * `cloudsecuritycompliance.resourceEnrollmentStatuses.get`
  * `cloudsecuritycompliance.resourceEnrollmentStatuses.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Security Compliance Service Agent 

(`roles/cloudsecuritycompliance.serviceAgent`) Gives CSC Service Account access to consumer resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `accessapproval.settings.get` `aiplatform.customJobs.get` `aiplatform.customJobs.list` `aiplatform.datasets.get` `aiplatform.datasets.list` `aiplatform.endpoints.get` `aiplatform.endpoints.list` `aiplatform.featurestores.get` `aiplatform.featurestores.list` `aiplatform.hyperparameterTuningJobs.get` `aiplatform.hyperparameterTuningJobs.list` `aiplatform.metadataStores.get` `aiplatform.metadataStores.list` `aiplatform.models.get` `aiplatform.models.list` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.trainingPipelines.get` `aiplatform.trainingPipelines.list` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `axt.labels.get` `bigquery.datasets.get` `binaryauthorization.policy.get` `certificatemanager.certs.list` `certificatemanager.trustconfigs.list` `cloudasset.assets.analyzeIamPolicy` `cloudasset.assets.analyzeMove` `cloudasset.assets.analyzeOrgPolicy` `cloudasset.assets.exportAccessLevel` `cloudasset.assets.exportAccessPolicy` `cloudasset.assets.exportAiplatformBatchPredictionJobs` `cloudasset.assets.exportAiplatformCustomJobs` `cloudasset.assets.exportAiplatformDataLabelingJobs` `cloudasset.assets.exportAiplatformDatasets` `cloudasset.assets.exportAiplatformEndpoints` `cloudasset.assets.exportAiplatformHyperparameterTuningJobs` `cloudasset.assets.exportAiplatformMetadataStores` `cloudasset.assets.exportAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.exportAiplatformModels` `cloudasset.assets.exportAiplatformPipelineJobs` `cloudasset.assets.exportAiplatformSpecialistPools` `cloudasset.assets.exportAiplatformTrainingPipelines` `cloudasset.assets.exportAllAccessPolicy` `cloudasset.assets.exportAnthosConnectedCluster` `cloudasset.assets.exportAnthosedgeCluster` `cloudasset.assets.exportApigatewayApi` `cloudasset.assets.exportApigatewayApiConfig` `cloudasset.assets.exportApigatewayGateway` `cloudasset.assets.exportApikeysKeys` `cloudasset.assets.exportAppengineApplications` `cloudasset.assets.exportAppengineServices` `cloudasset.assets.exportAppengineVersions` `cloudasset.assets.exportArtifactregistryDockerImages` `cloudasset.assets.exportArtifactregistryRepositories` `cloudasset.assets.exportAssuredWorkloadsWorkloads` `cloudasset.assets.exportBeyondCorpApiGateways` `cloudasset.assets.exportBeyondCorpAppConnections` `cloudasset.assets.exportBeyondCorpAppConnectors` `cloudasset.assets.exportBeyondCorpAppGateways` `cloudasset.assets.exportBeyondCorpClientConnectorServices` `cloudasset.assets.exportBeyondCorpClientGateways` `cloudasset.assets.exportBigqueryDatasets` `cloudasset.assets.exportBigqueryModels` `cloudasset.assets.exportBigqueryTables` `cloudasset.assets.exportBigtableAppProfile` `cloudasset.assets.exportBigtableBackup` `cloudasset.assets.exportBigtableCluster` `cloudasset.assets.exportBigtableInstance` `cloudasset.assets.exportBigtableTable` `cloudasset.assets.exportCloudAssetFeeds` `cloudasset.assets.exportCloudDeployDeliveryPipelines` `cloudasset.assets.exportCloudDeployReleases` `cloudasset.assets.exportCloudDeployRollouts` `cloudasset.assets.exportCloudDeployTargets` `cloudasset.assets.exportCloudDocumentAIEvaluation` `cloudasset.assets.exportCloudDocumentAIHumanReviewConfig` `cloudasset.assets.exportCloudDocumentAILabelerPool` `cloudasset.assets.exportCloudDocumentAIProcessor` `cloudasset.assets.exportCloudDocumentAIProcessorVersion` `cloudasset.assets.exportCloudbillingBillingAccounts` `cloudasset.assets.exportCloudbillingProjectBillingInfos` `cloudasset.assets.exportCloudfunctionsFunctions` `cloudasset.assets.exportCloudfunctionsGen2Functions` `cloudasset.assets.exportCloudkmsCryptoKeyVersions` `cloudasset.assets.exportCloudkmsCryptoKeys` `cloudasset.assets.exportCloudkmsEkmConnections` `cloudasset.assets.exportCloudkmsImportJobs` `cloudasset.assets.exportCloudkmsKeyRings` `cloudasset.assets.exportCloudmemcacheInstances` `cloudasset.assets.exportCloudresourcemanagerFolders` `cloudasset.assets.exportCloudresourcemanagerOrganizations` `cloudasset.assets.exportCloudresourcemanagerProjects` `cloudasset.assets.exportCloudresourcemanagerTagBindings` `cloudasset.assets.exportCloudresourcemanagerTagKeys` `cloudasset.assets.exportCloudresourcemanagerTagValues` `cloudasset.assets.exportComposerEnvironments` `cloudasset.assets.exportComputeAddress` `cloudasset.assets.exportComputeAutoscalers` `cloudasset.assets.exportComputeBackendBuckets` `cloudasset.assets.exportComputeBackendServices` `cloudasset.assets.exportComputeCommitments` `cloudasset.assets.exportComputeDisks` `cloudasset.assets.exportComputeExternalVpnGateways` `cloudasset.assets.exportComputeFirewallPolicies` `cloudasset.assets.exportComputeFirewalls` `cloudasset.assets.exportComputeForwardingRules` `cloudasset.assets.exportComputeGlobalAddress` `cloudasset.assets.exportComputeGlobalForwardingRules` `cloudasset.assets.exportComputeHealthChecks` `cloudasset.assets.exportComputeHttpHealthChecks` `cloudasset.assets.exportComputeHttpsHealthChecks` `cloudasset.assets.exportComputeImages` `cloudasset.assets.exportComputeInstanceGroupManagers` `cloudasset.assets.exportComputeInstanceGroups` `cloudasset.assets.exportComputeInstanceTemplates` `cloudasset.assets.exportComputeInstances` `cloudasset.assets.exportComputeInterconnect` `cloudasset.assets.exportComputeInterconnectAttachment` `cloudasset.assets.exportComputeLicenses` `cloudasset.assets.exportComputeNetworkEndpointGroups` `cloudasset.assets.exportComputeNetworks` `cloudasset.assets.exportComputeNodeGroups` `cloudasset.assets.exportComputeNodeTemplates` `cloudasset.assets.exportComputePacketMirrorings` `cloudasset.assets.exportComputeProjects` `cloudasset.assets.exportComputeRegionAutoscaler` `cloudasset.assets.exportComputeRegionBackendServices` `cloudasset.assets.exportComputeRegionDisk` `cloudasset.assets.exportComputeRegionInstanceGroup` `cloudasset.assets.exportComputeRegionInstanceGroupManager` `cloudasset.assets.exportComputeReservations` `cloudasset.assets.exportComputeResourcePolicies` `cloudasset.assets.exportComputeRouters` `cloudasset.assets.exportComputeRoutes` `cloudasset.assets.exportComputeSecurityPolicy` `cloudasset.assets.exportComputeServiceAttachments` `cloudasset.assets.exportComputeSnapshots` `cloudasset.assets.exportComputeSslCertificates` `cloudasset.assets.exportComputeSslPolicies` `cloudasset.assets.exportComputeSubnetworks` `cloudasset.assets.exportComputeTargetHttpProxies` `cloudasset.assets.exportComputeTargetHttpsProxies` `cloudasset.assets.exportComputeTargetInstances` `cloudasset.assets.exportComputeTargetPools` `cloudasset.assets.exportComputeTargetSslProxies` `cloudasset.assets.exportComputeTargetTcpProxies` `cloudasset.assets.exportComputeTargetVpnGateways` `cloudasset.assets.exportComputeUrlMaps` `cloudasset.assets.exportComputeVpnGateways` `cloudasset.assets.exportComputeVpnTunnels` `cloudasset.assets.exportConnectorsConnections` `cloudasset.assets.exportConnectorsConnectorVersions` `cloudasset.assets.exportConnectorsConnectors` `cloudasset.assets.exportConnectorsProviders` `cloudasset.assets.exportConnectorsRuntimeConfigs` `cloudasset.assets.exportContainerAppsDeployment` `cloudasset.assets.exportContainerAppsReplicaSets` `cloudasset.assets.exportContainerBatchJobs` `cloudasset.assets.exportContainerClusterrole` `cloudasset.assets.exportContainerClusterrolebinding` `cloudasset.assets.exportContainerClusters` `cloudasset.assets.exportContainerExtensionsIngresses` `cloudasset.assets.exportContainerJobs` `cloudasset.assets.exportContainerNamespace` `cloudasset.assets.exportContainerNetworkingIngresses` `cloudasset.assets.exportContainerNetworkingNetworkPolicies` `cloudasset.assets.exportContainerNode` `cloudasset.assets.exportContainerNodepool` `cloudasset.assets.exportContainerPod` `cloudasset.assets.exportContainerReplicaSets` `cloudasset.assets.exportContainerRole` `cloudasset.assets.exportContainerRolebinding` `cloudasset.assets.exportContainerServices` `cloudasset.assets.exportContainerregistryImage` `cloudasset.assets.exportDataMigrationConnectionProfiles` `cloudasset.assets.exportDataMigrationMigrationJobs` `cloudasset.assets.exportDataflowJobs` `cloudasset.assets.exportDatafusionInstance` `cloudasset.assets.exportDataplexAssets` `cloudasset.assets.exportDataplexLakes` `cloudasset.assets.exportDataplexTasks` `cloudasset.assets.exportDataplexZones` `cloudasset.assets.exportDataprocAutoscalingPolicies` `cloudasset.assets.exportDataprocBatches` `cloudasset.assets.exportDataprocClusters` `cloudasset.assets.exportDataprocJobs` `cloudasset.assets.exportDataprocSessions` `cloudasset.assets.exportDataprocWorkflowTemplates` `cloudasset.assets.exportDatastreamConnectionProfile` `cloudasset.assets.exportDatastreamPrivateConnection` `cloudasset.assets.exportDatastreamStream` `cloudasset.assets.exportDialogflowAgents` `cloudasset.assets.exportDialogflowConversationProfiles` `cloudasset.assets.exportDialogflowKnowledgeBases` `cloudasset.assets.exportDialogflowLocationSettings` `cloudasset.assets.exportDlpDeidentifyTemplates` `cloudasset.assets.exportDlpDlpJobs` `cloudasset.assets.exportDlpInspectTemplates` `cloudasset.assets.exportDlpJobTriggers` `cloudasset.assets.exportDlpStoredInfoTypes` `cloudasset.assets.exportDnsManagedZones` `cloudasset.assets.exportDnsPolicies` `cloudasset.assets.exportDomainsRegistrations` `cloudasset.assets.exportEventarcTriggers` `cloudasset.assets.exportFileBackups` `cloudasset.assets.exportFileInstances` `cloudasset.assets.exportFirebaseAppInfos` `cloudasset.assets.exportFirebaseProjects` `cloudasset.assets.exportFirestoreDatabases` `cloudasset.assets.exportGKEHubFeatures` `cloudasset.assets.exportGKEHubMemberships` `cloudasset.assets.exportGameservicesGameServerClusters` `cloudasset.assets.exportGameservicesGameServerConfigs` `cloudasset.assets.exportGameservicesGameServerDeployments` `cloudasset.assets.exportGameservicesRealms` `cloudasset.assets.exportGkeBackupBackupPlans` `cloudasset.assets.exportGkeBackupBackups` `cloudasset.assets.exportGkeBackupRestorePlans` `cloudasset.assets.exportGkeBackupRestores` `cloudasset.assets.exportGkeBackupVolumeBackups` `cloudasset.assets.exportGkeBackupVolumeRestores` `cloudasset.assets.exportHealthcareConsentStores` `cloudasset.assets.exportHealthcareDatasets` `cloudasset.assets.exportHealthcareDicomStores` `cloudasset.assets.exportHealthcareFhirStores` `cloudasset.assets.exportHealthcareHl7V2Stores` `cloudasset.assets.exportIamPolicy` `cloudasset.assets.exportIamRoles` `cloudasset.assets.exportIamServiceAccountKeys` `cloudasset.assets.exportIamServiceAccounts` `cloudasset.assets.exportIapTunnel` `cloudasset.assets.exportIapTunnelInstances` `cloudasset.assets.exportIapTunnelZones` `cloudasset.assets.exportIapWeb` `cloudasset.assets.exportIapWebServiceVersion` `cloudasset.assets.exportIapWebServices` `cloudasset.assets.exportIapWebType` `cloudasset.assets.exportIdsEndpoints` `cloudasset.assets.exportIntegrationsAuthConfigs` `cloudasset.assets.exportIntegrationsCertificates` `cloudasset.assets.exportIntegrationsExecutions` `cloudasset.assets.exportIntegrationsIntegrationVersions` `cloudasset.assets.exportIntegrationsIntegrations` `cloudasset.assets.exportIntegrationsSfdcChannels` `cloudasset.assets.exportIntegrationsSfdcInstances` `cloudasset.assets.exportIntegrationsSuspensions` `cloudasset.assets.exportLoggingLogMetrics` `cloudasset.assets.exportLoggingLogSinks` `cloudasset.assets.exportManagedidentitiesDomain` `cloudasset.assets.exportMetastoreBackups` `cloudasset.assets.exportMetastoreMetadataImports` `cloudasset.assets.exportMetastoreServices` `cloudasset.assets.exportMonitoringAlertPolicies` `cloudasset.assets.exportNetworkConnectivityHubs` `cloudasset.assets.exportNetworkConnectivitySpokes` `cloudasset.assets.exportNetworkManagementConnectivityTests` `cloudasset.assets.exportNetworkServicesEndpointPolicies` `cloudasset.assets.exportNetworkServicesGateways` `cloudasset.assets.exportNetworkServicesGrpcRoutes` `cloudasset.assets.exportNetworkServicesHttpRoutes` `cloudasset.assets.exportNetworkServicesMeshes` `cloudasset.assets.exportNetworkServicesServiceBindings` `cloudasset.assets.exportNetworkServicesTcpRoutes` `cloudasset.assets.exportNetworkServicesTlsRoutes` `cloudasset.assets.exportOSConfigOSPolicyAssignmentReports` `cloudasset.assets.exportOSConfigOSPolicyAssignments` `cloudasset.assets.exportOSConfigVulnerabilityReports` `cloudasset.assets.exportOSInventories` `cloudasset.assets.exportOrgPolicy` `cloudasset.assets.exportPatchDeployments` `cloudasset.assets.exportPubsubSnapshots` `cloudasset.assets.exportPubsubSubscriptions` `cloudasset.assets.exportPubsubTopics` `cloudasset.assets.exportRedisInstances` `cloudasset.assets.exportResource` `cloudasset.assets.exportSecretManagerSecretVersions` `cloudasset.assets.exportSecretManagerSecrets` `cloudasset.assets.exportServiceDirectoryNamespaces` `cloudasset.assets.exportServicePerimeter` `cloudasset.assets.exportServiceconsumermanagementConsumerProperty` `cloudasset.assets.exportServiceconsumermanagementConsumerQuotaLimits` `cloudasset.assets.exportServiceconsumermanagementConsumers` `cloudasset.assets.exportServiceconsumermanagementProducerOverrides` `cloudasset.assets.exportServiceconsumermanagementTenancyUnits` `cloudasset.assets.exportServiceconsumermanagementVisibility` `cloudasset.assets.exportServicemanagementServices` `cloudasset.assets.exportServiceusageAdminOverrides` `cloudasset.assets.exportServiceusageConsumerOverrides` `cloudasset.assets.exportServiceusageServices` `cloudasset.assets.exportSpannerBackups` `cloudasset.assets.exportSpannerDatabases` `cloudasset.assets.exportSpannerInstances` `cloudasset.assets.exportSpeakerIdPhrases` `cloudasset.assets.exportSpeakerIdSettings` `cloudasset.assets.exportSpeakerIdSpeakers` `cloudasset.assets.exportSpeechCustomClasses` `cloudasset.assets.exportSpeechPhraseSets` `cloudasset.assets.exportSqladminBackupRuns` `cloudasset.assets.exportSqladminInstances` `cloudasset.assets.exportStorageBuckets` `cloudasset.assets.exportTpuNodes` `cloudasset.assets.exportVpcaccessConnector` `cloudasset.assets.listAccessLevel` `cloudasset.assets.listAccessPolicy` `cloudasset.assets.listAiplatformBatchPredictionJobs` `cloudasset.assets.listAiplatformCustomJobs` `cloudasset.assets.listAiplatformDataLabelingJobs` `cloudasset.assets.listAiplatformDatasets` `cloudasset.assets.listAiplatformEndpoints` `cloudasset.assets.listAiplatformHyperparameterTuningJobs` `cloudasset.assets.listAiplatformMetadataStores` `cloudasset.assets.listAiplatformModelDeploymentMonitoringJobs` `cloudasset.assets.listAiplatformModels` `cloudasset.assets.listAiplatformPipelineJobs` `cloudasset.assets.listAiplatformSpecialistPools` `cloudasset.assets.listAiplatformTrainingPipelines` `cloudasset.assets.listAllAccessPolicy` `cloudasset.assets.listAnthosConnectedCluster` `cloudasset.assets.listAnthosedgeCluster` `cloudasset.assets.listApigatewayApi` `cloudasset.assets.listApigatewayApiConfig` `cloudasset.assets.listApigatewayGateway` `cloudasset.assets.listApikeysKeys` `cloudasset.assets.listAppengineApplications` `cloudasset.assets.listAppengineServices` `cloudasset.assets.listAppengineVersions` `cloudasset.assets.listArtifactregistryDockerImages` `cloudasset.assets.listArtifactregistryRepositories` `cloudasset.assets.listAssuredWorkloadsWorkloads` `cloudasset.assets.listBeyondCorpApiGateways` `cloudasset.assets.listBeyondCorpAppConnections` `cloudasset.assets.listBeyondCorpAppConnectors` `cloudasset.assets.listBeyondCorpAppGateways` `cloudasset.assets.listBeyondCorpClientConnectorServices` `cloudasset.assets.listBeyondCorpClientGateways` `cloudasset.assets.listBigqueryDatasets` `cloudasset.assets.listBigqueryModels` `cloudasset.assets.listBigqueryTables` `cloudasset.assets.listBigtableAppProfile` `cloudasset.assets.listBigtableBackup` `cloudasset.assets.listBigtableCluster` `cloudasset.assets.listBigtableInstance` `cloudasset.assets.listBigtableTable` `cloudasset.assets.listCloudAssetFeeds` `cloudasset.assets.listCloudDeployDeliveryPipelines` `cloudasset.assets.listCloudDeployReleases` `cloudasset.assets.listCloudDeployRollouts` `cloudasset.assets.listCloudDeployTargets` `cloudasset.assets.listCloudDocumentAIEvaluation` `cloudasset.assets.listCloudDocumentAIHumanReviewConfig` `cloudasset.assets.listCloudDocumentAILabelerPool` `cloudasset.assets.listCloudDocumentAIProcessor` `cloudasset.assets.listCloudDocumentAIProcessorVersion` `cloudasset.assets.listCloudbillingBillingAccounts` `cloudasset.assets.listCloudbillingProjectBillingInfos` `cloudasset.assets.listCloudfunctionsFunctions` `cloudasset.assets.listCloudfunctionsGen2Functions` `cloudasset.assets.listCloudkmsCryptoKeyVersions` `cloudasset.assets.listCloudkmsCryptoKeys` `cloudasset.assets.listCloudkmsEkmConnections` `cloudasset.assets.listCloudkmsImportJobs` `cloudasset.assets.listCloudkmsKeyRings` `cloudasset.assets.listCloudmemcacheInstances` `cloudasset.assets.listCloudresourcemanagerFolders` `cloudasset.assets.listCloudresourcemanagerOrganizations` `cloudasset.assets.listCloudresourcemanagerProjects` `cloudasset.assets.listCloudresourcemanagerTagBindings` `cloudasset.assets.listCloudresourcemanagerTagKeys` `cloudasset.assets.listCloudresourcemanagerTagValues` `cloudasset.assets.listComposerEnvironments` `cloudasset.assets.listComputeAddress` `cloudasset.assets.listComputeAutoscalers` `cloudasset.assets.listComputeBackendBuckets` `cloudasset.assets.listComputeBackendServices` `cloudasset.assets.listComputeCommitments` `cloudasset.assets.listComputeDisks` `cloudasset.assets.listComputeExternalVpnGateways` `cloudasset.assets.listComputeFirewallPolicies` `cloudasset.assets.listComputeFirewalls` `cloudasset.assets.listComputeForwardingRules` `cloudasset.assets.listComputeGlobalAddress` `cloudasset.assets.listComputeGlobalForwardingRules` `cloudasset.assets.listComputeHealthChecks` `cloudasset.assets.listComputeHttpHealthChecks` `cloudasset.assets.listComputeHttpsHealthChecks` `cloudasset.assets.listComputeImages` `cloudasset.assets.listComputeInstanceGroupManagers` `cloudasset.assets.listComputeInstanceGroups` `cloudasset.assets.listComputeInstanceTemplates` `cloudasset.assets.listComputeInstances` `cloudasset.assets.listComputeInterconnect` `cloudasset.assets.listComputeInterconnectAttachment` `cloudasset.assets.listComputeLicenses` `cloudasset.assets.listComputeNetworkEndpointGroups` `cloudasset.assets.listComputeNetworks` `cloudasset.assets.listComputeNodeGroups` `cloudasset.assets.listComputeNodeTemplates` `cloudasset.assets.listComputePacketMirrorings` `cloudasset.assets.listComputeProjects` `cloudasset.assets.listComputeRegionAutoscaler` `cloudasset.assets.listComputeRegionBackendServices` `cloudasset.assets.listComputeRegionDisk` `cloudasset.assets.listComputeRegionInstanceGroup` `cloudasset.assets.listComputeRegionInstanceGroupManager` `cloudasset.assets.listComputeReservations` `cloudasset.assets.listComputeResourcePolicies` `cloudasset.assets.listComputeRouters` `cloudasset.assets.listComputeRoutes` `cloudasset.assets.listComputeSecurityPolicy` `cloudasset.assets.listComputeServiceAttachments` `cloudasset.assets.listComputeSnapshots` `cloudasset.assets.listComputeSslCertificates` `cloudasset.assets.listComputeSslPolicies` `cloudasset.assets.listComputeSubnetworks` `cloudasset.assets.listComputeTargetHttpProxies` `cloudasset.assets.listComputeTargetHttpsProxies` `cloudasset.assets.listComputeTargetInstances` `cloudasset.assets.listComputeTargetPools` `cloudasset.assets.listComputeTargetSslProxies` `cloudasset.assets.listComputeTargetTcpProxies` `cloudasset.assets.listComputeTargetVpnGateways` `cloudasset.assets.listComputeUrlMaps` `cloudasset.assets.listComputeVpnGateways` `cloudasset.assets.listComputeVpnTunnels` `cloudasset.assets.listConnectorsConnections` `cloudasset.assets.listConnectorsConnectorVersions` `cloudasset.assets.listConnectorsConnectors` `cloudasset.assets.listConnectorsProviders` `cloudasset.assets.listConnectorsRuntimeConfigs` `cloudasset.assets.listContainerAppsDeployment` `cloudasset.assets.listContainerAppsReplicaSets` `cloudasset.assets.listContainerBatchJobs` `cloudasset.assets.listContainerClusterrole` `cloudasset.assets.listContainerClusterrolebinding` `cloudasset.assets.listContainerClusters` `cloudasset.assets.listContainerExtensionsIngresses` `cloudasset.assets.listContainerJobs` `cloudasset.assets.listContainerNamespace` `cloudasset.assets.listContainerNetworkingIngresses` `cloudasset.assets.listContainerNetworkingNetworkPolicies` `cloudasset.assets.listContainerNode` `cloudasset.assets.listContainerNodepool` `cloudasset.assets.listContainerPod` `cloudasset.assets.listContainerReplicaSets` `cloudasset.assets.listContainerRole` `cloudasset.assets.listContainerRolebinding` `cloudasset.assets.listContainerServices` `cloudasset.assets.listContainerregistryImage` `cloudasset.assets.listDataMigrationConnectionProfiles` `cloudasset.assets.listDataMigrationMigrationJobs` `cloudasset.assets.listDataflowJobs` `cloudasset.assets.listDatafusionInstance` `cloudasset.assets.listDataplexAssets` `cloudasset.assets.listDataplexLakes` `cloudasset.assets.listDataplexTasks` `cloudasset.assets.listDataplexZones` `cloudasset.assets.listDataprocAutoscalingPolicies` `cloudasset.assets.listDataprocBatches` `cloudasset.assets.listDataprocClusters` `cloudasset.assets.listDataprocJobs` `cloudasset.assets.listDataprocSessions` `cloudasset.assets.listDataprocWorkflowTemplates` `cloudasset.assets.listDatastreamConnectionProfile` `cloudasset.assets.listDatastreamPrivateConnection` `cloudasset.assets.listDatastreamStream` `cloudasset.assets.listDialogflowAgents` `cloudasset.assets.listDialogflowConversationProfiles` `cloudasset.assets.listDialogflowKnowledgeBases` `cloudasset.assets.listDialogflowLocationSettings` `cloudasset.assets.listDlpDeidentifyTemplates` `cloudasset.assets.listDlpDlpJobs` `cloudasset.assets.listDlpInspectTemplates` `cloudasset.assets.listDlpJobTriggers` `cloudasset.assets.listDlpStoredInfoTypes` `cloudasset.assets.listDnsManagedZones` `cloudasset.assets.listDnsPolicies` `cloudasset.assets.listDomainsRegistrations` `cloudasset.assets.listEventarcTriggers` `cloudasset.assets.listFileBackups` `cloudasset.assets.listFileInstances` `cloudasset.assets.listFirebaseAppInfos` `cloudasset.assets.listFirebaseProjects` `cloudasset.assets.listFirestoreDatabases` `cloudasset.assets.listGKEHubFeatures` `cloudasset.assets.listGKEHubMemberships` `cloudasset.assets.listGameservicesGameServerClusters` `cloudasset.assets.listGameservicesGameServerConfigs` `cloudasset.assets.listGameservicesGameServerDeployments` `cloudasset.assets.listGameservicesRealms` `cloudasset.assets.listGkeBackupBackupPlans` `cloudasset.assets.listGkeBackupBackups` `cloudasset.assets.listGkeBackupRestorePlans` `cloudasset.assets.listGkeBackupRestores` `cloudasset.assets.listGkeBackupVolumeBackups` `cloudasset.assets.listGkeBackupVolumeRestores` `cloudasset.assets.listHealthcareConsentStores` `cloudasset.assets.listHealthcareDatasets` `cloudasset.assets.listHealthcareDicomStores` `cloudasset.assets.listHealthcareFhirStores` `cloudasset.assets.listHealthcareHl7V2Stores` `cloudasset.assets.listIamPolicy` `cloudasset.assets.listIamRoles` `cloudasset.assets.listIamServiceAccountKeys` `cloudasset.assets.listIamServiceAccounts` `cloudasset.assets.listIapTunnel` `cloudasset.assets.listIapTunnelInstances` `cloudasset.assets.listIapTunnelZones` `cloudasset.assets.listIapWeb` `cloudasset.assets.listIapWebServiceVersion` `cloudasset.assets.listIapWebServices` `cloudasset.assets.listIapWebType` `cloudasset.assets.listIdsEndpoints` `cloudasset.assets.listIntegrationsAuthConfigs` `cloudasset.assets.listIntegrationsCertificates` `cloudasset.assets.listIntegrationsExecutions` `cloudasset.assets.listIntegrationsIntegrationVersions` `cloudasset.assets.listIntegrationsIntegrations` `cloudasset.assets.listIntegrationsSfdcChannels` `cloudasset.assets.listIntegrationsSfdcInstances` `cloudasset.assets.listIntegrationsSuspensions` `cloudasset.assets.listLoggingLogMetrics` `cloudasset.assets.listLoggingLogSinks` `cloudasset.assets.listManagedidentitiesDomain` `cloudasset.assets.listMetastoreBackups` `cloudasset.assets.listMetastoreMetadataImports` `cloudasset.assets.listMetastoreServices` `cloudasset.assets.listMonitoringAlertPolicies` `cloudasset.assets.listNetworkConnectivityHubs` `cloudasset.assets.listNetworkConnectivitySpokes` `cloudasset.assets.listNetworkManagementConnectivityTests` `cloudasset.assets.listNetworkServicesEndpointPolicies` `cloudasset.assets.listNetworkServicesGateways` `cloudasset.assets.listNetworkServicesGrpcRoutes` `cloudasset.assets.listNetworkServicesHttpRoutes` `cloudasset.assets.listNetworkServicesMeshes` `cloudasset.assets.listNetworkServicesServiceBindings` `cloudasset.assets.listNetworkServicesTcpRoutes` `cloudasset.assets.listNetworkServicesTlsRoutes` `cloudasset.assets.listOSConfigOSPolicyAssignmentReports` `cloudasset.assets.listOSConfigOSPolicyAssignments` `cloudasset.assets.listOSConfigVulnerabilityReports` `cloudasset.assets.listOSInventories` `cloudasset.assets.listOrgPolicy` `cloudasset.assets.listPatchDeployments` `cloudasset.assets.listPubsubSnapshots` `cloudasset.assets.listPubsubSubscriptions` `cloudasset.assets.listPubsubTopics` `cloudasset.assets.listRedisInstances` `cloudasset.assets.listResource` `cloudasset.assets.listRunDomainMapping` `cloudasset.assets.listRunRevision` `cloudasset.assets.listRunService` `cloudasset.assets.listSecretManagerSecretVersions` `cloudasset.assets.listSecretManagerSecrets` `cloudasset.assets.listServiceDirectoryNamespaces` `cloudasset.assets.listServicePerimeter` `cloudasset.assets.listServiceconsumermanagementConsumerProperty` `cloudasset.assets.listServiceconsumermanagementConsumerQuotaLimits` `cloudasset.assets.listServiceconsumermanagementConsumers` `cloudasset.assets.listServiceconsumermanagementProducerOverrides` `cloudasset.assets.listServiceconsumermanagementTenancyUnits` `cloudasset.assets.listServiceconsumermanagementVisibility` `cloudasset.assets.listServicemanagementServices` `cloudasset.assets.listServiceusageAdminOverrides` `cloudasset.assets.listServiceusageConsumerOverrides` `cloudasset.assets.listServiceusageServices` `cloudasset.assets.listSpannerBackups` `cloudasset.assets.listSpannerDatabases` `cloudasset.assets.listSpannerInstances` `cloudasset.assets.listSpeakerIdPhrases` `cloudasset.assets.listSpeakerIdSettings` `cloudasset.assets.listSpeakerIdSpeakers` `cloudasset.assets.listSpeechCustomClasses` `cloudasset.assets.listSpeechPhraseSets` `cloudasset.assets.listSqladminBackupRuns` `cloudasset.assets.listSqladminInstances` `cloudasset.assets.listStorageBuckets` `cloudasset.assets.listTpuNodes` `cloudasset.assets.listVpcaccessConnector` `cloudasset.assets.queryAccessPolicy` `cloudasset.assets.queryIamPolicy` `cloudasset.assets.queryOSInventories` `cloudasset.assets.queryResource` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `cloudasset.feeds.create` `cloudasset.feeds.delete` `cloudasset.feeds.get` `cloudasset.othercloudconnections.get` `cloudasset.othercloudconnections.list` `cloudasset.othercloudconnections.verify` `cloudasset.savedqueries.get` `cloudasset.savedqueries.list` `cloudkms.cryptoKeys.get` `cloudkms.cryptoKeys.list` `cloudkms.keyRings.list` `cloudsecuritycompliance.cloudControlDeployments.create` `cloudsecuritycompliance.cloudControlDeployments.delete` `cloudsecuritycompliance.cloudControlDeployments.get` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.frameworkDeployments.create` `cloudsecuritycompliance.frameworkDeployments.delete` `cloudsecuritycompliance.frameworkDeployments.get` `cloudsecuritycompliance.frameworkDeployments.list` `cloudsecuritycompliance.frameworks.create` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `cloudsecuritycompliance.operations.get` `cloudsecurityscanner.scans.get` `cloudsecurityscanner.scans.list` `cloudsql.instances.connect` `cloudsql.instances.get` `cloudsql.instances.list` `cloudsql.users.list` `compute.autoscalers.list` `compute.backendServices.list` `compute.disks.list` `compute.firewallPolicies.list` `compute.firewalls.list` `compute.forwardingRules.list` `compute.globalForwardingRules.list` `compute.instanceGroupManagers.list` `compute.instanceGroups.list` `compute.instances.get` `compute.instances.list` `compute.managedRulesets.*`

  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`

`compute.networks.list` `compute.regionSslPolicies.list` `compute.regionTargetHttpProxies.list` `compute.regionUrlMaps.list` `compute.routers.list` `compute.securityPolicies.list` `compute.sslCertificates.list` `compute.sslPolicies.list` `compute.subnetworks.list` `compute.targetHttpProxies.list` `compute.targetSslProxies.list` `compute.urlMaps.list` `compute.vpnGateways.list` `compute.zones.list` `container.clusters.get` `container.clusters.list` `discoveryengine.dataStores.get` `discoveryengine.dataStores.list` `dlp.fileStoreProfiles.list` `dlp.inspectTemplates.list` `dlp.jobTriggers.list` `dlp.jobs.list` `dlp.tableDataProfiles.get` `dns.managedZones.list` `iam.serviceAccountKeys.list` `iam.serviceAccounts.get` `iam.serviceAccounts.getIamPolicy` `logging.buckets.list` `logging.settings.update` `monitoring.alertPolicies.list` `monitoring.timeSeries.list` `notebooks.instances.get` `notebooks.instances.list` `orgpolicy.constraints.list` `orgpolicy.policy.get` `privateca.certificates.list` `recommender.cloudAssetInsights.get` `recommender.cloudAssetInsights.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.folders.get` `resourcemanager.folders.getIamPolicy` `resourcemanager.folders.list` `resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.hierarchyNodes.listTagBindings` `resourcemanager.organizations.get` `resourcemanager.organizations.getIamPolicy` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `resourcemanager.tagHolds.list` `resourcemanager.tagKeys.get` `resourcemanager.tagKeys.list` `resourcemanager.tagValues.get` `resourcemanager.tagValues.list` `securitycentermanagement.securityCenterServices.get` `securitycentermanagement.securityCenterServices.update` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list`  
  
## Security Posture API roles

The following IAM roles are available for the Security Posture API and its infrastructure as code (IaC) validation feature. Except as noted, you can grant these roles at the organization, folder, or project level.

Role | Permissions  
---|---  
  
#### Security Posture Admin 

(`roles/securityposture.admin`) Full access to Security Posture service APIs.  Lowest-level resources where you can grant this role:

  * Organization

|  `orgpolicy.*`

  * `orgpolicy.constraints.list`
  * `orgpolicy.customConstraints.create`
  * `orgpolicy.customConstraints.delete`
  * `orgpolicy.customConstraints.get`
  * `orgpolicy.customConstraints.list`
  * `orgpolicy.customConstraints.update`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`

`resourcemanager.organizations.get` `securitycenter.securityhealthanalyticssettings.*`

  * `securitycenter.securityhealthanalyticssettings.calculate`
  * `securitycenter.securityhealthanalyticssettings.get`
  * `securitycenter.securityhealthanalyticssettings.update`

`securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.*`

  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get`
  * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list`

`securitycentermanagement.securityCenterServices.*`

  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`

`securitycentermanagement.securityHealthAnalyticsCustomModules.create` `securitycentermanagement.securityHealthAnalyticsCustomModules.delete` `securitycentermanagement.securityHealthAnalyticsCustomModules.get` `securitycentermanagement.securityHealthAnalyticsCustomModules.list` `securitycentermanagement.securityHealthAnalyticsCustomModules.update` `securityposture.*`

  * `securityposture.locations.get`
  * `securityposture.locations.list`
  * `securityposture.operations.delete`
  * `securityposture.operations.get`
  * `securityposture.operations.list`
  * `securityposture.postureDeployments.create`
  * `securityposture.postureDeployments.delete`
  * `securityposture.postureDeployments.get`
  * `securityposture.postureDeployments.list`
  * `securityposture.postureDeployments.update`
  * `securityposture.postureTemplates.get`
  * `securityposture.postureTemplates.list`
  * `securityposture.postures.create`
  * `securityposture.postures.delete`
  * `securityposture.postures.extract`
  * `securityposture.postures.get`
  * `securityposture.postures.list`
  * `securityposture.postures.update`
  * `securityposture.reports.create`
  * `securityposture.reports.get`
  * `securityposture.reports.list`

  
  
#### Security Posture Viewer 

(`roles/securityposture.viewer`) Read only access to all the SecurityPosture Service resources.  |  `resourcemanager.organizations.get` `securityposture.locations.*`

  * `securityposture.locations.get`
  * `securityposture.locations.list`

`securityposture.operations.get` `securityposture.operations.list` `securityposture.postureDeployments.get` `securityposture.postureDeployments.list` `securityposture.postureTemplates.*`

  * `securityposture.postureTemplates.get`
  * `securityposture.postureTemplates.list`

`securityposture.postures.get` `securityposture.postures.list` `securityposture.reports.get` `securityposture.reports.list`  
  
#### Security Posture Deployer 

(`roles/securityposture.postureDeployer`) Mutate and read permissions to the Posture Deployment resource.  |  `orgpolicy.*`

  * `orgpolicy.constraints.list`
  * `orgpolicy.customConstraints.create`
  * `orgpolicy.customConstraints.delete`
  * `orgpolicy.customConstraints.get`
  * `orgpolicy.customConstraints.list`
  * `orgpolicy.customConstraints.update`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`

`resourcemanager.organizations.get` `securitycenter.securityhealthanalyticssettings.*`

  * `securitycenter.securityhealthanalyticssettings.calculate`
  * `securitycenter.securityhealthanalyticssettings.get`
  * `securitycenter.securityhealthanalyticssettings.update`

`securitycentermanagement.securityCenterServices.*`

  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`

`securitycentermanagement.securityHealthAnalyticsCustomModules.create` `securitycentermanagement.securityHealthAnalyticsCustomModules.delete` `securitycentermanagement.securityHealthAnalyticsCustomModules.update` `securityposture.operations.get` `securityposture.postureDeployments.*`

  * `securityposture.postureDeployments.create`
  * `securityposture.postureDeployments.delete`
  * `securityposture.postureDeployments.get`
  * `securityposture.postureDeployments.list`
  * `securityposture.postureDeployments.update`

  
  
#### Security Posture Deployments Viewer 

(`roles/securityposture.postureDeploymentsViewer`) Read only access to the Posture Deployment resource.  |  `resourcemanager.organizations.get` `securityposture.operations.get` `securityposture.postureDeployments.get` `securityposture.postureDeployments.list`  
  
#### Security Posture Resource Editor 

(`roles/securityposture.postureEditor`) Mutate and read permissions to the Posture resource.  |  `securityposture.operations.get` `securityposture.postures.*`

  * `securityposture.postures.create`
  * `securityposture.postures.delete`
  * `securityposture.postures.extract`
  * `securityposture.postures.get`
  * `securityposture.postures.list`
  * `securityposture.postures.update`

  
  
#### Security Posture Resource Viewer 

(`roles/securityposture.postureViewer`) Read only access to the Posture resource.  |  `resourcemanager.organizations.get` `securityposture.operations.get` `securityposture.postures.get` `securityposture.postures.list`  
  
#### Security Posture Shift-Left Validator 

(`roles/securityposture.reportCreator`) Create access for Reports, e.g. IaC Validation Report.  |  `securityposture.operations.get` `securityposture.reports.*`

  * `securityposture.reports.create`
  * `securityposture.reports.get`
  * `securityposture.reports.list`

  
  
## IAM roles in Data Security Posture Management

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The following is a list of IAM roles and permissions available for the Data Security Posture Management (DSPM) service. You can grant these roles at the organization, folder, or project level.

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
  
## Service agent roles

A service agent allows a service to access your resources.

After you activate Security Command Center, the following service agents are created for you:

  * `service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com`.

This service agent requires the `roles/securitycenter.serviceAgent` IAM role.

  * `service-org-ORGANIZATION_ID@gcp-sa-ktd-hpsa.iam.gserviceaccount.com`.

This service agent requires the `roles/containerthreatdetection.serviceAgent` IAM role.

  * `service-org-ORGANIZATION_ID@gcp-sa-csc-hpsa.iam.gserviceaccount.com` (Premium tier only)

This service agent requires the `roles/cloudsecuritycompliance.serviceAgent` IAM role.

  * `service-org-ORGANIZATION_ID@gcp-sa-dspm-hpsa.iam.gserviceaccount.com` (Premium tier only)

This service agent is used by Data Security Posture Management (DSPM) and requires the `roles/dspm.serviceAgent` IAM role.




During the [activation process](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#org-level-activation) of Security Command Center, you are prompted to grant one or more required IAM roles to each service agent. Granting the roles to each service agent is required for Security Command Center to function.

To view the permissions for each role, see the following:

  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent)
  * [Container Threat Detection Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerthreatdetection#containerthreatdetection.serviceAgent)



To grant the roles, you must have the `roles/resourcemanager.organizationAdmin` role.

If you don't have the `roles/resourcemanager.organizationAdmin` role, your organization administrator can grant the roles to the service agents for you with the following gcloud CLI command:
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member="SERVICE_AGENT_NAME" \
        --role="IAM_ROLE"
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID
  * `SERVICE_AGENT_NAME`: the name of the service agent that you are granting the role to. The name is one of the following service agent names: 
    * `service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com`
    * `service-org-ORGANIZATION_ID@gcp-sa-ktd-hpsa.iam.gserviceaccount.com`
  * `IAM_ROLE`: the following required role that corresponds to the specified service agent: 
    * `roles/securitycenter.serviceAgent`
    * `roles/containerthreatdetection.serviceAgent`



For more information about IAM roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Web Security Scanner roles

The following IAM roles are available for Web Security Scanner. You can grant these roles at the project level.

Role | Permissions  
---|---  
  
#### Web Security Scanner Admin 

(`roles/cloudsecurityscanner.admin`) Full access to all Web Security Scanner resources  |  `appengine.applications.get` `cloudsecurityscanner.*`

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

`compute.addresses.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Web Security Scanner Editor 

(`roles/cloudsecurityscanner.editor`) Full access to all Web Security Scanner resources  Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `cloudsecurityscanner.*`

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

`compute.addresses.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Web Security Scanner Viewer 

(`roles/cloudsecurityscanner.viewer`) Read access to all Web Security Scanner resources  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudsecurityscanner.crawledurls.list` `cloudsecurityscanner.results.*`

  * `cloudsecurityscanner.results.get`
  * `cloudsecurityscanner.results.list`

`cloudsecurityscanner.scanruns.get` `cloudsecurityscanner.scanruns.getSummary` `cloudsecurityscanner.scanruns.list` `cloudsecurityscanner.scans.get` `cloudsecurityscanner.scans.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Web Security Scanner Runner 

(`roles/cloudsecurityscanner.runner`) Read access to Scan and ScanRun, plus the ability to start scans  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudsecurityscanner.crawledurls.list` `cloudsecurityscanner.scanruns.get` `cloudsecurityscanner.scanruns.list` `cloudsecurityscanner.scanruns.stop` `cloudsecurityscanner.scans.get` `cloudsecurityscanner.scans.list` `cloudsecurityscanner.scans.run`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Web Security Scanner Service Agent 

(`roles/websecurityscanner.serviceAgent`) Gives the Cloud Web Security Scanner service account access to compute engine details and app engine details.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `appengine.applications.get` `cloudasset.assets.listResource` `compute.addresses.list` `compute.backendServices.get` `compute.forwardingRules.get` `compute.globalForwardingRules.get` `compute.sslCertificates.list` `compute.targetHttpProxies.get` `compute.targetHttpsProxies.get` `compute.urlMaps.get`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
