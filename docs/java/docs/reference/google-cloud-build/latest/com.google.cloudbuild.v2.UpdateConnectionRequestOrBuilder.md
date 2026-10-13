---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UpdateConnectionRequestOrBuilder
title: Interface UpdateConnectionRequestOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:36.570306+00:00
---

# Interface UpdateConnectionRequestOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UpdateConnectionRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdateConnectionRequestOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface UpdateConnectionRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllowMissing()
    
    
    public abstract boolean getAllowMissing()

If set to true, and the connection is not found a new connection will be created. In this situation `update_mask` is ignored. The creation will succeed only if the input connection has all the necessary information (e.g a github_config with both user_oauth_token and installation_id properties).

`bool allow_missing = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowMissing.  
  
### getConnection()
    
    
    public abstract Connection getConnection()

Required. The Connection to update.

` .google.devtools.cloudbuild.v2.Connection connection = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Connection)` | The connection.  
  
### getConnectionOrBuilder()
    
    
    public abstract ConnectionOrBuilder getConnectionOrBuilder()

Required. The Connection to update.

` .google.devtools.cloudbuild.v2.Connection connection = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ConnectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ConnectionOrBuilder)` |   
  
### getEtag()
    
    
    public abstract String getEtag()

The current etag of the connection. If an etag is provided and does not match the current etag of the connection, update will be blocked and an ABORTED error will be returned.

`string etag = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

The current etag of the connection. If an etag is provided and does not match the current etag of the connection, update will be blocked and an ABORTED error will be returned.

`string etag = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

The list of fields to be updated.

`.google.protobuf.FieldMask update_mask = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

The list of fields to be updated.

`.google.protobuf.FieldMask update_mask = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### hasConnection()
    
    
    public abstract boolean hasConnection()

Required. The Connection to update.

` .google.devtools.cloudbuild.v2.Connection connection = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the connection field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

The list of fields to be updated.

`.google.protobuf.FieldMask update_mask = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
