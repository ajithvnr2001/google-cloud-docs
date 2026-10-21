---
url: https://docs.cloud.google.com/build/docs/custom-constraints/
title: Use custom organization policies \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:26.374478+00:00
---

# Use custom organization policies  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Use custom organization policies Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `cloudbuild.googleapis.com/BitbucketServerConfig`
  * `cloudbuild.googleapis.com/Build`
  * `cloudbuild.googleapis.com/BuildTrigger`
  * `cloudbuild.googleapis.com/Connection`
  * `cloudbuild.googleapis.com/GithubEnterpriseConfig`
  * `cloudbuild.googleapis.com/Repository`
  * `cloudbuild.googleapis.com/WorkerPool`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Required roles

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Cloud Build supported resources

The following table lists the Cloud Build resources that you can reference in custom constraints. 

Resource | Field  
---|---  
cloudbuild.googleapis.com/BitbucketServerConfig |  `resource.apiKey`  
`resource.hostUri`  
`resource.name`  
`resource.peeredNetwork`  
`resource.peeredNetworkIpRange`  
`resource.secrets.adminAccessTokenVersionName`  
`resource.secrets.readAccessTokenVersionName`  
`resource.secrets.webhookSecretVersionName`  
`resource.sslCa`  
`resource.username`  
cloudbuild.googleapis.com/Build |  `resource.artifacts.goModules.modulePath`  
`resource.artifacts.goModules.moduleVersion`  
`resource.artifacts.goModules.repositoryLocation`  
`resource.artifacts.goModules.repositoryName`  
`resource.artifacts.goModules.repositoryProjectId`  
`resource.artifacts.goModules.sourcePath`  
`resource.artifacts.images`  
`resource.artifacts.mavenArtifacts.artifactId`  
`resource.artifacts.mavenArtifacts.groupId`  
`resource.artifacts.mavenArtifacts.path`  
`resource.artifacts.mavenArtifacts.repository`  
`resource.artifacts.mavenArtifacts.version`  
`resource.artifacts.npmPackages.packagePath`  
`resource.artifacts.npmPackages.repository`  
`resource.artifacts.objects.location`  
`resource.artifacts.objects.paths`  
`resource.artifacts.pythonPackages.paths`  
`resource.artifacts.pythonPackages.repository`  
`resource.availableSecrets.inline.envMap`  
`resource.availableSecrets.inline.kmsKeyName`  
`resource.availableSecrets.secretManager.env`  
`resource.availableSecrets.secretManager.versionName`  
`resource.dependencies.empty`  
`resource.dependencies.gitSource.depth`  
`resource.dependencies.gitSource.destPath`  
`resource.dependencies.gitSource.recurseSubmodules`  
`resource.dependencies.gitSource.repository.developerConnect`  
`resource.dependencies.gitSource.repository.url`  
`resource.dependencies.gitSource.revision`  
`resource.gitConfig.http.proxySecretVersionName`  
`resource.images`  
`resource.logsBucket`  
`resource.options.automapSubstitutions`  
`resource.options.defaultLogsBucketBehavior`  
`resource.options.diskSizeGb`  
`resource.options.dynamicSubstitutions`  
`resource.options.enableStructuredLogging`  
`resource.options.env`  
`resource.options.logging`  
`resource.options.logStreamingOption`  
`resource.options.machineType`  
`resource.options.pool.name`  
`resource.options.pubsubTopic`  
`resource.options.requestedVerifyOption`  
`resource.options.secretEnv`  
`resource.options.sourceProvenanceHash`  
`resource.options.substitutionOption`  
`resource.options.volumes.name`  
`resource.options.volumes.path`  
`resource.queueTtl`  
`resource.secrets.kmsKeyName`  
`resource.secrets.secretEnv`  
`resource.serviceAccount`  
`resource.source.connectedRepository.dir`  
`resource.source.connectedRepository.repository`  
`resource.source.connectedRepository.revision`  
`resource.source.developerConnectConfig.dir`  
`resource.source.developerConnectConfig.gitRepositoryLink`  
`resource.source.developerConnectConfig.revision`  
`resource.source.gitSource.dir`  
`resource.source.gitSource.revision`  
`resource.source.gitSource.url`  
`resource.source.repoSource.branchName`  
`resource.source.repoSource.commitSha`  
`resource.source.repoSource.dir`  
`resource.source.repoSource.invertRegex`  
`resource.source.repoSource.projectId`  
`resource.source.repoSource.repoName`  
`resource.source.repoSource.substitutions`  
`resource.source.repoSource.tagName`  
`resource.source.storageSource.bucket`  
`resource.source.storageSource.generation`  
`resource.source.storageSource.object`  
`resource.source.storageSource.sourceFetcher`  
`resource.source.storageSourceManifest.bucket`  
`resource.source.storageSourceManifest.generation`  
`resource.source.storageSourceManifest.object`  
`resource.steps.allowExitCodes`  
`resource.steps.allowFailure`  
`resource.steps.args`  
`resource.steps.automapSubstitutions`  
`resource.steps.dir`  
`resource.steps.entrypoint`  
`resource.steps.env`  
`resource.steps.id`  
`resource.steps.name`  
`resource.steps.script`  
`resource.steps.secretEnv`  
`resource.steps.timeout`  
`resource.steps.volumes.name`  
`resource.steps.volumes.path`  
`resource.steps.waitFor`  
`resource.substitutions`  
`resource.tags`  
`resource.timeout`  
cloudbuild.googleapis.com/BuildTrigger |  `resource.approvalConfig.approvalRequired`  
`resource.autodetect`  
`resource.bitbucketServerTriggerConfig.bitbucketServerConfigResource`  
`resource.bitbucketServerTriggerConfig.projectKey`  
`resource.bitbucketServerTriggerConfig.pullRequest.branch`  
`resource.bitbucketServerTriggerConfig.pullRequest.commentControl`  
`resource.bitbucketServerTriggerConfig.pullRequest.invertRegex`  
`resource.bitbucketServerTriggerConfig.push.branch`  
`resource.bitbucketServerTriggerConfig.push.invertRegex`  
`resource.bitbucketServerTriggerConfig.push.tag`  
`resource.bitbucketServerTriggerConfig.repoSlug`  
`resource.build.artifacts.images`  
`resource.build.artifacts.mavenArtifacts.artifactId`  
`resource.build.artifacts.mavenArtifacts.groupId`  
`resource.build.artifacts.mavenArtifacts.path`  
`resource.build.artifacts.mavenArtifacts.repository`  
`resource.build.artifacts.mavenArtifacts.version`  
`resource.build.artifacts.npmPackages.packagePath`  
`resource.build.artifacts.npmPackages.repository`  
`resource.build.artifacts.objects.location`  
`resource.build.artifacts.objects.paths`  
`resource.build.artifacts.pythonPackages.paths`  
`resource.build.artifacts.pythonPackages.repository`  
`resource.build.availableSecrets.inline.envMap`  
`resource.build.availableSecrets.inline.kmsKeyName`  
`resource.build.availableSecrets.secretManager.env`  
`resource.build.availableSecrets.secretManager.versionName`  
`resource.build.dependencies.empty`  
`resource.build.dependencies.gitSource.depth`  
`resource.build.dependencies.gitSource.destPath`  
`resource.build.dependencies.gitSource.recurseSubmodules`  
`resource.build.dependencies.gitSource.repository.developerConnect`  
`resource.build.dependencies.gitSource.repository.url`  
`resource.build.dependencies.gitSource.revision`  
`resource.build.gitConfig.http.proxySecretVersionName`  
`resource.build.images`  
`resource.build.logsBucket`  
`resource.build.options.automapSubstitutions`  
`resource.build.options.defaultLogsBucketBehavior`  
`resource.build.options.diskSizeGb`  
`resource.build.options.dynamicSubstitutions`  
`resource.build.options.env`  
`resource.build.options.logging`  
`resource.build.options.logStreamingOption`  
`resource.build.options.machineType`  
`resource.build.options.pool.name`  
`resource.build.options.requestedVerifyOption`  
`resource.build.options.secretEnv`  
`resource.build.options.sourceProvenanceHash`  
`resource.build.options.substitutionOption`  
`resource.build.options.volumes.name`  
`resource.build.options.volumes.path`  
`resource.build.queueTtl`  
`resource.build.secrets.kmsKeyName`  
`resource.build.secrets.secretEnv`  
`resource.build.serviceAccount`  
`resource.build.source.connectedRepository.dir`  
`resource.build.source.connectedRepository.repository`  
`resource.build.source.connectedRepository.revision`  
`resource.build.source.developerConnectConfig.dir`  
`resource.build.source.developerConnectConfig.gitRepositoryLink`  
`resource.build.source.developerConnectConfig.revision`  
`resource.build.source.gitSource.dir`  
`resource.build.source.gitSource.revision`  
`resource.build.source.gitSource.url`  
`resource.build.source.repoSource.branchName`  
`resource.build.source.repoSource.commitSha`  
`resource.build.source.repoSource.dir`  
`resource.build.source.repoSource.invertRegex`  
`resource.build.source.repoSource.projectId`  
`resource.build.source.repoSource.repoName`  
`resource.build.source.repoSource.substitutions`  
`resource.build.source.repoSource.tagName`  
`resource.build.source.storageSource.bucket`  
`resource.build.source.storageSource.generation`  
`resource.build.source.storageSource.object`  
`resource.build.source.storageSource.sourceFetcher`  
`resource.build.source.storageSourceManifest.bucket`  
`resource.build.source.storageSourceManifest.generation`  
`resource.build.source.storageSourceManifest.object`  
`resource.build.steps.allowExitCodes`  
`resource.build.steps.allowFailure`  
`resource.build.steps.args`  
`resource.build.steps.automapSubstitutions`  
`resource.build.steps.dir`  
`resource.build.steps.entrypoint`  
`resource.build.steps.env`  
`resource.build.steps.id`  
`resource.build.steps.name`  
`resource.build.steps.script`  
`resource.build.steps.secretEnv`  
`resource.build.steps.timeout`  
`resource.build.steps.volumes.name`  
`resource.build.steps.volumes.path`  
`resource.build.steps.waitFor`  
`resource.build.substitutions`  
`resource.build.tags`  
`resource.build.timeout`  
`resource.description`  
`resource.disabled`  
`resource.eventType`  
`resource.filename`  
`resource.filter`  
`resource.gitFileSource.bitbucketServerConfig`  
`resource.gitFileSource.githubEnterpriseConfig`  
`resource.gitFileSource.path`  
`resource.gitFileSource.repository`  
`resource.gitFileSource.repoType`  
`resource.gitFileSource.revision`  
`resource.gitFileSource.uri`  
`resource.github.enterpriseConfigResourceName`  
`resource.github.name`  
`resource.github.owner`  
`resource.github.pullRequest.branch`  
`resource.github.pullRequest.commentControl`  
`resource.github.pullRequest.invertRegex`  
`resource.github.push.branch`  
`resource.github.push.invertRegex`  
`resource.github.push.tag`  
`resource.gitlabEnterpriseEventsConfig.gitlabConfigResource`  
`resource.gitlabEnterpriseEventsConfig.projectNamespace`  
`resource.gitlabEnterpriseEventsConfig.pullRequest.branch`  
`resource.gitlabEnterpriseEventsConfig.pullRequest.commentControl`  
`resource.gitlabEnterpriseEventsConfig.pullRequest.invertRegex`  
`resource.gitlabEnterpriseEventsConfig.push.branch`  
`resource.gitlabEnterpriseEventsConfig.push.invertRegex`  
`resource.gitlabEnterpriseEventsConfig.push.tag`  
`resource.ignoredFiles`  
`resource.includeBuildLogs`  
`resource.includedFiles`  
`resource.name`  
`resource.pubsubConfig.serviceAccountEmail`  
`resource.pubsubConfig.topic`  
`resource.repositoryEventConfig.pullRequest.branch`  
`resource.repositoryEventConfig.pullRequest.commentControl`  
`resource.repositoryEventConfig.pullRequest.invertRegex`  
`resource.repositoryEventConfig.push.branch`  
`resource.repositoryEventConfig.push.invertRegex`  
`resource.repositoryEventConfig.push.tag`  
`resource.repositoryEventConfig.repository`  
`resource.resourceName`  
`resource.serviceAccount`  
`resource.sourceToBuild.bitbucketServerConfig`  
`resource.sourceToBuild.githubEnterpriseConfig`  
`resource.sourceToBuild.ref`  
`resource.sourceToBuild.repository`  
`resource.sourceToBuild.repoType`  
`resource.sourceToBuild.uri`  
`resource.substitutions`  
`resource.tags`  
`resource.triggerTemplate.branchName`  
`resource.triggerTemplate.commitSha`  
`resource.triggerTemplate.dir`  
`resource.triggerTemplate.invertRegex`  
`resource.triggerTemplate.projectId`  
`resource.triggerTemplate.repoName`  
`resource.triggerTemplate.substitutions`  
`resource.triggerTemplate.tagName`  
`resource.webhookConfig.secret`  
cloudbuild.googleapis.com/Connection |  `resource.annotations`  
`resource.bitbucketCloudConfig.authorizerCredential.userTokenSecretVersion`  
`resource.bitbucketCloudConfig.readAuthorizerCredential.userTokenSecretVersion`  
`resource.bitbucketCloudConfig.webhookSecretSecretVersion`  
`resource.bitbucketCloudConfig.workspace`  
`resource.bitbucketDataCenterConfig.authorizerCredential.userTokenSecretVersion`  
`resource.bitbucketDataCenterConfig.hostUri`  
`resource.bitbucketDataCenterConfig.readAuthorizerCredential.userTokenSecretVersion`  
`resource.bitbucketDataCenterConfig.serviceDirectoryConfig.service`  
`resource.bitbucketDataCenterConfig.sslCa`  
`resource.bitbucketDataCenterConfig.webhookSecretSecretVersion`  
`resource.disabled`  
`resource.githubConfig.appInstallationId`  
`resource.githubConfig.authorizerCredential.oauthTokenSecretVersion`  
`resource.githubEnterpriseConfig.apiKey`  
`resource.githubEnterpriseConfig.appId`  
`resource.githubEnterpriseConfig.appInstallationId`  
`resource.githubEnterpriseConfig.appSlug`  
`resource.githubEnterpriseConfig.authorizerCredential.oauthTokenSecretVersion`  
`resource.githubEnterpriseConfig.hostUri`  
`resource.githubEnterpriseConfig.oauthClientIdSecretVersion`  
`resource.githubEnterpriseConfig.oauthSecretSecretVersion`  
`resource.githubEnterpriseConfig.privateKeySecretVersion`  
`resource.githubEnterpriseConfig.serviceDirectoryConfig.service`  
`resource.githubEnterpriseConfig.sslCa`  
`resource.githubEnterpriseConfig.webhookSecretSecretVersion`  
`resource.gitlabConfig.authorizerCredential.userTokenSecretVersion`  
`resource.gitlabConfig.hostUri`  
`resource.gitlabConfig.readAuthorizerCredential.userTokenSecretVersion`  
`resource.gitlabConfig.serviceDirectoryConfig.service`  
`resource.gitlabConfig.sslCa`  
`resource.gitlabConfig.webhookSecretSecretVersion`  
`resource.name`  
cloudbuild.googleapis.com/GithubEnterpriseConfig |  `resource.appId`  
`resource.displayName`  
`resource.hostUrl`  
`resource.name`  
`resource.peeredNetwork`  
`resource.secrets.oauthClientIdVersionName`  
`resource.secrets.oauthSecretVersionName`  
`resource.secrets.privateKeyVersionName`  
`resource.secrets.webhookSecretVersionName`  
`resource.sslCa`  
`resource.webhookKey`  
cloudbuild.googleapis.com/Repository |  `resource.annotations`  
`resource.name`  
`resource.remoteUri`  
cloudbuild.googleapis.com/WorkerPool |  `resource.annotations`  
`resource.displayName`  
`resource.privatePoolV1Config.networkConfig.egressOption`  
`resource.privatePoolV1Config.networkConfig.peeredNetwork`  
`resource.privatePoolV1Config.networkConfig.peeredNetworkIpRange`  
`resource.privatePoolV1Config.privateServiceConnect.networkAttachment`  
`resource.privatePoolV1Config.privateServiceConnect.publicIpAddressDisabled`  
`resource.privatePoolV1Config.privateServiceConnect.routeAllTraffic`  
`resource.privatePoolV1Config.workerConfig.diskSizeGb`  
`resource.privatePoolV1Config.workerConfig.machineType`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.enableCloudBuildPubsubTrigger`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE  
      - UPDATE 
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.enableCloudBuildPubsubTrigger`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `cloudbuild.googleapis.com/BuildTrigger`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `resource.pubsubConfig != null && resource.pubsubConfig.topic.contains('cloud-build')`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Possible values are `ALLOW` and `DENY`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

The deny action means that if the condition evaluates to true, the operation to create or update the resource is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




## Enforce a custom organization policy

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.enableCloudBuildPubsubTrigger`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint and policy that allows creating a build trigger only if the trigger is of the Pub/Sub type and listens on topics that contain "cloud-build".

Before you begin, you must have the following:

  * Your organization ID
  * A project ID



### Create the constraint

To create a custom constraint, follow these steps:

  1. Create the following YAML file and save it as `constraint-enforce-vulnerabilityAssessmentTitle.yaml`:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.enableCloudBuildPubsubTrigger
         resourceTypes:
         - cloudbuild.googleapis.com/BuildTrigger
         methodTypes:
         - CREATE
         condition:  "resource.pubsubConfig != null && resource.pubsubConfig.topic.contains('cloud-build')"
         actionType: ALLOW
         displayName: Requires Pub/Sub triggers to contain "cloud-build" in the topic name.
         description: Pub/Sub triggers must contain "cloud-build" in the topic name.
         

Replace `ORGANIZATION_ID` with your organization ID.

  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint ~/constraint-enforce-vulnerabilityAssessmentTitle
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output is similar to the following:
         
         CUSTOM_CONSTRAINT                                          ACTION_TYPE  METHOD_TYPES   RESOURCE_TYPES                           DISPLAY_NAME
         custom.enableCloudBuildPubsubTrigger                       DENY         CREATE         cloudbuild.googleapis.com/BuildTrigger   Enable creating Pub/Sub trigger that listens on topics that contain "cloud-build".
         ...
         




### Create the policy

Create a policy and apply it to the custom constraint that you created:

  1. Save the following file as `policy-enforce-enableCloudBuildPubsubTrigger.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.enforceEnableCloudBuildPubsubTrigger
         spec:
           rules:
           - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy ~/policy-enforce-enableCloudBuildPubsubTrigger.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT                                     LIST_POLICY    BOOLEAN_POLICY    ETAG
         custom.enforceEnableCloudBuildPubsubTrigger    -              SET               COCsm5QGENiXi2E=
         




After you apply the policy, wait about two minutes for Google Cloud to start enforcing the policy.

### Test the policy

To test the policy, do the following:

  1. [Create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic) that doesn't include `cloud-build` in the topic ID.

  2. [Create a Pub/Sub trigger](https://docs.cloud.google.com/build/docs/automate-builds-pubsub-events?generation=2nd-gen#ar_build_trigger) for that topic.

The output is the following:
         
         Operation denied by custom org policies: ["customConstraints/custom.enableCloudBuildPubsubTrigger": "Pub/Sub triggers must contain "cloud-build" in the topic name."]
         




## Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints.

Description | Constraint syntax  
---|---  
Builds must use `cloudbuild.yaml` as the build config file. | 
    
    
        actionType: ALLOW
        condition: "resource.source.storageSource.object.endsWith('cloudbuild.yaml')"
        description: All builds must use cloudbuild.yaml as the build configuration file.
        displayName: Enforce cloudbuild.yaml as the build config file name.
        methodTypes:
          - CREATE
        name: organizations/ORGANIZATION_ID/customConstraints/custom.enforceCloudBuildFileName
        resourceTypes:
          - cloudbuild.googleapis.com/Build
          
  
Build triggers must use approved repository | 
    
    
        actionType: ALLOW
        condition: "resource.repoSource.repoName == 'projects/PROJECT_ID/repos/approved-app-repo'"
        description: All Cloud Build Triggers must use the approved-app-repo repository.
        displayName: Enforce approved repository for build triggers
        methodTypes:
          - CREATE
        name: organizations/ORGANIZATION_ID/customConstraints/custom.enforceCloudBuildFileName
        resourceTypes:
          - cloudbuild.googleapis.com/BuildTrigger
          
  
## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
