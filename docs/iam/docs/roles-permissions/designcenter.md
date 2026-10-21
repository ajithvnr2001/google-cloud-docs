---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter/
title: Application Design Center roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:36:45.887614+00:00
---

# Application Design Center roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Application Design Center roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Application Design Center. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Application Design Center roles

Role | Permissions  
---|---  
  
#### Application Design Center Admin 

(`roles/designcenter.admin`) Full access to Application Design Center resources.  |  `apphub.applications.create` `apphub.applications.delete` `apphub.applications.get` `apphub.applications.list` `apphub.applications.update` `apphub.boundaries.attach` `apphub.boundaries.update` `apphub.locations.*`

  * `apphub.locations.get`
  * `apphub.locations.list`

`apphub.serviceProjectAttachments.list` `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

  * `auditmanager.controlReports.get`
  * `auditmanager.controlReports.list`

`auditmanager.controls.list` `auditmanager.findings.list` `auditmanager.locations.get` `auditmanager.locations.list` `auditmanager.operations.*`

  * `auditmanager.operations.get`
  * `auditmanager.operations.list`

`auditmanager.resourceEnrollmentStatuses.*`

  * `auditmanager.resourceEnrollmentStatuses.get`
  * `auditmanager.resourceEnrollmentStatuses.list`

`cloudbuild.builds.get` `cloudbuild.builds.list` `cloudsecuritycompliance.auditReports.get` `cloudsecuritycompliance.auditReports.list` `cloudsecuritycompliance.billingSettings.get` `cloudsecuritycompliance.cloudControlDeployments.get` `cloudsecuritycompliance.cloudControlDeployments.list` `cloudsecuritycompliance.cloudControlPredictions.get` `cloudsecuritycompliance.cloudControlPredictions.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.cmEnrollments.get` `cloudsecuritycompliance.controlComplianceSummaries.list` `cloudsecuritycompliance.controlReports.get` `cloudsecuritycompliance.controls.*`

  * `cloudsecuritycompliance.controls.get`
  * `cloudsecuritycompliance.controls.list`

`cloudsecuritycompliance.findingSummaries.list` `cloudsecuritycompliance.findings.list` `cloudsecuritycompliance.frameworkAudits.get` `cloudsecuritycompliance.frameworkAudits.list` `cloudsecuritycompliance.frameworkComplianceReports.*`

  * `cloudsecuritycompliance.frameworkComplianceReports.aggregate`
  * `cloudsecuritycompliance.frameworkComplianceReports.get`

`cloudsecuritycompliance.frameworkComplianceSummaries.list` `cloudsecuritycompliance.frameworkDeployments.get` `cloudsecuritycompliance.frameworkDeployments.list` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `cloudsecuritycompliance.locations.get` `cloudsecuritycompliance.locations.list` `cloudsecuritycompliance.operations.get` `cloudsecuritycompliance.operations.list` `cloudsecuritycompliance.resourceEnrollmentStatuses.*`

  * `cloudsecuritycompliance.resourceEnrollmentStatuses.get`
  * `cloudsecuritycompliance.resourceEnrollmentStatuses.list`

`config.automigrationconfig.get` `config.deploymentgrouprevisions.*`

  * `config.deploymentgrouprevisions.get`
  * `config.deploymentgrouprevisions.list`

`config.deploymentgroups.get` `config.deploymentgroups.list` `config.deploymentgroups.listEffectiveTags` `config.deploymentgroups.listTagBindings` `config.deployments.get` `config.deployments.getIamPolicy` `config.deployments.list` `config.deployments.listEffectiveTags` `config.deployments.listTagBindings` `config.locations.*`

  * `config.locations.get`
  * `config.locations.list`

`config.operations.get` `config.operations.list` `config.previews.export` `config.previews.get` `config.previews.list` `config.previews.listEffectiveTags` `config.previews.listTagBindings` `config.resources.*`

  * `config.resources.get`
  * `config.resources.list`

`config.revisions.get` `config.revisions.list` `config.terraformversions.*`

  * `config.terraformversions.get`
  * `config.terraformversions.list`

`container.clusters.list` `designcenter.*`

  * `designcenter.applicationTemplateRevisions.delete`
  * `designcenter.applicationTemplateRevisions.get`
  * `designcenter.applicationTemplateRevisions.list`
  * `designcenter.applicationTemplates.create`
  * `designcenter.applicationTemplates.delete`
  * `designcenter.applicationTemplates.get`
  * `designcenter.applicationTemplates.list`
  * `designcenter.applicationTemplates.update`
  * `designcenter.applications.create`
  * `designcenter.applications.delete`
  * `designcenter.applications.get`
  * `designcenter.applications.list`
  * `designcenter.applications.update`
  * `designcenter.catalogTemplateRevisions.create`
  * `designcenter.catalogTemplateRevisions.delete`
  * `designcenter.catalogTemplateRevisions.get`
  * `designcenter.catalogTemplateRevisions.list`
  * `designcenter.catalogTemplates.create`
  * `designcenter.catalogTemplates.delete`
  * `designcenter.catalogTemplates.get`
  * `designcenter.catalogTemplates.list`
  * `designcenter.catalogTemplates.update`
  * `designcenter.catalogs.create`
  * `designcenter.catalogs.delete`
  * `designcenter.catalogs.get`
  * `designcenter.catalogs.list`
  * `designcenter.catalogs.update`
  * `designcenter.components.create`
  * `designcenter.components.delete`
  * `designcenter.components.get`
  * `designcenter.components.list`
  * `designcenter.components.update`
  * `designcenter.connections.create`
  * `designcenter.connections.delete`
  * `designcenter.connections.get`
  * `designcenter.connections.list`
  * `designcenter.connections.update`
  * `designcenter.locations.get`
  * `designcenter.locations.list`
  * `designcenter.operations.cancel`
  * `designcenter.operations.delete`
  * `designcenter.operations.get`
  * `designcenter.operations.list`
  * `designcenter.sharedTemplateRevisions.get`
  * `designcenter.sharedTemplateRevisions.list`
  * `designcenter.sharedTemplates.get`
  * `designcenter.sharedTemplates.list`
  * `designcenter.shares.create`
  * `designcenter.shares.delete`
  * `designcenter.shares.get`
  * `designcenter.shares.list`
  * `designcenter.spaces.create`
  * `designcenter.spaces.delete`
  * `designcenter.spaces.get`
  * `designcenter.spaces.getIamPolicy`
  * `designcenter.spaces.list`
  * `designcenter.spaces.setIamPolicy`
  * `designcenter.spaces.update`

`developerconnect.connections.constructGitHubAppManifest` `developerconnect.connections.create` `developerconnect.connections.delete` `developerconnect.connections.fetchGitHubInstallations` `developerconnect.connections.fetchLinkableGitRepositories` `developerconnect.connections.generateGitHubStateToken` `developerconnect.connections.get` `developerconnect.connections.list` `developerconnect.connections.processGitHubAppCreationCallback` `developerconnect.connections.processGitHubOAuthCallback` `developerconnect.connections.update` `developerconnect.gitRepositoryLinks.create` `developerconnect.gitRepositoryLinks.delete` `developerconnect.gitRepositoryLinks.fetchGitRefs` `developerconnect.gitRepositoryLinks.get` `developerconnect.gitRepositoryLinks.gitProxyRead` `developerconnect.gitRepositoryLinks.gitProxyWrite` `developerconnect.gitRepositoryLinks.list` `developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.*`

  * `developerconnect.operations.cancel`
  * `developerconnect.operations.delete`
  * `developerconnect.operations.get`
  * `developerconnect.operations.list`

`monitoring.timeSeries.create` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.create` `storage.managedFolders.delete` `storage.managedFolders.get` `storage.managedFolders.list` `storage.managedFolders.update` `storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.create` `storage.objects.createContext` `storage.objects.delete` `storage.objects.deleteContext` `storage.objects.get` `storage.objects.list` `storage.objects.move` `storage.objects.restore` `storage.objects.update` `storage.objects.updateContext`  
  
#### Designcenter Editor 

(`roles/designcenter.editor`) Editor role for designcenter  |  `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

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

`container.clusters.list` `designcenter.applicationTemplateRevisions.*`

  * `designcenter.applicationTemplateRevisions.delete`
  * `designcenter.applicationTemplateRevisions.get`
  * `designcenter.applicationTemplateRevisions.list`

`designcenter.applicationTemplates.*`

  * `designcenter.applicationTemplates.create`
  * `designcenter.applicationTemplates.delete`
  * `designcenter.applicationTemplates.get`
  * `designcenter.applicationTemplates.list`
  * `designcenter.applicationTemplates.update`

`designcenter.applications.*`

  * `designcenter.applications.create`
  * `designcenter.applications.delete`
  * `designcenter.applications.get`
  * `designcenter.applications.list`
  * `designcenter.applications.update`

`designcenter.catalogTemplateRevisions.*`

  * `designcenter.catalogTemplateRevisions.create`
  * `designcenter.catalogTemplateRevisions.delete`
  * `designcenter.catalogTemplateRevisions.get`
  * `designcenter.catalogTemplateRevisions.list`

`designcenter.catalogTemplates.*`

  * `designcenter.catalogTemplates.create`
  * `designcenter.catalogTemplates.delete`
  * `designcenter.catalogTemplates.get`
  * `designcenter.catalogTemplates.list`
  * `designcenter.catalogTemplates.update`

`designcenter.catalogs.*`

  * `designcenter.catalogs.create`
  * `designcenter.catalogs.delete`
  * `designcenter.catalogs.get`
  * `designcenter.catalogs.list`
  * `designcenter.catalogs.update`

`designcenter.components.*`

  * `designcenter.components.create`
  * `designcenter.components.delete`
  * `designcenter.components.get`
  * `designcenter.components.list`
  * `designcenter.components.update`

`designcenter.connections.*`

  * `designcenter.connections.create`
  * `designcenter.connections.delete`
  * `designcenter.connections.get`
  * `designcenter.connections.list`
  * `designcenter.connections.update`

`designcenter.locations.*`

  * `designcenter.locations.get`
  * `designcenter.locations.list`

`designcenter.operations.*`

  * `designcenter.operations.cancel`
  * `designcenter.operations.delete`
  * `designcenter.operations.get`
  * `designcenter.operations.list`

`designcenter.sharedTemplateRevisions.*`

  * `designcenter.sharedTemplateRevisions.get`
  * `designcenter.sharedTemplateRevisions.list`

`designcenter.sharedTemplates.*`

  * `designcenter.sharedTemplates.get`
  * `designcenter.sharedTemplates.list`

`designcenter.shares.*`

  * `designcenter.shares.create`
  * `designcenter.shares.delete`
  * `designcenter.shares.get`
  * `designcenter.shares.list`

`designcenter.spaces.create` `designcenter.spaces.delete` `designcenter.spaces.get` `designcenter.spaces.getIamPolicy` `designcenter.spaces.list` `designcenter.spaces.update` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.get` `storage.folders.list` `storage.managedFolders.get` `storage.managedFolders.list` `storage.objects.get` `storage.objects.list`  
  
#### Application Design Center Viewer 

(`roles/designcenter.viewer`) Readonly access to Application Design Center resources.  |  `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

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

`container.clusters.list` `designcenter.applicationTemplateRevisions.get` `designcenter.applicationTemplateRevisions.list` `designcenter.applicationTemplates.get` `designcenter.applicationTemplates.list` `designcenter.applications.get` `designcenter.applications.list` `designcenter.catalogTemplateRevisions.get` `designcenter.catalogTemplateRevisions.list` `designcenter.catalogTemplates.get` `designcenter.catalogTemplates.list` `designcenter.catalogs.get` `designcenter.catalogs.list` `designcenter.components.get` `designcenter.components.list` `designcenter.connections.get` `designcenter.connections.list` `designcenter.locations.*`

  * `designcenter.locations.get`
  * `designcenter.locations.list`

`designcenter.operations.get` `designcenter.operations.list` `designcenter.sharedTemplateRevisions.*`

  * `designcenter.sharedTemplateRevisions.get`
  * `designcenter.sharedTemplateRevisions.list`

`designcenter.sharedTemplates.*`

  * `designcenter.sharedTemplates.get`
  * `designcenter.sharedTemplates.list`

`designcenter.shares.get` `designcenter.shares.list` `designcenter.spaces.get` `designcenter.spaces.getIamPolicy` `designcenter.spaces.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.get` `storage.folders.list` `storage.managedFolders.get` `storage.managedFolders.list` `storage.objects.get` `storage.objects.list`  
  
#### Application Admin 

(`roles/designcenter.applicationAdmin`) Admin access to Application.  |  `apphub.applications.create` `apphub.applications.delete` `apphub.applications.get` `apphub.applications.list` `apphub.applications.update` `apphub.locations.*`

  * `apphub.locations.get`
  * `apphub.locations.list`

`apphub.serviceProjectAttachments.list` `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

  * `auditmanager.controlReports.get`
  * `auditmanager.controlReports.list`

`auditmanager.controls.list` `auditmanager.findings.list` `auditmanager.locations.get` `auditmanager.locations.list` `auditmanager.operations.*`

  * `auditmanager.operations.get`
  * `auditmanager.operations.list`

`auditmanager.resourceEnrollmentStatuses.*`

  * `auditmanager.resourceEnrollmentStatuses.get`
  * `auditmanager.resourceEnrollmentStatuses.list`

`cloudbuild.builds.get` `cloudbuild.builds.list` `cloudsecuritycompliance.auditReports.get` `cloudsecuritycompliance.auditReports.list` `cloudsecuritycompliance.billingSettings.get` `cloudsecuritycompliance.cloudControlDeployments.get` `cloudsecuritycompliance.cloudControlDeployments.list` `cloudsecuritycompliance.cloudControlPredictions.get` `cloudsecuritycompliance.cloudControlPredictions.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.cmEnrollments.get` `cloudsecuritycompliance.controlComplianceSummaries.list` `cloudsecuritycompliance.controlReports.get` `cloudsecuritycompliance.controls.*`

  * `cloudsecuritycompliance.controls.get`
  * `cloudsecuritycompliance.controls.list`

`cloudsecuritycompliance.findingSummaries.list` `cloudsecuritycompliance.findings.list` `cloudsecuritycompliance.frameworkAudits.get` `cloudsecuritycompliance.frameworkAudits.list` `cloudsecuritycompliance.frameworkComplianceReports.*`

  * `cloudsecuritycompliance.frameworkComplianceReports.aggregate`
  * `cloudsecuritycompliance.frameworkComplianceReports.get`

`cloudsecuritycompliance.frameworkComplianceSummaries.list` `cloudsecuritycompliance.frameworkDeployments.get` `cloudsecuritycompliance.frameworkDeployments.list` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `cloudsecuritycompliance.locations.get` `cloudsecuritycompliance.locations.list` `cloudsecuritycompliance.operations.get` `cloudsecuritycompliance.operations.list` `cloudsecuritycompliance.resourceEnrollmentStatuses.*`

  * `cloudsecuritycompliance.resourceEnrollmentStatuses.get`
  * `cloudsecuritycompliance.resourceEnrollmentStatuses.list`

`config.automigrationconfig.get` `config.deploymentgrouprevisions.*`

  * `config.deploymentgrouprevisions.get`
  * `config.deploymentgrouprevisions.list`

`config.deploymentgroups.get` `config.deploymentgroups.list` `config.deploymentgroups.listEffectiveTags` `config.deploymentgroups.listTagBindings` `config.deployments.get` `config.deployments.getIamPolicy` `config.deployments.list` `config.deployments.listEffectiveTags` `config.deployments.listTagBindings` `config.locations.*`

  * `config.locations.get`
  * `config.locations.list`

`config.operations.get` `config.operations.list` `config.previews.export` `config.previews.get` `config.previews.list` `config.previews.listEffectiveTags` `config.previews.listTagBindings` `config.resources.*`

  * `config.resources.get`
  * `config.resources.list`

`config.revisions.get` `config.revisions.list` `config.terraformversions.*`

  * `config.terraformversions.get`
  * `config.terraformversions.list`

`container.clusters.list` `designcenter.applicationTemplateRevisions.get` `designcenter.applicationTemplateRevisions.list` `designcenter.applicationTemplates.get` `designcenter.applicationTemplates.list` `designcenter.applications.*`

  * `designcenter.applications.create`
  * `designcenter.applications.delete`
  * `designcenter.applications.get`
  * `designcenter.applications.list`
  * `designcenter.applications.update`

`designcenter.sharedTemplateRevisions.*`

  * `designcenter.sharedTemplateRevisions.get`
  * `designcenter.sharedTemplateRevisions.list`

`designcenter.sharedTemplates.*`

  * `designcenter.sharedTemplates.get`
  * `designcenter.sharedTemplates.list`

`designcenter.shares.get` `designcenter.shares.list` `designcenter.spaces.get` `designcenter.spaces.list` `developerconnect.connections.constructGitHubAppManifest` `developerconnect.connections.create` `developerconnect.connections.delete` `developerconnect.connections.fetchGitHubInstallations` `developerconnect.connections.fetchLinkableGitRepositories` `developerconnect.connections.generateGitHubStateToken` `developerconnect.connections.get` `developerconnect.connections.list` `developerconnect.connections.processGitHubAppCreationCallback` `developerconnect.connections.processGitHubOAuthCallback` `developerconnect.connections.update` `developerconnect.gitRepositoryLinks.create` `developerconnect.gitRepositoryLinks.delete` `developerconnect.gitRepositoryLinks.fetchGitRefs` `developerconnect.gitRepositoryLinks.get` `developerconnect.gitRepositoryLinks.gitProxyRead` `developerconnect.gitRepositoryLinks.gitProxyWrite` `developerconnect.gitRepositoryLinks.list` `developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.*`

  * `developerconnect.operations.cancel`
  * `developerconnect.operations.delete`
  * `developerconnect.operations.get`
  * `developerconnect.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Editor 

(`roles/designcenter.applicationEditor`) Read and Write access to Application.  |  `apphub.applications.create` `apphub.applications.delete` `apphub.applications.get` `apphub.applications.list` `apphub.applications.update` `apphub.locations.*`

  * `apphub.locations.get`
  * `apphub.locations.list`

`apphub.serviceProjectAttachments.list` `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

  * `auditmanager.controlReports.get`
  * `auditmanager.controlReports.list`

`auditmanager.controls.list` `auditmanager.findings.list` `auditmanager.locations.get` `auditmanager.locations.list` `auditmanager.operations.*`

  * `auditmanager.operations.get`
  * `auditmanager.operations.list`

`auditmanager.resourceEnrollmentStatuses.*`

  * `auditmanager.resourceEnrollmentStatuses.get`
  * `auditmanager.resourceEnrollmentStatuses.list`

`cloudbuild.builds.get` `cloudbuild.builds.list` `cloudsecuritycompliance.auditReports.get` `cloudsecuritycompliance.auditReports.list` `cloudsecuritycompliance.billingSettings.get` `cloudsecuritycompliance.cloudControlDeployments.get` `cloudsecuritycompliance.cloudControlDeployments.list` `cloudsecuritycompliance.cloudControlPredictions.get` `cloudsecuritycompliance.cloudControlPredictions.list` `cloudsecuritycompliance.cloudControls.get` `cloudsecuritycompliance.cloudControls.list` `cloudsecuritycompliance.cmEnrollments.get` `cloudsecuritycompliance.controlComplianceSummaries.list` `cloudsecuritycompliance.controlReports.get` `cloudsecuritycompliance.controls.*`

  * `cloudsecuritycompliance.controls.get`
  * `cloudsecuritycompliance.controls.list`

`cloudsecuritycompliance.findingSummaries.list` `cloudsecuritycompliance.findings.list` `cloudsecuritycompliance.frameworkAudits.get` `cloudsecuritycompliance.frameworkAudits.list` `cloudsecuritycompliance.frameworkComplianceReports.*`

  * `cloudsecuritycompliance.frameworkComplianceReports.aggregate`
  * `cloudsecuritycompliance.frameworkComplianceReports.get`

`cloudsecuritycompliance.frameworkComplianceSummaries.list` `cloudsecuritycompliance.frameworkDeployments.get` `cloudsecuritycompliance.frameworkDeployments.list` `cloudsecuritycompliance.frameworks.get` `cloudsecuritycompliance.frameworks.list` `cloudsecuritycompliance.locations.get` `cloudsecuritycompliance.locations.list` `cloudsecuritycompliance.operations.get` `cloudsecuritycompliance.operations.list` `cloudsecuritycompliance.resourceEnrollmentStatuses.*`

  * `cloudsecuritycompliance.resourceEnrollmentStatuses.get`
  * `cloudsecuritycompliance.resourceEnrollmentStatuses.list`

`config.automigrationconfig.get` `config.deploymentgrouprevisions.*`

  * `config.deploymentgrouprevisions.get`
  * `config.deploymentgrouprevisions.list`

`config.deploymentgroups.get` `config.deploymentgroups.list` `config.deploymentgroups.listEffectiveTags` `config.deploymentgroups.listTagBindings` `config.deployments.get` `config.deployments.getIamPolicy` `config.deployments.list` `config.deployments.listEffectiveTags` `config.deployments.listTagBindings` `config.locations.*`

  * `config.locations.get`
  * `config.locations.list`

`config.operations.get` `config.operations.list` `config.previews.export` `config.previews.get` `config.previews.list` `config.previews.listEffectiveTags` `config.previews.listTagBindings` `config.resources.*`

  * `config.resources.get`
  * `config.resources.list`

`config.revisions.get` `config.revisions.list` `config.terraformversions.*`

  * `config.terraformversions.get`
  * `config.terraformversions.list`

`container.clusters.list` `designcenter.applicationTemplateRevisions.get` `designcenter.applicationTemplateRevisions.list` `designcenter.applicationTemplates.get` `designcenter.applicationTemplates.list` `designcenter.applications.*`

  * `designcenter.applications.create`
  * `designcenter.applications.delete`
  * `designcenter.applications.get`
  * `designcenter.applications.list`
  * `designcenter.applications.update`

`designcenter.sharedTemplateRevisions.*`

  * `designcenter.sharedTemplateRevisions.get`
  * `designcenter.sharedTemplateRevisions.list`

`designcenter.sharedTemplates.*`

  * `designcenter.sharedTemplates.get`
  * `designcenter.sharedTemplates.list`

`designcenter.shares.get` `designcenter.shares.list` `designcenter.spaces.get` `designcenter.spaces.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Viewer 

(`roles/designcenter.applicationViewer`) Readonly access to Application.  |  `apphub.applications.get` `apphub.applications.list` `apphub.locations.*`

  * `apphub.locations.get`
  * `apphub.locations.list`

`auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

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

`config.automigrationconfig.get` `config.deploymentgrouprevisions.*`

  * `config.deploymentgrouprevisions.get`
  * `config.deploymentgrouprevisions.list`

`config.deploymentgroups.get` `config.deploymentgroups.list` `config.deploymentgroups.listEffectiveTags` `config.deploymentgroups.listTagBindings` `config.deployments.get` `config.deployments.getIamPolicy` `config.deployments.list` `config.deployments.listEffectiveTags` `config.deployments.listTagBindings` `config.locations.*`

  * `config.locations.get`
  * `config.locations.list`

`config.operations.get` `config.operations.list` `config.previews.get` `config.previews.list` `config.previews.listEffectiveTags` `config.previews.listTagBindings` `config.resources.*`

  * `config.resources.get`
  * `config.resources.list`

`config.revisions.get` `config.revisions.list` `config.terraformversions.*`

  * `config.terraformversions.get`
  * `config.terraformversions.list`

`container.clusters.list` `designcenter.applicationTemplateRevisions.get` `designcenter.applicationTemplateRevisions.list` `designcenter.applicationTemplates.get` `designcenter.applicationTemplates.list` `designcenter.applications.get` `designcenter.applications.list` `designcenter.sharedTemplateRevisions.*`

  * `designcenter.sharedTemplateRevisions.get`
  * `designcenter.sharedTemplateRevisions.list`

`designcenter.sharedTemplates.*`

  * `designcenter.sharedTemplates.get`
  * `designcenter.sharedTemplates.list`

`designcenter.shares.get` `designcenter.shares.list` `designcenter.spaces.get` `designcenter.spaces.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Design Center User 

(`roles/designcenter.user`) Readonly access to Application Design Center resources.  |  `apphub.serviceProjectAttachments.list` `auditmanager.auditReports.get` `auditmanager.auditReports.list` `auditmanager.auditSchedules.get` `auditmanager.auditSchedules.list` `auditmanager.billingSettings.get` `auditmanager.controlReports.*`

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

`container.clusters.list` `designcenter.applicationTemplateRevisions.*`

  * `designcenter.applicationTemplateRevisions.delete`
  * `designcenter.applicationTemplateRevisions.get`
  * `designcenter.applicationTemplateRevisions.list`

`designcenter.applicationTemplates.*`

  * `designcenter.applicationTemplates.create`
  * `designcenter.applicationTemplates.delete`
  * `designcenter.applicationTemplates.get`
  * `designcenter.applicationTemplates.list`
  * `designcenter.applicationTemplates.update`

`designcenter.applications.get` `designcenter.applications.list` `designcenter.catalogTemplateRevisions.get` `designcenter.catalogTemplateRevisions.list` `designcenter.catalogTemplates.get` `designcenter.catalogTemplates.list` `designcenter.catalogs.get` `designcenter.catalogs.list` `designcenter.components.*`

  * `designcenter.components.create`
  * `designcenter.components.delete`
  * `designcenter.components.get`
  * `designcenter.components.list`
  * `designcenter.components.update`

`designcenter.connections.*`

  * `designcenter.connections.create`
  * `designcenter.connections.delete`
  * `designcenter.connections.get`
  * `designcenter.connections.list`
  * `designcenter.connections.update`

`designcenter.locations.*`

  * `designcenter.locations.get`
  * `designcenter.locations.list`

`designcenter.operations.get` `designcenter.operations.list` `designcenter.sharedTemplateRevisions.*`

  * `designcenter.sharedTemplateRevisions.get`
  * `designcenter.sharedTemplateRevisions.list`

`designcenter.sharedTemplates.*`

  * `designcenter.sharedTemplates.get`
  * `designcenter.sharedTemplates.list`

`designcenter.shares.get` `designcenter.shares.list` `designcenter.spaces.get` `designcenter.spaces.getIamPolicy` `designcenter.spaces.list` `monitoring.timeSeries.create` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.create` `storage.managedFolders.delete` `storage.managedFolders.get` `storage.managedFolders.list` `storage.managedFolders.update` `storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.create` `storage.objects.createContext` `storage.objects.delete` `storage.objects.deleteContext` `storage.objects.get` `storage.objects.list` `storage.objects.move` `storage.objects.restore` `storage.objects.update` `storage.objects.updateContext`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### DesignCenter Service Agent 

(`roles/designcenter.serviceAgent`) Gives the DesignCenter API Service Account access to necessary GCP resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `apphub.applications.create` `apphub.applications.delete` `apphub.applications.get` `apphub.applications.list` `apphub.applications.update` `apphub.boundaries.attach` `apphub.boundaries.update` `apphub.discoveredServices.*`

  * `apphub.discoveredServices.get`
  * `apphub.discoveredServices.list`
  * `apphub.discoveredServices.register`

`apphub.discoveredWorkloads.*`

  * `apphub.discoveredWorkloads.get`
  * `apphub.discoveredWorkloads.list`
  * `apphub.discoveredWorkloads.register`

`apphub.operations.get` `apphub.operations.list` `apphub.serviceProjectAttachments.get` `apphub.serviceProjectAttachments.list` `apphub.serviceProjectAttachments.lookup` `apphub.services.create` `apphub.workloads.create` `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `config.deploymentgrouprevisions.*`

  * `config.deploymentgrouprevisions.get`
  * `config.deploymentgrouprevisions.list`

`config.deploymentgroups.create` `config.deploymentgroups.delete` `config.deploymentgroups.deprovision` `config.deploymentgroups.get` `config.deploymentgroups.list` `config.deploymentgroups.provision` `config.deploymentgroups.update` `config.deployments.create` `config.deployments.delete` `config.deployments.get` `config.deployments.getState` `config.deployments.list` `config.deployments.lock` `config.deployments.unlock` `config.deployments.update` `config.locations.*`

  * `config.locations.get`
  * `config.locations.list`

`config.operations.*`

  * `config.operations.cancel`
  * `config.operations.delete`
  * `config.operations.get`
  * `config.operations.list`

`config.previews.create` `config.previews.delete` `config.previews.export` `config.previews.get` `config.previews.list` `config.resources.*`

  * `config.resources.get`
  * `config.resources.list`

`config.revisions.*`

  * `config.revisions.get`
  * `config.revisions.getState`
  * `config.revisions.list`

`config.terraformversions.*`

  * `config.terraformversions.get`
  * `config.terraformversions.list`

`developerconnect.gitRepositoryLinks.get` `developerconnect.gitRepositoryLinks.gitProxyRead` `developerconnect.gitRepositoryLinks.gitProxyWrite` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.buckets.update` `storage.managedFolders.create` `storage.managedFolders.delete` `storage.managedFolders.get` `storage.managedFolders.getIamPolicy` `storage.managedFolders.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Application Design Center permissions

Permission | Included in roles  
---|---  
  
#### `designcenter.applicationTemplateRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.applicationTemplateRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 

  
  
#### `designcenter.applicationTemplateRevisions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.applicationTemplates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.applicationTemplates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.applicationTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 

  
  
#### `designcenter.applicationTemplates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.applicationTemplates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 

  
  
#### `designcenter.applications.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)   
  
#### `designcenter.applications.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)   
  
#### `designcenter.applications.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.applications.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.applications.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)   
  
#### `designcenter.catalogTemplateRevisions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.catalogTemplateRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.catalogTemplateRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.catalogTemplateRevisions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.catalogTemplates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.catalogTemplates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.catalogTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.catalogTemplates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.catalogTemplates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.catalogs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.catalogs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.catalogs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.catalogs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.catalogs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.components.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.components.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.components.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.components.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.components.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.connections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.connections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.connections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.connections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.connections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)   
  
#### `designcenter.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 

  
  
#### `designcenter.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [SaaS Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent) (`roles/saasservicemgmt.serviceAgent`) 

  
  
#### `designcenter.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.sharedTemplateRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.sharedTemplateRevisions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.sharedTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.sharedTemplates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.shares.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.shares.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.shares.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.shares.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.spaces.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.spaces.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
#### `designcenter.spaces.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.spaces.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.spaces.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)  [Application Design Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.viewer) (`roles/designcenter.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Gemini Cloud Assist Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) (`roles/geminicloudassist.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.appManagementViewer) (`roles/apphub.appManagementViewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Application Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationViewer) (`roles/designcenter.applicationViewer`)  [Application Design Center User](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `designcenter.spaces.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `designcenter.spaces.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Designcenter Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.editor) (`roles/designcenter.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
