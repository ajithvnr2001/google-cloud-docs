---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpecOrBuilder
title: Interface ReasoningEngineSpecOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:12.788725+00:00
---

# Interface ReasoningEngineSpecOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReasoningEngineSpecOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface ReasoningEngineSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAgentFramework()
    
    
    public abstract String getAgentFramework()

Optional. The OSS agent framework used to develop the agent. Currently supported values: "google-adk", "langchain", "langgraph", "ag2", "llama-index", "custom".

`string agent_framework = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The agentFramework.  
  
### getAgentFrameworkBytes()
    
    
    public abstract ByteString getAgentFrameworkBytes()

Optional. The OSS agent framework used to develop the agent. Currently supported values: "google-adk", "langchain", "langgraph", "ag2", "llama-index", "custom".

`string agent_framework = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for agentFramework.  
  
### getBuildSpec()
    
    
    public abstract ReasoningEngineSpec.BuildSpec getBuildSpec()

Optional. Configuration for building container image.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.BuildSpec build_spec = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.BuildSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.BuildSpec)` | The buildSpec.  
  
### getBuildSpecOrBuilder()
    
    
    public abstract ReasoningEngineSpec.BuildSpecOrBuilder getBuildSpecOrBuilder()

Optional. Configuration for building container image.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.BuildSpec build_spec = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.BuildSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.BuildSpecOrBuilder)` |   
  
### getClassMethods(int index)
    
    
    public abstract Struct getClassMethods(int index)

Optional. Declarations for object class methods in OpenAPI specification format.

` repeated .google.protobuf.Struct class_methods = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` |   
  
### getClassMethodsCount()
    
    
    public abstract int getClassMethodsCount()

Optional. Declarations for object class methods in OpenAPI specification format.

` repeated .google.protobuf.Struct class_methods = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getClassMethodsList()
    
    
    public abstract List<Struct> getClassMethodsList()

Optional. Declarations for object class methods in OpenAPI specification format.

` repeated .google.protobuf.Struct class_methods = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### getClassMethodsOrBuilder(int index)
    
    
    public abstract StructOrBuilder getClassMethodsOrBuilder(int index)

Optional. Declarations for object class methods in OpenAPI specification format.

` repeated .google.protobuf.Struct class_methods = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getClassMethodsOrBuilderList()
    
    
    public abstract List<? extends StructOrBuilder> getClassMethodsOrBuilderList()

Optional. Declarations for object class methods in OpenAPI specification format.

` repeated .google.protobuf.Struct class_methods = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.StructOrBuilder>` |   
  
### getContainerSpec()
    
    
    public abstract ReasoningEngineSpec.ContainerSpec getContainerSpec()

Deploy from a container image with a defined entrypoint and commands.

`.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.ContainerSpec container_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.ContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.ContainerSpec)` | The containerSpec.  
  
### getContainerSpecOrBuilder()
    
    
    public abstract ReasoningEngineSpec.ContainerSpecOrBuilder getContainerSpecOrBuilder()

Deploy from a container image with a defined entrypoint and commands.

`.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.ContainerSpec container_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.ContainerSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.ContainerSpecOrBuilder)` |   
  
### getDeploymentSourceCase()
    
    
    public abstract ReasoningEngineSpec.DeploymentSourceCase getDeploymentSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.DeploymentSourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.DeploymentSourceCase)` |   
  
### getDeploymentSpec()
    
    
    public abstract ReasoningEngineSpec.DeploymentSpec getDeploymentSpec()

Optional. The specification of a Reasoning Engine deployment.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.DeploymentSpec deployment_spec = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.DeploymentSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.DeploymentSpec)` | The deploymentSpec.  
  
### getDeploymentSpecOrBuilder()
    
    
    public abstract ReasoningEngineSpec.DeploymentSpecOrBuilder getDeploymentSpecOrBuilder()

Optional. The specification of a Reasoning Engine deployment.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.DeploymentSpec deployment_spec = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.DeploymentSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.DeploymentSpecOrBuilder)` |   
  
### getIdentityType()
    
    
    public abstract ReasoningEngineSpec.IdentityType getIdentityType()

Optional. The identity type to use for the Reasoning Engine. If not specified, the `service_account` field will be used if set, otherwise the default Vertex AI Reasoning Engine Service Agent in the project will be used.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.IdentityType identity_type = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.IdentityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.IdentityType)` | The identityType.  
  
### getIdentityTypeValue()
    
    
    public abstract int getIdentityTypeValue()

Optional. The identity type to use for the Reasoning Engine. If not specified, the `service_account` field will be used if set, otherwise the default Vertex AI Reasoning Engine Service Agent in the project will be used.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.IdentityType identity_type = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for identityType.  
  
### getPackageSpec()
    
    
    public abstract ReasoningEngineSpec.PackageSpec getPackageSpec()

Optional. User provided package spec of the ReasoningEngine. Ignored when users directly specify a deployment image through `deployment_spec.first_party_image_override`, but keeping the field_behavior to avoid introducing breaking changes. The `deployment_source` field should not be set if `package_spec` is specified.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.PackageSpec package_spec = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.PackageSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.PackageSpec)` | The packageSpec.  
  
### getPackageSpecOrBuilder()
    
    
    public abstract ReasoningEngineSpec.PackageSpecOrBuilder getPackageSpecOrBuilder()

Optional. User provided package spec of the ReasoningEngine. Ignored when users directly specify a deployment image through `deployment_spec.first_party_image_override`, but keeping the field_behavior to avoid introducing breaking changes. The `deployment_source` field should not be set if `package_spec` is specified.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.PackageSpec package_spec = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.PackageSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.PackageSpecOrBuilder)` |   
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

Optional. The service account that the Reasoning Engine artifact runs as. It should have "roles/storage.objectViewer" for reading the user project's Cloud Storage and "roles/aiplatform.user" for using Vertex extensions. If not specified, the Vertex AI Reasoning Engine Service Agent in the project will be used.

`optional string service_account = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

Optional. The service account that the Reasoning Engine artifact runs as. It should have "roles/storage.objectViewer" for reading the user project's Cloud Storage and "roles/aiplatform.user" for using Vertex extensions. If not specified, the Vertex AI Reasoning Engine Service Agent in the project will be used.

`optional string service_account = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getSourceCodeSpec()
    
    
    public abstract ReasoningEngineSpec.SourceCodeSpec getSourceCodeSpec()

Deploy from source code files with a defined entrypoint.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.SourceCodeSpec source_code_spec = 11; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.SourceCodeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.SourceCodeSpec)` | The sourceCodeSpec.  
  
### getSourceCodeSpecOrBuilder()
    
    
    public abstract ReasoningEngineSpec.SourceCodeSpecOrBuilder getSourceCodeSpecOrBuilder()

Deploy from source code files with a defined entrypoint.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.SourceCodeSpec source_code_spec = 11; `

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineSpec.SourceCodeSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.SourceCodeSpecOrBuilder)` |   
  
### hasBuildSpec()
    
    
    public abstract boolean hasBuildSpec()

Optional. Configuration for building container image.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.BuildSpec build_spec = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the buildSpec field is set.  
  
### hasContainerSpec()
    
    
    public abstract boolean hasContainerSpec()

Deploy from a container image with a defined entrypoint and commands.

`.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.ContainerSpec container_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the containerSpec field is set.  
  
### hasDeploymentSpec()
    
    
    public abstract boolean hasDeploymentSpec()

Optional. The specification of a Reasoning Engine deployment.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.DeploymentSpec deployment_spec = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deploymentSpec field is set.  
  
### hasPackageSpec()
    
    
    public abstract boolean hasPackageSpec()

Optional. User provided package spec of the ReasoningEngine. Ignored when users directly specify a deployment image through `deployment_spec.first_party_image_override`, but keeping the field_behavior to avoid introducing breaking changes. The `deployment_source` field should not be set if `package_spec` is specified.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.PackageSpec package_spec = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the packageSpec field is set.  
  
### hasServiceAccount()
    
    
    public abstract boolean hasServiceAccount()

Optional. The service account that the Reasoning Engine artifact runs as. It should have "roles/storage.objectViewer" for reading the user project's Cloud Storage and "roles/aiplatform.user" for using Vertex extensions. If not specified, the Vertex AI Reasoning Engine Service Agent in the project will be used.

`optional string service_account = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serviceAccount field is set.  
  
### hasSourceCodeSpec()
    
    
    public abstract boolean hasSourceCodeSpec()

Deploy from source code files with a defined entrypoint.

` .google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.SourceCodeSpec source_code_spec = 11; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceCodeSpec field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
