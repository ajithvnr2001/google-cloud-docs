---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfigOrBuilder
title: Interface ServerConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:58.091259+00:00
---

# Interface ServerConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ServerConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface ServerConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChannels(int index)
    
    
    public abstract ServerConfig.ReleaseChannelConfig getChannels(int index)

List of release channel configurations.

`repeated .google.container.v1.ServerConfig.ReleaseChannelConfig channels = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServerConfig.ReleaseChannelConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig.ReleaseChannelConfig)` |   
  
### getChannelsCount()
    
    
    public abstract int getChannelsCount()

List of release channel configurations.

`repeated .google.container.v1.ServerConfig.ReleaseChannelConfig channels = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getChannelsList()
    
    
    public abstract List<ServerConfig.ReleaseChannelConfig> getChannelsList()

List of release channel configurations.

`repeated .google.container.v1.ServerConfig.ReleaseChannelConfig channels = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ReleaseChannelConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig.ReleaseChannelConfig)>` |   
  
### getChannelsOrBuilder(int index)
    
    
    public abstract ServerConfig.ReleaseChannelConfigOrBuilder getChannelsOrBuilder(int index)

List of release channel configurations.

`repeated .google.container.v1.ServerConfig.ReleaseChannelConfig channels = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServerConfig.ReleaseChannelConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig.ReleaseChannelConfigOrBuilder)` |   
  
### getChannelsOrBuilderList()
    
    
    public abstract List<? extends ServerConfig.ReleaseChannelConfigOrBuilder> getChannelsOrBuilderList()

List of release channel configurations.

`repeated .google.container.v1.ServerConfig.ReleaseChannelConfig channels = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.ServerConfig.ReleaseChannelConfigOrBuilder>` |   
  
### getDefaultClusterVersion()
    
    
    public abstract String getDefaultClusterVersion()

Version of Kubernetes the service deploys by default.

`string default_cluster_version = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The defaultClusterVersion.  
  
### getDefaultClusterVersionBytes()
    
    
    public abstract ByteString getDefaultClusterVersionBytes()

Version of Kubernetes the service deploys by default.

`string default_cluster_version = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for defaultClusterVersion.  
  
### getDefaultImageType()
    
    
    public abstract String getDefaultImageType()

Default image type.

`string default_image_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The defaultImageType.  
  
### getDefaultImageTypeBytes()
    
    
    public abstract ByteString getDefaultImageTypeBytes()

Default image type.

`string default_image_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for defaultImageType.  
  
### getValidImageTypes(int index)
    
    
    public abstract String getValidImageTypes(int index)

List of valid image types.

`repeated string valid_image_types = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The validImageTypes at the given index.  
  
### getValidImageTypesBytes(int index)
    
    
    public abstract ByteString getValidImageTypesBytes(int index)

List of valid image types.

`repeated string valid_image_types = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the validImageTypes at the given index.  
  
### getValidImageTypesCount()
    
    
    public abstract int getValidImageTypesCount()

List of valid image types.

`repeated string valid_image_types = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of validImageTypes.  
  
### getValidImageTypesList()
    
    
    public abstract List<String> getValidImageTypesList()

List of valid image types.

`repeated string valid_image_types = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the validImageTypes.  
  
### getValidMasterVersions(int index)
    
    
    public abstract String getValidMasterVersions(int index)

List of valid master versions, in descending order.

`repeated string valid_master_versions = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The validMasterVersions at the given index.  
  
### getValidMasterVersionsBytes(int index)
    
    
    public abstract ByteString getValidMasterVersionsBytes(int index)

List of valid master versions, in descending order.

`repeated string valid_master_versions = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the validMasterVersions at the given index.  
  
### getValidMasterVersionsCount()
    
    
    public abstract int getValidMasterVersionsCount()

List of valid master versions, in descending order.

`repeated string valid_master_versions = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of validMasterVersions.  
  
### getValidMasterVersionsList()
    
    
    public abstract List<String> getValidMasterVersionsList()

List of valid master versions, in descending order.

`repeated string valid_master_versions = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the validMasterVersions.  
  
### getValidNodeVersions(int index)
    
    
    public abstract String getValidNodeVersions(int index)

List of valid node upgrade target versions, in descending order.

`repeated string valid_node_versions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The validNodeVersions at the given index.  
  
### getValidNodeVersionsBytes(int index)
    
    
    public abstract ByteString getValidNodeVersionsBytes(int index)

List of valid node upgrade target versions, in descending order.

`repeated string valid_node_versions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the validNodeVersions at the given index.  
  
### getValidNodeVersionsCount()
    
    
    public abstract int getValidNodeVersionsCount()

List of valid node upgrade target versions, in descending order.

`repeated string valid_node_versions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of validNodeVersions.  
  
### getValidNodeVersionsList()
    
    
    public abstract List<String> getValidNodeVersionsList()

List of valid node upgrade target versions, in descending order.

`repeated string valid_node_versions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the validNodeVersions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
