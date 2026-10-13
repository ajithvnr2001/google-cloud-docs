---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/
title: AI Commerce Search API \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:08.031229+00:00
---

# AI Commerce Search API  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  AI Commerce Search API Stay organized with collections  Save and categorize content based on your preferences. 

The AI Commerce Search API is made up of Retail Search, Browse and Recommendations. These discovery AI solutions help you implement personalized search, browse and recommendations, based on machine learning models, across your websites and mobile applications.

  * REST Resource: v2beta.projects
  * REST Resource: v2beta.projects.locations.catalogs
  * REST Resource: v2beta.projects.locations.catalogs.attributesConfig
  * REST Resource: v2beta.projects.locations.catalogs.branches.operations
  * REST Resource: v2beta.projects.locations.catalogs.branches.products
  * REST Resource: v2beta.projects.locations.catalogs.completionData
  * REST Resource: v2beta.projects.locations.catalogs.controls
  * REST Resource: v2beta.projects.locations.catalogs.generativeQuestion
  * REST Resource: v2beta.projects.locations.catalogs.generativeQuestions
  * REST Resource: v2beta.projects.locations.catalogs.models
  * REST Resource: v2beta.projects.locations.catalogs.operations
  * REST Resource: v2beta.projects.locations.catalogs.placements
  * REST Resource: v2beta.projects.locations.catalogs.servingConfigs
  * REST Resource: v2beta.projects.locations.catalogs.userEvents
  * REST Resource: v2beta.projects.locations.operations
  * REST Resource: v2beta.projects.operations
  * REST Resource: v2alpha.projects
  * REST Resource: v2alpha.projects.locations.catalogs
  * REST Resource: v2alpha.projects.locations.catalogs.attributesConfig
  * REST Resource: v2alpha.projects.locations.catalogs.branches
  * REST Resource: v2alpha.projects.locations.catalogs.branches.operations
  * REST Resource: v2alpha.projects.locations.catalogs.branches.places.operations
  * REST Resource: v2alpha.projects.locations.catalogs.branches.products
  * REST Resource: v2alpha.projects.locations.catalogs.completionData
  * REST Resource: v2alpha.projects.locations.catalogs.controls
  * REST Resource: v2alpha.projects.locations.catalogs.generativeQuestion
  * REST Resource: v2alpha.projects.locations.catalogs.generativeQuestions
  * REST Resource: v2alpha.projects.locations.catalogs.merchantCenterAccountLinks
  * REST Resource: v2alpha.projects.locations.catalogs.models
  * REST Resource: v2alpha.projects.locations.catalogs.operations
  * REST Resource: v2alpha.projects.locations.catalogs.placements
  * REST Resource: v2alpha.projects.locations.catalogs.servingConfigs
  * REST Resource: v2alpha.projects.locations.catalogs.userEvents
  * REST Resource: v2alpha.projects.locations.operations
  * REST Resource: v2alpha.projects.operations
  * REST Resource: v2alpha.projects.retailProject
  * REST Resource: v2.projects.locations.catalogs
  * REST Resource: v2.projects.locations.catalogs.attributesConfig
  * REST Resource: v2.projects.locations.catalogs.branches.operations
  * REST Resource: v2.projects.locations.catalogs.branches.products
  * REST Resource: v2.projects.locations.catalogs.completionData
  * REST Resource: v2.projects.locations.catalogs.controls
  * REST Resource: v2.projects.locations.catalogs.generativeQuestion
  * REST Resource: v2.projects.locations.catalogs.generativeQuestions
  * REST Resource: v2.projects.locations.catalogs.models
  * REST Resource: v2.projects.locations.catalogs.operations
  * REST Resource: v2.projects.locations.catalogs.placements
  * REST Resource: v2.projects.locations.catalogs.servingConfigs
  * REST Resource: v2.projects.locations.catalogs.userEvents
  * REST Resource: v2.projects.locations.operations
  * REST Resource: v2.projects.operations



## Service: retail.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://retail.googleapis.com/$discovery/rest?version=v2>
  * <https://retail.googleapis.com/$discovery/rest?version=v2beta>
  * <https://retail.googleapis.com/$discovery/rest?version=v2alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://retail.googleapis.com`



## REST Resource: [v2beta.projects](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects)

Methods  
---  
`[getAlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects/getAlertConfig)` |  `GET /v2beta/{name=projects/*/alertConfig}`   
Get the `[AlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig)` of the requested project.  
`[updateAlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects/updateAlertConfig)` |  `PATCH /v2beta/{alertConfig.name=projects/*/alertConfig}`   
Update the alert config of the requested project.  
  
## REST Resource: [v2beta.projects.locations.catalogs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs)

Methods  
---  
`[completeQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/completeQuery)` |  `GET /v2beta/{catalog=projects/*/locations/*/catalogs/*}:completeQuery`   
Completes the specified prefix with keyword suggestions.  
`[exportAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/exportAnalyticsMetrics)` |  `POST /v2beta/{catalog=projects/*/locations/*/catalogs/*}:exportAnalyticsMetrics`   
Exports analytics metrics.  
`[getAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getAttributesConfig)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*/attributesConfig}`   
Gets an `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[getCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getCompletionConfig)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*/completionConfig}`   
Gets a `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionConfig)`.  
`[getConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getConversationalSearchCustomizationConfig)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*}/conversationalSearchCustomizationConfig`   
Returns the conversational search customization config for a given catalog.  
`[getDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getDefaultBranch)` |  `GET /v2beta/{catalog=projects/*/locations/*/catalogs/*}:getDefaultBranch`   
Get which branch is currently default branch set by `[CatalogService.SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/setDefaultBranch#google.cloud.retail.v2beta.CatalogService.SetDefaultBranch)` method under a specified parent catalog.  
`[getGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getGenerativeQuestionFeature)` |  `GET /v2beta/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature`   
Manages overal generative question feature state -- enables toggling feature on and off.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/list)` |  `GET /v2beta/{parent=projects/*/locations/*}/catalogs`   
Lists all the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#Catalog)`s associated with the project.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/patch)` |  `PATCH /v2beta/{catalog.name=projects/*/locations/*/catalogs/*}`   
Updates the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#Catalog)`s.  
`[setDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/setDefaultBranch)` |  `POST /v2beta/{catalog=projects/*/locations/*/catalogs/*}:setDefaultBranch`   
Set a specified branch id as default branch.  
`[updateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateAttributesConfig)` |  `PATCH /v2beta/{attributesConfig.name=projects/*/locations/*/catalogs/*/attributesConfig}`   
Updates the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[updateCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateCompletionConfig)` |  `PATCH /v2beta/{completionConfig.name=projects/*/locations/*/catalogs/*/completionConfig}`   
Updates the `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionConfig)`s.  
`[updateConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateConversationalSearchCustomizationConfig)` |  `PATCH /v2beta/{conversationalSearchCustomizationConfig.catalog=projects/*/locations/*/catalogs/*}/conversationalSearchCustomizationConfig`   
Updates the conversational search customization config for a given catalog.  
`[updateGenerativeQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateGenerativeQuestion)` |  `PATCH /v2beta/{generativeQuestionConfig.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion`   
Allows management of individual questions.  
`[updateGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateGenerativeQuestionFeature)` |  `PATCH /v2beta/{generativeQuestionsFeatureConfig.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature`   
Manages overal generative question feature state -- enables toggling feature on and off.  
  
## REST Resource: [v2beta.projects.locations.catalogs.attributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig)

Methods  
---  
`[addCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/addCatalogAttribute)` |  `POST /v2beta/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:addCatalogAttribute`   
Adds the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` to the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[batchRemoveCatalogAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/batchRemoveCatalogAttributes)` |  `POST /v2beta/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:batchRemoveCatalogAttributes`   
Removes all specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)`s from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[removeCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/removeCatalogAttribute)` |  `POST /v2beta/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:removeCatalogAttribute`   
Removes the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[replaceCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/replaceCatalogAttribute)` |  `POST /v2beta/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:replaceCatalogAttribute`   
Replaces the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` in the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)` by updating the catalog attribute with the same `[CatalogAttribute.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.key)`.  
  
## REST Resource: [v2beta.projects.locations.catalogs.branches.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.operations/get)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*/branches/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v2beta.projects.locations.catalogs.branches.products](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products)

Methods  
---  
`[addFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addFulfillmentPlaces)` |  `POST /v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces`   
We recommend that you use the `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addLocalInventories#google.cloud.retail.v2beta.ProductService.AddLocalInventories)` method instead of the `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addFulfillmentPlaces#google.cloud.retail.v2beta.ProductService.AddFulfillmentPlaces)` method.  
`[addLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addLocalInventories)` |  `POST /v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories`   
Updates local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` at a list of places, while respecting the last update timestamps of each inventory field.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/create)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products`   
Creates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/delete)` |  `DELETE /v2beta/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Deletes a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`.  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/export)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:export`   
Exports multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/get)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Gets a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`.  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import`   
Bulk import of multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/list)` |  `GET /v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products`   
Gets a list of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/patch)` |  `PATCH /v2beta/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Updates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`.  
`[purge](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/purge)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge`   
Permanently deletes all selected `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s under a branch.  
`[removeFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/removeFulfillmentPlaces)` |  `POST /v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces`   
We recommend that you use the `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/removeLocalInventories#google.cloud.retail.v2beta.ProductService.RemoveLocalInventories)` method instead of the `[ProductService.RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/removeFulfillmentPlaces#google.cloud.retail.v2beta.ProductService.RemoveFulfillmentPlaces)` method.  
`[removeLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/removeLocalInventories)` |  `POST /v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories`   
Remove local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` at a list of places at a removal timestamp.  
`[setInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/setInventory)` |  `POST /v2beta/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory`   
Updates inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` while respecting the last update timestamps of each inventory field.  
  
## REST Resource: [v2beta.projects.locations.catalogs.completionData](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.completionData)

Methods  
---  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.completionData/import)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/completionData:import`   
Bulk import of processed completion dataset.  
  
## REST Resource: [v2beta.projects.locations.catalogs.controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/create)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/controls`   
Creates a Control.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/delete)` |  `DELETE /v2beta/{name=projects/*/locations/*/catalogs/*/controls/*}`   
Deletes a Control.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/get)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*/controls/*}`   
Gets a Control.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/list)` |  `GET /v2beta/{parent=projects/*/locations/*/catalogs/*}/controls`   
Lists all Controls by their parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#Catalog)`.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls/patch)` |  `PATCH /v2beta/{control.name=projects/*/locations/*/catalogs/*/controls/*}`   
Updates a Control.  
  
## REST Resource: [v2beta.projects.locations.catalogs.generativeQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.generativeQuestion)

Methods  
---  
`[batchUpdate](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.generativeQuestion/batchUpdate)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate`   
Allows management of multiple questions.  
  
## REST Resource: [v2beta.projects.locations.catalogs.generativeQuestions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.generativeQuestions)

Methods  
---  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.generativeQuestions/list)` |  `GET /v2beta/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions`   
Returns all questions for a given catalog.  
  
## REST Resource: [v2beta.projects.locations.catalogs.models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/create)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/models`   
Creates a new model.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/delete)` |  `DELETE /v2beta/{name=projects/*/locations/*/catalogs/*/models/*}`   
Deletes an existing model.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/get)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*/models/*}`   
Gets a model.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/list)` |  `GET /v2beta/{parent=projects/*/locations/*/catalogs/*}/models`   
Lists all the models linked to this event store.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/patch)` |  `PATCH /v2beta/{model.name=projects/*/locations/*/catalogs/*/models/*}`   
Update of model metadata.  
`[pause](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/pause)` |  `POST /v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:pause`   
Pauses the training of an existing model.  
`[resume](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/resume)` |  `POST /v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:resume`   
Resumes the training of an existing model.  
`[tune](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/tune)` |  `POST /v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:tune`   
Tunes an existing model.  
  
## REST Resource: [v2beta.projects.locations.catalogs.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.operations/get)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.operations/list)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2beta.projects.locations.catalogs.placements](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements)

Methods  
---  
`[conversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/conversationalSearch)` |  `POST /v2beta/{placement=projects/*/locations/*/catalogs/*/placements/*}:conversationalSearch`   
Performs a conversational search.  
`[predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/predict)` |  `POST /v2beta/{placement=projects/*/locations/*/catalogs/*/placements/*}:predict`   
Makes a recommendation prediction.  
`[search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/search)` |  `POST /v2beta/{placement=projects/*/locations/*/catalogs/*/placements/*}:search`   
Performs a search.  
  
## REST Resource: [v2beta.projects.locations.catalogs.servingConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs)

Methods  
---  
`[addControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl)` |  `POST /v2beta/{servingConfig=projects/*/locations/*/catalogs/*/servingConfigs/*}:addControl`   
Enables a Control on the specified ServingConfig.  
`[conversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/conversationalSearch)` |  `POST /v2beta/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:conversationalSearch`   
Performs a conversational search.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/create)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/servingConfigs`   
Creates a ServingConfig.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/delete)` |  `DELETE /v2beta/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Deletes a ServingConfig.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/get)` |  `GET /v2beta/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Gets a ServingConfig.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/list)` |  `GET /v2beta/{parent=projects/*/locations/*/catalogs/*}/servingConfigs`   
Lists all ServingConfigs linked to this catalog.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/patch)` |  `PATCH /v2beta/{servingConfig.name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Updates a ServingConfig.  
`[predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/predict)` |  `POST /v2beta/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:predict`   
Makes a recommendation prediction.  
`[removeControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/removeControl)` |  `POST /v2beta/{servingConfig=projects/*/locations/*/catalogs/*/servingConfigs/*}:removeControl`   
Disables a Control on the specified ServingConfig.  
`[search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/search)` |  `POST /v2beta/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:search`   
Performs a search.  
  
## REST Resource: [v2beta.projects.locations.catalogs.userEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents)

Methods  
---  
`[collect](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/collect)` |  `GET /v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect`   
Writes a single user event from the browser.  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/export)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:export`   
Exports user events.  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/import)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:import`   
Bulk import of User events.  
`[purge](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/purge)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge`   
Deletes permanently all user events specified by the filter provided.  
`[rejoin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/rejoin)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin`   
Starts a user-event rejoin operation with latest product catalog.  
`[write](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/write)` |  `POST /v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:write`   
Writes a single user event.  
  
## REST Resource: [v2beta.projects.locations.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.operations/get)` |  `GET /v2beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.operations/list)` |  `GET /v2beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2beta.projects.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.operations/get)` |  `GET /v2beta/{name=projects/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.operations/list)` |  `GET /v2beta/{name=projects/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2alpha.projects](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects)

Methods  
---  
`[enrollSolution](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects/enrollSolution)` |  `POST /v2alpha/{project=projects/*}:enrollSolution`   
The method enrolls a solution of type `[Retail Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)` into a project.  
`[getAlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects/getAlertConfig)` |  `GET /v2alpha/{name=projects/*/alertConfig}`   
Get the `[AlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/AlertConfig)` of the requested project.  
`[getLoggingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects/getLoggingConfig)` |  `GET /v2alpha/{name=projects/*/loggingConfig}`   
Gets the `[LoggingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig)` of the requested project.  
`[getRetailProject](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects/getRetailProject)` |  `GET /v2alpha/{name=projects/*/retailProject}`   
Gets the project.  
`[listEnrolledSolutions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects/listEnrolledSolutions)` |  `GET /v2alpha/{parent=projects/*}:enrolledSolutions`   
Lists all the AI Commerce Search API solutions the project has enrolled.  
`[updateAlertConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects/updateAlertConfig)` |  `PATCH /v2alpha/{alertConfig.name=projects/*/alertConfig}`   
Update the alert config of the requested project.  
`[updateLoggingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects/updateLoggingConfig)` |  `PATCH /v2alpha/{loggingConfig.name=projects/*/loggingConfig}`   
Updates the `[LoggingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/LoggingConfig)` of the requested project.  
  
## REST Resource: [v2alpha.projects.locations.catalogs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs)

Methods  
---  
`[completeQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/completeQuery)` |  `GET /v2alpha/{catalog=projects/*/locations/*/catalogs/*}:completeQuery`   
Completes the specified prefix with keyword suggestions.  
`[exportAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/exportAnalyticsMetrics)` |  `POST /v2alpha/{catalog=projects/*/locations/*/catalogs/*}:exportAnalyticsMetrics`   
Exports analytics metrics.  
`[getAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/getAttributesConfig)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/attributesConfig}`   
Gets an `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[getCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/getCompletionConfig)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/completionConfig}`   
Gets a `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/CompletionConfig)`.  
`[getConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/getConversationalSearchCustomizationConfig)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*}/conversationalSearchCustomizationConfig`   
Returns the conversational search customization config for a given catalog.  
`[getDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/getDefaultBranch)` |  `GET /v2alpha/{catalog=projects/*/locations/*/catalogs/*}:getDefaultBranch`   
Get which branch is currently default branch set by `[CatalogService.SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/setDefaultBranch#google.cloud.retail.v2alpha.CatalogService.SetDefaultBranch)` method under a specified parent catalog.  
`[getGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/getGenerativeQuestionFeature)` |  `GET /v2alpha/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature`   
Manages overal generative question feature state -- enables toggling feature on and off.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/list)` |  `GET /v2alpha/{parent=projects/*/locations/*}/catalogs`   
Lists all the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)`s associated with the project.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/patch)` |  `PATCH /v2alpha/{catalog.name=projects/*/locations/*/catalogs/*}`   
Updates the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)`s.  
`[setDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/setDefaultBranch)` |  `POST /v2alpha/{catalog=projects/*/locations/*/catalogs/*}:setDefaultBranch`   
Set a specified branch id as default branch.  
`[updateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/updateAttributesConfig)` |  `PATCH /v2alpha/{attributesConfig.name=projects/*/locations/*/catalogs/*/attributesConfig}`   
Updates the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[updateCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/updateCompletionConfig)` |  `PATCH /v2alpha/{completionConfig.name=projects/*/locations/*/catalogs/*/completionConfig}`   
Updates the `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/CompletionConfig)`s.  
`[updateConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/updateConversationalSearchCustomizationConfig)` |  `PATCH /v2alpha/{conversationalSearchCustomizationConfig.catalog=projects/*/locations/*/catalogs/*}/conversationalSearchCustomizationConfig`   
Updates the conversational search customization config for a given catalog.  
`[updateGenerativeQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/updateGenerativeQuestion)` |  `PATCH /v2alpha/{generativeQuestionConfig.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion`   
Allows management of individual questions.  
`[updateGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/updateGenerativeQuestionFeature)` |  `PATCH /v2alpha/{generativeQuestionsFeatureConfig.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature`   
Manages overal generative question feature state -- enables toggling feature on and off.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.attributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig)

Methods  
---  
`[addCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig/addCatalogAttribute)` |  `POST /v2alpha/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:addCatalogAttribute`   
Adds the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#CatalogAttribute)` to the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[batchRemoveCatalogAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig/batchRemoveCatalogAttributes)` |  `POST /v2alpha/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:batchRemoveCatalogAttributes`   
Removes all specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#CatalogAttribute)`s from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[removeCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig/removeCatalogAttribute)` |  `POST /v2alpha/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:removeCatalogAttribute`   
Removes the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#CatalogAttribute)` from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[replaceCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig/replaceCatalogAttribute)` |  `POST /v2alpha/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:replaceCatalogAttribute`   
Replaces the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#CatalogAttribute)` in the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig)` by updating the catalog attribute with the same `[CatalogAttribute.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.key)`.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.branches](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches/get)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*}`   
Retrieves a `[Branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#Branch)`.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches/list)` |  `GET /v2alpha/{parent=projects/*/locations/*/catalogs/*}/branches`   
Lists all instances of `[Branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#Branch)` under the specified parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)`.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.branches.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.operations/get)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.branches.places.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.places.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.places.operations/get)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/places/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.branches.products](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products)

Methods  
---  
`[addFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addFulfillmentPlaces)` |  `POST /v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces`   
We recommend that you use the `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addLocalInventories#google.cloud.retail.v2alpha.ProductService.AddLocalInventories)` method instead of the `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addFulfillmentPlaces#google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlaces)` method.  
`[addLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addLocalInventories)` |  `POST /v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories`   
Updates local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` at a list of places, while respecting the last update timestamps of each inventory field.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/create)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products`   
Creates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/delete)` |  `DELETE /v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Deletes a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/export)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:export`   
Exports multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Gets a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/import)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import`   
Bulk import of multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/list)` |  `GET /v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products`   
Gets a list of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/patch)` |  `PATCH /v2alpha/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Updates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.  
`[purge](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/purge)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge`   
Permanently deletes all selected `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s under a branch.  
`[removeFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeFulfillmentPlaces)` |  `POST /v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces`   
We recommend that you use the `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeLocalInventories#google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories)` method instead of the `[ProductService.RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeFulfillmentPlaces#google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlaces)` method.  
`[removeLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeLocalInventories)` |  `POST /v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories`   
Remove local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` at a list of places at a removal timestamp.  
`[setInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/setInventory)` |  `POST /v2alpha/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory`   
Updates inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` while respecting the last update timestamps of each inventory field.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.completionData](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.completionData)

Methods  
---  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.completionData/import)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/completionData:import`   
Bulk import of processed completion dataset.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/create)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/controls`   
Creates a Control.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/delete)` |  `DELETE /v2alpha/{name=projects/*/locations/*/catalogs/*/controls/*}`   
Deletes a Control.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/get)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/controls/*}`   
Gets a Control.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/list)` |  `GET /v2alpha/{parent=projects/*/locations/*/catalogs/*}/controls`   
Lists all Controls by their parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)`.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.controls/patch)` |  `PATCH /v2alpha/{control.name=projects/*/locations/*/catalogs/*/controls/*}`   
Updates a Control.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.generativeQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.generativeQuestion)

Methods  
---  
`[batchUpdate](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.generativeQuestion/batchUpdate)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate`   
Allows management of multiple questions.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.generativeQuestions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.generativeQuestions)

Methods  
---  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.generativeQuestions/list)` |  `GET /v2alpha/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions`   
Returns all questions for a given catalog.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.merchantCenterAccountLinks](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.merchantCenterAccountLinks)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.merchantCenterAccountLinks/create)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/merchantCenterAccountLinks`   
Creates a `[MerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.merchantCenterAccountLinks#MerchantCenterAccountLink)`.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.merchantCenterAccountLinks/delete)` |  `DELETE /v2alpha/{name=projects/*/locations/*/catalogs/*/merchantCenterAccountLinks/*}`   
Deletes a `[MerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.merchantCenterAccountLinks#MerchantCenterAccountLink)`.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.merchantCenterAccountLinks/list)` |  `GET /v2alpha/{parent=projects/*/locations/*/catalogs/*}/merchantCenterAccountLinks`   
Lists all `[MerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.merchantCenterAccountLinks#MerchantCenterAccountLink)`s under the specified parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)`.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models/create)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/models`   
Creates a new model.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models/delete)` |  `DELETE /v2alpha/{name=projects/*/locations/*/catalogs/*/models/*}`   
Deletes an existing model.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models/get)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/models/*}`   
Gets a model.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models/list)` |  `GET /v2alpha/{parent=projects/*/locations/*/catalogs/*}/models`   
Lists all the models linked to this event store.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models/patch)` |  `PATCH /v2alpha/{model.name=projects/*/locations/*/catalogs/*/models/*}`   
Update of model metadata.  
`[pause](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models/pause)` |  `POST /v2alpha/{name=projects/*/locations/*/catalogs/*/models/*}:pause`   
Pauses the training of an existing model.  
`[resume](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models/resume)` |  `POST /v2alpha/{name=projects/*/locations/*/catalogs/*/models/*}:resume`   
Resumes the training of an existing model.  
`[tune](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.models/tune)` |  `POST /v2alpha/{name=projects/*/locations/*/catalogs/*/models/*}:tune`   
Tunes an existing model.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.operations/get)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.operations/list)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.placements](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements)

Methods  
---  
`[conversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/conversationalSearch)` |  `POST /v2alpha/{placement=projects/*/locations/*/catalogs/*/placements/*}:conversationalSearch`   
Performs a conversational search.  
`[predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/predict)` |  `POST /v2alpha/{placement=projects/*/locations/*/catalogs/*/placements/*}:predict`   
Makes a recommendation prediction.  
`[search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search)` |  `POST /v2alpha/{placement=projects/*/locations/*/catalogs/*/placements/*}:search`   
Performs a search.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.servingConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs)

Methods  
---  
`[addControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/addControl)` |  `POST /v2alpha/{servingConfig=projects/*/locations/*/catalogs/*/servingConfigs/*}:addControl`   
Enables a Control on the specified ServingConfig.  
`[conversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/conversationalSearch)` |  `POST /v2alpha/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:conversationalSearch`   
Performs a conversational search.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/create)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/servingConfigs`   
Creates a ServingConfig.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/delete)` |  `DELETE /v2alpha/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Deletes a ServingConfig.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/get)` |  `GET /v2alpha/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Gets a ServingConfig.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/list)` |  `GET /v2alpha/{parent=projects/*/locations/*/catalogs/*}/servingConfigs`   
Lists all ServingConfigs linked to this catalog.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/patch)` |  `PATCH /v2alpha/{servingConfig.name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Updates a ServingConfig.  
`[predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/predict)` |  `POST /v2alpha/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:predict`   
Makes a recommendation prediction.  
`[removeControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/removeControl)` |  `POST /v2alpha/{servingConfig=projects/*/locations/*/catalogs/*/servingConfigs/*}:removeControl`   
Disables a Control on the specified ServingConfig.  
`[search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.servingConfigs/search)` |  `POST /v2alpha/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:search`   
Performs a search.  
  
## REST Resource: [v2alpha.projects.locations.catalogs.userEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents)

Methods  
---  
`[collect](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/collect)` |  `GET /v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect`   
Writes a single user event from the browser.  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/export)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:export`   
Exports user events.  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/import)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:import`   
Bulk import of User events.  
`[purge](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/purge)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge`   
Deletes permanently all user events specified by the filter provided.  
`[rejoin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/rejoin)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin`   
Starts a user-event rejoin operation with latest product catalog.  
`[write](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/write)` |  `POST /v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:write`   
Writes a single user event.  
  
## REST Resource: [v2alpha.projects.locations.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.operations/get)` |  `GET /v2alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.operations/list)` |  `GET /v2alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2alpha.projects.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.operations/get)` |  `GET /v2alpha/{name=projects/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.operations/list)` |  `GET /v2alpha/{name=projects/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2alpha.projects.retailProject](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.retailProject)

Methods  
---  
`[acceptTerms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.retailProject/acceptTerms)` |  `POST /v2alpha/{project=projects/*/retailProject}:acceptTerms`   
Accepts service terms for this project.  
  
## REST Resource: [v2.projects.locations.catalogs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs)

Methods  
---  
`[completeQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/completeQuery)` |  `GET /v2/{catalog=projects/*/locations/*/catalogs/*}:completeQuery`   
Completes the specified prefix with keyword suggestions.  
`[exportAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/exportAnalyticsMetrics)` |  `POST /v2/{catalog=projects/*/locations/*/catalogs/*}:exportAnalyticsMetrics`   
Exports analytics metrics.  
`[getAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getAttributesConfig)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*/attributesConfig}`   
Gets an `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[getCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getCompletionConfig)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*/completionConfig}`   
Gets a `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/CompletionConfig)`.  
`[getConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getConversationalSearchCustomizationConfig)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*}/conversationalSearchCustomizationConfig`   
Returns the conversational search customization config for a given catalog.  
`[getDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getDefaultBranch)` |  `GET /v2/{catalog=projects/*/locations/*/catalogs/*}:getDefaultBranch`   
Get which branch is currently default branch set by `[CatalogService.SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/setDefaultBranch#google.cloud.retail.v2.CatalogService.SetDefaultBranch)` method under a specified parent catalog.  
`[getGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getGenerativeQuestionFeature)` |  `GET /v2/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature`   
Manages overal generative question feature state -- enables toggling feature on and off.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/list)` |  `GET /v2/{parent=projects/*/locations/*}/catalogs`   
Lists all the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#Catalog)`s associated with the project.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/patch)` |  `PATCH /v2/{catalog.name=projects/*/locations/*/catalogs/*}`   
Updates the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#Catalog)`s.  
`[setDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/setDefaultBranch)` |  `POST /v2/{catalog=projects/*/locations/*/catalogs/*}:setDefaultBranch`   
Set a specified branch id as default branch.  
`[updateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateAttributesConfig)` |  `PATCH /v2/{attributesConfig.name=projects/*/locations/*/catalogs/*/attributesConfig}`   
Updates the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[updateCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateCompletionConfig)` |  `PATCH /v2/{completionConfig.name=projects/*/locations/*/catalogs/*/completionConfig}`   
Updates the `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/CompletionConfig)`s.  
`[updateConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateConversationalSearchCustomizationConfig)` |  `PATCH /v2/{conversationalSearchCustomizationConfig.catalog=projects/*/locations/*/catalogs/*}/conversationalSearchCustomizationConfig`   
Updates the conversational search customization config for a given catalog.  
`[updateGenerativeQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateGenerativeQuestion)` |  `PATCH /v2/{generativeQuestionConfig.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion`   
Allows management of individual questions.  
`[updateGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateGenerativeQuestionFeature)` |  `PATCH /v2/{generativeQuestionsFeatureConfig.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature`   
Manages overal generative question feature state -- enables toggling feature on and off.  
  
## REST Resource: [v2.projects.locations.catalogs.attributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig)

Methods  
---  
`[addCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig/addCatalogAttribute)` |  `POST /v2/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:addCatalogAttribute`   
Adds the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#CatalogAttribute)` to the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[removeCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig/removeCatalogAttribute)` |  `POST /v2/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:removeCatalogAttribute`   
Removes the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#CatalogAttribute)` from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
`[replaceCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig/replaceCatalogAttribute)` |  `POST /v2/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:replaceCatalogAttribute`   
Replaces the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#CatalogAttribute)` in the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#AttributesConfig)` by updating the catalog attribute with the same `[CatalogAttribute.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.key)`.  
  
## REST Resource: [v2.projects.locations.catalogs.branches.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.operations/get)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*/branches/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v2.projects.locations.catalogs.branches.products](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products)

Methods  
---  
`[addFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/addFulfillmentPlaces)` |  `POST /v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces`   
We recommend that you use the `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/addLocalInventories#google.cloud.retail.v2.ProductService.AddLocalInventories)` method instead of the `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/addFulfillmentPlaces#google.cloud.retail.v2.ProductService.AddFulfillmentPlaces)` method.  
`[addLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/addLocalInventories)` |  `POST /v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories`   
Updates local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` at a list of places, while respecting the last update timestamps of each inventory field.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/create)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products`   
Creates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/delete)` |  `DELETE /v2/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Deletes a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/get)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Gets a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`.  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/import)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import`   
Bulk import of multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list)` |  `GET /v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products`   
Gets a list of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/patch)` |  `PATCH /v2/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}`   
Updates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`.  
`[purge](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/purge)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge`   
Permanently deletes all selected `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s under a branch.  
`[removeFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/removeFulfillmentPlaces)` |  `POST /v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces`   
We recommend that you use the `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/removeLocalInventories#google.cloud.retail.v2.ProductService.RemoveLocalInventories)` method instead of the `[ProductService.RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/removeFulfillmentPlaces#google.cloud.retail.v2.ProductService.RemoveFulfillmentPlaces)` method.  
`[removeLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/removeLocalInventories)` |  `POST /v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories`   
Remove local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` at a list of places at a removal timestamp.  
`[setInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/setInventory)` |  `POST /v2/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory`   
Updates inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` while respecting the last update timestamps of each inventory field.  
  
## REST Resource: [v2.projects.locations.catalogs.completionData](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.completionData)

Methods  
---  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.completionData/import)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/completionData:import`   
Bulk import of processed completion dataset.  
  
## REST Resource: [v2.projects.locations.catalogs.controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.controls)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.controls/create)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/controls`   
Creates a Control.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.controls/delete)` |  `DELETE /v2/{name=projects/*/locations/*/catalogs/*/controls/*}`   
Deletes a Control.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.controls/get)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*/controls/*}`   
Gets a Control.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.controls/list)` |  `GET /v2/{parent=projects/*/locations/*/catalogs/*}/controls`   
Lists all Controls by their parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#Catalog)`.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.controls/patch)` |  `PATCH /v2/{control.name=projects/*/locations/*/catalogs/*/controls/*}`   
Updates a Control.  
  
## REST Resource: [v2.projects.locations.catalogs.generativeQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.generativeQuestion)

Methods  
---  
`[batchUpdate](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.generativeQuestion/batchUpdate)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate`   
Allows management of multiple questions.  
  
## REST Resource: [v2.projects.locations.catalogs.generativeQuestions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.generativeQuestions)

Methods  
---  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.generativeQuestions/list)` |  `GET /v2/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions`   
Returns all questions for a given catalog.  
  
## REST Resource: [v2.projects.locations.catalogs.models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/create)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/models`   
Creates a new model.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/delete)` |  `DELETE /v2/{name=projects/*/locations/*/catalogs/*/models/*}`   
Deletes an existing model.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/get)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*/models/*}`   
Gets a model.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/list)` |  `GET /v2/{parent=projects/*/locations/*/catalogs/*}/models`   
Lists all the models linked to this event store.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/patch)` |  `PATCH /v2/{model.name=projects/*/locations/*/catalogs/*/models/*}`   
Update of model metadata.  
`[pause](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/pause)` |  `POST /v2/{name=projects/*/locations/*/catalogs/*/models/*}:pause`   
Pauses the training of an existing model.  
`[resume](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/resume)` |  `POST /v2/{name=projects/*/locations/*/catalogs/*/models/*}:resume`   
Resumes the training of an existing model.  
`[tune](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/tune)` |  `POST /v2/{name=projects/*/locations/*/catalogs/*/models/*}:tune`   
Tunes an existing model.  
  
## REST Resource: [v2.projects.locations.catalogs.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.operations/get)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.operations/list)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2.projects.locations.catalogs.placements](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements)

Methods  
---  
`[conversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/conversationalSearch)` |  `POST /v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:conversationalSearch`   
Performs a conversational search.  
`[predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/predict)` |  `POST /v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:predict`   
Makes a recommendation prediction.  
`[search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search)` |  `POST /v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:search`   
Performs a search.  
  
## REST Resource: [v2.projects.locations.catalogs.servingConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs)

Methods  
---  
`[addControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/addControl)` |  `POST /v2/{servingConfig=projects/*/locations/*/catalogs/*/servingConfigs/*}:addControl`   
Enables a Control on the specified ServingConfig.  
`[conversationalSearch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/conversationalSearch)` |  `POST /v2/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:conversationalSearch`   
Performs a conversational search.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/create)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/servingConfigs`   
Creates a ServingConfig.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/delete)` |  `DELETE /v2/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Deletes a ServingConfig.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/get)` |  `GET /v2/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Gets a ServingConfig.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/list)` |  `GET /v2/{parent=projects/*/locations/*/catalogs/*}/servingConfigs`   
Lists all ServingConfigs linked to this catalog.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/patch)` |  `PATCH /v2/{servingConfig.name=projects/*/locations/*/catalogs/*/servingConfigs/*}`   
Updates a ServingConfig.  
`[predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/predict)` |  `POST /v2/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:predict`   
Makes a recommendation prediction.  
`[removeControl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/removeControl)` |  `POST /v2/{servingConfig=projects/*/locations/*/catalogs/*/servingConfigs/*}:removeControl`   
Disables a Control on the specified ServingConfig.  
`[search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs/search)` |  `POST /v2/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:search`   
Performs a search.  
  
## REST Resource: [v2.projects.locations.catalogs.userEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents)

Methods  
---  
`[collect](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/collect)` |  `GET /v2/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect`   
Writes a single user event from the browser.  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/userEvents:import`   
Bulk import of User events.  
`[purge](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/purge)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge`   
Deletes permanently all user events specified by the filter provided.  
`[rejoin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/rejoin)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin`   
Starts a user-event rejoin operation with latest product catalog.  
`[write](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/write)` |  `POST /v2/{parent=projects/*/locations/*/catalogs/*}/userEvents:write`   
Writes a single user event.  
  
## REST Resource: [v2.projects.locations.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations/get)` |  `GET /v2/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations/list)` |  `GET /v2/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2.projects.operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.operations/get)` |  `GET /v2/{name=projects/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.operations/list)` |  `GET /v2/{name=projects/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
