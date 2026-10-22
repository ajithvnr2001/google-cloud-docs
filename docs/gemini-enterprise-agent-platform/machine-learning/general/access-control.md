---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control/
title: Agent Platform access control with IAM \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:43:20.953933+00:00
---

# Agent Platform access control with IAM  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Agent Platform access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to manage access to Gemini Enterprise Agent Platform resources. To manage access to Gemini Enterprise Agent Platform Workbench instances, see [Agent Platform Workbench instances access control](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/iam).

## Overview

Agent Platform uses IAM to manage access to resources. When you plan access control for your resources, consider the following:

  * You can manage access at the project level or resource level. Project-level access applies to all of the resources in that project. Access to a specific resource only applies to that resource. See Project-level versus resource-level access.

  * You grant access by assigning IAM roles to principals. Predefined roles are available to make it easier to set up access, but custom roles are recommended because you create them, so you can limit their access to only the permissions that are required. See IAM roles.




## IAM roles

There are different types of IAM roles that can be used in Agent Platform:

  * Custom roles let you choose a specific set of permissions, create your own role with those permissions, and grant the role to users in your organization.

  * Predefined roles let you grant a set of related permissions to your Agent Platform resources at the project level.

  * Basic roles (Owner, Editor, and Viewer) provide access control to your Agent Platform resources at the project level, and are common to all Google Cloud services.




To add, update, or remove these roles in your Agent Platform project, see the documentation on [granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Custom roles

Custom roles let you choose a specific set of permissions, create your own role with those permissions, and grant the role to users in your organization. For more information, see [Understanding IAM custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom).

### Use custom roles to grant least-privilege permissions

Predefined roles often contain more permissions than you need. You can create custom roles to grant your principals only the specific permissions that are required.

For example, you can create a custom role with the `aiplatform.endpoints.predict` permission, and then assign the role to a service account on an endpoint. This grants the service account the ability to call the endpoint for predictions, but not the ability of controlling the endpoint.

**Note:** When using custom roles, granting the `aiplatform.endpoints.deploy` permission might allow a user to export other deployed or deployable models from the project. If you want to grant the ability to deploy specific models but not others, we recommend using separate projects.

### Predefined roles for Agent Platform

Role | Permissions  
---|---  
  
#### Agent Platform Administrator 

(`roles/aiplatform.admin`) Grants full access to all resources in Agent Platform.  |  `aiplatform.agentAnomalyDetectionScopes.*`

  * `aiplatform.agentAnomalyDetectionScopes.create`
  * `aiplatform.agentAnomalyDetectionScopes.delete`
  * `aiplatform.agentAnomalyDetectionScopes.get`
  * `aiplatform.agentAnomalyDetectionScopes.list`

`aiplatform.agentExamples.*`

  * `aiplatform.agentExamples.create`
  * `aiplatform.agentExamples.delete`
  * `aiplatform.agentExamples.get`
  * `aiplatform.agentExamples.list`
  * `aiplatform.agentExamples.update`

`aiplatform.agents.create` `aiplatform.agents.delete` `aiplatform.agents.get` `aiplatform.agents.list` `aiplatform.agents.update` `aiplatform.analyzedInvocations.*`

  * `aiplatform.analyzedInvocations.get`
  * `aiplatform.analyzedInvocations.list`

`aiplatform.analyzedSessions.*`

  * `aiplatform.analyzedSessions.aggregate`
  * `aiplatform.analyzedSessions.get`
  * `aiplatform.analyzedSessions.list`

`aiplatform.annotationSpecs.*`

  * `aiplatform.annotationSpecs.create`
  * `aiplatform.annotationSpecs.delete`
  * `aiplatform.annotationSpecs.get`
  * `aiplatform.annotationSpecs.list`
  * `aiplatform.annotationSpecs.update`

`aiplatform.annotations.*`

  * `aiplatform.annotations.create`
  * `aiplatform.annotations.delete`
  * `aiplatform.annotations.get`
  * `aiplatform.annotations.list`
  * `aiplatform.annotations.update`

`aiplatform.apps.*`

  * `aiplatform.apps.create`
  * `aiplatform.apps.delete`
  * `aiplatform.apps.get`
  * `aiplatform.apps.list`
  * `aiplatform.apps.update`

`aiplatform.artifacts.*`

  * `aiplatform.artifacts.create`
  * `aiplatform.artifacts.delete`
  * `aiplatform.artifacts.get`
  * `aiplatform.artifacts.list`
  * `aiplatform.artifacts.update`

`aiplatform.batchPredictionJobs.*`

  * `aiplatform.batchPredictionJobs.cancel`
  * `aiplatform.batchPredictionJobs.create`
  * `aiplatform.batchPredictionJobs.delete`
  * `aiplatform.batchPredictionJobs.get`
  * `aiplatform.batchPredictionJobs.list`

`aiplatform.cacheConfigs.*`

  * `aiplatform.cacheConfigs.get`
  * `aiplatform.cacheConfigs.update`

`aiplatform.cachedContents.*`

  * `aiplatform.cachedContents.create`
  * `aiplatform.cachedContents.delete`
  * `aiplatform.cachedContents.get`
  * `aiplatform.cachedContents.list`
  * `aiplatform.cachedContents.update`

`aiplatform.consents.*`

  * `aiplatform.consents.get`
  * `aiplatform.consents.update`

`aiplatform.contexts.*`

  * `aiplatform.contexts.addContextArtifactsAndExecutions`
  * `aiplatform.contexts.addContextChildren`
  * `aiplatform.contexts.create`
  * `aiplatform.contexts.delete`
  * `aiplatform.contexts.get`
  * `aiplatform.contexts.list`
  * `aiplatform.contexts.queryContextLineageSubgraph`
  * `aiplatform.contexts.update`

`aiplatform.customJobs.*`

  * `aiplatform.customJobs.cancel`
  * `aiplatform.customJobs.create`
  * `aiplatform.customJobs.delete`
  * `aiplatform.customJobs.get`
  * `aiplatform.customJobs.list`

`aiplatform.dataItems.*`

  * `aiplatform.dataItems.create`
  * `aiplatform.dataItems.delete`
  * `aiplatform.dataItems.get`
  * `aiplatform.dataItems.list`
  * `aiplatform.dataItems.update`

`aiplatform.dataLabelingJobs.*`

  * `aiplatform.dataLabelingJobs.cancel`
  * `aiplatform.dataLabelingJobs.create`
  * `aiplatform.dataLabelingJobs.delete`
  * `aiplatform.dataLabelingJobs.get`
  * `aiplatform.dataLabelingJobs.list`

`aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.*`

  * `aiplatform.datasets.create`
  * `aiplatform.datasets.delete`
  * `aiplatform.datasets.export`
  * `aiplatform.datasets.get`
  * `aiplatform.datasets.import`
  * `aiplatform.datasets.list`
  * `aiplatform.datasets.update`

`aiplatform.deploymentResourcePools.*`

  * `aiplatform.deploymentResourcePools.create`
  * `aiplatform.deploymentResourcePools.delete`
  * `aiplatform.deploymentResourcePools.get`
  * `aiplatform.deploymentResourcePools.list`
  * `aiplatform.deploymentResourcePools.queryDeployedModels`
  * `aiplatform.deploymentResourcePools.update`

`aiplatform.edgeDeploymentJobs.*`

  * `aiplatform.edgeDeploymentJobs.create`
  * `aiplatform.edgeDeploymentJobs.delete`
  * `aiplatform.edgeDeploymentJobs.get`
  * `aiplatform.edgeDeploymentJobs.list`

`aiplatform.edgeDeviceDebugInfo.get` `aiplatform.edgeDevices.*`

  * `aiplatform.edgeDevices.create`
  * `aiplatform.edgeDevices.delete`
  * `aiplatform.edgeDevices.get`
  * `aiplatform.edgeDevices.list`
  * `aiplatform.edgeDevices.update`

`aiplatform.endpoints.*`

  * `aiplatform.endpoints.create`
  * `aiplatform.endpoints.delete`
  * `aiplatform.endpoints.deploy`
  * `aiplatform.endpoints.explain`
  * `aiplatform.endpoints.get`
  * `aiplatform.endpoints.getIamPolicy`
  * `aiplatform.endpoints.list`
  * `aiplatform.endpoints.predict`
  * `aiplatform.endpoints.setIamPolicy`
  * `aiplatform.endpoints.undeploy`
  * `aiplatform.endpoints.update`

`aiplatform.entityTypes.*`

  * `aiplatform.entityTypes.create`
  * `aiplatform.entityTypes.delete`
  * `aiplatform.entityTypes.deleteFeatureValues`
  * `aiplatform.entityTypes.exportFeatureValues`
  * `aiplatform.entityTypes.get`
  * `aiplatform.entityTypes.getIamPolicy`
  * `aiplatform.entityTypes.importFeatureValues`
  * `aiplatform.entityTypes.list`
  * `aiplatform.entityTypes.readFeatureValues`
  * `aiplatform.entityTypes.setIamPolicy`
  * `aiplatform.entityTypes.streamingReadFeatureValues`
  * `aiplatform.entityTypes.update`
  * `aiplatform.entityTypes.writeFeatureValues`

`aiplatform.evaluationExperiments.*`

  * `aiplatform.evaluationExperiments.create`
  * `aiplatform.evaluationExperiments.delete`
  * `aiplatform.evaluationExperiments.get`
  * `aiplatform.evaluationExperiments.list`
  * `aiplatform.evaluationExperiments.update`

`aiplatform.evaluationItems.*`

  * `aiplatform.evaluationItems.create`
  * `aiplatform.evaluationItems.delete`
  * `aiplatform.evaluationItems.get`
  * `aiplatform.evaluationItems.list`
  * `aiplatform.evaluationItems.update`

`aiplatform.evaluationMetrics.*`

  * `aiplatform.evaluationMetrics.create`
  * `aiplatform.evaluationMetrics.delete`
  * `aiplatform.evaluationMetrics.get`
  * `aiplatform.evaluationMetrics.list`

`aiplatform.evaluationRuns.*`

  * `aiplatform.evaluationRuns.cancel`
  * `aiplatform.evaluationRuns.create`
  * `aiplatform.evaluationRuns.delete`
  * `aiplatform.evaluationRuns.execute`
  * `aiplatform.evaluationRuns.get`
  * `aiplatform.evaluationRuns.list`
  * `aiplatform.evaluationRuns.update`

`aiplatform.evaluationSets.*`

  * `aiplatform.evaluationSets.create`
  * `aiplatform.evaluationSets.delete`
  * `aiplatform.evaluationSets.get`
  * `aiplatform.evaluationSets.import`
  * `aiplatform.evaluationSets.list`
  * `aiplatform.evaluationSets.update`

`aiplatform.exampleStores.*`

  * `aiplatform.exampleStores.create`
  * `aiplatform.exampleStores.delete`
  * `aiplatform.exampleStores.get`
  * `aiplatform.exampleStores.list`
  * `aiplatform.exampleStores.readExample`
  * `aiplatform.exampleStores.update`
  * `aiplatform.exampleStores.writeExample`

`aiplatform.executions.*`

  * `aiplatform.executions.addExecutionEvents`
  * `aiplatform.executions.create`
  * `aiplatform.executions.delete`
  * `aiplatform.executions.get`
  * `aiplatform.executions.list`
  * `aiplatform.executions.queryExecutionInputsAndOutputs`
  * `aiplatform.executions.update`

`aiplatform.extensions.*`

  * `aiplatform.extensions.delete`
  * `aiplatform.extensions.execute`
  * `aiplatform.extensions.get`
  * `aiplatform.extensions.import`
  * `aiplatform.extensions.list`
  * `aiplatform.extensions.update`

`aiplatform.featureGroups.*`

  * `aiplatform.featureGroups.create`
  * `aiplatform.featureGroups.delete`
  * `aiplatform.featureGroups.get`
  * `aiplatform.featureGroups.getIamPolicy`
  * `aiplatform.featureGroups.list`
  * `aiplatform.featureGroups.setIamPolicy`
  * `aiplatform.featureGroups.update`

`aiplatform.featureMonitorJobs.*`

  * `aiplatform.featureMonitorJobs.create`
  * `aiplatform.featureMonitorJobs.get`
  * `aiplatform.featureMonitorJobs.list`

`aiplatform.featureMonitors.*`

  * `aiplatform.featureMonitors.create`
  * `aiplatform.featureMonitors.delete`
  * `aiplatform.featureMonitors.get`
  * `aiplatform.featureMonitors.list`
  * `aiplatform.featureMonitors.update`

`aiplatform.featureOnlineStores.*`

  * `aiplatform.featureOnlineStores.create`
  * `aiplatform.featureOnlineStores.delete`
  * `aiplatform.featureOnlineStores.get`
  * `aiplatform.featureOnlineStores.getIamPolicy`
  * `aiplatform.featureOnlineStores.list`
  * `aiplatform.featureOnlineStores.setIamPolicy`
  * `aiplatform.featureOnlineStores.update`

`aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.*`

  * `aiplatform.featureViews.create`
  * `aiplatform.featureViews.delete`
  * `aiplatform.featureViews.directWrite`
  * `aiplatform.featureViews.fetchFeatureValues`
  * `aiplatform.featureViews.get`
  * `aiplatform.featureViews.getIamPolicy`
  * `aiplatform.featureViews.list`
  * `aiplatform.featureViews.searchNearestEntities`
  * `aiplatform.featureViews.setIamPolicy`
  * `aiplatform.featureViews.sync`
  * `aiplatform.featureViews.update`

`aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.*`

  * `aiplatform.featurestores.batchReadFeatureValues`
  * `aiplatform.featurestores.create`
  * `aiplatform.featurestores.delete`
  * `aiplatform.featurestores.exportFeatures`
  * `aiplatform.featurestores.get`
  * `aiplatform.featurestores.getIamPolicy`
  * `aiplatform.featurestores.importFeatures`
  * `aiplatform.featurestores.list`
  * `aiplatform.featurestores.readFeatures`
  * `aiplatform.featurestores.setIamPolicy`
  * `aiplatform.featurestores.update`
  * `aiplatform.featurestores.writeFeatures`

`aiplatform.humanInTheLoops.*`

  * `aiplatform.humanInTheLoops.cancel`
  * `aiplatform.humanInTheLoops.create`
  * `aiplatform.humanInTheLoops.delete`
  * `aiplatform.humanInTheLoops.get`
  * `aiplatform.humanInTheLoops.list`
  * `aiplatform.humanInTheLoops.queryAnnotationStats`
  * `aiplatform.humanInTheLoops.send`
  * `aiplatform.humanInTheLoops.update`

`aiplatform.hyperparameterTuningJobs.*`

  * `aiplatform.hyperparameterTuningJobs.cancel`
  * `aiplatform.hyperparameterTuningJobs.create`
  * `aiplatform.hyperparameterTuningJobs.delete`
  * `aiplatform.hyperparameterTuningJobs.get`
  * `aiplatform.hyperparameterTuningJobs.list`

`aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.interactions.*`

  * `aiplatform.interactions.cancel`
  * `aiplatform.interactions.create`
  * `aiplatform.interactions.delete`
  * `aiplatform.interactions.get`
  * `aiplatform.interactions.list`

`aiplatform.locations.*`

  * `aiplatform.locations.evaluateInstances`
  * `aiplatform.locations.get`
  * `aiplatform.locations.list`

`aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.memoryRevisions.*`

  * `aiplatform.memoryRevisions.get`
  * `aiplatform.memoryRevisions.list`
  * `aiplatform.memoryRevisions.rollback`

`aiplatform.metadataSchemas.*`

  * `aiplatform.metadataSchemas.create`
  * `aiplatform.metadataSchemas.delete`
  * `aiplatform.metadataSchemas.get`
  * `aiplatform.metadataSchemas.list`

`aiplatform.metadataStores.*`

  * `aiplatform.metadataStores.create`
  * `aiplatform.metadataStores.delete`
  * `aiplatform.metadataStores.get`
  * `aiplatform.metadataStores.list`

`aiplatform.migratableResources.*`

  * `aiplatform.migratableResources.migrate`
  * `aiplatform.migratableResources.search`

`aiplatform.modelDeploymentMonitoringJobs.*`

  * `aiplatform.modelDeploymentMonitoringJobs.create`
  * `aiplatform.modelDeploymentMonitoringJobs.delete`
  * `aiplatform.modelDeploymentMonitoringJobs.get`
  * `aiplatform.modelDeploymentMonitoringJobs.list`
  * `aiplatform.modelDeploymentMonitoringJobs.pause`
  * `aiplatform.modelDeploymentMonitoringJobs.resume`
  * `aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`
  * `aiplatform.modelDeploymentMonitoringJobs.update`

`aiplatform.modelEvaluationSlices.*`

  * `aiplatform.modelEvaluationSlices.get`
  * `aiplatform.modelEvaluationSlices.import`
  * `aiplatform.modelEvaluationSlices.list`

`aiplatform.modelEvaluations.*`

  * `aiplatform.modelEvaluations.exportEvaluatedDataItems`
  * `aiplatform.modelEvaluations.get`
  * `aiplatform.modelEvaluations.import`
  * `aiplatform.modelEvaluations.list`

`aiplatform.modelMonitoringJobs.*`

  * `aiplatform.modelMonitoringJobs.create`
  * `aiplatform.modelMonitoringJobs.delete`
  * `aiplatform.modelMonitoringJobs.get`
  * `aiplatform.modelMonitoringJobs.list`

`aiplatform.modelMonitors.*`

  * `aiplatform.modelMonitors.create`
  * `aiplatform.modelMonitors.delete`
  * `aiplatform.modelMonitors.get`
  * `aiplatform.modelMonitors.list`
  * `aiplatform.modelMonitors.searchModelMonitoringAlerts`
  * `aiplatform.modelMonitors.searchModelMonitoringStats`
  * `aiplatform.modelMonitors.update`

`aiplatform.models.*`

  * `aiplatform.models.delete`
  * `aiplatform.models.export`
  * `aiplatform.models.get`
  * `aiplatform.models.list`
  * `aiplatform.models.update`
  * `aiplatform.models.upload`

`aiplatform.monitoredAgents.*`

  * `aiplatform.monitoredAgents.clearTrainingData`
  * `aiplatform.monitoredAgents.disable`
  * `aiplatform.monitoredAgents.enable`
  * `aiplatform.monitoredAgents.get`
  * `aiplatform.monitoredAgents.list`

`aiplatform.nasJobs.*`

  * `aiplatform.nasJobs.cancel`
  * `aiplatform.nasJobs.create`
  * `aiplatform.nasJobs.delete`
  * `aiplatform.nasJobs.get`
  * `aiplatform.nasJobs.list`

`aiplatform.nasTrialDetails.*`

  * `aiplatform.nasTrialDetails.get`
  * `aiplatform.nasTrialDetails.list`

`aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.*`

  * `aiplatform.notebookRuntimeTemplates.apply`
  * `aiplatform.notebookRuntimeTemplates.create`
  * `aiplatform.notebookRuntimeTemplates.delete`
  * `aiplatform.notebookRuntimeTemplates.get`
  * `aiplatform.notebookRuntimeTemplates.getIamPolicy`
  * `aiplatform.notebookRuntimeTemplates.list`
  * `aiplatform.notebookRuntimeTemplates.setDefault`
  * `aiplatform.notebookRuntimeTemplates.setIamPolicy`
  * `aiplatform.notebookRuntimeTemplates.update`

`aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.onlineEvaluators.*`

  * `aiplatform.onlineEvaluators.create`
  * `aiplatform.onlineEvaluators.delete`
  * `aiplatform.onlineEvaluators.get`
  * `aiplatform.onlineEvaluators.list`
  * `aiplatform.onlineEvaluators.update`

`aiplatform.operations.list` `aiplatform.persistentResources.*`

  * `aiplatform.persistentResources.create`
  * `aiplatform.persistentResources.delete`
  * `aiplatform.persistentResources.get`
  * `aiplatform.persistentResources.list`

`aiplatform.pipelineJobs.*`

  * `aiplatform.pipelineJobs.cancel`
  * `aiplatform.pipelineJobs.create`
  * `aiplatform.pipelineJobs.delete`
  * `aiplatform.pipelineJobs.get`
  * `aiplatform.pipelineJobs.list`

`aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.*`

  * `aiplatform.provisionedThroughputs.cancel`
  * `aiplatform.provisionedThroughputs.changeScope`
  * `aiplatform.provisionedThroughputs.create`
  * `aiplatform.provisionedThroughputs.get`
  * `aiplatform.provisionedThroughputs.list`
  * `aiplatform.provisionedThroughputs.split`
  * `aiplatform.provisionedThroughputs.update`

`aiplatform.ragCorpora.*`

  * `aiplatform.ragCorpora.create`
  * `aiplatform.ragCorpora.delete`
  * `aiplatform.ragCorpora.get`
  * `aiplatform.ragCorpora.list`
  * `aiplatform.ragCorpora.query`
  * `aiplatform.ragCorpora.update`

`aiplatform.ragEngineConfigs.*`

  * `aiplatform.ragEngineConfigs.get`
  * `aiplatform.ragEngineConfigs.update`

`aiplatform.ragFiles.*`

  * `aiplatform.ragFiles.delete`
  * `aiplatform.ragFiles.get`
  * `aiplatform.ragFiles.import`
  * `aiplatform.ragFiles.list`
  * `aiplatform.ragFiles.upload`

`aiplatform.reasoningEngineRuntimeRevisions.*`

  * `aiplatform.reasoningEngineRuntimeRevisions.delete`
  * `aiplatform.reasoningEngineRuntimeRevisions.get`
  * `aiplatform.reasoningEngineRuntimeRevisions.list`
  * `aiplatform.reasoningEngineRuntimeRevisions.query`

`aiplatform.reasoningEngines.*`

  * `aiplatform.reasoningEngines.create`
  * `aiplatform.reasoningEngines.delete`
  * `aiplatform.reasoningEngines.get`
  * `aiplatform.reasoningEngines.getIamPolicy`
  * `aiplatform.reasoningEngines.list`
  * `aiplatform.reasoningEngines.query`
  * `aiplatform.reasoningEngines.setIamPolicy`
  * `aiplatform.reasoningEngines.update`

`aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`aiplatform.semanticGovernancePolicies.*`

  * `aiplatform.semanticGovernancePolicies.create`
  * `aiplatform.semanticGovernancePolicies.delete`
  * `aiplatform.semanticGovernancePolicies.get`
  * `aiplatform.semanticGovernancePolicies.list`
  * `aiplatform.semanticGovernancePolicies.update`

`aiplatform.semanticGovernancePolicyEngine.*`

  * `aiplatform.semanticGovernancePolicyEngine.get`
  * `aiplatform.semanticGovernancePolicyEngine.update`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.*`

  * `aiplatform.sessions.create`
  * `aiplatform.sessions.delete`
  * `aiplatform.sessions.get`
  * `aiplatform.sessions.list`
  * `aiplatform.sessions.run`
  * `aiplatform.sessions.update`

`aiplatform.specialistPools.*`

  * `aiplatform.specialistPools.create`
  * `aiplatform.specialistPools.delete`
  * `aiplatform.specialistPools.get`
  * `aiplatform.specialistPools.list`
  * `aiplatform.specialistPools.update`

`aiplatform.studies.*`

  * `aiplatform.studies.create`
  * `aiplatform.studies.delete`
  * `aiplatform.studies.get`
  * `aiplatform.studies.list`
  * `aiplatform.studies.update`

`aiplatform.tasks.*`

  * `aiplatform.tasks.cancel`
  * `aiplatform.tasks.create`
  * `aiplatform.tasks.delete`
  * `aiplatform.tasks.get`
  * `aiplatform.tasks.list`
  * `aiplatform.tasks.update`

`aiplatform.tensorboardExperiments.*`

  * `aiplatform.tensorboardExperiments.create`
  * `aiplatform.tensorboardExperiments.delete`
  * `aiplatform.tensorboardExperiments.get`
  * `aiplatform.tensorboardExperiments.list`
  * `aiplatform.tensorboardExperiments.update`
  * `aiplatform.tensorboardExperiments.write`

`aiplatform.tensorboardRuns.*`

  * `aiplatform.tensorboardRuns.batchCreate`
  * `aiplatform.tensorboardRuns.create`
  * `aiplatform.tensorboardRuns.delete`
  * `aiplatform.tensorboardRuns.get`
  * `aiplatform.tensorboardRuns.list`
  * `aiplatform.tensorboardRuns.update`
  * `aiplatform.tensorboardRuns.write`

`aiplatform.tensorboardTimeSeries.*`

  * `aiplatform.tensorboardTimeSeries.batchCreate`
  * `aiplatform.tensorboardTimeSeries.batchRead`
  * `aiplatform.tensorboardTimeSeries.create`
  * `aiplatform.tensorboardTimeSeries.delete`
  * `aiplatform.tensorboardTimeSeries.get`
  * `aiplatform.tensorboardTimeSeries.list`
  * `aiplatform.tensorboardTimeSeries.read`
  * `aiplatform.tensorboardTimeSeries.update`

`aiplatform.tensorboards.*`

  * `aiplatform.tensorboards.create`
  * `aiplatform.tensorboards.delete`
  * `aiplatform.tensorboards.get`
  * `aiplatform.tensorboards.list`
  * `aiplatform.tensorboards.recordAccess`
  * `aiplatform.tensorboards.update`

`aiplatform.trainingPipelines.*`

  * `aiplatform.trainingPipelines.cancel`
  * `aiplatform.trainingPipelines.create`
  * `aiplatform.trainingPipelines.delete`
  * `aiplatform.trainingPipelines.get`
  * `aiplatform.trainingPipelines.list`

`aiplatform.trials.*`

  * `aiplatform.trials.create`
  * `aiplatform.trials.delete`
  * `aiplatform.trials.get`
  * `aiplatform.trials.list`
  * `aiplatform.trials.update`

`aiplatform.tuningJobs.*`

  * `aiplatform.tuningJobs.cancel`
  * `aiplatform.tuningJobs.create`
  * `aiplatform.tuningJobs.delete`
  * `aiplatform.tuningJobs.get`
  * `aiplatform.tuningJobs.list`
  * `aiplatform.tuningJobs.optimizePrompt`
  * `aiplatform.tuningJobs.validateReinforcementTuningReward`
  * `aiplatform.tuningJobs.vertexTune`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Aiplatform Editor 

(`roles/aiplatform.editor`) Editor role for aiplatform  |  `aiplatform.agentAnomalyDetectionScopes.*`

  * `aiplatform.agentAnomalyDetectionScopes.create`
  * `aiplatform.agentAnomalyDetectionScopes.delete`
  * `aiplatform.agentAnomalyDetectionScopes.get`
  * `aiplatform.agentAnomalyDetectionScopes.list`

`aiplatform.agentExamples.*`

  * `aiplatform.agentExamples.create`
  * `aiplatform.agentExamples.delete`
  * `aiplatform.agentExamples.get`
  * `aiplatform.agentExamples.list`
  * `aiplatform.agentExamples.update`

`aiplatform.agents.create` `aiplatform.agents.delete` `aiplatform.agents.get` `aiplatform.agents.getIamPolicy` `aiplatform.agents.list` `aiplatform.agents.update` `aiplatform.analyzedInvocations.*`

  * `aiplatform.analyzedInvocations.get`
  * `aiplatform.analyzedInvocations.list`

`aiplatform.analyzedSessions.*`

  * `aiplatform.analyzedSessions.aggregate`
  * `aiplatform.analyzedSessions.get`
  * `aiplatform.analyzedSessions.list`

`aiplatform.annotationSpecs.*`

  * `aiplatform.annotationSpecs.create`
  * `aiplatform.annotationSpecs.delete`
  * `aiplatform.annotationSpecs.get`
  * `aiplatform.annotationSpecs.list`
  * `aiplatform.annotationSpecs.update`

`aiplatform.annotations.*`

  * `aiplatform.annotations.create`
  * `aiplatform.annotations.delete`
  * `aiplatform.annotations.get`
  * `aiplatform.annotations.list`
  * `aiplatform.annotations.update`

`aiplatform.apps.*`

  * `aiplatform.apps.create`
  * `aiplatform.apps.delete`
  * `aiplatform.apps.get`
  * `aiplatform.apps.list`
  * `aiplatform.apps.update`

`aiplatform.artifacts.*`

  * `aiplatform.artifacts.create`
  * `aiplatform.artifacts.delete`
  * `aiplatform.artifacts.get`
  * `aiplatform.artifacts.list`
  * `aiplatform.artifacts.update`

`aiplatform.batchPredictionJobs.*`

  * `aiplatform.batchPredictionJobs.cancel`
  * `aiplatform.batchPredictionJobs.create`
  * `aiplatform.batchPredictionJobs.delete`
  * `aiplatform.batchPredictionJobs.get`
  * `aiplatform.batchPredictionJobs.list`

`aiplatform.cacheConfigs.*`

  * `aiplatform.cacheConfigs.get`
  * `aiplatform.cacheConfigs.update`

`aiplatform.cachedContents.*`

  * `aiplatform.cachedContents.create`
  * `aiplatform.cachedContents.delete`
  * `aiplatform.cachedContents.get`
  * `aiplatform.cachedContents.list`
  * `aiplatform.cachedContents.update`

`aiplatform.consents.*`

  * `aiplatform.consents.get`
  * `aiplatform.consents.update`

`aiplatform.contexts.*`

  * `aiplatform.contexts.addContextArtifactsAndExecutions`
  * `aiplatform.contexts.addContextChildren`
  * `aiplatform.contexts.create`
  * `aiplatform.contexts.delete`
  * `aiplatform.contexts.get`
  * `aiplatform.contexts.list`
  * `aiplatform.contexts.queryContextLineageSubgraph`
  * `aiplatform.contexts.update`

`aiplatform.customJobs.*`

  * `aiplatform.customJobs.cancel`
  * `aiplatform.customJobs.create`
  * `aiplatform.customJobs.delete`
  * `aiplatform.customJobs.get`
  * `aiplatform.customJobs.list`

`aiplatform.dataItems.*`

  * `aiplatform.dataItems.create`
  * `aiplatform.dataItems.delete`
  * `aiplatform.dataItems.get`
  * `aiplatform.dataItems.list`
  * `aiplatform.dataItems.update`

`aiplatform.dataLabelingJobs.*`

  * `aiplatform.dataLabelingJobs.cancel`
  * `aiplatform.dataLabelingJobs.create`
  * `aiplatform.dataLabelingJobs.delete`
  * `aiplatform.dataLabelingJobs.get`
  * `aiplatform.dataLabelingJobs.list`

`aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.*`

  * `aiplatform.datasets.create`
  * `aiplatform.datasets.delete`
  * `aiplatform.datasets.export`
  * `aiplatform.datasets.get`
  * `aiplatform.datasets.import`
  * `aiplatform.datasets.list`
  * `aiplatform.datasets.update`

`aiplatform.deploymentResourcePools.*`

  * `aiplatform.deploymentResourcePools.create`
  * `aiplatform.deploymentResourcePools.delete`
  * `aiplatform.deploymentResourcePools.get`
  * `aiplatform.deploymentResourcePools.list`
  * `aiplatform.deploymentResourcePools.queryDeployedModels`
  * `aiplatform.deploymentResourcePools.update`

`aiplatform.edgeDeploymentJobs.*`

  * `aiplatform.edgeDeploymentJobs.create`
  * `aiplatform.edgeDeploymentJobs.delete`
  * `aiplatform.edgeDeploymentJobs.get`
  * `aiplatform.edgeDeploymentJobs.list`

`aiplatform.edgeDeviceDebugInfo.get` `aiplatform.edgeDevices.*`

  * `aiplatform.edgeDevices.create`
  * `aiplatform.edgeDevices.delete`
  * `aiplatform.edgeDevices.get`
  * `aiplatform.edgeDevices.list`
  * `aiplatform.edgeDevices.update`

`aiplatform.endpoints.create` `aiplatform.endpoints.delete` `aiplatform.endpoints.deploy` `aiplatform.endpoints.explain` `aiplatform.endpoints.get` `aiplatform.endpoints.getIamPolicy` `aiplatform.endpoints.list` `aiplatform.endpoints.predict` `aiplatform.endpoints.undeploy` `aiplatform.endpoints.update` `aiplatform.entityTypes.create` `aiplatform.entityTypes.delete` `aiplatform.entityTypes.deleteFeatureValues` `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.getIamPolicy` `aiplatform.entityTypes.importFeatureValues` `aiplatform.entityTypes.list` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.entityTypes.update` `aiplatform.entityTypes.writeFeatureValues` `aiplatform.evaluationExperiments.*`

  * `aiplatform.evaluationExperiments.create`
  * `aiplatform.evaluationExperiments.delete`
  * `aiplatform.evaluationExperiments.get`
  * `aiplatform.evaluationExperiments.list`
  * `aiplatform.evaluationExperiments.update`

`aiplatform.evaluationItems.*`

  * `aiplatform.evaluationItems.create`
  * `aiplatform.evaluationItems.delete`
  * `aiplatform.evaluationItems.get`
  * `aiplatform.evaluationItems.list`
  * `aiplatform.evaluationItems.update`

`aiplatform.evaluationMetrics.*`

  * `aiplatform.evaluationMetrics.create`
  * `aiplatform.evaluationMetrics.delete`
  * `aiplatform.evaluationMetrics.get`
  * `aiplatform.evaluationMetrics.list`

`aiplatform.evaluationRuns.*`

  * `aiplatform.evaluationRuns.cancel`
  * `aiplatform.evaluationRuns.create`
  * `aiplatform.evaluationRuns.delete`
  * `aiplatform.evaluationRuns.execute`
  * `aiplatform.evaluationRuns.get`
  * `aiplatform.evaluationRuns.list`
  * `aiplatform.evaluationRuns.update`

`aiplatform.evaluationSets.*`

  * `aiplatform.evaluationSets.create`
  * `aiplatform.evaluationSets.delete`
  * `aiplatform.evaluationSets.get`
  * `aiplatform.evaluationSets.import`
  * `aiplatform.evaluationSets.list`
  * `aiplatform.evaluationSets.update`

`aiplatform.exampleStores.*`

  * `aiplatform.exampleStores.create`
  * `aiplatform.exampleStores.delete`
  * `aiplatform.exampleStores.get`
  * `aiplatform.exampleStores.list`
  * `aiplatform.exampleStores.readExample`
  * `aiplatform.exampleStores.update`
  * `aiplatform.exampleStores.writeExample`

`aiplatform.executions.*`

  * `aiplatform.executions.addExecutionEvents`
  * `aiplatform.executions.create`
  * `aiplatform.executions.delete`
  * `aiplatform.executions.get`
  * `aiplatform.executions.list`
  * `aiplatform.executions.queryExecutionInputsAndOutputs`
  * `aiplatform.executions.update`

`aiplatform.extensions.*`

  * `aiplatform.extensions.delete`
  * `aiplatform.extensions.execute`
  * `aiplatform.extensions.get`
  * `aiplatform.extensions.import`
  * `aiplatform.extensions.list`
  * `aiplatform.extensions.update`

`aiplatform.featureGroups.create` `aiplatform.featureGroups.delete` `aiplatform.featureGroups.get` `aiplatform.featureGroups.getIamPolicy` `aiplatform.featureGroups.list` `aiplatform.featureGroups.update` `aiplatform.featureMonitorJobs.*`

  * `aiplatform.featureMonitorJobs.create`
  * `aiplatform.featureMonitorJobs.get`
  * `aiplatform.featureMonitorJobs.list`

`aiplatform.featureMonitors.*`

  * `aiplatform.featureMonitors.create`
  * `aiplatform.featureMonitors.delete`
  * `aiplatform.featureMonitors.get`
  * `aiplatform.featureMonitors.list`
  * `aiplatform.featureMonitors.update`

`aiplatform.featureOnlineStores.create` `aiplatform.featureOnlineStores.delete` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.getIamPolicy` `aiplatform.featureOnlineStores.list` `aiplatform.featureOnlineStores.update` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.create` `aiplatform.featureViews.delete` `aiplatform.featureViews.directWrite` `aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.getIamPolicy` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.featureViews.sync` `aiplatform.featureViews.update` `aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.batchReadFeatureValues` `aiplatform.featurestores.create` `aiplatform.featurestores.delete` `aiplatform.featurestores.exportFeatures` `aiplatform.featurestores.get` `aiplatform.featurestores.getIamPolicy` `aiplatform.featurestores.importFeatures` `aiplatform.featurestores.list` `aiplatform.featurestores.readFeatures` `aiplatform.featurestores.update` `aiplatform.featurestores.writeFeatures` `aiplatform.humanInTheLoops.*`

  * `aiplatform.humanInTheLoops.cancel`
  * `aiplatform.humanInTheLoops.create`
  * `aiplatform.humanInTheLoops.delete`
  * `aiplatform.humanInTheLoops.get`
  * `aiplatform.humanInTheLoops.list`
  * `aiplatform.humanInTheLoops.queryAnnotationStats`
  * `aiplatform.humanInTheLoops.send`
  * `aiplatform.humanInTheLoops.update`

`aiplatform.hyperparameterTuningJobs.*`

  * `aiplatform.hyperparameterTuningJobs.cancel`
  * `aiplatform.hyperparameterTuningJobs.create`
  * `aiplatform.hyperparameterTuningJobs.delete`
  * `aiplatform.hyperparameterTuningJobs.get`
  * `aiplatform.hyperparameterTuningJobs.list`

`aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.interactions.*`

  * `aiplatform.interactions.cancel`
  * `aiplatform.interactions.create`
  * `aiplatform.interactions.delete`
  * `aiplatform.interactions.get`
  * `aiplatform.interactions.list`

`aiplatform.locations.*`

  * `aiplatform.locations.evaluateInstances`
  * `aiplatform.locations.get`
  * `aiplatform.locations.list`

`aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.memoryRevisions.*`

  * `aiplatform.memoryRevisions.get`
  * `aiplatform.memoryRevisions.list`
  * `aiplatform.memoryRevisions.rollback`

`aiplatform.metadataSchemas.*`

  * `aiplatform.metadataSchemas.create`
  * `aiplatform.metadataSchemas.delete`
  * `aiplatform.metadataSchemas.get`
  * `aiplatform.metadataSchemas.list`

`aiplatform.metadataStores.*`

  * `aiplatform.metadataStores.create`
  * `aiplatform.metadataStores.delete`
  * `aiplatform.metadataStores.get`
  * `aiplatform.metadataStores.list`

`aiplatform.migratableResources.*`

  * `aiplatform.migratableResources.migrate`
  * `aiplatform.migratableResources.search`

`aiplatform.modelDeploymentMonitoringJobs.*`

  * `aiplatform.modelDeploymentMonitoringJobs.create`
  * `aiplatform.modelDeploymentMonitoringJobs.delete`
  * `aiplatform.modelDeploymentMonitoringJobs.get`
  * `aiplatform.modelDeploymentMonitoringJobs.list`
  * `aiplatform.modelDeploymentMonitoringJobs.pause`
  * `aiplatform.modelDeploymentMonitoringJobs.resume`
  * `aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`
  * `aiplatform.modelDeploymentMonitoringJobs.update`

`aiplatform.modelEvaluationSlices.*`

  * `aiplatform.modelEvaluationSlices.get`
  * `aiplatform.modelEvaluationSlices.import`
  * `aiplatform.modelEvaluationSlices.list`

`aiplatform.modelEvaluations.*`

  * `aiplatform.modelEvaluations.exportEvaluatedDataItems`
  * `aiplatform.modelEvaluations.get`
  * `aiplatform.modelEvaluations.import`
  * `aiplatform.modelEvaluations.list`

`aiplatform.modelMonitoringJobs.*`

  * `aiplatform.modelMonitoringJobs.create`
  * `aiplatform.modelMonitoringJobs.delete`
  * `aiplatform.modelMonitoringJobs.get`
  * `aiplatform.modelMonitoringJobs.list`

`aiplatform.modelMonitors.*`

  * `aiplatform.modelMonitors.create`
  * `aiplatform.modelMonitors.delete`
  * `aiplatform.modelMonitors.get`
  * `aiplatform.modelMonitors.list`
  * `aiplatform.modelMonitors.searchModelMonitoringAlerts`
  * `aiplatform.modelMonitors.searchModelMonitoringStats`
  * `aiplatform.modelMonitors.update`

`aiplatform.models.*`

  * `aiplatform.models.delete`
  * `aiplatform.models.export`
  * `aiplatform.models.get`
  * `aiplatform.models.list`
  * `aiplatform.models.update`
  * `aiplatform.models.upload`

`aiplatform.monitoredAgents.*`

  * `aiplatform.monitoredAgents.clearTrainingData`
  * `aiplatform.monitoredAgents.disable`
  * `aiplatform.monitoredAgents.enable`
  * `aiplatform.monitoredAgents.get`
  * `aiplatform.monitoredAgents.list`

`aiplatform.nasJobs.*`

  * `aiplatform.nasJobs.cancel`
  * `aiplatform.nasJobs.create`
  * `aiplatform.nasJobs.delete`
  * `aiplatform.nasJobs.get`
  * `aiplatform.nasJobs.list`

`aiplatform.nasTrialDetails.*`

  * `aiplatform.nasTrialDetails.get`
  * `aiplatform.nasTrialDetails.list`

`aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.create` `aiplatform.notebookRuntimeTemplates.delete` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimeTemplates.setDefault` `aiplatform.notebookRuntimeTemplates.update` `aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.onlineEvaluators.*`

  * `aiplatform.onlineEvaluators.create`
  * `aiplatform.onlineEvaluators.delete`
  * `aiplatform.onlineEvaluators.get`
  * `aiplatform.onlineEvaluators.list`
  * `aiplatform.onlineEvaluators.update`

`aiplatform.operations.list` `aiplatform.persistentResources.*`

  * `aiplatform.persistentResources.create`
  * `aiplatform.persistentResources.delete`
  * `aiplatform.persistentResources.get`
  * `aiplatform.persistentResources.list`

`aiplatform.pipelineJobs.*`

  * `aiplatform.pipelineJobs.cancel`
  * `aiplatform.pipelineJobs.create`
  * `aiplatform.pipelineJobs.delete`
  * `aiplatform.pipelineJobs.get`
  * `aiplatform.pipelineJobs.list`

`aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.*`

  * `aiplatform.provisionedThroughputs.cancel`
  * `aiplatform.provisionedThroughputs.changeScope`
  * `aiplatform.provisionedThroughputs.create`
  * `aiplatform.provisionedThroughputs.get`
  * `aiplatform.provisionedThroughputs.list`
  * `aiplatform.provisionedThroughputs.split`
  * `aiplatform.provisionedThroughputs.update`

`aiplatform.ragCorpora.*`

  * `aiplatform.ragCorpora.create`
  * `aiplatform.ragCorpora.delete`
  * `aiplatform.ragCorpora.get`
  * `aiplatform.ragCorpora.list`
  * `aiplatform.ragCorpora.query`
  * `aiplatform.ragCorpora.update`

`aiplatform.ragEngineConfigs.*`

  * `aiplatform.ragEngineConfigs.get`
  * `aiplatform.ragEngineConfigs.update`

`aiplatform.ragFiles.*`

  * `aiplatform.ragFiles.delete`
  * `aiplatform.ragFiles.get`
  * `aiplatform.ragFiles.import`
  * `aiplatform.ragFiles.list`
  * `aiplatform.ragFiles.upload`

`aiplatform.reasoningEngineRuntimeRevisions.*`

  * `aiplatform.reasoningEngineRuntimeRevisions.delete`
  * `aiplatform.reasoningEngineRuntimeRevisions.get`
  * `aiplatform.reasoningEngineRuntimeRevisions.list`
  * `aiplatform.reasoningEngineRuntimeRevisions.query`

`aiplatform.reasoningEngines.create` `aiplatform.reasoningEngines.delete` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.getIamPolicy` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.reasoningEngines.update` `aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`aiplatform.semanticGovernancePolicies.*`

  * `aiplatform.semanticGovernancePolicies.create`
  * `aiplatform.semanticGovernancePolicies.delete`
  * `aiplatform.semanticGovernancePolicies.get`
  * `aiplatform.semanticGovernancePolicies.list`
  * `aiplatform.semanticGovernancePolicies.update`

`aiplatform.semanticGovernancePolicyEngine.*`

  * `aiplatform.semanticGovernancePolicyEngine.get`
  * `aiplatform.semanticGovernancePolicyEngine.update`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.*`

  * `aiplatform.sessions.create`
  * `aiplatform.sessions.delete`
  * `aiplatform.sessions.get`
  * `aiplatform.sessions.list`
  * `aiplatform.sessions.run`
  * `aiplatform.sessions.update`

`aiplatform.specialistPools.*`

  * `aiplatform.specialistPools.create`
  * `aiplatform.specialistPools.delete`
  * `aiplatform.specialistPools.get`
  * `aiplatform.specialistPools.list`
  * `aiplatform.specialistPools.update`

`aiplatform.studies.*`

  * `aiplatform.studies.create`
  * `aiplatform.studies.delete`
  * `aiplatform.studies.get`
  * `aiplatform.studies.list`
  * `aiplatform.studies.update`

`aiplatform.tasks.*`

  * `aiplatform.tasks.cancel`
  * `aiplatform.tasks.create`
  * `aiplatform.tasks.delete`
  * `aiplatform.tasks.get`
  * `aiplatform.tasks.list`
  * `aiplatform.tasks.update`

`aiplatform.tensorboardExperiments.*`

  * `aiplatform.tensorboardExperiments.create`
  * `aiplatform.tensorboardExperiments.delete`
  * `aiplatform.tensorboardExperiments.get`
  * `aiplatform.tensorboardExperiments.list`
  * `aiplatform.tensorboardExperiments.update`
  * `aiplatform.tensorboardExperiments.write`

`aiplatform.tensorboardRuns.*`

  * `aiplatform.tensorboardRuns.batchCreate`
  * `aiplatform.tensorboardRuns.create`
  * `aiplatform.tensorboardRuns.delete`
  * `aiplatform.tensorboardRuns.get`
  * `aiplatform.tensorboardRuns.list`
  * `aiplatform.tensorboardRuns.update`
  * `aiplatform.tensorboardRuns.write`

`aiplatform.tensorboardTimeSeries.*`

  * `aiplatform.tensorboardTimeSeries.batchCreate`
  * `aiplatform.tensorboardTimeSeries.batchRead`
  * `aiplatform.tensorboardTimeSeries.create`
  * `aiplatform.tensorboardTimeSeries.delete`
  * `aiplatform.tensorboardTimeSeries.get`
  * `aiplatform.tensorboardTimeSeries.list`
  * `aiplatform.tensorboardTimeSeries.read`
  * `aiplatform.tensorboardTimeSeries.update`

`aiplatform.tensorboards.create` `aiplatform.tensorboards.delete` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.tensorboards.update` `aiplatform.trainingPipelines.*`

  * `aiplatform.trainingPipelines.cancel`
  * `aiplatform.trainingPipelines.create`
  * `aiplatform.trainingPipelines.delete`
  * `aiplatform.trainingPipelines.get`
  * `aiplatform.trainingPipelines.list`

`aiplatform.trials.*`

  * `aiplatform.trials.create`
  * `aiplatform.trials.delete`
  * `aiplatform.trials.get`
  * `aiplatform.trials.list`
  * `aiplatform.trials.update`

`aiplatform.tuningJobs.*`

  * `aiplatform.tuningJobs.cancel`
  * `aiplatform.tuningJobs.create`
  * `aiplatform.tuningJobs.delete`
  * `aiplatform.tuningJobs.get`
  * `aiplatform.tuningJobs.list`
  * `aiplatform.tuningJobs.optimizePrompt`
  * `aiplatform.tuningJobs.validateReinforcementTuningReward`
  * `aiplatform.tuningJobs.vertexTune`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Express User Beta

(`roles/aiplatform.expressUser`) Grants user access to Agent Platform Express.  |  `aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.create` `aiplatform.datasets.delete` `aiplatform.datasets.get` `aiplatform.datasets.list` `aiplatform.datasets.update` `aiplatform.endpoints.predict` `aiplatform.locations.evaluateInstances` `aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.operations.list` `aiplatform.reasoningEngines.create` `aiplatform.reasoningEngines.delete` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.reasoningEngines.update` `aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.create` `aiplatform.sessions.delete` `aiplatform.sessions.get` `aiplatform.sessions.list` `aiplatform.sessions.update`  
  
#### Agent Platform User 

(`roles/aiplatform.user`) Grants access to use all resource in Agent Platform.  |  `aiplatform.agentAnomalyDetectionScopes.*`

  * `aiplatform.agentAnomalyDetectionScopes.create`
  * `aiplatform.agentAnomalyDetectionScopes.delete`
  * `aiplatform.agentAnomalyDetectionScopes.get`
  * `aiplatform.agentAnomalyDetectionScopes.list`

`aiplatform.agentExamples.*`

  * `aiplatform.agentExamples.create`
  * `aiplatform.agentExamples.delete`
  * `aiplatform.agentExamples.get`
  * `aiplatform.agentExamples.list`
  * `aiplatform.agentExamples.update`

`aiplatform.agents.create` `aiplatform.agents.delete` `aiplatform.agents.get` `aiplatform.agents.list` `aiplatform.agents.update` `aiplatform.analyzedInvocations.*`

  * `aiplatform.analyzedInvocations.get`
  * `aiplatform.analyzedInvocations.list`

`aiplatform.analyzedSessions.*`

  * `aiplatform.analyzedSessions.aggregate`
  * `aiplatform.analyzedSessions.get`
  * `aiplatform.analyzedSessions.list`

`aiplatform.annotationSpecs.*`

  * `aiplatform.annotationSpecs.create`
  * `aiplatform.annotationSpecs.delete`
  * `aiplatform.annotationSpecs.get`
  * `aiplatform.annotationSpecs.list`
  * `aiplatform.annotationSpecs.update`

`aiplatform.annotations.*`

  * `aiplatform.annotations.create`
  * `aiplatform.annotations.delete`
  * `aiplatform.annotations.get`
  * `aiplatform.annotations.list`
  * `aiplatform.annotations.update`

`aiplatform.apps.*`

  * `aiplatform.apps.create`
  * `aiplatform.apps.delete`
  * `aiplatform.apps.get`
  * `aiplatform.apps.list`
  * `aiplatform.apps.update`

`aiplatform.artifacts.*`

  * `aiplatform.artifacts.create`
  * `aiplatform.artifacts.delete`
  * `aiplatform.artifacts.get`
  * `aiplatform.artifacts.list`
  * `aiplatform.artifacts.update`

`aiplatform.batchPredictionJobs.*`

  * `aiplatform.batchPredictionJobs.cancel`
  * `aiplatform.batchPredictionJobs.create`
  * `aiplatform.batchPredictionJobs.delete`
  * `aiplatform.batchPredictionJobs.get`
  * `aiplatform.batchPredictionJobs.list`

`aiplatform.cacheConfigs.get` `aiplatform.cachedContents.*`

  * `aiplatform.cachedContents.create`
  * `aiplatform.cachedContents.delete`
  * `aiplatform.cachedContents.get`
  * `aiplatform.cachedContents.list`
  * `aiplatform.cachedContents.update`

`aiplatform.consents.get` `aiplatform.contexts.*`

  * `aiplatform.contexts.addContextArtifactsAndExecutions`
  * `aiplatform.contexts.addContextChildren`
  * `aiplatform.contexts.create`
  * `aiplatform.contexts.delete`
  * `aiplatform.contexts.get`
  * `aiplatform.contexts.list`
  * `aiplatform.contexts.queryContextLineageSubgraph`
  * `aiplatform.contexts.update`

`aiplatform.customJobs.*`

  * `aiplatform.customJobs.cancel`
  * `aiplatform.customJobs.create`
  * `aiplatform.customJobs.delete`
  * `aiplatform.customJobs.get`
  * `aiplatform.customJobs.list`

`aiplatform.dataItems.*`

  * `aiplatform.dataItems.create`
  * `aiplatform.dataItems.delete`
  * `aiplatform.dataItems.get`
  * `aiplatform.dataItems.list`
  * `aiplatform.dataItems.update`

`aiplatform.dataLabelingJobs.*`

  * `aiplatform.dataLabelingJobs.cancel`
  * `aiplatform.dataLabelingJobs.create`
  * `aiplatform.dataLabelingJobs.delete`
  * `aiplatform.dataLabelingJobs.get`
  * `aiplatform.dataLabelingJobs.list`

`aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.*`

  * `aiplatform.datasets.create`
  * `aiplatform.datasets.delete`
  * `aiplatform.datasets.export`
  * `aiplatform.datasets.get`
  * `aiplatform.datasets.import`
  * `aiplatform.datasets.list`
  * `aiplatform.datasets.update`

`aiplatform.deploymentResourcePools.*`

  * `aiplatform.deploymentResourcePools.create`
  * `aiplatform.deploymentResourcePools.delete`
  * `aiplatform.deploymentResourcePools.get`
  * `aiplatform.deploymentResourcePools.list`
  * `aiplatform.deploymentResourcePools.queryDeployedModels`
  * `aiplatform.deploymentResourcePools.update`

`aiplatform.edgeDeploymentJobs.*`

  * `aiplatform.edgeDeploymentJobs.create`
  * `aiplatform.edgeDeploymentJobs.delete`
  * `aiplatform.edgeDeploymentJobs.get`
  * `aiplatform.edgeDeploymentJobs.list`

`aiplatform.edgeDeviceDebugInfo.get` `aiplatform.edgeDevices.*`

  * `aiplatform.edgeDevices.create`
  * `aiplatform.edgeDevices.delete`
  * `aiplatform.edgeDevices.get`
  * `aiplatform.edgeDevices.list`
  * `aiplatform.edgeDevices.update`

`aiplatform.endpoints.create` `aiplatform.endpoints.delete` `aiplatform.endpoints.deploy` `aiplatform.endpoints.explain` `aiplatform.endpoints.get` `aiplatform.endpoints.getIamPolicy` `aiplatform.endpoints.list` `aiplatform.endpoints.predict` `aiplatform.endpoints.undeploy` `aiplatform.endpoints.update` `aiplatform.entityTypes.create` `aiplatform.entityTypes.delete` `aiplatform.entityTypes.deleteFeatureValues` `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.getIamPolicy` `aiplatform.entityTypes.importFeatureValues` `aiplatform.entityTypes.list` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.entityTypes.update` `aiplatform.entityTypes.writeFeatureValues` `aiplatform.evaluationExperiments.*`

  * `aiplatform.evaluationExperiments.create`
  * `aiplatform.evaluationExperiments.delete`
  * `aiplatform.evaluationExperiments.get`
  * `aiplatform.evaluationExperiments.list`
  * `aiplatform.evaluationExperiments.update`

`aiplatform.evaluationItems.*`

  * `aiplatform.evaluationItems.create`
  * `aiplatform.evaluationItems.delete`
  * `aiplatform.evaluationItems.get`
  * `aiplatform.evaluationItems.list`
  * `aiplatform.evaluationItems.update`

`aiplatform.evaluationMetrics.*`

  * `aiplatform.evaluationMetrics.create`
  * `aiplatform.evaluationMetrics.delete`
  * `aiplatform.evaluationMetrics.get`
  * `aiplatform.evaluationMetrics.list`

`aiplatform.evaluationRuns.*`

  * `aiplatform.evaluationRuns.cancel`
  * `aiplatform.evaluationRuns.create`
  * `aiplatform.evaluationRuns.delete`
  * `aiplatform.evaluationRuns.execute`
  * `aiplatform.evaluationRuns.get`
  * `aiplatform.evaluationRuns.list`
  * `aiplatform.evaluationRuns.update`

`aiplatform.evaluationSets.*`

  * `aiplatform.evaluationSets.create`
  * `aiplatform.evaluationSets.delete`
  * `aiplatform.evaluationSets.get`
  * `aiplatform.evaluationSets.import`
  * `aiplatform.evaluationSets.list`
  * `aiplatform.evaluationSets.update`

`aiplatform.exampleStores.*`

  * `aiplatform.exampleStores.create`
  * `aiplatform.exampleStores.delete`
  * `aiplatform.exampleStores.get`
  * `aiplatform.exampleStores.list`
  * `aiplatform.exampleStores.readExample`
  * `aiplatform.exampleStores.update`
  * `aiplatform.exampleStores.writeExample`

`aiplatform.executions.*`

  * `aiplatform.executions.addExecutionEvents`
  * `aiplatform.executions.create`
  * `aiplatform.executions.delete`
  * `aiplatform.executions.get`
  * `aiplatform.executions.list`
  * `aiplatform.executions.queryExecutionInputsAndOutputs`
  * `aiplatform.executions.update`

`aiplatform.extensions.*`

  * `aiplatform.extensions.delete`
  * `aiplatform.extensions.execute`
  * `aiplatform.extensions.get`
  * `aiplatform.extensions.import`
  * `aiplatform.extensions.list`
  * `aiplatform.extensions.update`

`aiplatform.featureGroups.create` `aiplatform.featureGroups.delete` `aiplatform.featureGroups.get` `aiplatform.featureGroups.getIamPolicy` `aiplatform.featureGroups.list` `aiplatform.featureGroups.update` `aiplatform.featureMonitorJobs.*`

  * `aiplatform.featureMonitorJobs.create`
  * `aiplatform.featureMonitorJobs.get`
  * `aiplatform.featureMonitorJobs.list`

`aiplatform.featureMonitors.*`

  * `aiplatform.featureMonitors.create`
  * `aiplatform.featureMonitors.delete`
  * `aiplatform.featureMonitors.get`
  * `aiplatform.featureMonitors.list`
  * `aiplatform.featureMonitors.update`

`aiplatform.featureOnlineStores.create` `aiplatform.featureOnlineStores.delete` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.getIamPolicy` `aiplatform.featureOnlineStores.list` `aiplatform.featureOnlineStores.update` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.create` `aiplatform.featureViews.delete` `aiplatform.featureViews.directWrite` `aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.getIamPolicy` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.featureViews.sync` `aiplatform.featureViews.update` `aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.batchReadFeatureValues` `aiplatform.featurestores.create` `aiplatform.featurestores.delete` `aiplatform.featurestores.exportFeatures` `aiplatform.featurestores.get` `aiplatform.featurestores.getIamPolicy` `aiplatform.featurestores.importFeatures` `aiplatform.featurestores.list` `aiplatform.featurestores.readFeatures` `aiplatform.featurestores.update` `aiplatform.featurestores.writeFeatures` `aiplatform.humanInTheLoops.*`

  * `aiplatform.humanInTheLoops.cancel`
  * `aiplatform.humanInTheLoops.create`
  * `aiplatform.humanInTheLoops.delete`
  * `aiplatform.humanInTheLoops.get`
  * `aiplatform.humanInTheLoops.list`
  * `aiplatform.humanInTheLoops.queryAnnotationStats`
  * `aiplatform.humanInTheLoops.send`
  * `aiplatform.humanInTheLoops.update`

`aiplatform.hyperparameterTuningJobs.*`

  * `aiplatform.hyperparameterTuningJobs.cancel`
  * `aiplatform.hyperparameterTuningJobs.create`
  * `aiplatform.hyperparameterTuningJobs.delete`
  * `aiplatform.hyperparameterTuningJobs.get`
  * `aiplatform.hyperparameterTuningJobs.list`

`aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.interactions.*`

  * `aiplatform.interactions.cancel`
  * `aiplatform.interactions.create`
  * `aiplatform.interactions.delete`
  * `aiplatform.interactions.get`
  * `aiplatform.interactions.list`

`aiplatform.locations.*`

  * `aiplatform.locations.evaluateInstances`
  * `aiplatform.locations.get`
  * `aiplatform.locations.list`

`aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.memoryRevisions.*`

  * `aiplatform.memoryRevisions.get`
  * `aiplatform.memoryRevisions.list`
  * `aiplatform.memoryRevisions.rollback`

`aiplatform.metadataSchemas.*`

  * `aiplatform.metadataSchemas.create`
  * `aiplatform.metadataSchemas.delete`
  * `aiplatform.metadataSchemas.get`
  * `aiplatform.metadataSchemas.list`

`aiplatform.metadataStores.*`

  * `aiplatform.metadataStores.create`
  * `aiplatform.metadataStores.delete`
  * `aiplatform.metadataStores.get`
  * `aiplatform.metadataStores.list`

`aiplatform.migratableResources.search` `aiplatform.modelDeploymentMonitoringJobs.*`

  * `aiplatform.modelDeploymentMonitoringJobs.create`
  * `aiplatform.modelDeploymentMonitoringJobs.delete`
  * `aiplatform.modelDeploymentMonitoringJobs.get`
  * `aiplatform.modelDeploymentMonitoringJobs.list`
  * `aiplatform.modelDeploymentMonitoringJobs.pause`
  * `aiplatform.modelDeploymentMonitoringJobs.resume`
  * `aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`
  * `aiplatform.modelDeploymentMonitoringJobs.update`

`aiplatform.modelEvaluationSlices.*`

  * `aiplatform.modelEvaluationSlices.get`
  * `aiplatform.modelEvaluationSlices.import`
  * `aiplatform.modelEvaluationSlices.list`

`aiplatform.modelEvaluations.*`

  * `aiplatform.modelEvaluations.exportEvaluatedDataItems`
  * `aiplatform.modelEvaluations.get`
  * `aiplatform.modelEvaluations.import`
  * `aiplatform.modelEvaluations.list`

`aiplatform.modelMonitoringJobs.*`

  * `aiplatform.modelMonitoringJobs.create`
  * `aiplatform.modelMonitoringJobs.delete`
  * `aiplatform.modelMonitoringJobs.get`
  * `aiplatform.modelMonitoringJobs.list`

`aiplatform.modelMonitors.*`

  * `aiplatform.modelMonitors.create`
  * `aiplatform.modelMonitors.delete`
  * `aiplatform.modelMonitors.get`
  * `aiplatform.modelMonitors.list`
  * `aiplatform.modelMonitors.searchModelMonitoringAlerts`
  * `aiplatform.modelMonitors.searchModelMonitoringStats`
  * `aiplatform.modelMonitors.update`

`aiplatform.models.*`

  * `aiplatform.models.delete`
  * `aiplatform.models.export`
  * `aiplatform.models.get`
  * `aiplatform.models.list`
  * `aiplatform.models.update`
  * `aiplatform.models.upload`

`aiplatform.monitoredAgents.disable` `aiplatform.monitoredAgents.enable` `aiplatform.monitoredAgents.get` `aiplatform.monitoredAgents.list` `aiplatform.nasJobs.*`

  * `aiplatform.nasJobs.cancel`
  * `aiplatform.nasJobs.create`
  * `aiplatform.nasJobs.delete`
  * `aiplatform.nasJobs.get`
  * `aiplatform.nasJobs.list`

`aiplatform.nasTrialDetails.*`

  * `aiplatform.nasTrialDetails.get`
  * `aiplatform.nasTrialDetails.list`

`aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.create` `aiplatform.notebookRuntimeTemplates.delete` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimeTemplates.update` `aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.onlineEvaluators.*`

  * `aiplatform.onlineEvaluators.create`
  * `aiplatform.onlineEvaluators.delete`
  * `aiplatform.onlineEvaluators.get`
  * `aiplatform.onlineEvaluators.list`
  * `aiplatform.onlineEvaluators.update`

`aiplatform.operations.list` `aiplatform.persistentResources.get` `aiplatform.persistentResources.list` `aiplatform.pipelineJobs.*`

  * `aiplatform.pipelineJobs.cancel`
  * `aiplatform.pipelineJobs.create`
  * `aiplatform.pipelineJobs.delete`
  * `aiplatform.pipelineJobs.get`
  * `aiplatform.pipelineJobs.list`

`aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.get` `aiplatform.provisionedThroughputs.list` `aiplatform.ragCorpora.*`

  * `aiplatform.ragCorpora.create`
  * `aiplatform.ragCorpora.delete`
  * `aiplatform.ragCorpora.get`
  * `aiplatform.ragCorpora.list`
  * `aiplatform.ragCorpora.query`
  * `aiplatform.ragCorpora.update`

`aiplatform.ragEngineConfigs.get` `aiplatform.ragFiles.*`

  * `aiplatform.ragFiles.delete`
  * `aiplatform.ragFiles.get`
  * `aiplatform.ragFiles.import`
  * `aiplatform.ragFiles.list`
  * `aiplatform.ragFiles.upload`

`aiplatform.reasoningEngineRuntimeRevisions.*`

  * `aiplatform.reasoningEngineRuntimeRevisions.delete`
  * `aiplatform.reasoningEngineRuntimeRevisions.get`
  * `aiplatform.reasoningEngineRuntimeRevisions.list`
  * `aiplatform.reasoningEngineRuntimeRevisions.query`

`aiplatform.reasoningEngines.create` `aiplatform.reasoningEngines.delete` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.reasoningEngines.update` `aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`aiplatform.semanticGovernancePolicies.*`

  * `aiplatform.semanticGovernancePolicies.create`
  * `aiplatform.semanticGovernancePolicies.delete`
  * `aiplatform.semanticGovernancePolicies.get`
  * `aiplatform.semanticGovernancePolicies.list`
  * `aiplatform.semanticGovernancePolicies.update`

`aiplatform.semanticGovernancePolicyEngine.*`

  * `aiplatform.semanticGovernancePolicyEngine.get`
  * `aiplatform.semanticGovernancePolicyEngine.update`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.*`

  * `aiplatform.sessions.create`
  * `aiplatform.sessions.delete`
  * `aiplatform.sessions.get`
  * `aiplatform.sessions.list`
  * `aiplatform.sessions.run`
  * `aiplatform.sessions.update`

`aiplatform.specialistPools.*`

  * `aiplatform.specialistPools.create`
  * `aiplatform.specialistPools.delete`
  * `aiplatform.specialistPools.get`
  * `aiplatform.specialistPools.list`
  * `aiplatform.specialistPools.update`

`aiplatform.studies.*`

  * `aiplatform.studies.create`
  * `aiplatform.studies.delete`
  * `aiplatform.studies.get`
  * `aiplatform.studies.list`
  * `aiplatform.studies.update`

`aiplatform.tasks.*`

  * `aiplatform.tasks.cancel`
  * `aiplatform.tasks.create`
  * `aiplatform.tasks.delete`
  * `aiplatform.tasks.get`
  * `aiplatform.tasks.list`
  * `aiplatform.tasks.update`

`aiplatform.tensorboardExperiments.*`

  * `aiplatform.tensorboardExperiments.create`
  * `aiplatform.tensorboardExperiments.delete`
  * `aiplatform.tensorboardExperiments.get`
  * `aiplatform.tensorboardExperiments.list`
  * `aiplatform.tensorboardExperiments.update`
  * `aiplatform.tensorboardExperiments.write`

`aiplatform.tensorboardRuns.*`

  * `aiplatform.tensorboardRuns.batchCreate`
  * `aiplatform.tensorboardRuns.create`
  * `aiplatform.tensorboardRuns.delete`
  * `aiplatform.tensorboardRuns.get`
  * `aiplatform.tensorboardRuns.list`
  * `aiplatform.tensorboardRuns.update`
  * `aiplatform.tensorboardRuns.write`

`aiplatform.tensorboardTimeSeries.*`

  * `aiplatform.tensorboardTimeSeries.batchCreate`
  * `aiplatform.tensorboardTimeSeries.batchRead`
  * `aiplatform.tensorboardTimeSeries.create`
  * `aiplatform.tensorboardTimeSeries.delete`
  * `aiplatform.tensorboardTimeSeries.get`
  * `aiplatform.tensorboardTimeSeries.list`
  * `aiplatform.tensorboardTimeSeries.read`
  * `aiplatform.tensorboardTimeSeries.update`

`aiplatform.tensorboards.create` `aiplatform.tensorboards.delete` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.tensorboards.update` `aiplatform.trainingPipelines.*`

  * `aiplatform.trainingPipelines.cancel`
  * `aiplatform.trainingPipelines.create`
  * `aiplatform.trainingPipelines.delete`
  * `aiplatform.trainingPipelines.get`
  * `aiplatform.trainingPipelines.list`

`aiplatform.trials.*`

  * `aiplatform.trials.create`
  * `aiplatform.trials.delete`
  * `aiplatform.trials.get`
  * `aiplatform.trials.list`
  * `aiplatform.trials.update`

`aiplatform.tuningJobs.*`

  * `aiplatform.tuningJobs.cancel`
  * `aiplatform.tuningJobs.create`
  * `aiplatform.tuningJobs.delete`
  * `aiplatform.tuningJobs.get`
  * `aiplatform.tuningJobs.list`
  * `aiplatform.tuningJobs.optimizePrompt`
  * `aiplatform.tuningJobs.validateReinforcementTuningReward`
  * `aiplatform.tuningJobs.vertexTune`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Viewer 

(`roles/aiplatform.viewer`) Grants access to view all resource in Agent Platform.  |  `aiplatform.agentAnomalyDetectionScopes.get` `aiplatform.agentAnomalyDetectionScopes.list` `aiplatform.agentExamples.get` `aiplatform.agentExamples.list` `aiplatform.agents.get` `aiplatform.agents.list` `aiplatform.analyzedInvocations.*`

  * `aiplatform.analyzedInvocations.get`
  * `aiplatform.analyzedInvocations.list`

`aiplatform.analyzedSessions.*`

  * `aiplatform.analyzedSessions.aggregate`
  * `aiplatform.analyzedSessions.get`
  * `aiplatform.analyzedSessions.list`

`aiplatform.annotationSpecs.get` `aiplatform.annotationSpecs.list` `aiplatform.annotations.get` `aiplatform.annotations.list` `aiplatform.apps.get` `aiplatform.apps.list` `aiplatform.artifacts.get` `aiplatform.artifacts.list` `aiplatform.batchPredictionJobs.get` `aiplatform.batchPredictionJobs.list` `aiplatform.cacheConfigs.get` `aiplatform.cachedContents.get` `aiplatform.cachedContents.list` `aiplatform.consents.get` `aiplatform.contexts.get` `aiplatform.contexts.list` `aiplatform.contexts.queryContextLineageSubgraph` `aiplatform.customJobs.get` `aiplatform.customJobs.list` `aiplatform.dataItems.get` `aiplatform.dataItems.list` `aiplatform.dataLabelingJobs.get` `aiplatform.dataLabelingJobs.list` `aiplatform.datasetVersions.get` `aiplatform.datasetVersions.list` `aiplatform.datasets.get` `aiplatform.datasets.list` `aiplatform.deploymentResourcePools.get` `aiplatform.deploymentResourcePools.list` `aiplatform.deploymentResourcePools.queryDeployedModels` `aiplatform.edgeDeploymentJobs.get` `aiplatform.edgeDeploymentJobs.list` `aiplatform.edgeDeviceDebugInfo.get` `aiplatform.edgeDevices.get` `aiplatform.edgeDevices.list` `aiplatform.endpoints.explain` `aiplatform.endpoints.get` `aiplatform.endpoints.getIamPolicy` `aiplatform.endpoints.list` `aiplatform.entityTypes.get` `aiplatform.entityTypes.getIamPolicy` `aiplatform.entityTypes.list` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.evaluationExperiments.get` `aiplatform.evaluationExperiments.list` `aiplatform.evaluationItems.get` `aiplatform.evaluationItems.list` `aiplatform.evaluationMetrics.get` `aiplatform.evaluationMetrics.list` `aiplatform.evaluationRuns.get` `aiplatform.evaluationRuns.list` `aiplatform.evaluationSets.get` `aiplatform.evaluationSets.list` `aiplatform.exampleStores.get` `aiplatform.exampleStores.list` `aiplatform.exampleStores.readExample` `aiplatform.executions.get` `aiplatform.executions.list` `aiplatform.executions.queryExecutionInputsAndOutputs` `aiplatform.extensions.get` `aiplatform.extensions.list` `aiplatform.featureGroups.get` `aiplatform.featureGroups.getIamPolicy` `aiplatform.featureGroups.list` `aiplatform.featureMonitorJobs.get` `aiplatform.featureMonitorJobs.list` `aiplatform.featureMonitors.get` `aiplatform.featureMonitors.list` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.getIamPolicy` `aiplatform.featureOnlineStores.list` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.getIamPolicy` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.features.get` `aiplatform.features.list` `aiplatform.featurestores.get` `aiplatform.featurestores.getIamPolicy` `aiplatform.featurestores.list` `aiplatform.featurestores.readFeatures` `aiplatform.humanInTheLoops.get` `aiplatform.humanInTheLoops.list` `aiplatform.humanInTheLoops.queryAnnotationStats` `aiplatform.hyperparameterTuningJobs.get` `aiplatform.hyperparameterTuningJobs.list` `aiplatform.indexEndpoints.get` `aiplatform.indexEndpoints.list` `aiplatform.indexEndpoints.queryVectors` `aiplatform.indexes.get` `aiplatform.indexes.list` `aiplatform.interactions.get` `aiplatform.interactions.list` `aiplatform.locations.*`

  * `aiplatform.locations.evaluateInstances`
  * `aiplatform.locations.get`
  * `aiplatform.locations.list`

`aiplatform.memories.get` `aiplatform.memories.list` `aiplatform.memoryRevisions.get` `aiplatform.memoryRevisions.list` `aiplatform.metadataSchemas.get` `aiplatform.metadataSchemas.list` `aiplatform.metadataStores.get` `aiplatform.metadataStores.list` `aiplatform.migratableResources.search` `aiplatform.modelDeploymentMonitoringJobs.get` `aiplatform.modelDeploymentMonitoringJobs.list` `aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies` `aiplatform.modelEvaluationSlices.get` `aiplatform.modelEvaluationSlices.list` `aiplatform.modelEvaluations.get` `aiplatform.modelEvaluations.list` `aiplatform.modelMonitoringJobs.get` `aiplatform.modelMonitoringJobs.list` `aiplatform.modelMonitors.get` `aiplatform.modelMonitors.list` `aiplatform.modelMonitors.searchModelMonitoringAlerts` `aiplatform.modelMonitors.searchModelMonitoringStats` `aiplatform.models.get` `aiplatform.models.list` `aiplatform.monitoredAgents.get` `aiplatform.monitoredAgents.list` `aiplatform.nasJobs.get` `aiplatform.nasJobs.list` `aiplatform.nasTrialDetails.*`

  * `aiplatform.nasTrialDetails.get`
  * `aiplatform.nasTrialDetails.list`

`aiplatform.notebookExecutionJobs.get` `aiplatform.notebookExecutionJobs.list` `aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimes.get` `aiplatform.notebookRuntimes.list` `aiplatform.onlineEvaluators.get` `aiplatform.onlineEvaluators.list` `aiplatform.operations.list` `aiplatform.persistentResources.get` `aiplatform.persistentResources.list` `aiplatform.pipelineJobs.get` `aiplatform.pipelineJobs.list` `aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.get` `aiplatform.provisionedThroughputs.list` `aiplatform.ragCorpora.get` `aiplatform.ragCorpora.list` `aiplatform.ragCorpora.query` `aiplatform.ragEngineConfigs.get` `aiplatform.ragFiles.get` `aiplatform.ragFiles.list` `aiplatform.reasoningEngineRuntimeRevisions.get` `aiplatform.reasoningEngineRuntimeRevisions.list` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.sandboxEnvironments.get` `aiplatform.sandboxEnvironments.list` `aiplatform.schedules.get` `aiplatform.schedules.list` `aiplatform.semanticGovernancePolicies.get` `aiplatform.semanticGovernancePolicies.list` `aiplatform.semanticGovernancePolicyEngine.get` `aiplatform.sessionEvents.list` `aiplatform.sessions.get` `aiplatform.sessions.list` `aiplatform.specialistPools.get` `aiplatform.specialistPools.list` `aiplatform.specialistPools.update` `aiplatform.studies.get` `aiplatform.studies.list` `aiplatform.tasks.get` `aiplatform.tasks.list` `aiplatform.tensorboardExperiments.get` `aiplatform.tensorboardExperiments.list` `aiplatform.tensorboardRuns.get` `aiplatform.tensorboardRuns.list` `aiplatform.tensorboardTimeSeries.batchRead` `aiplatform.tensorboardTimeSeries.get` `aiplatform.tensorboardTimeSeries.list` `aiplatform.tensorboardTimeSeries.read` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.trainingPipelines.get` `aiplatform.trainingPipelines.list` `aiplatform.trials.get` `aiplatform.trials.list` `aiplatform.tuningJobs.get` `aiplatform.tuningJobs.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Agents Admin Role Beta

(`roles/aiplatform.agentsAdmin`) Grants full administrative access to Agent Platform agents, including reading and managing their memories and their access control policies.  |  `aiplatform.agentMemories.*`

  * `aiplatform.agentMemories.delete`
  * `aiplatform.agentMemories.get`
  * `aiplatform.agentMemories.list`
  * `aiplatform.agentMemories.undelete`
  * `aiplatform.agentMemories.update`

`aiplatform.agents.*`

  * `aiplatform.agents.create`
  * `aiplatform.agents.delete`
  * `aiplatform.agents.get`
  * `aiplatform.agents.getIamPolicy`
  * `aiplatform.agents.list`
  * `aiplatform.agents.suspend`
  * `aiplatform.agents.unsuspend`
  * `aiplatform.agents.update`

`aiplatform.tasks.delete`  
  
#### Agent Platform Agents Creator Role Beta

(`roles/aiplatform.agentsCreator`) Grants access to create and discover Agent Platform agents and their auth providers.  |  `aiplatform.agents.create` `aiplatform.agents.list`  
  
#### Agent Platform Agents User Role Beta

(`roles/aiplatform.agentsUser`) Grants access to view agents and to create, update, and delete their tasks.  |  `aiplatform.agents.get` `aiplatform.agents.list` `aiplatform.tasks.create` `aiplatform.tasks.delete` `aiplatform.tasks.get` `aiplatform.tasks.list` `aiplatform.tasks.update`  
  
#### Agent Platform Agents Viewer Role Beta

(`roles/aiplatform.agentsViewer`) Grants read-only access to Agent Platform agents.  |  `aiplatform.agents.get` `aiplatform.agents.list`  
  
#### Colab Enterprise Admin 

(`roles/aiplatform.colabEnterpriseAdmin`) Admin role of using colab enterprise.  |  `aiplatform.locations.get` `aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.*`

  * `aiplatform.notebookRuntimeTemplates.apply`
  * `aiplatform.notebookRuntimeTemplates.create`
  * `aiplatform.notebookRuntimeTemplates.delete`
  * `aiplatform.notebookRuntimeTemplates.get`
  * `aiplatform.notebookRuntimeTemplates.getIamPolicy`
  * `aiplatform.notebookRuntimeTemplates.list`
  * `aiplatform.notebookRuntimeTemplates.setDefault`
  * `aiplatform.notebookRuntimeTemplates.setIamPolicy`
  * `aiplatform.notebookRuntimeTemplates.update`

`aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.operations.list` `aiplatform.pipelineJobs.create` `aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`compute.reservations.get` `compute.reservations.list` `dataform.*`

  * `dataform.commentThreads.create`
  * `dataform.commentThreads.delete`
  * `dataform.commentThreads.get`
  * `dataform.commentThreads.list`
  * `dataform.commentThreads.update`
  * `dataform.comments.create`
  * `dataform.comments.delete`
  * `dataform.comments.get`
  * `dataform.comments.list`
  * `dataform.comments.update`
  * `dataform.compilationResults.create`
  * `dataform.compilationResults.get`
  * `dataform.compilationResults.list`
  * `dataform.compilationResults.query`
  * `dataform.config.get`
  * `dataform.config.update`
  * `dataform.folders.addContents`
  * `dataform.folders.create`
  * `dataform.folders.delete`
  * `dataform.folders.deleteTree`
  * `dataform.folders.get`
  * `dataform.folders.getIamPolicy`
  * `dataform.folders.move`
  * `dataform.folders.queryContents`
  * `dataform.folders.setIamPolicy`
  * `dataform.folders.update`
  * `dataform.locations.get`
  * `dataform.locations.list`
  * `dataform.operations.cancel`
  * `dataform.operations.delete`
  * `dataform.operations.get`
  * `dataform.operations.list`
  * `dataform.releaseConfigs.create`
  * `dataform.releaseConfigs.delete`
  * `dataform.releaseConfigs.get`
  * `dataform.releaseConfigs.list`
  * `dataform.releaseConfigs.update`
  * `dataform.repositories.commit`
  * `dataform.repositories.computeAccessTokenStatus`
  * `dataform.repositories.create`
  * `dataform.repositories.createTagBinding`
  * `dataform.repositories.delete`
  * `dataform.repositories.deleteTagBinding`
  * `dataform.repositories.fetchHistory`
  * `dataform.repositories.fetchRemoteBranches`
  * `dataform.repositories.get`
  * `dataform.repositories.getIamPolicy`
  * `dataform.repositories.list`
  * `dataform.repositories.listEffectiveTags`
  * `dataform.repositories.listTagBindings`
  * `dataform.repositories.move`
  * `dataform.repositories.queryDirectoryContents`
  * `dataform.repositories.readFile`
  * `dataform.repositories.scheduleRelease`
  * `dataform.repositories.scheduleWorkflow`
  * `dataform.repositories.setIamPolicy`
  * `dataform.repositories.update`
  * `dataform.teamFolders.create`
  * `dataform.teamFolders.delete`
  * `dataform.teamFolders.deleteTree`
  * `dataform.teamFolders.get`
  * `dataform.teamFolders.getIamPolicy`
  * `dataform.teamFolders.setIamPolicy`
  * `dataform.teamFolders.update`
  * `dataform.workflowConfigs.create`
  * `dataform.workflowConfigs.delete`
  * `dataform.workflowConfigs.get`
  * `dataform.workflowConfigs.list`
  * `dataform.workflowConfigs.update`
  * `dataform.workflowInvocations.cancel`
  * `dataform.workflowInvocations.create`
  * `dataform.workflowInvocations.delete`
  * `dataform.workflowInvocations.get`
  * `dataform.workflowInvocations.list`
  * `dataform.workflowInvocations.query`
  * `dataform.workspaces.commit`
  * `dataform.workspaces.create`
  * `dataform.workspaces.delete`
  * `dataform.workspaces.fetchFileDiff`
  * `dataform.workspaces.fetchFileGitStatuses`
  * `dataform.workspaces.fetchGitAheadBehind`
  * `dataform.workspaces.get`
  * `dataform.workspaces.getIamPolicy`
  * `dataform.workspaces.installNpmPackages`
  * `dataform.workspaces.list`
  * `dataform.workspaces.makeDirectory`
  * `dataform.workspaces.moveDirectory`
  * `dataform.workspaces.moveFile`
  * `dataform.workspaces.pull`
  * `dataform.workspaces.push`
  * `dataform.workspaces.queryDirectoryContents`
  * `dataform.workspaces.readFile`
  * `dataform.workspaces.removeDirectory`
  * `dataform.workspaces.removeFile`
  * `dataform.workspaces.reset`
  * `dataform.workspaces.searchFiles`
  * `dataform.workspaces.setIamPolicy`
  * `dataform.workspaces.writeFile`

`developerconnect.connections.constructGitHubAppManifest` `developerconnect.connections.create` `developerconnect.connections.delete` `developerconnect.connections.fetchGitHubInstallations` `developerconnect.connections.fetchLinkableGitRepositories` `developerconnect.connections.generateGitHubStateToken` `developerconnect.connections.get` `developerconnect.connections.list` `developerconnect.connections.processGitHubAppCreationCallback` `developerconnect.connections.processGitHubOAuthCallback` `developerconnect.connections.update` `developerconnect.gitRepositoryLinks.*`

  * `developerconnect.gitRepositoryLinks.create`
  * `developerconnect.gitRepositoryLinks.delete`
  * `developerconnect.gitRepositoryLinks.fetchGitRefs`
  * `developerconnect.gitRepositoryLinks.fetchReadToken`
  * `developerconnect.gitRepositoryLinks.fetchReadWriteToken`
  * `developerconnect.gitRepositoryLinks.get`
  * `developerconnect.gitRepositoryLinks.gitProxyRead`
  * `developerconnect.gitRepositoryLinks.gitProxyWrite`
  * `developerconnect.gitRepositoryLinks.list`

`developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.*`

  * `developerconnect.operations.cancel`
  * `developerconnect.operations.delete`
  * `developerconnect.operations.get`
  * `developerconnect.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Colab Enterprise User 

(`roles/aiplatform.colabEnterpriseUser`) User role of using colab enterprise.  |  `aiplatform.locations.get` `aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimes.assign` `aiplatform.notebookRuntimes.get` `aiplatform.notebookRuntimes.list` `aiplatform.operations.list` `aiplatform.pipelineJobs.create` `aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`dataform.commentThreads.get` `dataform.commentThreads.list` `dataform.comments.get` `dataform.comments.list` `dataform.folders.create` `dataform.locations.*`

  * `dataform.locations.get`
  * `dataform.locations.list`

`dataform.repositories.create` `dataform.repositories.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Feature Store EntityType owner 

(`roles/aiplatform.entityTypeOwner`) Provides full access to all permissions for a particular entity type resource.  Lowest-level resources where you can grant this role:

  * Entity type

|  `aiplatform.entityTypes.delete` `aiplatform.entityTypes.deleteFeatureValues` `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.getIamPolicy` `aiplatform.entityTypes.importFeatureValues` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.setIamPolicy` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.entityTypes.update` `aiplatform.entityTypes.writeFeatureValues` `aiplatform.featureGroups.get` `aiplatform.featureGroups.list` `aiplatform.featureMonitorJobs.get` `aiplatform.featureMonitorJobs.list` `aiplatform.featureMonitors.get` `aiplatform.featureMonitors.list` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.list` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.batchReadFeatureValues` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Express Admin Beta

(`roles/aiplatform.expressAdmin`) Grants admin access to Agent Platform Express.  |  `aiplatform.batchPredictionJobs.*`

  * `aiplatform.batchPredictionJobs.cancel`
  * `aiplatform.batchPredictionJobs.create`
  * `aiplatform.batchPredictionJobs.delete`
  * `aiplatform.batchPredictionJobs.get`
  * `aiplatform.batchPredictionJobs.list`

`aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.create` `aiplatform.datasets.delete` `aiplatform.datasets.get` `aiplatform.datasets.list` `aiplatform.datasets.update` `aiplatform.endpoints.predict` `aiplatform.locations.evaluateInstances` `aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.operations.list` `aiplatform.reasoningEngines.create` `aiplatform.reasoningEngines.delete` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.reasoningEngines.update` `aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.create` `aiplatform.sessions.delete` `aiplatform.sessions.get` `aiplatform.sessions.list` `aiplatform.sessions.update`  
  
#### Agent Platform Feature Store Admin 

(`roles/aiplatform.featurestoreAdmin`) Grants full access to all resources in Agent Platform Feature Store.  Lowest-level resources where you can grant this role:

  * Entity type

|  `aiplatform.entityTypes.*`

  * `aiplatform.entityTypes.create`
  * `aiplatform.entityTypes.delete`
  * `aiplatform.entityTypes.deleteFeatureValues`
  * `aiplatform.entityTypes.exportFeatureValues`
  * `aiplatform.entityTypes.get`
  * `aiplatform.entityTypes.getIamPolicy`
  * `aiplatform.entityTypes.importFeatureValues`
  * `aiplatform.entityTypes.list`
  * `aiplatform.entityTypes.readFeatureValues`
  * `aiplatform.entityTypes.setIamPolicy`
  * `aiplatform.entityTypes.streamingReadFeatureValues`
  * `aiplatform.entityTypes.update`
  * `aiplatform.entityTypes.writeFeatureValues`

`aiplatform.featureGroups.*`

  * `aiplatform.featureGroups.create`
  * `aiplatform.featureGroups.delete`
  * `aiplatform.featureGroups.get`
  * `aiplatform.featureGroups.getIamPolicy`
  * `aiplatform.featureGroups.list`
  * `aiplatform.featureGroups.setIamPolicy`
  * `aiplatform.featureGroups.update`

`aiplatform.featureMonitorJobs.*`

  * `aiplatform.featureMonitorJobs.create`
  * `aiplatform.featureMonitorJobs.get`
  * `aiplatform.featureMonitorJobs.list`

`aiplatform.featureMonitors.*`

  * `aiplatform.featureMonitors.create`
  * `aiplatform.featureMonitors.delete`
  * `aiplatform.featureMonitors.get`
  * `aiplatform.featureMonitors.list`
  * `aiplatform.featureMonitors.update`

`aiplatform.featureOnlineStores.*`

  * `aiplatform.featureOnlineStores.create`
  * `aiplatform.featureOnlineStores.delete`
  * `aiplatform.featureOnlineStores.get`
  * `aiplatform.featureOnlineStores.getIamPolicy`
  * `aiplatform.featureOnlineStores.list`
  * `aiplatform.featureOnlineStores.setIamPolicy`
  * `aiplatform.featureOnlineStores.update`

`aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.*`

  * `aiplatform.featureViews.create`
  * `aiplatform.featureViews.delete`
  * `aiplatform.featureViews.directWrite`
  * `aiplatform.featureViews.fetchFeatureValues`
  * `aiplatform.featureViews.get`
  * `aiplatform.featureViews.getIamPolicy`
  * `aiplatform.featureViews.list`
  * `aiplatform.featureViews.searchNearestEntities`
  * `aiplatform.featureViews.setIamPolicy`
  * `aiplatform.featureViews.sync`
  * `aiplatform.featureViews.update`

`aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.*`

  * `aiplatform.featurestores.batchReadFeatureValues`
  * `aiplatform.featurestores.create`
  * `aiplatform.featurestores.delete`
  * `aiplatform.featurestores.exportFeatures`
  * `aiplatform.featurestores.get`
  * `aiplatform.featurestores.getIamPolicy`
  * `aiplatform.featurestores.importFeatures`
  * `aiplatform.featurestores.list`
  * `aiplatform.featurestores.readFeatures`
  * `aiplatform.featurestores.setIamPolicy`
  * `aiplatform.featurestores.update`
  * `aiplatform.featurestores.writeFeatures`

`aiplatform.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Feature Store Data Viewer 

(`roles/aiplatform.featurestoreDataViewer`) This role provides permissions to read Feature data.  Lowest-level resources where you can grant this role:

  * Entity type

|  `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.featureGroups.get` `aiplatform.featureGroups.list` `aiplatform.featureMonitorJobs.get` `aiplatform.featureMonitorJobs.list` `aiplatform.featureMonitors.get` `aiplatform.featureMonitors.list` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.list` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.features.get` `aiplatform.features.list` `aiplatform.featurestores.batchReadFeatureValues` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Feature Store Data Writer 

(`roles/aiplatform.featurestoreDataWriter`) This role provides permissions to read and write Feature data.  Lowest-level resources where you can grant this role:

  * Entity type

|  `aiplatform.entityTypes.deleteFeatureValues` `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.importFeatureValues` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.entityTypes.writeFeatureValues` `aiplatform.featureGroups.get` `aiplatform.featureGroups.list` `aiplatform.featureMonitorJobs.get` `aiplatform.featureMonitorJobs.list` `aiplatform.featureMonitors.get` `aiplatform.featureMonitors.list` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.list` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.features.get` `aiplatform.features.list` `aiplatform.featurestores.batchReadFeatureValues` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Feature Store Instance Creator 

(`roles/aiplatform.featurestoreInstanceCreator`) Administrator of Featurestore resources, but not the child resources under Featurestores.  Lowest-level resources where you can grant this role:

  * Featurestore

|  `aiplatform.featurestores.create` `aiplatform.featurestores.delete` `aiplatform.featurestores.get` `aiplatform.featurestores.list` `aiplatform.featurestores.update`  
  
#### Agent Platform Feature Store Resource Viewer 

(`roles/aiplatform.featurestoreResourceViewer`) Viewer of all resources in Agent Platform Feature Store but cannot make changes.  Lowest-level resources where you can grant this role:

  * Entity type

|  `aiplatform.entityTypes.get` `aiplatform.entityTypes.list` `aiplatform.featureGroups.get` `aiplatform.featureGroups.list` `aiplatform.featureMonitorJobs.get` `aiplatform.featureMonitorJobs.list` `aiplatform.featureMonitors.get` `aiplatform.featureMonitors.list` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.list` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.get` `aiplatform.featureViews.list` `aiplatform.features.get` `aiplatform.features.list` `aiplatform.featurestores.get` `aiplatform.featurestores.list` `aiplatform.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Feature Store User Beta

(`roles/aiplatform.featurestoreUser`) Deprecated. Use featurestoreAdmin instead.  |  `aiplatform.entityTypes.*`

  * `aiplatform.entityTypes.create`
  * `aiplatform.entityTypes.delete`
  * `aiplatform.entityTypes.deleteFeatureValues`
  * `aiplatform.entityTypes.exportFeatureValues`
  * `aiplatform.entityTypes.get`
  * `aiplatform.entityTypes.getIamPolicy`
  * `aiplatform.entityTypes.importFeatureValues`
  * `aiplatform.entityTypes.list`
  * `aiplatform.entityTypes.readFeatureValues`
  * `aiplatform.entityTypes.setIamPolicy`
  * `aiplatform.entityTypes.streamingReadFeatureValues`
  * `aiplatform.entityTypes.update`
  * `aiplatform.entityTypes.writeFeatureValues`

`aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.*`

  * `aiplatform.featurestores.batchReadFeatureValues`
  * `aiplatform.featurestores.create`
  * `aiplatform.featurestores.delete`
  * `aiplatform.featurestores.exportFeatures`
  * `aiplatform.featurestores.get`
  * `aiplatform.featurestores.getIamPolicy`
  * `aiplatform.featurestores.importFeatures`
  * `aiplatform.featurestores.list`
  * `aiplatform.featurestores.readFeatures`
  * `aiplatform.featurestores.setIamPolicy`
  * `aiplatform.featurestores.update`
  * `aiplatform.featurestores.writeFeatures`

`aiplatform.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Agent Platform Memory Bank Editor Role 

(`roles/aiplatform.memoryEditor`) Grants edit access to Agent Platform Memory Bank.  |  `aiplatform.memories.create` `aiplatform.memories.delete` `aiplatform.memories.generate` `aiplatform.memories.update` `aiplatform.memoryRevisions.rollback`  
  
#### Agent Platform Memory Bank User Role 

(`roles/aiplatform.memoryUser`) Grants full user access to Agent Platform Memory Bank.  |  `aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.memoryRevisions.*`

  * `aiplatform.memoryRevisions.get`
  * `aiplatform.memoryRevisions.list`
  * `aiplatform.memoryRevisions.rollback`

  
  
#### Agent Platform Memory Bank Viewer Role 

(`roles/aiplatform.memoryViewer`) Grants viewer access to Agent Platform Memory Bank.  |  `aiplatform.memories.get` `aiplatform.memories.list` `aiplatform.memories.retrieve` `aiplatform.memoryRevisions.get` `aiplatform.memoryRevisions.list`  
  
#### Agent Platform Migration Service User 

(`roles/aiplatform.migrator`) Grants access to use migration service in Agent Platform  |  `aiplatform.migratableResources.*`

  * `aiplatform.migratableResources.migrate`
  * `aiplatform.migratableResources.search`

  
  
#### Notebook Executor User Beta

(`roles/aiplatform.notebookExecutorUser`) Grants users full access to schedules and notebook execution jobs.  |  `aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.operations.list` `aiplatform.pipelineJobs.create` `aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

  
  
#### Notebook Runtime Admin 

(`roles/aiplatform.notebookRuntimeAdmin`) Grants full access to all runtime templates and runtimes in Notebook Service.  |  `aiplatform.locations.get` `aiplatform.notebookRuntimeTemplates.*`

  * `aiplatform.notebookRuntimeTemplates.apply`
  * `aiplatform.notebookRuntimeTemplates.create`
  * `aiplatform.notebookRuntimeTemplates.delete`
  * `aiplatform.notebookRuntimeTemplates.get`
  * `aiplatform.notebookRuntimeTemplates.getIamPolicy`
  * `aiplatform.notebookRuntimeTemplates.list`
  * `aiplatform.notebookRuntimeTemplates.setDefault`
  * `aiplatform.notebookRuntimeTemplates.setIamPolicy`
  * `aiplatform.notebookRuntimeTemplates.update`

`aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.operations.list` `compute.reservations.get` `compute.reservations.list`  
  
#### Notebook Runtime User 

(`roles/aiplatform.notebookRuntimeUser`) Grants users permissions to create runtime resources using a runtime template and manage the runtime resources they created.  |  `aiplatform.locations.get` `aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimes.assign` `aiplatform.notebookRuntimes.get` `aiplatform.notebookRuntimes.list` `aiplatform.operations.list`  
  
#### Vertex AI Platform Provisioned Throughput Admin Beta

(`roles/aiplatform.provisionedThroughputAdmin`) Grants access to use all resources related to Vertex AI Provisioned Throughput  |  `aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.*`

  * `aiplatform.provisionedThroughputs.cancel`
  * `aiplatform.provisionedThroughputs.changeScope`
  * `aiplatform.provisionedThroughputs.create`
  * `aiplatform.provisionedThroughputs.get`
  * `aiplatform.provisionedThroughputs.list`
  * `aiplatform.provisionedThroughputs.split`
  * `aiplatform.provisionedThroughputs.update`

  
  
#### Vertex AI Platform Publisher Provisioned Throughput Admin Beta

(`roles/aiplatform.publisherProvisionedThroughputAdmin`) Grants Publisher access to use all resources related to Vertex AI Provisioned Throughput Orders  |   
  
#### Vertex AI Platform Publisher Provisioned Throughput Viewer Beta

(`roles/aiplatform.publisherProvisionedThroughputViewer`) Grants Publisher access to view all resources related to Vertex AI Provisioned Throughput Orders  |   
  
#### Agent Platform Sessions Editor Role 

(`roles/aiplatform.sessionEditor`) Grants edit access to Agent Platform Sessions.  |  `aiplatform.sessionEvents.append` `aiplatform.sessions.create` `aiplatform.sessions.delete` `aiplatform.sessions.update`  
  
#### Agent Platform Sessions User Role 

(`roles/aiplatform.sessionUser`) Grants full user access to Agent Platform Sessions.  |  `aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.create` `aiplatform.sessions.delete` `aiplatform.sessions.get` `aiplatform.sessions.list` `aiplatform.sessions.update`  
  
#### Agent Platform Sessions Viewer Role 

(`roles/aiplatform.sessionViewer`) Grants viewer access to Agent Platform Sessions  |  `aiplatform.sessionEvents.list` `aiplatform.sessions.get` `aiplatform.sessions.list`  
  
#### Agent Platform Tensorboard Web App User Beta

(`roles/aiplatform.tensorboardWebAppUser`) Grants access to the Vertex AI TensorBoard web app.  |  `aiplatform.tensorboards.recordAccess`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Vertex AI Agent Sandbox Service Agent 

(`roles/aiplatform.agentSandboxServiceAgent`) Vertex AI Service Agent used to access Agent Sandbox managed resources in consumer project with restricted permissions.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.repositories.downloadArtifacts` `logging.logEntries.create` `logging.logEntries.route` `serviceusage.services.use` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list`  
  
#### Vertex AI Batch Prediction Service Agent 

(`roles/aiplatform.batchPredictionServiceAgent`) Vertex AI Batch Prediction Service Agent for serving batch prediction requests.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.models.create` `bigquery.models.export` `bigquery.models.getData` `bigquery.readsessions.create` `bigquery.readsessions.getData` `bigquery.tables.create` `bigquery.tables.createSnapshot` `bigquery.tables.deleteSnapshot` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.restoreSnapshot` `bigquery.tables.update` `bigquery.tables.updateData` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Vertex AI Colab Service Agent 

(`roles/aiplatform.colabServiceAgent`) Gives Vertex AI Colab the proper permissions to function.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.notebookExecutionJobs.create` `compute.addresses.get` `compute.addresses.list` `compute.addresses.use` `compute.addresses.useInternal` `compute.disks.create` `compute.disks.createSnapshot` `compute.disks.createTagBinding` `compute.disks.delete` `compute.disks.get` `compute.disks.setLabels` `compute.disks.use` `compute.disks.useReadOnly` `compute.globalOperations.get` `compute.instances.attachDisk` `compute.instances.create` `compute.instances.createTagBinding` `compute.instances.delete` `compute.instances.detachDisk` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.reset` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setServiceAccount` `compute.instances.setTags` `compute.instances.start` `compute.instances.stop` `compute.instances.useReadOnly` `compute.networks.get` `compute.networks.use` `compute.networks.useExternalIp` `compute.snapshots.create` `compute.snapshots.delete` `compute.snapshots.useReadOnly` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `compute.zoneOperations.list` `iam.serviceAccounts.actAs` `notebooks.instances.create` `notebooks.instances.delete` `notebooks.instances.get`  
  
#### Vertex AI Custom Code Service Agent 

(`roles/aiplatform.customCodeServiceAgent`) Gives Vertex AI Custom Code the proper permissions. The aiplatform.customJobs.create IAM permission is highly privileged. Through Vertex AI Custom Training jobs, it effectively grants editor-level access to other services activated for the consumer project, such as GCS and BigQuery.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.agentAnomalyDetectionScopes.*`

  * `aiplatform.agentAnomalyDetectionScopes.create`
  * `aiplatform.agentAnomalyDetectionScopes.delete`
  * `aiplatform.agentAnomalyDetectionScopes.get`
  * `aiplatform.agentAnomalyDetectionScopes.list`

`aiplatform.agentExamples.*`

  * `aiplatform.agentExamples.create`
  * `aiplatform.agentExamples.delete`
  * `aiplatform.agentExamples.get`
  * `aiplatform.agentExamples.list`
  * `aiplatform.agentExamples.update`

`aiplatform.agents.create` `aiplatform.agents.delete` `aiplatform.agents.get` `aiplatform.agents.list` `aiplatform.agents.update` `aiplatform.analyzedInvocations.*`

  * `aiplatform.analyzedInvocations.get`
  * `aiplatform.analyzedInvocations.list`

`aiplatform.analyzedSessions.*`

  * `aiplatform.analyzedSessions.aggregate`
  * `aiplatform.analyzedSessions.get`
  * `aiplatform.analyzedSessions.list`

`aiplatform.annotationSpecs.*`

  * `aiplatform.annotationSpecs.create`
  * `aiplatform.annotationSpecs.delete`
  * `aiplatform.annotationSpecs.get`
  * `aiplatform.annotationSpecs.list`
  * `aiplatform.annotationSpecs.update`

`aiplatform.annotations.*`

  * `aiplatform.annotations.create`
  * `aiplatform.annotations.delete`
  * `aiplatform.annotations.get`
  * `aiplatform.annotations.list`
  * `aiplatform.annotations.update`

`aiplatform.apps.*`

  * `aiplatform.apps.create`
  * `aiplatform.apps.delete`
  * `aiplatform.apps.get`
  * `aiplatform.apps.list`
  * `aiplatform.apps.update`

`aiplatform.artifacts.*`

  * `aiplatform.artifacts.create`
  * `aiplatform.artifacts.delete`
  * `aiplatform.artifacts.get`
  * `aiplatform.artifacts.list`
  * `aiplatform.artifacts.update`

`aiplatform.batchPredictionJobs.*`

  * `aiplatform.batchPredictionJobs.cancel`
  * `aiplatform.batchPredictionJobs.create`
  * `aiplatform.batchPredictionJobs.delete`
  * `aiplatform.batchPredictionJobs.get`
  * `aiplatform.batchPredictionJobs.list`

`aiplatform.cacheConfigs.get` `aiplatform.cachedContents.*`

  * `aiplatform.cachedContents.create`
  * `aiplatform.cachedContents.delete`
  * `aiplatform.cachedContents.get`
  * `aiplatform.cachedContents.list`
  * `aiplatform.cachedContents.update`

`aiplatform.consents.get` `aiplatform.contexts.*`

  * `aiplatform.contexts.addContextArtifactsAndExecutions`
  * `aiplatform.contexts.addContextChildren`
  * `aiplatform.contexts.create`
  * `aiplatform.contexts.delete`
  * `aiplatform.contexts.get`
  * `aiplatform.contexts.list`
  * `aiplatform.contexts.queryContextLineageSubgraph`
  * `aiplatform.contexts.update`

`aiplatform.customJobs.*`

  * `aiplatform.customJobs.cancel`
  * `aiplatform.customJobs.create`
  * `aiplatform.customJobs.delete`
  * `aiplatform.customJobs.get`
  * `aiplatform.customJobs.list`

`aiplatform.dataItems.*`

  * `aiplatform.dataItems.create`
  * `aiplatform.dataItems.delete`
  * `aiplatform.dataItems.get`
  * `aiplatform.dataItems.list`
  * `aiplatform.dataItems.update`

`aiplatform.dataLabelingJobs.*`

  * `aiplatform.dataLabelingJobs.cancel`
  * `aiplatform.dataLabelingJobs.create`
  * `aiplatform.dataLabelingJobs.delete`
  * `aiplatform.dataLabelingJobs.get`
  * `aiplatform.dataLabelingJobs.list`

`aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.*`

  * `aiplatform.datasets.create`
  * `aiplatform.datasets.delete`
  * `aiplatform.datasets.export`
  * `aiplatform.datasets.get`
  * `aiplatform.datasets.import`
  * `aiplatform.datasets.list`
  * `aiplatform.datasets.update`

`aiplatform.deploymentResourcePools.*`

  * `aiplatform.deploymentResourcePools.create`
  * `aiplatform.deploymentResourcePools.delete`
  * `aiplatform.deploymentResourcePools.get`
  * `aiplatform.deploymentResourcePools.list`
  * `aiplatform.deploymentResourcePools.queryDeployedModels`
  * `aiplatform.deploymentResourcePools.update`

`aiplatform.edgeDeploymentJobs.*`

  * `aiplatform.edgeDeploymentJobs.create`
  * `aiplatform.edgeDeploymentJobs.delete`
  * `aiplatform.edgeDeploymentJobs.get`
  * `aiplatform.edgeDeploymentJobs.list`

`aiplatform.edgeDeviceDebugInfo.get` `aiplatform.edgeDevices.*`

  * `aiplatform.edgeDevices.create`
  * `aiplatform.edgeDevices.delete`
  * `aiplatform.edgeDevices.get`
  * `aiplatform.edgeDevices.list`
  * `aiplatform.edgeDevices.update`

`aiplatform.endpoints.create` `aiplatform.endpoints.delete` `aiplatform.endpoints.deploy` `aiplatform.endpoints.explain` `aiplatform.endpoints.get` `aiplatform.endpoints.getIamPolicy` `aiplatform.endpoints.list` `aiplatform.endpoints.predict` `aiplatform.endpoints.undeploy` `aiplatform.endpoints.update` `aiplatform.entityTypes.create` `aiplatform.entityTypes.delete` `aiplatform.entityTypes.deleteFeatureValues` `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.getIamPolicy` `aiplatform.entityTypes.importFeatureValues` `aiplatform.entityTypes.list` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.entityTypes.update` `aiplatform.entityTypes.writeFeatureValues` `aiplatform.evaluationExperiments.*`

  * `aiplatform.evaluationExperiments.create`
  * `aiplatform.evaluationExperiments.delete`
  * `aiplatform.evaluationExperiments.get`
  * `aiplatform.evaluationExperiments.list`
  * `aiplatform.evaluationExperiments.update`

`aiplatform.evaluationItems.*`

  * `aiplatform.evaluationItems.create`
  * `aiplatform.evaluationItems.delete`
  * `aiplatform.evaluationItems.get`
  * `aiplatform.evaluationItems.list`
  * `aiplatform.evaluationItems.update`

`aiplatform.evaluationMetrics.*`

  * `aiplatform.evaluationMetrics.create`
  * `aiplatform.evaluationMetrics.delete`
  * `aiplatform.evaluationMetrics.get`
  * `aiplatform.evaluationMetrics.list`

`aiplatform.evaluationRuns.*`

  * `aiplatform.evaluationRuns.cancel`
  * `aiplatform.evaluationRuns.create`
  * `aiplatform.evaluationRuns.delete`
  * `aiplatform.evaluationRuns.execute`
  * `aiplatform.evaluationRuns.get`
  * `aiplatform.evaluationRuns.list`
  * `aiplatform.evaluationRuns.update`

`aiplatform.evaluationSets.*`

  * `aiplatform.evaluationSets.create`
  * `aiplatform.evaluationSets.delete`
  * `aiplatform.evaluationSets.get`
  * `aiplatform.evaluationSets.import`
  * `aiplatform.evaluationSets.list`
  * `aiplatform.evaluationSets.update`

`aiplatform.exampleStores.*`

  * `aiplatform.exampleStores.create`
  * `aiplatform.exampleStores.delete`
  * `aiplatform.exampleStores.get`
  * `aiplatform.exampleStores.list`
  * `aiplatform.exampleStores.readExample`
  * `aiplatform.exampleStores.update`
  * `aiplatform.exampleStores.writeExample`

`aiplatform.executions.*`

  * `aiplatform.executions.addExecutionEvents`
  * `aiplatform.executions.create`
  * `aiplatform.executions.delete`
  * `aiplatform.executions.get`
  * `aiplatform.executions.list`
  * `aiplatform.executions.queryExecutionInputsAndOutputs`
  * `aiplatform.executions.update`

`aiplatform.extensions.*`

  * `aiplatform.extensions.delete`
  * `aiplatform.extensions.execute`
  * `aiplatform.extensions.get`
  * `aiplatform.extensions.import`
  * `aiplatform.extensions.list`
  * `aiplatform.extensions.update`

`aiplatform.featureGroups.create` `aiplatform.featureGroups.delete` `aiplatform.featureGroups.get` `aiplatform.featureGroups.getIamPolicy` `aiplatform.featureGroups.list` `aiplatform.featureGroups.update` `aiplatform.featureMonitorJobs.*`

  * `aiplatform.featureMonitorJobs.create`
  * `aiplatform.featureMonitorJobs.get`
  * `aiplatform.featureMonitorJobs.list`

`aiplatform.featureMonitors.*`

  * `aiplatform.featureMonitors.create`
  * `aiplatform.featureMonitors.delete`
  * `aiplatform.featureMonitors.get`
  * `aiplatform.featureMonitors.list`
  * `aiplatform.featureMonitors.update`

`aiplatform.featureOnlineStores.create` `aiplatform.featureOnlineStores.delete` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.getIamPolicy` `aiplatform.featureOnlineStores.list` `aiplatform.featureOnlineStores.update` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.create` `aiplatform.featureViews.delete` `aiplatform.featureViews.directWrite` `aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.getIamPolicy` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.featureViews.sync` `aiplatform.featureViews.update` `aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.batchReadFeatureValues` `aiplatform.featurestores.create` `aiplatform.featurestores.delete` `aiplatform.featurestores.exportFeatures` `aiplatform.featurestores.get` `aiplatform.featurestores.getIamPolicy` `aiplatform.featurestores.importFeatures` `aiplatform.featurestores.list` `aiplatform.featurestores.readFeatures` `aiplatform.featurestores.update` `aiplatform.featurestores.writeFeatures` `aiplatform.humanInTheLoops.*`

  * `aiplatform.humanInTheLoops.cancel`
  * `aiplatform.humanInTheLoops.create`
  * `aiplatform.humanInTheLoops.delete`
  * `aiplatform.humanInTheLoops.get`
  * `aiplatform.humanInTheLoops.list`
  * `aiplatform.humanInTheLoops.queryAnnotationStats`
  * `aiplatform.humanInTheLoops.send`
  * `aiplatform.humanInTheLoops.update`

`aiplatform.hyperparameterTuningJobs.*`

  * `aiplatform.hyperparameterTuningJobs.cancel`
  * `aiplatform.hyperparameterTuningJobs.create`
  * `aiplatform.hyperparameterTuningJobs.delete`
  * `aiplatform.hyperparameterTuningJobs.get`
  * `aiplatform.hyperparameterTuningJobs.list`

`aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.interactions.*`

  * `aiplatform.interactions.cancel`
  * `aiplatform.interactions.create`
  * `aiplatform.interactions.delete`
  * `aiplatform.interactions.get`
  * `aiplatform.interactions.list`

`aiplatform.locations.*`

  * `aiplatform.locations.evaluateInstances`
  * `aiplatform.locations.get`
  * `aiplatform.locations.list`

`aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.memoryRevisions.*`

  * `aiplatform.memoryRevisions.get`
  * `aiplatform.memoryRevisions.list`
  * `aiplatform.memoryRevisions.rollback`

`aiplatform.metadataSchemas.*`

  * `aiplatform.metadataSchemas.create`
  * `aiplatform.metadataSchemas.delete`
  * `aiplatform.metadataSchemas.get`
  * `aiplatform.metadataSchemas.list`

`aiplatform.metadataStores.*`

  * `aiplatform.metadataStores.create`
  * `aiplatform.metadataStores.delete`
  * `aiplatform.metadataStores.get`
  * `aiplatform.metadataStores.list`

`aiplatform.migratableResources.search` `aiplatform.modelDeploymentMonitoringJobs.*`

  * `aiplatform.modelDeploymentMonitoringJobs.create`
  * `aiplatform.modelDeploymentMonitoringJobs.delete`
  * `aiplatform.modelDeploymentMonitoringJobs.get`
  * `aiplatform.modelDeploymentMonitoringJobs.list`
  * `aiplatform.modelDeploymentMonitoringJobs.pause`
  * `aiplatform.modelDeploymentMonitoringJobs.resume`
  * `aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`
  * `aiplatform.modelDeploymentMonitoringJobs.update`

`aiplatform.modelEvaluationSlices.*`

  * `aiplatform.modelEvaluationSlices.get`
  * `aiplatform.modelEvaluationSlices.import`
  * `aiplatform.modelEvaluationSlices.list`

`aiplatform.modelEvaluations.*`

  * `aiplatform.modelEvaluations.exportEvaluatedDataItems`
  * `aiplatform.modelEvaluations.get`
  * `aiplatform.modelEvaluations.import`
  * `aiplatform.modelEvaluations.list`

`aiplatform.modelMonitoringJobs.*`

  * `aiplatform.modelMonitoringJobs.create`
  * `aiplatform.modelMonitoringJobs.delete`
  * `aiplatform.modelMonitoringJobs.get`
  * `aiplatform.modelMonitoringJobs.list`

`aiplatform.modelMonitors.*`

  * `aiplatform.modelMonitors.create`
  * `aiplatform.modelMonitors.delete`
  * `aiplatform.modelMonitors.get`
  * `aiplatform.modelMonitors.list`
  * `aiplatform.modelMonitors.searchModelMonitoringAlerts`
  * `aiplatform.modelMonitors.searchModelMonitoringStats`
  * `aiplatform.modelMonitors.update`

`aiplatform.models.*`

  * `aiplatform.models.delete`
  * `aiplatform.models.export`
  * `aiplatform.models.get`
  * `aiplatform.models.list`
  * `aiplatform.models.update`
  * `aiplatform.models.upload`

`aiplatform.monitoredAgents.disable` `aiplatform.monitoredAgents.enable` `aiplatform.monitoredAgents.get` `aiplatform.monitoredAgents.list` `aiplatform.nasJobs.*`

  * `aiplatform.nasJobs.cancel`
  * `aiplatform.nasJobs.create`
  * `aiplatform.nasJobs.delete`
  * `aiplatform.nasJobs.get`
  * `aiplatform.nasJobs.list`

`aiplatform.nasTrialDetails.*`

  * `aiplatform.nasTrialDetails.get`
  * `aiplatform.nasTrialDetails.list`

`aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.create` `aiplatform.notebookRuntimeTemplates.delete` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimeTemplates.update` `aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.onlineEvaluators.*`

  * `aiplatform.onlineEvaluators.create`
  * `aiplatform.onlineEvaluators.delete`
  * `aiplatform.onlineEvaluators.get`
  * `aiplatform.onlineEvaluators.list`
  * `aiplatform.onlineEvaluators.update`

`aiplatform.operations.list` `aiplatform.persistentResources.get` `aiplatform.persistentResources.list` `aiplatform.pipelineJobs.*`

  * `aiplatform.pipelineJobs.cancel`
  * `aiplatform.pipelineJobs.create`
  * `aiplatform.pipelineJobs.delete`
  * `aiplatform.pipelineJobs.get`
  * `aiplatform.pipelineJobs.list`

`aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.get` `aiplatform.provisionedThroughputs.list` `aiplatform.ragCorpora.*`

  * `aiplatform.ragCorpora.create`
  * `aiplatform.ragCorpora.delete`
  * `aiplatform.ragCorpora.get`
  * `aiplatform.ragCorpora.list`
  * `aiplatform.ragCorpora.query`
  * `aiplatform.ragCorpora.update`

`aiplatform.ragEngineConfigs.get` `aiplatform.ragFiles.*`

  * `aiplatform.ragFiles.delete`
  * `aiplatform.ragFiles.get`
  * `aiplatform.ragFiles.import`
  * `aiplatform.ragFiles.list`
  * `aiplatform.ragFiles.upload`

`aiplatform.reasoningEngineRuntimeRevisions.*`

  * `aiplatform.reasoningEngineRuntimeRevisions.delete`
  * `aiplatform.reasoningEngineRuntimeRevisions.get`
  * `aiplatform.reasoningEngineRuntimeRevisions.list`
  * `aiplatform.reasoningEngineRuntimeRevisions.query`

`aiplatform.reasoningEngines.create` `aiplatform.reasoningEngines.delete` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.reasoningEngines.update` `aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`aiplatform.semanticGovernancePolicies.*`

  * `aiplatform.semanticGovernancePolicies.create`
  * `aiplatform.semanticGovernancePolicies.delete`
  * `aiplatform.semanticGovernancePolicies.get`
  * `aiplatform.semanticGovernancePolicies.list`
  * `aiplatform.semanticGovernancePolicies.update`

`aiplatform.semanticGovernancePolicyEngine.*`

  * `aiplatform.semanticGovernancePolicyEngine.get`
  * `aiplatform.semanticGovernancePolicyEngine.update`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.*`

  * `aiplatform.sessions.create`
  * `aiplatform.sessions.delete`
  * `aiplatform.sessions.get`
  * `aiplatform.sessions.list`
  * `aiplatform.sessions.run`
  * `aiplatform.sessions.update`

`aiplatform.specialistPools.*`

  * `aiplatform.specialistPools.create`
  * `aiplatform.specialistPools.delete`
  * `aiplatform.specialistPools.get`
  * `aiplatform.specialistPools.list`
  * `aiplatform.specialistPools.update`

`aiplatform.studies.*`

  * `aiplatform.studies.create`
  * `aiplatform.studies.delete`
  * `aiplatform.studies.get`
  * `aiplatform.studies.list`
  * `aiplatform.studies.update`

`aiplatform.tasks.*`

  * `aiplatform.tasks.cancel`
  * `aiplatform.tasks.create`
  * `aiplatform.tasks.delete`
  * `aiplatform.tasks.get`
  * `aiplatform.tasks.list`
  * `aiplatform.tasks.update`

`aiplatform.tensorboardExperiments.*`

  * `aiplatform.tensorboardExperiments.create`
  * `aiplatform.tensorboardExperiments.delete`
  * `aiplatform.tensorboardExperiments.get`
  * `aiplatform.tensorboardExperiments.list`
  * `aiplatform.tensorboardExperiments.update`
  * `aiplatform.tensorboardExperiments.write`

`aiplatform.tensorboardRuns.*`

  * `aiplatform.tensorboardRuns.batchCreate`
  * `aiplatform.tensorboardRuns.create`
  * `aiplatform.tensorboardRuns.delete`
  * `aiplatform.tensorboardRuns.get`
  * `aiplatform.tensorboardRuns.list`
  * `aiplatform.tensorboardRuns.update`
  * `aiplatform.tensorboardRuns.write`

`aiplatform.tensorboardTimeSeries.*`

  * `aiplatform.tensorboardTimeSeries.batchCreate`
  * `aiplatform.tensorboardTimeSeries.batchRead`
  * `aiplatform.tensorboardTimeSeries.create`
  * `aiplatform.tensorboardTimeSeries.delete`
  * `aiplatform.tensorboardTimeSeries.get`
  * `aiplatform.tensorboardTimeSeries.list`
  * `aiplatform.tensorboardTimeSeries.read`
  * `aiplatform.tensorboardTimeSeries.update`

`aiplatform.tensorboards.create` `aiplatform.tensorboards.delete` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.tensorboards.update` `aiplatform.trainingPipelines.*`

  * `aiplatform.trainingPipelines.cancel`
  * `aiplatform.trainingPipelines.create`
  * `aiplatform.trainingPipelines.delete`
  * `aiplatform.trainingPipelines.get`
  * `aiplatform.trainingPipelines.list`

`aiplatform.trials.*`

  * `aiplatform.trials.create`
  * `aiplatform.trials.delete`
  * `aiplatform.trials.get`
  * `aiplatform.trials.list`
  * `aiplatform.trials.update`

`aiplatform.tuningJobs.*`

  * `aiplatform.tuningJobs.cancel`
  * `aiplatform.tuningJobs.create`
  * `aiplatform.tuningJobs.delete`
  * `aiplatform.tuningJobs.get`
  * `aiplatform.tuningJobs.list`
  * `aiplatform.tuningJobs.optimizePrompt`
  * `aiplatform.tuningJobs.validateReinforcementTuningReward`
  * `aiplatform.tuningJobs.vertexTune`

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.tags.get` `artifactregistry.versions.get` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.readsessions.create` `bigquery.readsessions.getData` `bigquery.tables.create` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.update` `bigquery.tables.updateData` `cloudtrace.traces.list` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.implicitDelegation` `iam.serviceAccounts.list` `iam.serviceAccounts.signBlob` `iam.serviceAccounts.signJwt` `logging.logEntries.create` `logging.logEntries.route` `logging.views.access` `logging.views.get` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `observability.views.access` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicemanagement.services.report` `serviceusage.services.use` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Vertex AI Extension Custom Code Service Agent 

(`roles/aiplatform.extensionCustomCodeServiceAgent`) Gives Vertex AI Extension that executes custom code the permissions it needs to function.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `logging.logEntries.create` `logging.logEntries.route` `monitoring.timeSeries.create` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.folders.*`

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

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

  
  
#### Vertex AI Extension Service Agent 

(`roles/aiplatform.extensionServiceAgent`) Gives Vertex AI Extension the permissions it needs to function.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.predict` `aiplatform.locations.get` `aiplatform.ragCorpora.query` `discoveryengine.servingConfigs.search` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `logging.logEntries.create` `logging.logEntries.route` `serviceusage.services.use` `storage.objects.get`  
  
#### Vertex AI Model Monitoring Service Agent 

(`roles/aiplatform.modelMonitoringServiceAgent`) Gives Vertex AI Model Monitoring the permissions it needs to function.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.batchPredictionJobs.create` `aiplatform.batchPredictionJobs.get` `aiplatform.batchPredictionJobs.list` `aiplatform.locations.evaluateInstances` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.tables.create` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.update` `bigquery.tables.updateData` `monitoring.notificationChannels.get` `serviceusage.services.use` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Vertex AI Notebook Service Agent 

(`roles/aiplatform.notebookServiceAgent`) Vertex AI Service Agent used to run Notebook managed resources in user project with restricted permissions.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `logging.logEntries.create` `logging.logEntries.route` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create`  
  
#### Vertex AI Online Prediction Service Agent 

(`roles/aiplatform.onlinePredictionServiceAgent`) Gives Vertex AI Online Prediction the permissions it needs to function.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `gkehub.features.get` `gkehub.features.getIamPolicy` `gkehub.features.list` `gkehub.fleet.get` `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.get` `gkehub.memberships.getIamPolicy` `gkehub.memberships.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Vertex AI RAG Data Service Agent 

(`roles/aiplatform.ragServiceAgent`) Vertex AI Service Agent used by Vertex RAG to access user imported data, Vertex AI, Document AI processors, and Vector Search in the project  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.get` `aiplatform.endpoints.predict` `aiplatform.featureViews.get` `aiplatform.featureViews.list` `aiplatform.featureViews.sync` `aiplatform.featureViews.update` `aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.models.get` `aiplatform.ragCorpora.get` `aiplatform.ragCorpora.list` `aiplatform.ragCorpora.query` `aiplatform.ragFiles.get` `aiplatform.ragFiles.list` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.readsessions.create` `bigquery.readsessions.getData` `bigquery.tables.create` `bigquery.tables.createSnapshot` `bigquery.tables.deleteSnapshot` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.restoreSnapshot` `bigquery.tables.update` `bigquery.tables.updateData` `documentai.processorVersions.processOnline` `documentai.processors.get` `documentai.processors.processOnline` `logging.logEntries.create` `logging.logEntries.route` `storage.buckets.get` `storage.buckets.list` `storage.objects.get` `storage.objects.list` `vectorsearch.collections.*`

  * `vectorsearch.collections.create`
  * `vectorsearch.collections.delete`
  * `vectorsearch.collections.get`
  * `vectorsearch.collections.list`
  * `vectorsearch.collections.update`

`vectorsearch.dataObjects.create` `vectorsearch.dataObjects.delete` `vectorsearch.dataObjects.get` `vectorsearch.dataObjects.import` `vectorsearch.dataObjects.query` `vectorsearch.dataObjects.search` `vectorsearch.dataObjects.update` `vectorsearch.indexes.create` `vectorsearch.indexes.delete` `vectorsearch.indexes.get` `vectorsearch.indexes.list` `vectorsearch.operations.get` `vectorsearch.operations.list`  
  
#### Vertex AI Rapid Eval Service Agent 

(`roles/aiplatform.rapidevalServiceAgent`) Vertex AI Service Agent used by GenAI Rapid Evaluation Service to access publisher model endpoints in the user project  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.predict`  
  
#### Vertex AI Reasoning Engine Service Agent 

(`roles/aiplatform.reasoningEngineServiceAgent`) Gives Vertex AI Reasoning Engine the proper permissions to function. The aiplatform.reasoningEngines.create IAM permission implies read access to the GCS objects of the consumer project through this service agent.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.create` `aiplatform.endpoints.delete` `aiplatform.endpoints.deploy` `aiplatform.endpoints.explain` `aiplatform.endpoints.get` `aiplatform.endpoints.list` `aiplatform.endpoints.predict` `aiplatform.endpoints.undeploy` `aiplatform.endpoints.update` `aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.create` `aiplatform.sessions.delete` `aiplatform.sessions.get` `aiplatform.sessions.list` `aiplatform.sessions.update` `cloudapiregistry.*`

  * `cloudapiregistry.locations.get`
  * `cloudapiregistry.locations.list`
  * `cloudapiregistry.mcpServers.get`
  * `cloudapiregistry.mcpServers.list`
  * `cloudapiregistry.mcpTools.get`
  * `cloudapiregistry.mcpTools.list`

`cloudtrace.traces.patch` `developerconnect.connections.get` `developerconnect.gitRepositoryLinks.fetchReadToken` `developerconnect.gitRepositoryLinks.get` `logging.logEntries.create` `logging.logEntries.route` `modelarmor.callouts.invoke` `modelarmor.locations.*`

  * `modelarmor.locations.get`
  * `modelarmor.locations.list`

`modelarmor.templates.useToSanitizeInput` `modelarmor.templates.useToSanitizeModelResponse` `modelarmor.templates.useToSanitizeOutput` `modelarmor.templates.useToSanitizeUserPrompt` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.services.use` `storage.buckets.get` `storage.buckets.list` `storage.objects.get` `storage.objects.list` `telemetry.traces.write`  
  
#### Vertex AI Service Agent 

(`roles/aiplatform.serviceAgent`) Gives Vertex AI the permissions it needs to function.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `agentregistry.agents.get` `agentregistry.agents.list` `agentregistry.endpoints.*`

  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`

`agentregistry.mcpServers.get` `agentregistry.mcpServers.list` `agentregistry.operations.*`

  * `agentregistry.operations.cancel`
  * `agentregistry.operations.delete`
  * `agentregistry.operations.get`
  * `agentregistry.operations.list`

`agentregistry.skills.create` `agentregistry.skills.delete` `aiplatform.agentAnomalyDetectionScopes.*`

  * `aiplatform.agentAnomalyDetectionScopes.create`
  * `aiplatform.agentAnomalyDetectionScopes.delete`
  * `aiplatform.agentAnomalyDetectionScopes.get`
  * `aiplatform.agentAnomalyDetectionScopes.list`

`aiplatform.agentExamples.*`

  * `aiplatform.agentExamples.create`
  * `aiplatform.agentExamples.delete`
  * `aiplatform.agentExamples.get`
  * `aiplatform.agentExamples.list`
  * `aiplatform.agentExamples.update`

`aiplatform.agents.create` `aiplatform.agents.delete` `aiplatform.agents.get` `aiplatform.agents.list` `aiplatform.agents.update` `aiplatform.analyzedInvocations.*`

  * `aiplatform.analyzedInvocations.get`
  * `aiplatform.analyzedInvocations.list`

`aiplatform.analyzedSessions.*`

  * `aiplatform.analyzedSessions.aggregate`
  * `aiplatform.analyzedSessions.get`
  * `aiplatform.analyzedSessions.list`

`aiplatform.annotationSpecs.*`

  * `aiplatform.annotationSpecs.create`
  * `aiplatform.annotationSpecs.delete`
  * `aiplatform.annotationSpecs.get`
  * `aiplatform.annotationSpecs.list`
  * `aiplatform.annotationSpecs.update`

`aiplatform.annotations.*`

  * `aiplatform.annotations.create`
  * `aiplatform.annotations.delete`
  * `aiplatform.annotations.get`
  * `aiplatform.annotations.list`
  * `aiplatform.annotations.update`

`aiplatform.apps.*`

  * `aiplatform.apps.create`
  * `aiplatform.apps.delete`
  * `aiplatform.apps.get`
  * `aiplatform.apps.list`
  * `aiplatform.apps.update`

`aiplatform.artifacts.*`

  * `aiplatform.artifacts.create`
  * `aiplatform.artifacts.delete`
  * `aiplatform.artifacts.get`
  * `aiplatform.artifacts.list`
  * `aiplatform.artifacts.update`

`aiplatform.batchPredictionJobs.*`

  * `aiplatform.batchPredictionJobs.cancel`
  * `aiplatform.batchPredictionJobs.create`
  * `aiplatform.batchPredictionJobs.delete`
  * `aiplatform.batchPredictionJobs.get`
  * `aiplatform.batchPredictionJobs.list`

`aiplatform.cacheConfigs.get` `aiplatform.cachedContents.*`

  * `aiplatform.cachedContents.create`
  * `aiplatform.cachedContents.delete`
  * `aiplatform.cachedContents.get`
  * `aiplatform.cachedContents.list`
  * `aiplatform.cachedContents.update`

`aiplatform.consents.get` `aiplatform.contexts.*`

  * `aiplatform.contexts.addContextArtifactsAndExecutions`
  * `aiplatform.contexts.addContextChildren`
  * `aiplatform.contexts.create`
  * `aiplatform.contexts.delete`
  * `aiplatform.contexts.get`
  * `aiplatform.contexts.list`
  * `aiplatform.contexts.queryContextLineageSubgraph`
  * `aiplatform.contexts.update`

`aiplatform.customJobs.*`

  * `aiplatform.customJobs.cancel`
  * `aiplatform.customJobs.create`
  * `aiplatform.customJobs.delete`
  * `aiplatform.customJobs.get`
  * `aiplatform.customJobs.list`

`aiplatform.dataItems.*`

  * `aiplatform.dataItems.create`
  * `aiplatform.dataItems.delete`
  * `aiplatform.dataItems.get`
  * `aiplatform.dataItems.list`
  * `aiplatform.dataItems.update`

`aiplatform.dataLabelingJobs.*`

  * `aiplatform.dataLabelingJobs.cancel`
  * `aiplatform.dataLabelingJobs.create`
  * `aiplatform.dataLabelingJobs.delete`
  * `aiplatform.dataLabelingJobs.get`
  * `aiplatform.dataLabelingJobs.list`

`aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.*`

  * `aiplatform.datasets.create`
  * `aiplatform.datasets.delete`
  * `aiplatform.datasets.export`
  * `aiplatform.datasets.get`
  * `aiplatform.datasets.import`
  * `aiplatform.datasets.list`
  * `aiplatform.datasets.update`

`aiplatform.deploymentResourcePools.*`

  * `aiplatform.deploymentResourcePools.create`
  * `aiplatform.deploymentResourcePools.delete`
  * `aiplatform.deploymentResourcePools.get`
  * `aiplatform.deploymentResourcePools.list`
  * `aiplatform.deploymentResourcePools.queryDeployedModels`
  * `aiplatform.deploymentResourcePools.update`

`aiplatform.edgeDeploymentJobs.*`

  * `aiplatform.edgeDeploymentJobs.create`
  * `aiplatform.edgeDeploymentJobs.delete`
  * `aiplatform.edgeDeploymentJobs.get`
  * `aiplatform.edgeDeploymentJobs.list`

`aiplatform.edgeDeviceDebugInfo.get` `aiplatform.edgeDevices.*`

  * `aiplatform.edgeDevices.create`
  * `aiplatform.edgeDevices.delete`
  * `aiplatform.edgeDevices.get`
  * `aiplatform.edgeDevices.list`
  * `aiplatform.edgeDevices.update`

`aiplatform.endpoints.create` `aiplatform.endpoints.delete` `aiplatform.endpoints.deploy` `aiplatform.endpoints.explain` `aiplatform.endpoints.get` `aiplatform.endpoints.getIamPolicy` `aiplatform.endpoints.list` `aiplatform.endpoints.predict` `aiplatform.endpoints.undeploy` `aiplatform.endpoints.update` `aiplatform.entityTypes.create` `aiplatform.entityTypes.delete` `aiplatform.entityTypes.deleteFeatureValues` `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.getIamPolicy` `aiplatform.entityTypes.importFeatureValues` `aiplatform.entityTypes.list` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.entityTypes.update` `aiplatform.entityTypes.writeFeatureValues` `aiplatform.evaluationExperiments.*`

  * `aiplatform.evaluationExperiments.create`
  * `aiplatform.evaluationExperiments.delete`
  * `aiplatform.evaluationExperiments.get`
  * `aiplatform.evaluationExperiments.list`
  * `aiplatform.evaluationExperiments.update`

`aiplatform.evaluationItems.*`

  * `aiplatform.evaluationItems.create`
  * `aiplatform.evaluationItems.delete`
  * `aiplatform.evaluationItems.get`
  * `aiplatform.evaluationItems.list`
  * `aiplatform.evaluationItems.update`

`aiplatform.evaluationMetrics.*`

  * `aiplatform.evaluationMetrics.create`
  * `aiplatform.evaluationMetrics.delete`
  * `aiplatform.evaluationMetrics.get`
  * `aiplatform.evaluationMetrics.list`

`aiplatform.evaluationRuns.*`

  * `aiplatform.evaluationRuns.cancel`
  * `aiplatform.evaluationRuns.create`
  * `aiplatform.evaluationRuns.delete`
  * `aiplatform.evaluationRuns.execute`
  * `aiplatform.evaluationRuns.get`
  * `aiplatform.evaluationRuns.list`
  * `aiplatform.evaluationRuns.update`

`aiplatform.evaluationSets.*`

  * `aiplatform.evaluationSets.create`
  * `aiplatform.evaluationSets.delete`
  * `aiplatform.evaluationSets.get`
  * `aiplatform.evaluationSets.import`
  * `aiplatform.evaluationSets.list`
  * `aiplatform.evaluationSets.update`

`aiplatform.exampleStores.*`

  * `aiplatform.exampleStores.create`
  * `aiplatform.exampleStores.delete`
  * `aiplatform.exampleStores.get`
  * `aiplatform.exampleStores.list`
  * `aiplatform.exampleStores.readExample`
  * `aiplatform.exampleStores.update`
  * `aiplatform.exampleStores.writeExample`

`aiplatform.executions.*`

  * `aiplatform.executions.addExecutionEvents`
  * `aiplatform.executions.create`
  * `aiplatform.executions.delete`
  * `aiplatform.executions.get`
  * `aiplatform.executions.list`
  * `aiplatform.executions.queryExecutionInputsAndOutputs`
  * `aiplatform.executions.update`

`aiplatform.extensions.*`

  * `aiplatform.extensions.delete`
  * `aiplatform.extensions.execute`
  * `aiplatform.extensions.get`
  * `aiplatform.extensions.import`
  * `aiplatform.extensions.list`
  * `aiplatform.extensions.update`

`aiplatform.featureGroups.create` `aiplatform.featureGroups.delete` `aiplatform.featureGroups.get` `aiplatform.featureGroups.getIamPolicy` `aiplatform.featureGroups.list` `aiplatform.featureGroups.update` `aiplatform.featureMonitorJobs.*`

  * `aiplatform.featureMonitorJobs.create`
  * `aiplatform.featureMonitorJobs.get`
  * `aiplatform.featureMonitorJobs.list`

`aiplatform.featureMonitors.*`

  * `aiplatform.featureMonitors.create`
  * `aiplatform.featureMonitors.delete`
  * `aiplatform.featureMonitors.get`
  * `aiplatform.featureMonitors.list`
  * `aiplatform.featureMonitors.update`

`aiplatform.featureOnlineStores.create` `aiplatform.featureOnlineStores.delete` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.getIamPolicy` `aiplatform.featureOnlineStores.list` `aiplatform.featureOnlineStores.update` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.create` `aiplatform.featureViews.delete` `aiplatform.featureViews.directWrite` `aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.getIamPolicy` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.featureViews.sync` `aiplatform.featureViews.update` `aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.batchReadFeatureValues` `aiplatform.featurestores.create` `aiplatform.featurestores.delete` `aiplatform.featurestores.exportFeatures` `aiplatform.featurestores.get` `aiplatform.featurestores.getIamPolicy` `aiplatform.featurestores.importFeatures` `aiplatform.featurestores.list` `aiplatform.featurestores.readFeatures` `aiplatform.featurestores.update` `aiplatform.featurestores.writeFeatures` `aiplatform.humanInTheLoops.*`

  * `aiplatform.humanInTheLoops.cancel`
  * `aiplatform.humanInTheLoops.create`
  * `aiplatform.humanInTheLoops.delete`
  * `aiplatform.humanInTheLoops.get`
  * `aiplatform.humanInTheLoops.list`
  * `aiplatform.humanInTheLoops.queryAnnotationStats`
  * `aiplatform.humanInTheLoops.send`
  * `aiplatform.humanInTheLoops.update`

`aiplatform.hyperparameterTuningJobs.*`

  * `aiplatform.hyperparameterTuningJobs.cancel`
  * `aiplatform.hyperparameterTuningJobs.create`
  * `aiplatform.hyperparameterTuningJobs.delete`
  * `aiplatform.hyperparameterTuningJobs.get`
  * `aiplatform.hyperparameterTuningJobs.list`

`aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.interactions.*`

  * `aiplatform.interactions.cancel`
  * `aiplatform.interactions.create`
  * `aiplatform.interactions.delete`
  * `aiplatform.interactions.get`
  * `aiplatform.interactions.list`

`aiplatform.locations.*`

  * `aiplatform.locations.evaluateInstances`
  * `aiplatform.locations.get`
  * `aiplatform.locations.list`

`aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.memoryRevisions.*`

  * `aiplatform.memoryRevisions.get`
  * `aiplatform.memoryRevisions.list`
  * `aiplatform.memoryRevisions.rollback`

`aiplatform.metadataSchemas.*`

  * `aiplatform.metadataSchemas.create`
  * `aiplatform.metadataSchemas.delete`
  * `aiplatform.metadataSchemas.get`
  * `aiplatform.metadataSchemas.list`

`aiplatform.metadataStores.*`

  * `aiplatform.metadataStores.create`
  * `aiplatform.metadataStores.delete`
  * `aiplatform.metadataStores.get`
  * `aiplatform.metadataStores.list`

`aiplatform.migratableResources.search` `aiplatform.modelDeploymentMonitoringJobs.*`

  * `aiplatform.modelDeploymentMonitoringJobs.create`
  * `aiplatform.modelDeploymentMonitoringJobs.delete`
  * `aiplatform.modelDeploymentMonitoringJobs.get`
  * `aiplatform.modelDeploymentMonitoringJobs.list`
  * `aiplatform.modelDeploymentMonitoringJobs.pause`
  * `aiplatform.modelDeploymentMonitoringJobs.resume`
  * `aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`
  * `aiplatform.modelDeploymentMonitoringJobs.update`

`aiplatform.modelEvaluationSlices.*`

  * `aiplatform.modelEvaluationSlices.get`
  * `aiplatform.modelEvaluationSlices.import`
  * `aiplatform.modelEvaluationSlices.list`

`aiplatform.modelEvaluations.*`

  * `aiplatform.modelEvaluations.exportEvaluatedDataItems`
  * `aiplatform.modelEvaluations.get`
  * `aiplatform.modelEvaluations.import`
  * `aiplatform.modelEvaluations.list`

`aiplatform.modelMonitoringJobs.*`

  * `aiplatform.modelMonitoringJobs.create`
  * `aiplatform.modelMonitoringJobs.delete`
  * `aiplatform.modelMonitoringJobs.get`
  * `aiplatform.modelMonitoringJobs.list`

`aiplatform.modelMonitors.*`

  * `aiplatform.modelMonitors.create`
  * `aiplatform.modelMonitors.delete`
  * `aiplatform.modelMonitors.get`
  * `aiplatform.modelMonitors.list`
  * `aiplatform.modelMonitors.searchModelMonitoringAlerts`
  * `aiplatform.modelMonitors.searchModelMonitoringStats`
  * `aiplatform.modelMonitors.update`

`aiplatform.models.*`

  * `aiplatform.models.delete`
  * `aiplatform.models.export`
  * `aiplatform.models.get`
  * `aiplatform.models.list`
  * `aiplatform.models.update`
  * `aiplatform.models.upload`

`aiplatform.monitoredAgents.disable` `aiplatform.monitoredAgents.enable` `aiplatform.monitoredAgents.get` `aiplatform.monitoredAgents.list` `aiplatform.nasJobs.*`

  * `aiplatform.nasJobs.cancel`
  * `aiplatform.nasJobs.create`
  * `aiplatform.nasJobs.delete`
  * `aiplatform.nasJobs.get`
  * `aiplatform.nasJobs.list`

`aiplatform.nasTrialDetails.*`

  * `aiplatform.nasTrialDetails.get`
  * `aiplatform.nasTrialDetails.list`

`aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.create` `aiplatform.notebookRuntimeTemplates.delete` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimeTemplates.update` `aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.onlineEvaluators.*`

  * `aiplatform.onlineEvaluators.create`
  * `aiplatform.onlineEvaluators.delete`
  * `aiplatform.onlineEvaluators.get`
  * `aiplatform.onlineEvaluators.list`
  * `aiplatform.onlineEvaluators.update`

`aiplatform.operations.list` `aiplatform.persistentResources.get` `aiplatform.persistentResources.list` `aiplatform.pipelineJobs.*`

  * `aiplatform.pipelineJobs.cancel`
  * `aiplatform.pipelineJobs.create`
  * `aiplatform.pipelineJobs.delete`
  * `aiplatform.pipelineJobs.get`
  * `aiplatform.pipelineJobs.list`

`aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.get` `aiplatform.provisionedThroughputs.list` `aiplatform.ragCorpora.*`

  * `aiplatform.ragCorpora.create`
  * `aiplatform.ragCorpora.delete`
  * `aiplatform.ragCorpora.get`
  * `aiplatform.ragCorpora.list`
  * `aiplatform.ragCorpora.query`
  * `aiplatform.ragCorpora.update`

`aiplatform.ragEngineConfigs.get` `aiplatform.ragFiles.*`

  * `aiplatform.ragFiles.delete`
  * `aiplatform.ragFiles.get`
  * `aiplatform.ragFiles.import`
  * `aiplatform.ragFiles.list`
  * `aiplatform.ragFiles.upload`

`aiplatform.reasoningEngineRuntimeRevisions.*`

  * `aiplatform.reasoningEngineRuntimeRevisions.delete`
  * `aiplatform.reasoningEngineRuntimeRevisions.get`
  * `aiplatform.reasoningEngineRuntimeRevisions.list`
  * `aiplatform.reasoningEngineRuntimeRevisions.query`

`aiplatform.reasoningEngines.create` `aiplatform.reasoningEngines.delete` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.reasoningEngines.update` `aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`aiplatform.semanticGovernancePolicies.*`

  * `aiplatform.semanticGovernancePolicies.create`
  * `aiplatform.semanticGovernancePolicies.delete`
  * `aiplatform.semanticGovernancePolicies.get`
  * `aiplatform.semanticGovernancePolicies.list`
  * `aiplatform.semanticGovernancePolicies.update`

`aiplatform.semanticGovernancePolicyEngine.*`

  * `aiplatform.semanticGovernancePolicyEngine.get`
  * `aiplatform.semanticGovernancePolicyEngine.update`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.*`

  * `aiplatform.sessions.create`
  * `aiplatform.sessions.delete`
  * `aiplatform.sessions.get`
  * `aiplatform.sessions.list`
  * `aiplatform.sessions.run`
  * `aiplatform.sessions.update`

`aiplatform.specialistPools.*`

  * `aiplatform.specialistPools.create`
  * `aiplatform.specialistPools.delete`
  * `aiplatform.specialistPools.get`
  * `aiplatform.specialistPools.list`
  * `aiplatform.specialistPools.update`

`aiplatform.studies.*`

  * `aiplatform.studies.create`
  * `aiplatform.studies.delete`
  * `aiplatform.studies.get`
  * `aiplatform.studies.list`
  * `aiplatform.studies.update`

`aiplatform.tasks.*`

  * `aiplatform.tasks.cancel`
  * `aiplatform.tasks.create`
  * `aiplatform.tasks.delete`
  * `aiplatform.tasks.get`
  * `aiplatform.tasks.list`
  * `aiplatform.tasks.update`

`aiplatform.tensorboardExperiments.*`

  * `aiplatform.tensorboardExperiments.create`
  * `aiplatform.tensorboardExperiments.delete`
  * `aiplatform.tensorboardExperiments.get`
  * `aiplatform.tensorboardExperiments.list`
  * `aiplatform.tensorboardExperiments.update`
  * `aiplatform.tensorboardExperiments.write`

`aiplatform.tensorboardRuns.*`

  * `aiplatform.tensorboardRuns.batchCreate`
  * `aiplatform.tensorboardRuns.create`
  * `aiplatform.tensorboardRuns.delete`
  * `aiplatform.tensorboardRuns.get`
  * `aiplatform.tensorboardRuns.list`
  * `aiplatform.tensorboardRuns.update`
  * `aiplatform.tensorboardRuns.write`

`aiplatform.tensorboardTimeSeries.*`

  * `aiplatform.tensorboardTimeSeries.batchCreate`
  * `aiplatform.tensorboardTimeSeries.batchRead`
  * `aiplatform.tensorboardTimeSeries.create`
  * `aiplatform.tensorboardTimeSeries.delete`
  * `aiplatform.tensorboardTimeSeries.get`
  * `aiplatform.tensorboardTimeSeries.list`
  * `aiplatform.tensorboardTimeSeries.read`
  * `aiplatform.tensorboardTimeSeries.update`

`aiplatform.tensorboards.create` `aiplatform.tensorboards.delete` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.tensorboards.update` `aiplatform.trainingPipelines.*`

  * `aiplatform.trainingPipelines.cancel`
  * `aiplatform.trainingPipelines.create`
  * `aiplatform.trainingPipelines.delete`
  * `aiplatform.trainingPipelines.get`
  * `aiplatform.trainingPipelines.list`

`aiplatform.trials.*`

  * `aiplatform.trials.create`
  * `aiplatform.trials.delete`
  * `aiplatform.trials.get`
  * `aiplatform.trials.list`
  * `aiplatform.trials.update`

`aiplatform.tuningJobs.*`

  * `aiplatform.tuningJobs.cancel`
  * `aiplatform.tuningJobs.create`
  * `aiplatform.tuningJobs.delete`
  * `aiplatform.tuningJobs.get`
  * `aiplatform.tuningJobs.list`
  * `aiplatform.tuningJobs.optimizePrompt`
  * `aiplatform.tuningJobs.validateReinforcementTuningReward`
  * `aiplatform.tuningJobs.vertexTune`

`artifactregistry.repositories.create` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.get` `artifactregistry.versions.get` `automl.datasets.export` `automl.datasets.get` `automl.datasets.list` `automl.modelEvaluations.list` `automl.models.get` `automl.models.list` `automl.operations.get` `automl.tableSpecs.get` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.models.create` `bigquery.models.export` `bigquery.models.getData` `bigquery.objectRefs.read` `bigquery.readsessions.create` `bigquery.readsessions.getData` `bigquery.tables.create` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `bigtable.tables.get` `bigtable.tables.list` `bigtable.tables.readRows` `binaryauthorization.policy.evaluatePolicy` `cloudtrace.traces.get` `cloudtrace.traces.list` `compute.addresses.get` `compute.addresses.list` `compute.addresses.use` `compute.addresses.useInternal` `compute.disks.create` `compute.disks.createSnapshot` `compute.disks.createTagBinding` `compute.disks.delete` `compute.disks.get` `compute.disks.setLabels` `compute.disks.use` `compute.disks.useReadOnly` `compute.globalOperations.get` `compute.instanceGroupManagers.update` `compute.instances.attachDisk` `compute.instances.create` `compute.instances.createTagBinding` `compute.instances.delete` `compute.instances.detachDisk` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.list` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setServiceAccount` `compute.instances.setTags` `compute.instances.start` `compute.instances.stop` `compute.instances.update` `compute.instances.useReadOnly` `compute.machineTypes.get` `compute.networks.get` `compute.networks.use` `compute.networks.useExternalIp` `compute.snapshots.create` `compute.snapshots.delete` `compute.snapshots.useReadOnly` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `dataflow.jobs.*`

  * `dataflow.jobs.cancel`
  * `dataflow.jobs.create`
  * `dataflow.jobs.get`
  * `dataflow.jobs.list`
  * `dataflow.jobs.snapshot`
  * `dataflow.jobs.updateContents`

`dataflow.messages.list` `dataflow.metrics.get` `dataflow.snapshots.*`

  * `dataflow.snapshots.delete`
  * `dataflow.snapshots.get`
  * `dataflow.snapshots.list`

`datalabeling.annotateddatasets.get` `datalabeling.datasets.export` `datalabeling.datasets.get` `datalabeling.datasets.list` `datalabeling.operations.get` `hypercomputecluster.clusters.*`

  * `hypercomputecluster.clusters.create`
  * `hypercomputecluster.clusters.delete`
  * `hypercomputecluster.clusters.get`
  * `hypercomputecluster.clusters.list`
  * `hypercomputecluster.clusters.update`

`hypercomputecluster.locations.*`

  * `hypercomputecluster.locations.get`
  * `hypercomputecluster.locations.list`

`hypercomputecluster.operations.*`

  * `hypercomputecluster.operations.cancel`
  * `hypercomputecluster.operations.delete`
  * `hypercomputecluster.operations.get`
  * `hypercomputecluster.operations.list`

`iam.serviceAccounts.actAs` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `logging.links.*`

  * `logging.links.create`
  * `logging.links.delete`
  * `logging.links.get`
  * `logging.links.list`

`logging.logEntries.create` `logging.logEntries.route` `logging.operations.get` `logging.operations.list` `logging.views.access` `logging.views.get` `ml.models.list` `ml.operations.get` `ml.versions.get` `ml.versions.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.timeSeries.create` `networkservices.agentGateways.get` `networkservices.agentGateways.use` `networkservices.operations.get` `notebooks.instances.create` `notebooks.instances.delete` `notebooks.instances.get` `observability.links.create` `observability.links.delete` `observability.links.get` `observability.links.list` `observability.operations.get` `observability.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `run.executions.delete` `run.executions.get` `run.jobs.create` `run.jobs.delete` `run.jobs.get` `run.jobs.run` `run.jobs.update` `run.operations.delete` `run.operations.get` `run.routes.invoke` `run.services.create` `run.services.delete` `run.services.get` `servicemanagement.services.report` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.folders.create` `storage.folders.delete` `storage.folders.get` `storage.folders.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Vertex AI Telemetry Service Agent 

(`roles/aiplatform.telemetryServiceAgent`) Allows Vertex AI Telemetry Service Agent to access telemetry data.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `logging.logEntries.create` `logging.logEntries.list` `logging.logEntries.route` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`servicemanagement.services.report`  
  
#### Vertex AI Tuning Service Agent 

(`roles/aiplatform.tuningServiceAgent`) Vertex AI Service Agent used for tuning in user project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.artifacts.*`

  * `aiplatform.artifacts.create`
  * `aiplatform.artifacts.delete`
  * `aiplatform.artifacts.get`
  * `aiplatform.artifacts.list`
  * `aiplatform.artifacts.update`

`aiplatform.batchPredictionJobs.cancel` `aiplatform.batchPredictionJobs.create` `aiplatform.batchPredictionJobs.get` `aiplatform.contexts.*`

  * `aiplatform.contexts.addContextArtifactsAndExecutions`
  * `aiplatform.contexts.addContextChildren`
  * `aiplatform.contexts.create`
  * `aiplatform.contexts.delete`
  * `aiplatform.contexts.get`
  * `aiplatform.contexts.list`
  * `aiplatform.contexts.queryContextLineageSubgraph`
  * `aiplatform.contexts.update`

`aiplatform.endpoints.create` `aiplatform.endpoints.deploy` `aiplatform.endpoints.get` `aiplatform.endpoints.predict` `aiplatform.evaluationRuns.create` `aiplatform.evaluationRuns.get` `aiplatform.locations.evaluateInstances` `aiplatform.locations.get` `aiplatform.metadataSchemas.*`

  * `aiplatform.metadataSchemas.create`
  * `aiplatform.metadataSchemas.delete`
  * `aiplatform.metadataSchemas.get`
  * `aiplatform.metadataSchemas.list`

`aiplatform.metadataStores.*`

  * `aiplatform.metadataStores.create`
  * `aiplatform.metadataStores.delete`
  * `aiplatform.metadataStores.get`
  * `aiplatform.metadataStores.list`

`aiplatform.models.get` `aiplatform.models.update` `aiplatform.models.upload` `aiplatform.operations.list` `aiplatform.pipelineJobs.get` `aiplatform.pipelineJobs.list` `aiplatform.tensorboardExperiments.*`

  * `aiplatform.tensorboardExperiments.create`
  * `aiplatform.tensorboardExperiments.delete`
  * `aiplatform.tensorboardExperiments.get`
  * `aiplatform.tensorboardExperiments.list`
  * `aiplatform.tensorboardExperiments.update`
  * `aiplatform.tensorboardExperiments.write`

`aiplatform.tensorboardRuns.*`

  * `aiplatform.tensorboardRuns.batchCreate`
  * `aiplatform.tensorboardRuns.create`
  * `aiplatform.tensorboardRuns.delete`
  * `aiplatform.tensorboardRuns.get`
  * `aiplatform.tensorboardRuns.list`
  * `aiplatform.tensorboardRuns.update`
  * `aiplatform.tensorboardRuns.write`

`aiplatform.tensorboardTimeSeries.*`

  * `aiplatform.tensorboardTimeSeries.batchCreate`
  * `aiplatform.tensorboardTimeSeries.batchRead`
  * `aiplatform.tensorboardTimeSeries.create`
  * `aiplatform.tensorboardTimeSeries.delete`
  * `aiplatform.tensorboardTimeSeries.get`
  * `aiplatform.tensorboardTimeSeries.list`
  * `aiplatform.tensorboardTimeSeries.read`
  * `aiplatform.tensorboardTimeSeries.update`

`aiplatform.tensorboards.create` `aiplatform.tensorboards.delete` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.tensorboards.update` `aiplatform.tuningJobs.cancel` `aiplatform.tuningJobs.create` `aiplatform.tuningJobs.delete` `aiplatform.tuningJobs.get` `aiplatform.tuningJobs.list` `aiplatform.tuningJobs.vertexTune` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.tables.create` `bigquery.tables.delete` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `resourcemanager.projects.get` `serviceusage.services.use` `storage.buckets.create` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.getIamPolicy` `storage.objects.list` `storage.objects.update`  
  
### Basic roles

The older Google Cloud [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) are common to all Google Cloud services. These roles are Owner, Editor, and Viewer.

Basic roles include thousands of permissions across all Google Cloud services. In production environments, don't grant basic roles unless there is no alternative. Instead, grant the most limited predefined roles or custom roles that meet your needs. 

## Project-level versus resource-level access

You can manage access at the project level or resource level. You might also have the ability to manage access at a folder or organization level.

For most Agent Platform resources, access can only be controlled by the project, folder, and organization. Access to individual resources can be granted only for specific resource types, for example, an endpoint or a featurestore.

Users share control of all resources they can access. For example, if a user registers a model, all other authorized users in the project can access, change, and delete the model.

To grant access to resources at the project level, assign one or more [roles](https://docs.cloud.google.com/iam/docs/roles-overview) to a principal (user, group, or [service account](https://docs.cloud.google.com/iam/docs/service-account-overview)).

For Agent Platform resources that let you grant access at the resource level, you set an IAM policy on that resource. The policy defines which roles are assigned to which principals.

Setting a [policy](https://docs.cloud.google.com/iam/docs/allow-policies#structure) at the resource level doesn't affect project-level policies. A resource inherits all policies from its ancestry. You can use these two levels of granularity to customize permissions. For example, you can grant users read permissions at the project level so that they can read all resources in the project, and then you can grant users write permissions per resource (at the resource level).

Not all Agent Platform predefined roles and resources support resource-level policies. To identify which roles can be used on which resources, see the Predefined roles table.

### Supported resources

Agent Platform supports Vertex AI Feature Store featurestore, entity type, and Model Registry resources. For more information, see [Control access to Vertex AI Feature Store resources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/control-access). Model Registry access is managed at the Agent Platform level.

After granting or revoking access to a resource, those changes take time to propagate. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Resources, service accounts, and service agents

Agent Platform services often manage long-running resources that perform actions, such as running a training job that reads training data, or serving a machine learning (ML) model that reads model weight. Such standalone resources have their own resource identity when performing actions. This identity is distinct from the identity of the principal that created the resource. Permissions granted to the resource identity define which data and other resources that the resource identity can access, not the permissions of the principal that created the resource.

By default, Agent Platform resources use service accounts managed by Agent Platform as a resource identity. These service accounts are called Agent Platform service agents, and they are attached to the project where the resource is created. Users with specific Agent Platform permissions can create resources that use Agent Platform service agents. For some services, you can specify a service account to attach to the resource. The resource uses this service account to access other resources and services. To learn more about service accounts, see service accounts.

Agent Platform uses different service agents depending on the APIs being called. Each service agent has specific IAM permissions on the project to which they are tied. These permissions are used by the resource identity to perform actions, and the permissions can include read-only access to all Cloud Storage resources and BigQuery data in the project.

### Service accounts

A [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) is a special account used by an application or a virtual machine (VM) instance, not a person. You can create and assign permissions to service accounts to provide specific permissions to a resource or application.

For information about using a service account to customize the permissions available to a custom training container or a container that serves online predictions for a custom-trained model, read [Use a custom service account](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/custom-service-account).

Service accounts are identified by an email address.

### Service agents

[Service agents](https://docs.cloud.google.com/iam/docs/service-agents) are automatically provided; they enable a service to access resources on your behalf.

**Note:** Don't remove default roles and permissions of service agents unless you are sure that they are unnecessary.

When a service agent is created, the service agent is granted a predefined role for your project. The following table lists Agent Platform service agents, their email addresses, and their respective roles:

Name | Used for | Email address | Role  
---|---|---|---  
Agent Platform Service Agent | Agent Platform capabilities | `service-PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com` | `roles/aiplatform.serviceAgent`  
Gemini Enterprise Agent Platform RAG Data Service Agent | Agent Platform RAG accesses user-imported data, Agent Platform, Document AI processors in the project | `service-PROJECT_NUMBER@gcp-sa-vertex-rag.iam.gserviceaccount.com` | `roles/aiplatform.ragServiceAgent`  
Gemini Enterprise Agent Platform Custom Code Service Agent |  Custom training code Ray on Agent Platform application code | `service-PROJECT_NUMBER@gcp-sa-aiplatform-cc.iam.gserviceaccount.com` | `roles/aiplatform.customCodeServiceAgent`  
Agent Platform Extension Service Agent | Vertex Extensions | `service-PROJECT_NUMBER@gcp-sa-vertex-ex.iam.gserviceaccount.com` | ``roles/aiplatform.extensionServiceAgent``  
Cloud AI Platform Notebooks Service Account | Agent Platform Workbench capabilities | `service-PROJECT_NUMBER@gcp-sa-notebooks.iam.gserviceaccount.com` | `roles/notebooks.serviceAgent`  
  
The Gemini Enterprise Agent Platform Custom Code Service Agent is created only if you run custom training code to train a custom-trained model.

For Agent Platform to perform tasks like training a model using data from a Cloud Storage bucket, it needs permission to read that data. To handle this securely, Agent Platform uses a Google-managed service account called a Service Agent to access your resources. When you use the Agent Platform API, this Service Agent is automatically granted IAM roles (like [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)) on your project. This is expected and necessary for the service to function. This mechanism allows Agent Platform to access the data it needs for tasks you initiate, while your data remains under your project's access control policies. 

#### Service agent roles and permissions

See the following roles and permissions that are granted to Agent Platform service agents.

Role | Permissions  
---|---  
  
#### Vertex AI Service Agent 

(`roles/aiplatform.serviceAgent`) Gives Vertex AI the permissions it needs to function.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `agentregistry.agents.get` `agentregistry.agents.list` `agentregistry.endpoints.*`

  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`

`agentregistry.mcpServers.get` `agentregistry.mcpServers.list` `agentregistry.operations.*`

  * `agentregistry.operations.cancel`
  * `agentregistry.operations.delete`
  * `agentregistry.operations.get`
  * `agentregistry.operations.list`

`agentregistry.skills.create` `agentregistry.skills.delete` `aiplatform.agentAnomalyDetectionScopes.*`

  * `aiplatform.agentAnomalyDetectionScopes.create`
  * `aiplatform.agentAnomalyDetectionScopes.delete`
  * `aiplatform.agentAnomalyDetectionScopes.get`
  * `aiplatform.agentAnomalyDetectionScopes.list`

`aiplatform.agentExamples.*`

  * `aiplatform.agentExamples.create`
  * `aiplatform.agentExamples.delete`
  * `aiplatform.agentExamples.get`
  * `aiplatform.agentExamples.list`
  * `aiplatform.agentExamples.update`

`aiplatform.agents.create` `aiplatform.agents.delete` `aiplatform.agents.get` `aiplatform.agents.list` `aiplatform.agents.update` `aiplatform.analyzedInvocations.*`

  * `aiplatform.analyzedInvocations.get`
  * `aiplatform.analyzedInvocations.list`

`aiplatform.analyzedSessions.*`

  * `aiplatform.analyzedSessions.aggregate`
  * `aiplatform.analyzedSessions.get`
  * `aiplatform.analyzedSessions.list`

`aiplatform.annotationSpecs.*`

  * `aiplatform.annotationSpecs.create`
  * `aiplatform.annotationSpecs.delete`
  * `aiplatform.annotationSpecs.get`
  * `aiplatform.annotationSpecs.list`
  * `aiplatform.annotationSpecs.update`

`aiplatform.annotations.*`

  * `aiplatform.annotations.create`
  * `aiplatform.annotations.delete`
  * `aiplatform.annotations.get`
  * `aiplatform.annotations.list`
  * `aiplatform.annotations.update`

`aiplatform.apps.*`

  * `aiplatform.apps.create`
  * `aiplatform.apps.delete`
  * `aiplatform.apps.get`
  * `aiplatform.apps.list`
  * `aiplatform.apps.update`

`aiplatform.artifacts.*`

  * `aiplatform.artifacts.create`
  * `aiplatform.artifacts.delete`
  * `aiplatform.artifacts.get`
  * `aiplatform.artifacts.list`
  * `aiplatform.artifacts.update`

`aiplatform.batchPredictionJobs.*`

  * `aiplatform.batchPredictionJobs.cancel`
  * `aiplatform.batchPredictionJobs.create`
  * `aiplatform.batchPredictionJobs.delete`
  * `aiplatform.batchPredictionJobs.get`
  * `aiplatform.batchPredictionJobs.list`

`aiplatform.cacheConfigs.get` `aiplatform.cachedContents.*`

  * `aiplatform.cachedContents.create`
  * `aiplatform.cachedContents.delete`
  * `aiplatform.cachedContents.get`
  * `aiplatform.cachedContents.list`
  * `aiplatform.cachedContents.update`

`aiplatform.consents.get` `aiplatform.contexts.*`

  * `aiplatform.contexts.addContextArtifactsAndExecutions`
  * `aiplatform.contexts.addContextChildren`
  * `aiplatform.contexts.create`
  * `aiplatform.contexts.delete`
  * `aiplatform.contexts.get`
  * `aiplatform.contexts.list`
  * `aiplatform.contexts.queryContextLineageSubgraph`
  * `aiplatform.contexts.update`

`aiplatform.customJobs.*`

  * `aiplatform.customJobs.cancel`
  * `aiplatform.customJobs.create`
  * `aiplatform.customJobs.delete`
  * `aiplatform.customJobs.get`
  * `aiplatform.customJobs.list`

`aiplatform.dataItems.*`

  * `aiplatform.dataItems.create`
  * `aiplatform.dataItems.delete`
  * `aiplatform.dataItems.get`
  * `aiplatform.dataItems.list`
  * `aiplatform.dataItems.update`

`aiplatform.dataLabelingJobs.*`

  * `aiplatform.dataLabelingJobs.cancel`
  * `aiplatform.dataLabelingJobs.create`
  * `aiplatform.dataLabelingJobs.delete`
  * `aiplatform.dataLabelingJobs.get`
  * `aiplatform.dataLabelingJobs.list`

`aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.*`

  * `aiplatform.datasets.create`
  * `aiplatform.datasets.delete`
  * `aiplatform.datasets.export`
  * `aiplatform.datasets.get`
  * `aiplatform.datasets.import`
  * `aiplatform.datasets.list`
  * `aiplatform.datasets.update`

`aiplatform.deploymentResourcePools.*`

  * `aiplatform.deploymentResourcePools.create`
  * `aiplatform.deploymentResourcePools.delete`
  * `aiplatform.deploymentResourcePools.get`
  * `aiplatform.deploymentResourcePools.list`
  * `aiplatform.deploymentResourcePools.queryDeployedModels`
  * `aiplatform.deploymentResourcePools.update`

`aiplatform.edgeDeploymentJobs.*`

  * `aiplatform.edgeDeploymentJobs.create`
  * `aiplatform.edgeDeploymentJobs.delete`
  * `aiplatform.edgeDeploymentJobs.get`
  * `aiplatform.edgeDeploymentJobs.list`

`aiplatform.edgeDeviceDebugInfo.get` `aiplatform.edgeDevices.*`

  * `aiplatform.edgeDevices.create`
  * `aiplatform.edgeDevices.delete`
  * `aiplatform.edgeDevices.get`
  * `aiplatform.edgeDevices.list`
  * `aiplatform.edgeDevices.update`

`aiplatform.endpoints.create` `aiplatform.endpoints.delete` `aiplatform.endpoints.deploy` `aiplatform.endpoints.explain` `aiplatform.endpoints.get` `aiplatform.endpoints.getIamPolicy` `aiplatform.endpoints.list` `aiplatform.endpoints.predict` `aiplatform.endpoints.undeploy` `aiplatform.endpoints.update` `aiplatform.entityTypes.create` `aiplatform.entityTypes.delete` `aiplatform.entityTypes.deleteFeatureValues` `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.getIamPolicy` `aiplatform.entityTypes.importFeatureValues` `aiplatform.entityTypes.list` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.entityTypes.update` `aiplatform.entityTypes.writeFeatureValues` `aiplatform.evaluationExperiments.*`

  * `aiplatform.evaluationExperiments.create`
  * `aiplatform.evaluationExperiments.delete`
  * `aiplatform.evaluationExperiments.get`
  * `aiplatform.evaluationExperiments.list`
  * `aiplatform.evaluationExperiments.update`

`aiplatform.evaluationItems.*`

  * `aiplatform.evaluationItems.create`
  * `aiplatform.evaluationItems.delete`
  * `aiplatform.evaluationItems.get`
  * `aiplatform.evaluationItems.list`
  * `aiplatform.evaluationItems.update`

`aiplatform.evaluationMetrics.*`

  * `aiplatform.evaluationMetrics.create`
  * `aiplatform.evaluationMetrics.delete`
  * `aiplatform.evaluationMetrics.get`
  * `aiplatform.evaluationMetrics.list`

`aiplatform.evaluationRuns.*`

  * `aiplatform.evaluationRuns.cancel`
  * `aiplatform.evaluationRuns.create`
  * `aiplatform.evaluationRuns.delete`
  * `aiplatform.evaluationRuns.execute`
  * `aiplatform.evaluationRuns.get`
  * `aiplatform.evaluationRuns.list`
  * `aiplatform.evaluationRuns.update`

`aiplatform.evaluationSets.*`

  * `aiplatform.evaluationSets.create`
  * `aiplatform.evaluationSets.delete`
  * `aiplatform.evaluationSets.get`
  * `aiplatform.evaluationSets.import`
  * `aiplatform.evaluationSets.list`
  * `aiplatform.evaluationSets.update`

`aiplatform.exampleStores.*`

  * `aiplatform.exampleStores.create`
  * `aiplatform.exampleStores.delete`
  * `aiplatform.exampleStores.get`
  * `aiplatform.exampleStores.list`
  * `aiplatform.exampleStores.readExample`
  * `aiplatform.exampleStores.update`
  * `aiplatform.exampleStores.writeExample`

`aiplatform.executions.*`

  * `aiplatform.executions.addExecutionEvents`
  * `aiplatform.executions.create`
  * `aiplatform.executions.delete`
  * `aiplatform.executions.get`
  * `aiplatform.executions.list`
  * `aiplatform.executions.queryExecutionInputsAndOutputs`
  * `aiplatform.executions.update`

`aiplatform.extensions.*`

  * `aiplatform.extensions.delete`
  * `aiplatform.extensions.execute`
  * `aiplatform.extensions.get`
  * `aiplatform.extensions.import`
  * `aiplatform.extensions.list`
  * `aiplatform.extensions.update`

`aiplatform.featureGroups.create` `aiplatform.featureGroups.delete` `aiplatform.featureGroups.get` `aiplatform.featureGroups.getIamPolicy` `aiplatform.featureGroups.list` `aiplatform.featureGroups.update` `aiplatform.featureMonitorJobs.*`

  * `aiplatform.featureMonitorJobs.create`
  * `aiplatform.featureMonitorJobs.get`
  * `aiplatform.featureMonitorJobs.list`

`aiplatform.featureMonitors.*`

  * `aiplatform.featureMonitors.create`
  * `aiplatform.featureMonitors.delete`
  * `aiplatform.featureMonitors.get`
  * `aiplatform.featureMonitors.list`
  * `aiplatform.featureMonitors.update`

`aiplatform.featureOnlineStores.create` `aiplatform.featureOnlineStores.delete` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.getIamPolicy` `aiplatform.featureOnlineStores.list` `aiplatform.featureOnlineStores.update` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.create` `aiplatform.featureViews.delete` `aiplatform.featureViews.directWrite` `aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.getIamPolicy` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.featureViews.sync` `aiplatform.featureViews.update` `aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.batchReadFeatureValues` `aiplatform.featurestores.create` `aiplatform.featurestores.delete` `aiplatform.featurestores.exportFeatures` `aiplatform.featurestores.get` `aiplatform.featurestores.getIamPolicy` `aiplatform.featurestores.importFeatures` `aiplatform.featurestores.list` `aiplatform.featurestores.readFeatures` `aiplatform.featurestores.update` `aiplatform.featurestores.writeFeatures` `aiplatform.humanInTheLoops.*`

  * `aiplatform.humanInTheLoops.cancel`
  * `aiplatform.humanInTheLoops.create`
  * `aiplatform.humanInTheLoops.delete`
  * `aiplatform.humanInTheLoops.get`
  * `aiplatform.humanInTheLoops.list`
  * `aiplatform.humanInTheLoops.queryAnnotationStats`
  * `aiplatform.humanInTheLoops.send`
  * `aiplatform.humanInTheLoops.update`

`aiplatform.hyperparameterTuningJobs.*`

  * `aiplatform.hyperparameterTuningJobs.cancel`
  * `aiplatform.hyperparameterTuningJobs.create`
  * `aiplatform.hyperparameterTuningJobs.delete`
  * `aiplatform.hyperparameterTuningJobs.get`
  * `aiplatform.hyperparameterTuningJobs.list`

`aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.interactions.*`

  * `aiplatform.interactions.cancel`
  * `aiplatform.interactions.create`
  * `aiplatform.interactions.delete`
  * `aiplatform.interactions.get`
  * `aiplatform.interactions.list`

`aiplatform.locations.*`

  * `aiplatform.locations.evaluateInstances`
  * `aiplatform.locations.get`
  * `aiplatform.locations.list`

`aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.memoryRevisions.*`

  * `aiplatform.memoryRevisions.get`
  * `aiplatform.memoryRevisions.list`
  * `aiplatform.memoryRevisions.rollback`

`aiplatform.metadataSchemas.*`

  * `aiplatform.metadataSchemas.create`
  * `aiplatform.metadataSchemas.delete`
  * `aiplatform.metadataSchemas.get`
  * `aiplatform.metadataSchemas.list`

`aiplatform.metadataStores.*`

  * `aiplatform.metadataStores.create`
  * `aiplatform.metadataStores.delete`
  * `aiplatform.metadataStores.get`
  * `aiplatform.metadataStores.list`

`aiplatform.migratableResources.search` `aiplatform.modelDeploymentMonitoringJobs.*`

  * `aiplatform.modelDeploymentMonitoringJobs.create`
  * `aiplatform.modelDeploymentMonitoringJobs.delete`
  * `aiplatform.modelDeploymentMonitoringJobs.get`
  * `aiplatform.modelDeploymentMonitoringJobs.list`
  * `aiplatform.modelDeploymentMonitoringJobs.pause`
  * `aiplatform.modelDeploymentMonitoringJobs.resume`
  * `aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`
  * `aiplatform.modelDeploymentMonitoringJobs.update`

`aiplatform.modelEvaluationSlices.*`

  * `aiplatform.modelEvaluationSlices.get`
  * `aiplatform.modelEvaluationSlices.import`
  * `aiplatform.modelEvaluationSlices.list`

`aiplatform.modelEvaluations.*`

  * `aiplatform.modelEvaluations.exportEvaluatedDataItems`
  * `aiplatform.modelEvaluations.get`
  * `aiplatform.modelEvaluations.import`
  * `aiplatform.modelEvaluations.list`

`aiplatform.modelMonitoringJobs.*`

  * `aiplatform.modelMonitoringJobs.create`
  * `aiplatform.modelMonitoringJobs.delete`
  * `aiplatform.modelMonitoringJobs.get`
  * `aiplatform.modelMonitoringJobs.list`

`aiplatform.modelMonitors.*`

  * `aiplatform.modelMonitors.create`
  * `aiplatform.modelMonitors.delete`
  * `aiplatform.modelMonitors.get`
  * `aiplatform.modelMonitors.list`
  * `aiplatform.modelMonitors.searchModelMonitoringAlerts`
  * `aiplatform.modelMonitors.searchModelMonitoringStats`
  * `aiplatform.modelMonitors.update`

`aiplatform.models.*`

  * `aiplatform.models.delete`
  * `aiplatform.models.export`
  * `aiplatform.models.get`
  * `aiplatform.models.list`
  * `aiplatform.models.update`
  * `aiplatform.models.upload`

`aiplatform.monitoredAgents.disable` `aiplatform.monitoredAgents.enable` `aiplatform.monitoredAgents.get` `aiplatform.monitoredAgents.list` `aiplatform.nasJobs.*`

  * `aiplatform.nasJobs.cancel`
  * `aiplatform.nasJobs.create`
  * `aiplatform.nasJobs.delete`
  * `aiplatform.nasJobs.get`
  * `aiplatform.nasJobs.list`

`aiplatform.nasTrialDetails.*`

  * `aiplatform.nasTrialDetails.get`
  * `aiplatform.nasTrialDetails.list`

`aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.create` `aiplatform.notebookRuntimeTemplates.delete` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimeTemplates.update` `aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.onlineEvaluators.*`

  * `aiplatform.onlineEvaluators.create`
  * `aiplatform.onlineEvaluators.delete`
  * `aiplatform.onlineEvaluators.get`
  * `aiplatform.onlineEvaluators.list`
  * `aiplatform.onlineEvaluators.update`

`aiplatform.operations.list` `aiplatform.persistentResources.get` `aiplatform.persistentResources.list` `aiplatform.pipelineJobs.*`

  * `aiplatform.pipelineJobs.cancel`
  * `aiplatform.pipelineJobs.create`
  * `aiplatform.pipelineJobs.delete`
  * `aiplatform.pipelineJobs.get`
  * `aiplatform.pipelineJobs.list`

`aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.get` `aiplatform.provisionedThroughputs.list` `aiplatform.ragCorpora.*`

  * `aiplatform.ragCorpora.create`
  * `aiplatform.ragCorpora.delete`
  * `aiplatform.ragCorpora.get`
  * `aiplatform.ragCorpora.list`
  * `aiplatform.ragCorpora.query`
  * `aiplatform.ragCorpora.update`

`aiplatform.ragEngineConfigs.get` `aiplatform.ragFiles.*`

  * `aiplatform.ragFiles.delete`
  * `aiplatform.ragFiles.get`
  * `aiplatform.ragFiles.import`
  * `aiplatform.ragFiles.list`
  * `aiplatform.ragFiles.upload`

`aiplatform.reasoningEngineRuntimeRevisions.*`

  * `aiplatform.reasoningEngineRuntimeRevisions.delete`
  * `aiplatform.reasoningEngineRuntimeRevisions.get`
  * `aiplatform.reasoningEngineRuntimeRevisions.list`
  * `aiplatform.reasoningEngineRuntimeRevisions.query`

`aiplatform.reasoningEngines.create` `aiplatform.reasoningEngines.delete` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.reasoningEngines.update` `aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`aiplatform.semanticGovernancePolicies.*`

  * `aiplatform.semanticGovernancePolicies.create`
  * `aiplatform.semanticGovernancePolicies.delete`
  * `aiplatform.semanticGovernancePolicies.get`
  * `aiplatform.semanticGovernancePolicies.list`
  * `aiplatform.semanticGovernancePolicies.update`

`aiplatform.semanticGovernancePolicyEngine.*`

  * `aiplatform.semanticGovernancePolicyEngine.get`
  * `aiplatform.semanticGovernancePolicyEngine.update`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.*`

  * `aiplatform.sessions.create`
  * `aiplatform.sessions.delete`
  * `aiplatform.sessions.get`
  * `aiplatform.sessions.list`
  * `aiplatform.sessions.run`
  * `aiplatform.sessions.update`

`aiplatform.specialistPools.*`

  * `aiplatform.specialistPools.create`
  * `aiplatform.specialistPools.delete`
  * `aiplatform.specialistPools.get`
  * `aiplatform.specialistPools.list`
  * `aiplatform.specialistPools.update`

`aiplatform.studies.*`

  * `aiplatform.studies.create`
  * `aiplatform.studies.delete`
  * `aiplatform.studies.get`
  * `aiplatform.studies.list`
  * `aiplatform.studies.update`

`aiplatform.tasks.*`

  * `aiplatform.tasks.cancel`
  * `aiplatform.tasks.create`
  * `aiplatform.tasks.delete`
  * `aiplatform.tasks.get`
  * `aiplatform.tasks.list`
  * `aiplatform.tasks.update`

`aiplatform.tensorboardExperiments.*`

  * `aiplatform.tensorboardExperiments.create`
  * `aiplatform.tensorboardExperiments.delete`
  * `aiplatform.tensorboardExperiments.get`
  * `aiplatform.tensorboardExperiments.list`
  * `aiplatform.tensorboardExperiments.update`
  * `aiplatform.tensorboardExperiments.write`

`aiplatform.tensorboardRuns.*`

  * `aiplatform.tensorboardRuns.batchCreate`
  * `aiplatform.tensorboardRuns.create`
  * `aiplatform.tensorboardRuns.delete`
  * `aiplatform.tensorboardRuns.get`
  * `aiplatform.tensorboardRuns.list`
  * `aiplatform.tensorboardRuns.update`
  * `aiplatform.tensorboardRuns.write`

`aiplatform.tensorboardTimeSeries.*`

  * `aiplatform.tensorboardTimeSeries.batchCreate`
  * `aiplatform.tensorboardTimeSeries.batchRead`
  * `aiplatform.tensorboardTimeSeries.create`
  * `aiplatform.tensorboardTimeSeries.delete`
  * `aiplatform.tensorboardTimeSeries.get`
  * `aiplatform.tensorboardTimeSeries.list`
  * `aiplatform.tensorboardTimeSeries.read`
  * `aiplatform.tensorboardTimeSeries.update`

`aiplatform.tensorboards.create` `aiplatform.tensorboards.delete` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.tensorboards.update` `aiplatform.trainingPipelines.*`

  * `aiplatform.trainingPipelines.cancel`
  * `aiplatform.trainingPipelines.create`
  * `aiplatform.trainingPipelines.delete`
  * `aiplatform.trainingPipelines.get`
  * `aiplatform.trainingPipelines.list`

`aiplatform.trials.*`

  * `aiplatform.trials.create`
  * `aiplatform.trials.delete`
  * `aiplatform.trials.get`
  * `aiplatform.trials.list`
  * `aiplatform.trials.update`

`aiplatform.tuningJobs.*`

  * `aiplatform.tuningJobs.cancel`
  * `aiplatform.tuningJobs.create`
  * `aiplatform.tuningJobs.delete`
  * `aiplatform.tuningJobs.get`
  * `aiplatform.tuningJobs.list`
  * `aiplatform.tuningJobs.optimizePrompt`
  * `aiplatform.tuningJobs.validateReinforcementTuningReward`
  * `aiplatform.tuningJobs.vertexTune`

`artifactregistry.repositories.create` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.get` `artifactregistry.versions.get` `automl.datasets.export` `automl.datasets.get` `automl.datasets.list` `automl.modelEvaluations.list` `automl.models.get` `automl.models.list` `automl.operations.get` `automl.tableSpecs.get` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.models.create` `bigquery.models.export` `bigquery.models.getData` `bigquery.objectRefs.read` `bigquery.readsessions.create` `bigquery.readsessions.getData` `bigquery.tables.create` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `bigtable.tables.get` `bigtable.tables.list` `bigtable.tables.readRows` `binaryauthorization.policy.evaluatePolicy` `cloudtrace.traces.get` `cloudtrace.traces.list` `compute.addresses.get` `compute.addresses.list` `compute.addresses.use` `compute.addresses.useInternal` `compute.disks.create` `compute.disks.createSnapshot` `compute.disks.createTagBinding` `compute.disks.delete` `compute.disks.get` `compute.disks.setLabels` `compute.disks.use` `compute.disks.useReadOnly` `compute.globalOperations.get` `compute.instanceGroupManagers.update` `compute.instances.attachDisk` `compute.instances.create` `compute.instances.createTagBinding` `compute.instances.delete` `compute.instances.detachDisk` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.list` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setServiceAccount` `compute.instances.setTags` `compute.instances.start` `compute.instances.stop` `compute.instances.update` `compute.instances.useReadOnly` `compute.machineTypes.get` `compute.networks.get` `compute.networks.use` `compute.networks.useExternalIp` `compute.snapshots.create` `compute.snapshots.delete` `compute.snapshots.useReadOnly` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.zoneOperations.get` `dataflow.jobs.*`

  * `dataflow.jobs.cancel`
  * `dataflow.jobs.create`
  * `dataflow.jobs.get`
  * `dataflow.jobs.list`
  * `dataflow.jobs.snapshot`
  * `dataflow.jobs.updateContents`

`dataflow.messages.list` `dataflow.metrics.get` `dataflow.snapshots.*`

  * `dataflow.snapshots.delete`
  * `dataflow.snapshots.get`
  * `dataflow.snapshots.list`

`datalabeling.annotateddatasets.get` `datalabeling.datasets.export` `datalabeling.datasets.get` `datalabeling.datasets.list` `datalabeling.operations.get` `hypercomputecluster.clusters.*`

  * `hypercomputecluster.clusters.create`
  * `hypercomputecluster.clusters.delete`
  * `hypercomputecluster.clusters.get`
  * `hypercomputecluster.clusters.list`
  * `hypercomputecluster.clusters.update`

`hypercomputecluster.locations.*`

  * `hypercomputecluster.locations.get`
  * `hypercomputecluster.locations.list`

`hypercomputecluster.operations.*`

  * `hypercomputecluster.operations.cancel`
  * `hypercomputecluster.operations.delete`
  * `hypercomputecluster.operations.get`
  * `hypercomputecluster.operations.list`

`iam.serviceAccounts.actAs` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `logging.links.*`

  * `logging.links.create`
  * `logging.links.delete`
  * `logging.links.get`
  * `logging.links.list`

`logging.logEntries.create` `logging.logEntries.route` `logging.operations.get` `logging.operations.list` `logging.views.access` `logging.views.get` `ml.models.list` `ml.operations.get` `ml.versions.get` `ml.versions.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.timeSeries.create` `networkservices.agentGateways.get` `networkservices.agentGateways.use` `networkservices.operations.get` `notebooks.instances.create` `notebooks.instances.delete` `notebooks.instances.get` `observability.links.create` `observability.links.delete` `observability.links.get` `observability.links.list` `observability.operations.get` `observability.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `run.executions.delete` `run.executions.get` `run.jobs.create` `run.jobs.delete` `run.jobs.get` `run.jobs.run` `run.jobs.update` `run.operations.delete` `run.operations.get` `run.routes.invoke` `run.services.create` `run.services.delete` `run.services.get` `servicemanagement.services.report` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.folders.create` `storage.folders.delete` `storage.folders.get` `storage.folders.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Vertex AI RAG Data Service Agent 

(`roles/aiplatform.ragServiceAgent`) Vertex AI Service Agent used by Vertex RAG to access user imported data, Vertex AI, Document AI processors, and Vector Search in the project  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.get` `aiplatform.endpoints.predict` `aiplatform.featureViews.get` `aiplatform.featureViews.list` `aiplatform.featureViews.sync` `aiplatform.featureViews.update` `aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.models.get` `aiplatform.ragCorpora.get` `aiplatform.ragCorpora.list` `aiplatform.ragCorpora.query` `aiplatform.ragFiles.get` `aiplatform.ragFiles.list` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.readsessions.create` `bigquery.readsessions.getData` `bigquery.tables.create` `bigquery.tables.createSnapshot` `bigquery.tables.deleteSnapshot` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.restoreSnapshot` `bigquery.tables.update` `bigquery.tables.updateData` `documentai.processorVersions.processOnline` `documentai.processors.get` `documentai.processors.processOnline` `logging.logEntries.create` `logging.logEntries.route` `storage.buckets.get` `storage.buckets.list` `storage.objects.get` `storage.objects.list` `vectorsearch.collections.*`

  * `vectorsearch.collections.create`
  * `vectorsearch.collections.delete`
  * `vectorsearch.collections.get`
  * `vectorsearch.collections.list`
  * `vectorsearch.collections.update`

`vectorsearch.dataObjects.create` `vectorsearch.dataObjects.delete` `vectorsearch.dataObjects.get` `vectorsearch.dataObjects.import` `vectorsearch.dataObjects.query` `vectorsearch.dataObjects.search` `vectorsearch.dataObjects.update` `vectorsearch.indexes.create` `vectorsearch.indexes.delete` `vectorsearch.indexes.get` `vectorsearch.indexes.list` `vectorsearch.operations.get` `vectorsearch.operations.list`  
  
#### Vertex AI Custom Code Service Agent 

(`roles/aiplatform.customCodeServiceAgent`) Gives Vertex AI Custom Code the proper permissions. The aiplatform.customJobs.create IAM permission is highly privileged. Through Vertex AI Custom Training jobs, it effectively grants editor-level access to other services activated for the consumer project, such as GCS and BigQuery.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.agentAnomalyDetectionScopes.*`

  * `aiplatform.agentAnomalyDetectionScopes.create`
  * `aiplatform.agentAnomalyDetectionScopes.delete`
  * `aiplatform.agentAnomalyDetectionScopes.get`
  * `aiplatform.agentAnomalyDetectionScopes.list`

`aiplatform.agentExamples.*`

  * `aiplatform.agentExamples.create`
  * `aiplatform.agentExamples.delete`
  * `aiplatform.agentExamples.get`
  * `aiplatform.agentExamples.list`
  * `aiplatform.agentExamples.update`

`aiplatform.agents.create` `aiplatform.agents.delete` `aiplatform.agents.get` `aiplatform.agents.list` `aiplatform.agents.update` `aiplatform.analyzedInvocations.*`

  * `aiplatform.analyzedInvocations.get`
  * `aiplatform.analyzedInvocations.list`

`aiplatform.analyzedSessions.*`

  * `aiplatform.analyzedSessions.aggregate`
  * `aiplatform.analyzedSessions.get`
  * `aiplatform.analyzedSessions.list`

`aiplatform.annotationSpecs.*`

  * `aiplatform.annotationSpecs.create`
  * `aiplatform.annotationSpecs.delete`
  * `aiplatform.annotationSpecs.get`
  * `aiplatform.annotationSpecs.list`
  * `aiplatform.annotationSpecs.update`

`aiplatform.annotations.*`

  * `aiplatform.annotations.create`
  * `aiplatform.annotations.delete`
  * `aiplatform.annotations.get`
  * `aiplatform.annotations.list`
  * `aiplatform.annotations.update`

`aiplatform.apps.*`

  * `aiplatform.apps.create`
  * `aiplatform.apps.delete`
  * `aiplatform.apps.get`
  * `aiplatform.apps.list`
  * `aiplatform.apps.update`

`aiplatform.artifacts.*`

  * `aiplatform.artifacts.create`
  * `aiplatform.artifacts.delete`
  * `aiplatform.artifacts.get`
  * `aiplatform.artifacts.list`
  * `aiplatform.artifacts.update`

`aiplatform.batchPredictionJobs.*`

  * `aiplatform.batchPredictionJobs.cancel`
  * `aiplatform.batchPredictionJobs.create`
  * `aiplatform.batchPredictionJobs.delete`
  * `aiplatform.batchPredictionJobs.get`
  * `aiplatform.batchPredictionJobs.list`

`aiplatform.cacheConfigs.get` `aiplatform.cachedContents.*`

  * `aiplatform.cachedContents.create`
  * `aiplatform.cachedContents.delete`
  * `aiplatform.cachedContents.get`
  * `aiplatform.cachedContents.list`
  * `aiplatform.cachedContents.update`

`aiplatform.consents.get` `aiplatform.contexts.*`

  * `aiplatform.contexts.addContextArtifactsAndExecutions`
  * `aiplatform.contexts.addContextChildren`
  * `aiplatform.contexts.create`
  * `aiplatform.contexts.delete`
  * `aiplatform.contexts.get`
  * `aiplatform.contexts.list`
  * `aiplatform.contexts.queryContextLineageSubgraph`
  * `aiplatform.contexts.update`

`aiplatform.customJobs.*`

  * `aiplatform.customJobs.cancel`
  * `aiplatform.customJobs.create`
  * `aiplatform.customJobs.delete`
  * `aiplatform.customJobs.get`
  * `aiplatform.customJobs.list`

`aiplatform.dataItems.*`

  * `aiplatform.dataItems.create`
  * `aiplatform.dataItems.delete`
  * `aiplatform.dataItems.get`
  * `aiplatform.dataItems.list`
  * `aiplatform.dataItems.update`

`aiplatform.dataLabelingJobs.*`

  * `aiplatform.dataLabelingJobs.cancel`
  * `aiplatform.dataLabelingJobs.create`
  * `aiplatform.dataLabelingJobs.delete`
  * `aiplatform.dataLabelingJobs.get`
  * `aiplatform.dataLabelingJobs.list`

`aiplatform.datasetVersions.*`

  * `aiplatform.datasetVersions.create`
  * `aiplatform.datasetVersions.delete`
  * `aiplatform.datasetVersions.get`
  * `aiplatform.datasetVersions.list`
  * `aiplatform.datasetVersions.restore`

`aiplatform.datasets.*`

  * `aiplatform.datasets.create`
  * `aiplatform.datasets.delete`
  * `aiplatform.datasets.export`
  * `aiplatform.datasets.get`
  * `aiplatform.datasets.import`
  * `aiplatform.datasets.list`
  * `aiplatform.datasets.update`

`aiplatform.deploymentResourcePools.*`

  * `aiplatform.deploymentResourcePools.create`
  * `aiplatform.deploymentResourcePools.delete`
  * `aiplatform.deploymentResourcePools.get`
  * `aiplatform.deploymentResourcePools.list`
  * `aiplatform.deploymentResourcePools.queryDeployedModels`
  * `aiplatform.deploymentResourcePools.update`

`aiplatform.edgeDeploymentJobs.*`

  * `aiplatform.edgeDeploymentJobs.create`
  * `aiplatform.edgeDeploymentJobs.delete`
  * `aiplatform.edgeDeploymentJobs.get`
  * `aiplatform.edgeDeploymentJobs.list`

`aiplatform.edgeDeviceDebugInfo.get` `aiplatform.edgeDevices.*`

  * `aiplatform.edgeDevices.create`
  * `aiplatform.edgeDevices.delete`
  * `aiplatform.edgeDevices.get`
  * `aiplatform.edgeDevices.list`
  * `aiplatform.edgeDevices.update`

`aiplatform.endpoints.create` `aiplatform.endpoints.delete` `aiplatform.endpoints.deploy` `aiplatform.endpoints.explain` `aiplatform.endpoints.get` `aiplatform.endpoints.getIamPolicy` `aiplatform.endpoints.list` `aiplatform.endpoints.predict` `aiplatform.endpoints.undeploy` `aiplatform.endpoints.update` `aiplatform.entityTypes.create` `aiplatform.entityTypes.delete` `aiplatform.entityTypes.deleteFeatureValues` `aiplatform.entityTypes.exportFeatureValues` `aiplatform.entityTypes.get` `aiplatform.entityTypes.getIamPolicy` `aiplatform.entityTypes.importFeatureValues` `aiplatform.entityTypes.list` `aiplatform.entityTypes.readFeatureValues` `aiplatform.entityTypes.streamingReadFeatureValues` `aiplatform.entityTypes.update` `aiplatform.entityTypes.writeFeatureValues` `aiplatform.evaluationExperiments.*`

  * `aiplatform.evaluationExperiments.create`
  * `aiplatform.evaluationExperiments.delete`
  * `aiplatform.evaluationExperiments.get`
  * `aiplatform.evaluationExperiments.list`
  * `aiplatform.evaluationExperiments.update`

`aiplatform.evaluationItems.*`

  * `aiplatform.evaluationItems.create`
  * `aiplatform.evaluationItems.delete`
  * `aiplatform.evaluationItems.get`
  * `aiplatform.evaluationItems.list`
  * `aiplatform.evaluationItems.update`

`aiplatform.evaluationMetrics.*`

  * `aiplatform.evaluationMetrics.create`
  * `aiplatform.evaluationMetrics.delete`
  * `aiplatform.evaluationMetrics.get`
  * `aiplatform.evaluationMetrics.list`

`aiplatform.evaluationRuns.*`

  * `aiplatform.evaluationRuns.cancel`
  * `aiplatform.evaluationRuns.create`
  * `aiplatform.evaluationRuns.delete`
  * `aiplatform.evaluationRuns.execute`
  * `aiplatform.evaluationRuns.get`
  * `aiplatform.evaluationRuns.list`
  * `aiplatform.evaluationRuns.update`

`aiplatform.evaluationSets.*`

  * `aiplatform.evaluationSets.create`
  * `aiplatform.evaluationSets.delete`
  * `aiplatform.evaluationSets.get`
  * `aiplatform.evaluationSets.import`
  * `aiplatform.evaluationSets.list`
  * `aiplatform.evaluationSets.update`

`aiplatform.exampleStores.*`

  * `aiplatform.exampleStores.create`
  * `aiplatform.exampleStores.delete`
  * `aiplatform.exampleStores.get`
  * `aiplatform.exampleStores.list`
  * `aiplatform.exampleStores.readExample`
  * `aiplatform.exampleStores.update`
  * `aiplatform.exampleStores.writeExample`

`aiplatform.executions.*`

  * `aiplatform.executions.addExecutionEvents`
  * `aiplatform.executions.create`
  * `aiplatform.executions.delete`
  * `aiplatform.executions.get`
  * `aiplatform.executions.list`
  * `aiplatform.executions.queryExecutionInputsAndOutputs`
  * `aiplatform.executions.update`

`aiplatform.extensions.*`

  * `aiplatform.extensions.delete`
  * `aiplatform.extensions.execute`
  * `aiplatform.extensions.get`
  * `aiplatform.extensions.import`
  * `aiplatform.extensions.list`
  * `aiplatform.extensions.update`

`aiplatform.featureGroups.create` `aiplatform.featureGroups.delete` `aiplatform.featureGroups.get` `aiplatform.featureGroups.getIamPolicy` `aiplatform.featureGroups.list` `aiplatform.featureGroups.update` `aiplatform.featureMonitorJobs.*`

  * `aiplatform.featureMonitorJobs.create`
  * `aiplatform.featureMonitorJobs.get`
  * `aiplatform.featureMonitorJobs.list`

`aiplatform.featureMonitors.*`

  * `aiplatform.featureMonitors.create`
  * `aiplatform.featureMonitors.delete`
  * `aiplatform.featureMonitors.get`
  * `aiplatform.featureMonitors.list`
  * `aiplatform.featureMonitors.update`

`aiplatform.featureOnlineStores.create` `aiplatform.featureOnlineStores.delete` `aiplatform.featureOnlineStores.get` `aiplatform.featureOnlineStores.getIamPolicy` `aiplatform.featureOnlineStores.list` `aiplatform.featureOnlineStores.update` `aiplatform.featureViewSyncs.*`

  * `aiplatform.featureViewSyncs.get`
  * `aiplatform.featureViewSyncs.list`

`aiplatform.featureViews.create` `aiplatform.featureViews.delete` `aiplatform.featureViews.directWrite` `aiplatform.featureViews.fetchFeatureValues` `aiplatform.featureViews.get` `aiplatform.featureViews.getIamPolicy` `aiplatform.featureViews.list` `aiplatform.featureViews.searchNearestEntities` `aiplatform.featureViews.sync` `aiplatform.featureViews.update` `aiplatform.features.*`

  * `aiplatform.features.create`
  * `aiplatform.features.delete`
  * `aiplatform.features.get`
  * `aiplatform.features.list`
  * `aiplatform.features.update`

`aiplatform.featurestores.batchReadFeatureValues` `aiplatform.featurestores.create` `aiplatform.featurestores.delete` `aiplatform.featurestores.exportFeatures` `aiplatform.featurestores.get` `aiplatform.featurestores.getIamPolicy` `aiplatform.featurestores.importFeatures` `aiplatform.featurestores.list` `aiplatform.featurestores.readFeatures` `aiplatform.featurestores.update` `aiplatform.featurestores.writeFeatures` `aiplatform.humanInTheLoops.*`

  * `aiplatform.humanInTheLoops.cancel`
  * `aiplatform.humanInTheLoops.create`
  * `aiplatform.humanInTheLoops.delete`
  * `aiplatform.humanInTheLoops.get`
  * `aiplatform.humanInTheLoops.list`
  * `aiplatform.humanInTheLoops.queryAnnotationStats`
  * `aiplatform.humanInTheLoops.send`
  * `aiplatform.humanInTheLoops.update`

`aiplatform.hyperparameterTuningJobs.*`

  * `aiplatform.hyperparameterTuningJobs.cancel`
  * `aiplatform.hyperparameterTuningJobs.create`
  * `aiplatform.hyperparameterTuningJobs.delete`
  * `aiplatform.hyperparameterTuningJobs.get`
  * `aiplatform.hyperparameterTuningJobs.list`

`aiplatform.indexEndpoints.*`

  * `aiplatform.indexEndpoints.create`
  * `aiplatform.indexEndpoints.delete`
  * `aiplatform.indexEndpoints.deploy`
  * `aiplatform.indexEndpoints.get`
  * `aiplatform.indexEndpoints.list`
  * `aiplatform.indexEndpoints.queryVectors`
  * `aiplatform.indexEndpoints.undeploy`
  * `aiplatform.indexEndpoints.update`

`aiplatform.indexes.*`

  * `aiplatform.indexes.create`
  * `aiplatform.indexes.delete`
  * `aiplatform.indexes.get`
  * `aiplatform.indexes.list`
  * `aiplatform.indexes.update`

`aiplatform.interactions.*`

  * `aiplatform.interactions.cancel`
  * `aiplatform.interactions.create`
  * `aiplatform.interactions.delete`
  * `aiplatform.interactions.get`
  * `aiplatform.interactions.list`

`aiplatform.locations.*`

  * `aiplatform.locations.evaluateInstances`
  * `aiplatform.locations.get`
  * `aiplatform.locations.list`

`aiplatform.memories.*`

  * `aiplatform.memories.create`
  * `aiplatform.memories.delete`
  * `aiplatform.memories.generate`
  * `aiplatform.memories.get`
  * `aiplatform.memories.list`
  * `aiplatform.memories.retrieve`
  * `aiplatform.memories.update`

`aiplatform.memoryRevisions.*`

  * `aiplatform.memoryRevisions.get`
  * `aiplatform.memoryRevisions.list`
  * `aiplatform.memoryRevisions.rollback`

`aiplatform.metadataSchemas.*`

  * `aiplatform.metadataSchemas.create`
  * `aiplatform.metadataSchemas.delete`
  * `aiplatform.metadataSchemas.get`
  * `aiplatform.metadataSchemas.list`

`aiplatform.metadataStores.*`

  * `aiplatform.metadataStores.create`
  * `aiplatform.metadataStores.delete`
  * `aiplatform.metadataStores.get`
  * `aiplatform.metadataStores.list`

`aiplatform.migratableResources.search` `aiplatform.modelDeploymentMonitoringJobs.*`

  * `aiplatform.modelDeploymentMonitoringJobs.create`
  * `aiplatform.modelDeploymentMonitoringJobs.delete`
  * `aiplatform.modelDeploymentMonitoringJobs.get`
  * `aiplatform.modelDeploymentMonitoringJobs.list`
  * `aiplatform.modelDeploymentMonitoringJobs.pause`
  * `aiplatform.modelDeploymentMonitoringJobs.resume`
  * `aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`
  * `aiplatform.modelDeploymentMonitoringJobs.update`

`aiplatform.modelEvaluationSlices.*`

  * `aiplatform.modelEvaluationSlices.get`
  * `aiplatform.modelEvaluationSlices.import`
  * `aiplatform.modelEvaluationSlices.list`

`aiplatform.modelEvaluations.*`

  * `aiplatform.modelEvaluations.exportEvaluatedDataItems`
  * `aiplatform.modelEvaluations.get`
  * `aiplatform.modelEvaluations.import`
  * `aiplatform.modelEvaluations.list`

`aiplatform.modelMonitoringJobs.*`

  * `aiplatform.modelMonitoringJobs.create`
  * `aiplatform.modelMonitoringJobs.delete`
  * `aiplatform.modelMonitoringJobs.get`
  * `aiplatform.modelMonitoringJobs.list`

`aiplatform.modelMonitors.*`

  * `aiplatform.modelMonitors.create`
  * `aiplatform.modelMonitors.delete`
  * `aiplatform.modelMonitors.get`
  * `aiplatform.modelMonitors.list`
  * `aiplatform.modelMonitors.searchModelMonitoringAlerts`
  * `aiplatform.modelMonitors.searchModelMonitoringStats`
  * `aiplatform.modelMonitors.update`

`aiplatform.models.*`

  * `aiplatform.models.delete`
  * `aiplatform.models.export`
  * `aiplatform.models.get`
  * `aiplatform.models.list`
  * `aiplatform.models.update`
  * `aiplatform.models.upload`

`aiplatform.monitoredAgents.disable` `aiplatform.monitoredAgents.enable` `aiplatform.monitoredAgents.get` `aiplatform.monitoredAgents.list` `aiplatform.nasJobs.*`

  * `aiplatform.nasJobs.cancel`
  * `aiplatform.nasJobs.create`
  * `aiplatform.nasJobs.delete`
  * `aiplatform.nasJobs.get`
  * `aiplatform.nasJobs.list`

`aiplatform.nasTrialDetails.*`

  * `aiplatform.nasTrialDetails.get`
  * `aiplatform.nasTrialDetails.list`

`aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimeTemplates.apply` `aiplatform.notebookRuntimeTemplates.create` `aiplatform.notebookRuntimeTemplates.delete` `aiplatform.notebookRuntimeTemplates.get` `aiplatform.notebookRuntimeTemplates.getIamPolicy` `aiplatform.notebookRuntimeTemplates.list` `aiplatform.notebookRuntimeTemplates.update` `aiplatform.notebookRuntimes.*`

  * `aiplatform.notebookRuntimes.assign`
  * `aiplatform.notebookRuntimes.delete`
  * `aiplatform.notebookRuntimes.get`
  * `aiplatform.notebookRuntimes.list`
  * `aiplatform.notebookRuntimes.start`
  * `aiplatform.notebookRuntimes.update`
  * `aiplatform.notebookRuntimes.upgrade`

`aiplatform.onlineEvaluators.*`

  * `aiplatform.onlineEvaluators.create`
  * `aiplatform.onlineEvaluators.delete`
  * `aiplatform.onlineEvaluators.get`
  * `aiplatform.onlineEvaluators.list`
  * `aiplatform.onlineEvaluators.update`

`aiplatform.operations.list` `aiplatform.persistentResources.get` `aiplatform.persistentResources.list` `aiplatform.pipelineJobs.*`

  * `aiplatform.pipelineJobs.cancel`
  * `aiplatform.pipelineJobs.create`
  * `aiplatform.pipelineJobs.delete`
  * `aiplatform.pipelineJobs.get`
  * `aiplatform.pipelineJobs.list`

`aiplatform.provisionedThroughputRevisions.*`

  * `aiplatform.provisionedThroughputRevisions.get`
  * `aiplatform.provisionedThroughputRevisions.list`

`aiplatform.provisionedThroughputs.get` `aiplatform.provisionedThroughputs.list` `aiplatform.ragCorpora.*`

  * `aiplatform.ragCorpora.create`
  * `aiplatform.ragCorpora.delete`
  * `aiplatform.ragCorpora.get`
  * `aiplatform.ragCorpora.list`
  * `aiplatform.ragCorpora.query`
  * `aiplatform.ragCorpora.update`

`aiplatform.ragEngineConfigs.get` `aiplatform.ragFiles.*`

  * `aiplatform.ragFiles.delete`
  * `aiplatform.ragFiles.get`
  * `aiplatform.ragFiles.import`
  * `aiplatform.ragFiles.list`
  * `aiplatform.ragFiles.upload`

`aiplatform.reasoningEngineRuntimeRevisions.*`

  * `aiplatform.reasoningEngineRuntimeRevisions.delete`
  * `aiplatform.reasoningEngineRuntimeRevisions.get`
  * `aiplatform.reasoningEngineRuntimeRevisions.list`
  * `aiplatform.reasoningEngineRuntimeRevisions.query`

`aiplatform.reasoningEngines.create` `aiplatform.reasoningEngines.delete` `aiplatform.reasoningEngines.get` `aiplatform.reasoningEngines.list` `aiplatform.reasoningEngines.query` `aiplatform.reasoningEngines.update` `aiplatform.sandboxEnvironments.*`

  * `aiplatform.sandboxEnvironments.create`
  * `aiplatform.sandboxEnvironments.delete`
  * `aiplatform.sandboxEnvironments.execute`
  * `aiplatform.sandboxEnvironments.get`
  * `aiplatform.sandboxEnvironments.list`

`aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`aiplatform.semanticGovernancePolicies.*`

  * `aiplatform.semanticGovernancePolicies.create`
  * `aiplatform.semanticGovernancePolicies.delete`
  * `aiplatform.semanticGovernancePolicies.get`
  * `aiplatform.semanticGovernancePolicies.list`
  * `aiplatform.semanticGovernancePolicies.update`

`aiplatform.semanticGovernancePolicyEngine.*`

  * `aiplatform.semanticGovernancePolicyEngine.get`
  * `aiplatform.semanticGovernancePolicyEngine.update`

`aiplatform.sessionEvents.*`

  * `aiplatform.sessionEvents.append`
  * `aiplatform.sessionEvents.list`

`aiplatform.sessions.*`

  * `aiplatform.sessions.create`
  * `aiplatform.sessions.delete`
  * `aiplatform.sessions.get`
  * `aiplatform.sessions.list`
  * `aiplatform.sessions.run`
  * `aiplatform.sessions.update`

`aiplatform.specialistPools.*`

  * `aiplatform.specialistPools.create`
  * `aiplatform.specialistPools.delete`
  * `aiplatform.specialistPools.get`
  * `aiplatform.specialistPools.list`
  * `aiplatform.specialistPools.update`

`aiplatform.studies.*`

  * `aiplatform.studies.create`
  * `aiplatform.studies.delete`
  * `aiplatform.studies.get`
  * `aiplatform.studies.list`
  * `aiplatform.studies.update`

`aiplatform.tasks.*`

  * `aiplatform.tasks.cancel`
  * `aiplatform.tasks.create`
  * `aiplatform.tasks.delete`
  * `aiplatform.tasks.get`
  * `aiplatform.tasks.list`
  * `aiplatform.tasks.update`

`aiplatform.tensorboardExperiments.*`

  * `aiplatform.tensorboardExperiments.create`
  * `aiplatform.tensorboardExperiments.delete`
  * `aiplatform.tensorboardExperiments.get`
  * `aiplatform.tensorboardExperiments.list`
  * `aiplatform.tensorboardExperiments.update`
  * `aiplatform.tensorboardExperiments.write`

`aiplatform.tensorboardRuns.*`

  * `aiplatform.tensorboardRuns.batchCreate`
  * `aiplatform.tensorboardRuns.create`
  * `aiplatform.tensorboardRuns.delete`
  * `aiplatform.tensorboardRuns.get`
  * `aiplatform.tensorboardRuns.list`
  * `aiplatform.tensorboardRuns.update`
  * `aiplatform.tensorboardRuns.write`

`aiplatform.tensorboardTimeSeries.*`

  * `aiplatform.tensorboardTimeSeries.batchCreate`
  * `aiplatform.tensorboardTimeSeries.batchRead`
  * `aiplatform.tensorboardTimeSeries.create`
  * `aiplatform.tensorboardTimeSeries.delete`
  * `aiplatform.tensorboardTimeSeries.get`
  * `aiplatform.tensorboardTimeSeries.list`
  * `aiplatform.tensorboardTimeSeries.read`
  * `aiplatform.tensorboardTimeSeries.update`

`aiplatform.tensorboards.create` `aiplatform.tensorboards.delete` `aiplatform.tensorboards.get` `aiplatform.tensorboards.list` `aiplatform.tensorboards.update` `aiplatform.trainingPipelines.*`

  * `aiplatform.trainingPipelines.cancel`
  * `aiplatform.trainingPipelines.create`
  * `aiplatform.trainingPipelines.delete`
  * `aiplatform.trainingPipelines.get`
  * `aiplatform.trainingPipelines.list`

`aiplatform.trials.*`

  * `aiplatform.trials.create`
  * `aiplatform.trials.delete`
  * `aiplatform.trials.get`
  * `aiplatform.trials.list`
  * `aiplatform.trials.update`

`aiplatform.tuningJobs.*`

  * `aiplatform.tuningJobs.cancel`
  * `aiplatform.tuningJobs.create`
  * `aiplatform.tuningJobs.delete`
  * `aiplatform.tuningJobs.get`
  * `aiplatform.tuningJobs.list`
  * `aiplatform.tuningJobs.optimizePrompt`
  * `aiplatform.tuningJobs.validateReinforcementTuningReward`
  * `aiplatform.tuningJobs.vertexTune`

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.tags.get` `artifactregistry.versions.get` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.readsessions.create` `bigquery.readsessions.getData` `bigquery.tables.create` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.update` `bigquery.tables.updateData` `cloudtrace.traces.list` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.implicitDelegation` `iam.serviceAccounts.list` `iam.serviceAccounts.signBlob` `iam.serviceAccounts.signJwt` `logging.logEntries.create` `logging.logEntries.route` `logging.views.access` `logging.views.get` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `observability.views.access` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicemanagement.services.report` `serviceusage.services.use` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Vertex AI Extension Service Agent 

(`roles/aiplatform.extensionServiceAgent`) Gives Vertex AI Extension the permissions it needs to function.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.predict` `aiplatform.locations.get` `aiplatform.ragCorpora.query` `discoveryengine.servingConfigs.search` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `logging.logEntries.create` `logging.logEntries.route` `serviceusage.services.use` `storage.objects.get`  
  
#### AI Platform Notebooks Service Agent 

(`roles/notebooks.serviceAgent`) Provide access for notebooks service agent to manage notebook instances in user projects  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.customJobs.cancel` `aiplatform.customJobs.create` `aiplatform.customJobs.get` `aiplatform.customJobs.list` `aiplatform.notebookExecutionJobs.*`

  * `aiplatform.notebookExecutionJobs.create`
  * `aiplatform.notebookExecutionJobs.delete`
  * `aiplatform.notebookExecutionJobs.get`
  * `aiplatform.notebookExecutionJobs.list`

`aiplatform.notebookRuntimes.get` `aiplatform.operations.list` `aiplatform.pipelineJobs.create` `aiplatform.schedules.*`

  * `aiplatform.schedules.create`
  * `aiplatform.schedules.delete`
  * `aiplatform.schedules.get`
  * `aiplatform.schedules.list`
  * `aiplatform.schedules.update`

`backupdr.backupPlanAssociations.createForComputeDisk` `backupdr.backupPlanAssociations.createForComputeInstance` `backupdr.backupPlanAssociations.deleteForComputeDisk` `backupdr.backupPlanAssociations.deleteForComputeInstance` `backupdr.backupPlanAssociations.fetchForComputeDisk` `backupdr.backupPlanAssociations.getForComputeDisk` `backupdr.backupPlanAssociations.list` `backupdr.backupPlanAssociations.triggerBackupForComputeDisk` `backupdr.backupPlanAssociations.triggerBackupForComputeInstance` `backupdr.backupPlanAssociations.updateForComputeDisk` `backupdr.backupPlanAssociations.updateForComputeInstance` `backupdr.backupPlans.get` `backupdr.backupPlans.list` `backupdr.backupPlans.useForComputeDisk` `backupdr.backupPlans.useForComputeInstance` `backupdr.backupVaults.get` `backupdr.backupVaults.list` `backupdr.locations.list` `backupdr.operations.get` `backupdr.operations.list` `backupdr.serviceConfig.initialize` `compute.acceleratorTypes.*`

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`

`compute.addresses.createInternal` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.addresses.listEffectiveTags` `compute.addresses.listTagBindings` `compute.addresses.use` `compute.addresses.useInternal` `compute.advice.capacity` `compute.advice.capacityHistory` `compute.autoscalers.*`

  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`

`compute.backendBuckets.get` `compute.backendBuckets.getIamPolicy` `compute.backendBuckets.list` `compute.backendBuckets.listEffectiveTags` `compute.backendBuckets.listTagBindings` `compute.backendServices.get` `compute.backendServices.getIamPolicy` `compute.backendServices.list` `compute.backendServices.listEffectiveTags` `compute.backendServices.listTagBindings` `compute.commitments.get` `compute.commitments.list` `compute.commitments.listEffectiveTags` `compute.commitments.listTagBindings` `compute.crossSiteNetworks.get` `compute.crossSiteNetworks.list` `compute.diskSettings.get` `compute.diskTypes.*`

  * `compute.diskTypes.get`
  * `compute.diskTypes.list`

`compute.disks.*`

  * `compute.disks.addResourcePolicies`
  * `compute.disks.create`
  * `compute.disks.createSnapshot`
  * `compute.disks.createTagBinding`
  * `compute.disks.delete`
  * `compute.disks.deleteTagBinding`
  * `compute.disks.get`
  * `compute.disks.getIamPolicy`
  * `compute.disks.list`
  * `compute.disks.listEffectiveTags`
  * `compute.disks.listTagBindings`
  * `compute.disks.removeResourcePolicies`
  * `compute.disks.resize`
  * `compute.disks.setIamPolicy`
  * `compute.disks.setLabels`
  * `compute.disks.startAsyncReplication`
  * `compute.disks.stopAsyncReplication`
  * `compute.disks.stopGroupAsyncReplication`
  * `compute.disks.update`
  * `compute.disks.updateKmsKey`
  * `compute.disks.use`
  * `compute.disks.useReadOnly`

`compute.externalVpnGateways.get` `compute.externalVpnGateways.list` `compute.externalVpnGateways.listEffectiveTags` `compute.externalVpnGateways.listTagBindings` `compute.firewallPolicies.get` `compute.firewallPolicies.getIamPolicy` `compute.firewallPolicies.list` `compute.firewallPolicies.listEffectiveTags` `compute.firewallPolicies.listTagBindings` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.listEffectiveTags` `compute.firewalls.listTagBindings` `compute.folderRolloutPlans.get` `compute.folderRolloutPlans.list` `compute.folderRollouts.get` `compute.folderRollouts.list` `compute.folderVmExtensionPolicies.get` `compute.folderVmExtensionPolicies.list` `compute.folderVmExtensions.*`

  * `compute.folderVmExtensions.get`
  * `compute.folderVmExtensions.list`

`compute.forwardingRules.get` `compute.forwardingRules.list` `compute.forwardingRules.listEffectiveTags` `compute.forwardingRules.listTagBindings` `compute.futureReservations.get` `compute.futureReservations.getIamPolicy` `compute.futureReservations.list` `compute.futureReservations.listEffectiveTags` `compute.futureReservations.listTagBindings` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalAddresses.listEffectiveTags` `compute.globalAddresses.listTagBindings` `compute.globalAddresses.use` `compute.globalForwardingRules.get` `compute.globalForwardingRules.list` `compute.globalForwardingRules.listEffectiveTags` `compute.globalForwardingRules.listTagBindings` `compute.globalFrontendSettings.get` `compute.globalNetworkEndpointGroups.*`

  * `compute.globalNetworkEndpointGroups.attachNetworkEndpoints`
  * `compute.globalNetworkEndpointGroups.create`
  * `compute.globalNetworkEndpointGroups.createTagBinding`
  * `compute.globalNetworkEndpointGroups.delete`
  * `compute.globalNetworkEndpointGroups.deleteTagBinding`
  * `compute.globalNetworkEndpointGroups.detachNetworkEndpoints`
  * `compute.globalNetworkEndpointGroups.get`
  * `compute.globalNetworkEndpointGroups.list`
  * `compute.globalNetworkEndpointGroups.listEffectiveTags`
  * `compute.globalNetworkEndpointGroups.listTagBindings`
  * `compute.globalNetworkEndpointGroups.use`

`compute.globalOperations.get` `compute.globalOperations.getIamPolicy` `compute.globalOperations.list` `compute.globalPublicDelegatedPrefixes.get` `compute.globalPublicDelegatedPrefixes.list` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.listEffectiveTags` `compute.healthChecks.listTagBindings` `compute.hosts.*`

  * `compute.hosts.get`
  * `compute.hosts.getVersion`
  * `compute.hosts.list`

`compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.listEffectiveTags` `compute.httpHealthChecks.listTagBindings` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.list` `compute.httpsHealthChecks.listEffectiveTags` `compute.httpsHealthChecks.listTagBindings` `compute.images.*`

  * `compute.images.create`
  * `compute.images.createTagBinding`
  * `compute.images.delete`
  * `compute.images.deleteTagBinding`
  * `compute.images.deprecate`
  * `compute.images.get`
  * `compute.images.getFromFamily`
  * `compute.images.getIamPolicy`
  * `compute.images.list`
  * `compute.images.listEffectiveTags`
  * `compute.images.listTagBindings`
  * `compute.images.setIamPolicy`
  * `compute.images.setLabels`
  * `compute.images.update`
  * `compute.images.useReadOnly`

`compute.instanceGroupManagers.*`

  * `compute.instanceGroupManagers.create`
  * `compute.instanceGroupManagers.createTagBinding`
  * `compute.instanceGroupManagers.delete`
  * `compute.instanceGroupManagers.deleteTagBinding`
  * `compute.instanceGroupManagers.get`
  * `compute.instanceGroupManagers.list`
  * `compute.instanceGroupManagers.listEffectiveTags`
  * `compute.instanceGroupManagers.listTagBindings`
  * `compute.instanceGroupManagers.update`
  * `compute.instanceGroupManagers.use`

`compute.instanceGroups.*`

  * `compute.instanceGroups.create`
  * `compute.instanceGroups.createTagBinding`
  * `compute.instanceGroups.delete`
  * `compute.instanceGroups.deleteTagBinding`
  * `compute.instanceGroups.get`
  * `compute.instanceGroups.list`
  * `compute.instanceGroups.listEffectiveTags`
  * `compute.instanceGroups.listTagBindings`
  * `compute.instanceGroups.update`
  * `compute.instanceGroups.use`

`compute.instanceSettings.*`

  * `compute.instanceSettings.get`
  * `compute.instanceSettings.update`

`compute.instanceTemplates.*`

  * `compute.instanceTemplates.create`
  * `compute.instanceTemplates.delete`
  * `compute.instanceTemplates.get`
  * `compute.instanceTemplates.getIamPolicy`
  * `compute.instanceTemplates.list`
  * `compute.instanceTemplates.setIamPolicy`
  * `compute.instanceTemplates.useReadOnly`

`compute.instances.*`

  * `compute.instances.addAccessConfig`
  * `compute.instances.addNetworkInterface`
  * `compute.instances.addResourcePolicies`
  * `compute.instances.attachDisk`
  * `compute.instances.create`
  * `compute.instances.createTagBinding`
  * `compute.instances.delete`
  * `compute.instances.deleteAccessConfig`
  * `compute.instances.deleteNetworkInterface`
  * `compute.instances.deleteTagBinding`
  * `compute.instances.detachDisk`
  * `compute.instances.get`
  * `compute.instances.getEffectiveFirewalls`
  * `compute.instances.getGuestAttributes`
  * `compute.instances.getIamPolicy`
  * `compute.instances.getScreenshot`
  * `compute.instances.getSerialPortOutput`
  * `compute.instances.getShieldedInstanceIdentity`
  * `compute.instances.getShieldedVmIdentity`
  * `compute.instances.getVmExtensionState`
  * `compute.instances.list`
  * `compute.instances.listEffectiveTags`
  * `compute.instances.listReferrers`
  * `compute.instances.listTagBindings`
  * `compute.instances.listVmExtensionStates`
  * `compute.instances.osAdminLogin`
  * `compute.instances.osLogin`
  * `compute.instances.performMaintenance`
  * `compute.instances.pscInterfaceCreate`
  * `compute.instances.removeResourcePolicies`
  * `compute.instances.reset`
  * `compute.instances.resume`
  * `compute.instances.sendDiagnosticInterrupt`
  * `compute.instances.setDeletionProtection`
  * `compute.instances.setDiskAutoDelete`
  * `compute.instances.setIamPolicy`
  * `compute.instances.setLabels`
  * `compute.instances.setMachineResources`
  * `compute.instances.setMachineType`
  * `compute.instances.setMetadata`
  * `compute.instances.setMinCpuPlatform`
  * `compute.instances.setName`
  * `compute.instances.setScheduling`
  * `compute.instances.setSecurityPolicy`
  * `compute.instances.setServiceAccount`
  * `compute.instances.setShieldedInstanceIntegrityPolicy`
  * `compute.instances.setShieldedVmIntegrityPolicy`
  * `compute.instances.setTags`
  * `compute.instances.simulateMaintenanceEvent`
  * `compute.instances.start`
  * `compute.instances.startWithEncryptionKey`
  * `compute.instances.stop`
  * `compute.instances.suspend`
  * `compute.instances.troubleshoot`
  * `compute.instances.update`
  * `compute.instances.updateAccessConfig`
  * `compute.instances.updateDisplayDevice`
  * `compute.instances.updateNetworkInterface`
  * `compute.instances.updateSecurity`
  * `compute.instances.updateShieldedInstanceConfig`
  * `compute.instances.updateShieldedVmConfig`
  * `compute.instances.use`
  * `compute.instances.useReadOnly`

`compute.instantSnapshotGroups.*`

  * `compute.instantSnapshotGroups.create`
  * `compute.instantSnapshotGroups.delete`
  * `compute.instantSnapshotGroups.get`
  * `compute.instantSnapshotGroups.getIamPolicy`
  * `compute.instantSnapshotGroups.list`
  * `compute.instantSnapshotGroups.setIamPolicy`
  * `compute.instantSnapshotGroups.useReadOnly`

`compute.instantSnapshots.create` `compute.instantSnapshots.delete` `compute.instantSnapshots.export` `compute.instantSnapshots.get` `compute.instantSnapshots.getIamPolicy` `compute.instantSnapshots.list` `compute.instantSnapshots.listEffectiveTags` `compute.instantSnapshots.listTagBindings` `compute.instantSnapshots.setIamPolicy` `compute.instantSnapshots.setLabels` `compute.instantSnapshots.useReadOnly` `compute.interconnectAttachmentGroups.get` `compute.interconnectAttachmentGroups.list` `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnectAttachments.listEffectiveTags` `compute.interconnectAttachments.listTagBindings` `compute.interconnectGroups.get` `compute.interconnectGroups.list` `compute.interconnectLocations.*`

  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`

`compute.interconnectRemoteLocations.*`

  * `compute.interconnectRemoteLocations.get`
  * `compute.interconnectRemoteLocations.list`

`compute.interconnects.get` `compute.interconnects.list` `compute.interconnects.listEffectiveTags` `compute.interconnects.listTagBindings` `compute.licenseCodes.*`

  * `compute.licenseCodes.get`
  * `compute.licenseCodes.getIamPolicy`
  * `compute.licenseCodes.list`
  * `compute.licenseCodes.setIamPolicy`

`compute.licenses.create` `compute.licenses.delete` `compute.licenses.get` `compute.licenses.getIamPolicy` `compute.licenses.list` `compute.licenses.listEffectiveTags` `compute.licenses.listTagBindings` `compute.licenses.setIamPolicy` `compute.licenses.update` `compute.machineImages.create` `compute.machineImages.delete` `compute.machineImages.get` `compute.machineImages.getIamPolicy` `compute.machineImages.list` `compute.machineImages.listEffectiveTags` `compute.machineImages.listTagBindings` `compute.machineImages.setIamPolicy` `compute.machineImages.setLabels` `compute.machineImages.useReadOnly` `compute.machineTypes.*`

  * `compute.machineTypes.get`
  * `compute.machineTypes.list`

`compute.managedRulesets.*`

  * `compute.managedRulesets.get`
  * `compute.managedRulesets.list`

`compute.multiMig.*`

  * `compute.multiMig.create`
  * `compute.multiMig.delete`
  * `compute.multiMig.get`
  * `compute.multiMig.list`

`compute.multiMigMembers.*`

  * `compute.multiMigMembers.get`
  * `compute.multiMigMembers.list`

`compute.networkAttachments.get` `compute.networkAttachments.getIamPolicy` `compute.networkAttachments.list` `compute.networkAttachments.listEffectiveTags` `compute.networkAttachments.listTagBindings` `compute.networkEdgeSecurityServices.get` `compute.networkEdgeSecurityServices.list` `compute.networkEdgeSecurityServices.listEffectiveTags` `compute.networkEdgeSecurityServices.listTagBindings` `compute.networkEndpointGroups.*`

  * `compute.networkEndpointGroups.attachNetworkEndpoints`
  * `compute.networkEndpointGroups.create`
  * `compute.networkEndpointGroups.createTagBinding`
  * `compute.networkEndpointGroups.delete`
  * `compute.networkEndpointGroups.deleteTagBinding`
  * `compute.networkEndpointGroups.detachNetworkEndpoints`
  * `compute.networkEndpointGroups.get`
  * `compute.networkEndpointGroups.list`
  * `compute.networkEndpointGroups.listEffectiveTags`
  * `compute.networkEndpointGroups.listTagBindings`
  * `compute.networkEndpointGroups.use`

`compute.networkProfiles.*`

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`

`compute.networks.get` `compute.networks.getEffectiveFirewalls` `compute.networks.getRegionEffectiveFirewalls` `compute.networks.list` `compute.networks.listEffectiveTags` `compute.networks.listPeeringRoutes` `compute.networks.listTagBindings` `compute.networks.use` `compute.networks.useExternalIp` `compute.nodeGroups.get` `compute.nodeGroups.getIamPolicy` `compute.nodeGroups.list` `compute.nodeTemplates.get` `compute.nodeTemplates.getIamPolicy` `compute.nodeTemplates.list` `compute.nodeTypes.*`

  * `compute.nodeTypes.get`
  * `compute.nodeTypes.list`

`compute.orgRolloutPlans.get` `compute.orgRolloutPlans.list` `compute.orgRollouts.get` `compute.orgRollouts.list` `compute.orgVmExtensionPolicies.get` `compute.orgVmExtensionPolicies.list` `compute.orgVmExtensions.*`

  * `compute.orgVmExtensions.get`
  * `compute.orgVmExtensions.list`

`compute.organizations.listAssociations` `compute.packetMirrorings.get` `compute.packetMirrorings.list` `compute.packetMirrorings.listEffectiveTags` `compute.packetMirrorings.listTagBindings` `compute.previewFeatures.get` `compute.previewFeatures.list` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.publicAdvertisedPrefixes.get` `compute.publicAdvertisedPrefixes.list` `compute.publicDelegatedPrefixes.get` `compute.publicDelegatedPrefixes.list` `compute.publicDelegatedPrefixes.listEffectiveTags` `compute.publicDelegatedPrefixes.listTagBindings` `compute.recoverableSnapshots.*`

  * `compute.recoverableSnapshots.delete`
  * `compute.recoverableSnapshots.get`
  * `compute.recoverableSnapshots.getIamPolicy`
  * `compute.recoverableSnapshots.list`
  * `compute.recoverableSnapshots.recover`
  * `compute.recoverableSnapshots.setIamPolicy`

`compute.regionBackendBuckets.get` `compute.regionBackendBuckets.getIamPolicy` `compute.regionBackendBuckets.list` `compute.regionBackendBuckets.listEffectiveTags` `compute.regionBackendBuckets.listTagBindings` `compute.regionBackendServices.get` `compute.regionBackendServices.getIamPolicy` `compute.regionBackendServices.list` `compute.regionBackendServices.listEffectiveTags` `compute.regionBackendServices.listTagBindings` `compute.regionCompositeHealthChecks.get` `compute.regionCompositeHealthChecks.list` `compute.regionFirewallPolicies.get` `compute.regionFirewallPolicies.getIamPolicy` `compute.regionFirewallPolicies.list` `compute.regionFirewallPolicies.listEffectiveTags` `compute.regionFirewallPolicies.listTagBindings` `compute.regionHealthAggregationPolicies.get` `compute.regionHealthAggregationPolicies.list` `compute.regionHealthCheckServices.get` `compute.regionHealthCheckServices.list` `compute.regionHealthChecks.get` `compute.regionHealthChecks.list` `compute.regionHealthChecks.listEffectiveTags` `compute.regionHealthChecks.listTagBindings` `compute.regionHealthSources.get` `compute.regionHealthSources.list` `compute.regionNetworkEndpointGroups.*`

  * `compute.regionNetworkEndpointGroups.attachNetworkEndpoints`
  * `compute.regionNetworkEndpointGroups.create`
  * `compute.regionNetworkEndpointGroups.createTagBinding`
  * `compute.regionNetworkEndpointGroups.delete`
  * `compute.regionNetworkEndpointGroups.deleteTagBinding`
  * `compute.regionNetworkEndpointGroups.detachNetworkEndpoints`
  * `compute.regionNetworkEndpointGroups.get`
  * `compute.regionNetworkEndpointGroups.list`
  * `compute.regionNetworkEndpointGroups.listEffectiveTags`
  * `compute.regionNetworkEndpointGroups.listTagBindings`
  * `compute.regionNetworkEndpointGroups.use`

`compute.regionNetworkPolicies.get` `compute.regionNetworkPolicies.list` `compute.regionNotificationEndpoints.get` `compute.regionNotificationEndpoints.list` `compute.regionOperations.get` `compute.regionOperations.getIamPolicy` `compute.regionOperations.list` `compute.regionSecurityPolicies.get` `compute.regionSecurityPolicies.list` `compute.regionSecurityPolicies.listEffectiveTags` `compute.regionSecurityPolicies.listTagBindings` `compute.regionSslCertificates.get` `compute.regionSslCertificates.list` `compute.regionSslCertificates.listEffectiveTags` `compute.regionSslCertificates.listTagBindings` `compute.regionSslPolicies.get` `compute.regionSslPolicies.getIamPolicy` `compute.regionSslPolicies.list` `compute.regionSslPolicies.listAvailableFeatures` `compute.regionSslPolicies.listEffectiveTags` `compute.regionSslPolicies.listTagBindings` `compute.regionTargetHttpProxies.get` `compute.regionTargetHttpProxies.list` `compute.regionTargetHttpProxies.listEffectiveTags` `compute.regionTargetHttpProxies.listTagBindings` `compute.regionTargetHttpsProxies.get` `compute.regionTargetHttpsProxies.list` `compute.regionTargetHttpsProxies.listEffectiveTags` `compute.regionTargetHttpsProxies.listTagBindings` `compute.regionTargetTcpProxies.get` `compute.regionTargetTcpProxies.list` `compute.regionTargetTcpProxies.listEffectiveTags` `compute.regionTargetTcpProxies.listTagBindings` `compute.regionUrlMaps.get` `compute.regionUrlMaps.list` `compute.regionUrlMaps.listEffectiveTags` `compute.regionUrlMaps.listTagBindings` `compute.regionUrlMaps.validate` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.reliabilityRisks.*`

  * `compute.reliabilityRisks.get`
  * `compute.reliabilityRisks.list`

`compute.reservationBlocks.get` `compute.reservationBlocks.list` `compute.reservationConsumedInstances.list` `compute.reservationSlots.*`

  * `compute.reservationSlots.get`
  * `compute.reservationSlots.list`
  * `compute.reservationSlots.update`

`compute.reservationSubBlocks.get` `compute.reservationSubBlocks.list` `compute.reservations.get` `compute.reservations.list` `compute.reservations.listEffectiveTags` `compute.reservations.listTagBindings` `compute.resourcePolicies.*`

  * `compute.resourcePolicies.create`
  * `compute.resourcePolicies.delete`
  * `compute.resourcePolicies.get`
  * `compute.resourcePolicies.getIamPolicy`
  * `compute.resourcePolicies.list`
  * `compute.resourcePolicies.setIamPolicy`
  * `compute.resourcePolicies.update`
  * `compute.resourcePolicies.use`
  * `compute.resourcePolicies.useReadOnly`

`compute.rolloutPlans.get` `compute.rolloutPlans.list` `compute.rollouts.get` `compute.rollouts.list` `compute.routers.get` `compute.routers.getRoutePolicy` `compute.routers.list` `compute.routers.listBgpRoutes` `compute.routers.listEffectiveTags` `compute.routers.listRoutePolicies` `compute.routers.listTagBindings` `compute.routes.get` `compute.routes.list` `compute.routes.listEffectiveTags` `compute.routes.listTagBindings` `compute.securityPolicies.get` `compute.securityPolicies.list` `compute.securityPolicies.listEffectiveTags` `compute.securityPolicies.listTagBindings` `compute.serviceAttachments.get` `compute.serviceAttachments.getIamPolicy` `compute.serviceAttachments.list` `compute.serviceAttachments.listEffectiveTags` `compute.serviceAttachments.listTagBindings` `compute.snapshotGroups.*`

  * `compute.snapshotGroups.create`
  * `compute.snapshotGroups.delete`
  * `compute.snapshotGroups.get`
  * `compute.snapshotGroups.getIamPolicy`
  * `compute.snapshotGroups.list`
  * `compute.snapshotGroups.setIamPolicy`
  * `compute.snapshotGroups.useReadOnly`

`compute.snapshotRecycleBinPolicy.get` `compute.snapshotSettings.get` `compute.snapshots.*`

  * `compute.snapshots.create`
  * `compute.snapshots.createTagBinding`
  * `compute.snapshots.delete`
  * `compute.snapshots.deleteTagBinding`
  * `compute.snapshots.get`
  * `compute.snapshots.getEffectiveRecycleBinRule`
  * `compute.snapshots.getIamPolicy`
  * `compute.snapshots.list`
  * `compute.snapshots.listEffectiveTags`
  * `compute.snapshots.listTagBindings`
  * `compute.snapshots.setIamPolicy`
  * `compute.snapshots.setLabels`
  * `compute.snapshots.updateKmsKey`
  * `compute.snapshots.useReadOnly`

`compute.spotAssistants.get` `compute.sslCertificates.get` `compute.sslCertificates.list` `compute.sslCertificates.listEffectiveTags` `compute.sslCertificates.listTagBindings` `compute.sslPolicies.get` `compute.sslPolicies.getIamPolicy` `compute.sslPolicies.list` `compute.sslPolicies.listAvailableFeatures` `compute.sslPolicies.listEffectiveTags` `compute.sslPolicies.listTagBindings` `compute.storagePools.get` `compute.storagePools.getIamPolicy` `compute.storagePools.list` `compute.storagePools.listEffectiveTags` `compute.storagePools.listTagBindings` `compute.storagePools.use` `compute.subnetworks.get` `compute.subnetworks.getIamPolicy` `compute.subnetworks.list` `compute.subnetworks.listEffectiveTags` `compute.subnetworks.listTagBindings` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.targetGrpcProxies.get` `compute.targetGrpcProxies.list` `compute.targetGrpcProxies.listEffectiveTags` `compute.targetGrpcProxies.listTagBindings` `compute.targetHttpProxies.get` `compute.targetHttpProxies.list` `compute.targetHttpProxies.listEffectiveTags` `compute.targetHttpProxies.listTagBindings` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.list` `compute.targetHttpsProxies.listEffectiveTags` `compute.targetHttpsProxies.listTagBindings` `compute.targetInstances.get` `compute.targetInstances.list` `compute.targetInstances.listEffectiveTags` `compute.targetInstances.listTagBindings` `compute.targetPools.get` `compute.targetPools.list` `compute.targetPools.listEffectiveTags` `compute.targetPools.listTagBindings` `compute.targetSslProxies.get` `compute.targetSslProxies.list` `compute.targetSslProxies.listEffectiveTags` `compute.targetSslProxies.listTagBindings` `compute.targetTcpProxies.get` `compute.targetTcpProxies.list` `compute.targetTcpProxies.listEffectiveTags` `compute.targetTcpProxies.listTagBindings` `compute.targetVpnGateways.get` `compute.targetVpnGateways.list` `compute.targetVpnGateways.listEffectiveTags` `compute.targetVpnGateways.listTagBindings` `compute.urlMaps.get` `compute.urlMaps.list` `compute.urlMaps.listEffectiveTags` `compute.urlMaps.listTagBindings` `compute.urlMaps.validate` `compute.vmExtensionPolicies.get` `compute.vmExtensionPolicies.list` `compute.vmExtensions.*`

  * `compute.vmExtensions.get`
  * `compute.vmExtensions.list`

`compute.vpnGateways.get` `compute.vpnGateways.list` `compute.vpnGateways.listEffectiveTags` `compute.vpnGateways.listTagBindings` `compute.vpnTunnels.get` `compute.vpnTunnels.list` `compute.vpnTunnels.listEffectiveTags` `compute.vpnTunnels.listTagBindings` `compute.wireGroups.get` `compute.wireGroups.list` `compute.zoneOperations.get` `compute.zoneOperations.getIamPolicy` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`dataproc.clusters.get` `dataproc.clusters.use` `dataproc.jobs.cancel` `dataproc.jobs.create` `dataproc.jobs.delete` `dataproc.jobs.get` `dataproc.jobs.list` `dataproc.jobs.update` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.list` `ml.jobs.create` `ml.jobs.get` `ml.jobs.list` `notebooks.environments.*`

  * `notebooks.environments.create`
  * `notebooks.environments.delete`
  * `notebooks.environments.get`
  * `notebooks.environments.getIamPolicy`
  * `notebooks.environments.list`
  * `notebooks.environments.setIamPolicy`

`notebooks.executions.*`

  * `notebooks.executions.create`
  * `notebooks.executions.delete`
  * `notebooks.executions.get`
  * `notebooks.executions.getIamPolicy`
  * `notebooks.executions.list`
  * `notebooks.executions.setIamPolicy`

`notebooks.instances.checkUpgradability` `notebooks.instances.create` `notebooks.instances.delete` `notebooks.instances.diagnose` `notebooks.instances.get` `notebooks.instances.getHealth` `notebooks.instances.getIamPolicy` `notebooks.instances.list` `notebooks.instances.listEffectiveTags` `notebooks.instances.listTagBindings` `notebooks.instances.reset` `notebooks.instances.setAccelerator` `notebooks.instances.setIamPolicy` `notebooks.instances.setLabels` `notebooks.instances.setMachineType` `notebooks.instances.start` `notebooks.instances.stop` `notebooks.instances.update` `notebooks.instances.updateConfig` `notebooks.instances.updateShieldInstanceConfig` `notebooks.instances.upgrade` `notebooks.instances.use` `notebooks.locations.*`

  * `notebooks.locations.get`
  * `notebooks.locations.list`

`notebooks.operations.*`

  * `notebooks.operations.cancel`
  * `notebooks.operations.delete`
  * `notebooks.operations.get`
  * `notebooks.operations.list`

`notebooks.runtimes.*`

  * `notebooks.runtimes.create`
  * `notebooks.runtimes.delete`
  * `notebooks.runtimes.diagnose`
  * `notebooks.runtimes.get`
  * `notebooks.runtimes.getIamPolicy`
  * `notebooks.runtimes.list`
  * `notebooks.runtimes.reset`
  * `notebooks.runtimes.setIamPolicy`
  * `notebooks.runtimes.start`
  * `notebooks.runtimes.stop`
  * `notebooks.runtimes.switch`
  * `notebooks.runtimes.update`
  * `notebooks.runtimes.upgrade`

`notebooks.schedules.*`

  * `notebooks.schedules.create`
  * `notebooks.schedules.delete`
  * `notebooks.schedules.get`
  * `notebooks.schedules.getIamPolicy`
  * `notebooks.schedules.list`
  * `notebooks.schedules.setIamPolicy`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Grant Agent Platform service agents access to other resources

Sometimes you need to grant additional roles to an Agent Platform service agent. For example, if you need Agent Platform to access a Cloud Storage bucket in a different project, you'll need to grant one or more additional roles to the service agent.

**Note:** If you want your custom training code to obtain an OAuth 2.0 access token with the `https://www.googleapis.com/auth/cloud-platform` scope, then you must use a [custom service account](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/custom-service-account) for training. You can't give this level of access to the Gemini Enterprise Agent Platform Custom Code Service Agent.

### Role addition requirements for BigQuery

The following table describes the required additional roles needed to be added to the Agent Platform Service Agent for BigQuery tables or view in a different project or backed by an external data source.

The term _home project_ refers to the project where the Agent Platform dataset or model is located. The term _different project_ refers to any other project.

Table type | Table project | Data source project | Role addition required  
---|---|---|---  
[Native BigQuery table](https://docs.cloud.google.com/bigquery/docs/tables-intro) | Home project | N/A | None.  
[Native BigQuery table](https://docs.cloud.google.com/bigquery/docs/tables-intro) | Different project | N/A | `BigQuery Data Viewer` for different project. Learn more.  
[BigQuery view](https://docs.cloud.google.com/bigquery/docs/views) | Home project | N/A | None.  
[BigQuery view](https://docs.cloud.google.com/bigquery/docs/views) | Different project | N/A | `BigQuery Data Viewer` for different project. Learn more.  
[External BigQuery data source backed by Bigtable](https://docs.cloud.google.com/bigquery/external-data-bigtable) | Home project | Home project | `Bigtable Reader` for home project. Learn more.  
[External BigQuery data source backed by Bigtable](https://docs.cloud.google.com/bigquery/external-data-bigtable) | Home project | Different project | `Bigtable Reader` for different project. Learn more.  
[External BigQuery data source backed by Bigtable](https://docs.cloud.google.com/bigquery/external-data-bigtable) | Different project | Different project | `BigQuery Reader` and `Bigtable Reader` for different project. Learn more.  
[External BigQuery data source backed by Cloud Storage](https://docs.cloud.google.com/bigquery/external-data-cloud-storage) | Home project | Home project | None.  
[External BigQuery data source backed by Cloud Storage](https://docs.cloud.google.com/bigquery/external-data-cloud-storage) | Home project | Different project | `Storage Object Viewer` for different project. Learn more.  
[External BigQuery data source backed by Cloud Storage](https://docs.cloud.google.com/bigquery/external-data-cloud-storage) | Different project | Different project | `Storage Object Viewer` and `BigQuery Data Viewer` for different project. Learn more.  
[External BigQuery data source backed by Google Sheets](https://docs.cloud.google.com/bigquery/external-data-drive) | Home project | N/A | Share your Sheets file with the Agent Platform service account. Learn more.  
[External BigQuery data source backed by Google Sheets](https://docs.cloud.google.com/bigquery/external-data-drive) | Different project | N/A | `BigQuery Reader` for different project and share your Sheets file with the Agent Platform service account.  
  
### Role addition requirements for Cloud Storage

If you are accessing data in a Cloud Storage bucket in a different project, you must give the `Storage > Storage Object Viewer` role to Agent Platform in that project. Learn more.

If you are using a Cloud Storage bucket to receive data from your local computer for an import operation, and the bucket is in a different project than Google Cloud project, you must give the `Storage > Storage Object Creator` role to Agent Platform in that project. Learn more.

### Grant access to Agent Platform to resources in your home project

To grant additional roles to a service agent for Agent Platform in your home project:

  1. Go to the **IAM** page of the Google Cloud console for your home project.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **Include Google-provided role grants** checkbox.

  3. Determine the service agent you want to grant the permissions to and click the edit pencil icon.

You can filter for **Principal:@gcp-sa-aiplatform-cc.iam.gserviceaccount.com** to find the Agent Platform service agents.

  4. Grant the required roles to the service agent and save your changes.




### Grant access to Agent Platform to resources in a different project

When you use data sources or destinations in a different project, you must give the Agent Platform service agent permissions in that project. The Agent Platform service agent is created after you start the first asynchronous job (for example, creating an endpoint). You can also explicitly create the Agent Platform service agent. For more information, see [gcloud beta services identity create](https://cloud.google.com/sdk/gcloud/reference/beta/services/identity/create). This Google Cloud CLI command creates the primary service agent and the custom code service agent. However, only the primary service agent is returned in the response.

To add permissions to Agent Platform in a different project:

  1. Go to the **IAM** page of the Google Cloud console for your home project (the project where you are using Agent Platform).

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **Include Google-provided role grants** checkbox.

  3. Determine the service agent you want to grant the permissions to and copy its email address (listed under **Principal**).

You can filter for **Principal:@gcp-sa-aiplatform-cc.iam.gserviceaccount.com** to find the Agent Platform service agents.

  4. Change projects to the project where you need to grant the permissions.

  5. Click **Add** , and enter the email address in **New principals**.

  6. Add all required roles and click **Save**.




### Provide access to Google Sheets

If you use an external BigQuery data source backed by Google Sheets, you must share your sheet with the Agent Platform service account. The Agent Platform service account is created after you start the first asynchronous job (for example, creating an endpoint). You can also explicitly create the Agent Platform service account by using gcloud CLI by following [this instruction](https://cloud.google.com/sdk/gcloud/reference/beta/services/identity/create).

To authorize Agent Platform to access your Sheets file:

  1. Go to the **IAM** page of the Google Cloud console.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Look for the service account with the name `Agent Platform Service Agent` and copy its email address (listed under **Principal**).

  3. Open your Sheets file and share it with that address.




## What's next

  * [Learn more about IAM](https://docs.cloud.google.com/iam/docs).
  * [Learn about specific IAM permissions and the operations they support](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/iam-permissions).
  * To learn about recommended ways to set up a project for a team, see [Set up a project for a team](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/set-up-project).
  * [Get an overview of Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
