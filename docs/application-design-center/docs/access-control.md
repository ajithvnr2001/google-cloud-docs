---
url: https://docs.cloud.google.com/application-design-center/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:02:11.120099+00:00
---

# Access control with IAM  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Application Design Center roles and permissions. To control access to App Design Center, use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) to assign roles to users, groups, and service accounts.

## Predefined Application Design Center roles

To grant access to specific Google Cloud resources and prevent unauthorized access to other resources, assign App Design Center's [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project).

Use the following IAM roles to manage spaces and author templates:

  * Application Design Center Admin (`roles/designcenter.admin`)
  * Application Design Center User (`roles/designcenter.user`)
  * Application Design Center Viewer (`roles/designcenter.viewer`)



Use the following IAM roles to create application configurations and manage deployment lifecycles:

  * Application Admin (`roles/designcenter.applicationAdmin`)
  * Application Editor (`roles/designcenter.applicationEditor`)
  * Application Viewer (`roles/designcenter.applicationViewer`)



The Application Design Center Admin role includes all permissions in the other Application Design Center roles.

## Application Design Center role descriptions

The following table describes App Design Center roles and their typical responsibilities.

**Role** | **Description** | **Purpose**  
---|---|---  
**Application Design Center Admin** | Create and manage all App Design Center artifacts, and delegate application control to other users. | 

  * To manage the full lifecycle of an application.
  * For platform administrators, who have administrative permissions and full visibility of the end-to-end architecture.

  
**Application Design Center User** | Create and update application templates. | 

  * To scale the ability to create, update, or delete application templates to reduce the workload of platform administrators.
  * For platform engineers, who create and manage application templates.

  
**Application Design Center Viewer** | View spaces, catalogs, templates, applications, and their attributes. | 

  * To view App Design Center spaces, catalogs, templates, applications, and their dependencies.
  * For most personnel in the organization. Grant this role who only need to view spaces, catalogs, templates, and applications.

  
**Application Admin** | Create, manage, and deploy applications, and delegate application control to other application developers. | 

  * To manage application drafts and deployments, and attach service projects required to store individual resources.
  * For administrators and developers responsible for application creation.

  
**Application Editor** | Create, manage, and deploy applications. | 

  * To manage drafts and deployments and reduce the workload of application administrators.
  * For application operators who understand deployments.

  
**Application Viewer** | View applications. | 

  * To view templates, applications, and their dependencies.
  * For most personnel in the organization. Grant this role to users who only need to view templates and application.

  
  
## Application Design Center permissions

The following table lists App Design Center IAM roles and their permissions.

Application Design Center AdminApplication Design Center UserApplication Design Center ViewerApplication AdminApplication EditorApplication ViewerClear all

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
---|---  
  
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
  
## What's next

  * Manage access to your deployment resources by [granting roles to your service account](https://docs.cloud.google.com/application-design-center/docs/grant-roles-service-account).
  * Organize team spaces and access controls by [managing and assigning spaces](https://docs.cloud.google.com/application-design-center/docs/manage-spaces).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
