---
url: https://docs.cloud.google.com/vision-ai/docs/reference/rpc/
title: Vision AI API \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:18.624399+00:00
---

# Vision AI API  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/rpc/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback 

#  Vision AI API Stay organized with collections  Save and categorize content based on your preferences. 

## Service: visionai.googleapis.com

The Service name `visionai.googleapis.com` is needed to create RPC client stubs.

## `[google.cloud.location.Locations](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.location#google.cloud.location.Locations)`

Methods  
---  
``[GetLocation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.location#google.cloud.location.Locations.GetLocation)`` |  Gets information about a location.  
``[ListLocations](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.location#google.cloud.location.Locations.ListLocations)`` |  Lists information about the supported locations for this service.  
  
## `[google.cloud.visionai.v1.AppPlatform](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform)`

Methods  
---  
``[AddApplicationStreamInput](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.AddApplicationStreamInput)`` |  Adds target stream input to the Application.  
``[CreateApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.CreateApplication)`` |  Creates a new Application in a given project and location.  
``[CreateApplicationInstances](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.CreateApplicationInstances)`` |  Adds target stream input to the Application.  
``[CreateDraft](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.CreateDraft)`` |  Creates a new Draft in a given project and location.  
``[CreateProcessor](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.CreateProcessor)`` |  Creates a new Processor in a given project and location.  
``[DeleteApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.DeleteApplication)`` |  Deletes a single Application.  
``[DeleteApplicationInstances](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.DeleteApplicationInstances)`` |  Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted.  
``[DeleteDraft](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.DeleteDraft)`` |  Deletes a single Draft.  
``[DeleteProcessor](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.DeleteProcessor)`` |  Deletes a single Processor.  
``[DeployApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.DeployApplication)`` |  Deploys a single Application.  
``[GetApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.GetApplication)`` |  Gets details of a single Application.  
``[GetDraft](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.GetDraft)`` |  Gets details of a single Draft.  
``[GetInstance](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.GetInstance)`` |  Gets details of a single Instance.  
``[GetProcessor](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.GetProcessor)`` |  Gets details of a single Processor.  
``[ListApplications](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.ListApplications)`` |  Lists Applications in a given project and location.  
``[ListDrafts](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.ListDrafts)`` |  Lists Drafts in a given project and location.  
``[ListInstances](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.ListInstances)`` |  Lists Instances in a given project and location.  
``[ListPrebuiltProcessors](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.ListPrebuiltProcessors)`` |  ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.  
``[ListProcessors](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.ListProcessors)`` |  Lists Processors in a given project and location.  
``[RemoveApplicationStreamInput](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.RemoveApplicationStreamInput)`` |  Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted.  
``[UndeployApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.UndeployApplication)`` |  Undeploys a single Application.  
``[UpdateApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.UpdateApplication)`` |  Updates the parameters of a single Application.  
``[UpdateApplicationInstances](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.UpdateApplicationInstances)`` |  Adds target stream input to the Application.  
``[UpdateApplicationStreamInput](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.UpdateApplicationStreamInput)`` |  Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed.  
``[UpdateDraft](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.UpdateDraft)`` |  Updates the parameters of a single Draft.  
``[UpdateProcessor](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.AppPlatform.UpdateProcessor)`` |  Updates the parameters of a single Processor.  
  
## `[google.cloud.visionai.v1.EventDiscoveryService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.EventDiscoveryService)`

Methods  
---  
``[WatchEvents](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.EventDiscoveryService.WatchEvents)`` |  Watch for event updates happening on the given streams.  
  
## `[google.cloud.visionai.v1.LiveVideoAnalytics](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics)`

Methods  
---  
``[CreateAnalysis](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.CreateAnalysis)`` |  Creates a new Analysis in a given project and location.  
``[CreateProcess](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.CreateProcess)`` |  Creates a new Process in a given project and location.  
``[DeleteAnalysis](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.DeleteAnalysis)`` |  Deletes a single Analysis.  
``[DeleteProcess](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.DeleteProcess)`` |  Deletes a single Process.  
``[GetAnalysis](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.GetAnalysis)`` |  Gets details of a single Analysis.  
``[GetProcess](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.GetProcess)`` |  Gets details of a single Process.  
``[ListAnalyses](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.ListAnalyses)`` |  Lists Analyses in a given project and location.  
``[ListProcesses](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.ListProcesses)`` |  Lists Processes in a given project and location.  
``[UpdateAnalysis](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.UpdateAnalysis)`` |  Updates the parameters of a single Analysis.  
``[UpdateProcess](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.LiveVideoAnalytics.UpdateProcess)`` |  Updates the parameters of a single Process.  
  
## `[google.cloud.visionai.v1.RetailService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.RetailService)`

Methods  
---  
  
## `[google.cloud.visionai.v1.SmartDeviceService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.SmartDeviceService)`

Methods  
---  
  
## `[google.cloud.visionai.v1.StreamingService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.StreamingService)`

Methods  
---  
  
## `[google.cloud.visionai.v1.StreamsService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.StreamsService)`

Methods  
---  
  
## `[google.cloud.visionai.v1.Warehouse](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse)`

Methods  
---  
``[AddCollectionItem](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.AddCollectionItem)`` |  Adds an item into a Collection.  
``[AnalyzeAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.AnalyzeAsset)`` |  Analyze asset to power search capability.  
``[AnalyzeCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.AnalyzeCorpus)`` |  Analyzes a corpus.  
``[ClipAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ClipAsset)`` |  Generates clips for downloading.  
``[CreateAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateAnnotation)`` |  Creates annotation inside asset.  
``[CreateAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateAsset)`` |  Creates an asset inside corpus.  
``[CreateCollection](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateCollection)`` |  Creates a collection.  
``[CreateCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateCorpus)`` |  Creates a corpus inside a project.  
``[CreateDataSchema](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateDataSchema)`` |  Creates data schema inside corpus.  
``[CreateIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateIndex)`` |  Creates an Index under the corpus.  
``[CreateIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateIndexEndpoint)`` |  Creates an IndexEndpoint.  
``[CreateSearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateSearchConfig)`` |  Creates a search configuration inside a corpus.  
``[CreateSearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.CreateSearchHypernym)`` |  Creates a SearchHypernym inside a corpus.  
``[DeleteAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteAnnotation)`` |  Deletes annotation inside asset.  
``[DeleteAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteAsset)`` |  Deletes asset inside corpus.  
``[DeleteCollection](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteCollection)`` |  Deletes a collection.  
``[DeleteCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteCorpus)`` |  Deletes a corpus only if its empty.  
``[DeleteDataSchema](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteDataSchema)`` |  Deletes data schema inside corpus.  
``[DeleteIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteIndex)`` |  Delete a single Index.  
``[DeleteIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteIndexEndpoint)`` |  Deletes an IndexEndpoint.  
``[DeleteSearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteSearchConfig)`` |  Deletes a search configuration inside a corpus.  
``[DeleteSearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeleteSearchHypernym)`` |  Deletes a SearchHypernym inside a corpus.  
``[DeployIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.DeployIndex)`` |  Deploys an Index to IndexEndpoint.  
``[GenerateHlsUri](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GenerateHlsUri)`` |  Generates a uri for an HLS manifest.  
``[GenerateRetrievalUrl](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GenerateRetrievalUrl)`` |  Generates a signed url for downloading the asset.  
``[GetAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetAnnotation)`` |  Reads annotation inside asset.  
``[GetAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetAsset)`` |  Reads an asset inside corpus.  
``[GetCollection](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetCollection)`` |  Gets a collection.  
``[GetCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetCorpus)`` |  Gets corpus details inside a project.  
``[GetDataSchema](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetDataSchema)`` |  Gets data schema inside corpus.  
``[GetIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetIndex)`` |  Gets the details of a single Index under a Corpus.  
``[GetIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetIndexEndpoint)`` |  Gets an IndexEndpoint.  
``[GetSearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetSearchConfig)`` |  Gets a search configuration inside a corpus.  
``[GetSearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.GetSearchHypernym)`` |  Gets a SearchHypernym inside a corpus.  
``[ImportAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ImportAssets)`` |  Imports assets (images plus annotations) from a meta file on cloud storage.  
``[IndexAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.IndexAsset)`` |  Index one asset for search.  
``[IngestAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.IngestAsset)`` |  Ingests data for the asset.  
``[ListAnnotations](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListAnnotations)`` |  Lists a list of annotations inside asset.  
``[ListAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListAssets)`` |  Lists an list of assets inside corpus.  
``[ListCollections](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListCollections)`` |  Lists collections inside a corpus.  
``[ListCorpora](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListCorpora)`` |  Lists all corpora in a project.  
``[ListDataSchemas](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListDataSchemas)`` |  Lists a list of data schemas inside corpus.  
``[ListIndexEndpoints](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListIndexEndpoints)`` |  Lists all IndexEndpoints in a project.  
``[ListIndexes](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListIndexes)`` |  List all Indexes in a given Corpus.  
``[ListSearchConfigs](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListSearchConfigs)`` |  Lists all search configurations inside a corpus.  
``[ListSearchHypernyms](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ListSearchHypernyms)`` |  Lists SearchHypernyms inside a corpus.  
``[RemoveCollectionItem](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.RemoveCollectionItem)`` |  Removes an item from a collection.  
``[RemoveIndexAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.RemoveIndexAsset)`` |  Remove one asset's index data for search.  
``[SearchAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.SearchAssets)`` |  Search media asset.  
``[SearchIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.SearchIndexEndpoint)`` |  Search a deployed index endpoint (IMAGE corpus type only).  
``[UndeployIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UndeployIndex)`` |  Undeploys an Index from IndexEndpoint.  
``[UpdateAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateAnnotation)`` |  Updates annotation inside asset.  
``[UpdateAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateAsset)`` |  Updates an asset inside corpus.  
``[UpdateCollection](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateCollection)`` |  Updates a collection.  
``[UpdateCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateCorpus)`` |  Updates a corpus in a project.  
``[UpdateDataSchema](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateDataSchema)`` |  Updates data schema inside corpus.  
``[UpdateIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateIndex)`` |  Updates an Index under the corpus.  
``[UpdateIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateIndexEndpoint)`` |  Updates an IndexEndpoint.  
``[UpdateSearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateSearchConfig)`` |  Updates a search configuration inside a corpus.  
``[UpdateSearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UpdateSearchHypernym)`` |  Updates a SearchHypernym inside a corpus.  
``[UploadAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.UploadAsset)`` |  Upload asset by specifing the asset Cloud Storage uri.  
``[ViewCollectionItems](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ViewCollectionItems)`` |  View items inside a collection.  
``[ViewIndexedAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#google.cloud.visionai.v1.Warehouse.ViewIndexedAssets)`` |  Lists a list of assets inside an index.  
  
## `[google.cloud.visionai.v1alpha1.AppPlatform](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform)`

Methods  
---  
``[AddApplicationStreamInput](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.AddApplicationStreamInput)`` |  Adds target stream input to the Application.  
``[CreateApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.CreateApplication)`` |  Creates a new Application in a given project and location.  
``[CreateApplicationInstances](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.CreateApplicationInstances)`` |  Adds target stream input to the Application.  
``[CreateDraft](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.CreateDraft)`` |  Creates a new Draft in a given project and location.  
``[CreateProcessor](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.CreateProcessor)`` |  Creates a new Processor in a given project and location.  
``[DeleteApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.DeleteApplication)`` |  Deletes a single Application.  
``[DeleteApplicationInstances](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.DeleteApplicationInstances)`` |  Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted.  
``[DeleteDraft](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.DeleteDraft)`` |  Deletes a single Draft.  
``[DeleteProcessor](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.DeleteProcessor)`` |  Deletes a single Processor.  
``[DeployApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.DeployApplication)`` |  Deploys a single Application.  
``[GetApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.GetApplication)`` |  Gets details of a single Application.  
``[GetDraft](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.GetDraft)`` |  Gets details of a single Draft.  
``[GetInstance](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.GetInstance)`` |  Gets details of a single Instance.  
``[GetProcessor](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.GetProcessor)`` |  Gets details of a single Processor.  
``[ListApplications](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.ListApplications)`` |  Lists Applications in a given project and location.  
``[ListDrafts](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.ListDrafts)`` |  Lists Drafts in a given project and location.  
``[ListInstances](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.ListInstances)`` |  Lists Instances in a given project and location.  
``[ListPrebuiltProcessors](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.ListPrebuiltProcessors)`` |  ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.  
``[ListProcessors](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.ListProcessors)`` |  Lists Processors in a given project and location.  
``[RemoveApplicationStreamInput](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.RemoveApplicationStreamInput)`` |  Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted.  
``[UndeployApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.UndeployApplication)`` |  Undeploys a single Application.  
``[UpdateApplication](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.UpdateApplication)`` |  Updates the parameters of a single Application.  
``[UpdateApplicationInstances](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.UpdateApplicationInstances)`` |  Adds target stream input to the Application.  
``[UpdateApplicationStreamInput](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.UpdateApplicationStreamInput)`` |  Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed.  
``[UpdateDraft](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.UpdateDraft)`` |  Updates the parameters of a single Draft.  
``[UpdateProcessor](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.AppPlatform.UpdateProcessor)`` |  Updates the parameters of a single Processor.  
  
## `[google.cloud.visionai.v1alpha1.EventDiscoveryService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.EventDiscoveryService)`

Methods  
---  
``[WatchEvents](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.EventDiscoveryService.WatchEvents)`` |  Watch for event updates happening on the given streams.  
  
## `[google.cloud.visionai.v1alpha1.LiveVideoAnalytics](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics)`

Methods  
---  
``[CreateAnalysis](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.CreateAnalysis)`` |  Creates a new Analysis in a given project and location.  
``[CreateProcess](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.CreateProcess)`` |  Creates a new Process in a given project and location.  
``[DeleteAnalysis](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.DeleteAnalysis)`` |  Deletes a single Analysis.  
``[DeleteProcess](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.DeleteProcess)`` |  Deletes a single Process.  
``[GetAnalysis](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.GetAnalysis)`` |  Gets details of a single Analysis.  
``[GetProcess](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.GetProcess)`` |  Gets details of a single Process.  
``[ListAnalyses](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.ListAnalyses)`` |  Lists Analyses in a given project and location.  
``[ListProcesses](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.ListProcesses)`` |  Lists Processes in a given project and location.  
``[UpdateAnalysis](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.UpdateAnalysis)`` |  Updates the parameters of a single Analysis.  
``[UpdateProcess](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.LiveVideoAnalytics.UpdateProcess)`` |  Updates the parameters of a single Process.  
  
## `[google.cloud.visionai.v1alpha1.RetailService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.RetailService)`

Methods  
---  
  
## `[google.cloud.visionai.v1alpha1.SmartDeviceService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.SmartDeviceService)`

Methods  
---  
  
## `[google.cloud.visionai.v1alpha1.StreamingService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.StreamingService)`

Methods  
---  
  
## `[google.cloud.visionai.v1alpha1.StreamsService](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.StreamsService)`

Methods  
---  
  
## `[google.cloud.visionai.v1alpha1.Warehouse](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse)`

Methods  
---  
``[AddCollectionItem](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.AddCollectionItem)`` |  Adds an item into a Collection.  
``[AnalyzeAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.AnalyzeAsset)`` |  Analyze asset to power search capability.  
``[AnalyzeCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.AnalyzeCorpus)`` |  Analyzes a corpus.  
``[ClipAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ClipAsset)`` |  Generates clips for downloading.  
``[CreateAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateAnnotation)`` |  Creates annotation inside asset.  
``[CreateAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateAsset)`` |  Creates an asset inside corpus.  
``[CreateCollection](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateCollection)`` |  Creates a collection.  
``[CreateCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateCorpus)`` |  Creates a corpus inside a project.  
``[CreateDataSchema](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateDataSchema)`` |  Creates data schema inside corpus.  
``[CreateIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateIndex)`` |  Creates an Index under the corpus.  
``[CreateIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateIndexEndpoint)`` |  Creates an IndexEndpoint.  
``[CreateSearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateSearchConfig)`` |  Creates a search configuration inside a corpus.  
``[CreateSearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.CreateSearchHypernym)`` |  Creates a SearchHypernym inside a corpus.  
``[DeleteAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteAnnotation)`` |  Deletes annotation inside asset.  
``[DeleteAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteAsset)`` |  Deletes asset inside corpus.  
``[DeleteCollection](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteCollection)`` |  Deletes a collection.  
``[DeleteCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteCorpus)`` |  Deletes a corpus only if its empty.  
``[DeleteDataSchema](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteDataSchema)`` |  Deletes data schema inside corpus.  
``[DeleteIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteIndex)`` |  Delete a single Index.  
``[DeleteIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteIndexEndpoint)`` |  Deletes an IndexEndpoint.  
``[DeleteSearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteSearchConfig)`` |  Deletes a search configuration inside a corpus.  
``[DeleteSearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeleteSearchHypernym)`` |  Deletes a SearchHypernym inside a corpus.  
``[DeployIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.DeployIndex)`` |  Deploys an Index to IndexEndpoint.  
``[GenerateHlsUri](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GenerateHlsUri)`` |  Generates a uri for an HLS manifest.  
``[GenerateRetrievalUrl](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GenerateRetrievalUrl)`` |  Generates a signed url for downloading the asset.  
``[GetAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetAnnotation)`` |  Reads annotation inside asset.  
``[GetAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetAsset)`` |  Reads an asset inside corpus.  
``[GetCollection](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetCollection)`` |  Gets a collection.  
``[GetCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetCorpus)`` |  Gets corpus details inside a project.  
``[GetDataSchema](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetDataSchema)`` |  Gets data schema inside corpus.  
``[GetIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetIndex)`` |  Gets the details of a single Index under a Corpus.  
``[GetIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetIndexEndpoint)`` |  Gets an IndexEndpoint.  
``[GetSearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetSearchConfig)`` |  Gets a search configuration inside a corpus.  
``[GetSearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.GetSearchHypernym)`` |  Gets a SearchHypernym inside a corpus.  
``[ImportAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ImportAssets)`` |  Imports assets (images plus annotations) from a meta file on cloud storage.  
``[IndexAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.IndexAsset)`` |  Index one asset for search.  
``[IngestAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.IngestAsset)`` |  Ingests data for the asset.  
``[ListAnnotations](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListAnnotations)`` |  Lists a list of annotations inside asset.  
``[ListAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListAssets)`` |  Lists an list of assets inside corpus.  
``[ListCollections](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListCollections)`` |  Lists collections inside a corpus.  
``[ListCorpora](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListCorpora)`` |  Lists all corpora in a project.  
``[ListDataSchemas](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListDataSchemas)`` |  Lists a list of data schemas inside corpus.  
``[ListIndexEndpoints](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListIndexEndpoints)`` |  Lists all IndexEndpoints in a project.  
``[ListIndexes](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListIndexes)`` |  List all Indexes in a given Corpus.  
``[ListSearchConfigs](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListSearchConfigs)`` |  Lists all search configurations inside a corpus.  
``[ListSearchHypernyms](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ListSearchHypernyms)`` |  Lists SearchHypernyms inside a corpus.  
``[RemoveCollectionItem](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.RemoveCollectionItem)`` |  Removes an item from a collection.  
``[RemoveIndexAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.RemoveIndexAsset)`` |  Remove one asset's index data for search.  
``[SearchAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.SearchAssets)`` |  Search media asset.  
``[SearchIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.SearchIndexEndpoint)`` |  Search a deployed index endpoint (IMAGE corpus type only).  
``[UndeployIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UndeployIndex)`` |  Undeploys an Index from IndexEndpoint.  
``[UpdateAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateAnnotation)`` |  Updates annotation inside asset.  
``[UpdateAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateAsset)`` |  Updates an asset inside corpus.  
``[UpdateCollection](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateCollection)`` |  Updates a collection.  
``[UpdateCorpus](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateCorpus)`` |  Updates a corpus in a project.  
``[UpdateDataSchema](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateDataSchema)`` |  Updates data schema inside corpus.  
``[UpdateIndex](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateIndex)`` |  Updates an Index under the corpus.  
``[UpdateIndexEndpoint](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateIndexEndpoint)`` |  Updates an IndexEndpoint.  
``[UpdateSearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateSearchConfig)`` |  Updates a search configuration inside a corpus.  
``[UpdateSearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UpdateSearchHypernym)`` |  Updates a SearchHypernym inside a corpus.  
``[UploadAsset](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.UploadAsset)`` |  Upload asset by specifing the asset Cloud Storage uri.  
``[ViewCollectionItems](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ViewCollectionItems)`` |  View items inside a collection.  
``[ViewIndexedAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1alpha1#google.cloud.visionai.v1alpha1.Warehouse.ViewIndexedAssets)`` |  Lists a list of assets inside an index.  
  
## `[google.iam.v1.IAMPolicy](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy)`

Methods  
---  
``[GetIamPolicy](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy.GetIamPolicy)`` |  Gets the access control policy for a resource.  
``[SetIamPolicy](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy.SetIamPolicy)`` |  Sets the access control policy on the specified resource.  
``[TestIamPermissions](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy.TestIamPermissions)`` |  Returns permissions that a caller has on the specified resource.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[CancelOperation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)`` |  Starts asynchronous cancellation on a long-running operation.  
``[DeleteOperation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.longrunning#google.longrunning.Operations.DeleteOperation)`` |  Deletes a long-running operation.  
``[GetOperation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
``[ListOperations](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`` |  Lists operations that match the specified filter in the request.  
``[WaitOperation](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.longrunning#google.longrunning.Operations.WaitOperation)`` |  Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
