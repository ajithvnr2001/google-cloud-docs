---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplainRequestOrBuilder
title: Interface ExplainRequestOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:55.715389+00:00
---

# Interface ExplainRequestOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplainRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExplainRequestOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface ExplainRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsConcurrentExplanationSpecOverride(String key)
    
    
    public abstract boolean containsConcurrentExplanationSpecOverride(String key)

Optional. This field is the same as the one above, but supports multiple explanations to occur in parallel. The key can be any string. Each override will be run against the model, then its explanations will be grouped together.

Note - these explanations are run **In Addition** to the default Explanation in the deployed model.

` map<string, .google.cloud.aiplatform.v1beta1.ExplanationSpecOverride> concurrent_explanation_spec_override = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConcurrentExplanationSpecOverride() (deprecated)
    
    
    public abstract Map<String,ExplanationSpecOverride> getConcurrentExplanationSpecOverride()

Use [#getConcurrentExplanationSpecOverrideMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplainRequestOrBuilder#com_google_cloud_aiplatform_v1beta1_ExplainRequestOrBuilder_getConcurrentExplanationSpecOverrideMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[ExplanationSpecOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride)>` |   
  
### getConcurrentExplanationSpecOverrideCount()
    
    
    public abstract int getConcurrentExplanationSpecOverrideCount()

Optional. This field is the same as the one above, but supports multiple explanations to occur in parallel. The key can be any string. Each override will be run against the model, then its explanations will be grouped together.

Note - these explanations are run **In Addition** to the default Explanation in the deployed model.

` map<string, .google.cloud.aiplatform.v1beta1.ExplanationSpecOverride> concurrent_explanation_spec_override = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConcurrentExplanationSpecOverrideMap()
    
    
    public abstract Map<String,ExplanationSpecOverride> getConcurrentExplanationSpecOverrideMap()

Optional. This field is the same as the one above, but supports multiple explanations to occur in parallel. The key can be any string. Each override will be run against the model, then its explanations will be grouped together.

Note - these explanations are run **In Addition** to the default Explanation in the deployed model.

` map<string, .google.cloud.aiplatform.v1beta1.ExplanationSpecOverride> concurrent_explanation_spec_override = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[ExplanationSpecOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride)>` |   
  
### getConcurrentExplanationSpecOverrideOrDefault(String key, ExplanationSpecOverride defaultValue)
    
    
    public abstract ExplanationSpecOverride getConcurrentExplanationSpecOverrideOrDefault(String key, ExplanationSpecOverride defaultValue)

Optional. This field is the same as the one above, but supports multiple explanations to occur in parallel. The key can be any string. Each override will be run against the model, then its explanations will be grouped together.

Note - these explanations are run **In Addition** to the default Explanation in the deployed model.

` map<string, .google.cloud.aiplatform.v1beta1.ExplanationSpecOverride> concurrent_explanation_spec_override = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[ExplanationSpecOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExplanationSpecOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride)` |   
  
### getConcurrentExplanationSpecOverrideOrThrow(String key)
    
    
    public abstract ExplanationSpecOverride getConcurrentExplanationSpecOverrideOrThrow(String key)

Optional. This field is the same as the one above, but supports multiple explanations to occur in parallel. The key can be any string. Each override will be run against the model, then its explanations will be grouped together.

Note - these explanations are run **In Addition** to the default Explanation in the deployed model.

` map<string, .google.cloud.aiplatform.v1beta1.ExplanationSpecOverride> concurrent_explanation_spec_override = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExplanationSpecOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride)` |   
  
### getDeployedModelId()
    
    
    public abstract String getDeployedModelId()

If specified, this ExplainRequest will be served by the chosen DeployedModel, overriding Endpoint.traffic_split.

`string deployed_model_id = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The deployedModelId.  
  
### getDeployedModelIdBytes()
    
    
    public abstract ByteString getDeployedModelIdBytes()

If specified, this ExplainRequest will be served by the chosen DeployedModel, overriding Endpoint.traffic_split.

`string deployed_model_id = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for deployedModelId.  
  
### getEndpoint()
    
    
    public abstract String getEndpoint()

Required. The name of the Endpoint requested to serve the explanation. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

` string endpoint = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endpoint.  
  
### getEndpointBytes()
    
    
    public abstract ByteString getEndpointBytes()

Required. The name of the Endpoint requested to serve the explanation. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

` string endpoint = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endpoint.  
  
### getExplanationSpecOverride()
    
    
    public abstract ExplanationSpecOverride getExplanationSpecOverride()

If specified, overrides the explanation_spec of the DeployedModel. Can be used for explaining prediction results with different configurations, such as:

  * Explaining top-5 predictions results as opposed to top-1;
  * Increasing path count or step count of the attribution methods to reduce approximate errors;
  * Using different baselines for explaining the prediction results.



`.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride explanation_spec_override = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ExplanationSpecOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride)` | The explanationSpecOverride.  
  
### getExplanationSpecOverrideOrBuilder()
    
    
    public abstract ExplanationSpecOverrideOrBuilder getExplanationSpecOverrideOrBuilder()

If specified, overrides the explanation_spec of the DeployedModel. Can be used for explaining prediction results with different configurations, such as:

  * Explaining top-5 predictions results as opposed to top-1;
  * Increasing path count or step count of the attribution methods to reduce approximate errors;
  * Using different baselines for explaining the prediction results.



`.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride explanation_spec_override = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ExplanationSpecOverrideOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExplanationSpecOverrideOrBuilder)` |   
  
### getInstances(int index)
    
    
    public abstract Value getInstances(int index)

Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value instances = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getInstancesCount()
    
    
    public abstract int getInstancesCount()

Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value instances = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInstancesList()
    
    
    public abstract List<Value> getInstancesList()

Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value instances = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getInstancesOrBuilder(int index)
    
    
    public abstract ValueOrBuilder getInstancesOrBuilder(int index)

Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value instances = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### getInstancesOrBuilderList()
    
    
    public abstract List<? extends ValueOrBuilder> getInstancesOrBuilderList()

Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value instances = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.ValueOrBuilder>` |   
  
### getParameters()
    
    
    public abstract Value getParameters()

The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' Model's  PredictSchemata's parameters_schema_uri.

`.google.protobuf.Value parameters = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` | The parameters.  
  
### getParametersOrBuilder()
    
    
    public abstract ValueOrBuilder getParametersOrBuilder()

The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' Model's  PredictSchemata's parameters_schema_uri.

`.google.protobuf.Value parameters = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### hasExplanationSpecOverride()
    
    
    public abstract boolean hasExplanationSpecOverride()

If specified, overrides the explanation_spec of the DeployedModel. Can be used for explaining prediction results with different configurations, such as:

  * Explaining top-5 predictions results as opposed to top-1;
  * Increasing path count or step count of the attribution methods to reduce approximate errors;
  * Using different baselines for explaining the prediction results.



`.google.cloud.aiplatform.v1beta1.ExplanationSpecOverride explanation_spec_override = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the explanationSpecOverride field is set.  
  
### hasParameters()
    
    
    public abstract boolean hasParameters()

The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' Model's  PredictSchemata's parameters_schema_uri.

`.google.protobuf.Value parameters = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parameters field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
