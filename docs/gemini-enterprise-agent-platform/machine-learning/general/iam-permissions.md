---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/iam-permissions/
title: Gemini Enterprise Agent Platform IAM permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:43:43.867302+00:00
---

# Gemini Enterprise Agent Platform IAM permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini Enterprise Agent Platform IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists common Agent Platform operations and the permissions that they require.

To determine if one or more **permissions** are included in a [Gemini Enterprise Agent Platform IAM role](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control), you can use one of the following methods:

  * The [`gcloud iam roles describe`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/describe) command
  * The [`roles.get()`](https://docs.cloud.google.com/iam/reference/rest/v1/roles/get) method in the IAM API



  


Resource | Operation | Permissions needed  
---|---|---  
batchPredictionJobs  |  [Cancel a batchPredictionJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.batchPredictionJobs/cancel) | 

  * aiplatform.batchPredictionJobs.cancel (permission needed on the `name` resource) 

  
batchPredictionJobs  |  [Create a batchPredictionJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.batchPredictionJobs/create) | 

  * aiplatform.batchPredictionJobs.create (permission needed on the `parent` resource) 

  
batchPredictionJobs  |  [Delete a batchPredictionJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.batchPredictionJobs/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.batchPredictionJobs.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.batchPredictionJobs.get (to call GET on the long-running operation returned)
  * aiplatform.batchPredictionJobs.get (to call DELETE on the long-running operation returned)
  * aiplatform.batchPredictionJobs.get (to call WAIT on the long-running operation returned)
  * aiplatform.batchPredictionJobs.delete (to call CANCEL on the long-running operation returned)

  
batchPredictionJobs  |  [Get a batchPredictionJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.batchPredictionJobs/get) | 

  * aiplatform.batchPredictionJobs.get (permission needed on the `name` resource) 

  
batchPredictionJobs  |  [List a batchPredictionJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.batchPredictionJobs/list) | 

  * aiplatform.batchPredictionJobs.list (permission needed on the `parent` resource) 

  
customJobs  |  [Cancel a customJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/cancel) | 

  * aiplatform.customJobs.cancel (permission needed on the `name` resource) 

  
customJobs  |  [Create a customJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/create) | 

  * aiplatform.customJobs.create (permission needed on the `parent` resource) 

  
customJobs  |  [Delete a customJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.customJobs.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.customJobs.get (to call GET on the long-running operation returned)
  * aiplatform.customJobs.get (to call DELETE on the long-running operation returned)
  * aiplatform.customJobs.get (to call WAIT on the long-running operation returned)
  * aiplatform.customJobs.delete (to call CANCEL on the long-running operation returned)

  
customJobs  |  [Get a customJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/get) | 

  * aiplatform.customJobs.get (permission needed on the `name` resource) 

  
customJobs  |  [List a customJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.customJobs/list) | 

  * aiplatform.customJobs.list (permission needed on the `parent` resource) 

  
datasets  |  [Create a dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.datasets.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.update (to call CANCEL on the long-running operation returned)

  
datasets  |  [Delete a dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.datasets.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.delete (to call CANCEL on the long-running operation returned)

  
datasets  |  [Export a dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/export) †  
  
  
† Starts a long-running operation | 

  * aiplatform.datasets.export (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.export (to call CANCEL on the long-running operation returned)

  
datasets  |  [Get a dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/get) | 

  * aiplatform.datasets.get (permission needed on the `name` resource) 

  
datasets  |  [Import a dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/import) †  
  
  
† Starts a long-running operation | 

  * aiplatform.datasets.import (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.import (to call CANCEL on the long-running operation returned)

  
datasets  |  [List a dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/list) | 

  * aiplatform.datasets.list (permission needed on the `parent` resource) 

  
datasets  |  [Update a dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/patch) | 

  * aiplatform.datasets.update (permission needed on the `name` resource) 

  
datasets.annotationSpecs  |  [Get a dataset's annotationSpecs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets.annotationSpecs/get) | 

  * aiplatform.annotationSpecs.get (permission needed on the `name` resource) 

  
datasets.dataItems  |  [List a dataset's dataItems](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets.dataItems/list) | 

  * aiplatform.dataItems.list (permission needed on the `parent` resource) 

  
datasets.dataItems.annotations  |  [List a dataset.dataItems.annotations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets.dataItems.annotations/list) | 

  * aiplatform.annotations.list (permission needed on the `parent` resource) 

  
datasets.savedQueries  |  [Lists SavedQueries in a Dataset.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets.savedQueries/list) | 

  * aiplatform.datasets.get (permission needed on the `parent` resource) 

  
endpoints  |  [Create an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.endpoints.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.endpoints.get (to call GET on the long-running operation returned)
  * aiplatform.endpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.endpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.endpoints.update (to call CANCEL on the long-running operation returned)

  
endpoints  |  [Delete an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.endpoints.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.endpoints.get (to call GET on the long-running operation returned)
  * aiplatform.endpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.endpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.endpoints.delete (to call CANCEL on the long-running operation returned)

  
endpoints  |  [Deploy model to an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/deployModel) †  
  
  
† Starts a long-running operation | 

  * aiplatform.endpoints.deploy (permission needed on the `endpoint` resource) 

  
**Other permissions:**

  * aiplatform.endpoints.get (to call GET on the long-running operation returned)
  * aiplatform.endpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.endpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.endpoints.deploy (to call CANCEL on the long-running operation returned)

  
endpoints  |  [Explain an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/explain) | 

  * aiplatform.endpoints.explain (permission needed on the `endpoint` resource) 

  
endpoints  |  [Get an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/get) | 

  * aiplatform.endpoints.get (permission needed on the `name` resource) 

  
endpoints  |  [List an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/list) | 

  * aiplatform.endpoints.list (permission needed on the `parent` resource) 

  
endpoints  |  [Update an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/patch) | 

  * aiplatform.endpoints.update (permission needed on the `name` resource) 

  
endpoints  |  [Predict an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/predict) | 

  * aiplatform.endpoints.predict (permission needed on the `endpoint` resource) 

  
endpoints  |  [Perform an online prediction with an arbitrary HTTP payload.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/rawPredict) | 

  * aiplatform.endpoints.predict (permission needed on the `endpoint` resource) 

  
endpoints  |  [Undeploy a model to an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/undeployModel) †  
  
  
† Starts a long-running operation | 

  * aiplatform.endpoints.undeploy (permission needed on the `endpoint` resource) 

  
**Other permissions:**

  * aiplatform.endpoints.get (to call GET on the long-running operation returned)
  * aiplatform.endpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.endpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.endpoints.undeploy (to call CANCEL on the long-running operation returned)

  
featurestores  |  [Batch reads Feature values from a Featurestore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/batchReadFeatureValues) †  
  
  
† Starts a long-running operation | 

  * aiplatform.featurestores.batchReadFeatureValues (permission needed on the `featurestore` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)
  * aiplatform.featurestores.get (to call WAIT on the long-running operation returned)
  * aiplatform.featurestores.batchReadFeatureValues (to call CANCEL on the long-running operation returned)

  
featurestores  |  [Creates a new Featurestore in a given project and location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.featurestores.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)
  * aiplatform.featurestores.get (to call WAIT on the long-running operation returned)
  * aiplatform.featurestores.update (to call CANCEL on the long-running operation returned)

  
featurestores  |  [Deletes a single Featurestore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.featurestores.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)

  
featurestores  |  [Gets details of a single Featurestore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/get) | 

  * aiplatform.featurestores.get (permission needed on the `name` resource) 

  
featurestores  |  [Lists Featurestores in a given project and location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/list) | 

  * aiplatform.featurestores.list (permission needed on the `parent` resource) 

  
featurestores  |  [Updates the parameters of a single Featurestore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/patch) †  
  
  
† Starts a long-running operation | 

  * aiplatform.featurestores.update (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)

  
featurestores  |  [Searches Features matching a query in a given project.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/searchFeatures) | 

  * aiplatform.features.list (permission needed on the `location` resource) 

  
featurestores.entityTypes  |  [Creates a new EntityType in a given Featurestore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.entityTypes.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)
  * aiplatform.featurestores.get (to call WAIT on the long-running operation returned)
  * aiplatform.featurestores.update (to call CANCEL on the long-running operation returned)

  
featurestores.entityTypes  |  [Deletes a single EntityType.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.entityTypes.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)
  * aiplatform.featurestores.get (to call WAIT on the long-running operation returned)
  * aiplatform.featurestores.update (to call CANCEL on the long-running operation returned)

  
featurestores.entityTypes  |  [Exports Feature values from all the entities of a target EntityType.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/exportFeatureValues) †  
  
  
† Starts a long-running operation | 

  * aiplatform.entityTypes.exportFeatureValues (permission needed on the `entityType` resource) 

  
**Other permissions:**

  * aiplatform.entityTypes.get (to call GET on the long-running operation returned)
  * aiplatform.entityTypes.update (to call DELETE on the long-running operation returned)
  * aiplatform.entityTypes.get (to call WAIT on the long-running operation returned)
  * aiplatform.entityTypes.exportFeatureValues (to call CANCEL on the long-running operation returned)

  
featurestores.entityTypes  |  [Gets details of a single EntityType.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/get) | 

  * aiplatform.entityTypes.get (permission needed on the `name` resource) 

  
featurestores.entityTypes  |  [Imports Feature values into the Featurestore from a source storage.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/importFeatureValues) †  
  
  
† Starts a long-running operation | 

  * aiplatform.entityTypes.importFeatureValues (permission needed on the `entityType` resource) 

  
**Other permissions:**

  * aiplatform.entityTypes.get (to call GET on the long-running operation returned)
  * aiplatform.entityTypes.update (to call DELETE on the long-running operation returned)
  * aiplatform.entityTypes.get (to call WAIT on the long-running operation returned)
  * aiplatform.entityTypes.importFeatureValues (to call CANCEL on the long-running operation returned)

  
featurestores.entityTypes  |  [Lists EntityTypes in a given Featurestore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/list) | 

  * aiplatform.entityTypes.list (permission needed on the `parent` resource) 

  
featurestores.entityTypes  |  [Updates the parameters of a single EntityType.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/patch) | 

  * aiplatform.entityTypes.update (permission needed on the `name` resource) 

  
featurestores.entityTypes  |  [Reads Feature values of a specific entity of an EntityType.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/readFeatureValues) | 

  * aiplatform.entityTypes.readFeatureValues (permission needed on the `entityType` resource) 

  
featurestores.entityTypes  |  [Reads Feature values for multiple entities.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes/streamingReadFeatureValues) | 

  * aiplatform.entityTypes.streamingReadFeatureValues (permission needed on the `entityType` resource) 

  
featurestores.entityTypes.features  |  [Creates a batch of Features in a given EntityType.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/batchCreate) †  
  
  
† Starts a long-running operation | 

  * aiplatform.features.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)
  * aiplatform.featurestores.get (to call WAIT on the long-running operation returned)
  * aiplatform.featurestores.update (to call CANCEL on the long-running operation returned)

  
featurestores.entityTypes.features  |  [Creates a new Feature in a given EntityType.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.features.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)
  * aiplatform.featurestores.get (to call WAIT on the long-running operation returned)
  * aiplatform.featurestores.update (to call CANCEL on the long-running operation returned)

  
featurestores.entityTypes.features  |  [Deletes a single Feature.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.features.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)
  * aiplatform.featurestores.get (to call WAIT on the long-running operation returned)
  * aiplatform.featurestores.update (to call CANCEL on the long-running operation returned)

  
featurestores.entityTypes.features  |  [Gets details of a single Feature.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/get) | 

  * aiplatform.features.get (permission needed on the `name` resource) 

  
featurestores.entityTypes.features  |  [Lists Features in a given EntityType.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/list) | 

  * aiplatform.features.list (permission needed on the `parent` resource) 

  
featurestores.entityTypes.features  |  [Updates the paramters of a single Feature](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/patch) | 

  * aiplatform.features.update (permission needed on the `name` resource) 

  
hyperparameterTuningJobs  |  [Cancel a hyperparameterTuningJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/cancel) | 

  * aiplatform.hyperparameterTuningJobs.cancel (permission needed on the `name` resource) 

  
hyperparameterTuningJobs  |  [Create a hyperparameterTuningJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/create) | 

  * aiplatform.hyperparameterTuningJobs.create (permission needed on the `parent` resource) 

  
hyperparameterTuningJobs  |  [Delete a hyperparameterTuningJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/delete) | 

  * aiplatform.hyperparameterTuningJobs.delete (permission needed on the `name` resource) 

  
hyperparameterTuningJobs  |  [Get a hyperparameterTuningJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/get) | 

  * aiplatform.hyperparameterTuningJobs.get (permission needed on the `name` resource) 

  
hyperparameterTuningJobs  |  [List a hyperparameterTuningJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/list) | 

  * aiplatform.hyperparameterTuningJobs.list (permission needed on the `parent` resource) 

  
indexEndpoints  |  [Creates an IndexEndpoint.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexEndpoints/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.indexEndpoints.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.indexEndpoints.get (to call GET on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexEndpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call CANCEL on the long-running operation returned)

  
indexEndpoints  |  [Deletes an IndexEndpoint.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexEndpoints/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.indexEndpoints.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.indexEndpoints.get (to call GET on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexEndpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call CANCEL on the long-running operation returned)

  
indexEndpoints  |  [Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexEndpoints/deployIndex) †  
  
  
† Starts a long-running operation | 

  * aiplatform.indexEndpoints.deploy (permission needed on the `indexEndpoint` resource) 

  
**Other permissions:**

  * aiplatform.indexEndpoints.get (to call GET on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexEndpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call CANCEL on the long-running operation returned)

  
indexEndpoints  |  [Gets an IndexEndpoint.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexEndpoints/get) | 

  * aiplatform.indexEndpoints.get (permission needed on the `name` resource) 

  
indexEndpoints  |  [Lists IndexEndpoints in a Location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexEndpoints/list) | 

  * aiplatform.indexEndpoints.list (permission needed on the `parent` resource) 

  
indexEndpoints  |  [Update an existing DeployedIndex under an IndexEndpoint.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexEndpoints/mutateDeployedIndex) †  
  
  
† Starts a long-running operation | 

  * aiplatform.indexEndpoints.deploy (permission needed on the `indexEndpoint` resource) 

  
**Other permissions:**

  * aiplatform.indexEndpoints.get (to call GET on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexEndpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call CANCEL on the long-running operation returned)

  
indexEndpoints  |  [Updates an IndexEndpoint.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexEndpoints/patch) | 

  * aiplatform.indexEndpoints.update (permission needed on the `name` resource) 

  
indexEndpoints  |  [Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexEndpoints/undeployIndex) †  
  
  
† Starts a long-running operation | 

  * aiplatform.indexEndpoints.undeploy (permission needed on the `indexEndpoint` resource) 

  
**Other permissions:**

  * aiplatform.indexEndpoints.get (to call GET on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexEndpoints.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexEndpoints.update (to call CANCEL on the long-running operation returned)

  
indexes  |  [Creates an Index.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexes/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.indexes.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.indexes.get (to call GET on the long-running operation returned)
  * aiplatform.indexes.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexes.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexes.update (to call CANCEL on the long-running operation returned)

  
indexes  |  [Deletes an Index.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexes/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.indexes.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.indexes.get (to call GET on the long-running operation returned)
  * aiplatform.indexes.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexes.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexes.update (to call CANCEL on the long-running operation returned)

  
indexes  |  [Gets an Index.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexes/get) | 

  * aiplatform.indexes.get (permission needed on the `name` resource) 

  
indexes  |  [Lists Indexes in a Location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexes/list) | 

  * aiplatform.indexes.list (permission needed on the `parent` resource) 

  
indexes  |  [Updates an Index.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexes/patch) †  
  
  
† Starts a long-running operation | 

  * aiplatform.indexes.update (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.indexes.get (to call GET on the long-running operation returned)
  * aiplatform.indexes.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexes.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexes.update (to call CANCEL on the long-running operation returned)

  
metadataStores  |  [Initializes a MetadataStore, including allocation of resources.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.metadataStores.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.locations.get (to call GET on the long-running operation returned)
  * aiplatform.locations.get (to call DELETE on the long-running operation returned)
  * aiplatform.locations.get (to call WAIT on the long-running operation returned)
  * aiplatform.locations.get (to call CANCEL on the long-running operation returned)

  
metadataStores  |  [Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.metadataStores.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.locations.get (to call GET on the long-running operation returned)
  * aiplatform.locations.get (to call DELETE on the long-running operation returned)
  * aiplatform.locations.get (to call WAIT on the long-running operation returned)
  * aiplatform.locations.get (to call CANCEL on the long-running operation returned)

  
metadataStores  |  [Retrieves a specific MetadataStore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores/get) | 

  * aiplatform.metadataStores.get (permission needed on the `name` resource) 

  
metadataStores  |  [Lists MetadataStores for a Location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores/list) | 

  * aiplatform.metadataStores.list (permission needed on the `parent` resource) 

  
metadataStores.artifacts  |  [Creates an Artifact associated with a MetadataStore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts/create) | 

  * aiplatform.artifacts.create (permission needed on the `parent` resource) 

  
metadataStores.artifacts  |  [Deletes an Artifact.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.artifacts.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.artifacts.get (to call GET on the long-running operation returned)
  * aiplatform.artifacts.delete (to call DELETE on the long-running operation returned)
  * aiplatform.artifacts.get (to call WAIT on the long-running operation returned)
  * aiplatform.artifacts.delete (to call CANCEL on the long-running operation returned)

  
metadataStores.artifacts  |  [Retrieves a specific Artifact.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts/get) | 

  * aiplatform.artifacts.get (permission needed on the `name` resource) 

  
metadataStores.artifacts  |  [Lists Artifacts in the MetadataStore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts/list) | 

  * aiplatform.artifacts.list (permission needed on the `parent` resource) 

  
metadataStores.artifacts  |  [Updates a stored Artifact.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts/patch) | 

  * aiplatform.artifacts.update (permission needed on the `name` resource) 

  
metadataStores.artifacts  |  [Purges Artifacts.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts/purge) †  
  
  
† Starts a long-running operation | 

  * aiplatform.artifacts.delete (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.artifacts.get (to call GET on the long-running operation returned)
  * aiplatform.artifacts.delete (to call DELETE on the long-running operation returned)
  * aiplatform.artifacts.get (to call WAIT on the long-running operation returned)
  * aiplatform.artifacts.delete (to call CANCEL on the long-running operation returned)

  
metadataStores.artifacts  |  [Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts/queryArtifactLineageSubgraph) | 

  * aiplatform.artifacts.get (permission needed on the `artifact` resource) 

  
metadataStores.contexts  |  [Adds a set of Artifacts and Executions to a Context.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/addContextArtifactsAndExecutions) | 

  * aiplatform.contexts.addContextArtifactsAndExecutions (permission needed on the `context` resource) 

  
metadataStores.contexts  |  [Adds a set of Contexts as children to a parent Context.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/addContextChildren) | 

  * aiplatform.contexts.addContextChildren (permission needed on the `context` resource) 

  
metadataStores.contexts  |  [Creates a Context associated with a MetadataStore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/create) | 

  * aiplatform.contexts.create (permission needed on the `parent` resource) 

  
metadataStores.contexts  |  [Deletes a stored Context.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.contexts.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.contexts.get (to call GET on the long-running operation returned)
  * aiplatform.contexts.delete (to call DELETE on the long-running operation returned)
  * aiplatform.contexts.get (to call WAIT on the long-running operation returned)
  * aiplatform.contexts.delete (to call CANCEL on the long-running operation returned)

  
metadataStores.contexts  |  [Retrieves a specific Context.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/get) | 

  * aiplatform.contexts.get (permission needed on the `name` resource) 

  
metadataStores.contexts  |  [Lists Contexts on the MetadataStore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/list) | 

  * aiplatform.contexts.list (permission needed on the `parent` resource) 

  
metadataStores.contexts  |  [Updates a stored Context.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/patch) | 

  * aiplatform.contexts.update (permission needed on the `name` resource) 

  
metadataStores.contexts  |  [Purges Contexts.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/purge) †  
  
  
† Starts a long-running operation | 

  * aiplatform.contexts.delete (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.contexts.get (to call GET on the long-running operation returned)
  * aiplatform.contexts.delete (to call DELETE on the long-running operation returned)
  * aiplatform.contexts.get (to call WAIT on the long-running operation returned)
  * aiplatform.contexts.delete (to call CANCEL on the long-running operation returned)

  
metadataStores.contexts  |  [Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.contexts/queryContextLineageSubgraph) | 

  * aiplatform.contexts.queryContextLineageSubgraph (permission needed on the `context` resource) 

  
metadataStores.executions  |  [Adds Events to the specified Execution.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/addExecutionEvents) | 

  * aiplatform.executions.addExecutionEvents (permission needed on the `execution` resource) 

  
metadataStores.executions  |  [Creates an Execution associated with a MetadataStore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/create) | 

  * aiplatform.executions.create (permission needed on the `parent` resource) 

  
metadataStores.executions  |  [Deletes an Execution.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.executions.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.executions.get (to call GET on the long-running operation returned)
  * aiplatform.executions.delete (to call DELETE on the long-running operation returned)
  * aiplatform.executions.get (to call WAIT on the long-running operation returned)
  * aiplatform.executions.delete (to call CANCEL on the long-running operation returned)

  
metadataStores.executions  |  [Retrieves a specific Execution.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/get) | 

  * aiplatform.executions.get (permission needed on the `name` resource) 

  
metadataStores.executions  |  [Lists Executions in the MetadataStore.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/list) | 

  * aiplatform.executions.list (permission needed on the `parent` resource) 

  
metadataStores.executions  |  [Updates a stored Execution.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/patch) | 

  * aiplatform.executions.update (permission needed on the `name` resource) 

  
metadataStores.executions  |  [Purges Executions.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/purge) †  
  
  
† Starts a long-running operation | 

  * aiplatform.executions.delete (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.executions.get (to call GET on the long-running operation returned)
  * aiplatform.executions.delete (to call DELETE on the long-running operation returned)
  * aiplatform.executions.get (to call WAIT on the long-running operation returned)
  * aiplatform.executions.delete (to call CANCEL on the long-running operation returned)

  
metadataStores.executions  |  [Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/queryExecutionInputsAndOutputs) | 

  * aiplatform.executions.queryExecutionInputsAndOutputs (permission needed on the `execution` resource) 

  
metadataStores.metadataSchemas  |  [Creates a MetadataSchema.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas/create) | 

  * aiplatform.metadataSchemas.create (permission needed on the `parent` resource) 

  
metadataStores.metadataSchemas  |  [Retrieves a specific MetadataSchema.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas/get) | 

  * aiplatform.metadataSchemas.get (permission needed on the `name` resource) 

  
metadataStores.metadataSchemas  |  [Lists MetadataSchemas.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.metadataSchemas/list) | 

  * aiplatform.metadataSchemas.list (permission needed on the `parent` resource) 

  
migratableResources  |  [Batchmigrate a migratableResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.migratableResources/batchMigrate) | 

  * aiplatform.migratableResources.migrate (permission needed on the `parent` resource) 

  
migratableResources  |  [Search a migratableResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.migratableResources/search) | 

  * aiplatform.migratableResources.search (permission needed on the `parent` resource) 

  
modelDeploymentMonitoringJobs  |  [Creates a ModelDeploymentMonitoringJob.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs/create) | 

  * aiplatform.modelDeploymentMonitoringJobs.create (permission needed on the `parent` resource) 

  
modelDeploymentMonitoringJobs  |  [Deletes a ModelDeploymentMonitoringJob.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.modelDeploymentMonitoringJobs.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.indexes.get (to call GET on the long-running operation returned)
  * aiplatform.indexes.update (to call DELETE on the long-running operation returned)
  * aiplatform.indexes.get (to call WAIT on the long-running operation returned)
  * aiplatform.indexes.update (to call CANCEL on the long-running operation returned)

  
modelDeploymentMonitoringJobs  |  [Gets a ModelDeploymentMonitoringJob.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs/get) | 

  * aiplatform.modelDeploymentMonitoringJobs.get (permission needed on the `name` resource) 

  
modelDeploymentMonitoringJobs  |  [Lists ModelDeploymentMonitoringJobs in a Location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs/list) | 

  * aiplatform.modelDeploymentMonitoringJobs.list (permission needed on the `parent` resource) 

  
modelDeploymentMonitoringJobs  |  [Updates a ModelDeploymentMonitoringJob.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs/patch) †  
  
  
† Starts a long-running operation | 

  * aiplatform.modelDeploymentMonitoringJobs.update (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.modelDeploymentMonitoringJobs.get (to call GET on the long-running operation returned)
  * aiplatform.modelDeploymentMonitoringJobs.update (to call DELETE on the long-running operation returned)

  
modelDeploymentMonitoringJobs  |  [Pauses a ModelDeploymentMonitoringJob.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs/pause) | 

  * aiplatform.modelDeploymentMonitoringJobs.pause (permission needed on the `name` resource) 

  
modelDeploymentMonitoringJobs  |  [Resumes a paused ModelDeploymentMonitoringJob.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs/resume) | 

  * aiplatform.modelDeploymentMonitoringJobs.resume (permission needed on the `name` resource) 

  
modelDeploymentMonitoringJobs  |  [Searches Model Monitoring Statistics generated within a given time window.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs/searchModelDeploymentMonitoringStatsAnomalies) | 

  * aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies (permission needed on the `modelDeploymentMonitoringJob` resource) 

  
models  |  [Delete a model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.models.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.models.get (to call GET on the long-running operation returned)
  * aiplatform.models.get (to call DELETE on the long-running operation returned)
  * aiplatform.models.get (to call WAIT on the long-running operation returned)
  * aiplatform.models.delete (to call CANCEL on the long-running operation returned)

  
models  |  [Export a model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/export) †  
  
  
† Starts a long-running operation | 

  * aiplatform.models.export (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.models.get (to call GET on the long-running operation returned)
  * aiplatform.models.get (to call DELETE on the long-running operation returned)
  * aiplatform.models.get (to call WAIT on the long-running operation returned)
  * aiplatform.models.export (to call CANCEL on the long-running operation returned)

  
models  |  [Get a model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/get) | 

  * aiplatform.models.get (permission needed on the `name` resource) 

  
models  |  [List a model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/list) | 

  * aiplatform.models.list (permission needed on the `parent` resource) 

  
models  |  [Update a model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/patch) | 

  * aiplatform.models.update (permission needed on the `name` resource) 

  
models  |  [Upload a model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/upload) †  
  
  
† Starts a long-running operation | 

  * aiplatform.models.upload (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.models.get (to call GET on the long-running operation returned)
  * aiplatform.models.get (to call DELETE on the long-running operation returned)
  * aiplatform.models.get (to call WAIT on the long-running operation returned)
  * aiplatform.models.update (to call CANCEL on the long-running operation returned)

  
models.evaluations  |  [Get a model evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models.evaluations/get) | 

  * aiplatform.modelEvaluations.get (permission needed on the `name` resource) 

  
models.evaluations  |  [List a model evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models.evaluations/list) | 

  * aiplatform.modelEvaluations.list (permission needed on the `parent` resource) 

  
models.evaluations.slices  |  [Get a model evaluations slice](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models.evaluations.slices/get) | 

  * aiplatform.modelEvaluationSlices.get (permission needed on the `name` resource) 

  
models.evaluations.slices  |  [List a model evaluations slice](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models.evaluations.slices/list) | 

  * aiplatform.modelEvaluationSlices.list (permission needed on the `parent` resource) 

  
pipelineJobs  |  [Cancel a pipelineJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.pipelineJobs/cancel) | 

  * aiplatform.pipelineJobs.cancel (permission needed on the `name` resource) 

  
pipelineJobs  |  [Create a pipelineJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.pipelineJobs/create) | 

  * aiplatform.pipelineJobs.create (permission needed on the `parent` resource) 

  
pipelineJobs  |  [Delete a pipelineJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.pipelineJobs/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.pipelineJobs.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.pipelinejobs.get (to call GET on the long-running operation returned)
  * aiplatform.pipelinejobs.get (to call DELETE on the long-running operation returned)

  
pipelineJobs  |  [Get a pipelineJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.pipelineJobs/get) | 

  * aiplatform.pipelineJobs.get (permission needed on the `name` resource) 

  
pipelineJobs  |  [List a pipelineJob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.pipelineJobs/list) | 

  * aiplatform.pipelineJobs.list (permission needed on the `parent` resource) 

  
specialistPools  |  [Create a specialistPool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.specialistPools.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.specialistPools.get (to call GET on the long-running operation returned)
  * aiplatform.specialistPools.update (to call DELETE on the long-running operation returned)
  * aiplatform.specialistPools.get (to call WAIT on the long-running operation returned)
  * aiplatform.specialistPools.update (to call CANCEL on the long-running operation returned)

  
specialistPools  |  [Delete a specialistPool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.specialistPools.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.specialistPools.get (to call GET on the long-running operation returned)
  * aiplatform.specialistPools.update (to call DELETE on the long-running operation returned)
  * aiplatform.specialistPools.get (to call WAIT on the long-running operation returned)
  * aiplatform.specialistPools.delete (to call CANCEL on the long-running operation returned)

  
specialistPools  |  [Get a specialistPool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/get) | 

  * aiplatform.specialistPools.get (permission needed on the `name` resource) 

  
specialistPools  |  [List a specialistPool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/list) | 

  * aiplatform.specialistPools.list (permission needed on the `parent` resource) 

  
specialistPools  |  [Update a specialistPool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/patch) †  
  
  
† Starts a long-running operation | 

  * aiplatform.specialistPools.update (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.specialistPools.get (to call GET on the long-running operation returned)
  * aiplatform.specialistPools.update (to call DELETE on the long-running operation returned)
  * aiplatform.specialistPools.get (to call WAIT on the long-running operation returned)
  * aiplatform.specialistPools.update (to call CANCEL on the long-running operation returned)

  
studies  |  [Creates a Study.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies/create) | 

  * aiplatform.studies.create (permission needed on the `parent` resource) 

  
studies  |  [Deletes a Study.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies/delete) | 

  * aiplatform.studies.delete (permission needed on the `name` resource) 

  
studies  |  [Gets a Study by name.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies/get) | 

  * aiplatform.studies.get (permission needed on the `name` resource) 

  
studies  |  [Lists all the studies in a region for an associated project.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies/list) | 

  * aiplatform.studies.list (permission needed on the `parent` resource) 

  
studies  |  [Looks a study up using the user-defined displayName field instead of the fully qualified resource name.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies/lookup) | 

  * aiplatform.studies.list (permission needed on the `parent` resource) 

  
studies.trials  |  [Adds a measurement of the objective metrics to a Trial.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/addTrialMeasurement) | 

  * aiplatform.trials.update (permission needed on the `trialName` resource) 

  
studies.trials  |  [Checks whether a Trial should stop or not.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/checkTrialEarlyStoppingState) †  
  
  
† Starts a long-running operation | 

  * aiplatform.trials.get (permission needed on the `trialName` resource) 

  
**Other permissions:**

  * aiplatform.trials.get (to call GET on the long-running operation returned)
  * aiplatform.trials.update (to call DELETE on the long-running operation returned)
  * aiplatform.trials.get (to call WAIT on the long-running operation returned)
  * aiplatform.trials.update (to call CANCEL on the long-running operation returned)

  
studies.trials  |  [Marks a Trial as complete.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/complete) | 

  * aiplatform.trials.update (permission needed on the `name` resource) 

  
studies.trials  |  [Adds a user provided Trial to a Study.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/create) | 

  * aiplatform.trials.create (permission needed on the `parent` resource) 

  
studies.trials  |  [Deletes a Trial.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/delete) | 

  * aiplatform.trials.delete (permission needed on the `name` resource) 

  
studies.trials  |  [Gets a Trial.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/get) | 

  * aiplatform.trials.get (permission needed on the `name` resource) 

  
studies.trials  |  [Lists the Trials associated with a Study.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/list) | 

  * aiplatform.trials.list (permission needed on the `parent` resource) 

  
studies.trials  |  [Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/listOptimalTrials) | 

  * aiplatform.trials.list (permission needed on the `parent` resource) 

  
studies.trials  |  [Stops a Trial.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/stop) | 

  * aiplatform.trials.update (permission needed on the `name` resource) 

  
studies.trials  |  [Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials/suggest) †  
  
  
† Starts a long-running operation | 

  * aiplatform.trials.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.studies.get (to call GET on the long-running operation returned)
  * aiplatform.studies.update (to call DELETE on the long-running operation returned)
  * aiplatform.studies.get (to call WAIT on the long-running operation returned)
  * aiplatform.studies.update (to call CANCEL on the long-running operation returned)

  
tensorboards  |  [Creates a Tensorboard.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/create) †  
  
  
† Starts a long-running operation | 

  * aiplatform.tensorboards.create (permission needed on the `parent` resource) 

  
**Other permissions:**

  * aiplatform.locations.get (to call GET on the long-running operation returned)
  * aiplatform.locations.get (to call DELETE on the long-running operation returned)
  * aiplatform.locations.get (to call WAIT on the long-running operation returned)
  * aiplatform.locations.get (to call CANCEL on the long-running operation returned)

  
tensorboards  |  [Deletes a Tensorboard.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.tensorboards.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.tensorboardRuns.get (to call GET on the long-running operation returned)
  * aiplatform.tensorboardRuns.update (to call DELETE on the long-running operation returned)
  * aiplatform.tensorboardRuns.get (to call WAIT on the long-running operation returned)
  * aiplatform.tensorboardRuns.delete (to call CANCEL on the long-running operation returned)

  
tensorboards  |  [Gets a Tensorboard.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/get) | 

  * aiplatform.tensorboards.get (permission needed on the `name` resource) 

  
tensorboards  |  [Lists Tensorboards in a Location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/list) | 

  * aiplatform.tensorboards.list (permission needed on the `parent` resource) 

  
tensorboards  |  [Updates a Tensorboard.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/patch) †  
  
  
† Starts a long-running operation | 

  * aiplatform.tensorboards.update (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.tensorboards.get (to call GET on the long-running operation returned)
  * aiplatform.tensorboards.update (to call DELETE on the long-running operation returned)
  * aiplatform.tensorboards.get (to call WAIT on the long-running operation returned)
  * aiplatform.tensorboards.update (to call CANCEL on the long-running operation returned)

  
tensorboards.experiments  |  [Creates a TensorboardExperiment.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/create) | 

  * aiplatform.tensorboardExperiments.create (permission needed on the `parent` resource) 

  
tensorboards.experiments  |  [Deletes a TensorboardExperiment.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.tensorboardExperiments.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.tensorboardExperiments.get (to call GET on the long-running operation returned)
  * aiplatform.tensorboardExperiments.update (to call DELETE on the long-running operation returned)
  * aiplatform.tensorboardExperiments.get (to call WAIT on the long-running operation returned)
  * aiplatform.tensorboardExperiments.delete (to call CANCEL on the long-running operation returned)

  
tensorboards.experiments  |  [Gets a TensorboardExperiment.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/get) | 

  * aiplatform.tensorboardExperiments.get (permission needed on the `name` resource) 

  
tensorboards.experiments  |  [Lists TensorboardExperiments in a Location](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/list) | 

  * aiplatform.tensorboardExperiments.list (permission needed on the `parent` resource) 

  
tensorboards.experiments  |  [Updates a TensorboardExperiment.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/patch) | 

  * aiplatform.tensorboardExperiments.update (permission needed on the `name` resource) 

  
tensorboards.experiments  |  [Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun's.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/write) | 

  * aiplatform.tensorboardExperiments.write (permission needed on the `tensorboardExperiment` resource) 

  
tensorboards.experiments.runs  |  [Batch create TensorboardRuns.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/batchCreate) | 

  * aiplatform.tensorboardRuns.batchCreate (permission needed on the `parent` resource) 

  
tensorboards.experiments.runs  |  [Creates a TensorboardRun.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/create) | 

  * aiplatform.tensorboardRuns.create (permission needed on the `parent` resource) 

  
tensorboards.experiments.runs  |  [Deletes a TensorboardRun.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.tensorboardRuns.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.tensorboardRuns.get (to call GET on the long-running operation returned)
  * aiplatform.tensorboardRuns.update (to call DELETE on the long-running operation returned)
  * aiplatform.tensorboardRuns.get (to call WAIT on the long-running operation returned)
  * aiplatform.tensorboardRuns.delete (to call CANCEL on the long-running operation returned)

  
tensorboards.experiments.runs  |  [Gets a TensorboardRun.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/get) | 

  * aiplatform.tensorboardRuns.get (permission needed on the `name` resource) 

  
tensorboards.experiments.runs  |  [Lists TensorboardRuns in a Location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/list) | 

  * aiplatform.tensorboardRuns.list (permission needed on the `parent` resource) 

  
tensorboards.experiments.runs  |  [Updates a TensorboardRun.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/patch) | 

  * aiplatform.tensorboardRuns.update (permission needed on the `name` resource) 

  
tensorboards.experiments.runs  |  [Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/write) | 

  * aiplatform.tensorboardRuns.write (permission needed on the `tensorboardRun` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/batchCreate) | 

  * aiplatform.tensorboardTimeSeries.batchCreate (permission needed on the `parent` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Reads multiple TensorboardTimeSeries' data.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/batchRead) | 

  * aiplatform.tensorboardTimeSeries.batchRead (permission needed on the `tensorboard` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Creates a TensorboardTimeSeries.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/create) | 

  * aiplatform.tensorboardTimeSeries.create (permission needed on the `parent` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Deletes a TensorboardTimeSeries.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.tensorboardTimeSeries.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.tensorboardRuns.get (to call GET on the long-running operation returned)
  * aiplatform.tensorboardRuns.update (to call DELETE on the long-running operation returned)

  
tensorboards.experiments.runs.timeSeries  |  [Exports a TensorboardTimeSeries' data.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/exportTensorboardTimeSeries) | 

  * aiplatform.tensorboardTimeSeries.read (permission needed on the `tensorboardTimeSeries` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Gets a TensorboardTimeSeries.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/get) | 

  * aiplatform.tensorboardTimeSeries.get (permission needed on the `name` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Lists TensorboardTimeSeries in a Location.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/list) | 

  * aiplatform.tensorboardTimeSeries.list (permission needed on the `parent` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Updates a TensorboardTimeSeries.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/patch) | 

  * aiplatform.tensorboardTimeSeries.update (permission needed on the `name` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Reads a TensorboardTimeSeries' data.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/read) | 

  * aiplatform.tensorboardTimeSeries.read (permission needed on the `tensorboardTimeSeries` resource) 

  
tensorboards.experiments.runs.timeSeries  |  [Gets bytes of TensorboardBlobs.](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/readBlobData) | 

  * aiplatform.tensorboardTimeSeries.read (permission needed on the `timeSeries` resource) 

  
trainingPipelines  |  [Cancel a trainingPipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines/cancel) | 

  * aiplatform.trainingPipelines.cancel (permission needed on the `name` resource) 

  
trainingPipelines  |  [Create a trainingPipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines/create) | 

  * aiplatform.trainingPipelines.create (permission needed on the `parent` resource) 

  
trainingPipelines  |  [Delete a trainingPipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines/delete) †  
  
  
† Starts a long-running operation | 

  * aiplatform.trainingPipelines.delete (permission needed on the `name` resource) 

  
**Other permissions:**

  * aiplatform.trainingPipelines.get (to call GET on the long-running operation returned)
  * aiplatform.trainingPipelines.get (to call DELETE on the long-running operation returned)
  * aiplatform.trainingPipelines.get (to call WAIT on the long-running operation returned)
  * aiplatform.trainingPipelines.delete (to call CANCEL on the long-running operation returned)

  
trainingPipelines  |  [Get a trainingPipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines/get) | 

  * aiplatform.trainingPipelines.get (permission needed on the `name` resource) 

  
trainingPipelines  |  [List a trainingPipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines/list) | 

  * aiplatform.trainingPipelines.list (permission needed on the `parent` resource) 

  
N/A  |  Generic delete operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.locations.get (to call GET on the long-running operation returned)
  * aiplatform.locations.get (to call DELETE on the long-running operation returned)
  * aiplatform.locations.get (to call WAIT on the long-running operation returned)
  * aiplatform.locations.get (to call CANCEL on the long-running operation returned)

  
datasets  |  Delete data item operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.update (to call CANCEL on the long-running operation returned)

  
featurestores  |  Import features operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)
  * aiplatform.featurestores.update (to call DELETE on the long-running operation returned)
  * aiplatform.featurestores.get (to call WAIT on the long-running operation returned)
  * aiplatform.featurestores.importFeatures (to call CANCEL on the long-running operation returned)

  
datasets  |  Delete annotation operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.update (to call CANCEL on the long-running operation returned)

  
datasets  |  Batch delete DataItems operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.update (to call CANCEL on the long-running operation returned)

  
datasets  |  Generate stats operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.update (to call CANCEL on the long-running operation returned)

  
datasets  |  Delete AnnotationSpec operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.update (to call CANCEL on the long-running operation returned)

  
hyperparameterTuningJobs  |  Delete HP tuning job †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.hyperparameterTuningJobs.get (to call GET on the long-running operation returned)
  * aiplatform.hyperparameterTuningJobs.get (to call DELETE on the long-running operation returned)
  * aiplatform.hyperparameterTuningJobs.get (to call WAIT on the long-running operation returned)
  * aiplatform.hyperparameterTuningJobs.delete (to call CANCEL on the long-running operation returned)

  
nasJobs  |  Delete NAS job †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.nasJobs.get (to call GET on the long-running operation returned)
  * aiplatform.nasJobs.get (to call DELETE on the long-running operation returned)
  * aiplatform.nasJobs.get (to call WAIT on the long-running operation returned)
  * aiplatform.nasJobs.delete (to call CANCEL on the long-running operation returned)

  
N/A  |  Create HumanInTheLoop operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.locations.get (to call GET on the long-running operation returned)
  * aiplatform.locations.get (to call DELETE on the long-running operation returned)
  * aiplatform.locations.get (to call WAIT on the long-running operation returned)
  * aiplatform.locations.get (to call CANCEL on the long-running operation returned)

  
featurestores  |  Export features operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.featurestores.get (to call GET on the long-running operation returned)

  
N/A  |  Delete HumanInTheLoop operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.locations.get (to call GET on the long-running operation returned)
  * aiplatform.locations.get (to call DELETE on the long-running operation returned)

  
N/A  |  Send HumanInTheLoop entry operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.locations.get (to call GET on the long-running operation returned)
  * aiplatform.locations.get (to call DELETE on the long-running operation returned)
  * aiplatform.humanInTheLoops.send (to call CANCEL on the long-running operation returned)

  
datasets  |  Calculate data item label stats †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.update (to call CANCEL on the long-running operation returned)

  
N/A  |  Migrate resources operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.locations.get (to call GET on the long-running operation returned)
  * aiplatform.locations.get (to call DELETE on the long-running operation returned)

  
datasets  |  Create DataItem operation †  
  
  
† Starts a long-running operation |    
**Other permissions:**

  * aiplatform.datasets.get (to call GET on the long-running operation returned)
  * aiplatform.datasets.update (to call DELETE on the long-running operation returned)
  * aiplatform.datasets.get (to call WAIT on the long-running operation returned)
  * aiplatform.datasets.update (to call CANCEL on the long-running operation returned)

  
N/A  |  †  
  
  
† Starts a long-running operation |   
  
## What's next

  * For information about Agent Platform predefined, basic and custom roles, as well as general information about service accounts and agents, see [Access control](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control).
  * For detailed information about controlling permissions with a custom service account, see [Using a custom service account](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/custom-service-account).
  * Learn more about using IAM to access resources in the [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) topic of the IAM documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
