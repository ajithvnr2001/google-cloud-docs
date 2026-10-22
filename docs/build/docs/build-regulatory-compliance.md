---
url: https://docs.cloud.google.com/build/docs/build-regulatory-compliance/
title: Regulatory support in Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:53.844161+00:00
---

# Regulatory support in Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/build-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Resources ](https://docs.cloud.google.com/build/docs/resources)



Send feedback 

#  Regulatory support in Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Cloud Build that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Cloud Build APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
cloudbuild.googleapis.com | v1 |  SUPPORTED   
cloudbuild.googleapis.com | v2 |  SUPPORTED   
  
### Compliance supported regions

Cloud Build is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### API fields for sensitive data

#### Resource: No resource

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/appmanifest:constructAppManifest` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.ConstructAppManifest`

| 

  * `apiKey`
  * `hostUrl`
  * `sslCa`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/appmanifest:constructAppManifest` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.ConstructAppManifest`

| 

  * `apiKey`
  * `hostUrl`
  * `sslCa`

  
  
#### Resource: cloudbuild.googleapis.com/Build

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudbuild.googleapis.com` REST API: `GET` `/v1/projects/{project_id}/builds` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.ListBuilds`

| 

  * `filter`

  
Service: `cloudbuild.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/builds` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.ListBuilds`

| 

  * `filter`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/projects/{project_id}/builds` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.CreateBuild`

| 

  * `build.artifacts.genericArtifacts.contentHandling`
  * `build.artifacts.genericArtifacts.folder`
  * `build.artifacts.genericArtifacts.registryPath`
  * `build.artifacts.goModules.modulePath`
  * `build.artifacts.goModules.moduleVersion`
  * `build.artifacts.goModules.sourcePath`
  * `build.artifacts.images`
  * `build.artifacts.mavenArtifacts.artifactId`
  * `build.artifacts.mavenArtifacts.deployFolder`
  * `build.artifacts.mavenArtifacts.groupId`
  * `build.artifacts.mavenArtifacts.path`
  * `build.artifacts.mavenArtifacts.pomPath`
  * `build.artifacts.mavenArtifacts.version`
  * `build.artifacts.npmPackages.archive`
  * `build.artifacts.npmPackages.packagePath`
  * `build.artifacts.npmPackages.repository`
  * `build.artifacts.objects.location`
  * `build.artifacts.objects.paths`
  * `build.artifacts.oci.file`
  * `build.artifacts.oci.registryPath`
  * `build.artifacts.oci.tags`
  * `build.artifacts.pythonPackages.paths`
  * `build.artifacts.testResults.bucketUri`
  * `build.artifacts.testResults.format`
  * `build.artifacts.testResults.paths`
  * `build.artifacts.volumes.name`
  * `build.artifacts.volumes.path`
  * `build.availableSecrets.inline.envMap.key`
  * `build.availableSecrets.inline.envMap.value`
  * `build.availableSecrets.inline.kmsKeyName`
  * `build.availableSecrets.secretManager.env`
  * `build.availableSecrets.secretManager.versionName`
  * `build.buildReceipt.workerDiagnostics.identityEndpointSuccesses`
  * `build.dependencies.empty`
  * `build.dependencies.genericArtifact.destPath`
  * `build.dependencies.genericArtifact.resource`
  * `build.dependencies.gitSource.depth`
  * `build.dependencies.gitSource.destPath`
  * `build.dependencies.gitSource.recurseSubmodules`
  * `build.dependencies.gitSource.repository.developerConnect`
  * `build.dependencies.gitSource.repository.proxyUrlEnabled`
  * `build.dependencies.gitSource.repository.url`
  * `build.dependencies.gitSource.revision`
  * `build.gitConfig.http.proxySecretVersionName`
  * `build.gitConfig.http.sslCaInfo`
  * `build.images`
  * `build.logsBucket`
  * `build.options.env`
  * `build.options.secretEnv`
  * `build.options.volumes.name`
  * `build.options.volumes.path`
  * `build.secrets.kmsKeyName`
  * `build.secrets.secretEnv.key`
  * `build.secrets.secretEnv.value`
  * `build.serviceAccount`
  * `build.source.buildConfigFileName`
  * `build.source.connectedRepository.dir`
  * `build.source.connectedRepository.repository`
  * `build.source.connectedRepository.revision`
  * `build.source.developerConnectConfig.dir`
  * `build.source.developerConnectConfig.gitRepositoryLink`
  * `build.source.developerConnectConfig.revision`
  * `build.source.gitSource.commitSha`
  * `build.source.gitSource.dir`
  * `build.source.gitSource.revision`
  * `build.source.gitSource.url`
  * `build.source.repoSource.branchName`
  * `build.source.repoSource.commitSha`
  * `build.source.repoSource.dir`
  * `build.source.repoSource.invertRegex`
  * `build.source.repoSource.projectId`
  * `build.source.repoSource.repoName`
  * `build.source.repoSource.substitutions.key`
  * `build.source.repoSource.substitutions.value`
  * `build.source.repoSource.tagName`
  * `build.source.storageSource.bucket`
  * `build.source.storageSource.generation`
  * `build.source.storageSource.object`
  * `build.source.storageSource.sourceFetcher`
  * `build.source.storageSource.stripComponents`
  * `build.source.storageSourceManifest.bucket`
  * `build.source.storageSourceManifest.generation`
  * `build.source.storageSourceManifest.object`
  * `build.steps.args`
  * `build.steps.dir`
  * `build.steps.entrypoint`
  * `build.steps.env`
  * `build.steps.id`
  * `build.steps.name`
  * `build.steps.remoteConfig`
  * `build.steps.results.attestationContent`
  * `build.steps.results.attestationType`
  * `build.steps.results.name`
  * `build.steps.script`
  * `build.steps.secretEnv`
  * `build.steps.volumes.name`
  * `build.steps.volumes.path`
  * `build.steps.waitFor`
  * `build.substitutions.key`
  * `build.substitutions.value`
  * `build.tags`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/{name=projects/*/builds/*}:approve` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.ApproveBuild`

| 

  * `approvalResult.comment`
  * `approvalResult.url`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/builds/*}:approve` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.ApproveBuild`

| 

  * `approvalResult.comment`
  * `approvalResult.url`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/builds` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.CreateBuild`

| 

  * `build.artifacts.genericArtifacts.contentHandling`
  * `build.artifacts.genericArtifacts.folder`
  * `build.artifacts.genericArtifacts.registryPath`
  * `build.artifacts.goModules.modulePath`
  * `build.artifacts.goModules.moduleVersion`
  * `build.artifacts.goModules.sourcePath`
  * `build.artifacts.images`
  * `build.artifacts.mavenArtifacts.artifactId`
  * `build.artifacts.mavenArtifacts.deployFolder`
  * `build.artifacts.mavenArtifacts.groupId`
  * `build.artifacts.mavenArtifacts.path`
  * `build.artifacts.mavenArtifacts.pomPath`
  * `build.artifacts.mavenArtifacts.version`
  * `build.artifacts.npmPackages.archive`
  * `build.artifacts.npmPackages.packagePath`
  * `build.artifacts.npmPackages.repository`
  * `build.artifacts.objects.location`
  * `build.artifacts.objects.paths`
  * `build.artifacts.oci.file`
  * `build.artifacts.oci.registryPath`
  * `build.artifacts.oci.tags`
  * `build.artifacts.pythonPackages.paths`
  * `build.artifacts.testResults.bucketUri`
  * `build.artifacts.testResults.format`
  * `build.artifacts.testResults.paths`
  * `build.artifacts.volumes.name`
  * `build.artifacts.volumes.path`
  * `build.availableSecrets.inline.envMap.key`
  * `build.availableSecrets.inline.envMap.value`
  * `build.availableSecrets.inline.kmsKeyName`
  * `build.availableSecrets.secretManager.env`
  * `build.availableSecrets.secretManager.versionName`
  * `build.buildReceipt.workerDiagnostics.identityEndpointSuccesses`
  * `build.dependencies.empty`
  * `build.dependencies.genericArtifact.destPath`
  * `build.dependencies.genericArtifact.resource`
  * `build.dependencies.gitSource.depth`
  * `build.dependencies.gitSource.destPath`
  * `build.dependencies.gitSource.recurseSubmodules`
  * `build.dependencies.gitSource.repository.developerConnect`
  * `build.dependencies.gitSource.repository.proxyUrlEnabled`
  * `build.dependencies.gitSource.repository.url`
  * `build.dependencies.gitSource.revision`
  * `build.gitConfig.http.proxySecretVersionName`
  * `build.gitConfig.http.sslCaInfo`
  * `build.images`
  * `build.logsBucket`
  * `build.options.env`
  * `build.options.secretEnv`
  * `build.options.volumes.name`
  * `build.options.volumes.path`
  * `build.secrets.kmsKeyName`
  * `build.secrets.secretEnv.key`
  * `build.secrets.secretEnv.value`
  * `build.serviceAccount`
  * `build.source.buildConfigFileName`
  * `build.source.connectedRepository.dir`
  * `build.source.connectedRepository.repository`
  * `build.source.connectedRepository.revision`
  * `build.source.developerConnectConfig.dir`
  * `build.source.developerConnectConfig.gitRepositoryLink`
  * `build.source.developerConnectConfig.revision`
  * `build.source.gitSource.commitSha`
  * `build.source.gitSource.dir`
  * `build.source.gitSource.revision`
  * `build.source.gitSource.url`
  * `build.source.repoSource.branchName`
  * `build.source.repoSource.commitSha`
  * `build.source.repoSource.dir`
  * `build.source.repoSource.invertRegex`
  * `build.source.repoSource.projectId`
  * `build.source.repoSource.repoName`
  * `build.source.repoSource.substitutions.key`
  * `build.source.repoSource.substitutions.value`
  * `build.source.repoSource.tagName`
  * `build.source.storageSource.bucket`
  * `build.source.storageSource.generation`
  * `build.source.storageSource.object`
  * `build.source.storageSource.sourceFetcher`
  * `build.source.storageSource.stripComponents`
  * `build.source.storageSourceManifest.bucket`
  * `build.source.storageSourceManifest.generation`
  * `build.source.storageSourceManifest.object`
  * `build.steps.args`
  * `build.steps.dir`
  * `build.steps.entrypoint`
  * `build.steps.env`
  * `build.steps.id`
  * `build.steps.name`
  * `build.steps.remoteConfig`
  * `build.steps.results.attestationContent`
  * `build.steps.results.attestationType`
  * `build.steps.results.name`
  * `build.steps.script`
  * `build.steps.secretEnv`
  * `build.steps.volumes.name`
  * `build.steps.volumes.path`
  * `build.steps.waitFor`
  * `build.substitutions.key`
  * `build.substitutions.value`
  * `build.tags`

  
  
#### Resource: cloudbuild.googleapis.com/BuildTrigger

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudbuild.googleapis.com` REST API: `PATCH` `/v1/projects/{project_id}/triggers/{trigger_id}` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.UpdateBuildTrigger`

| 

  * `trigger.baseImage.imageName`
  * `trigger.bitbucketServerTriggerConfig.pullRequest.branch`
  * `trigger.bitbucketServerTriggerConfig.push.branch`
  * `trigger.bitbucketServerTriggerConfig.push.tag`
  * `trigger.build.artifacts.genericArtifacts.contentHandling`
  * `trigger.build.artifacts.genericArtifacts.folder`
  * `trigger.build.artifacts.genericArtifacts.registryPath`
  * `trigger.build.artifacts.goModules.modulePath`
  * `trigger.build.artifacts.goModules.moduleVersion`
  * `trigger.build.artifacts.goModules.sourcePath`
  * `trigger.build.artifacts.images`
  * `trigger.build.artifacts.mavenArtifacts.artifactId`
  * `trigger.build.artifacts.mavenArtifacts.deployFolder`
  * `trigger.build.artifacts.mavenArtifacts.groupId`
  * `trigger.build.artifacts.mavenArtifacts.path`
  * `trigger.build.artifacts.mavenArtifacts.pomPath`
  * `trigger.build.artifacts.mavenArtifacts.version`
  * `trigger.build.artifacts.npmPackages.archive`
  * `trigger.build.artifacts.npmPackages.packagePath`
  * `trigger.build.artifacts.npmPackages.repository`
  * `trigger.build.artifacts.objects.location`
  * `trigger.build.artifacts.objects.paths`
  * `trigger.build.artifacts.oci.file`
  * `trigger.build.artifacts.oci.registryPath`
  * `trigger.build.artifacts.oci.tags`
  * `trigger.build.artifacts.pythonPackages.paths`
  * `trigger.build.artifacts.testResults.bucketUri`
  * `trigger.build.artifacts.testResults.format`
  * `trigger.build.artifacts.testResults.paths`
  * `trigger.build.artifacts.volumes.name`
  * `trigger.build.artifacts.volumes.path`
  * `trigger.build.availableSecrets.inline.envMap.key`
  * `trigger.build.availableSecrets.inline.envMap.value`
  * `trigger.build.availableSecrets.inline.kmsKeyName`
  * `trigger.build.availableSecrets.secretManager.env`
  * `trigger.build.availableSecrets.secretManager.versionName`
  * `trigger.build.buildReceipt.workerDiagnostics.identityEndpointSuccesses`
  * `trigger.build.dependencies.empty`
  * `trigger.build.dependencies.genericArtifact.destPath`
  * `trigger.build.dependencies.genericArtifact.resource`
  * `trigger.build.dependencies.gitSource.depth`
  * `trigger.build.dependencies.gitSource.destPath`
  * `trigger.build.dependencies.gitSource.recurseSubmodules`
  * `trigger.build.dependencies.gitSource.repository.developerConnect`
  * `trigger.build.dependencies.gitSource.repository.proxyUrlEnabled`
  * `trigger.build.dependencies.gitSource.repository.url`
  * `trigger.build.dependencies.gitSource.revision`
  * `trigger.build.gitConfig.http.proxySecretVersionName`
  * `trigger.build.gitConfig.http.sslCaInfo`
  * `trigger.build.images`
  * `trigger.build.logsBucket`
  * `trigger.build.options.env`
  * `trigger.build.options.secretEnv`
  * `trigger.build.options.volumes.name`
  * `trigger.build.options.volumes.path`
  * `trigger.build.secrets.kmsKeyName`
  * `trigger.build.secrets.secretEnv.key`
  * `trigger.build.secrets.secretEnv.value`
  * `trigger.build.serviceAccount`
  * `trigger.build.source.buildConfigFileName`
  * `trigger.build.source.connectedRepository.dir`
  * `trigger.build.source.connectedRepository.repository`
  * `trigger.build.source.connectedRepository.revision`
  * `trigger.build.source.developerConnectConfig.dir`
  * `trigger.build.source.developerConnectConfig.gitRepositoryLink`
  * `trigger.build.source.developerConnectConfig.revision`
  * `trigger.build.source.gitSource.commitSha`
  * `trigger.build.source.gitSource.dir`
  * `trigger.build.source.gitSource.revision`
  * `trigger.build.source.gitSource.url`
  * `trigger.build.source.repoSource.branchName`
  * `trigger.build.source.repoSource.commitSha`
  * `trigger.build.source.repoSource.dir`
  * `trigger.build.source.repoSource.invertRegex`
  * `trigger.build.source.repoSource.projectId`
  * `trigger.build.source.repoSource.repoName`
  * `trigger.build.source.repoSource.substitutions.key`
  * `trigger.build.source.repoSource.substitutions.value`
  * `trigger.build.source.repoSource.tagName`
  * `trigger.build.source.storageSource.bucket`
  * `trigger.build.source.storageSource.generation`
  * `trigger.build.source.storageSource.object`
  * `trigger.build.source.storageSource.sourceFetcher`
  * `trigger.build.source.storageSource.stripComponents`
  * `trigger.build.source.storageSourceManifest.bucket`
  * `trigger.build.source.storageSourceManifest.generation`
  * `trigger.build.source.storageSourceManifest.object`
  * `trigger.build.steps.args`
  * `trigger.build.steps.dir`
  * `trigger.build.steps.entrypoint`
  * `trigger.build.steps.env`
  * `trigger.build.steps.id`
  * `trigger.build.steps.name`
  * `trigger.build.steps.remoteConfig`
  * `trigger.build.steps.results.attestationContent`
  * `trigger.build.steps.results.attestationType`
  * `trigger.build.steps.results.name`
  * `trigger.build.steps.script`
  * `trigger.build.steps.secretEnv`
  * `trigger.build.steps.volumes.name`
  * `trigger.build.steps.volumes.path`
  * `trigger.build.steps.waitFor`
  * `trigger.build.substitutions.key`
  * `trigger.build.substitutions.value`
  * `trigger.build.tags`
  * `trigger.cloudCode.codeReview.branch`
  * `trigger.cloudCode.project`
  * `trigger.cloudCode.repo`
  * `trigger.description`
  * `trigger.developerConnectEventConfig.gitRepositoryLink`
  * `trigger.developerConnectEventConfig.pullRequest.branch`
  * `trigger.developerConnectEventConfig.pullRequest.commentControl`
  * `trigger.developerConnectEventConfig.pullRequest.invertRegex`
  * `trigger.developerConnectEventConfig.push.branch`
  * `trigger.developerConnectEventConfig.push.invertRegex`
  * `trigger.developerConnectEventConfig.push.tag`
  * `trigger.dir`
  * `trigger.eventType`
  * `trigger.filename`
  * `trigger.gitFileSource.bitbucketServerConfig`
  * `trigger.gitFileSource.githubEnterpriseConfig`
  * `trigger.gitFileSource.path`
  * `trigger.gitFileSource.repoType`
  * `trigger.gitFileSource.repository`
  * `trigger.gitFileSource.revision`
  * `trigger.gitFileSource.uri`
  * `trigger.github.pullRequest.branch`
  * `trigger.github.push.branch`
  * `trigger.github.push.tag`
  * `trigger.gitlabEnterpriseEventsConfig.pullRequest.branch`
  * `trigger.gitlabEnterpriseEventsConfig.push.branch`
  * `trigger.gitlabEnterpriseEventsConfig.push.tag`
  * `trigger.gitlabEventsConfig.pullRequest.branch`
  * `trigger.gitlabEventsConfig.push.branch`
  * `trigger.gitlabEventsConfig.push.tag`
  * `trigger.ignoredFiles`
  * `trigger.includeBuildLogs`
  * `trigger.includedFiles`
  * `trigger.internalAnnotations.tags`
  * `trigger.name`
  * `trigger.repositoryEventConfig.pullRequest.branch`
  * `trigger.repositoryEventConfig.pullRequest.commentControl`
  * `trigger.repositoryEventConfig.pullRequest.invertRegex`
  * `trigger.repositoryEventConfig.push.branch`
  * `trigger.repositoryEventConfig.push.invertRegex`
  * `trigger.repositoryEventConfig.push.tag`
  * `trigger.repositoryEventConfig.repository`
  * `trigger.serviceAccount`
  * `trigger.sourceToBuild.bitbucketServerConfig`
  * `trigger.sourceToBuild.githubEnterpriseConfig`
  * `trigger.sourceToBuild.ref`
  * `trigger.sourceToBuild.repoType`
  * `trigger.sourceToBuild.repository`
  * `trigger.sourceToBuild.uri`
  * `trigger.substitutions.key`
  * `trigger.substitutions.value`
  * `trigger.tags`
  * `trigger.triggerTemplate.branchName`
  * `trigger.triggerTemplate.commitSha`
  * `trigger.triggerTemplate.dir`
  * `trigger.triggerTemplate.invertRegex`
  * `trigger.triggerTemplate.repoName`
  * `trigger.triggerTemplate.substitutions.key`
  * `trigger.triggerTemplate.substitutions.value`
  * `trigger.triggerTemplate.tagName`
  * `trigger.uri`
  * `trigger.webhookConfig.secret`

  
Service: `cloudbuild.googleapis.com` REST API: `PATCH` `/v1/{trigger.resource_name=projects/*/locations/*/triggers/*}` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.UpdateBuildTrigger`

| 

  * `trigger.baseImage.imageName`
  * `trigger.bitbucketServerTriggerConfig.pullRequest.branch`
  * `trigger.bitbucketServerTriggerConfig.push.branch`
  * `trigger.bitbucketServerTriggerConfig.push.tag`
  * `trigger.build.artifacts.genericArtifacts.contentHandling`
  * `trigger.build.artifacts.genericArtifacts.folder`
  * `trigger.build.artifacts.genericArtifacts.registryPath`
  * `trigger.build.artifacts.goModules.modulePath`
  * `trigger.build.artifacts.goModules.moduleVersion`
  * `trigger.build.artifacts.goModules.sourcePath`
  * `trigger.build.artifacts.images`
  * `trigger.build.artifacts.mavenArtifacts.artifactId`
  * `trigger.build.artifacts.mavenArtifacts.deployFolder`
  * `trigger.build.artifacts.mavenArtifacts.groupId`
  * `trigger.build.artifacts.mavenArtifacts.path`
  * `trigger.build.artifacts.mavenArtifacts.pomPath`
  * `trigger.build.artifacts.mavenArtifacts.version`
  * `trigger.build.artifacts.npmPackages.archive`
  * `trigger.build.artifacts.npmPackages.packagePath`
  * `trigger.build.artifacts.npmPackages.repository`
  * `trigger.build.artifacts.objects.location`
  * `trigger.build.artifacts.objects.paths`
  * `trigger.build.artifacts.oci.file`
  * `trigger.build.artifacts.oci.registryPath`
  * `trigger.build.artifacts.oci.tags`
  * `trigger.build.artifacts.pythonPackages.paths`
  * `trigger.build.artifacts.testResults.bucketUri`
  * `trigger.build.artifacts.testResults.format`
  * `trigger.build.artifacts.testResults.paths`
  * `trigger.build.artifacts.volumes.name`
  * `trigger.build.artifacts.volumes.path`
  * `trigger.build.availableSecrets.inline.envMap.key`
  * `trigger.build.availableSecrets.inline.envMap.value`
  * `trigger.build.availableSecrets.inline.kmsKeyName`
  * `trigger.build.availableSecrets.secretManager.env`
  * `trigger.build.availableSecrets.secretManager.versionName`
  * `trigger.build.buildReceipt.workerDiagnostics.identityEndpointSuccesses`
  * `trigger.build.dependencies.empty`
  * `trigger.build.dependencies.genericArtifact.destPath`
  * `trigger.build.dependencies.genericArtifact.resource`
  * `trigger.build.dependencies.gitSource.depth`
  * `trigger.build.dependencies.gitSource.destPath`
  * `trigger.build.dependencies.gitSource.recurseSubmodules`
  * `trigger.build.dependencies.gitSource.repository.developerConnect`
  * `trigger.build.dependencies.gitSource.repository.proxyUrlEnabled`
  * `trigger.build.dependencies.gitSource.repository.url`
  * `trigger.build.dependencies.gitSource.revision`
  * `trigger.build.gitConfig.http.proxySecretVersionName`
  * `trigger.build.gitConfig.http.sslCaInfo`
  * `trigger.build.images`
  * `trigger.build.logsBucket`
  * `trigger.build.options.env`
  * `trigger.build.options.secretEnv`
  * `trigger.build.options.volumes.name`
  * `trigger.build.options.volumes.path`
  * `trigger.build.secrets.kmsKeyName`
  * `trigger.build.secrets.secretEnv.key`
  * `trigger.build.secrets.secretEnv.value`
  * `trigger.build.serviceAccount`
  * `trigger.build.source.buildConfigFileName`
  * `trigger.build.source.connectedRepository.dir`
  * `trigger.build.source.connectedRepository.repository`
  * `trigger.build.source.connectedRepository.revision`
  * `trigger.build.source.developerConnectConfig.dir`
  * `trigger.build.source.developerConnectConfig.gitRepositoryLink`
  * `trigger.build.source.developerConnectConfig.revision`
  * `trigger.build.source.gitSource.commitSha`
  * `trigger.build.source.gitSource.dir`
  * `trigger.build.source.gitSource.revision`
  * `trigger.build.source.gitSource.url`
  * `trigger.build.source.repoSource.branchName`
  * `trigger.build.source.repoSource.commitSha`
  * `trigger.build.source.repoSource.dir`
  * `trigger.build.source.repoSource.invertRegex`
  * `trigger.build.source.repoSource.projectId`
  * `trigger.build.source.repoSource.repoName`
  * `trigger.build.source.repoSource.substitutions.key`
  * `trigger.build.source.repoSource.substitutions.value`
  * `trigger.build.source.repoSource.tagName`
  * `trigger.build.source.storageSource.bucket`
  * `trigger.build.source.storageSource.generation`
  * `trigger.build.source.storageSource.object`
  * `trigger.build.source.storageSource.sourceFetcher`
  * `trigger.build.source.storageSource.stripComponents`
  * `trigger.build.source.storageSourceManifest.bucket`
  * `trigger.build.source.storageSourceManifest.generation`
  * `trigger.build.source.storageSourceManifest.object`
  * `trigger.build.steps.args`
  * `trigger.build.steps.dir`
  * `trigger.build.steps.entrypoint`
  * `trigger.build.steps.env`
  * `trigger.build.steps.id`
  * `trigger.build.steps.name`
  * `trigger.build.steps.remoteConfig`
  * `trigger.build.steps.results.attestationContent`
  * `trigger.build.steps.results.attestationType`
  * `trigger.build.steps.results.name`
  * `trigger.build.steps.script`
  * `trigger.build.steps.secretEnv`
  * `trigger.build.steps.volumes.name`
  * `trigger.build.steps.volumes.path`
  * `trigger.build.steps.waitFor`
  * `trigger.build.substitutions.key`
  * `trigger.build.substitutions.value`
  * `trigger.build.tags`
  * `trigger.cloudCode.codeReview.branch`
  * `trigger.cloudCode.project`
  * `trigger.cloudCode.repo`
  * `trigger.description`
  * `trigger.developerConnectEventConfig.gitRepositoryLink`
  * `trigger.developerConnectEventConfig.pullRequest.branch`
  * `trigger.developerConnectEventConfig.pullRequest.commentControl`
  * `trigger.developerConnectEventConfig.pullRequest.invertRegex`
  * `trigger.developerConnectEventConfig.push.branch`
  * `trigger.developerConnectEventConfig.push.invertRegex`
  * `trigger.developerConnectEventConfig.push.tag`
  * `trigger.dir`
  * `trigger.eventType`
  * `trigger.filename`
  * `trigger.gitFileSource.bitbucketServerConfig`
  * `trigger.gitFileSource.githubEnterpriseConfig`
  * `trigger.gitFileSource.path`
  * `trigger.gitFileSource.repoType`
  * `trigger.gitFileSource.repository`
  * `trigger.gitFileSource.revision`
  * `trigger.gitFileSource.uri`
  * `trigger.github.pullRequest.branch`
  * `trigger.github.push.branch`
  * `trigger.github.push.tag`
  * `trigger.gitlabEnterpriseEventsConfig.pullRequest.branch`
  * `trigger.gitlabEnterpriseEventsConfig.push.branch`
  * `trigger.gitlabEnterpriseEventsConfig.push.tag`
  * `trigger.gitlabEventsConfig.pullRequest.branch`
  * `trigger.gitlabEventsConfig.push.branch`
  * `trigger.gitlabEventsConfig.push.tag`
  * `trigger.ignoredFiles`
  * `trigger.includeBuildLogs`
  * `trigger.includedFiles`
  * `trigger.internalAnnotations.tags`
  * `trigger.name`
  * `trigger.repositoryEventConfig.pullRequest.branch`
  * `trigger.repositoryEventConfig.pullRequest.commentControl`
  * `trigger.repositoryEventConfig.pullRequest.invertRegex`
  * `trigger.repositoryEventConfig.push.branch`
  * `trigger.repositoryEventConfig.push.invertRegex`
  * `trigger.repositoryEventConfig.push.tag`
  * `trigger.repositoryEventConfig.repository`
  * `trigger.serviceAccount`
  * `trigger.sourceToBuild.bitbucketServerConfig`
  * `trigger.sourceToBuild.githubEnterpriseConfig`
  * `trigger.sourceToBuild.ref`
  * `trigger.sourceToBuild.repoType`
  * `trigger.sourceToBuild.repository`
  * `trigger.sourceToBuild.uri`
  * `trigger.substitutions.key`
  * `trigger.substitutions.value`
  * `trigger.tags`
  * `trigger.triggerTemplate.branchName`
  * `trigger.triggerTemplate.commitSha`
  * `trigger.triggerTemplate.dir`
  * `trigger.triggerTemplate.invertRegex`
  * `trigger.triggerTemplate.repoName`
  * `trigger.triggerTemplate.substitutions.key`
  * `trigger.triggerTemplate.substitutions.value`
  * `trigger.triggerTemplate.tagName`
  * `trigger.uri`
  * `trigger.webhookConfig.secret`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/projects/{project_id}/triggers` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.CreateBuildTrigger`

| 

  * `trigger.baseImage.imageName`
  * `trigger.bitbucketServerTriggerConfig.pullRequest.branch`
  * `trigger.bitbucketServerTriggerConfig.push.branch`
  * `trigger.bitbucketServerTriggerConfig.push.tag`
  * `trigger.build.artifacts.genericArtifacts.contentHandling`
  * `trigger.build.artifacts.genericArtifacts.folder`
  * `trigger.build.artifacts.genericArtifacts.registryPath`
  * `trigger.build.artifacts.goModules.modulePath`
  * `trigger.build.artifacts.goModules.moduleVersion`
  * `trigger.build.artifacts.goModules.sourcePath`
  * `trigger.build.artifacts.images`
  * `trigger.build.artifacts.mavenArtifacts.artifactId`
  * `trigger.build.artifacts.mavenArtifacts.deployFolder`
  * `trigger.build.artifacts.mavenArtifacts.groupId`
  * `trigger.build.artifacts.mavenArtifacts.path`
  * `trigger.build.artifacts.mavenArtifacts.pomPath`
  * `trigger.build.artifacts.mavenArtifacts.version`
  * `trigger.build.artifacts.npmPackages.archive`
  * `trigger.build.artifacts.npmPackages.packagePath`
  * `trigger.build.artifacts.npmPackages.repository`
  * `trigger.build.artifacts.objects.location`
  * `trigger.build.artifacts.objects.paths`
  * `trigger.build.artifacts.oci.file`
  * `trigger.build.artifacts.oci.registryPath`
  * `trigger.build.artifacts.oci.tags`
  * `trigger.build.artifacts.pythonPackages.paths`
  * `trigger.build.artifacts.testResults.bucketUri`
  * `trigger.build.artifacts.testResults.format`
  * `trigger.build.artifacts.testResults.paths`
  * `trigger.build.artifacts.volumes.name`
  * `trigger.build.artifacts.volumes.path`
  * `trigger.build.availableSecrets.inline.envMap.key`
  * `trigger.build.availableSecrets.inline.envMap.value`
  * `trigger.build.availableSecrets.inline.kmsKeyName`
  * `trigger.build.availableSecrets.secretManager.env`
  * `trigger.build.availableSecrets.secretManager.versionName`
  * `trigger.build.buildReceipt.workerDiagnostics.identityEndpointSuccesses`
  * `trigger.build.dependencies.empty`
  * `trigger.build.dependencies.genericArtifact.destPath`
  * `trigger.build.dependencies.genericArtifact.resource`
  * `trigger.build.dependencies.gitSource.depth`
  * `trigger.build.dependencies.gitSource.destPath`
  * `trigger.build.dependencies.gitSource.recurseSubmodules`
  * `trigger.build.dependencies.gitSource.repository.developerConnect`
  * `trigger.build.dependencies.gitSource.repository.proxyUrlEnabled`
  * `trigger.build.dependencies.gitSource.repository.url`
  * `trigger.build.dependencies.gitSource.revision`
  * `trigger.build.gitConfig.http.proxySecretVersionName`
  * `trigger.build.gitConfig.http.sslCaInfo`
  * `trigger.build.images`
  * `trigger.build.logsBucket`
  * `trigger.build.options.env`
  * `trigger.build.options.secretEnv`
  * `trigger.build.options.volumes.name`
  * `trigger.build.options.volumes.path`
  * `trigger.build.secrets.kmsKeyName`
  * `trigger.build.secrets.secretEnv.key`
  * `trigger.build.secrets.secretEnv.value`
  * `trigger.build.serviceAccount`
  * `trigger.build.source.buildConfigFileName`
  * `trigger.build.source.connectedRepository.dir`
  * `trigger.build.source.connectedRepository.repository`
  * `trigger.build.source.connectedRepository.revision`
  * `trigger.build.source.developerConnectConfig.dir`
  * `trigger.build.source.developerConnectConfig.gitRepositoryLink`
  * `trigger.build.source.developerConnectConfig.revision`
  * `trigger.build.source.gitSource.commitSha`
  * `trigger.build.source.gitSource.dir`
  * `trigger.build.source.gitSource.revision`
  * `trigger.build.source.gitSource.url`
  * `trigger.build.source.repoSource.branchName`
  * `trigger.build.source.repoSource.commitSha`
  * `trigger.build.source.repoSource.dir`
  * `trigger.build.source.repoSource.invertRegex`
  * `trigger.build.source.repoSource.projectId`
  * `trigger.build.source.repoSource.repoName`
  * `trigger.build.source.repoSource.substitutions.key`
  * `trigger.build.source.repoSource.substitutions.value`
  * `trigger.build.source.repoSource.tagName`
  * `trigger.build.source.storageSource.bucket`
  * `trigger.build.source.storageSource.generation`
  * `trigger.build.source.storageSource.object`
  * `trigger.build.source.storageSource.sourceFetcher`
  * `trigger.build.source.storageSource.stripComponents`
  * `trigger.build.source.storageSourceManifest.bucket`
  * `trigger.build.source.storageSourceManifest.generation`
  * `trigger.build.source.storageSourceManifest.object`
  * `trigger.build.steps.args`
  * `trigger.build.steps.dir`
  * `trigger.build.steps.entrypoint`
  * `trigger.build.steps.env`
  * `trigger.build.steps.id`
  * `trigger.build.steps.name`
  * `trigger.build.steps.remoteConfig`
  * `trigger.build.steps.results.attestationContent`
  * `trigger.build.steps.results.attestationType`
  * `trigger.build.steps.results.name`
  * `trigger.build.steps.script`
  * `trigger.build.steps.secretEnv`
  * `trigger.build.steps.volumes.name`
  * `trigger.build.steps.volumes.path`
  * `trigger.build.steps.waitFor`
  * `trigger.build.substitutions.key`
  * `trigger.build.substitutions.value`
  * `trigger.build.tags`
  * `trigger.cloudCode.codeReview.branch`
  * `trigger.cloudCode.project`
  * `trigger.cloudCode.repo`
  * `trigger.description`
  * `trigger.developerConnectEventConfig.gitRepositoryLink`
  * `trigger.developerConnectEventConfig.pullRequest.branch`
  * `trigger.developerConnectEventConfig.pullRequest.commentControl`
  * `trigger.developerConnectEventConfig.pullRequest.invertRegex`
  * `trigger.developerConnectEventConfig.push.branch`
  * `trigger.developerConnectEventConfig.push.invertRegex`
  * `trigger.developerConnectEventConfig.push.tag`
  * `trigger.dir`
  * `trigger.eventType`
  * `trigger.filename`
  * `trigger.gitFileSource.bitbucketServerConfig`
  * `trigger.gitFileSource.githubEnterpriseConfig`
  * `trigger.gitFileSource.path`
  * `trigger.gitFileSource.repoType`
  * `trigger.gitFileSource.repository`
  * `trigger.gitFileSource.revision`
  * `trigger.gitFileSource.uri`
  * `trigger.github.pullRequest.branch`
  * `trigger.github.push.branch`
  * `trigger.github.push.tag`
  * `trigger.gitlabEnterpriseEventsConfig.pullRequest.branch`
  * `trigger.gitlabEnterpriseEventsConfig.push.branch`
  * `trigger.gitlabEnterpriseEventsConfig.push.tag`
  * `trigger.gitlabEventsConfig.pullRequest.branch`
  * `trigger.gitlabEventsConfig.push.branch`
  * `trigger.gitlabEventsConfig.push.tag`
  * `trigger.ignoredFiles`
  * `trigger.includeBuildLogs`
  * `trigger.includedFiles`
  * `trigger.internalAnnotations.tags`
  * `trigger.name`
  * `trigger.repositoryEventConfig.pullRequest.branch`
  * `trigger.repositoryEventConfig.pullRequest.commentControl`
  * `trigger.repositoryEventConfig.pullRequest.invertRegex`
  * `trigger.repositoryEventConfig.push.branch`
  * `trigger.repositoryEventConfig.push.invertRegex`
  * `trigger.repositoryEventConfig.push.tag`
  * `trigger.repositoryEventConfig.repository`
  * `trigger.serviceAccount`
  * `trigger.sourceToBuild.bitbucketServerConfig`
  * `trigger.sourceToBuild.githubEnterpriseConfig`
  * `trigger.sourceToBuild.ref`
  * `trigger.sourceToBuild.repoType`
  * `trigger.sourceToBuild.repository`
  * `trigger.sourceToBuild.uri`
  * `trigger.substitutions.key`
  * `trigger.substitutions.value`
  * `trigger.tags`
  * `trigger.triggerTemplate.branchName`
  * `trigger.triggerTemplate.commitSha`
  * `trigger.triggerTemplate.dir`
  * `trigger.triggerTemplate.invertRegex`
  * `trigger.triggerTemplate.repoName`
  * `trigger.triggerTemplate.substitutions.key`
  * `trigger.triggerTemplate.substitutions.value`
  * `trigger.triggerTemplate.tagName`
  * `trigger.uri`
  * `trigger.webhookConfig.secret`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/projects/{project_id}/triggers/{trigger_id}:run` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.RunBuildTrigger`

| 

  * `source.branchName`
  * `source.commitSha`
  * `source.dir`
  * `source.invertRegex`
  * `source.projectId`
  * `source.repoName`
  * `source.substitutions.key`
  * `source.substitutions.value`
  * `source.tagName`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/triggers/*}:run` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.RunBuildTrigger`

| 

  * `source.branchName`
  * `source.commitSha`
  * `source.dir`
  * `source.invertRegex`
  * `source.projectId`
  * `source.repoName`
  * `source.substitutions.key`
  * `source.substitutions.value`
  * `source.tagName`

  
Service: `cloudbuild.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/triggers` RPC methods:

  * `google.devtools.cloudbuild.v1.CloudBuild.CreateBuildTrigger`

| 

  * `trigger.baseImage.imageName`
  * `trigger.bitbucketServerTriggerConfig.pullRequest.branch`
  * `trigger.bitbucketServerTriggerConfig.push.branch`
  * `trigger.bitbucketServerTriggerConfig.push.tag`
  * `trigger.build.artifacts.genericArtifacts.contentHandling`
  * `trigger.build.artifacts.genericArtifacts.folder`
  * `trigger.build.artifacts.genericArtifacts.registryPath`
  * `trigger.build.artifacts.goModules.modulePath`
  * `trigger.build.artifacts.goModules.moduleVersion`
  * `trigger.build.artifacts.goModules.sourcePath`
  * `trigger.build.artifacts.images`
  * `trigger.build.artifacts.mavenArtifacts.artifactId`
  * `trigger.build.artifacts.mavenArtifacts.deployFolder`
  * `trigger.build.artifacts.mavenArtifacts.groupId`
  * `trigger.build.artifacts.mavenArtifacts.path`
  * `trigger.build.artifacts.mavenArtifacts.pomPath`
  * `trigger.build.artifacts.mavenArtifacts.version`
  * `trigger.build.artifacts.npmPackages.archive`
  * `trigger.build.artifacts.npmPackages.packagePath`
  * `trigger.build.artifacts.npmPackages.repository`
  * `trigger.build.artifacts.objects.location`
  * `trigger.build.artifacts.objects.paths`
  * `trigger.build.artifacts.oci.file`
  * `trigger.build.artifacts.oci.registryPath`
  * `trigger.build.artifacts.oci.tags`
  * `trigger.build.artifacts.pythonPackages.paths`
  * `trigger.build.artifacts.testResults.bucketUri`
  * `trigger.build.artifacts.testResults.format`
  * `trigger.build.artifacts.testResults.paths`
  * `trigger.build.artifacts.volumes.name`
  * `trigger.build.artifacts.volumes.path`
  * `trigger.build.availableSecrets.inline.envMap.key`
  * `trigger.build.availableSecrets.inline.envMap.value`
  * `trigger.build.availableSecrets.inline.kmsKeyName`
  * `trigger.build.availableSecrets.secretManager.env`
  * `trigger.build.availableSecrets.secretManager.versionName`
  * `trigger.build.buildReceipt.workerDiagnostics.identityEndpointSuccesses`
  * `trigger.build.dependencies.empty`
  * `trigger.build.dependencies.genericArtifact.destPath`
  * `trigger.build.dependencies.genericArtifact.resource`
  * `trigger.build.dependencies.gitSource.depth`
  * `trigger.build.dependencies.gitSource.destPath`
  * `trigger.build.dependencies.gitSource.recurseSubmodules`
  * `trigger.build.dependencies.gitSource.repository.developerConnect`
  * `trigger.build.dependencies.gitSource.repository.proxyUrlEnabled`
  * `trigger.build.dependencies.gitSource.repository.url`
  * `trigger.build.dependencies.gitSource.revision`
  * `trigger.build.gitConfig.http.proxySecretVersionName`
  * `trigger.build.gitConfig.http.sslCaInfo`
  * `trigger.build.images`
  * `trigger.build.logsBucket`
  * `trigger.build.options.env`
  * `trigger.build.options.secretEnv`
  * `trigger.build.options.volumes.name`
  * `trigger.build.options.volumes.path`
  * `trigger.build.secrets.kmsKeyName`
  * `trigger.build.secrets.secretEnv.key`
  * `trigger.build.secrets.secretEnv.value`
  * `trigger.build.serviceAccount`
  * `trigger.build.source.buildConfigFileName`
  * `trigger.build.source.connectedRepository.dir`
  * `trigger.build.source.connectedRepository.repository`
  * `trigger.build.source.connectedRepository.revision`
  * `trigger.build.source.developerConnectConfig.dir`
  * `trigger.build.source.developerConnectConfig.gitRepositoryLink`
  * `trigger.build.source.developerConnectConfig.revision`
  * `trigger.build.source.gitSource.commitSha`
  * `trigger.build.source.gitSource.dir`
  * `trigger.build.source.gitSource.revision`
  * `trigger.build.source.gitSource.url`
  * `trigger.build.source.repoSource.branchName`
  * `trigger.build.source.repoSource.commitSha`
  * `trigger.build.source.repoSource.dir`
  * `trigger.build.source.repoSource.invertRegex`
  * `trigger.build.source.repoSource.projectId`
  * `trigger.build.source.repoSource.repoName`
  * `trigger.build.source.repoSource.substitutions.key`
  * `trigger.build.source.repoSource.substitutions.value`
  * `trigger.build.source.repoSource.tagName`
  * `trigger.build.source.storageSource.bucket`
  * `trigger.build.source.storageSource.generation`
  * `trigger.build.source.storageSource.object`
  * `trigger.build.source.storageSource.sourceFetcher`
  * `trigger.build.source.storageSource.stripComponents`
  * `trigger.build.source.storageSourceManifest.bucket`
  * `trigger.build.source.storageSourceManifest.generation`
  * `trigger.build.source.storageSourceManifest.object`
  * `trigger.build.steps.args`
  * `trigger.build.steps.dir`
  * `trigger.build.steps.entrypoint`
  * `trigger.build.steps.env`
  * `trigger.build.steps.id`
  * `trigger.build.steps.name`
  * `trigger.build.steps.remoteConfig`
  * `trigger.build.steps.results.attestationContent`
  * `trigger.build.steps.results.attestationType`
  * `trigger.build.steps.results.name`
  * `trigger.build.steps.script`
  * `trigger.build.steps.secretEnv`
  * `trigger.build.steps.volumes.name`
  * `trigger.build.steps.volumes.path`
  * `trigger.build.steps.waitFor`
  * `trigger.build.substitutions.key`
  * `trigger.build.substitutions.value`
  * `trigger.build.tags`
  * `trigger.cloudCode.codeReview.branch`
  * `trigger.cloudCode.project`
  * `trigger.cloudCode.repo`
  * `trigger.description`
  * `trigger.developerConnectEventConfig.gitRepositoryLink`
  * `trigger.developerConnectEventConfig.pullRequest.branch`
  * `trigger.developerConnectEventConfig.pullRequest.commentControl`
  * `trigger.developerConnectEventConfig.pullRequest.invertRegex`
  * `trigger.developerConnectEventConfig.push.branch`
  * `trigger.developerConnectEventConfig.push.invertRegex`
  * `trigger.developerConnectEventConfig.push.tag`
  * `trigger.dir`
  * `trigger.eventType`
  * `trigger.filename`
  * `trigger.gitFileSource.bitbucketServerConfig`
  * `trigger.gitFileSource.githubEnterpriseConfig`
  * `trigger.gitFileSource.path`
  * `trigger.gitFileSource.repoType`
  * `trigger.gitFileSource.repository`
  * `trigger.gitFileSource.revision`
  * `trigger.gitFileSource.uri`
  * `trigger.github.pullRequest.branch`
  * `trigger.github.push.branch`
  * `trigger.github.push.tag`
  * `trigger.gitlabEnterpriseEventsConfig.pullRequest.branch`
  * `trigger.gitlabEnterpriseEventsConfig.push.branch`
  * `trigger.gitlabEnterpriseEventsConfig.push.tag`
  * `trigger.gitlabEventsConfig.pullRequest.branch`
  * `trigger.gitlabEventsConfig.push.branch`
  * `trigger.gitlabEventsConfig.push.tag`
  * `trigger.ignoredFiles`
  * `trigger.includeBuildLogs`
  * `trigger.includedFiles`
  * `trigger.internalAnnotations.tags`
  * `trigger.name`
  * `trigger.repositoryEventConfig.pullRequest.branch`
  * `trigger.repositoryEventConfig.pullRequest.commentControl`
  * `trigger.repositoryEventConfig.pullRequest.invertRegex`
  * `trigger.repositoryEventConfig.push.branch`
  * `trigger.repositoryEventConfig.push.invertRegex`
  * `trigger.repositoryEventConfig.push.tag`
  * `trigger.repositoryEventConfig.repository`
  * `trigger.serviceAccount`
  * `trigger.sourceToBuild.bitbucketServerConfig`
  * `trigger.sourceToBuild.githubEnterpriseConfig`
  * `trigger.sourceToBuild.ref`
  * `trigger.sourceToBuild.repoType`
  * `trigger.sourceToBuild.repository`
  * `trigger.sourceToBuild.uri`
  * `trigger.substitutions.key`
  * `trigger.substitutions.value`
  * `trigger.tags`
  * `trigger.triggerTemplate.branchName`
  * `trigger.triggerTemplate.commitSha`
  * `trigger.triggerTemplate.dir`
  * `trigger.triggerTemplate.invertRegex`
  * `trigger.triggerTemplate.repoName`
  * `trigger.triggerTemplate.substitutions.key`
  * `trigger.triggerTemplate.substitutions.value`
  * `trigger.triggerTemplate.tagName`
  * `trigger.uri`
  * `trigger.webhookConfig.secret`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Authentication | 

  * `authUser`
  * `userOauthCode`

  
Build/Trigger specifics | 

  * `build.buildReceipt.buildConfigSubstitutions.value`
  * `build.buildReceipt.queue`
  * `build.options.pool.name`
  * `build.source.gitSource.gitCredential.password`
  * `build.source.gitSource.gitCredential.username`
  * `triggerId`

  
Configuration | 

  * `appConfigJson.bucket`
  * `appConfigJson.object`
  * `code`
  * `eventSource`
  * `hostUrl`
  * `peeredNetwork`

  
Connection specifics | 

  * `connection.bitbucketCloudConfig.authorizerCredential.userTokenSecretVersion`
  * `connection.bitbucketCloudConfig.readAuthorizerCredential.userTokenSecretVersion`
  * `connection.bitbucketCloudConfig.webhookSecretSecretVersion`
  * `connection.githubEnterpriseConfig.oauthClientIdSecretVersion`
  * `connection.githubEnterpriseConfig.oauthSecretSecretVersion`
  * `connection.gitlabConfig.readAuthorizerCredential.userTokenSecretVersion`

  
Network configuration |  N/A   
Repository/Project details | 

  * `installation.repositorySettingList.repositorySettings.name`
  * `installation.repositorySettingList.repositorySettings.owner`
  * `owner`

  
Resource identification | 

  * `enterpriseConfigResourceName`
  * `id`
  * `name`
  * `parent`
  * `projectId`
  * `repo`

  
Secret management | 

  * `sslCa`
  * `webhookKey`

  
Service/API access | 

  * `connection.githubEnterpriseConfig.serviceDirectoryConfig.service`
  * `connection.gitlabConfig.serviceDirectoryConfig.service`
  * `gitlabConfig.secrets.apiAccessTokenVersion`
  * `gitlabConfig.secrets.apiKeyVersion`

  
State management | 

  * `etag`
  * `pageToken`
  * `state`
  * `updateMask.paths`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
