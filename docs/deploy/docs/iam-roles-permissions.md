---
url: https://docs.cloud.google.com/deploy/docs/iam-roles-permissions/
title: IAM roles and permissions \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:46.728000+00:00
---

# IAM roles and permissions  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/iam-roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  IAM roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Cloud Deploy service accounts, roles, and permissions.

Access in Cloud Deploy is controlled using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam). IAM lets you create and manage permissions for Google Cloud resources. Cloud Deploy provides a specific set of [predefined IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#role-types) where each role contains a set of permissions. You can use these roles to give more fine-grained access to specific Google Cloud resources and prevent unwanted access to other resources. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

See [Using IAM to restrict Cloud Deploy access](https://docs.cloud.google.com/deploy/docs/securing/iam) to learn about advanced access-control security features.

## Service accounts in Cloud Deploy

By default, Cloud Deploy runs using the default Compute Engine service account. For more information on configuring this service account for use with Cloud Deploy, or choosing a different account, see the [Cloud Deploy execution service account](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#execution-service-account) documentation.

[Find out more](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account) about how Cloud Deploy uses service accounts.

## Predefined Cloud Deploy roles

With IAM, every API method in Cloud Deploy API requires that the identity making the API request has the appropriate permissions to use the resource. Permissions are granted by setting policies that grant roles to a principal (user, group, or service account) of your project. You can grant multiple roles to a principal on the same resource.

The IAM documentation includes a [searchable reference](https://docs.cloud.google.com/iam/docs/roles-permissions) of all predefined roles.

The following table lists the Cloud Deploy IAM roles and the permissions that they include:

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
**Note:** If an [alternate service account](https://docs.cloud.google.com/deploy/docs/execution-environment#changing_from_the_default_to_custom_execution_service_account) is specified on the target, users with the `roles/clouddeploy.admin`, `.developer`, and `.operator` roles must also have the `iam.serviceAccounts.actAs` permission for the service accounts specified in a rollout target.

In addition to the Cloud Deploy predefined roles, the [basic](https://docs.cloud.google.com/iam/docs/roles-overview#basic) Viewer, Editor, and Owner roles also include permissions related to Cloud Deploy. However, we recommend that you grant predefined roles where possible to comply with the [security principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

## Permissions

The following table lists the permissions that the caller must have to call each method:

API Method | Required permission | Description  
---|---|---  
`automations.create()` | `clouddeploy.automations.create` | Create a new automation resource.  
`automations.delete()` | `clouddeploy.automations.delete` | Delete an existing automation resource.  
`automations.get()` | `clouddeploy.automations.get` | Retrieve details for an individual automation resource.  
`automations.list()` | `clouddeploy.automations.list` | List automation resources and their metadata.  
`automations.update()` | `clouddeploy.automations.update` | Update an existing automation resource.  
`automationRuns.cancel()` | `clouddeploy.automationRuns.cancel` | Cancel a running automation.  
`automationRuns.get()` | `clouddeploy.automationRuns.get` | Retrieve details for an individual automation run.  
`automationRuns.list()` | `clouddeploy.automationRuns.list` | List automation runs and their metadata.  
`customTargetTypes.create()` | `clouddeploy.customTargetTypes.create` | Create a custom target type resource.  
`customTargetTypes.delete()` | `clouddeploy.customTargetTypes.delete` | Delete a custom target type resource.  
`customTargetTypes.get()` | `clouddeploy.customTargetTypes.get` | Retrieve details for a custom target type.  
`customTargetTypes.getIamPolicy()` | `clouddeploy.customTargetTypes.getIamPolicy` | Get the IAM policy for a custom target type resource.  
`customTargetTypes.list()` | `clouddeploy.customTargetTypes.list` | List available custom target types and their metadata.  
`customTargetTypes.patch()` | `clouddeploy.customTargetTypes.patch` | Update an existing custom target type.  
`customTargetTypes.setIamPolicy()` | `clouddeploy.customTargetTypes.setIamPolicy` | Set the IAM policy for a custom target type resource.  
`deliveryPipelines.create()` | `clouddeploy.deliveryPipelines.create` | Create a new delivery pipeline resource.  
`deliveryPipelines.delete()` | `clouddeploy.deliveryPipelines.delete` | Delete an existing delivery pipeline resource.  
`deliveryPipelines.get()` | `clouddeploy.deliveryPipelines.get` | Retrieve details for an individual delivery pipeline.  
`deliveryPipelines.getIamPolicy()` | `clouddeploy.deliveryPipelines.getIamPolicy` | Get the IAM policy for a delivery pipeline resource.  
`deliveryPipelines.list()` | `clouddeploy.deliveryPipelines.list` | List delivery pipelines and their metadata.  
`deliveryPipelines.rollbackTarget()` | `clouddeploy.rollouts.rollback` | Rolls back a target.  
`deliveryPipelines.setIamPolicy()` | `clouddeploy.deliveryPipelines.setIamPolicy` | Set the IAM policy for a delivery pipeline resource.  
`deliveryPipelines.update()` | `clouddeploy.deliveryPipelines.update` | Update an existing delivery pipeline resource.  
`deployPolicies.create()` | `clouddeploy.deployPolicies.create` | Create a deploy policy resource.  
`deployPolicies.delete()` | `clouddeploy.deployPolicies.delete` | Delete a deploy policy resource.  
`deployPolicies.get()` | `clouddeploy.deployPolicies.get` | Retrieve details for a deploy policy resource.  
`deployPolicies.list()` | `clouddeploy.deployPolicies.list` | List available deploy policies and their metadata.  
`jobRuns.get()` | `clouddeploy.jobRuns.get` | Retrieve a `JobRuns` resource.  
`jobRuns.list()` | `clouddeploy.jobRuns.list` | List `JobRuns` resources and their metadata.  
`jobRuns.terminate()` | `clouddeploy.jobRuns.terminate` | Terminate an in-progress job run.  
`operations.cancel()` | `clouddeploy.operations.cancel` | Cancel a long-running operation.  
`operation.delete()` | `clouddeploy.operations.delete` | Delete a long-running operation.  
`operations.get()` | `clouddeploy.operations.get` | Get a specific long-running operation (for example, to return the status of a release's creation).  
`operations.list()` | `clouddeploy.operations.list` | List long-running operations.  
`releases.abandon()` | `clouddeploy.releases.abandon` | Abandon a release and prevent further rollouts against the release.  
`releases.create()` | `clouddeploy.releases.create` | Create a new release resource. The caller also requires `iam.serviceAccounts.actAs` permission on the service account used to render the manifest.  
`releases.get()` | `clouddeploy.releases.get` | Retrieve details for individual release.  
`releases.list()` | `clouddeploy.releases.list` | List releases and metadata.  
`rollouts.advance()` | `clouddeploy.rollouts.advance` | Advance a rollout to the next phase.  
`rollouts.approve()` | `clouddeploy.rollouts.approve` | Approve or reject a rollout with approval state of `required`.  
`rollouts.cancel()` | `clouddeploy.rollouts.cancel` | Cancel a rollout.  
`rollouts.create()` | `clouddeploy.rollouts.create` | Create a new rollout resource or promote a release. The caller also requires `iam.serviceAccounts.actAs` permission on the project or service account used to deploy.  
`rollouts.get()` | `clouddeploy.rollouts.get` | Retrieve details for individual rollout.  
`rollouts.ignoreJob()` | `clouddeploy.rollouts.ignoreJob` | Ignore a failed job.  
`rollouts.list()` | `clouddeploy.rollouts.list` | List rollouts and metadata.  
`rollouts.retryJob()` | `clouddeploy.rollouts.retryJob` | Retries a failed job.  
`rollouts.advance()`, `rollouts.approve()`, `rollouts.cancel()`, `rollouts.create()`, `rollouts.ignoreJob()`, `rollouts.retryJob()`, `deliveryPipelines.rollbackTarget()`, `jobRuns.terminate()` | `clouddeploy.deployPolicies.override` | Override a deploy policy resource.  
`deployPolicies.update()` | `clouddeploy.deployPolicies.update` | Update an existing deploy policy resource.  
`targets.create()` | `clouddeploy.targets.create` | Create a new target resource.  
`targets.delete()` | `clouddeploy.targets.delete` | Delete an existing target resource.  
`targets.get()` | `clouddeploy.targets.get` | Retrieve details for an individual target.  
`targets.getIamPolicy()` | `clouddeploy.targets.getIamPolicy` | Gets the IAM policy for a target resource.  
`targets.list()` | `clouddeploy.targets.list` | List targets and their metadata.  
`targets.setIamPolicy()` | `clouddeploy.targets.setIamPolicy` | Sets the IAM policy for a target resource.  
`targets.update()` | `clouddeploy.targets.update` | Update an existing target resource.  
  
## Using IAM to restrict actions on Cloud Deploy resources

You can secure your Cloud Deploy resources using IAM in the following ways:

  * IAM meta APIs

Use [`setIamPolicy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) on Cloud Deploy resources to restrict actions on those resources.

  * Conditional IAM

Programmatically apply [access policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview), including the [conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) under which to grant or deny access.




You can use these policies and conditions to restrict the following actions on your Cloud Deploy resources:

  * Create a delivery pipeline or target

You can grant this access to specific users or groups.

  * Update or delete a specific delivery pipeline

You can grant this access to specific users or groups.

  * Create a release for a specific delivery pipeline

You can grant this access to specific users or groups.

  * Update or delete a specific target

You can grant this access to specific users or groups.

  * Create or approve a rollout or promote a release

You can grant this access to specific users or groups for a specific target or delivery pipeline.

You can also set a condition that limits this access to within a specified time window.




## What's next

  * Learn about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [using conditions in IAM](https://docs.cloud.google.com/deploy/docs/securing/iam#about_iam_conditions)
  * Find out more about [Cloud Deploy service accounts](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
