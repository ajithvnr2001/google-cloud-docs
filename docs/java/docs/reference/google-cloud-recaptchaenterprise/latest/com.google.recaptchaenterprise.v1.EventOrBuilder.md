---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.EventOrBuilder
title: Interface EventOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:37.848677+00:00
---

# Interface EventOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.EventOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EventOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface EventOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExpectedAction()
    
    
    public abstract String getExpectedAction()

Optional. The expected action for this type of event. This should be the same action provided at token generation time on client-side platforms already integrated with recaptcha enterprise. Required for Universal keys.

`string expected_action = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The expectedAction.  
  
### getExpectedActionBytes()
    
    
    public abstract ByteString getExpectedActionBytes()

Optional. The expected action for this type of event. This should be the same action provided at token generation time on client-side platforms already integrated with recaptcha enterprise. Required for Universal keys.

`string expected_action = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for expectedAction.  
  
### getExpress()
    
    
    public abstract boolean getExpress()

Optional. Flag for a reCAPTCHA express request for an assessment without a token. If enabled, `site_key` must reference an Express site key.

`bool express = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The express.  
  
### getFirewallPolicyEvaluation()
    
    
    public abstract boolean getFirewallPolicyEvaluation()

Optional. Flag for enabling firewall policy config assessment. If this flag is enabled, the firewall policy is evaluated and a suggested firewall action is returned in the response.

`bool firewall_policy_evaluation = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The firewallPolicyEvaluation.  
  
### getFraudPrevention()
    
    
    public abstract Event.FraudPrevention getFraudPrevention()

Optional. The Fraud Prevention setting for this assessment.

` .google.cloud.recaptchaenterprise.v1.Event.FraudPrevention fraud_prevention = 17 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Event.FraudPrevention](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.FraudPrevention)` | The fraudPrevention.  
  
### getFraudPreventionValue()
    
    
    public abstract int getFraudPreventionValue()

Optional. The Fraud Prevention setting for this assessment.

` .google.cloud.recaptchaenterprise.v1.Event.FraudPrevention fraud_prevention = 17 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for fraudPrevention.  
  
### getHashedAccountId() (deprecated)
    
    
    public abstract ByteString getHashedAccountId()

**Deprecated.** _google.cloud.recaptchaenterprise.v1.Event.hashed_account_id is deprecated. See google/cloud/recaptchaenterprise/v1/recaptchaenterprise.proto;l=786_

Optional. Deprecated: use `user_info.account_id` instead. Unique stable hashed user identifier for the request. The identifier must be hashed using hmac-sha256 with stable secret.

`bytes hashed_account_id = 6 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The hashedAccountId.  
  
### getHeaders(int index)
    
    
    public abstract String getHeaders(int index)

Optional. HTTP header information about the request.

`repeated string headers = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The headers at the given index.  
  
### getHeadersBytes(int index)
    
    
    public abstract ByteString getHeadersBytes(int index)

Optional. HTTP header information about the request.

`repeated string headers = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the headers at the given index.  
  
### getHeadersCount()
    
    
    public abstract int getHeadersCount()

Optional. HTTP header information about the request.

`repeated string headers = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of headers.  
  
### getHeadersList()
    
    
    public abstract List<String> getHeadersList()

Optional. HTTP header information about the request.

`repeated string headers = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the headers.  
  
### getJa3()
    
    
    public abstract String getJa3()

Optional. JA3 fingerprint for SSL clients. To learn how to compute this fingerprint, please refer to <https://github.com/salesforce/ja3>.

`string ja3 = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ja3.  
  
### getJa3Bytes()
    
    
    public abstract ByteString getJa3Bytes()

Optional. JA3 fingerprint for SSL clients. To learn how to compute this fingerprint, please refer to <https://github.com/salesforce/ja3>.

`string ja3 = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ja3.  
  
### getJa4()
    
    
    public abstract String getJa4()

Optional. JA4 fingerprint for SSL clients. To learn how to compute this fingerprint, please refer to <https://github.com/FoxIO-LLC/ja4>.

`string ja4 = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ja4.  
  
### getJa4Bytes()
    
    
    public abstract ByteString getJa4Bytes()

Optional. JA4 fingerprint for SSL clients. To learn how to compute this fingerprint, please refer to <https://github.com/FoxIO-LLC/ja4>.

`string ja4 = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ja4.  
  
### getRequestedUri()
    
    
    public abstract String getRequestedUri()

Optional. The URI resource the user requested that triggered an assessment.

`string requested_uri = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestedUri.  
  
### getRequestedUriBytes()
    
    
    public abstract ByteString getRequestedUriBytes()

Optional. The URI resource the user requested that triggered an assessment.

`string requested_uri = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestedUri.  
  
### getSiteKey()
    
    
    public abstract String getSiteKey()

Optional. The site key that was used to invoke reCAPTCHA Enterprise on your site and generate the token.

`string site_key = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The siteKey.  
  
### getSiteKeyBytes()
    
    
    public abstract ByteString getSiteKeyBytes()

Optional. The site key that was used to invoke reCAPTCHA Enterprise on your site and generate the token.

`string site_key = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for siteKey.  
  
### getToken()
    
    
    public abstract String getToken()

Optional. The user response token provided by the reCAPTCHA Enterprise client-side integration on your site.

`string token = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The token.  
  
### getTokenBytes()
    
    
    public abstract ByteString getTokenBytes()

Optional. The user response token provided by the reCAPTCHA Enterprise client-side integration on your site.

`string token = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for token.  
  
### getTransactionData()
    
    
    public abstract TransactionData getTransactionData()

Optional. Data describing a payment transaction to be assessed. Sending this data enables reCAPTCHA Enterprise Fraud Prevention and the FraudPreventionAssessment component in the response.

` .google.cloud.recaptchaenterprise.v1.TransactionData transaction_data = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TransactionData](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TransactionData)` | The transactionData.  
  
### getTransactionDataOrBuilder()
    
    
    public abstract TransactionDataOrBuilder getTransactionDataOrBuilder()

Optional. Data describing a payment transaction to be assessed. Sending this data enables reCAPTCHA Enterprise Fraud Prevention and the FraudPreventionAssessment component in the response.

` .google.cloud.recaptchaenterprise.v1.TransactionData transaction_data = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TransactionDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TransactionDataOrBuilder)` |   
  
### getUserAgent()
    
    
    public abstract String getUserAgent()

Optional. The user agent present in the request from the user's device related to this event.

`string user_agent = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userAgent.  
  
### getUserAgentBytes()
    
    
    public abstract ByteString getUserAgentBytes()

Optional. The user agent present in the request from the user's device related to this event.

`string user_agent = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userAgent.  
  
### getUserInfo()
    
    
    public abstract UserInfo getUserInfo()

Optional. Information about the user that generates this event, when they can be identified. They are often identified through the use of an account for logged-in requests or login/registration requests, or by providing user identifiers for guest actions like checkout.

` .google.cloud.recaptchaenterprise.v1.UserInfo user_info = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[UserInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserInfo)` | The userInfo.  
  
### getUserInfoOrBuilder()
    
    
    public abstract UserInfoOrBuilder getUserInfoOrBuilder()

Optional. Information about the user that generates this event, when they can be identified. They are often identified through the use of an account for logged-in requests or login/registration requests, or by providing user identifiers for guest actions like checkout.

` .google.cloud.recaptchaenterprise.v1.UserInfo user_info = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[UserInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UserInfoOrBuilder)` |   
  
### getUserIpAddress()
    
    
    public abstract String getUserIpAddress()

Optional. The IP address in the request from the user's device related to this event.

` string user_ip_address = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userIpAddress.  
  
### getUserIpAddressBytes()
    
    
    public abstract ByteString getUserIpAddressBytes()

Optional. The IP address in the request from the user's device related to this event.

` string user_ip_address = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userIpAddress.  
  
### getWafTokenAssessment()
    
    
    public abstract boolean getWafTokenAssessment()

Optional. Flag for running Web Application Firewall (WAF) token assessment. If enabled, the token must be specified, and have been created by a WAF-enabled key.

`bool waf_token_assessment = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The wafTokenAssessment.  
  
### hasTransactionData()
    
    
    public abstract boolean hasTransactionData()

Optional. Data describing a payment transaction to be assessed. Sending this data enables reCAPTCHA Enterprise Fraud Prevention and the FraudPreventionAssessment component in the response.

` .google.cloud.recaptchaenterprise.v1.TransactionData transaction_data = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transactionData field is set.  
  
### hasUserInfo()
    
    
    public abstract boolean hasUserInfo()

Optional. Information about the user that generates this event, when they can be identified. They are often identified through the use of an account for logged-in requests or login/registration requests, or by providing user identifiers for guest actions like checkout.

` .google.cloud.recaptchaenterprise.v1.UserInfo user_info = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userInfo field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
