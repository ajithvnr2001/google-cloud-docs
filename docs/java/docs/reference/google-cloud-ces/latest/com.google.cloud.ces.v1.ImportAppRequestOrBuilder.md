---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ImportAppRequestOrBuilder
title: Interface ImportAppRequestOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:57.087310+00:00
---

# Interface ImportAppRequestOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ImportAppRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportAppRequestOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ImportAppRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAppCase()
    
    
    public abstract ImportAppRequest.AppCase getAppCase()

**Returns**  
---  
**Type** | **Description**  
`[ImportAppRequest.AppCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ImportAppRequest.AppCase)` |   
  
### getAppContent()
    
    
    public abstract ByteString getAppContent()

Raw bytes representing the compressed zip file with the app folder structure.

`bytes app_content = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The appContent.  
  
### getAppId()
    
    
    public abstract String getAppId()

Optional. The ID to use for the imported app.

  * If not specified, a unique ID will be automatically assigned for the app.
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.



`string app_id = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The appId.  
  
### getAppIdBytes()
    
    
    public abstract ByteString getAppIdBytes()

Optional. The ID to use for the imported app.

  * If not specified, a unique ID will be automatically assigned for the app.
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.



`string app_id = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for appId.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. The display name of the app to import.

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.



`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. The display name of the app to import.

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.



`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getGcsUri()
    
    
    public abstract String getGcsUri()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import app. The format of this URI must be `gs://<bucket-name>/<object-name>`.

`string gcs_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcsUri.  
  
### getGcsUriBytes()
    
    
    public abstract ByteString getGcsUriBytes()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import app. The format of this URI must be `gs://<bucket-name>/<object-name>`.

`string gcs_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcsUri.  
  
### getIgnoreAppLock()
    
    
    public abstract boolean getIgnoreAppLock()

Optional. Flag for overriding the app lock during import. If set to true, the import process will ignore the app lock.

`bool ignore_app_lock = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ignoreAppLock.  
  
### getImportOptions()
    
    
    public abstract ImportAppRequest.ImportOptions getImportOptions()

Optional. Options governing the import process for the app.

` .google.cloud.ces.v1.ImportAppRequest.ImportOptions import_options = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportAppRequest.ImportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ImportAppRequest.ImportOptions)` | The importOptions.  
  
### getImportOptionsOrBuilder()
    
    
    public abstract ImportAppRequest.ImportOptionsOrBuilder getImportOptionsOrBuilder()

Optional. Options governing the import process for the app.

` .google.cloud.ces.v1.ImportAppRequest.ImportOptions import_options = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportAppRequest.ImportOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ImportAppRequest.ImportOptionsOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The parent resource name with the location of the app to import.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent resource name with the location of the app to import.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasAppContent()
    
    
    public abstract boolean hasAppContent()

Raw bytes representing the compressed zip file with the app folder structure.

`bytes app_content = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the appContent field is set.  
  
### hasGcsUri()
    
    
    public abstract boolean hasGcsUri()

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import app. The format of this URI must be `gs://<bucket-name>/<object-name>`.

`string gcs_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsUri field is set.  
  
### hasImportOptions()
    
    
    public abstract boolean hasImportOptions()

Optional. Options governing the import process for the app.

` .google.cloud.ces.v1.ImportAppRequest.ImportOptions import_options = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the importOptions field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
