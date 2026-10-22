---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss/
title: Assured Open Source Software roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:56.188196+00:00
---

# Assured Open Source Software roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Assured Open Source Software roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Assured Open Source Software. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Assured Open Source Software roles

Role | Permissions  
---|---  
  
#### Assured OSS Admin 

(`roles/assuredoss.admin`) Access to use Assured OSS and manage configuration.  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`iam.serviceAccountKeys.create` `iam.serviceAccounts.create` `iam.serviceAccounts.get` `pubsub.messageTransforms.validate` `pubsub.schemas.get` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.validate` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.subscriptions.create` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.update` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Assured OSS Editor 

(`roles/assuredoss.editor`) Editor role for Assured OSS  |  `assuredoss.config.get` `assuredoss.locations.*`

  * `assuredoss.locations.get`
  * `assuredoss.locations.list`

`assuredoss.metadata.*`

  * `assuredoss.metadata.get`
  * `assuredoss.metadata.list`

`assuredoss.operations.get` `assuredoss.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Assured OSS Viewer 

(`roles/assuredoss.viewer`) Viewer role for Assured OSS  |  `assuredoss.config.get` `assuredoss.locations.*`

  * `assuredoss.locations.get`
  * `assuredoss.locations.list`

`assuredoss.metadata.*`

  * `assuredoss.metadata.get`
  * `assuredoss.metadata.list`

`assuredoss.operations.get` `assuredoss.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Assured OSS Project Admin Beta

(`roles/assuredoss.projectAdmin`) Access to use Assured OSS and manage configuration.  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`iam.serviceAccounts.create` `iam.serviceAccounts.get` `pubsub.messageTransforms.validate` `pubsub.schemas.get` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.validate` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Assured OSS Reader 

(`roles/assuredoss.reader`) Access to use Assured OSS and view Assured OSS configuration.  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`assuredoss.operations.get` `assuredoss.operations.list` `pubsub.messageTransforms.validate` `pubsub.schemas.get` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.validate` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Assured OSS User 

(`roles/assuredoss.user`) Access to use Assured OSS.  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `assuredoss.locations.*`

  * `assuredoss.locations.get`
  * `assuredoss.locations.list`

`assuredoss.metadata.*`

  * `assuredoss.metadata.get`
  * `assuredoss.metadata.list`

`assuredoss.operations.get` `assuredoss.operations.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Assured Open Source Software permissions

Permission | Included in roles  
---|---  
  
#### `assuredoss.config.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Assured OSS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.editor) (`roles/assuredoss.editor`)  [Assured OSS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.viewer) (`roles/assuredoss.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `assuredoss.customers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)   
  
#### `assuredoss.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Assured OSS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.editor) (`roles/assuredoss.editor`)  [Assured OSS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.viewer) (`roles/assuredoss.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Assured OSS User](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.user) (`roles/assuredoss.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `assuredoss.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Assured OSS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.editor) (`roles/assuredoss.editor`)  [Assured OSS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.viewer) (`roles/assuredoss.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Assured OSS User](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.user) (`roles/assuredoss.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `assuredoss.metadata.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Assured OSS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.editor) (`roles/assuredoss.editor`)  [Assured OSS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.viewer) (`roles/assuredoss.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Assured OSS User](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.user) (`roles/assuredoss.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `assuredoss.metadata.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Assured OSS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.editor) (`roles/assuredoss.editor`)  [Assured OSS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.viewer) (`roles/assuredoss.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Assured OSS User](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.user) (`roles/assuredoss.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `assuredoss.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)   
  
#### `assuredoss.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)   
  
#### `assuredoss.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Assured OSS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.editor) (`roles/assuredoss.editor`)  [Assured OSS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.viewer) (`roles/assuredoss.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Assured OSS User](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.user) (`roles/assuredoss.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
#### `assuredoss.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Assured OSS Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.editor) (`roles/assuredoss.editor`)  [Assured OSS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.viewer) (`roles/assuredoss.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Assured OSS User](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.user) (`roles/assuredoss.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
