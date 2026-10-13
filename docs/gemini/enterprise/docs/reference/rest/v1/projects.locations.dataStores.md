---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores
title: REST Resource: projects.locations.dataStores \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:56.256412+00:00
---

# REST Resource: projects.locations.dataStores  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dataStores Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DataStore
    * JSON representation
  * Methods



## Resource: DataStore

DataStore captures global settings and configs at the DataStore level.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "industryVertical": enum ([IndustryVertical](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/IndustryVertical)),
      "solutionTypes": [
        enum ([SolutionType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SolutionType))
      ],
      "defaultSchemaId": string,
      "contentConfig": enum ([ContentConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.ContentConfig)),
      "createTime": string,
      "advancedSiteSearchConfig": {
        object ([AdvancedSiteSearchConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.AdvancedSiteSearchConfig))
      },
      "naturalLanguageQueryUnderstandingConfig": {
        object ([NaturalLanguageQueryUnderstandingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.NaturalLanguageQueryUnderstandingConfig))
      },
      "kmsKeyName": string,
      "cmekConfig": {
        object ([CmekConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs#CmekConfig))
      },
      "billingEstimation": {
        object ([BillingEstimation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.BillingEstimation))
      },
      "aclEnabled": boolean,
      "workspaceConfig": {
        object ([WorkspaceConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.WorkspaceConfig))
      },
      "documentProcessingConfig": {
        object ([DocumentProcessingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.DocumentProcessingConfig))
      },
      "startingSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas#Schema))
      },
      "healthcareFhirConfig": {
        object ([HealthcareFhirConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.HealthcareFhirConfig))
      },
      "servingConfigDataStore": {
        object ([ServingConfigDataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.ServingConfigDataStore))
      },
      "identityMappingStore": string,
      "isInfobotFaqDataStore": boolean,
      "federatedSearchConfig": {
        object ([FederatedSearchConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.FederatedSearchConfig))
      },
      "configurableBillingApproach": enum ([ConfigurableBillingApproach](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.ConfigurableBillingApproach)),
      "configurableBillingApproachUpdateTime": string,
      "dataProtectionPolicy": {
        object ([DataProtectionPolicy](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/DataProtectionPolicy))
      }
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The full resource name of the data store. Format: `projects/{project}/locations/{location}/collections/{collectionId}/dataStores/{dataStoreId}`.This field must be a UTF-8 encoded string with a length limit of 1024 characters.  
`displayName` |  `string` Required. The data store display name.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`industryVertical` |  `enum (`[IndustryVertical](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/IndustryVertical)`)` Immutable. The industry vertical that the data store registers.  
`solutionTypes[]` |  `enum (`[SolutionType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SolutionType)`)` The solutions that the data store enrolls. Available solutions for each `[industryVertical](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.FIELDS.industry_vertical)`:

  * `MEDIA`: `SOLUTION_TYPE_RECOMMENDATION` and `SOLUTION_TYPE_SEARCH`.
  * `SITE_SEARCH`: `SOLUTION_TYPE_SEARCH` is automatically enrolled. Other solutions cannot be enrolled.

  
`defaultSchemaId` |  `string` Output only. The ID of the default `[Schema](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas#Schema)` associated to this data store.  
`contentConfig` |  `enum (`[ContentConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.ContentConfig)`)` Immutable. The content config of the data store. If this field is unset, the server behavior defaults to `[ContentConfig.NO_CONTENT](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.ContentConfig.ENUM_VALUES.NO_CONTENT)`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)` was created at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`advancedSiteSearchConfig` |  `object (`[AdvancedSiteSearchConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.AdvancedSiteSearchConfig)`)` Optional. Configuration for advanced site search.  
`naturalLanguageQueryUnderstandingConfig` |  `object (`[NaturalLanguageQueryUnderstandingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.NaturalLanguageQueryUnderstandingConfig)`)` Optional. Configuration for Natural Language Query Understanding.  
`kmsKeyName` |  `string` Input only. The KMS key to be used to protect this DataStore at creation time.Must be set for requests that need to comply with CMEK Org Policy protections.If this field is set and processed successfully, the DataStore will be protected by the KMS key, as indicated in the cmekConfig field.  
`cmekConfig` |  `object (`[CmekConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs#CmekConfig)`)` Output only. CMEK-related information for the DataStore.  
`billingEstimation` |  `object (`[BillingEstimation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.BillingEstimation)`)` Output only. Data size estimation for billing.  
`aclEnabled` |  `boolean` Immutable. Whether data in the `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)` has ACL information. If set to `true`, the source data must have ACL. ACL will be ingested when data is ingested by `[DocumentService.ImportDocuments](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.branches.documents/import#google.cloud.discoveryengine.v1.DocumentService.ImportDocuments)` methods.When ACL is enabled for the `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`, `[Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document)` can't be accessed by calling `[DocumentService.GetDocument](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.branches.documents/get#google.cloud.discoveryengine.v1.DocumentService.GetDocument)` or `[DocumentService.ListDocuments](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.branches.documents/list#google.cloud.discoveryengine.v1.DocumentService.ListDocuments)`.Currently ACL is only supported in `GENERIC` industry vertical with non-`PUBLIC_WEBSITE` content config.  
`workspaceConfig` |  `object (`[WorkspaceConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.WorkspaceConfig)`)` Config to store data store type configuration for workspace data. This must be set when `[DataStore.content_config](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.FIELDS.content_config)` is set as `[DataStore.ContentConfig.GOOGLE_WORKSPACE](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.ContentConfig.ENUM_VALUES.GOOGLE_WORKSPACE)`.  
`documentProcessingConfig` |  `object (`[DocumentProcessingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.DocumentProcessingConfig)`)` Configuration for Document understanding and enrichment.  
`startingSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas#Schema)`)` The start schema to use for this `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)` when provisioning it. If unset, a default vertical specialized schema will be used.This field is only used by `[dataStores.create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/create#google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore)` API, and will be ignored if used in other APIs. This field will be omitted from all API responses including `[dataStores.create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/create#google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore)` API. To retrieve a schema of a `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`, use `[SchemaService.GetSchema](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.schemas/get#google.cloud.discoveryengine.v1.SchemaService.GetSchema)` API instead.The provided schema will be validated against certain rules on schema. Learn more from [this doc](https://cloud.google.com/generative-ai-app-builder/docs/provide-schema).  
`healthcareFhirConfig` |  `object (`[HealthcareFhirConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.HealthcareFhirConfig)`)` Optional. Configuration for `HEALTHCARE_FHIR` vertical.  
`servingConfigDataStore` |  `object (`[ServingConfigDataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.ServingConfigDataStore)`)` Optional. Stores serving config at DataStore level.  
`identityMappingStore` |  `string` Immutable. The fully qualified resource name of the associated `[IdentityMappingStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores#IdentityMappingStore)`. This field can only be set for aclEnabled DataStores with `THIRD_PARTY` or `GSUITE` IdP. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`.  
`isInfobotFaqDataStore` |  `boolean` Optional. If set, this DataStore is an Infobot FAQ DataStore.  
`federatedSearchConfig` |  `object (`[FederatedSearchConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.FederatedSearchConfig)`)` Optional. If set, this DataStore is a federated search DataStore.  
`configurableBillingApproach` |  `enum (`[ConfigurableBillingApproach](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore.ConfigurableBillingApproach)`)` Optional. Configuration for configurable billing approach. See  
`configurableBillingApproachUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when configurableBillingApproach was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dataProtectionPolicy` |  `object (`[DataProtectionPolicy](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/DataProtectionPolicy)`)` Optional. Specifies the data protection policy for the data store.  
  
## Methods  
  
---  
  
### `[completeQuery](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/completeQuery)`

|  Completes the specified user input with keyword suggestions.  
  
### `[create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/create)`

|  Creates a `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`.  
  
### `[delete](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/delete)`

|  Deletes a `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`.  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/get)`

|  Gets a `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`.  
  
### `[getIamPolicy](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/getIamPolicy)`

|  Gets the IAM access control policy for a `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`.  
  
### `[getSiteSearchEngine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/getSiteSearchEngine)`

|  Gets the `[SiteSearchEngine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SiteSearchEngine)`.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/list)`

|  Lists all the `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`s associated with the project.  
  
### `[patch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/patch)`

|  Updates a `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`  
  
### `[setIamPolicy](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/setIamPolicy)`

|  Sets the IAM access control policy for a `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
