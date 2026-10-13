---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines
title: REST Resource: projects.locations.collections.engines \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:52.026498+00:00
---

# REST Resource: projects.locations.collections.engines  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.engines Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Engine
    * JSON representation
  * ChatEngineConfig
    * JSON representation
  * AgentCreationConfig
    * JSON representation
  * SearchEngineConfig
    * JSON representation
  * SearchTier
  * SearchAddOn
  * MediaRecommendationEngineConfig
    * JSON representation
  * OptimizationObjectiveConfig
    * JSON representation
  * TrainingState
  * EngineFeaturesConfig
    * JSON representation
  * RecommendedForYouFeatureConfig
    * JSON representation
  * MostPopularFeatureConfig
    * JSON representation
  * ChatEngineMetadata
    * JSON representation
  * CommonConfig
    * JSON representation
  * KnowledgeGraphConfig
    * JSON representation
  * FeatureConfig
    * JSON representation
  * AppType
  * SessionConfig
    * JSON representation
  * SessionManagementPolicy
  * SessionTtl
    * JSON representation
  * FeatureState
  * ConfigurableBillingApproach
  * ModelState
  * ObservabilityConfig
    * JSON representation
  * AgentGatewaySetting
    * JSON representation
  * AgentGatewayReference
    * JSON representation
  * MarketplaceAgentVisibility
  * Methods



## Resource: Engine

Metadata that describes the training and serving parameters of an `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "dataStoreIds": [
        string
      ],
      "solutionType": enum ([SolutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType)),
      "industryVertical": enum ([IndustryVertical](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/IndustryVertical)),
      "commonConfig": {
        object ([CommonConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#CommonConfig))
      },
      "knowledgeGraphConfig": {
        object ([KnowledgeGraphConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#KnowledgeGraphConfig))
      },
      "appType": enum ([AppType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#AppType)),
      "disableAnalytics": boolean,
      "sessionConfig": {
        object ([SessionConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SessionConfig))
      },
      "features": {
        string: enum ([FeatureState](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#FeatureState)),
        ...
      },
      "cmekConfig": {
        object ([CmekConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.cmekConfigs#CmekConfig))
      },
      "configurableBillingApproach": enum ([ConfigurableBillingApproach](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ConfigurableBillingApproach)),
      "modelConfigs": {
        string: enum ([ModelState](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ModelState)),
        ...
      },
      "observabilityConfig": {
        object ([ObservabilityConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ObservabilityConfig))
      },
      "connectorTenantInfo": {
        string: string,
        ...
      },
      "agentGatewaySetting": {
        object ([AgentGatewaySetting](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#AgentGatewaySetting))
      },
      "marketplaceAgentVisibility": enum ([MarketplaceAgentVisibility](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#MarketplaceAgentVisibility)),
      "procurementContactEmails": [
        string
      ],
      "associatedAgentRegistry": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "chatEngineConfig": {
        object ([ChatEngineConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ChatEngineConfig))
      },
      "searchEngineConfig": {
        object ([SearchEngineConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SearchEngineConfig))
      },
      "mediaRecommendationEngineConfig": {
        object ([MediaRecommendationEngineConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#MediaRecommendationEngineConfig))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "chatEngineMetadata": {
        object ([ChatEngineMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ChatEngineMetadata))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The fully qualified resource name of the engine.This field must be a UTF-8 encoded string with a length limit of 1024 characters.Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}` engine should be 1-63 characters, and valid characters are /[a-z0-9][a-z0-9-_]*/. Otherwise, an INVALID_ARGUMENT error is returned.  
`displayName` |  `string` Required. The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the Recommendation Engine was created at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the Recommendation Engine was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dataStoreIds[]` |  `string` Optional. The data stores associated with this engine.For `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)` and `[SOLUTION_TYPE_RECOMMENDATION](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_RECOMMENDATION)` type of engines, they can only associate with at most one data store.If `[solutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine.FIELDS.solution_type)` is `[SOLUTION_TYPE_CHAT](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_CHAT)`, multiple `[DataStore](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`s in the same `Collection` can be associated here.Note that when used in `CreateEngineRequest`, one DataStore ID must be provided as the system will use it for necessary initializations.  
`solutionType` |  `enum (`[SolutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType)`)` Required. The solutions of the engine.  
`industryVertical` |  `enum (`[IndustryVertical](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/IndustryVertical)`)` Optional. The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on `[DataStore](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`: Vertical on Engine has to match vertical of the DataStore linked to the engine.  
`commonConfig` |  `object (`[CommonConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#CommonConfig)`)` Common config spec that specifies the metadata of the engine.  
`knowledgeGraphConfig` |  `object (`[KnowledgeGraphConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#KnowledgeGraphConfig)`)` Optional. Configurations for the Knowledge Graph. Only applicable if `[solutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine.FIELDS.solution_type)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`appType` |  `enum (`[AppType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#AppType)`)` Optional. Immutable. This the application type which this engine resource represents. NOTE: this is a new concept independ of existing industry vertical or solution type.  
`disableAnalytics` |  `boolean` Optional. Whether to disable analytics for searches performed on this engine.  
`sessionConfig` |  `object (`[SessionConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SessionConfig)`)` Optional. Non-empty default. Session config for the engine.  
`features` |  `map (key: string, value: enum (`[FeatureState](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#FeatureState)`))` Optional. Feature config for the engine to opt in or opt out of features. Supported keys:

  * `*`: all features, if it's present, all other feature state settings are ignored.
  * `agent-gallery`
  * `no-code-agent-builder`
  * `prompt-gallery`
  * `model-selector`
  * `notebook-lm`
  * `people-search`
  * `people-search-org-chart`
  * `bi-directional-audio`
  * `speech-to-text`
  * `feedback`
  * `session-sharing`
  * `personalization-memory`
  * `personalization-suggested-highlights`
  * `mobile-app-access`
  * `disable-agent-sharing`
  * `disable-image-generation`
  * `disable-video-generation`
  * `disable-onedrive-upload`
  * `disable-talk-to-content`
  * `disable-google-drive-upload`
  * `disable-welcome-emails`
  * `disable-canvas`
  * `canvas-workspace`
  * `canvas-app-builder`
  * `skills`
  * `skill-sharing`
  * `skill-sharing-without-admin-approval`
  * `disable-projects`
  * `sobi`
  * `enable-end-user-sharing-with-groups`
  * `single-agent-orchestration`
  * `multi-agent-orchestration`
  * `cross-product-intelligence`
  * `workflow-agents`
  * `in-app-notifications`

  
`cmekConfig` |  `object (`[CmekConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.cmekConfigs#CmekConfig)`)` Output only. CMEK-related information for the Engine.  
`configurableBillingApproach` |  `enum (`[ConfigurableBillingApproach](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ConfigurableBillingApproach)`)` Optional. Configuration for configurable billing approach.  
`modelConfigs` |  `map (key: string, value: enum (`[ModelState](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ModelState)`))` Optional. Maps a model name to its specific configuration for this engine. This allows admin users to turn on/off individual models. This only stores models whose states are overridden by the admin.When the state is unspecified, or modelConfigs is empty for this model, the system will decide if this model should be available or not based on the default configuration. For example, a preview model should be disabled by default if the admin has not chosen to enable it.  
`observabilityConfig` |  `object (`[ObservabilityConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ObservabilityConfig)`)` Optional. Observability config for the engine.  
`connectorTenantInfo` |  `map (key: string, value: string)` Optional. Maps a connector ID (e.g., "hybrid-github", "shopify") to tenant-specific information required for that connector. The structure of the tenant information string is connector-dependent.  
`agentGatewaySetting` |  `object (`[AgentGatewaySetting](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#AgentGatewaySetting)`)` Optional. The agent gateway setting for the engine.  
`marketplaceAgentVisibility` |  `enum (`[MarketplaceAgentVisibility](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#MarketplaceAgentVisibility)`)` Optional. The visibility of marketplace agents in the agent gallery.  
`procurementContactEmails[]` |  `string` Optional. The emails of the procurement contacts.  
`associatedAgentRegistry` |  `string` Output only. The Agent registry containing the agents, MCP servers and tools associated with this engine. Derived server-side from the linked Agent Gateway's registry.  
Additional config specs that defines the behavior of the engine. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`chatEngineConfig` |  `object (`[ChatEngineConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ChatEngineConfig)`)` Configurations for the Chat Engine. Only applicable if `[solutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine.FIELDS.solution_type)` is `[SOLUTION_TYPE_CHAT](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_CHAT)`.  
`searchEngineConfig` |  `object (`[SearchEngineConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SearchEngineConfig)`)` Configurations for the Search Engine. Only applicable if `[solutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine.FIELDS.solution_type)` is `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`mediaRecommendationEngineConfig` |  `object (`[MediaRecommendationEngineConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#MediaRecommendationEngineConfig)`)` Configurations for the Media Engine. Only applicable on the data stores with `[solutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine.FIELDS.solution_type)` `[SOLUTION_TYPE_RECOMMENDATION](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_RECOMMENDATION)` and `[IndustryVertical.MEDIA](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/IndustryVertical#ENUM_VALUES.MEDIA)` vertical.  
End of mutually exclusive fields.  
Engine metadata to monitor the status of the engine. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`chatEngineMetadata` |  `object (`[ChatEngineMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ChatEngineMetadata)`)` Output only. Additional information of the Chat Engine. Only applicable if `[solutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine.FIELDS.solution_type)` is `[SOLUTION_TYPE_CHAT](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_CHAT)`.  
End of mutually exclusive fields.  
  
## ChatEngineConfig

Configurations for a Chat Engine.

JSON representation  
---  
      
    
    {
      "agentCreationConfig": {
        object ([AgentCreationConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#AgentCreationConfig))
      },
      "dialogflowAgentToLink": string,
      "allowCrossRegion": boolean
    }  
  
Fields  
---  
`agentCreationConfig` |  `object (`[AgentCreationConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#AgentCreationConfig)`)` The configurationt generate the Dialogflow agent that is associated to this Engine.Note that these configurations are one-time consumed by and passed to Dialogflow service. It means they cannot be retrieved using `[EngineService.GetEngine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/get#google.cloud.discoveryengine.v1.EngineService.GetEngine)` or `[EngineService.ListEngines](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/list#google.cloud.discoveryengine.v1.EngineService.ListEngines)` API after engine creation.  
`dialogflowAgentToLink` |  `string` The resource name of an exist Dialogflow agent to link to this Chat Engine. Customers can either provide `agentCreationConfig` to create agent or provide an agent name that links the agent with the Chat engine.Format: `projects/<Project ID>/locations/<location ID>/agents/<Agent ID>`.Note that the `dialogflowAgentToLink` are one-time consumed by and passed to Dialogflow service. It means they cannot be retrieved using `[EngineService.GetEngine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/get#google.cloud.discoveryengine.v1.EngineService.GetEngine)` or `[EngineService.ListEngines](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/list#google.cloud.discoveryengine.v1.EngineService.ListEngines)` API after engine creation. Use `[ChatEngineMetadata.dialogflow_agent](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#ChatEngineMetadata.FIELDS.dialogflow_agent)` for actual agent association after Engine is created.  
`allowCrossRegion` |  `boolean` Optional. If the flag set to true, we allow the agent and engine are in different locations, otherwise the agent and engine are required to be in the same location. The flag is set to false by default.Note that the `allowCrossRegion` are one-time consumed by and passed to `[EngineService.CreateEngine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/create#google.cloud.discoveryengine.v1.EngineService.CreateEngine)`. It means they cannot be retrieved using `[EngineService.GetEngine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/get#google.cloud.discoveryengine.v1.EngineService.GetEngine)` or `[EngineService.ListEngines](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/list#google.cloud.discoveryengine.v1.EngineService.ListEngines)` API after engine creation.  
  
## AgentCreationConfig

Configurations for generating a Dialogflow agent.

Note that these configurations are one-time consumed by and passed to Dialogflow service. It means they cannot be retrieved using `[EngineService.GetEngine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/get#google.cloud.discoveryengine.v1.EngineService.GetEngine)` or `[EngineService.ListEngines](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/list#google.cloud.discoveryengine.v1.EngineService.ListEngines)` API after engine creation.

JSON representation  
---  
      
    
    {
      "business": string,
      "defaultLanguageCode": string,
      "timeZone": string,
      "location": string
    }  
  
Fields  
---  
`business` |  `string` Name of the company, organization or other entity that the agent represents. Used for knowledge connector LLM prompt and for knowledge search.  
`defaultLanguageCode` |  `string` Required. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes.  
`timeZone` |  `string` Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris.  
`location` |  `string` Agent location for Agent creation, supported values: global/us/eu. If not provided, us Engine will create Agent using us-central-1 by default; eu Engine will create Agent using eu-west-1 by default.  
  
## SearchEngineConfig

Configurations for a Search Engine.

JSON representation  
---  
      
    
    {
      "searchTier": enum ([SearchTier](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SearchTier)),
      "requiredSubscriptionTier": enum ([SubscriptionTier](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SubscriptionTier)),
      "searchAddOns": [
        enum ([SearchAddOn](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SearchAddOn))
      ]
    }  
  
Fields  
---  
`searchTier` |  `enum (`[SearchTier](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SearchTier)`)` The search feature tier of this engine.Different tiers might have different pricing. To learn more, check the pricing documentation.Defaults to `[SearchTier.SEARCH_TIER_STANDARD](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SearchTier.ENUM_VALUES.SEARCH_TIER_STANDARD)` if not specified.  
`requiredSubscriptionTier` |  `enum (`[SubscriptionTier](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SubscriptionTier)`)` Optional. The required subscription tier of this engine.If the required subscription tier is search, user with higher license tier like assist can still access the standalone app associated with this engine.Web grounding feature is only available on the app if it is set as `[SubscriptionTier.SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SubscriptionTier#ENUM_VALUES.SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT)`.  
`searchAddOns[]` |  `enum (`[SearchAddOn](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SearchAddOn)`)` The add-on that this search engine enables.  
  
## SearchTier

Tiers of search features. Different tiers might have different pricing. To learn more, check the pricing documentation.

Enums  
---  
`SEARCH_TIER_UNSPECIFIED` | Default value when the enum is unspecified. This is invalid to use.  
`SEARCH_TIER_STANDARD` | Standard tier.  
`SEARCH_TIER_ENTERPRISE` | Enterprise tier.  
  
## SearchAddOn

Add-on that provides additional functionality for search.

Enums  
---  
`SEARCH_ADD_ON_UNSPECIFIED` | Default value when the enum is unspecified. This is invalid to use.  
`SEARCH_ADD_ON_LLM` | Large language model add-on.  
  
## MediaRecommendationEngineConfig

Additional config specs for a Media Recommendation engine.

JSON representation  
---  
      
    
    {
      "type": string,
      "optimizationObjective": string,
      "optimizationObjectiveConfig": {
        object ([OptimizationObjectiveConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#OptimizationObjectiveConfig))
      },
      "trainingState": enum ([TrainingState](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#TrainingState)),
      "engineFeaturesConfig": {
        object ([EngineFeaturesConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#EngineFeaturesConfig))
      }
    }  
  
Fields  
---  
`type` |  `string` Required. The type of engine. e.g., `recommended-for-you`.This field together with `[optimizationObjective](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#MediaRecommendationEngineConfig.FIELDS.optimization_objective)` describe engine metadata to use to control engine training and serving.Currently supported values: `recommended-for-you`, `others-you-may-like`, `more-like-this`, `most-popular-items`.  
`optimizationObjective` |  `string` The optimization objective. e.g., `cvr`.This field together with `[optimizationObjective](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#MediaRecommendationEngineConfig.FIELDS.type)` describe engine metadata to use to control engine training and serving.Currently supported values: `ctr`, `cvr`.If not specified, we choose default based on engine type. Default depends on type of recommendation:`recommended-for-you` => `ctr``others-you-may-like` => `ctr`  
`optimizationObjectiveConfig` |  `object (`[OptimizationObjectiveConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#OptimizationObjectiveConfig)`)` Name and value of the custom threshold for cvr optimizationObjective. For targetField `watch-time`, target_field_value must be an integer value indicating the media progress time in seconds between (0, 86400] (excludes 0, includes 86400) (e.g., 90). For targetField `watch-percentage`, the target_field_value must be a valid float value between (0, 1.0] (excludes 0, includes 1.0) (e.g., 0.5).  
`trainingState` |  `enum (`[TrainingState](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#TrainingState)`)` The training state that the engine is in (e.g. `TRAINING` or `PAUSED`).Since part of the cost of running the service is frequency of training - this can be used to determine when to train engine in order to control cost. If not specified: the default value for `engines.create` method is `TRAINING`. The default value for `engines.patch` method is to keep the state the same as before.  
`engineFeaturesConfig` |  `object (`[EngineFeaturesConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#EngineFeaturesConfig)`)` Optional. Additional engine features config.  
  
## OptimizationObjectiveConfig

Custom threshold for `cvr` optimizationObjective.

JSON representation  
---  
      
    
    {
      "targetField": string,
      "targetFieldValueFloat": number
    }  
  
Fields  
---  
`targetField` |  `string` Required. The name of the field to target. Currently supported values: `watch-percentage`, `watch-time`.  
`targetFieldValueFloat` |  `number` Required. The threshold to be applied to the target (e.g., 0.5).  
  
## TrainingState

The training state of the engine.

Enums  
---  
`TRAINING_STATE_UNSPECIFIED` | Unspecified training state.  
`PAUSED` | The engine training is paused.  
`TRAINING` | The engine is training.  
  
## EngineFeaturesConfig

More feature configs of the selected engine type.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "recommendedForYouConfig": {
        object ([RecommendedForYouFeatureConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#RecommendedForYouFeatureConfig))
      },
      "mostPopularConfig": {
        object ([MostPopularFeatureConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#MostPopularFeatureConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Feature related configurations applied to a specific type of media recommendation engines. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`recommendedForYouConfig` |  `object (`[RecommendedForYouFeatureConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#RecommendedForYouFeatureConfig)`)` Recommended for you engine feature config.  
`mostPopularConfig` |  `object (`[MostPopularFeatureConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#MostPopularFeatureConfig)`)` Most popular engine feature config.  
End of mutually exclusive fields.  
  
## RecommendedForYouFeatureConfig

Additional feature configurations for creating a `recommended-for-you` engine.

JSON representation  
---  
      
    
    {
      "contextEventType": string
    }  
  
Fields  
---  
`contextEventType` |  `string` The type of event with which the engine is queried at prediction time. If set to `generic`, only `view-item`, `media-play`,and `media-complete` will be used as `context-event` in engine training. If set to `view-home-page`, `view-home-page` will also be used as `context-events` in addition to `view-item`, `media-play`, and `media-complete`. Currently supported for the `recommended-for-you` engine. Currently supported values: `view-home-page`, `generic`.  
  
## MostPopularFeatureConfig

Feature configurations that are required for creating a Most Popular engine.

JSON representation  
---  
      
    
    {
      "timeWindowDays": string
    }  
  
Fields  
---  
`timeWindowDays` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The time window of which the engine is queried at training and prediction time. Positive integers only. The value translates to the last X days of events. Currently required for the `most-popular-items` engine.  
  
## ChatEngineMetadata

Additional information of a Chat Engine. Fields in this message are output only.

JSON representation  
---  
      
    
    {
      "dialogflowAgent": string
    }  
  
Fields  
---  
`dialogflowAgent` |  `string` The resource name of a Dialogflow agent, that this Chat Engine refers to.Format: `projects/<Project ID>/locations/<location ID>/agents/<Agent ID>`.  
  
## CommonConfig

Common configurations for an Engine.

JSON representation  
---  
      
    
    {
      "companyName": string
    }  
  
Fields  
---  
`companyName` |  `string` The name of the company, business or entity that is associated with the engine. Setting this may help improve LLM related features.  
  
## KnowledgeGraphConfig

Configuration message for the Knowledge Graph.

JSON representation  
---  
      
    
    {
      "enableCloudKnowledgeGraph": boolean,
      "cloudKnowledgeGraphTypes": [
        string
      ],
      "enablePrivateKnowledgeGraph": boolean,
      "privateKnowledgeGraphTypes": [
        string
      ],
      "featureConfig": {
        object ([FeatureConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#FeatureConfig))
      }
    }  
  
Fields  
---  
`enableCloudKnowledgeGraph` |  `boolean` Whether to enable the Cloud Knowledge Graph for the engine.Defaults to false if not specified.  
`cloudKnowledgeGraphTypes[]` |  `string` Specify entity types to support.  
`enablePrivateKnowledgeGraph` |  `boolean` Whether to enable the Private Knowledge Graph for the engine.Defaults to false if not specified.  
`privateKnowledgeGraphTypes[]` |  `string` Specify entity types to support.  
`featureConfig` |  `object (`[FeatureConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#FeatureConfig)`)` Optional. Feature config for the Knowledge Graph.  
  
## FeatureConfig

Feature config for the Knowledge Graph.

JSON representation  
---  
      
    
    {
      "disablePrivateKgQueryUnderstanding": boolean,
      "disablePrivateKgEnrichment": boolean,
      "disablePrivateKgAutoComplete": boolean,
      "disablePrivateKgQueryUiChips": boolean
    }  
  
Fields  
---  
`disablePrivateKgQueryUnderstanding` |  `boolean` Whether to disable the private KG query understanding for the engine.Defaults to false if not specified.  
`disablePrivateKgEnrichment` |  `boolean` Whether to disable the private KG enrichment for the engine.Defaults to false if not specified.  
`disablePrivateKgAutoComplete` |  `boolean` Whether to disable the private KG auto complete for the engine.Defaults to false if not specified.  
`disablePrivateKgQueryUiChips` |  `boolean` Whether to disable the private KG for query UI chips.Defaults to false if not specified.  
  
## AppType

The app of the engine.

Enums  
---  
`APP_TYPE_UNSPECIFIED` | All non specified apps.  
`APP_TYPE_INTRANET` | App type for intranet search and Agentspace.  
  
## SessionConfig

Configuration for the session.

JSON representation  
---  
      
    
    {
      "sessionManagementPolicy": enum ([SessionManagementPolicy](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SessionManagementPolicy)),
      "sessionTtl": {
        object ([SessionTtl](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SessionTtl))
      }
    }  
  
Fields  
---  
`sessionManagementPolicy` |  `enum (`[SessionManagementPolicy](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SessionManagementPolicy)`)` Optional. Session management policy that defines who will manage the session.  
`sessionTtl` |  `object (`[SessionTtl](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#SessionTtl)`)` Optional. The TTL for the session. If unset, the default value is 60 days.  
  
## SessionManagementPolicy

Session management policy that defines who will manage the session.

Enums  
---  
`SESSION_MANAGEMENT_POLICY_UNSPECIFIED` | Default value.  
`NOT_MANAGED` | The session will be managed by the customer.  
`VERTEX_AI_MANAGED` | Sessions multi-tenancy will be controlled by Google using 1P or 3P identity providers.  
  
## SessionTtl

Defines the TTL for sessions.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "days": integer
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
TTL can be either a number of days or indefinite. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`days` |  `integer` Defines the number of days for session TTL.  
End of mutually exclusive fields.  
  
## FeatureState

The state of the feature for the engine.

Enums  
---  
`FEATURE_STATE_UNSPECIFIED` | The feature state is unspecified.  
`FEATURE_STATE_ON` | The feature is turned on to be accessible.  
`FEATURE_STATE_OFF` | The feature is turned off to be inaccessible.  
  
## ConfigurableBillingApproach

Configuration for configurable billing approach.

Enums  
---  
`CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED` | Default value. For Spark and non-Spark non-configurable billing approach. General pricing model.  
`CONFIGURABLE_BILLING_APPROACH_ENABLED` | The billing approach follows configurations specified by customer.  
  
## ModelState

The status of the model for the engine.

Enums  
---  
`MODEL_STATE_UNSPECIFIED` | The model state is unspecified.  
`MODEL_ENABLED` | The model is enabled by admin.  
`MODEL_DISABLED` | The model is disabled by admin.  
  
## ObservabilityConfig

Observability config for a resource.

JSON representation  
---  
      
    
    {
      "observabilityEnabled": boolean,
      "sensitiveLoggingEnabled": boolean
    }  
  
Fields  
---  
`observabilityEnabled` |  `boolean` Optional. Enables observability. If `false`, all other flags are ignored.  
`sensitiveLoggingEnabled` |  `boolean` Optional. Enables sensitive logging. Sensitive logging includes customer core content (e.g. prompts, responses). If `false`, will sanitize all sensitive fields.  
  
## AgentGatewaySetting

Agent Gateway setting, which may be attached to Gemini Enterprise resources for egress control of Gemini Enterprise agents to agents and tools outside of Gemini Enterprise.

JSON representation  
---  
      
    
    {
      "defaultEgressAgentGateway": {
        object ([AgentGatewayReference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#AgentGatewayReference))
      }
    }  
  
Fields  
---  
`defaultEgressAgentGateway` |  `object (`[AgentGatewayReference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#AgentGatewayReference)`)` Optional. The default egress agent gateway to use, when this setting is applied to a Gemini Enterprise resource.The deployment mode must be GOOGLE_MANAGED, and the governed access path must be AGENT_TO_ANYWHERE.  
  
## AgentGatewayReference

Reference to an Agent Gateway resource.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. The resource name of the agent gateway.Expected format: `projects/{projectNumber}/locations/{location}/agentGateways/{agent_gateway}`.  
  
## MarketplaceAgentVisibility

Represents which marketplace agents are visible to any users in agent gallery.

Enums  
---  
`MARKETPLACE_AGENT_VISIBILITY_UNSPECIFIED` | Defaults to `MARKETPLACE_AGENT_VISIBILITY_UNSPECIFIED`.  
`SHOW_AVAILABLE_AGENTS_ONLY` | Only agents that are currently available for use by the user are visible.  
`SHOW_AGENTS_ALREADY_INTEGRATED` | Show marketplace agents that the user does not yet have access to but are integrated into the engine. This level also includes all agents visible with `SHOW_AVAILABLE_AGENTS_ONLY`.  
`SHOW_AGENTS_ALREADY_PURCHASED` | Show all agents visible with `SHOW_AGENTS_ALREADY_INTEGRATED`, plus agents that have already been purchased by the project/organization, even if they are not currently integrated into the engine.  
`SHOW_ALL_AGENTS` | All agents in the marketplace are visible, regardless of access or purchase status. This level encompasses all agents shown in the previous levels.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/create)`

|  Creates an `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine)`.  
  
### `[delete](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/delete)`

|  Deletes an `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine)`.  
  
### `[get](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/get)`

|  Gets an `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine)`.  
  
### `[getIamPolicy](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/getIamPolicy)`

|  Gets the IAM access control policy for an `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine)`.  
  
### `[list](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/list)`

|  Lists all the `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine)`s associated with the project.  
  
### `[patch](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/patch)`

|  Updates an `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine)`  
  
### `[setIamPolicy](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/setIamPolicy)`

|  Sets the IAM access control policy for an `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines#Engine)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
