---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.CustomNodeInit.InitScriptOrBuilder
title: Interface LinuxNodeConfig.CustomNodeInit.InitScriptOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:31.560581+00:00
---

# Interface LinuxNodeConfig.CustomNodeInit.InitScriptOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.CustomNodeInit.InitScriptOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LinuxNodeConfig.CustomNodeInit.InitScriptOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public static interface LinuxNodeConfig.CustomNodeInit.InitScriptOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArgs(int index)
    
    
    public abstract String getArgs(int index)

Optional. The optional arguments line to be passed to the init script.

`repeated string args = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The args at the given index.  
  
### getArgsBytes(int index)
    
    
    public abstract ByteString getArgsBytes(int index)

Optional. The optional arguments line to be passed to the init script.

`repeated string args = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the args at the given index.  
  
### getArgsCount()
    
    
    public abstract int getArgsCount()

Optional. The optional arguments line to be passed to the init script.

`repeated string args = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of args.  
  
### getArgsList()
    
    
    public abstract List<String> getArgsList()

Optional. The optional arguments line to be passed to the init script.

`repeated string args = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the args.  
  
### getGcpSecretManagerSecretUri()
    
    
    public abstract String getGcpSecretManagerSecretUri()

The resource name of the secret manager secret hosting the init script. Both global and regional secrets are supported with format below: Global secret: projects/{project}/secrets/{secret}/versions/{version} Regional secret: projects/{project}/locations/{location}/secrets/{secret}/versions/{version} Example: projects/1234567890/secrets/script_1/versions/1. Accept version number only, not support version alias. User can't configure both gcp_secret_manager_secret_uri and gcs_uri.

`string gcp_secret_manager_secret_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcpSecretManagerSecretUri.  
  
### getGcpSecretManagerSecretUriBytes()
    
    
    public abstract ByteString getGcpSecretManagerSecretUriBytes()

The resource name of the secret manager secret hosting the init script. Both global and regional secrets are supported with format below: Global secret: projects/{project}/secrets/{secret}/versions/{version} Regional secret: projects/{project}/locations/{location}/secrets/{secret}/versions/{version} Example: projects/1234567890/secrets/script_1/versions/1. Accept version number only, not support version alias. User can't configure both gcp_secret_manager_secret_uri and gcs_uri.

`string gcp_secret_manager_secret_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcpSecretManagerSecretUri.  
  
### getGcsGeneration()
    
    
    public abstract long getGcsGeneration()

The generation of the init script stored in Gloud Storage. This is the required field to identify the version of the init script. User can get the genetaion from `gcloud storage objects describe gs://BUCKET_NAME/OBJECT_NAME --format="value(generation)"` or from the "Version history" tab of the object in the Cloud Console UI.

`int64 gcs_generation = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The gcsGeneration.  
  
### getGcsUri()
    
    
    public abstract String getGcsUri()

The Cloud Storage URI for storing the init script. Format: gs://BUCKET_NAME/OBJECT_NAME The service account on the node pool must have read access to the object. User can't configure both gcs_uri and gcp_secret_manager_secret_uri.

`string gcs_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcsUri.  
  
### getGcsUriBytes()
    
    
    public abstract ByteString getGcsUriBytes()

The Cloud Storage URI for storing the init script. Format: gs://BUCKET_NAME/OBJECT_NAME The service account on the node pool must have read access to the object. User can't configure both gcs_uri and gcp_secret_manager_secret_uri.

`string gcs_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcsUri.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
