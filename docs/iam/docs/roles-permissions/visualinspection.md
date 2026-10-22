---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection/
title: Visual Inspection AI roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:08.207221+00:00
---

# Visual Inspection AI roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Visual Inspection AI roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Visual Inspection AI. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Visual Inspection AI roles

Role | Permissions  
---|---  
  
#### Visual Inspection AI Admin 

(`roles/visualinspection.admin`) Admin role for Visual Inspection AI  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `visualinspection.*`

  * `visualinspection.annotationSets.create`
  * `visualinspection.annotationSets.delete`
  * `visualinspection.annotationSets.get`
  * `visualinspection.annotationSets.list`
  * `visualinspection.annotationSets.update`
  * `visualinspection.annotationSpecs.create`
  * `visualinspection.annotationSpecs.delete`
  * `visualinspection.annotationSpecs.get`
  * `visualinspection.annotationSpecs.list`
  * `visualinspection.annotations.create`
  * `visualinspection.annotations.delete`
  * `visualinspection.annotations.get`
  * `visualinspection.annotations.list`
  * `visualinspection.annotations.update`
  * `visualinspection.datasets.create`
  * `visualinspection.datasets.delete`
  * `visualinspection.datasets.export`
  * `visualinspection.datasets.get`
  * `visualinspection.datasets.import`
  * `visualinspection.datasets.list`
  * `visualinspection.datasets.update`
  * `visualinspection.images.delete`
  * `visualinspection.images.get`
  * `visualinspection.images.list`
  * `visualinspection.images.update`
  * `visualinspection.locations.get`
  * `visualinspection.locations.list`
  * `visualinspection.locations.reportUsageMetrics`
  * `visualinspection.modelEvaluations.get`
  * `visualinspection.modelEvaluations.list`
  * `visualinspection.models.create`
  * `visualinspection.models.delete`
  * `visualinspection.models.get`
  * `visualinspection.models.list`
  * `visualinspection.models.update`
  * `visualinspection.models.writePrediction`
  * `visualinspection.modules.create`
  * `visualinspection.modules.delete`
  * `visualinspection.modules.get`
  * `visualinspection.modules.list`
  * `visualinspection.modules.update`
  * `visualinspection.operations.get`
  * `visualinspection.operations.list`
  * `visualinspection.solutionArtifacts.create`
  * `visualinspection.solutionArtifacts.delete`
  * `visualinspection.solutionArtifacts.get`
  * `visualinspection.solutionArtifacts.list`
  * `visualinspection.solutionArtifacts.predict`
  * `visualinspection.solutionArtifacts.update`
  * `visualinspection.solutions.create`
  * `visualinspection.solutions.delete`
  * `visualinspection.solutions.get`
  * `visualinspection.solutions.list`

  
  
#### Visual Inspection AI Solution Editor 

(`roles/visualinspection.editor`) Read and write access to all Visual Inspection AI resources except visualinspection.locations.reportUsageMetrics  |  `visualinspection.*`

  * `visualinspection.annotationSets.create`
  * `visualinspection.annotationSets.delete`
  * `visualinspection.annotationSets.get`
  * `visualinspection.annotationSets.list`
  * `visualinspection.annotationSets.update`
  * `visualinspection.annotationSpecs.create`
  * `visualinspection.annotationSpecs.delete`
  * `visualinspection.annotationSpecs.get`
  * `visualinspection.annotationSpecs.list`
  * `visualinspection.annotations.create`
  * `visualinspection.annotations.delete`
  * `visualinspection.annotations.get`
  * `visualinspection.annotations.list`
  * `visualinspection.annotations.update`
  * `visualinspection.datasets.create`
  * `visualinspection.datasets.delete`
  * `visualinspection.datasets.export`
  * `visualinspection.datasets.get`
  * `visualinspection.datasets.import`
  * `visualinspection.datasets.list`
  * `visualinspection.datasets.update`
  * `visualinspection.images.delete`
  * `visualinspection.images.get`
  * `visualinspection.images.list`
  * `visualinspection.images.update`
  * `visualinspection.locations.get`
  * `visualinspection.locations.list`
  * `visualinspection.locations.reportUsageMetrics`
  * `visualinspection.modelEvaluations.get`
  * `visualinspection.modelEvaluations.list`
  * `visualinspection.models.create`
  * `visualinspection.models.delete`
  * `visualinspection.models.get`
  * `visualinspection.models.list`
  * `visualinspection.models.update`
  * `visualinspection.models.writePrediction`
  * `visualinspection.modules.create`
  * `visualinspection.modules.delete`
  * `visualinspection.modules.get`
  * `visualinspection.modules.list`
  * `visualinspection.modules.update`
  * `visualinspection.operations.get`
  * `visualinspection.operations.list`
  * `visualinspection.solutionArtifacts.create`
  * `visualinspection.solutionArtifacts.delete`
  * `visualinspection.solutionArtifacts.get`
  * `visualinspection.solutionArtifacts.list`
  * `visualinspection.solutionArtifacts.predict`
  * `visualinspection.solutionArtifacts.update`
  * `visualinspection.solutions.create`
  * `visualinspection.solutions.delete`
  * `visualinspection.solutions.get`
  * `visualinspection.solutions.list`

  
  
#### Visual Inspection AI Viewer 

(`roles/visualinspection.viewer`) Read access to Visual Inspection AI resources  |  `visualinspection.annotationSets.get` `visualinspection.annotationSets.list` `visualinspection.annotationSpecs.get` `visualinspection.annotationSpecs.list` `visualinspection.annotations.get` `visualinspection.annotations.list` `visualinspection.datasets.export` `visualinspection.datasets.get` `visualinspection.datasets.list` `visualinspection.images.get` `visualinspection.images.list` `visualinspection.locations.get` `visualinspection.locations.list` `visualinspection.modelEvaluations.*`

  * `visualinspection.modelEvaluations.get`
  * `visualinspection.modelEvaluations.list`

`visualinspection.models.get` `visualinspection.models.list` `visualinspection.modules.get` `visualinspection.modules.list` `visualinspection.operations.*`

  * `visualinspection.operations.get`
  * `visualinspection.operations.list`

`visualinspection.solutionArtifacts.get` `visualinspection.solutionArtifacts.list` `visualinspection.solutionArtifacts.predict` `visualinspection.solutions.get` `visualinspection.solutions.list`  
  
#### Visual Inspection AI Usage Metrics Reporter 

(`roles/visualinspection.usageMetricsReporter`) ReportUsageMetric access to Visual Inspection AI Service  |  `visualinspection.locations.reportUsageMetrics`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Visual Inspection AI Service Agent 

(`roles/visualinspection.serviceAgent`) Grants Visual Inspection AI Service Agent admin roles for accessing/exporting training data, pushing containers artifacts to GCR and ArtifactsRegistry, and Vertex AI for storing data and running training jobs.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.agentAnomalyDetectionScopes.*`

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

`artifactregistry.*`

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

`cloudaicompanion.instances.completeTask` `firebase.projects.get` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`orgpolicy.policy.get` `recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

  * `storage.anywhereCaches.create`
  * `storage.anywhereCaches.disable`
  * `storage.anywhereCaches.get`
  * `storage.anywhereCaches.list`
  * `storage.anywhereCaches.pause`
  * `storage.anywhereCaches.resume`
  * `storage.anywhereCaches.update`

`storage.bucketOperations.*`

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`

`storage.buckets.*`

  * `storage.buckets.create`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.delete`
  * `storage.buckets.deleteTagBinding`
  * `storage.buckets.enableObjectRetention`
  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.getIpFilter`
  * `storage.buckets.getObjectInsights`
  * `storage.buckets.list`
  * `storage.buckets.listEffectiveTags`
  * `storage.buckets.listTagBindings`
  * `storage.buckets.relocate`
  * `storage.buckets.restore`
  * `storage.buckets.setIamPolicy`
  * `storage.buckets.setIpFilter`
  * `storage.buckets.update`
  * `storage.buckets.viewIntelligenceDetails`
  * `storage.buckets.viewSecurityIntelligenceDetails`

`storage.featureConfigs.*`

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.delete`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.update`

`storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.intelligenceConfigs.*`

  * `storage.intelligenceConfigs.get`
  * `storage.intelligenceConfigs.update`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

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

`storagebatchoperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`
  * `storagebatchoperations.jobs.cancel`
  * `storagebatchoperations.jobs.create`
  * `storagebatchoperations.jobs.delete`
  * `storagebatchoperations.jobs.get`
  * `storagebatchoperations.jobs.list`
  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`
  * `storagebatchoperations.operations.cancel`
  * `storagebatchoperations.operations.delete`
  * `storagebatchoperations.operations.get`
  * `storagebatchoperations.operations.list`

  
  
## Visual Inspection AI permissions

Permission | Included in roles  
---|---  
  
#### `visualinspection.annotationSets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.annotationSets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.annotationSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.annotationSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.annotationSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.annotationSpecs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.annotationSpecs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.annotationSpecs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.annotationSpecs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.annotations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.annotations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.annotations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.annotations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.annotations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.datasets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.datasets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.datasets.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.datasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.datasets.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.datasets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.datasets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.images.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.images.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.images.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.images.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.locations.reportUsageMetrics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Usage Metrics Reporter](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.usageMetricsReporter) (`roles/visualinspection.usageMetricsReporter`)   
  
#### `visualinspection.modelEvaluations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.modelEvaluations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.models.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.models.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.models.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.models.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.models.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.models.writePrediction`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.modules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.modules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.modules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.modules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.modules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.solutionArtifacts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.solutionArtifacts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.solutionArtifacts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.solutionArtifacts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.solutionArtifacts.predict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.solutionArtifacts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.solutions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.solutions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)   
  
#### `visualinspection.solutions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `visualinspection.solutions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Visual Inspection AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.admin) (`roles/visualinspection.admin`)  [Visual Inspection AI Solution Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.editor) (`roles/visualinspection.editor`)  [Visual Inspection AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.viewer) (`roles/visualinspection.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
