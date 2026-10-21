---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain/
title: Method: endpoints.explain \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:23:55.323520+00:00
---

# Method: endpoints.explain  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: endpoints.explain Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.endpoints.explain

Perform an online explanation.

If `[deployedModelId](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#body.request_body.FIELDS.deployed_model_id)` is specified, the corresponding endpoints.deployModel must have `[explanationSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#DeployedModel.FIELDS.explanation_spec)` populated. If `[deployedModelId](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#body.request_body.FIELDS.deployed_model_id)` is not specified, all DeployedModels must have `[explanationSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#DeployedModel.FIELDS.explanation_spec)` populated.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{endpoint}:explain`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`endpoint` `string` Required. The name of the Endpoint requested to serve the explanation. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

### Request body

The request body contains data with the following structure: | Fields  
  
`instances[]` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' `[Model's](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#DeployedModel.FIELDS.model)` `[PredictSchemata's](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models#Model.FIELDS.predict_schemata)` `[instanceSchemaUri](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictSchemata#FIELDS.instance_schema_uri)`. | `parameters` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' `[Model's ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#DeployedModel.FIELDS.model)` `[PredictSchemata's](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models#Model.FIELDS.predict_schemata)` `[parametersSchemaUri](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictSchemata#FIELDS.parameters_schema_uri)`. | `explanationSpecOverride` `object (`[ExplanationSpecOverride](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ExplanationSpecOverride)`)` If specified, overrides the `[explanationSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#DeployedModel.FIELDS.explanation_spec)` of the DeployedModel. Can be used for explaining prediction results with different configurations, such as: - Explaining top-5 predictions results as opposed to top-1; - Increasing path count or step count of the attribution methods to reduce approximate errors; - Using different baselines for explaining the prediction results. | `concurrentExplanationSpecOverride` `map (key: string, value: object (`[ExplanationSpecOverride](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ExplanationSpecOverride)`))` Optional. This field is the same as the one above, but supports multiple explanations to occur in parallel. The key can be any string. Each override will be run against the model, then its explanations will be grouped together.Note - these explanations are run **In Addition** to the default Explanation in the deployed model. | `deployedModelId` `string` If specified, this ExplainRequest will be served by the chosen DeployedModel, overriding `[Endpoint.traffic_split](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#Endpoint.FIELDS.traffic_split)`.

### Response body

Response message for `[PredictionService.Explain](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#google.cloud.aiplatform.v1beta1.PredictionService.Explain)`. If successful, the response body contains data with the following structure: | Fields  
  
`explanations[]` `object (`[Explanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Explanation)`)` The explanations of the Model's `[PredictResponse.predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictResponse#FIELDS.predictions)`.It has the same number of elements as `[instances](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#body.request_body.FIELDS.instances)` to be explained. | `concurrentExplanations` `map (key: string, value: object (`[ConcurrentExplanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ConcurrentExplanation)`))` This field stores the results of the explanations run in parallel with The default explanation strategy/method. | `deployedModelId` `string` id of the Endpoint's DeployedModel that served this explanation. | `predictions[]` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The predictions that are the output of the predictions call. Same as `[PredictResponse.predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictResponse#FIELDS.predictions)`. | JSON representation  
---  
      
    
    {
      "explanations": [
        {
          object ([Explanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Explanation))
        }
      ],
      "concurrentExplanations": {
        string: {
          object ([ConcurrentExplanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ConcurrentExplanation))
        },
        ...
      },
      "deployedModelId": string,
      "predictions": [
        value
      ]
    }  
  
## ExplanationSpecOverride

The `[ExplanationSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExplanationSpec)` entries that can be overridden at `[online explanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#google.cloud.aiplatform.v1beta1.PredictionService.Explain)` time.

Fields  
  
`parameters` `object (`[ExplanationParameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExplanationSpec#ExplanationParameters)`)` The parameters to be overridden. Note that the attribution method cannot be changed. If not specified, no parameter is overridden. | `metadata` `object (`[ExplanationMetadataOverride](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ExplanationMetadataOverride)`)` The metadata to be overridden. If not specified, no metadata is overridden. | `examplesOverride` `object (`[ExamplesOverride](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ExamplesOverride)`)` The example-based explanations parameter overrides. | JSON representation  
---  
      
    
    {
      "parameters": {
        object ([ExplanationParameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExplanationSpec#ExplanationParameters))
      },
      "metadata": {
        object ([ExplanationMetadataOverride](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ExplanationMetadataOverride))
      },
      "examplesOverride": {
        object ([ExamplesOverride](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ExamplesOverride))
      }
    }  
  
## ExplanationMetadataOverride

The `[ExplanationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExplanationSpec#ExplanationMetadata)` entries that can be overridden at `[online explanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#google.cloud.aiplatform.v1beta1.PredictionService.Explain)` time.

Fields  
  
`inputs` `map (key: string, value: object (`[InputMetadataOverride](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#InputMetadataOverride)`))` Required. Overrides the `[input metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExplanationSpec#ExplanationMetadata.FIELDS.inputs)` of the features. The key is the name of the feature to be overridden. The keys specified here must exist in the input metadata to be overridden. If a feature is not specified here, the corresponding feature's input metadata is not overridden. | JSON representation  
---  
      
    
    {
      "inputs": {
        string: {
          object ([InputMetadataOverride](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#InputMetadataOverride))
        },
        ...
      }
    }  
  
## InputMetadataOverride

The `[input metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExplanationSpec#InputMetadata)` entries to be overridden.

Fields  
  
`inputBaselines[]` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` baseline inputs for this feature.This overrides the `input_baseline` field of the `[ExplanationMetadata.InputMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExplanationSpec#InputMetadata)` object of the corresponding feature's input metadata. If it's not specified, the original baselines are not overridden. | JSON representation  
---  
      
    
    {
      "inputBaselines": [
        value
      ]
    }  
  
## ExamplesOverride

Overrides for example-based explanations.

Fields  
  
`neighborCount` `integer` The number of neighbors to return. | `crowdingCount` `integer` The number of neighbors to return that have the same crowding tag. | `restrictions[]` `object (`[ExamplesRestrictionsNamespace](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ExamplesRestrictionsNamespace)`)` Restrict the resulting nearest neighbors to respect these constraints. | `returnEmbeddings` `boolean` If true, return the embeddings instead of neighbors. | `dataFormat` `enum (`[DataFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#DataFormat)`)` The format of the data being provided with each call. | JSON representation  
---  
      
    
    {
      "neighborCount": integer,
      "crowdingCount": integer,
      "restrictions": [
        {
          object ([ExamplesRestrictionsNamespace](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#ExamplesRestrictionsNamespace))
        }
      ],
      "returnEmbeddings": boolean,
      "dataFormat": enum ([DataFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#DataFormat))
    }  
  
## ExamplesRestrictionsNamespace

Restrictions namespace for example-based explanations overrides.

Fields  
  
`namespaceName` `string` The namespace name. | `allow[]` `string` The list of allowed tags. | `deny[]` `string` The list of deny tags. | JSON representation  
---  
      
    
    {
      "namespaceName": string,
      "allow": [
        string
      ],
      "deny": [
        string
      ]
    }  
  
## DataFormat

data format enum.

Enums  
---  
`DATA_FORMAT_UNSPECIFIED` | Unspecified format. Must not be used.  
`INSTANCES` | Provided data is a set of model inputs.  
`EMBEDDINGS` | Provided data is a set of embeddings.  
  
## ConcurrentExplanation

This message is a wrapper grouping Concurrent Explanations.

Fields  
  
`explanations[]` `object (`[Explanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Explanation)`)` The explanations of the Model's `[PredictResponse.predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictResponse#FIELDS.predictions)`.It has the same number of elements as `[instances](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/explain#body.request_body.FIELDS.instances)` to be explained. | JSON representation  
---  
      
    
    {
      "explanations": [
        {
          object ([Explanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Explanation))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
