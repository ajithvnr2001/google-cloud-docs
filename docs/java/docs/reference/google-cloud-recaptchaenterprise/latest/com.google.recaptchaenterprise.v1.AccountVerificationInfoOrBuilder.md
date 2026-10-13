---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountVerificationInfoOrBuilder
title: Interface AccountVerificationInfoOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:33.782809+00:00
---

# Interface AccountVerificationInfoOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountVerificationInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AccountVerificationInfoOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface AccountVerificationInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEndpoints(int index)
    
    
    public abstract EndpointVerificationInfo getEndpoints(int index)

Optional. Endpoints that can be used for identity verification.

` repeated .google.cloud.recaptchaenterprise.v1.EndpointVerificationInfo endpoints = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EndpointVerificationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.EndpointVerificationInfo)` |   
  
### getEndpointsCount()
    
    
    public abstract int getEndpointsCount()

Optional. Endpoints that can be used for identity verification.

` repeated .google.cloud.recaptchaenterprise.v1.EndpointVerificationInfo endpoints = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEndpointsList()
    
    
    public abstract List<EndpointVerificationInfo> getEndpointsList()

Optional. Endpoints that can be used for identity verification.

` repeated .google.cloud.recaptchaenterprise.v1.EndpointVerificationInfo endpoints = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EndpointVerificationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.EndpointVerificationInfo)>` |   
  
### getEndpointsOrBuilder(int index)
    
    
    public abstract EndpointVerificationInfoOrBuilder getEndpointsOrBuilder(int index)

Optional. Endpoints that can be used for identity verification.

` repeated .google.cloud.recaptchaenterprise.v1.EndpointVerificationInfo endpoints = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EndpointVerificationInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.EndpointVerificationInfoOrBuilder)` |   
  
### getEndpointsOrBuilderList()
    
    
    public abstract List<? extends EndpointVerificationInfoOrBuilder> getEndpointsOrBuilderList()

Optional. Endpoints that can be used for identity verification.

` repeated .google.cloud.recaptchaenterprise.v1.EndpointVerificationInfo endpoints = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.recaptchaenterprise.v1.EndpointVerificationInfoOrBuilder>` |   
  
### getLanguageCode()
    
    
    public abstract String getLanguageCode()

Optional. Language code preference for the verification message, set as a IETF BCP 47 language code.

`string language_code = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public abstract ByteString getLanguageCodeBytes()

Optional. Language code preference for the verification message, set as a IETF BCP 47 language code.

`string language_code = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getLatestVerificationResult()
    
    
    public abstract AccountVerificationInfo.Result getLatestVerificationResult()

Output only. Result of the latest account verification challenge.

` .google.cloud.recaptchaenterprise.v1.AccountVerificationInfo.Result latest_verification_result = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AccountVerificationInfo.Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AccountVerificationInfo.Result)` | The latestVerificationResult.  
  
### getLatestVerificationResultValue()
    
    
    public abstract int getLatestVerificationResultValue()

Output only. Result of the latest account verification challenge.

` .google.cloud.recaptchaenterprise.v1.AccountVerificationInfo.Result latest_verification_result = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for latestVerificationResult.  
  
### getUsername() (deprecated)
    
    
    public abstract String getUsername()

**Deprecated.** _google.cloud.recaptchaenterprise.v1.AccountVerificationInfo.username is deprecated. See google/cloud/recaptchaenterprise/v1/recaptchaenterprise.proto;l=638_

Username of the account that is being verified. Deprecated. Customers should now provide the `account_id` field in `event.user_info`.

`string username = 2 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The username.  
  
### getUsernameBytes() (deprecated)
    
    
    public abstract ByteString getUsernameBytes()

**Deprecated.** _google.cloud.recaptchaenterprise.v1.AccountVerificationInfo.username is deprecated. See google/cloud/recaptchaenterprise/v1/recaptchaenterprise.proto;l=638_

Username of the account that is being verified. Deprecated. Customers should now provide the `account_id` field in `event.user_info`.

`string username = 2 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for username.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
