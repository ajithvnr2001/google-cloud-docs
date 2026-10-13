---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ImportDataRequestOrBuilder
title: Interface ImportDataRequestOrBuilder (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:20.101973+00:00
---

# Interface ImportDataRequestOrBuilder (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ImportDataRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportDataRequestOrBuilder (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public interface ImportDataRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDestinationCase()
    
    
    public abstract ImportDataRequest.DestinationCase getDestinationCase()

**Returns**  
---  
**Type** | **Description**  
`[ImportDataRequest.DestinationCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ImportDataRequest.DestinationCase)` |   
  
### getGcsPath()
    
    
    public abstract GcsPath getGcsPath()

The Cloud Storage source bucket and, optionally, path inside the bucket. If a path inside the bucket is specified, it must end with a forward slash (`/`).

`.google.cloud.lustre.v1.GcsPath gcs_path = 2;`

**Returns**  
---  
**Type** | **Description**  
`[GcsPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.GcsPath)` | The gcsPath.  
  
### getGcsPathOrBuilder()
    
    
    public abstract GcsPathOrBuilder getGcsPathOrBuilder()

The Cloud Storage source bucket and, optionally, path inside the bucket. If a path inside the bucket is specified, it must end with a forward slash (`/`).

`.google.cloud.lustre.v1.GcsPath gcs_path = 2;`

**Returns**  
---  
**Type** | **Description**  
`[GcsPathOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.GcsPathOrBuilder)` |   
  
### getLustrePath()
    
    
    public abstract LustrePath getLustrePath()

Lustre path destination.

`.google.cloud.lustre.v1.LustrePath lustre_path = 3;`

**Returns**  
---  
**Type** | **Description**  
`[LustrePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustrePath)` | The lustrePath.  
  
### getLustrePathOrBuilder()
    
    
    public abstract LustrePathOrBuilder getLustrePathOrBuilder()

Lustre path destination.

`.google.cloud.lustre.v1.LustrePath lustre_path = 3;`

**Returns**  
---  
**Type** | **Description**  
`[LustrePathOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustrePathOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRequestId()
    
    
    public abstract String getRequestId()

Optional. UUID to identify requests.

` string request_id = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

Optional. UUID to identify requests.

` string request_id = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

Optional. User-specified service account used to perform the transfer. If unspecified, the default Managed Lustre service agent will be used.

Use one of the following formats:

  * `{EMAIL_ADDRESS_OR_UNIQUE_ID}`
  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`
  * `projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`



` string service_account = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

Optional. User-specified service account used to perform the transfer. If unspecified, the default Managed Lustre service agent will be used.

Use one of the following formats:

  * `{EMAIL_ADDRESS_OR_UNIQUE_ID}`
  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`
  * `projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`



` string service_account = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getSourceCase()
    
    
    public abstract ImportDataRequest.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[ImportDataRequest.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ImportDataRequest.SourceCase)` |   
  
### hasGcsPath()
    
    
    public abstract boolean hasGcsPath()

The Cloud Storage source bucket and, optionally, path inside the bucket. If a path inside the bucket is specified, it must end with a forward slash (`/`).

`.google.cloud.lustre.v1.GcsPath gcs_path = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsPath field is set.  
  
### hasLustrePath()
    
    
    public abstract boolean hasLustrePath()

Lustre path destination.

`.google.cloud.lustre.v1.LustrePath lustre_path = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lustrePath field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
