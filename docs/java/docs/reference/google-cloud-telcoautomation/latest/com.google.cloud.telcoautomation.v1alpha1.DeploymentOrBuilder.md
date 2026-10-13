---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.DeploymentOrBuilder
title: Interface DeploymentOrBuilder (0.69.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:14.347182+00:00
---

# Interface DeploymentOrBuilder (0.69.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.DeploymentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DeploymentOrBuilder (0.69.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.69.0 (latest)  0.65.0  0.64.0  0.63.0  0.61.0  0.58.0  0.57.0  0.55.0  0.53.0  0.52.0  0.50.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.34.0  0.33.0  0.32.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DeploymentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Labels are key-value attributes that can be set on a deployment resource by the user.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Deployment creation time.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Deployment creation time.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDeploymentLevel()
    
    
    public abstract DeploymentLevel getDeploymentLevel()

Output only. Attributes to where the deployment can inflict changes. The value can only be [SINGLE_DEPLOYMENT, MULTI_DEPLOYMENT].

` .google.cloud.telcoautomation.v1alpha1.DeploymentLevel deployment_level = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DeploymentLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.DeploymentLevel)` | The deploymentLevel.  
  
### getDeploymentLevelValue()
    
    
    public abstract int getDeploymentLevelValue()

Output only. Attributes to where the deployment can inflict changes. The value can only be [SINGLE_DEPLOYMENT, MULTI_DEPLOYMENT].

` .google.cloud.telcoautomation.v1alpha1.DeploymentLevel deployment_level = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for deploymentLevel.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. Human readable name of a Deployment.

`string display_name = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. Human readable name of a Deployment.

`string display_name = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getFiles(int index)
    
    
    public abstract File getFiles(int index)

Optional. Files present in a deployment. When invoking UpdateDeployment API, only the modified files should be included in this. Files that are not included in the update of a deployment will not be changed.

` repeated .google.cloud.telcoautomation.v1alpha1.File files = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[File](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.File)` |   
  
### getFilesCount()
    
    
    public abstract int getFilesCount()

Optional. Files present in a deployment. When invoking UpdateDeployment API, only the modified files should be included in this. Files that are not included in the update of a deployment will not be changed.

` repeated .google.cloud.telcoautomation.v1alpha1.File files = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFilesList()
    
    
    public abstract List<File> getFilesList()

Optional. Files present in a deployment. When invoking UpdateDeployment API, only the modified files should be included in this. Files that are not included in the update of a deployment will not be changed.

` repeated .google.cloud.telcoautomation.v1alpha1.File files = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[File](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.File)>` |   
  
### getFilesOrBuilder(int index)
    
    
    public abstract FileOrBuilder getFilesOrBuilder(int index)

Optional. Files present in a deployment. When invoking UpdateDeployment API, only the modified files should be included in this. Files that are not included in the update of a deployment will not be changed.

` repeated .google.cloud.telcoautomation.v1alpha1.File files = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.FileOrBuilder)` |   
  
### getFilesOrBuilderList()
    
    
    public abstract List<? extends FileOrBuilder> getFilesOrBuilderList()

Optional. Files present in a deployment. When invoking UpdateDeployment API, only the modified files should be included in this. Files that are not included in the update of a deployment will not be changed.

` repeated .google.cloud.telcoautomation.v1alpha1.File files = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.telcoautomation.v1alpha1.FileOrBuilder>` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.DeploymentOrBuilder#com_google_cloud_telcoautomation_v1alpha1_DeploymentOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Labels are key-value attributes that can be set on a deployment resource by the user.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Labels are key-value attributes that can be set on a deployment resource by the user.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels are key-value attributes that can be set on a deployment resource by the user.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. Labels are key-value attributes that can be set on a deployment resource by the user.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

The name of the deployment.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The name of the deployment.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRepository()
    
    
    public abstract String getRepository()

Output only. Name of the repository where the deployment package files are stored.

`string repository = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The repository.  
  
### getRepositoryBytes()
    
    
    public abstract ByteString getRepositoryBytes()

Output only. Name of the repository where the deployment package files are stored.

`string repository = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for repository.  
  
### getRevisionCreateTime()
    
    
    public abstract Timestamp getRevisionCreateTime()

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The revisionCreateTime.  
  
### getRevisionCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getRevisionCreateTimeOrBuilder()

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getRevisionId()
    
    
    public abstract String getRevisionId()

Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever a change in deployment is applied.

` string revision_id = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The revisionId.  
  
### getRevisionIdBytes()
    
    
    public abstract ByteString getRevisionIdBytes()

Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever a change in deployment is applied.

` string revision_id = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for revisionId.  
  
### getRollbackSupport()
    
    
    public abstract boolean getRollbackSupport()

Output only. Indicates if the deployment can be rolled back, exported from public blueprint.

`bool rollback_support = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The rollbackSupport.  
  
### getSourceBlueprintRevision()
    
    
    public abstract String getSourceBlueprintRevision()

Required. The blueprint revision from which this deployment was created.

`string source_blueprint_revision = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceBlueprintRevision.  
  
### getSourceBlueprintRevisionBytes()
    
    
    public abstract ByteString getSourceBlueprintRevisionBytes()

Required. The blueprint revision from which this deployment was created.

`string source_blueprint_revision = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceBlueprintRevision.  
  
### getSourceProvider()
    
    
    public abstract String getSourceProvider()

Output only. Source provider is the author of a public blueprint, from which this deployment is created.

`string source_provider = 12 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceProvider.  
  
### getSourceProviderBytes()
    
    
    public abstract ByteString getSourceProviderBytes()

Output only. Source provider is the author of a public blueprint, from which this deployment is created.

`string source_provider = 12 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceProvider.  
  
### getState()
    
    
    public abstract Deployment.State getState()

Output only. State of the deployment (DRAFT, APPLIED, DELETING).

` .google.cloud.telcoautomation.v1alpha1.Deployment.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Deployment.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.Deployment.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. State of the deployment (DRAFT, APPLIED, DELETING).

` .google.cloud.telcoautomation.v1alpha1.Deployment.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The timestamp when the deployment was updated.

`.google.protobuf.Timestamp update_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when the deployment was updated.

`.google.protobuf.Timestamp update_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getWorkloadCluster()
    
    
    public abstract String getWorkloadCluster()

Optional. Immutable. The WorkloadCluster on which to create the Deployment. This field should only be passed when the deployment_level of the source blueprint specifies deployments on workload clusters e.g. WORKLOAD_CLUSTER_DEPLOYMENT.

` string workload_cluster = 13 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The workloadCluster.  
  
### getWorkloadClusterBytes()
    
    
    public abstract ByteString getWorkloadClusterBytes()

Optional. Immutable. The WorkloadCluster on which to create the Deployment. This field should only be passed when the deployment_level of the source blueprint specifies deployments on workload clusters e.g. WORKLOAD_CLUSTER_DEPLOYMENT.

` string workload_cluster = 13 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for workloadCluster.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Deployment creation time.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasRevisionCreateTime()
    
    
    public abstract boolean hasRevisionCreateTime()

Output only. The timestamp that the revision was created.

` .google.protobuf.Timestamp revision_create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the revisionCreateTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The timestamp when the deployment was updated.

`.google.protobuf.Timestamp update_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
