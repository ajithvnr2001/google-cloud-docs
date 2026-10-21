---
url: https://docs.cloud.google.com/food-ai/reference/rpc/
title: Food Ordering AI Agent API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:06:27.403324+00:00
---

# Food Ordering AI Agent API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Food Ordering AI Agent API Stay organized with collections  Save and categorize content based on your preferences. 

foodorderingaiagent.googleapis.com API.

## Service: foodorderingaiagent.googleapis.com

The Service name `foodorderingaiagent.googleapis.com` is needed to create RPC client stubs.

## `[google.cloud.foodorderingaiagent.v1.EvaluationRunService](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService)`

Methods  
---  
``[RunEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService.RunEvaluationCase)`` |  Runs an evaluation case.  
``[RunEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService.RunEvaluationDataset)`` |  Runs an evaluation dataset.  
  
## `[google.cloud.foodorderingaiagent.v1.FoodOrderingService](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FoodOrderingService)`

Methods  
---  
``[BidiProcessOrder](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FoodOrderingService.BidiProcessOrder)`` |  A bidirectional streaming API that processes continuous client inputs across multiple modalities (e.g., text, audio) and generates real-time multimodal output streams.  
``[ProcessOrder](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FoodOrderingService.ProcessOrder)`` |  Performs a single turn logic to process user input and return the result.  
  
## `[google.cloud.foodorderingaiagent.v1.MenuService](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService)`

Methods  
---  
``[AppendIngestionPhase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.AppendIngestionPhase)`` |  Appends an ingestion phase to an ingestion log.  
``[BatchCreateEvaluationCases](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchCreateEvaluationCases)`` |  Batch creates EvaluationCases.  
``[BatchDeleteStores](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchDeleteStores)`` |  Batch deletes stores.  
``[BatchGetMenuEntities](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchGetMenuEntities)`` |  Batch gets entities for a menu.  
``[BatchUpdateEvaluationCases](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchUpdateEvaluationCases)`` |  Batch updates EvaluationCases.  
``[BatchUpdateStores](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchUpdateStores)`` |  Batch updates stores.  
``[ComputeAnalyticsMetrics](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ComputeAnalyticsMetrics)`` |  Computes analytics metrics for a given brand for specified time period with optional store filter.  
``[CreateBrand](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateBrand)`` |  Creates a brand.  
``[CreateChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateChannelConfig)`` |  Creates a ChannelConfig.  
``[CreateConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateConfigApplicationRule)`` |  Creates a ConfigApplicationRule.  
``[CreateDiscount](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateDiscount)`` |  Creates a discount.  
``[CreateEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateEvaluationCase)`` |  Creates an EvaluationCase.  
``[CreateEvaluationContext](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateEvaluationContext)`` |  Creates an EvaluationContext.  
``[CreateEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateEvaluationDataset)`` |  Creates an EvaluationDataset.  
``[CreateEvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateEvaluationMatcher)`` |  Creates an EvaluationMatcher.  
``[CreateIngestionLog](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateIngestionLog)`` |  Creates an ingestion log.  
``[CreateInventory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateInventory)`` |  Creates an inventory.  
``[CreateMenu](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateMenu)`` |  Creates a menu.  
``[CreateStore](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateStore)`` |  Creates a store.  
``[DeleteBrand](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteBrand)`` |  Deletes the specified brand.  
``[DeleteBrandRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteBrandRevision)`` |  Deletes the specified BrandRevision.  
``[DeleteChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteChannelConfig)`` |  Deletes the specified ChannelConfig.  
``[DeleteChannelConfigRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteChannelConfigRevision)`` |  Deletes the specified ChannelConfigRevision.  
``[DeleteConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteConfigApplicationRule)`` |  Deletes the specified ConfigApplicationRule.  
``[DeleteConfigApplicationRuleRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteConfigApplicationRuleRevision)`` |  Deletes the specified ConfigApplicationRuleRevision.  
``[DeleteDiscount](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteDiscount)`` |  Deletes the specified discount.  
``[DeleteEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationCase)`` |  Deletes the specified EvaluationCase.  
``[DeleteEvaluationCaseResult](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationCaseResult)`` |  Deletes the specified EvaluationCaseResult.  
``[DeleteEvaluationContext](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationContext)`` |  Deletes the specified EvaluationContext.  
``[DeleteEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationDataset)`` |  Deletes the specified EvaluationDataset.  
``[DeleteEvaluationDatasetResult](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationDatasetResult)`` |  Deletes the specified EvaluationDatasetResult.  
``[DeleteEvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationMatcher)`` |  Deletes the specified EvaluationMatcher.  
``[DeleteIngestionLog](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteIngestionLog)`` |  Deletes the specified ingestion log.  
``[DeleteInventory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteInventory)`` |  Deletes the specified inventory.  
``[DeleteMenu](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteMenu)`` |  Deletes the specified menu.  
``[DeleteSessionRecord](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteSessionRecord)`` |  Deletes an SessionRecord.  
``[DeleteStore](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteStore)`` |  Deletes the specified store.  
``[DeleteStoreRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteStoreRevision)`` |  Deletes the specified StoreRevision.  
``[GetBrand](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetBrand)`` |  Gets a brand.  
``[GetBrandRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetBrandRevision)`` |  Gets a BrandRevision.  
``[GetChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetChannelConfig)`` |  Gets a ChannelConfig.  
``[GetChannelConfigRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetChannelConfigRevision)`` |  Gets a ChannelConfigRevision.  
``[GetConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetConfigApplicationRule)`` |  Gets a ConfigApplicationRule.  
``[GetConfigApplicationRuleRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetConfigApplicationRuleRevision)`` |  Gets a ConfigApplicationRuleRevision.  
``[GetDiscount](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetDiscount)`` |  Gets a discount.  
``[GetEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationCase)`` |  Gets an EvaluationCase.  
``[GetEvaluationCaseResult](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationCaseResult)`` |  Gets an EvaluationCaseResult.  
``[GetEvaluationContext](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationContext)`` |  Gets an EvaluationContext.  
``[GetEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationDataset)`` |  Gets an EvaluationDataset.  
``[GetEvaluationDatasetResult](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationDatasetResult)`` |  Gets an EvaluationDatasetResult.  
``[GetEvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationMatcher)`` |  Gets an EvaluationMatcher.  
``[GetIngestionLog](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetIngestionLog)`` |  Gets an ingestion log.  
``[GetInventory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetInventory)`` |  Gets an inventory.  
``[GetMenu](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetMenu)`` |  Gets a menu.  
``[GetSessionRecord](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetSessionRecord)`` |  Gets a specific SessionRecord.  
``[GetStore](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetStore)`` |  Gets a store.  
``[GetStoreRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetStoreRevision)`` |  Gets a StoreRevision.  
``[ListBrandHistory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrandHistory)`` |  Lists history entries for a brand.  
``[ListBrandRevisions](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrandRevisions)`` |  Lists BrandRevisions.  
``[ListBrands](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrands)`` |  Lists brands.  
``[ListChannelConfigRevisions](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListChannelConfigRevisions)`` |  Lists ChannelConfigRevisions.  
``[ListChannelConfigs](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListChannelConfigs)`` |  Lists ChannelConfigs.  
``[ListConfigApplicationRuleRevisions](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListConfigApplicationRuleRevisions)`` |  Lists ConfigApplicationRuleRevisions.  
``[ListConfigApplicationRules](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListConfigApplicationRules)`` |  Lists ConfigApplicationRules.  
``[ListDiscounts](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListDiscounts)`` |  Lists discounts.  
``[ListEvaluationCaseResults](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationCaseResults)`` |  Lists EvaluationCaseResults.  
``[ListEvaluationCases](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationCases)`` |  Lists EvaluationCases.  
``[ListEvaluationContexts](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationContexts)`` |  Lists EvaluationContexts.  
``[ListEvaluationDatasetResults](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationDatasetResults)`` |  Lists EvaluationDatasetResults.  
``[ListEvaluationDatasets](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationDatasets)`` |  Lists EvaluationDatasets.  
``[ListEvaluationMatchers](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationMatchers)`` |  Lists EvaluationMatchers.  
``[ListIngestionLogs](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListIngestionLogs)`` |  Lists ingestion logs.  
``[ListInventories](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListInventories)`` |  Lists inventories.  
``[ListMenus](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListMenus)`` |  Lists menus.  
``[ListSessionRecords](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListSessionRecords)`` |  Lists SessionRecords for a given brand.  
``[ListStoreRevisions](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListStoreRevisions)`` |  Lists StoreRevisions.  
``[ListStores](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListStores)`` |  Lists stores.  
``[PromoteChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.PromoteChannelConfig)`` |  Promotes the specified channel config.  
``[UpdateBrand](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateBrand)`` |  Updates the specified brand.  
``[UpdateChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateChannelConfig)`` |  Updates the specified ChannelConfig.  
``[UpdateConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateConfigApplicationRule)`` |  Updates the specified ConfigApplicationRule.  
``[UpdateDiscount](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateDiscount)`` |  Updates the specified discount.  
``[UpdateEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationCase)`` |  Updates the specified EvaluationCase.  
``[UpdateEvaluationContext](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationContext)`` |  Updates the specified EvaluationContext.  
``[UpdateEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationDataset)`` |  Updates the specified EvaluationDataset.  
``[UpdateEvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationMatcher)`` |  Updates the specified EvaluationMatcher.  
``[UpdateInventory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateInventory)`` |  Updates the specified inventory.  
``[UpdateStore](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateStore)`` |  Update the specified store.  
  
## `[google.cloud.foodorderingaiagent.v1beta.EvaluationRunService](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.EvaluationRunService)`

Methods  
---  
``[RunEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.EvaluationRunService.RunEvaluationCase)`` |  Runs an evaluation case.  
``[RunEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.EvaluationRunService.RunEvaluationDataset)`` |  Runs an evaluation dataset.  
  
## `[google.cloud.foodorderingaiagent.v1beta.FoodOrderingService](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.FoodOrderingService)`

Methods  
---  
``[BidiProcessOrder](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.FoodOrderingService.BidiProcessOrder)`` |  A bidirectional streaming API that processes continuous client inputs across multiple modalities (e.g., text, audio) and generates real-time multimodal output streams.  
``[ProcessOrder](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.FoodOrderingService.ProcessOrder)`` |  Performs a single turn logic to process user input and return the result.  
  
## `[google.cloud.foodorderingaiagent.v1beta.MenuService](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService)`

Methods  
---  
``[AppendIngestionPhase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.AppendIngestionPhase)`` |  Appends an ingestion phase to an ingestion log.  
``[BatchCreateEvaluationCases](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.BatchCreateEvaluationCases)`` |  Batch creates EvaluationCases.  
``[BatchDeleteStores](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.BatchDeleteStores)`` |  Batch deletes stores.  
``[BatchGetMenuEntities](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.BatchGetMenuEntities)`` |  Batch gets entities for a menu.  
``[BatchUpdateEvaluationCases](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.BatchUpdateEvaluationCases)`` |  Batch updates EvaluationCases.  
``[BatchUpdateStores](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.BatchUpdateStores)`` |  Batch updates stores.  
``[ComputeAnalyticsMetrics](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ComputeAnalyticsMetrics)`` |  Computes analytics metrics for a given brand for specified time period with optional store filter.  
``[CreateBrand](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateBrand)`` |  Creates a brand.  
``[CreateChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateChannelConfig)`` |  Creates a ChannelConfig.  
``[CreateConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateConfigApplicationRule)`` |  Creates a ConfigApplicationRule.  
``[CreateDiscount](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateDiscount)`` |  Creates a discount.  
``[CreateEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateEvaluationCase)`` |  Creates an EvaluationCase.  
``[CreateEvaluationContext](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateEvaluationContext)`` |  Creates an EvaluationContext.  
``[CreateEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateEvaluationDataset)`` |  Creates an EvaluationDataset.  
``[CreateEvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateEvaluationMatcher)`` |  Creates an EvaluationMatcher.  
``[CreateIngestionLog](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateIngestionLog)`` |  Creates an ingestion log.  
``[CreateInventory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateInventory)`` |  Creates an inventory.  
``[CreateMenu](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateMenu)`` |  Creates a menu.  
``[CreateStore](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.CreateStore)`` |  Creates a store.  
``[DeleteBrand](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteBrand)`` |  Deletes the specified brand.  
``[DeleteBrandRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteBrandRevision)`` |  Deletes the specified BrandRevision.  
``[DeleteChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteChannelConfig)`` |  Deletes the specified ChannelConfig.  
``[DeleteChannelConfigRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteChannelConfigRevision)`` |  Deletes the specified ChannelConfigRevision.  
``[DeleteConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteConfigApplicationRule)`` |  Deletes the specified ConfigApplicationRule.  
``[DeleteConfigApplicationRuleRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteConfigApplicationRuleRevision)`` |  Deletes the specified ConfigApplicationRuleRevision.  
``[DeleteDiscount](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteDiscount)`` |  Deletes the specified discount.  
``[DeleteEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteEvaluationCase)`` |  Deletes the specified EvaluationCase.  
``[DeleteEvaluationCaseResult](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteEvaluationCaseResult)`` |  Deletes the specified EvaluationCaseResult.  
``[DeleteEvaluationContext](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteEvaluationContext)`` |  Deletes the specified EvaluationContext.  
``[DeleteEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteEvaluationDataset)`` |  Deletes the specified EvaluationDataset.  
``[DeleteEvaluationDatasetResult](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteEvaluationDatasetResult)`` |  Deletes the specified EvaluationDatasetResult.  
``[DeleteEvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteEvaluationMatcher)`` |  Deletes the specified EvaluationMatcher.  
``[DeleteIngestionLog](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteIngestionLog)`` |  Deletes the specified ingestion log.  
``[DeleteInventory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteInventory)`` |  Deletes the specified inventory.  
``[DeleteMenu](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteMenu)`` |  Deletes the specified menu.  
``[DeleteSessionRecord](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteSessionRecord)`` |  Deletes an SessionRecord.  
``[DeleteStore](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteStore)`` |  Deletes the specified store.  
``[DeleteStoreRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.DeleteStoreRevision)`` |  Deletes the specified StoreRevision.  
``[GetBrand](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetBrand)`` |  Gets a brand.  
``[GetBrandRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetBrandRevision)`` |  Gets a BrandRevision.  
``[GetChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetChannelConfig)`` |  Gets a ChannelConfig.  
``[GetChannelConfigRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetChannelConfigRevision)`` |  Gets a ChannelConfigRevision.  
``[GetConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetConfigApplicationRule)`` |  Gets a ConfigApplicationRule.  
``[GetConfigApplicationRuleRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetConfigApplicationRuleRevision)`` |  Gets a ConfigApplicationRuleRevision.  
``[GetDiscount](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetDiscount)`` |  Gets a discount.  
``[GetEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetEvaluationCase)`` |  Gets an EvaluationCase.  
``[GetEvaluationCaseResult](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetEvaluationCaseResult)`` |  Gets an EvaluationCaseResult.  
``[GetEvaluationContext](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetEvaluationContext)`` |  Gets an EvaluationContext.  
``[GetEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetEvaluationDataset)`` |  Gets an EvaluationDataset.  
``[GetEvaluationDatasetResult](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetEvaluationDatasetResult)`` |  Gets an EvaluationDatasetResult.  
``[GetEvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetEvaluationMatcher)`` |  Gets an EvaluationMatcher.  
``[GetIngestionLog](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetIngestionLog)`` |  Gets an ingestion log.  
``[GetInventory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetInventory)`` |  Gets an inventory.  
``[GetMenu](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetMenu)`` |  Gets a menu.  
``[GetSessionRecord](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetSessionRecord)`` |  Gets a specific SessionRecord.  
``[GetStore](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetStore)`` |  Gets a store.  
``[GetStoreRevision](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.GetStoreRevision)`` |  Gets a StoreRevision.  
``[ListBrandHistory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListBrandHistory)`` |  Lists history entries for a brand.  
``[ListBrandRevisions](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListBrandRevisions)`` |  Lists BrandRevisions.  
``[ListBrands](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListBrands)`` |  Lists brands.  
``[ListChannelConfigRevisions](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListChannelConfigRevisions)`` |  Lists ChannelConfigRevisions.  
``[ListChannelConfigs](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListChannelConfigs)`` |  Lists ChannelConfigs.  
``[ListConfigApplicationRuleRevisions](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListConfigApplicationRuleRevisions)`` |  Lists ConfigApplicationRuleRevisions.  
``[ListConfigApplicationRules](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListConfigApplicationRules)`` |  Lists ConfigApplicationRules.  
``[ListDiscounts](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListDiscounts)`` |  Lists discounts.  
``[ListEvaluationCaseResults](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListEvaluationCaseResults)`` |  Lists EvaluationCaseResults.  
``[ListEvaluationCases](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListEvaluationCases)`` |  Lists EvaluationCases.  
``[ListEvaluationContexts](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListEvaluationContexts)`` |  Lists EvaluationContexts.  
``[ListEvaluationDatasetResults](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListEvaluationDatasetResults)`` |  Lists EvaluationDatasetResults.  
``[ListEvaluationDatasets](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListEvaluationDatasets)`` |  Lists EvaluationDatasets.  
``[ListEvaluationMatchers](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListEvaluationMatchers)`` |  Lists EvaluationMatchers.  
``[ListIngestionLogs](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListIngestionLogs)`` |  Lists ingestion logs.  
``[ListInventories](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListInventories)`` |  Lists inventories.  
``[ListMenus](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListMenus)`` |  Lists menus.  
``[ListSessionRecords](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListSessionRecords)`` |  Lists SessionRecords for a given brand.  
``[ListStoreRevisions](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListStoreRevisions)`` |  Lists StoreRevisions.  
``[ListStores](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.ListStores)`` |  Lists stores.  
``[PromoteChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.PromoteChannelConfig)`` |  Promotes the specified channel config.  
``[UpdateBrand](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateBrand)`` |  Updates the specified brand.  
``[UpdateChannelConfig](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateChannelConfig)`` |  Updates the specified ChannelConfig.  
``[UpdateConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateConfigApplicationRule)`` |  Updates the specified ConfigApplicationRule.  
``[UpdateDiscount](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateDiscount)`` |  Updates the specified discount.  
``[UpdateEvaluationCase](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateEvaluationCase)`` |  Updates the specified EvaluationCase.  
``[UpdateEvaluationContext](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateEvaluationContext)`` |  Updates the specified EvaluationContext.  
``[UpdateEvaluationDataset](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateEvaluationDataset)`` |  Updates the specified EvaluationDataset.  
``[UpdateEvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateEvaluationMatcher)`` |  Updates the specified EvaluationMatcher.  
``[UpdateInventory](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateInventory)`` |  Updates the specified inventory.  
``[UpdateStore](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.MenuService.UpdateStore)`` |  Update the specified store.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/food-ai/reference/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[CancelOperation](https://docs.cloud.google.com/food-ai/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)`` |  Starts asynchronous cancellation on a long-running operation.  
``[DeleteOperation](https://docs.cloud.google.com/food-ai/reference/rpc/google.longrunning#google.longrunning.Operations.DeleteOperation)`` |  Deletes a long-running operation.  
``[GetOperation](https://docs.cloud.google.com/food-ai/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
``[ListOperations](https://docs.cloud.google.com/food-ai/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`` |  Lists operations that match the specified filter in the request.  
``[WaitOperation](https://docs.cloud.google.com/food-ai/reference/rpc/google.longrunning#google.longrunning.Operations.WaitOperation)`` |  Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
