---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.TargetOrBuilder
title: Interface TargetOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:28.202120+00:00
---

# Interface TargetOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.TargetOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TargetOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.TargetOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.deploy.v1.TargetOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.deploy.v1.TargetOrBuilder)


    
    
    public interface TargetOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsAnnotations(String key)
    
    
    public abstract boolean containsAnnotations(String key)

Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.

`map<string, string> annotations = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsDeployParameters(String key)
    
    
    public abstract boolean containsDeployParameters(String key)

Optional. The deploy parameters to use for this target.

`map<string, string> deploy_parameters = 20;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes.



`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotations()
    
    
    public abstract Map<String,String> getAnnotations()

Use [#getAnnotationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.TargetOrBuilder#com_google_events_cloud_deploy_v1_TargetOrBuilder_getAnnotationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsCount()
    
    
    public abstract int getAnnotationsCount()

Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.

`map<string, string> annotations = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsMap()
    
    
    public abstract Map<String,String> getAnnotationsMap()

Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.

`map<string, string> annotations = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsOrDefault(String key, String defaultValue)
    
    
    public abstract String getAnnotationsOrDefault(String key, String defaultValue)

Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.

`map<string, string> annotations = 5;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnnotationsOrThrow(String key)
    
    
    public abstract String getAnnotationsOrThrow(String key)

Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.

`map<string, string> annotations = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnthosCluster()
    
    
    public abstract AnthosCluster getAnthosCluster()

Optional. Information specifying an Anthos Cluster.

`.google.events.cloud.deploy.v1.AnthosCluster anthos_cluster = 17;`

**Returns**  
---  
**Type** | **Description**  
`[AnthosCluster](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.AnthosCluster)` | The anthosCluster.  
  
### getAnthosClusterOrBuilder()
    
    
    public abstract AnthosClusterOrBuilder getAnthosClusterOrBuilder()

Optional. Information specifying an Anthos Cluster.

`.google.events.cloud.deploy.v1.AnthosCluster anthos_cluster = 17;`

**Returns**  
---  
**Type** | **Description**  
`[AnthosClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.AnthosClusterOrBuilder)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time at which the `Target` was created.

`.google.protobuf.Timestamp create_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time at which the `Target` was created.

`.google.protobuf.Timestamp create_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCustomTarget()
    
    
    public abstract CustomTarget getCustomTarget()

Optional. Information specifying a Custom Target.

`.google.events.cloud.deploy.v1.CustomTarget custom_target = 21;`

**Returns**  
---  
**Type** | **Description**  
`[CustomTarget](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CustomTarget)` | The customTarget.  
  
### getCustomTargetOrBuilder()
    
    
    public abstract CustomTargetOrBuilder getCustomTargetOrBuilder()

Optional. Information specifying a Custom Target.

`.google.events.cloud.deploy.v1.CustomTarget custom_target = 21;`

**Returns**  
---  
**Type** | **Description**  
`[CustomTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CustomTargetOrBuilder)` |   
  
### getDeployParameters()
    
    
    public abstract Map<String,String> getDeployParameters()

Use [#getDeployParametersMap()](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.TargetOrBuilder#com_google_events_cloud_deploy_v1_TargetOrBuilder_getDeployParametersMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getDeployParametersCount()
    
    
    public abstract int getDeployParametersCount()

Optional. The deploy parameters to use for this target.

`map<string, string> deploy_parameters = 20;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDeployParametersMap()
    
    
    public abstract Map<String,String> getDeployParametersMap()

Optional. The deploy parameters to use for this target.

`map<string, string> deploy_parameters = 20;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getDeployParametersOrDefault(String key, String defaultValue)
    
    
    public abstract String getDeployParametersOrDefault(String key, String defaultValue)

Optional. The deploy parameters to use for this target.

`map<string, string> deploy_parameters = 20;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDeployParametersOrThrow(String key)
    
    
    public abstract String getDeployParametersOrThrow(String key)

Optional. The deploy parameters to use for this target.

`map<string, string> deploy_parameters = 20;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDeploymentTargetCase()
    
    
    public abstract Target.DeploymentTargetCase getDeploymentTargetCase()

**Returns**  
---  
**Type** | **Description**  
`[Target.DeploymentTargetCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.Target.DeploymentTargetCase)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Description of the `Target`. Max length is 255 characters.

`string description = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description of the `Target`. Max length is 255 characters.

`string description = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getEtag()
    
    
    public abstract String getEtag()

Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.

`string etag = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.

`string etag = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getExecutionConfigs(int index)
    
    
    public abstract ExecutionConfig getExecutionConfigs(int index)

Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`.

`repeated .google.events.cloud.deploy.v1.ExecutionConfig execution_configs = 16;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExecutionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.ExecutionConfig)` |   
  
### getExecutionConfigsCount()
    
    
    public abstract int getExecutionConfigsCount()

Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`.

`repeated .google.events.cloud.deploy.v1.ExecutionConfig execution_configs = 16;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExecutionConfigsList()
    
    
    public abstract List<ExecutionConfig> getExecutionConfigsList()

Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`.

`repeated .google.events.cloud.deploy.v1.ExecutionConfig execution_configs = 16;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ExecutionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.ExecutionConfig)>` |   
  
### getExecutionConfigsOrBuilder(int index)
    
    
    public abstract ExecutionConfigOrBuilder getExecutionConfigsOrBuilder(int index)

Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`.

`repeated .google.events.cloud.deploy.v1.ExecutionConfig execution_configs = 16;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExecutionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.ExecutionConfigOrBuilder)` |   
  
### getExecutionConfigsOrBuilderList()
    
    
    public abstract List<? extends ExecutionConfigOrBuilder> getExecutionConfigsOrBuilderList()

Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`.

`repeated .google.events.cloud.deploy.v1.ExecutionConfig execution_configs = 16;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.events.cloud.deploy.v1.ExecutionConfigOrBuilder>` |   
  
### getGke()
    
    
    public abstract GkeCluster getGke()

Optional. Information specifying a GKE Cluster.

`.google.events.cloud.deploy.v1.GkeCluster gke = 15;`

**Returns**  
---  
**Type** | **Description**  
`[GkeCluster](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.GkeCluster)` | The gke.  
  
### getGkeOrBuilder()
    
    
    public abstract GkeClusterOrBuilder getGkeOrBuilder()

Optional. Information specifying a GKE Cluster.

`.google.events.cloud.deploy.v1.GkeCluster gke = 15;`

**Returns**  
---  
**Type** | **Description**  
`[GkeClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.GkeClusterOrBuilder)` |   
  
### getLabels()
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.TargetOrBuilder#com_google_events_cloud_deploy_v1_TargetOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes.



`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes.



`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes.



`map<string, string> labels = 6;`

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

Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes.



`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMultiTarget()
    
    
    public abstract MultiTarget getMultiTarget()

Optional. Information specifying a multiTarget.

`.google.events.cloud.deploy.v1.MultiTarget multi_target = 19;`

**Returns**  
---  
**Type** | **Description**  
`[MultiTarget](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.MultiTarget)` | The multiTarget.  
  
### getMultiTargetOrBuilder()
    
    
    public abstract MultiTargetOrBuilder getMultiTargetOrBuilder()

Optional. Information specifying a multiTarget.

`.google.events.cloud.deploy.v1.MultiTarget multi_target = 19;`

**Returns**  
---  
**Type** | **Description**  
`[MultiTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.MultiTargetOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Optional. Name of the `Target`. Format is `projects/{project}/locations/{location}/targets/a-z{0,62}`.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Optional. Name of the `Target`. Format is `projects/{project}/locations/{location}/targets/a-z{0,62}`.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRequireApproval()
    
    
    public abstract boolean getRequireApproval()

Optional. Whether or not the `Target` requires approval.

`bool require_approval = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The requireApproval.  
  
### getRun()
    
    
    public abstract CloudRunLocation getRun()

Optional. Information specifying a Cloud Run deployment target.

`.google.events.cloud.deploy.v1.CloudRunLocation run = 18;`

**Returns**  
---  
**Type** | **Description**  
`[CloudRunLocation](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CloudRunLocation)` | The run.  
  
### getRunOrBuilder()
    
    
    public abstract CloudRunLocationOrBuilder getRunOrBuilder()

Optional. Information specifying a Cloud Run deployment target.

`.google.events.cloud.deploy.v1.CloudRunLocation run = 18;`

**Returns**  
---  
**Type** | **Description**  
`[CloudRunLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CloudRunLocationOrBuilder)` |   
  
### getTargetId()
    
    
    public abstract String getTargetId()

Output only. Resource id of the `Target`.

`string target_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetId.  
  
### getTargetIdBytes()
    
    
    public abstract ByteString getTargetIdBytes()

Output only. Resource id of the `Target`.

`string target_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetId.  
  
### getUid()
    
    
    public abstract String getUid()

Output only. Unique identifier of the `Target`.

`string uid = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. Unique identifier of the `Target`.

`string uid = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Most recent time at which the `Target` was updated.

`.google.protobuf.Timestamp update_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Most recent time at which the `Target` was updated.

`.google.protobuf.Timestamp update_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasAnthosCluster()
    
    
    public abstract boolean hasAnthosCluster()

Optional. Information specifying an Anthos Cluster.

`.google.events.cloud.deploy.v1.AnthosCluster anthos_cluster = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the anthosCluster field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time at which the `Target` was created.

`.google.protobuf.Timestamp create_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasCustomTarget()
    
    
    public abstract boolean hasCustomTarget()

Optional. Information specifying a Custom Target.

`.google.events.cloud.deploy.v1.CustomTarget custom_target = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customTarget field is set.  
  
### hasGke()
    
    
    public abstract boolean hasGke()

Optional. Information specifying a GKE Cluster.

`.google.events.cloud.deploy.v1.GkeCluster gke = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gke field is set.  
  
### hasMultiTarget()
    
    
    public abstract boolean hasMultiTarget()

Optional. Information specifying a multiTarget.

`.google.events.cloud.deploy.v1.MultiTarget multi_target = 19;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the multiTarget field is set.  
  
### hasRun()
    
    
    public abstract boolean hasRun()

Optional. Information specifying a Cloud Run deployment target.

`.google.events.cloud.deploy.v1.CloudRunLocation run = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the run field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Most recent time at which the `Target` was updated.

`.google.protobuf.Timestamp update_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
