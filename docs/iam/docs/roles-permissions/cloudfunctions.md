---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions/
title: Cloud Run functions roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:31.251806+00:00
---

# Cloud Run functions roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Run functions roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Run functions. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Run functions roles

Role | Permissions  
---|---  
  
#### Cloud Functions Admin 

(`roles/cloudfunctions.admin`) Full access to functions, operations and locations.  This role applies to functions created using the Cloud Functions API. For functions created using Cloud Run, refer to the [Cloud Run roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/run) page.  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudfunctions.*`

  * `cloudfunctions.functions.call`
  * `cloudfunctions.functions.create`
  * `cloudfunctions.functions.delete`
  * `cloudfunctions.functions.generationUpgrade`
  * `cloudfunctions.functions.get`
  * `cloudfunctions.functions.getIamPolicy`
  * `cloudfunctions.functions.invoke`
  * `cloudfunctions.functions.list`
  * `cloudfunctions.functions.setIamPolicy`
  * `cloudfunctions.functions.sourceCodeGet`
  * `cloudfunctions.functions.sourceCodeSet`
  * `cloudfunctions.functions.update`
  * `cloudfunctions.locations.list`
  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`eventarc.*`

  * `eventarc.channelConnections.create`
  * `eventarc.channelConnections.createTagBinding`
  * `eventarc.channelConnections.delete`
  * `eventarc.channelConnections.deleteTagBinding`
  * `eventarc.channelConnections.get`
  * `eventarc.channelConnections.getIamPolicy`
  * `eventarc.channelConnections.list`
  * `eventarc.channelConnections.listEffectiveTags`
  * `eventarc.channelConnections.listTagBindings`
  * `eventarc.channelConnections.publish`
  * `eventarc.channelConnections.setIamPolicy`
  * `eventarc.channels.attach`
  * `eventarc.channels.create`
  * `eventarc.channels.createTagBinding`
  * `eventarc.channels.delete`
  * `eventarc.channels.deleteTagBinding`
  * `eventarc.channels.get`
  * `eventarc.channels.getIamPolicy`
  * `eventarc.channels.list`
  * `eventarc.channels.listEffectiveTags`
  * `eventarc.channels.listTagBindings`
  * `eventarc.channels.publish`
  * `eventarc.channels.setIamPolicy`
  * `eventarc.channels.undelete`
  * `eventarc.channels.update`
  * `eventarc.enrollments.create`
  * `eventarc.enrollments.delete`
  * `eventarc.enrollments.get`
  * `eventarc.enrollments.getIamPolicy`
  * `eventarc.enrollments.list`
  * `eventarc.enrollments.setIamPolicy`
  * `eventarc.enrollments.update`
  * `eventarc.events.receiveAuditLogWritten`
  * `eventarc.events.receiveEvent`
  * `eventarc.googleApiSources.create`
  * `eventarc.googleApiSources.delete`
  * `eventarc.googleApiSources.get`
  * `eventarc.googleApiSources.getIamPolicy`
  * `eventarc.googleApiSources.list`
  * `eventarc.googleApiSources.setIamPolicy`
  * `eventarc.googleApiSources.update`
  * `eventarc.googleChannelConfigs.get`
  * `eventarc.googleChannelConfigs.update`
  * `eventarc.kafkaSources.create`
  * `eventarc.kafkaSources.delete`
  * `eventarc.kafkaSources.get`
  * `eventarc.kafkaSources.getIamPolicy`
  * `eventarc.kafkaSources.list`
  * `eventarc.kafkaSources.setIamPolicy`
  * `eventarc.locations.get`
  * `eventarc.locations.list`
  * `eventarc.messageBuses.create`
  * `eventarc.messageBuses.delete`
  * `eventarc.messageBuses.get`
  * `eventarc.messageBuses.getIamPolicy`
  * `eventarc.messageBuses.list`
  * `eventarc.messageBuses.publish`
  * `eventarc.messageBuses.setIamPolicy`
  * `eventarc.messageBuses.update`
  * `eventarc.messageBuses.use`
  * `eventarc.multiProjectSources.collectGoogleApiEvents`
  * `eventarc.operations.cancel`
  * `eventarc.operations.delete`
  * `eventarc.operations.get`
  * `eventarc.operations.list`
  * `eventarc.pipelines.create`
  * `eventarc.pipelines.delete`
  * `eventarc.pipelines.get`
  * `eventarc.pipelines.getIamPolicy`
  * `eventarc.pipelines.list`
  * `eventarc.pipelines.setIamPolicy`
  * `eventarc.pipelines.update`
  * `eventarc.providers.get`
  * `eventarc.providers.list`
  * `eventarc.triggers.create`
  * `eventarc.triggers.createTagBinding`
  * `eventarc.triggers.delete`
  * `eventarc.triggers.deleteTagBinding`
  * `eventarc.triggers.get`
  * `eventarc.triggers.getIamPolicy`
  * `eventarc.triggers.list`
  * `eventarc.triggers.listEffectiveTags`
  * `eventarc.triggers.listTagBindings`
  * `eventarc.triggers.setIamPolicy`
  * `eventarc.triggers.undelete`
  * `eventarc.triggers.update`

`recommender.cloudFunctionsPerformanceInsights.*`

  * `recommender.cloudFunctionsPerformanceInsights.get`
  * `recommender.cloudFunctionsPerformanceInsights.list`
  * `recommender.cloudFunctionsPerformanceInsights.update`

`recommender.cloudFunctionsPerformanceRecommendations.*`

  * `recommender.cloudFunctionsPerformanceRecommendations.get`
  * `recommender.cloudFunctionsPerformanceRecommendations.list`
  * `recommender.cloudFunctionsPerformanceRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.*`

  * `recommender.runServiceCostInsights.get`
  * `recommender.runServiceCostInsights.list`
  * `recommender.runServiceCostInsights.update`

`recommender.runServiceCostRecommendations.*`

  * `recommender.runServiceCostRecommendations.get`
  * `recommender.runServiceCostRecommendations.list`
  * `recommender.runServiceCostRecommendations.update`

`recommender.runServiceIdentityInsights.*`

  * `recommender.runServiceIdentityInsights.get`
  * `recommender.runServiceIdentityInsights.list`
  * `recommender.runServiceIdentityInsights.update`

`recommender.runServiceIdentityRecommendations.*`

  * `recommender.runServiceIdentityRecommendations.get`
  * `recommender.runServiceIdentityRecommendations.list`
  * `recommender.runServiceIdentityRecommendations.update`

`recommender.runServicePerformanceInsights.*`

  * `recommender.runServicePerformanceInsights.get`
  * `recommender.runServicePerformanceInsights.list`
  * `recommender.runServicePerformanceInsights.update`

`recommender.runServicePerformanceRecommendations.*`

  * `recommender.runServicePerformanceRecommendations.get`
  * `recommender.runServicePerformanceRecommendations.list`
  * `recommender.runServicePerformanceRecommendations.update`

`recommender.runServiceSecurityInsights.*`

  * `recommender.runServiceSecurityInsights.get`
  * `recommender.runServiceSecurityInsights.list`
  * `recommender.runServiceSecurityInsights.update`

`recommender.runServiceSecurityRecommendations.*`

  * `recommender.runServiceSecurityRecommendations.get`
  * `recommender.runServiceSecurityRecommendations.list`
  * `recommender.runServiceSecurityRecommendations.update`

`remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `run.*`

  * `run.configurations.get`
  * `run.configurations.list`
  * `run.executions.cancel`
  * `run.executions.delete`
  * `run.executions.get`
  * `run.executions.list`
  * `run.instances.create`
  * `run.instances.delete`
  * `run.instances.get`
  * `run.instances.getIamPolicy`
  * `run.instances.invoke`
  * `run.instances.list`
  * `run.instances.setIamPolicy`
  * `run.instances.sshRead`
  * `run.instances.sshRoot`
  * `run.instances.start`
  * `run.instances.stop`
  * `run.instances.update`
  * `run.jobs.create`
  * `run.jobs.createTagBinding`
  * `run.jobs.delete`
  * `run.jobs.deleteTagBinding`
  * `run.jobs.get`
  * `run.jobs.getIamPolicy`
  * `run.jobs.list`
  * `run.jobs.listEffectiveTags`
  * `run.jobs.listTagBindings`
  * `run.jobs.run`
  * `run.jobs.runWithOverrides`
  * `run.jobs.setIamPolicy`
  * `run.jobs.sshRead`
  * `run.jobs.sshRoot`
  * `run.jobs.update`
  * `run.locations.list`
  * `run.locations.uploadSource`
  * `run.operations.delete`
  * `run.operations.get`
  * `run.operations.list`
  * `run.prompts.get`
  * `run.revisions.delete`
  * `run.revisions.get`
  * `run.revisions.list`
  * `run.routes.get`
  * `run.routes.invoke`
  * `run.routes.list`
  * `run.services.create`
  * `run.services.createTagBinding`
  * `run.services.delete`
  * `run.services.deleteTagBinding`
  * `run.services.get`
  * `run.services.getIamPolicy`
  * `run.services.list`
  * `run.services.listEffectiveTags`
  * `run.services.listTagBindings`
  * `run.services.setIamPolicy`
  * `run.services.sshRead`
  * `run.services.sshRoot`
  * `run.services.update`
  * `run.tasks.get`
  * `run.tasks.list`
  * `run.workerpools.create`
  * `run.workerpools.delete`
  * `run.workerpools.get`
  * `run.workerpools.getIamPolicy`
  * `run.workerpools.list`
  * `run.workerpools.setIamPolicy`
  * `run.workerpools.sshRead`
  * `run.workerpools.sshRoot`
  * `run.workerpools.update`

`serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Cloud Functions Editor 

(`roles/cloudfunctions.editor`) Editor role for Cloud Functions  This role applies to functions created using the Cloud Functions API. For functions created using Cloud Run, refer to the [Cloud Run roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/run) page.  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudfunctions.functions.call` `cloudfunctions.functions.create` `cloudfunctions.functions.delete` `cloudfunctions.functions.generationUpgrade` `cloudfunctions.functions.get` `cloudfunctions.functions.getIamPolicy` `cloudfunctions.functions.invoke` `cloudfunctions.functions.list` `cloudfunctions.functions.sourceCodeGet` `cloudfunctions.functions.sourceCodeSet` `cloudfunctions.functions.update` `cloudfunctions.locations.list` `cloudfunctions.operations.*`

  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`eventarc.channelConnections.create` `eventarc.channelConnections.delete` `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channelConnections.publish` `eventarc.channels.attach` `eventarc.channels.create` `eventarc.channels.delete` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.channels.publish` `eventarc.channels.undelete` `eventarc.channels.update` `eventarc.enrollments.create` `eventarc.enrollments.delete` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.enrollments.update` `eventarc.googleApiSources.create` `eventarc.googleApiSources.delete` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleApiSources.update` `eventarc.googleChannelConfigs.*`

  * `eventarc.googleChannelConfigs.get`
  * `eventarc.googleChannelConfigs.update`

`eventarc.kafkaSources.create` `eventarc.kafkaSources.delete` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.messageBuses.get` `eventarc.messageBuses.getIamPolicy` `eventarc.messageBuses.list` `eventarc.messageBuses.use` `eventarc.multiProjectSources.collectGoogleApiEvents` `eventarc.operations.*`

  * `eventarc.operations.cancel`
  * `eventarc.operations.delete`
  * `eventarc.operations.get`
  * `eventarc.operations.list`

`eventarc.pipelines.create` `eventarc.pipelines.delete` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.pipelines.update` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.create` `eventarc.triggers.delete` `eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `eventarc.triggers.undelete` `eventarc.triggers.update` `recommender.cloudFunctionsPerformanceInsights.*`

  * `recommender.cloudFunctionsPerformanceInsights.get`
  * `recommender.cloudFunctionsPerformanceInsights.list`
  * `recommender.cloudFunctionsPerformanceInsights.update`

`recommender.cloudFunctionsPerformanceRecommendations.*`

  * `recommender.cloudFunctionsPerformanceRecommendations.get`
  * `recommender.cloudFunctionsPerformanceRecommendations.list`
  * `recommender.cloudFunctionsPerformanceRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.*`

  * `recommender.runServiceCostInsights.get`
  * `recommender.runServiceCostInsights.list`
  * `recommender.runServiceCostInsights.update`

`recommender.runServiceCostRecommendations.*`

  * `recommender.runServiceCostRecommendations.get`
  * `recommender.runServiceCostRecommendations.list`
  * `recommender.runServiceCostRecommendations.update`

`recommender.runServiceIdentityInsights.*`

  * `recommender.runServiceIdentityInsights.get`
  * `recommender.runServiceIdentityInsights.list`
  * `recommender.runServiceIdentityInsights.update`

`recommender.runServiceIdentityRecommendations.*`

  * `recommender.runServiceIdentityRecommendations.get`
  * `recommender.runServiceIdentityRecommendations.list`
  * `recommender.runServiceIdentityRecommendations.update`

`recommender.runServicePerformanceInsights.*`

  * `recommender.runServicePerformanceInsights.get`
  * `recommender.runServicePerformanceInsights.list`
  * `recommender.runServicePerformanceInsights.update`

`recommender.runServicePerformanceRecommendations.*`

  * `recommender.runServicePerformanceRecommendations.get`
  * `recommender.runServicePerformanceRecommendations.list`
  * `recommender.runServicePerformanceRecommendations.update`

`recommender.runServiceSecurityInsights.*`

  * `recommender.runServiceSecurityInsights.get`
  * `recommender.runServiceSecurityInsights.list`
  * `recommender.runServiceSecurityInsights.update`

`recommender.runServiceSecurityRecommendations.*`

  * `recommender.runServiceSecurityRecommendations.get`
  * `recommender.runServiceSecurityRecommendations.list`
  * `recommender.runServiceSecurityRecommendations.update`

`remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `run.configurations.*`

  * `run.configurations.get`
  * `run.configurations.list`

`run.executions.*`

  * `run.executions.cancel`
  * `run.executions.delete`
  * `run.executions.get`
  * `run.executions.list`

`run.instances.create` `run.instances.delete` `run.instances.get` `run.instances.getIamPolicy` `run.instances.invoke` `run.instances.list` `run.instances.sshRead` `run.instances.sshRoot` `run.instances.start` `run.instances.stop` `run.instances.update` `run.jobs.create` `run.jobs.delete` `run.jobs.get` `run.jobs.getIamPolicy` `run.jobs.list` `run.jobs.listEffectiveTags` `run.jobs.listTagBindings` `run.jobs.run` `run.jobs.runWithOverrides` `run.jobs.sshRead` `run.jobs.sshRoot` `run.jobs.update` `run.locations.*`

  * `run.locations.list`
  * `run.locations.uploadSource`

`run.operations.*`

  * `run.operations.delete`
  * `run.operations.get`
  * `run.operations.list`

`run.prompts.get` `run.revisions.*`

  * `run.revisions.delete`
  * `run.revisions.get`
  * `run.revisions.list`

`run.routes.*`

  * `run.routes.get`
  * `run.routes.invoke`
  * `run.routes.list`

`run.services.create` `run.services.delete` `run.services.get` `run.services.getIamPolicy` `run.services.list` `run.services.listEffectiveTags` `run.services.listTagBindings` `run.services.sshRead` `run.services.sshRoot` `run.services.update` `run.tasks.*`

  * `run.tasks.get`
  * `run.tasks.list`

`run.workerpools.create` `run.workerpools.delete` `run.workerpools.get` `run.workerpools.getIamPolicy` `run.workerpools.list` `run.workerpools.sshRead` `run.workerpools.sshRoot` `run.workerpools.update` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Cloud Functions Invoker 

(`roles/cloudfunctions.invoker`) Ability to invoke 1st gen HTTP functions with restricted access. 2nd gen functions need the Cloud Run Invoker role instead.  This role applies to functions created using the Cloud Functions API. For functions created using Cloud Run, refer to the [Cloud Run roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/run) page.  |  `cloudfunctions.functions.invoke`  
  
#### Cloud Functions Viewer 

(`roles/cloudfunctions.viewer`) Read-only access to functions and locations.  This role applies to functions created using the Cloud Functions API. For functions created using Cloud Run, refer to the [Cloud Run roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/run) page.  |  `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudfunctions.functions.get` `cloudfunctions.functions.getIamPolicy` `cloudfunctions.functions.list` `cloudfunctions.locations.list` `cloudfunctions.operations.*`

  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleChannelConfigs.get` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.messageBuses.get` `eventarc.messageBuses.getIamPolicy` `eventarc.messageBuses.list` `eventarc.messageBuses.use` `eventarc.multiProjectSources.collectGoogleApiEvents` `eventarc.operations.get` `eventarc.operations.list` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `recommender.cloudFunctionsPerformanceInsights.get` `recommender.cloudFunctionsPerformanceInsights.list` `recommender.cloudFunctionsPerformanceRecommendations.get` `recommender.cloudFunctionsPerformanceRecommendations.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.get` `recommender.runServiceCostInsights.list` `recommender.runServiceCostRecommendations.get` `recommender.runServiceCostRecommendations.list` `recommender.runServiceIdentityInsights.get` `recommender.runServiceIdentityInsights.list` `recommender.runServiceIdentityRecommendations.get` `recommender.runServiceIdentityRecommendations.list` `recommender.runServicePerformanceInsights.get` `recommender.runServicePerformanceInsights.list` `recommender.runServicePerformanceRecommendations.get` `recommender.runServicePerformanceRecommendations.list` `recommender.runServiceSecurityInsights.get` `recommender.runServiceSecurityInsights.list` `recommender.runServiceSecurityRecommendations.get` `recommender.runServiceSecurityRecommendations.list` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `run.configurations.*`

  * `run.configurations.get`
  * `run.configurations.list`

`run.executions.get` `run.executions.list` `run.instances.get` `run.instances.getIamPolicy` `run.instances.list` `run.jobs.get` `run.jobs.getIamPolicy` `run.jobs.list` `run.jobs.listEffectiveTags` `run.jobs.listTagBindings` `run.locations.list` `run.operations.get` `run.operations.list` `run.prompts.get` `run.revisions.get` `run.revisions.list` `run.routes.get` `run.routes.list` `run.services.get` `run.services.getIamPolicy` `run.services.list` `run.services.listEffectiveTags` `run.services.listTagBindings` `run.tasks.*`

  * `run.tasks.get`
  * `run.tasks.list`

`run.workerpools.get` `run.workerpools.getIamPolicy` `run.workerpools.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Cloud Functions Developer 

(`roles/cloudfunctions.developer`) Read and write access to all functions-related resources.  This role applies to functions created using the Cloud Functions API. For functions created using Cloud Run, refer to the [Cloud Run roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/run) page.  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudfunctions.functions.call` `cloudfunctions.functions.create` `cloudfunctions.functions.delete` `cloudfunctions.functions.generationUpgrade` `cloudfunctions.functions.get` `cloudfunctions.functions.invoke` `cloudfunctions.functions.list` `cloudfunctions.functions.sourceCodeGet` `cloudfunctions.functions.sourceCodeSet` `cloudfunctions.functions.update` `cloudfunctions.locations.list` `cloudfunctions.operations.*`

  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`eventarc.channelConnections.create` `eventarc.channelConnections.createTagBinding` `eventarc.channelConnections.delete` `eventarc.channelConnections.deleteTagBinding` `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channelConnections.publish` `eventarc.channels.attach` `eventarc.channels.create` `eventarc.channels.createTagBinding` `eventarc.channels.delete` `eventarc.channels.deleteTagBinding` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.channels.publish` `eventarc.channels.undelete` `eventarc.channels.update` `eventarc.enrollments.create` `eventarc.enrollments.delete` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.enrollments.update` `eventarc.googleApiSources.create` `eventarc.googleApiSources.delete` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleApiSources.update` `eventarc.googleChannelConfigs.*`

  * `eventarc.googleChannelConfigs.get`
  * `eventarc.googleChannelConfigs.update`

`eventarc.kafkaSources.create` `eventarc.kafkaSources.delete` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.operations.*`

  * `eventarc.operations.cancel`
  * `eventarc.operations.delete`
  * `eventarc.operations.get`
  * `eventarc.operations.list`

`eventarc.pipelines.create` `eventarc.pipelines.delete` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.pipelines.update` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.create` `eventarc.triggers.createTagBinding` `eventarc.triggers.delete` `eventarc.triggers.deleteTagBinding` `eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `eventarc.triggers.undelete` `eventarc.triggers.update` `recommender.cloudFunctionsPerformanceInsights.*`

  * `recommender.cloudFunctionsPerformanceInsights.get`
  * `recommender.cloudFunctionsPerformanceInsights.list`
  * `recommender.cloudFunctionsPerformanceInsights.update`

`recommender.cloudFunctionsPerformanceRecommendations.*`

  * `recommender.cloudFunctionsPerformanceRecommendations.get`
  * `recommender.cloudFunctionsPerformanceRecommendations.list`
  * `recommender.cloudFunctionsPerformanceRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.*`

  * `recommender.runServiceCostInsights.get`
  * `recommender.runServiceCostInsights.list`
  * `recommender.runServiceCostInsights.update`

`recommender.runServiceCostRecommendations.*`

  * `recommender.runServiceCostRecommendations.get`
  * `recommender.runServiceCostRecommendations.list`
  * `recommender.runServiceCostRecommendations.update`

`recommender.runServiceIdentityInsights.*`

  * `recommender.runServiceIdentityInsights.get`
  * `recommender.runServiceIdentityInsights.list`
  * `recommender.runServiceIdentityInsights.update`

`recommender.runServiceIdentityRecommendations.*`

  * `recommender.runServiceIdentityRecommendations.get`
  * `recommender.runServiceIdentityRecommendations.list`
  * `recommender.runServiceIdentityRecommendations.update`

`recommender.runServicePerformanceInsights.*`

  * `recommender.runServicePerformanceInsights.get`
  * `recommender.runServicePerformanceInsights.list`
  * `recommender.runServicePerformanceInsights.update`

`recommender.runServicePerformanceRecommendations.*`

  * `recommender.runServicePerformanceRecommendations.get`
  * `recommender.runServicePerformanceRecommendations.list`
  * `recommender.runServicePerformanceRecommendations.update`

`recommender.runServiceSecurityInsights.*`

  * `recommender.runServiceSecurityInsights.get`
  * `recommender.runServiceSecurityInsights.list`
  * `recommender.runServiceSecurityInsights.update`

`recommender.runServiceSecurityRecommendations.*`

  * `recommender.runServiceSecurityRecommendations.get`
  * `recommender.runServiceSecurityRecommendations.list`
  * `recommender.runServiceSecurityRecommendations.update`

`remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `run.configurations.*`

  * `run.configurations.get`
  * `run.configurations.list`

`run.executions.*`

  * `run.executions.cancel`
  * `run.executions.delete`
  * `run.executions.get`
  * `run.executions.list`

`run.instances.create` `run.instances.delete` `run.instances.get` `run.instances.getIamPolicy` `run.instances.invoke` `run.instances.list` `run.instances.sshRead` `run.instances.sshRoot` `run.instances.start` `run.instances.stop` `run.instances.update` `run.jobs.create` `run.jobs.delete` `run.jobs.get` `run.jobs.getIamPolicy` `run.jobs.list` `run.jobs.listEffectiveTags` `run.jobs.listTagBindings` `run.jobs.run` `run.jobs.runWithOverrides` `run.jobs.sshRead` `run.jobs.sshRoot` `run.jobs.update` `run.locations.*`

  * `run.locations.list`
  * `run.locations.uploadSource`

`run.operations.*`

  * `run.operations.delete`
  * `run.operations.get`
  * `run.operations.list`

`run.prompts.get` `run.revisions.*`

  * `run.revisions.delete`
  * `run.revisions.get`
  * `run.revisions.list`

`run.routes.*`

  * `run.routes.get`
  * `run.routes.invoke`
  * `run.routes.list`

`run.services.create` `run.services.delete` `run.services.get` `run.services.getIamPolicy` `run.services.list` `run.services.listEffectiveTags` `run.services.listTagBindings` `run.services.sshRead` `run.services.sshRoot` `run.services.update` `run.tasks.*`

  * `run.tasks.get`
  * `run.tasks.list`

`run.workerpools.create` `run.workerpools.delete` `run.workerpools.get` `run.workerpools.getIamPolicy` `run.workerpools.list` `run.workerpools.sshRead` `run.workerpools.sshRoot` `run.workerpools.update` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### (Deprecated) Cloud Functions Service Agent 

(`roles/cloudfunctions.serviceAgent`) Gives Cloud Functions service account access to managed resources.  This role applies to functions created using the Cloud Functions API. For functions created using Cloud Run, refer to the [Cloud Run roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/run) page.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.*`

  * `artifactregistry.aptartifacts.create`
  * `artifactregistry.attachments.create`
  * `artifactregistry.attachments.delete`
  * `artifactregistry.attachments.get`
  * `artifactregistry.attachments.list`
  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`
  * `artifactregistry.files.delete`
  * `artifactregistry.files.download`
  * `artifactregistry.files.get`
  * `artifactregistry.files.list`
  * `artifactregistry.files.update`
  * `artifactregistry.files.upload`
  * `artifactregistry.kfpartifacts.create`
  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`
  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`
  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`
  * `artifactregistry.packages.delete`
  * `artifactregistry.packages.get`
  * `artifactregistry.packages.list`
  * `artifactregistry.packages.update`
  * `artifactregistry.projectconfigs.get`
  * `artifactregistry.projectconfigs.update`
  * `artifactregistry.projectsettings.get`
  * `artifactregistry.projectsettings.update`
  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`
  * `artifactregistry.repositories.create`
  * `artifactregistry.repositories.createOnPush`
  * `artifactregistry.repositories.createTagBinding`
  * `artifactregistry.repositories.delete`
  * `artifactregistry.repositories.deleteArtifacts`
  * `artifactregistry.repositories.deleteTagBinding`
  * `artifactregistry.repositories.downloadArtifacts`
  * `artifactregistry.repositories.exportArtifacts`
  * `artifactregistry.repositories.get`
  * `artifactregistry.repositories.getIamPolicy`
  * `artifactregistry.repositories.list`
  * `artifactregistry.repositories.listEffectiveTags`
  * `artifactregistry.repositories.listTagBindings`
  * `artifactregistry.repositories.readViaVirtualRepository`
  * `artifactregistry.repositories.setIamPolicy`
  * `artifactregistry.repositories.update`
  * `artifactregistry.repositories.uploadArtifacts`
  * `artifactregistry.rules.create`
  * `artifactregistry.rules.delete`
  * `artifactregistry.rules.get`
  * `artifactregistry.rules.list`
  * `artifactregistry.rules.update`
  * `artifactregistry.tags.create`
  * `artifactregistry.tags.delete`
  * `artifactregistry.tags.get`
  * `artifactregistry.tags.list`
  * `artifactregistry.tags.update`
  * `artifactregistry.versions.delete`
  * `artifactregistry.versions.get`
  * `artifactregistry.versions.list`
  * `artifactregistry.versions.update`
  * `artifactregistry.yumartifacts.create`

`clientauthconfig.clients.list` `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudbuild.workerpools.use` `cloudfunctions.functions.get` `cloudfunctions.functions.invoke` `cloudfunctions.functions.list` `cloudfunctions.operations.*`

  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`compute.globalOperations.get` `compute.networks.access` `eventarc.channelConnections.create` `eventarc.channelConnections.delete` `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channelConnections.publish` `eventarc.channels.attach` `eventarc.channels.create` `eventarc.channels.delete` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.channels.publish` `eventarc.channels.undelete` `eventarc.channels.update` `eventarc.enrollments.create` `eventarc.enrollments.delete` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.enrollments.update` `eventarc.googleApiSources.create` `eventarc.googleApiSources.delete` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleApiSources.update` `eventarc.googleChannelConfigs.*`

  * `eventarc.googleChannelConfigs.get`
  * `eventarc.googleChannelConfigs.update`

`eventarc.kafkaSources.create` `eventarc.kafkaSources.delete` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.operations.*`

  * `eventarc.operations.cancel`
  * `eventarc.operations.delete`
  * `eventarc.operations.get`
  * `eventarc.operations.list`

`eventarc.pipelines.create` `eventarc.pipelines.delete` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.pipelines.update` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.create` `eventarc.triggers.delete` `eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `eventarc.triggers.undelete` `eventarc.triggers.update` `firebasedatabase.instances.get` `firebasedatabase.instances.update` `iam.serviceAccounts.actAs` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.signBlob` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.getIamPolicy` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.setIamPolicy` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.get` `pubsub.topics.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.*`

  * `recommender.runServiceCostInsights.get`
  * `recommender.runServiceCostInsights.list`
  * `recommender.runServiceCostInsights.update`

`recommender.runServiceCostRecommendations.*`

  * `recommender.runServiceCostRecommendations.get`
  * `recommender.runServiceCostRecommendations.list`
  * `recommender.runServiceCostRecommendations.update`

`recommender.runServiceIdentityInsights.*`

  * `recommender.runServiceIdentityInsights.get`
  * `recommender.runServiceIdentityInsights.list`
  * `recommender.runServiceIdentityInsights.update`

`recommender.runServiceIdentityRecommendations.*`

  * `recommender.runServiceIdentityRecommendations.get`
  * `recommender.runServiceIdentityRecommendations.list`
  * `recommender.runServiceIdentityRecommendations.update`

`recommender.runServicePerformanceInsights.*`

  * `recommender.runServicePerformanceInsights.get`
  * `recommender.runServicePerformanceInsights.list`
  * `recommender.runServicePerformanceInsights.update`

`recommender.runServicePerformanceRecommendations.*`

  * `recommender.runServicePerformanceRecommendations.get`
  * `recommender.runServicePerformanceRecommendations.list`
  * `recommender.runServicePerformanceRecommendations.update`

`recommender.runServiceSecurityInsights.*`

  * `recommender.runServiceSecurityInsights.get`
  * `recommender.runServiceSecurityInsights.list`
  * `recommender.runServiceSecurityInsights.update`

`recommender.runServiceSecurityRecommendations.*`

  * `recommender.runServiceSecurityRecommendations.get`
  * `recommender.runServiceSecurityRecommendations.list`
  * `recommender.runServiceSecurityRecommendations.update`

`remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `run.configurations.*`

  * `run.configurations.get`
  * `run.configurations.list`

`run.executions.*`

  * `run.executions.cancel`
  * `run.executions.delete`
  * `run.executions.get`
  * `run.executions.list`

`run.instances.create` `run.instances.delete` `run.instances.get` `run.instances.getIamPolicy` `run.instances.invoke` `run.instances.list` `run.instances.sshRead` `run.instances.sshRoot` `run.instances.start` `run.instances.stop` `run.instances.update` `run.jobs.create` `run.jobs.delete` `run.jobs.get` `run.jobs.getIamPolicy` `run.jobs.list` `run.jobs.listEffectiveTags` `run.jobs.listTagBindings` `run.jobs.run` `run.jobs.runWithOverrides` `run.jobs.sshRead` `run.jobs.sshRoot` `run.jobs.update` `run.locations.*`

  * `run.locations.list`
  * `run.locations.uploadSource`

`run.operations.*`

  * `run.operations.delete`
  * `run.operations.get`
  * `run.operations.list`

`run.prompts.get` `run.revisions.*`

  * `run.revisions.delete`
  * `run.revisions.get`
  * `run.revisions.list`

`run.routes.*`

  * `run.routes.get`
  * `run.routes.invoke`
  * `run.routes.list`

`run.services.create` `run.services.delete` `run.services.get` `run.services.getIamPolicy` `run.services.list` `run.services.listEffectiveTags` `run.services.listTagBindings` `run.services.sshRead` `run.services.sshRoot` `run.services.update` `run.tasks.*`

  * `run.tasks.get`
  * `run.tasks.list`

`run.workerpools.create` `run.workerpools.delete` `run.workerpools.get` `run.workerpools.getIamPolicy` `run.workerpools.list` `run.workerpools.sshRead` `run.workerpools.sshRoot` `run.workerpools.update` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.disable` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `source.repos.get` `source.repos.list` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `vpcaccess.connectors.get`  
  
## Cloud Run functions permissions

Permission | Included in roles  
---|---  
  
#### `cloudfunctions.functions.call`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `cloudfunctions.functions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `cloudfunctions.functions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `cloudfunctions.functions.generationUpgrade`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudfunctions.functions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Wiz Serverless & Container Image Registry Scanner](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.serverlessImageRegistryScanner) (`roles/wiz.serverlessImageRegistryScanner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent) (`roles/monitoring.notificationServiceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `cloudfunctions.functions.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudfunctions.functions.invoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.invoker) (`roles/cloudfunctions.invoker`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Identity Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.serviceAgent) (`roles/identitytoolkit.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `cloudfunctions.functions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `cloudfunctions.functions.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudfunctions.functions.sourceCodeGet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  [Wiz Serverless & Container Image Registry Scanner](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.serverlessImageRegistryScanner) (`roles/wiz.serverlessImageRegistryScanner`)   
  
#### `cloudfunctions.functions.sourceCodeSet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudfunctions.functions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `cloudfunctions.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudfunctions.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 

  
  
#### `cloudfunctions.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
