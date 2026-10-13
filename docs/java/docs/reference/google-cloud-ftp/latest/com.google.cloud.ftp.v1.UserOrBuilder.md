---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserOrBuilder
title: Interface UserOrBuilder (0.4.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:06.422400+00:00
---

# Interface UserOrBuilder (0.4.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UserOrBuilder (0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface UserOrBuilder extends MessageOrBuilder

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
  
### getCustomerServiceAccount()
    
    
    public abstract String getCustomerServiceAccount()

Required. Service account in customer project attached to this SFTP User.

`string customer_service_account = 7 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customerServiceAccount.  
  
### getCustomerServiceAccountBytes()
    
    
    public abstract ByteString getCustomerServiceAccountBytes()

Required. Service account in customer project attached to this SFTP User.

`string customer_service_account = 7 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customerServiceAccount.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserOrBuilder#com_google_cloud_ftp_v1_UserOrBuilder_getLabelsMap__) instead.

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

Identifier. User-friendly name via which User will be identified. projects/{project}/locations/{location}/servers/{server}/users/{user}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. User-friendly name via which User will be identified. projects/{project}/locations/{location}/servers/{server}/users/{user}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getState()
    
    
    public abstract User.State getState()

Output only. Tracks user creation.

`.google.cloud.ftp.v1.User.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[User.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. Tracks user creation.

`.google.cloud.ftp.v1.User.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getStorageDirectoryMappings(int index)
    
    
    public abstract StorageDirectoryMapping getStorageDirectoryMappings(int index)

Required. Mapping of Cloud Storage buckets to directories where the user will land in the SFTP server.

` repeated .google.cloud.ftp.v1.StorageDirectoryMapping storage_directory_mappings = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageDirectoryMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.StorageDirectoryMapping)` |   
  
### getStorageDirectoryMappingsCount()
    
    
    public abstract int getStorageDirectoryMappingsCount()

Required. Mapping of Cloud Storage buckets to directories where the user will land in the SFTP server.

` repeated .google.cloud.ftp.v1.StorageDirectoryMapping storage_directory_mappings = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStorageDirectoryMappingsList()
    
    
    public abstract List<StorageDirectoryMapping> getStorageDirectoryMappingsList()

Required. Mapping of Cloud Storage buckets to directories where the user will land in the SFTP server.

` repeated .google.cloud.ftp.v1.StorageDirectoryMapping storage_directory_mappings = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StorageDirectoryMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.StorageDirectoryMapping)>` |   
  
### getStorageDirectoryMappingsOrBuilder(int index)
    
    
    public abstract StorageDirectoryMappingOrBuilder getStorageDirectoryMappingsOrBuilder(int index)

Required. Mapping of Cloud Storage buckets to directories where the user will land in the SFTP server.

` repeated .google.cloud.ftp.v1.StorageDirectoryMapping storage_directory_mappings = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageDirectoryMappingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.StorageDirectoryMappingOrBuilder)` |   
  
### getStorageDirectoryMappingsOrBuilderList()
    
    
    public abstract List<? extends StorageDirectoryMappingOrBuilder> getStorageDirectoryMappingsOrBuilderList()

Required. Mapping of Cloud Storage buckets to directories where the user will land in the SFTP server.

` repeated .google.cloud.ftp.v1.StorageDirectoryMapping storage_directory_mappings = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.ftp.v1.StorageDirectoryMappingOrBuilder>` |   
  
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
  
### getUserCredentials(int index)
    
    
    public abstract UserCredential getUserCredentials(int index)

Required. User credential for the user. The maximum number of user credentials is 10.

` repeated .google.cloud.ftp.v1.UserCredential user_credentials = 9 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserCredential](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserCredential)` |   
  
### getUserCredentialsCount()
    
    
    public abstract int getUserCredentialsCount()

Required. User credential for the user. The maximum number of user credentials is 10.

` repeated .google.cloud.ftp.v1.UserCredential user_credentials = 9 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUserCredentialsList()
    
    
    public abstract List<UserCredential> getUserCredentialsList()

Required. User credential for the user. The maximum number of user credentials is 10.

` repeated .google.cloud.ftp.v1.UserCredential user_credentials = 9 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UserCredential](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserCredential)>` |   
  
### getUserCredentialsOrBuilder(int index)
    
    
    public abstract UserCredentialOrBuilder getUserCredentialsOrBuilder(int index)

Required. User credential for the user. The maximum number of user credentials is 10.

` repeated .google.cloud.ftp.v1.UserCredential user_credentials = 9 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserCredentialOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserCredentialOrBuilder)` |   
  
### getUserCredentialsOrBuilderList()
    
    
    public abstract List<? extends UserCredentialOrBuilder> getUserCredentialsOrBuilderList()

Required. User credential for the user. The maximum number of user credentials is 10.

` repeated .google.cloud.ftp.v1.UserCredential user_credentials = 9 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.ftp.v1.UserCredentialOrBuilder>` |   
  
### getUsername()
    
    
    public abstract String getUsername()

Output only. [Output only] The username of the user.

`string username = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The username.  
  
### getUsernameBytes()
    
    
    public abstract ByteString getUsernameBytes()

Output only. [Output only] The username of the user.

`string username = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for username.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. [Output only] Create time stamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
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

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
