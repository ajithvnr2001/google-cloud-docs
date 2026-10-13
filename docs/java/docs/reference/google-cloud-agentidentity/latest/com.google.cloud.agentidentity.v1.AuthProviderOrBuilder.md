---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderOrBuilder
title: Interface AuthProviderOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:55.070489+00:00
---

# Interface AuthProviderOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AuthProviderOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface AuthProviderOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Labels as key value pairs

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowedScopes(int index)
    
    
    public abstract String getAllowedScopes(int index)

Optional. List of scopes that are allowed to be requested for this auth_provider. If this list is non-empty, only scopes within this list may be requested. If this list is empty, all scopes may be requested. Scopes appearing in `blocked_scopes` are disallowed even if they appear in `allowed_scopes`. The number of allowed scopes is limited to 200.

`repeated string allowed_scopes = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowedScopes at the given index.  
  
### getAllowedScopesBytes(int index)
    
    
    public abstract ByteString getAllowedScopesBytes(int index)

Optional. List of scopes that are allowed to be requested for this auth_provider. If this list is non-empty, only scopes within this list may be requested. If this list is empty, all scopes may be requested. Scopes appearing in `blocked_scopes` are disallowed even if they appear in `allowed_scopes`. The number of allowed scopes is limited to 200.

`repeated string allowed_scopes = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the allowedScopes at the given index.  
  
### getAllowedScopesCount()
    
    
    public abstract int getAllowedScopesCount()

Optional. List of scopes that are allowed to be requested for this auth_provider. If this list is non-empty, only scopes within this list may be requested. If this list is empty, all scopes may be requested. Scopes appearing in `blocked_scopes` are disallowed even if they appear in `allowed_scopes`. The number of allowed scopes is limited to 200.

`repeated string allowed_scopes = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of allowedScopes.  
  
### getAllowedScopesList()
    
    
    public abstract List<String> getAllowedScopesList()

Optional. List of scopes that are allowed to be requested for this auth_provider. If this list is non-empty, only scopes within this list may be requested. If this list is empty, all scopes may be requested. Scopes appearing in `blocked_scopes` are disallowed even if they appear in `allowed_scopes`. The number of allowed scopes is limited to 200.

`repeated string allowed_scopes = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the allowedScopes.  
  
### getAuthProviderTypeParams()
    
    
    public abstract AuthProvider.AuthProviderTypeParams getAuthProviderTypeParams()

Required. AuthProvider type specific parameters.

` .google.cloud.agentidentity.v1.AuthProvider.AuthProviderTypeParams auth_provider_type_params = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AuthProvider.AuthProviderTypeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider.AuthProviderTypeParams)` | The authProviderTypeParams.  
  
### getAuthProviderTypeParamsOrBuilder()
    
    
    public abstract AuthProvider.AuthProviderTypeParamsOrBuilder getAuthProviderTypeParamsOrBuilder()

Required. AuthProvider type specific parameters.

` .google.cloud.agentidentity.v1.AuthProvider.AuthProviderTypeParams auth_provider_type_params = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AuthProvider.AuthProviderTypeParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider.AuthProviderTypeParamsOrBuilder)` |   
  
### getBlockedScopes(int index)
    
    
    public abstract String getBlockedScopes(int index)

Optional. List of scopes that are blocked from being requested for this auth_provider. If a scope appears in this list, it will not be requested, even if it also appears in `allowed_scopes`. `blocked_scopes` takes precedence over `allowed_scopes`. The number of blocked scopes is limited to 200.

`repeated string blocked_scopes = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The blockedScopes at the given index.  
  
### getBlockedScopesBytes(int index)
    
    
    public abstract ByteString getBlockedScopesBytes(int index)

Optional. List of scopes that are blocked from being requested for this auth_provider. If a scope appears in this list, it will not be requested, even if it also appears in `allowed_scopes`. `blocked_scopes` takes precedence over `allowed_scopes`. The number of blocked scopes is limited to 200.

`repeated string blocked_scopes = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the blockedScopes at the given index.  
  
### getBlockedScopesCount()
    
    
    public abstract int getBlockedScopesCount()

Optional. List of scopes that are blocked from being requested for this auth_provider. If a scope appears in this list, it will not be requested, even if it also appears in `allowed_scopes`. `blocked_scopes` takes precedence over `allowed_scopes`. The number of blocked scopes is limited to 200.

`repeated string blocked_scopes = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of blockedScopes.  
  
### getBlockedScopesList()
    
    
    public abstract List<String> getBlockedScopesList()

Optional. List of scopes that are blocked from being requested for this auth_provider. If a scope appears in this list, it will not be requested, even if it also appears in `allowed_scopes`. `blocked_scopes` takes precedence over `allowed_scopes`. The number of blocked scopes is limited to 200.

`repeated string blocked_scopes = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the blockedScopes.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. [Output only] Create time stamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. [Output only] Create time stamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDeleted()
    
    
    public abstract boolean getDeleted()

Output only. This is set to true if the auth_provider is deleted.

`bool deleted = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The deleted.  
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Description of the resource. Must be less than 256 characters.

`string description = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description of the resource. Must be less than 256 characters.

`string description = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getExpireTime()
    
    
    public abstract Timestamp getExpireTime()

Output only. The time when the auth_provider will expire.

`.google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The expireTime.  
  
### getExpireTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getExpireTimeOrBuilder()

Output only. The time when the auth_provider will expire.

`.google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderOrBuilder#com_google_cloud_agentidentity_v1_AuthProviderOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Labels as key value pairs

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Labels as key value pairs

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels as key value pairs

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. Labels as key value pairs

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

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

Identifier. The full resource name of the auth_provider. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The full resource name of the auth_provider. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getState()
    
    
    public abstract AuthProvider.State getState()

Output only. The state of the auth_provider.

` .google.cloud.agentidentity.v1.AuthProvider.State state = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AuthProvider.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The state of the auth_provider.

` .google.cloud.agentidentity.v1.AuthProvider.State state = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. [Output only] Update time stamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. [Output only] Update time stamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getWorkloadIds(int index)
    
    
    public abstract String getWorkloadIds(int index)

Optional. Input only. Represents the workload identity in IAM `principal://` format of the agent(s) that will use this AuthProvider. Example: `principal://agents.global.org-${ORG_ID}.system.id.goog/resources/aiplatform/projects/{PROJECT_ID}/locations/{LOCATIONS}/reasoningEngines/{ID}`

` repeated string workload_ids = 12 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The workloadIds at the given index.  
  
### getWorkloadIdsBytes(int index)
    
    
    public abstract ByteString getWorkloadIdsBytes(int index)

Optional. Input only. Represents the workload identity in IAM `principal://` format of the agent(s) that will use this AuthProvider. Example: `principal://agents.global.org-${ORG_ID}.system.id.goog/resources/aiplatform/projects/{PROJECT_ID}/locations/{LOCATIONS}/reasoningEngines/{ID}`

` repeated string workload_ids = 12 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the workloadIds at the given index.  
  
### getWorkloadIdsCount()
    
    
    public abstract int getWorkloadIdsCount()

Optional. Input only. Represents the workload identity in IAM `principal://` format of the agent(s) that will use this AuthProvider. Example: `principal://agents.global.org-${ORG_ID}.system.id.goog/resources/aiplatform/projects/{PROJECT_ID}/locations/{LOCATIONS}/reasoningEngines/{ID}`

` repeated string workload_ids = 12 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of workloadIds.  
  
### getWorkloadIdsList()
    
    
    public abstract List<String> getWorkloadIdsList()

Optional. Input only. Represents the workload identity in IAM `principal://` format of the agent(s) that will use this AuthProvider. Example: `principal://agents.global.org-${ORG_ID}.system.id.goog/resources/aiplatform/projects/{PROJECT_ID}/locations/{LOCATIONS}/reasoningEngines/{ID}`

` repeated string workload_ids = 12 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the workloadIds.  
  
### hasAuthProviderTypeParams()
    
    
    public abstract boolean hasAuthProviderTypeParams()

Required. AuthProvider type specific parameters.

` .google.cloud.agentidentity.v1.AuthProvider.AuthProviderTypeParams auth_provider_type_params = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the authProviderTypeParams field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. [Output only] Create time stamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasExpireTime()
    
    
    public abstract boolean hasExpireTime()

Output only. The time when the auth_provider will expire.

`.google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expireTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. [Output only] Update time stamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
