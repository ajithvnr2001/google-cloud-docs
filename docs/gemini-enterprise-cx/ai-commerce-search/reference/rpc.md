---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/
title: AI Commerce Search API \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:37:59.494490+00:00
---

# AI Commerce Search API  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  AI Commerce Search API Stay organized with collections  Save and categorize content based on your preferences. 

The AI Commerce Search API is made up of Retail Search, Browse and Recommendations. These discovery AI solutions help you implement personalized search, browse and recommendations, based on machine learning models, across your websites and mobile applications.

## Service: retail.googleapis.com

The Service name `retail.googleapis.com` is needed to create RPC client stubs.

## `[google.cloud.location.Locations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.location#google.cloud.location.Locations)`

Methods  
---  
  
## `[google.cloud.retail.v2.AnalyticsService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AnalyticsService)`

Methods  
---  
``[ExportAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AnalyticsService.ExportAnalyticsMetrics)`` |  Exports analytics metrics.  
  
## `[google.cloud.retail.v2.CatalogService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService)`

Methods  
---  
``[AddCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.AddCatalogAttribute)`` |  Adds the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogAttribute)` to the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AttributesConfig)`.  
``[GetAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.GetAttributesConfig)`` |  Gets an `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AttributesConfig)`.  
``[GetCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.GetCompletionConfig)`` |  Gets a `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CompletionConfig)`.  
``[GetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.GetDefaultBranch)`` |  Get which branch is currently default branch set by `[CatalogService.SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.SetDefaultBranch)` method under a specified parent catalog.  
``[ListCatalogs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.ListCatalogs)`` |  Lists all the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Catalog)`s associated with the project.  
``[RemoveCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.RemoveCatalogAttribute)`` |  Removes the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogAttribute)` from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AttributesConfig)`.  
``[ReplaceCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.ReplaceCatalogAttribute)`` |  Replaces the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogAttribute)` in the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AttributesConfig)` by updating the catalog attribute with the same `[CatalogAttribute.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogAttribute.FIELDS.string.google.cloud.retail.v2.CatalogAttribute.key)`.  
``[SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.SetDefaultBranch)`` |  Set a specified branch id as default branch.  
``[UpdateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.UpdateAttributesConfig)`` |  Updates the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AttributesConfig)`.  
``[UpdateCatalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.UpdateCatalog)`` |  Updates the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Catalog)`s.  
``[UpdateCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CatalogService.UpdateCompletionConfig)`` |  Updates the `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CompletionConfig)`s.  
  
## `[google.cloud.retail.v2.CompletionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CompletionService)`

Methods  
---  
``[CompleteQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CompletionService.CompleteQuery)`` |  Completes the specified prefix with keyword suggestions.  
``[ImportCompletionData](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CompletionService.ImportCompletionData)`` |  Bulk import of processed completion dataset.  
  
## `[google.cloud.retail.v2.ControlService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ControlService)`

Methods  
---  
``[CreateControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ControlService.CreateControl)`` |  Creates a Control.  
``[DeleteControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ControlService.DeleteControl)`` |  Deletes a Control.  
``[GetControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ControlService.GetControl)`` |  Gets a Control.  
``[ListControls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ControlService.ListControls)`` |  Lists all Controls by their parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Catalog)`.  
``[UpdateControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ControlService.UpdateControl)`` |  Updates a Control.  
  
## `[google.cloud.retail.v2.ConversationalSearchService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ConversationalSearchService)`

Methods  
---  
``[ConversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ConversationalSearchService.ConversationalSearch)`` |  Performs a conversational search.  
  
## `[google.cloud.retail.v2.GenerativeQuestionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.GenerativeQuestionService)`

Methods  
---  
``[BatchUpdateGenerativeQuestionConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.GenerativeQuestionService.BatchUpdateGenerativeQuestionConfigs)`` |  Allows management of multiple questions.  
``[GetConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.GenerativeQuestionService.GetConversationalSearchCustomizationConfig)`` |  Returns the conversational search customization config for a given catalog.  
``[GetGenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.GenerativeQuestionService.GetGenerativeQuestionsFeatureConfig)`` |  Manages overal generative question feature state -- enables toggling feature on and off.  
``[ListGenerativeQuestionConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.GenerativeQuestionService.ListGenerativeQuestionConfigs)`` |  Returns all questions for a given catalog.  
``[UpdateConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.GenerativeQuestionService.UpdateConversationalSearchCustomizationConfig)`` |  Updates the conversational search customization config for a given catalog.  
``[UpdateGenerativeQuestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.GenerativeQuestionService.UpdateGenerativeQuestionConfig)`` |  Allows management of individual questions.  
``[UpdateGenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.GenerativeQuestionService.UpdateGenerativeQuestionsFeatureConfig)`` |  Manages overal generative question feature state -- enables toggling feature on and off.  
  
## `[google.cloud.retail.v2.ModelService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService)`

Methods  
---  
``[CreateModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService.CreateModel)`` |  Creates a new model.  
``[DeleteModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService.DeleteModel)`` |  Deletes an existing model.  
``[GetModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService.GetModel)`` |  Gets a model.  
``[ListModels](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService.ListModels)`` |  Lists all the models linked to this event store.  
``[PauseModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService.PauseModel)`` |  Pauses the training of an existing model.  
``[ResumeModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService.ResumeModel)`` |  Resumes the training of an existing model.  
``[TuneModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService.TuneModel)`` |  Tunes an existing model.  
``[UpdateModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ModelService.UpdateModel)`` |  Update of model metadata.  
  
## `[google.cloud.retail.v2.PredictionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.PredictionService)`

Methods  
---  
``[Predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.PredictionService.Predict)`` |  Makes a recommendation prediction.  
  
## `[google.cloud.retail.v2.ProductService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService)`

Methods  
---  
``[AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.AddFulfillmentPlaces)`` |  We recommend that you use the `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.AddLocalInventories)` method instead of the `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.AddFulfillmentPlaces)` method.  
``[AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.AddLocalInventories)`` |  Updates local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)` at a list of places, while respecting the last update timestamps of each inventory field.  
``[CreateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.CreateProduct)`` |  Creates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)`.  
``[DeleteProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.DeleteProduct)`` |  Deletes a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)`.  
``[GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.GetProduct)`` |  Gets a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)`.  
``[ImportProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.ImportProducts)`` |  Bulk import of multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)`s.  
``[ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.ListProducts)`` |  Gets a list of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)`s.  
``[PurgeProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.PurgeProducts)`` |  Permanently deletes all selected `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)`s under a branch.  
``[RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.RemoveFulfillmentPlaces)`` |  We recommend that you use the `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.RemoveLocalInventories)` method instead of the `[ProductService.RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.RemoveFulfillmentPlaces)` method.  
``[RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.RemoveLocalInventories)`` |  Remove local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)` at a list of places at a removal timestamp.  
``[SetInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.SetInventory)`` |  Updates inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)` while respecting the last update timestamps of each inventory field.  
``[UpdateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ProductService.UpdateProduct)`` |  Updates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.Product)`.  
  
## `[google.cloud.retail.v2.SearchService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.SearchService)`

Methods  
---  
``[Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.SearchService.Search)`` |  Performs a search.  
  
## `[google.cloud.retail.v2.ServingConfigService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ServingConfigService)`

Methods  
---  
``[AddControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ServingConfigService.AddControl)`` |  Enables a Control on the specified ServingConfig.  
``[CreateServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ServingConfigService.CreateServingConfig)`` |  Creates a ServingConfig.  
``[DeleteServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ServingConfigService.DeleteServingConfig)`` |  Deletes a ServingConfig.  
``[GetServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ServingConfigService.GetServingConfig)`` |  Gets a ServingConfig.  
``[ListServingConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ServingConfigService.ListServingConfigs)`` |  Lists all ServingConfigs linked to this catalog.  
``[RemoveControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ServingConfigService.RemoveControl)`` |  Disables a Control on the specified ServingConfig.  
``[UpdateServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ServingConfigService.UpdateServingConfig)`` |  Updates a ServingConfig.  
  
## `[google.cloud.retail.v2.UserEventService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UserEventService)`

Methods  
---  
``[CollectUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UserEventService.CollectUserEvent)`` |  Writes a single user event from the browser.  
``[ImportUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UserEventService.ImportUserEvents)`` |  Bulk import of User events.  
``[PurgeUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UserEventService.PurgeUserEvents)`` |  Deletes permanently all user events specified by the filter provided.  
``[RejoinUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UserEventService.RejoinUserEvents)`` |  Starts a user-event rejoin operation with latest product catalog.  
``[WriteUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UserEventService.WriteUserEvent)`` |  Writes a single user event.  
  
## `[google.cloud.retail.v2alpha.AnalyticsService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AnalyticsService)`

Methods  
---  
``[ExportAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AnalyticsService.ExportAnalyticsMetrics)`` |  Exports analytics metrics.  
  
## `[google.cloud.retail.v2alpha.BranchService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.BranchService)`

Methods  
---  
``[GetBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.BranchService.GetBranch)`` |  Retrieves a `[Branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Branch)`.  
``[ListBranches](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.BranchService.ListBranches)`` |  Lists all instances of `[Branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Branch)` under the specified parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Catalog)`.  
  
## `[google.cloud.retail.v2alpha.CatalogService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService)`

Methods  
---  
``[AddCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.AddCatalogAttribute)`` |  Adds the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogAttribute)` to the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AttributesConfig)`.  
``[BatchRemoveCatalogAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.BatchRemoveCatalogAttributes)`` |  Removes all specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogAttribute)`s from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AttributesConfig)`.  
``[GetAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.GetAttributesConfig)`` |  Gets an `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AttributesConfig)`.  
``[GetCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.GetCompletionConfig)`` |  Gets a `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CompletionConfig)`.  
``[GetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.GetDefaultBranch)`` |  Get which branch is currently default branch set by `[CatalogService.SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.SetDefaultBranch)` method under a specified parent catalog.  
``[ListCatalogs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.ListCatalogs)`` |  Lists all the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Catalog)`s associated with the project.  
``[RemoveCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.RemoveCatalogAttribute)`` |  Removes the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogAttribute)` from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AttributesConfig)`.  
``[ReplaceCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.ReplaceCatalogAttribute)`` |  Replaces the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogAttribute)` in the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AttributesConfig)` by updating the catalog attribute with the same `[CatalogAttribute.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogAttribute.FIELDS.string.google.cloud.retail.v2alpha.CatalogAttribute.key)`.  
``[SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.SetDefaultBranch)`` |  Set a specified branch id as default branch.  
``[UpdateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.UpdateAttributesConfig)`` |  Updates the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AttributesConfig)`.  
``[UpdateCatalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.UpdateCatalog)`` |  Updates the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Catalog)`s.  
``[UpdateCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.UpdateCompletionConfig)`` |  Updates the `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CompletionConfig)`s.  
  
## `[google.cloud.retail.v2alpha.CompletionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CompletionService)`

Methods  
---  
``[CompleteQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CompletionService.CompleteQuery)`` |  Completes the specified prefix with keyword suggestions.  
``[ImportCompletionData](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CompletionService.ImportCompletionData)`` |  Bulk import of processed completion dataset.  
  
## `[google.cloud.retail.v2alpha.ControlService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ControlService)`

Methods  
---  
``[CreateControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ControlService.CreateControl)`` |  Creates a Control.  
``[DeleteControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ControlService.DeleteControl)`` |  Deletes a Control.  
``[GetControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ControlService.GetControl)`` |  Gets a Control.  
``[ListControls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ControlService.ListControls)`` |  Lists all Controls by their parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Catalog)`.  
``[UpdateControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ControlService.UpdateControl)`` |  Updates a Control.  
  
## `[google.cloud.retail.v2alpha.ConversationalSearchService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ConversationalSearchService)`

Methods  
---  
``[ConversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ConversationalSearchService.ConversationalSearch)`` |  Performs a conversational search.  
  
## `[google.cloud.retail.v2alpha.GenerativeQuestionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.GenerativeQuestionService)`

Methods  
---  
``[BatchUpdateGenerativeQuestionConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.GenerativeQuestionService.BatchUpdateGenerativeQuestionConfigs)`` |  Allows management of multiple questions.  
``[GetConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.GenerativeQuestionService.GetConversationalSearchCustomizationConfig)`` |  Returns the conversational search customization config for a given catalog.  
``[GetGenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.GenerativeQuestionService.GetGenerativeQuestionsFeatureConfig)`` |  Manages overal generative question feature state -- enables toggling feature on and off.  
``[ListGenerativeQuestionConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.GenerativeQuestionService.ListGenerativeQuestionConfigs)`` |  Returns all questions for a given catalog.  
``[UpdateConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.GenerativeQuestionService.UpdateConversationalSearchCustomizationConfig)`` |  Updates the conversational search customization config for a given catalog.  
``[UpdateGenerativeQuestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.GenerativeQuestionService.UpdateGenerativeQuestionConfig)`` |  Allows management of individual questions.  
``[UpdateGenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.GenerativeQuestionService.UpdateGenerativeQuestionsFeatureConfig)`` |  Manages overal generative question feature state -- enables toggling feature on and off.  
  
## `[google.cloud.retail.v2alpha.MerchantCenterAccountLinkService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.MerchantCenterAccountLinkService)`

Methods  
---  
``[CreateMerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.MerchantCenterAccountLinkService.CreateMerchantCenterAccountLink)`` |  Creates a `[MerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.MerchantCenterAccountLink)`.  
``[DeleteMerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.MerchantCenterAccountLinkService.DeleteMerchantCenterAccountLink)`` |  Deletes a `[MerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.MerchantCenterAccountLink)`.  
``[ListMerchantCenterAccountLinks](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.MerchantCenterAccountLinkService.ListMerchantCenterAccountLinks)`` |  Lists all `[MerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.MerchantCenterAccountLink)`s under the specified parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Catalog)`.  
  
## `[google.cloud.retail.v2alpha.MetricService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.MetricService)`

Methods  
---  
  
## `[google.cloud.retail.v2alpha.ModelService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService)`

Methods  
---  
``[CreateModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.CreateModel)`` |  Creates a new model.  
``[DeleteModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.DeleteModel)`` |  Deletes an existing model.  
``[GetModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.GetModel)`` |  Gets a model.  
``[ListModels](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.ListModels)`` |  Lists all the models linked to this event store.  
``[PauseModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.PauseModel)`` |  Pauses the training of an existing model.  
``[ResumeModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.ResumeModel)`` |  Resumes the training of an existing model.  
``[TuneModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.TuneModel)`` |  Tunes an existing model.  
``[UpdateModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.UpdateModel)`` |  Update of model metadata.  
  
## `[google.cloud.retail.v2alpha.PredictionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.PredictionService)`

Methods  
---  
``[Predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.PredictionService.Predict)`` |  Makes a recommendation prediction.  
  
## `[google.cloud.retail.v2alpha.ProductService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService)`

Methods  
---  
``[AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlaces)`` |  We recommend that you use the `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.AddLocalInventories)` method instead of the `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlaces)` method.  
``[AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.AddLocalInventories)`` |  Updates local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)` at a list of places, while respecting the last update timestamps of each inventory field.  
``[CreateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.CreateProduct)`` |  Creates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)`.  
``[DeleteProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.DeleteProduct)`` |  Deletes a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)`.  
``[ExportProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.ExportProducts)`` |  Exports multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)`s.  
``[GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.GetProduct)`` |  Gets a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)`.  
``[ImportProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.ImportProducts)`` |  Bulk import of multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)`s.  
``[ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.ListProducts)`` |  Gets a list of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)`s.  
``[PurgeProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.PurgeProducts)`` |  Permanently deletes all selected `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)`s under a branch.  
``[RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlaces)`` |  We recommend that you use the `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories)` method instead of the `[ProductService.RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlaces)` method.  
``[RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories)`` |  Remove local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)` at a list of places at a removal timestamp.  
``[SetInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.SetInventory)`` |  Updates inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)` while respecting the last update timestamps of each inventory field.  
``[UpdateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.UpdateProduct)`` |  Updates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.Product)`.  
  
## `[google.cloud.retail.v2alpha.ProjectService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService)`

Methods  
---  
``[AcceptTerms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService.AcceptTerms)`` |  Accepts service terms for this project.  
``[EnrollSolution](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService.EnrollSolution)`` |  The method enrolls a solution of type `[Retail Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.SolutionType.ENUM_VALUES.google.cloud.retail.v2alpha.SolutionType.SOLUTION_TYPE_SEARCH)` into a project.  
``[GetAlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService.GetAlertConfig)`` |  Get the `[AlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.AlertConfig)` of the requested project.  
``[GetLoggingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService.GetLoggingConfig)`` |  Gets the `[LoggingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.LoggingConfig)` of the requested project.  
``[GetProject](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService.GetProject)`` |  Gets the project.  
``[ListEnrolledSolutions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService.ListEnrolledSolutions)`` |  Lists all the AI Commerce Search API solutions the project has enrolled.  
``[UpdateAlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService.UpdateAlertConfig)`` |  Update the alert config of the requested project.  
``[UpdateLoggingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProjectService.UpdateLoggingConfig)`` |  Updates the `[LoggingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.LoggingConfig)` of the requested project.  
  
## `[google.cloud.retail.v2alpha.SearchService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.SearchService)`

Methods  
---  
``[Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.SearchService.Search)`` |  Performs a search.  
  
## `[google.cloud.retail.v2alpha.ServingConfigService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ServingConfigService)`

Methods  
---  
``[AddControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ServingConfigService.AddControl)`` |  Enables a Control on the specified ServingConfig.  
``[CreateServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ServingConfigService.CreateServingConfig)`` |  Creates a ServingConfig.  
``[DeleteServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ServingConfigService.DeleteServingConfig)`` |  Deletes a ServingConfig.  
``[GetServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ServingConfigService.GetServingConfig)`` |  Gets a ServingConfig.  
``[ListServingConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ServingConfigService.ListServingConfigs)`` |  Lists all ServingConfigs linked to this catalog.  
``[RemoveControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ServingConfigService.RemoveControl)`` |  Disables a Control on the specified ServingConfig.  
``[UpdateServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ServingConfigService.UpdateServingConfig)`` |  Updates a ServingConfig.  
  
## `[google.cloud.retail.v2alpha.UserEventService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService)`

Methods  
---  
``[CollectUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.CollectUserEvent)`` |  Writes a single user event from the browser.  
``[ExportUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.ExportUserEvents)`` |  Exports user events.  
``[ImportUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.ImportUserEvents)`` |  Bulk import of User events.  
``[PurgeUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.PurgeUserEvents)`` |  Deletes permanently all user events specified by the filter provided.  
``[RejoinUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.RejoinUserEvents)`` |  Starts a user-event rejoin operation with latest product catalog.  
``[WriteUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.WriteUserEvent)`` |  Writes a single user event.  
  
## `[google.cloud.retail.v2beta.AnalyticsService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AnalyticsService)`

Methods  
---  
``[ExportAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AnalyticsService.ExportAnalyticsMetrics)`` |  Exports analytics metrics.  
  
## `[google.cloud.retail.v2beta.CatalogService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService)`

Methods  
---  
``[AddCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.AddCatalogAttribute)`` |  Adds the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogAttribute)` to the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AttributesConfig)`.  
``[BatchRemoveCatalogAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.BatchRemoveCatalogAttributes)`` |  Removes all specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogAttribute)`s from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AttributesConfig)`.  
``[GetAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.GetAttributesConfig)`` |  Gets an `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AttributesConfig)`.  
``[GetCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.GetCompletionConfig)`` |  Gets a `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CompletionConfig)`.  
``[GetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.GetDefaultBranch)`` |  Get which branch is currently default branch set by `[CatalogService.SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.SetDefaultBranch)` method under a specified parent catalog.  
``[ListCatalogs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.ListCatalogs)`` |  Lists all the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Catalog)`s associated with the project.  
``[RemoveCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.RemoveCatalogAttribute)`` |  Removes the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogAttribute)` from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AttributesConfig)`.  
``[ReplaceCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.ReplaceCatalogAttribute)`` |  Replaces the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogAttribute)` in the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AttributesConfig)` by updating the catalog attribute with the same `[CatalogAttribute.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogAttribute.FIELDS.string.google.cloud.retail.v2beta.CatalogAttribute.key)`.  
``[SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.SetDefaultBranch)`` |  Set a specified branch id as default branch.  
``[UpdateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.UpdateAttributesConfig)`` |  Updates the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AttributesConfig)`.  
``[UpdateCatalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.UpdateCatalog)`` |  Updates the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Catalog)`s.  
``[UpdateCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CatalogService.UpdateCompletionConfig)`` |  Updates the `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CompletionConfig)`s.  
  
## `[google.cloud.retail.v2beta.CompletionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CompletionService)`

Methods  
---  
``[CompleteQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CompletionService.CompleteQuery)`` |  Completes the specified prefix with keyword suggestions.  
``[ImportCompletionData](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.CompletionService.ImportCompletionData)`` |  Bulk import of processed completion dataset.  
  
## `[google.cloud.retail.v2beta.ControlService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ControlService)`

Methods  
---  
``[CreateControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ControlService.CreateControl)`` |  Creates a Control.  
``[DeleteControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ControlService.DeleteControl)`` |  Deletes a Control.  
``[GetControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ControlService.GetControl)`` |  Gets a Control.  
``[ListControls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ControlService.ListControls)`` |  Lists all Controls by their parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Catalog)`.  
``[UpdateControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ControlService.UpdateControl)`` |  Updates a Control.  
  
## `[google.cloud.retail.v2beta.ConversationalSearchService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ConversationalSearchService)`

Methods  
---  
``[ConversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ConversationalSearchService.ConversationalSearch)`` |  Performs a conversational search.  
  
## `[google.cloud.retail.v2beta.GenerativeQuestionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.GenerativeQuestionService)`

Methods  
---  
``[BatchUpdateGenerativeQuestionConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.GenerativeQuestionService.BatchUpdateGenerativeQuestionConfigs)`` |  Allows management of multiple questions.  
``[GetConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.GenerativeQuestionService.GetConversationalSearchCustomizationConfig)`` |  Returns the conversational search customization config for a given catalog.  
``[GetGenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.GenerativeQuestionService.GetGenerativeQuestionsFeatureConfig)`` |  Manages overal generative question feature state -- enables toggling feature on and off.  
``[ListGenerativeQuestionConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.GenerativeQuestionService.ListGenerativeQuestionConfigs)`` |  Returns all questions for a given catalog.  
``[UpdateConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.GenerativeQuestionService.UpdateConversationalSearchCustomizationConfig)`` |  Updates the conversational search customization config for a given catalog.  
``[UpdateGenerativeQuestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.GenerativeQuestionService.UpdateGenerativeQuestionConfig)`` |  Allows management of individual questions.  
``[UpdateGenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.GenerativeQuestionService.UpdateGenerativeQuestionsFeatureConfig)`` |  Manages overal generative question feature state -- enables toggling feature on and off.  
  
## `[google.cloud.retail.v2beta.ModelService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService)`

Methods  
---  
``[CreateModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService.CreateModel)`` |  Creates a new model.  
``[DeleteModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService.DeleteModel)`` |  Deletes an existing model.  
``[GetModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService.GetModel)`` |  Gets a model.  
``[ListModels](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService.ListModels)`` |  Lists all the models linked to this event store.  
``[PauseModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService.PauseModel)`` |  Pauses the training of an existing model.  
``[ResumeModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService.ResumeModel)`` |  Resumes the training of an existing model.  
``[TuneModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService.TuneModel)`` |  Tunes an existing model.  
``[UpdateModel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ModelService.UpdateModel)`` |  Update of model metadata.  
  
## `[google.cloud.retail.v2beta.PredictionService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.PredictionService)`

Methods  
---  
``[Predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.PredictionService.Predict)`` |  Makes a recommendation prediction.  
  
## `[google.cloud.retail.v2beta.ProductService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService)`

Methods  
---  
``[AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.AddFulfillmentPlaces)`` |  We recommend that you use the `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.AddLocalInventories)` method instead of the `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.AddFulfillmentPlaces)` method.  
``[AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.AddLocalInventories)`` |  Updates local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)` at a list of places, while respecting the last update timestamps of each inventory field.  
``[CreateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.CreateProduct)`` |  Creates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)`.  
``[DeleteProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.DeleteProduct)`` |  Deletes a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)`.  
``[ExportProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.ExportProducts)`` |  Exports multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)`s.  
``[GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.GetProduct)`` |  Gets a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)`.  
``[ImportProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.ImportProducts)`` |  Bulk import of multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)`s.  
``[ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.ListProducts)`` |  Gets a list of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)`s.  
``[PurgeProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.PurgeProducts)`` |  Permanently deletes all selected `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)`s under a branch.  
``[RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.RemoveFulfillmentPlaces)`` |  We recommend that you use the `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.RemoveLocalInventories)` method instead of the `[ProductService.RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.RemoveFulfillmentPlaces)` method.  
``[RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.RemoveLocalInventories)`` |  Remove local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)` at a list of places at a removal timestamp.  
``[SetInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.SetInventory)`` |  Updates inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)` while respecting the last update timestamps of each inventory field.  
``[UpdateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProductService.UpdateProduct)`` |  Updates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.Product)`.  
  
## `[google.cloud.retail.v2beta.ProjectService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProjectService)`

Methods  
---  
``[GetAlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProjectService.GetAlertConfig)`` |  Get the `[AlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.AlertConfig)` of the requested project.  
``[UpdateAlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ProjectService.UpdateAlertConfig)`` |  Update the alert config of the requested project.  
  
## `[google.cloud.retail.v2beta.SearchService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.SearchService)`

Methods  
---  
``[Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.SearchService.Search)`` |  Performs a search.  
  
## `[google.cloud.retail.v2beta.ServingConfigService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ServingConfigService)`

Methods  
---  
``[AddControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ServingConfigService.AddControl)`` |  Enables a Control on the specified ServingConfig.  
``[CreateServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ServingConfigService.CreateServingConfig)`` |  Creates a ServingConfig.  
``[DeleteServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ServingConfigService.DeleteServingConfig)`` |  Deletes a ServingConfig.  
``[GetServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ServingConfigService.GetServingConfig)`` |  Gets a ServingConfig.  
``[ListServingConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ServingConfigService.ListServingConfigs)`` |  Lists all ServingConfigs linked to this catalog.  
``[RemoveControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ServingConfigService.RemoveControl)`` |  Disables a Control on the specified ServingConfig.  
``[UpdateServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.ServingConfigService.UpdateServingConfig)`` |  Updates a ServingConfig.  
  
## `[google.cloud.retail.v2beta.UserEventService](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.UserEventService)`

Methods  
---  
``[CollectUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.UserEventService.CollectUserEvent)`` |  Writes a single user event from the browser.  
``[ExportUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.UserEventService.ExportUserEvents)`` |  Exports user events.  
``[ImportUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.UserEventService.ImportUserEvents)`` |  Bulk import of User events.  
``[PurgeUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.UserEventService.PurgeUserEvents)`` |  Deletes permanently all user events specified by the filter provided.  
``[RejoinUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.UserEventService.RejoinUserEvents)`` |  Starts a user-event rejoin operation with latest product catalog.  
``[WriteUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2beta#google.cloud.retail.v2beta.UserEventService.WriteUserEvent)`` |  Writes a single user event.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[GetOperation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
``[ListOperations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`` |  Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
