---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitKindRequestOrBuilder
title: Interface UpdateUnitKindRequestOrBuilder (0.29.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:24.589237+00:00
---

# Interface UpdateUnitKindRequestOrBuilder (0.29.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitKindRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdateUnitKindRequestOrBuilder (0.29.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.0 (latest)  0.25.0  0.24.0  0.23.0  0.21.0  0.18.0  0.17.0  0.15.0  0.13.0  0.12.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0 
    
    
    public interface UpdateUnitKindRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getRequestId()
    
    
    public abstract String getRequestId()

An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

`string request_id = 10502;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

`string request_id = 10502;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### getUnitKind()
    
    
    public abstract UnitKind getUnitKind()

Required. The desired state for the unit kind.

` .google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind unit_kind = 10504 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` | The unitKind.  
  
### getUnitKindOrBuilder()
    
    
    public abstract UnitKindOrBuilder getUnitKindOrBuilder()

Required. The desired state for the unit kind.

` .google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind unit_kind = 10504 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UnitKindOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKindOrBuilder)` |   
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

Field mask is used to specify the fields to be overwritten in the UnitKind resource by the update.

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.

If the user does not provide a mask then all fields in the UnitKind will be overwritten.

`.google.protobuf.FieldMask update_mask = 10512;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

Field mask is used to specify the fields to be overwritten in the UnitKind resource by the update.

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.

If the user does not provide a mask then all fields in the UnitKind will be overwritten.

`.google.protobuf.FieldMask update_mask = 10512;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

If "validate_only" is set to true, the service will try to validate that this request would succeed, but will not actually make changes.

`bool validate_only = 10501;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
### hasUnitKind()
    
    
    public abstract boolean hasUnitKind()

Required. The desired state for the unit kind.

` .google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind unit_kind = 10504 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the unitKind field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

Field mask is used to specify the fields to be overwritten in the UnitKind resource by the update.

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.

If the user does not provide a mask then all fields in the UnitKind will be overwritten.

`.google.protobuf.FieldMask update_mask = 10512;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
