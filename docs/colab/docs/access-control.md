---
url: https://docs.cloud.google.com/colab/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:27.767657+00:00
---

# Access control with IAM  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access control with IAM

This page describes how to use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) to manage access to Colab Enterprise resources. To manage access for other Gemini Enterprise Agent Platform resources, see [Agent Platform access control with IAM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control).

## Control access to notebooks with IAM

You can manage access to Colab Enterprise notebooks (IPYNB files) at the project level or per notebook.

  * To grant access to notebooks at the project level, assign one or more [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to a principal (user, group, or [service account](https://docs.cloud.google.com/iam/docs/overview#service_account)).
  * To grant access to a specific notebook, assign one or more roles to a principal on the notebook. To learn more, see [Manage access to a notebook](https://docs.cloud.google.com/colab/docs/manage-access-notebook).



## Running code that interacts with other Google Cloud services

Granting access to a notebook is limited to the specific permissions related to interacting with the notebook. For example, you can grant the ability to create a notebook, write code in it, or delete the notebook.

To run code that interacts with other Google Cloud services, you must use one of the following methods:

  * Run code in a runtime with end-user credentials enabled. This means your notebook has the same access to Google Cloud services as your notebook user.

  * Run code that authenticates and authorizes your notebook to interact with Google Cloud services.




To learn more, see [Run code that interacts with Google Cloud](https://docs.cloud.google.com/colab/docs/run-code-adc).

## Types of IAM roles

There are different types of IAM roles that can be used in Colab Enterprise:

  * Predefined roles let you grant a set of related permissions to your Colab Enterprise resources at the project level.

  * Basic roles (Owner, Editor, and Viewer) provide access control to your Colab Enterprise resources at the project level, and are common to all Google Cloud services.

  * Custom roles enable you to choose a specific set of permissions, create your own role with those permissions, and grant the role to users in your organization.




To add, update, or remove these roles in your Colab Enterprise project, see the documentation on [managing access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Predefined roles for Colab Enterprise

Colab Enterprise is a part of Agent Platform, and Colab Enterprise resources are managed through the Agent Platform API. Therefore, you can grant principals access to Colab Enterprise resources through Agent Platform roles.

The following table includes all Agent Platform predefined roles.

  * To use predefined roles for common Colab Enterprise operations, see Colab Enterprise Admin (`roles/aiplatform.colabEnterpriseAdmin`) and Colab Enterprise User (`roles/aiplatform.colabEnterpriseUser`).

  * For roles related to runtime management, see Notebook Runtime Admin (`roles/aiplatform.notebookRuntimeAdmin`) and Notebook Runtime User (`roles/aiplatform.notebookRuntimeUser`).

  * Agent Platform Administrator (`roles/aiplatform.admin`), Agent Platform User (`roles/aiplatform.user`), and Agent Platform Viewer (`roles/aiplatform.viewer`) also include Colab Enterprise permissions.




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
  
## Basic roles

The older Google Cloud [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) are common to all Google Cloud services. These roles are Owner, Editor, and Viewer.

The basic roles provide permissions across Google Cloud, not just for Colab Enterprise. For this reason, you should use Colab Enterprise roles whenever possible.

## Custom roles

If the predefined IAM roles for Colab Enterprise don't meet your needs, you can define custom roles. Custom roles enable you to choose a specific set of permissions, create your own role with those permissions, and grant the role to users in your organization. For more information, see [Understanding IAM custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

## Service agents for Colab Enterprise

Colab Enterprise automatically creates and uses [service agents](https://docs.cloud.google.com/iam/docs/service-agents) to access resources on your behalf. When a service agent is created, the service agent is granted a predefined role for your project.

**Note:** Don't remove default roles and permissions of default service accounts unless you are sure that they are unnecessary.

The following table lists Colab Enterprise service agents, their email addresses, and their respective roles:

Name | Used for | Email address | Role  
---|---|---|---  
Vertex AI Service Agent | Agent Platform capabilities | `service-PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com` | [`roles/aiplatform.serviceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent)  
Vertex AI Colab Service Agent | Gives Colab Enterprise the proper permissions to function | `service-PROJECT_NUMBER@gcp-sa-vertex-nb.iam.gserviceaccount.com` | [`roles/aiplatform.colabServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabServiceAgent)  
Vertex AI Notebook Service Agent | Run notebook-managed resources in the user project with restricted permissions | `service-PROJECT_NUMBER@gcp-sa-aiplatform-vm.iam.gserviceaccount.com` | [`roles/aiplatform.notebookServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.notebookServiceAgent)  
  
If you remove the default roles of the Colab Enterprise service agents, Colab Enterprise can automatically reassign those roles to ensure uninterrupted service functionality. To turn off the Colab Enterprise service, you must turn off the relevant APIs instead of removing roles.

## Security considerations for Colab Enterprise permissions

When a user creates a Colab Enterprise notebook, they are automatically granted the [Code Owner (`roles/dataform.codeOwner`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeOwner) role on that notebook. This resource-level role grant is separate from any project-level IAM roles.

IAM organizes policies in a [hierarchical manner](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control#example_cloud_pubsub):

  * A user can have a role in the project IAM policy, which is automatically propagated to all resources in the project.
  * A user can also have a role in a specific resource policy, such as an individual notebook.



A user has access to a resource if they have a role in the resource policy **or** any of its parent policies.

**Caution:** Removing a user's project-level IAM roles **doesn't** automatically remove their resource-level roles on notebooks they created. The user retains access to those notebooks until their resource-level roles are also removed.

To fully revoke a user's access, administrators can do any of the following:

  * Remove the user's roles from each individual notebook. To learn more, see [Remove resource-level access from a notebook](https://docs.cloud.google.com/colab/docs/manage-access-notebook#revoke-resource-access).
  * Create an [IAM Deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) to revoke all of the user's permissions across all resources in the project.



Because notebooks in Colab Enterprise are stored in Dataform, you should consider the following security implications for users with access to these notebooks:

  * Visibility for notebooks is governed by project-level Dataform permissions. Users with the `dataform.repositories.list` permission, which is included in standard Colab Enterprise roles such as Colab Enterprise User (`roles/aiplatform.colabEnterpriseUser`) and Colab Enterprise Admin (`roles/aiplatform.colabEnterpriseAdmin`), can see all notebooks in the Google Cloud project, regardless of whether they created these notebooks or these notebooks were shared with them. To restrict visibility, you can create [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that exclude the `dataform.repositories.list` permission.
  * Any secrets shared with the Dataform service agent can potentially be accessed by users who have edit access to the notebooks. To secure your credentials, restrict edit access to trusted users, and limit the secrets accessible to the Dataform service agent. For more information, see [Secrets access during package installation](https://docs.cloud.google.com/dataform/docs/access-control#secret-access-risk).



For more information, see [Security considerations for Dataform permissions](https://docs.cloud.google.com/dataform/docs/access-control#security-considerations-permissions).

## What's next

  * [Grant a principal access to a Colab Enterprise notebook.](https://docs.cloud.google.com/colab/docs/manage-access-notebook)

  * [Learn more about IAM](https://docs.cloud.google.com/iam).

  * Learn how to [create and manage custom IAM roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

  * Learn more about [Service agents](https://docs.cloud.google.com/iam/docs/service-agents#vertex-ai-colab-service-account)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
