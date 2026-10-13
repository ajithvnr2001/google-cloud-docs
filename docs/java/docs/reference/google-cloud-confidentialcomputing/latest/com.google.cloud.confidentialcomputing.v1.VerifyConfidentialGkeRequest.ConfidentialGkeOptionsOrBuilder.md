---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialGkeRequest.ConfidentialGkeOptionsOrBuilder
title: Interface VerifyConfidentialGkeRequest.ConfidentialGkeOptionsOrBuilder (0.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:40.604264+00:00
---

# Interface VerifyConfidentialGkeRequest.ConfidentialGkeOptionsOrBuilder (0.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialGkeRequest.ConfidentialGkeOptionsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface VerifyConfidentialGkeRequest.ConfidentialGkeOptionsOrBuilder (0.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.85.0 (latest)  0.81.0  0.80.0  0.79.0  0.77.0  0.74.0  0.73.0  0.71.0  0.69.0  0.68.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.56.0  0.54.0  0.53.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface VerifyConfidentialGkeRequest.ConfidentialGkeOptionsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAudience()
    
    
    public abstract String getAudience()

Optional. Optional string to issue the token with a custom audience claim. Required if custom nonces are specified.

`string audience = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The audience.  
  
### getAudienceBytes()
    
    
    public abstract ByteString getAudienceBytes()

Optional. Optional string to issue the token with a custom audience claim. Required if custom nonces are specified.

`string audience = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for audience.  
  
### getNonce(int index)
    
    
    public abstract String getNonce(int index)

Optional. Optional parameter to place one or more nonces in the eat_nonce claim in the output token. The minimum size for JSON-encoded EATs is 10 bytes and the maximum size is 74 bytes.

`repeated string nonce = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nonce at the given index.  
  
### getNonceBytes(int index)
    
    
    public abstract ByteString getNonceBytes(int index)

Optional. Optional parameter to place one or more nonces in the eat_nonce claim in the output token. The minimum size for JSON-encoded EATs is 10 bytes and the maximum size is 74 bytes.

`repeated string nonce = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the nonce at the given index.  
  
### getNonceCount()
    
    
    public abstract int getNonceCount()

Optional. Optional parameter to place one or more nonces in the eat_nonce claim in the output token. The minimum size for JSON-encoded EATs is 10 bytes and the maximum size is 74 bytes.

`repeated string nonce = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of nonce.  
  
### getNonceList()
    
    
    public abstract List<String> getNonceList()

Optional. Optional parameter to place one or more nonces in the eat_nonce claim in the output token. The minimum size for JSON-encoded EATs is 10 bytes and the maximum size is 74 bytes.

`repeated string nonce = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the nonce.  
  
### getSignatureType()
    
    
    public abstract SignatureType getSignatureType()

Optional. Optional specification for how to sign the attestation token. Defaults to SIGNATURE_TYPE_OIDC if unspecified.

` .google.cloud.confidentialcomputing.v1.SignatureType signature_type = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SignatureType](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.SignatureType)` | The signatureType.  
  
### getSignatureTypeValue()
    
    
    public abstract int getSignatureTypeValue()

Optional. Optional specification for how to sign the attestation token. Defaults to SIGNATURE_TYPE_OIDC if unspecified.

` .google.cloud.confidentialcomputing.v1.SignatureType signature_type = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for signatureType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
