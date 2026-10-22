---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy/
title: Cloud Deploy roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:03.222007+00:00
---

# Cloud Deploy roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Deploy roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Deploy. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Deploy roles

Role | Permissions  
---|---  
  
#### Cloud Deploy Admin 

(`roles/clouddeploy.admin`) Full control of Cloud Deploy resources.  |  `clouddeploy.*`

  * `clouddeploy.automationRuns.cancel`
  * `clouddeploy.automationRuns.get`
  * `clouddeploy.automationRuns.list`
  * `clouddeploy.automations.create`
  * `clouddeploy.automations.delete`
  * `clouddeploy.automations.get`
  * `clouddeploy.automations.list`
  * `clouddeploy.automations.update`
  * `clouddeploy.config.get`
  * `clouddeploy.customTargetTypes.create`
  * `clouddeploy.customTargetTypes.delete`
  * `clouddeploy.customTargetTypes.get`
  * `clouddeploy.customTargetTypes.getIamPolicy`
  * `clouddeploy.customTargetTypes.list`
  * `clouddeploy.customTargetTypes.setIamPolicy`
  * `clouddeploy.customTargetTypes.update`
  * `clouddeploy.deliveryPipelines.create`
  * `clouddeploy.deliveryPipelines.createTagBinding`
  * `clouddeploy.deliveryPipelines.delete`
  * `clouddeploy.deliveryPipelines.deleteTagBinding`
  * `clouddeploy.deliveryPipelines.get`
  * `clouddeploy.deliveryPipelines.getIamPolicy`
  * `clouddeploy.deliveryPipelines.list`
  * `clouddeploy.deliveryPipelines.listEffectiveTags`
  * `clouddeploy.deliveryPipelines.listTagBindings`
  * `clouddeploy.deliveryPipelines.setIamPolicy`
  * `clouddeploy.deliveryPipelines.update`
  * `clouddeploy.deployPolicies.create`
  * `clouddeploy.deployPolicies.delete`
  * `clouddeploy.deployPolicies.get`
  * `clouddeploy.deployPolicies.getIamPolicy`
  * `clouddeploy.deployPolicies.list`
  * `clouddeploy.deployPolicies.override`
  * `clouddeploy.deployPolicies.setIamPolicy`
  * `clouddeploy.deployPolicies.update`
  * `clouddeploy.jobRuns.get`
  * `clouddeploy.jobRuns.list`
  * `clouddeploy.jobRuns.terminate`
  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`
  * `clouddeploy.operations.cancel`
  * `clouddeploy.operations.delete`
  * `clouddeploy.operations.get`
  * `clouddeploy.operations.list`
  * `clouddeploy.releases.abandon`
  * `clouddeploy.releases.create`
  * `clouddeploy.releases.get`
  * `clouddeploy.releases.list`
  * `clouddeploy.rollouts.advance`
  * `clouddeploy.rollouts.approve`
  * `clouddeploy.rollouts.cancel`
  * `clouddeploy.rollouts.create`
  * `clouddeploy.rollouts.get`
  * `clouddeploy.rollouts.ignoreJob`
  * `clouddeploy.rollouts.list`
  * `clouddeploy.rollouts.retryJob`
  * `clouddeploy.rollouts.rollback`
  * `clouddeploy.targets.create`
  * `clouddeploy.targets.createTagBinding`
  * `clouddeploy.targets.delete`
  * `clouddeploy.targets.deleteTagBinding`
  * `clouddeploy.targets.get`
  * `clouddeploy.targets.getIamPolicy`
  * `clouddeploy.targets.list`
  * `clouddeploy.targets.listEffectiveTags`
  * `clouddeploy.targets.listTagBindings`
  * `clouddeploy.targets.setIamPolicy`
  * `clouddeploy.targets.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Editor 

(`roles/clouddeploy.editor`) Editor role for Cloud Deploy  |  `clouddeploy.automationRuns.*`

  * `clouddeploy.automationRuns.cancel`
  * `clouddeploy.automationRuns.get`
  * `clouddeploy.automationRuns.list`

`clouddeploy.automations.*`

  * `clouddeploy.automations.create`
  * `clouddeploy.automations.delete`
  * `clouddeploy.automations.get`
  * `clouddeploy.automations.list`
  * `clouddeploy.automations.update`

`clouddeploy.config.get` `clouddeploy.customTargetTypes.create` `clouddeploy.customTargetTypes.delete` `clouddeploy.customTargetTypes.get` `clouddeploy.customTargetTypes.getIamPolicy` `clouddeploy.customTargetTypes.list` `clouddeploy.customTargetTypes.update` `clouddeploy.deliveryPipelines.create` `clouddeploy.deliveryPipelines.delete` `clouddeploy.deliveryPipelines.get` `clouddeploy.deliveryPipelines.getIamPolicy` `clouddeploy.deliveryPipelines.list` `clouddeploy.deliveryPipelines.listEffectiveTags` `clouddeploy.deliveryPipelines.listTagBindings` `clouddeploy.deliveryPipelines.update` `clouddeploy.deployPolicies.create` `clouddeploy.deployPolicies.delete` `clouddeploy.deployPolicies.get` `clouddeploy.deployPolicies.getIamPolicy` `clouddeploy.deployPolicies.list` `clouddeploy.deployPolicies.override` `clouddeploy.deployPolicies.update` `clouddeploy.jobRuns.*`

  * `clouddeploy.jobRuns.get`
  * `clouddeploy.jobRuns.list`
  * `clouddeploy.jobRuns.terminate`

`clouddeploy.locations.*`

  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`

`clouddeploy.operations.*`

  * `clouddeploy.operations.cancel`
  * `clouddeploy.operations.delete`
  * `clouddeploy.operations.get`
  * `clouddeploy.operations.list`

`clouddeploy.releases.*`

  * `clouddeploy.releases.abandon`
  * `clouddeploy.releases.create`
  * `clouddeploy.releases.get`
  * `clouddeploy.releases.list`

`clouddeploy.rollouts.*`

  * `clouddeploy.rollouts.advance`
  * `clouddeploy.rollouts.approve`
  * `clouddeploy.rollouts.cancel`
  * `clouddeploy.rollouts.create`
  * `clouddeploy.rollouts.get`
  * `clouddeploy.rollouts.ignoreJob`
  * `clouddeploy.rollouts.list`
  * `clouddeploy.rollouts.retryJob`
  * `clouddeploy.rollouts.rollback`

`clouddeploy.targets.create` `clouddeploy.targets.delete` `clouddeploy.targets.get` `clouddeploy.targets.getIamPolicy` `clouddeploy.targets.list` `clouddeploy.targets.listEffectiveTags` `clouddeploy.targets.listTagBindings` `clouddeploy.targets.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Viewer 

(`roles/clouddeploy.viewer`) Can view Cloud Deploy resources.  |  `clouddeploy.automationRuns.get` `clouddeploy.automationRuns.list` `clouddeploy.automations.get` `clouddeploy.automations.list` `clouddeploy.config.get` `clouddeploy.customTargetTypes.get` `clouddeploy.customTargetTypes.getIamPolicy` `clouddeploy.customTargetTypes.list` `clouddeploy.deliveryPipelines.get` `clouddeploy.deliveryPipelines.getIamPolicy` `clouddeploy.deliveryPipelines.list` `clouddeploy.deliveryPipelines.listEffectiveTags` `clouddeploy.deliveryPipelines.listTagBindings` `clouddeploy.deployPolicies.get` `clouddeploy.deployPolicies.getIamPolicy` `clouddeploy.deployPolicies.list` `clouddeploy.jobRuns.get` `clouddeploy.jobRuns.list` `clouddeploy.locations.*`

  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`

`clouddeploy.operations.get` `clouddeploy.operations.list` `clouddeploy.releases.get` `clouddeploy.releases.list` `clouddeploy.rollouts.get` `clouddeploy.rollouts.list` `clouddeploy.targets.get` `clouddeploy.targets.getIamPolicy` `clouddeploy.targets.list` `clouddeploy.targets.listEffectiveTags` `clouddeploy.targets.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Approver 

(`roles/clouddeploy.approver`) Permission to approve or reject rollouts.  |  `clouddeploy.config.get` `clouddeploy.jobRuns.get` `clouddeploy.jobRuns.list` `clouddeploy.locations.*`

  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`

`clouddeploy.operations.*`

  * `clouddeploy.operations.cancel`
  * `clouddeploy.operations.delete`
  * `clouddeploy.operations.get`
  * `clouddeploy.operations.list`

`clouddeploy.rollouts.approve` `clouddeploy.rollouts.get` `clouddeploy.rollouts.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Custom Target Type Admin 

(`roles/clouddeploy.customTargetTypeAdmin`) Permission to manage CustomTargetType resources  |  `clouddeploy.config.get` `clouddeploy.customTargetTypes.*`

  * `clouddeploy.customTargetTypes.create`
  * `clouddeploy.customTargetTypes.delete`
  * `clouddeploy.customTargetTypes.get`
  * `clouddeploy.customTargetTypes.getIamPolicy`
  * `clouddeploy.customTargetTypes.list`
  * `clouddeploy.customTargetTypes.setIamPolicy`
  * `clouddeploy.customTargetTypes.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Developer 

(`roles/clouddeploy.developer`) Permission to manage deployment configuration without permission to access operational resources, such as targets.  |  `clouddeploy.automationRuns.get` `clouddeploy.automationRuns.list` `clouddeploy.automations.get` `clouddeploy.automations.list` `clouddeploy.config.get` `clouddeploy.deliveryPipelines.create` `clouddeploy.deliveryPipelines.createTagBinding` `clouddeploy.deliveryPipelines.delete` `clouddeploy.deliveryPipelines.deleteTagBinding` `clouddeploy.deliveryPipelines.get` `clouddeploy.deliveryPipelines.getIamPolicy` `clouddeploy.deliveryPipelines.list` `clouddeploy.deliveryPipelines.listEffectiveTags` `clouddeploy.deliveryPipelines.listTagBindings` `clouddeploy.deliveryPipelines.update` `clouddeploy.deployPolicies.get` `clouddeploy.deployPolicies.list` `clouddeploy.jobRuns.get` `clouddeploy.jobRuns.list` `clouddeploy.locations.*`

  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`

`clouddeploy.operations.*`

  * `clouddeploy.operations.cancel`
  * `clouddeploy.operations.delete`
  * `clouddeploy.operations.get`
  * `clouddeploy.operations.list`

`clouddeploy.releases.*`

  * `clouddeploy.releases.abandon`
  * `clouddeploy.releases.create`
  * `clouddeploy.releases.get`
  * `clouddeploy.releases.list`

`clouddeploy.rollouts.get` `clouddeploy.rollouts.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Runner 

(`roles/clouddeploy.jobRunner`) Permission to execute Cloud Deploy work without permission to deliver to a target.  |  `clouddeploy.config.get` `logging.logEntries.create` `storage.objects.create` `storage.objects.get` `storage.objects.list`  
  
#### Cloud Deploy Operator 

(`roles/clouddeploy.operator`) Permission to manage deployment configuration.  |  `clouddeploy.automationRuns.*`

  * `clouddeploy.automationRuns.cancel`
  * `clouddeploy.automationRuns.get`
  * `clouddeploy.automationRuns.list`

`clouddeploy.automations.*`

  * `clouddeploy.automations.create`
  * `clouddeploy.automations.delete`
  * `clouddeploy.automations.get`
  * `clouddeploy.automations.list`
  * `clouddeploy.automations.update`

`clouddeploy.config.get` `clouddeploy.customTargetTypes.get` `clouddeploy.customTargetTypes.getIamPolicy` `clouddeploy.customTargetTypes.list` `clouddeploy.deliveryPipelines.create` `clouddeploy.deliveryPipelines.createTagBinding` `clouddeploy.deliveryPipelines.delete` `clouddeploy.deliveryPipelines.deleteTagBinding` `clouddeploy.deliveryPipelines.get` `clouddeploy.deliveryPipelines.getIamPolicy` `clouddeploy.deliveryPipelines.list` `clouddeploy.deliveryPipelines.listEffectiveTags` `clouddeploy.deliveryPipelines.listTagBindings` `clouddeploy.deliveryPipelines.update` `clouddeploy.deployPolicies.get` `clouddeploy.deployPolicies.getIamPolicy` `clouddeploy.deployPolicies.list` `clouddeploy.jobRuns.*`

  * `clouddeploy.jobRuns.get`
  * `clouddeploy.jobRuns.list`
  * `clouddeploy.jobRuns.terminate`

`clouddeploy.locations.*`

  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`

`clouddeploy.operations.*`

  * `clouddeploy.operations.cancel`
  * `clouddeploy.operations.delete`
  * `clouddeploy.operations.get`
  * `clouddeploy.operations.list`

`clouddeploy.releases.*`

  * `clouddeploy.releases.abandon`
  * `clouddeploy.releases.create`
  * `clouddeploy.releases.get`
  * `clouddeploy.releases.list`

`clouddeploy.rollouts.advance` `clouddeploy.rollouts.cancel` `clouddeploy.rollouts.create` `clouddeploy.rollouts.get` `clouddeploy.rollouts.ignoreJob` `clouddeploy.rollouts.list` `clouddeploy.rollouts.retryJob` `clouddeploy.rollouts.rollback` `clouddeploy.targets.create` `clouddeploy.targets.createTagBinding` `clouddeploy.targets.delete` `clouddeploy.targets.deleteTagBinding` `clouddeploy.targets.get` `clouddeploy.targets.getIamPolicy` `clouddeploy.targets.list` `clouddeploy.targets.listEffectiveTags` `clouddeploy.targets.listTagBindings` `clouddeploy.targets.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Policy Admin 

(`roles/clouddeploy.policyAdmin`) Permission to manage Deploy Policies.  |  `clouddeploy.deployPolicies.*`

  * `clouddeploy.deployPolicies.create`
  * `clouddeploy.deployPolicies.delete`
  * `clouddeploy.deployPolicies.get`
  * `clouddeploy.deployPolicies.getIamPolicy`
  * `clouddeploy.deployPolicies.list`
  * `clouddeploy.deployPolicies.override`
  * `clouddeploy.deployPolicies.setIamPolicy`
  * `clouddeploy.deployPolicies.update`

`clouddeploy.locations.*`

  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`

`clouddeploy.operations.*`

  * `clouddeploy.operations.cancel`
  * `clouddeploy.operations.delete`
  * `clouddeploy.operations.get`
  * `clouddeploy.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Policy Overrider 

(`roles/clouddeploy.policyOverrider`) Permission to override Deploy Policies.  |  `clouddeploy.deployPolicies.get` `clouddeploy.deployPolicies.list` `clouddeploy.deployPolicies.override` `clouddeploy.locations.*`

  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`

`clouddeploy.operations.*`

  * `clouddeploy.operations.cancel`
  * `clouddeploy.operations.delete`
  * `clouddeploy.operations.get`
  * `clouddeploy.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Deploy Releaser 

(`roles/clouddeploy.releaser`) Permission to create Cloud Deploy releases and rollouts.  |  `clouddeploy.config.get` `clouddeploy.customTargetTypes.get` `clouddeploy.deliveryPipelines.get` `clouddeploy.jobRuns.get` `clouddeploy.jobRuns.list` `clouddeploy.locations.*`

  * `clouddeploy.locations.get`
  * `clouddeploy.locations.list`

`clouddeploy.operations.*`

  * `clouddeploy.operations.cancel`
  * `clouddeploy.operations.delete`
  * `clouddeploy.operations.get`
  * `clouddeploy.operations.list`

`clouddeploy.releases.create` `clouddeploy.releases.get` `clouddeploy.releases.list` `clouddeploy.rollouts.advance` `clouddeploy.rollouts.cancel` `clouddeploy.rollouts.create` `clouddeploy.rollouts.get` `clouddeploy.rollouts.list` `clouddeploy.rollouts.rollback` `clouddeploy.targets.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Deploy Service Agent 

(`roles/clouddeploy.serviceAgent`) Gives Cloud Deploy Service Account access to managed resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.workerpools.use` `iam.serviceAccounts.actAs` `iam.serviceAccounts.getAccessToken` `logging.logEntries.create` `pubsub.topics.get` `pubsub.topics.publish` `servicemanagement.services.report` `serviceusage.services.use` `storage.buckets.create` `storage.buckets.get` `storage.objects.get`  
  
## Cloud Deploy permissions

Permission | Included in roles  
---|---  
  
#### `clouddeploy.automationRuns.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.automationRuns.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.automationRuns.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.automations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.automations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.automations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.automations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.automations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.config.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Custom Target Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.customTargetTypeAdmin) (`roles/clouddeploy.customTargetTypeAdmin`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.jobRunner) (`roles/clouddeploy.jobRunner`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.customTargetTypes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Custom Target Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.customTargetTypeAdmin) (`roles/clouddeploy.customTargetTypeAdmin`)   
  
#### `clouddeploy.customTargetTypes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Custom Target Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.customTargetTypeAdmin) (`roles/clouddeploy.customTargetTypeAdmin`)   
  
#### `clouddeploy.customTargetTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Custom Target Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.customTargetTypeAdmin) (`roles/clouddeploy.customTargetTypeAdmin`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.customTargetTypes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Custom Target Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.customTargetTypeAdmin) (`roles/clouddeploy.customTargetTypeAdmin`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.customTargetTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Custom Target Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.customTargetTypeAdmin) (`roles/clouddeploy.customTargetTypeAdmin`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.customTargetTypes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Deploy Custom Target Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.customTargetTypeAdmin) (`roles/clouddeploy.customTargetTypeAdmin`)   
  
#### `clouddeploy.customTargetTypes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Custom Target Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.customTargetTypeAdmin) (`roles/clouddeploy.customTargetTypeAdmin`)   
  
#### `clouddeploy.deliveryPipelines.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.deliveryPipelines.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.deliveryPipelines.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.deliveryPipelines.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.deliveryPipelines.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.deliveryPipelines.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.deliveryPipelines.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.deliveryPipelines.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.deliveryPipelines.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.deliveryPipelines.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `clouddeploy.deliveryPipelines.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.deployPolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)   
  
#### `clouddeploy.deployPolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)   
  
#### `clouddeploy.deployPolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.deployPolicies.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.deployPolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.deployPolicies.override`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)   
  
#### `clouddeploy.deployPolicies.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)   
  
#### `clouddeploy.deployPolicies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)   
  
#### `clouddeploy.jobRuns.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.jobRuns.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.jobRuns.terminate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyAdmin) (`roles/clouddeploy.policyAdmin`)  [Cloud Deploy Policy Overrider](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.policyOverrider) (`roles/clouddeploy.policyOverrider`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.releases.abandon`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.releases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `clouddeploy.releases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.releases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.rollouts.advance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)   
  
#### `clouddeploy.rollouts.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)   
  
#### `clouddeploy.rollouts.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)   
  
#### `clouddeploy.rollouts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)   
  
#### `clouddeploy.rollouts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.rollouts.ignoreJob`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.rollouts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.approver) (`roles/clouddeploy.approver`)  [Cloud Deploy Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.developer) (`roles/clouddeploy.developer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.rollouts.retryJob`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.rollouts.rollback`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)   
  
#### `clouddeploy.targets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.targets.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `clouddeploy.targets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
#### `clouddeploy.targets.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `clouddeploy.targets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Cloud Deploy Releaser](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.releaser) (`roles/clouddeploy.releaser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.targets.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.targets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.targets.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.targets.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.viewer) (`roles/clouddeploy.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `clouddeploy.targets.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `clouddeploy.targets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Deploy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.admin) (`roles/clouddeploy.admin`)  [Cloud Deploy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.editor) (`roles/clouddeploy.editor`)  [Cloud Deploy Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.operator) (`roles/clouddeploy.operator`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
