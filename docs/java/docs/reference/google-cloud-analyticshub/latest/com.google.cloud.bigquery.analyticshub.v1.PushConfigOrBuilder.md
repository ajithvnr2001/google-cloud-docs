---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfigOrBuilder
title: Interface PushConfigOrBuilder (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:10.850577+00:00
---

# Interface PushConfigOrBuilder (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PushConfigOrBuilder (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface PushConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsAttributes(String key)
    
    
    public abstract boolean containsAttributes(String key)

Optional. Endpoint configuration attributes that can be used to control different aspects of the message delivery.

The only currently supported attribute is `x-goog-version`, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata).

If not present during the `CreateSubscription` call, it will default to the version of the Pub/Sub API used to make such call. If not present in a `ModifyPushConfig` call, its value will not be changed. `GetSubscription` calls will always return a valid version, even if the subscription was created without this attribute.

The only supported values for the `x-goog-version` attribute are:

  * `v1beta1`: uses the push format defined in the v1beta1 Pub/Sub API.
  * `v1` or `v1beta2`: uses the push format defined in the v1 Pub/Sub API.

For example: `attributes { "x-goog-version": "v1" }`




`map<string, string> attributes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributes() (deprecated)
    
    
    public abstract Map<String,String> getAttributes()

Use [#getAttributesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfigOrBuilder#com_google_cloud_bigquery_analyticshub_v1_PushConfigOrBuilder_getAttributesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAttributesCount()
    
    
    public abstract int getAttributesCount()

Optional. Endpoint configuration attributes that can be used to control different aspects of the message delivery.

The only currently supported attribute is `x-goog-version`, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata).

If not present during the `CreateSubscription` call, it will default to the version of the Pub/Sub API used to make such call. If not present in a `ModifyPushConfig` call, its value will not be changed. `GetSubscription` calls will always return a valid version, even if the subscription was created without this attribute.

The only supported values for the `x-goog-version` attribute are:

  * `v1beta1`: uses the push format defined in the v1beta1 Pub/Sub API.
  * `v1` or `v1beta2`: uses the push format defined in the v1 Pub/Sub API.

For example: `attributes { "x-goog-version": "v1" }`




`map<string, string> attributes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributesMap()
    
    
    public abstract Map<String,String> getAttributesMap()

Optional. Endpoint configuration attributes that can be used to control different aspects of the message delivery.

The only currently supported attribute is `x-goog-version`, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata).

If not present during the `CreateSubscription` call, it will default to the version of the Pub/Sub API used to make such call. If not present in a `ModifyPushConfig` call, its value will not be changed. `GetSubscription` calls will always return a valid version, even if the subscription was created without this attribute.

The only supported values for the `x-goog-version` attribute are:

  * `v1beta1`: uses the push format defined in the v1beta1 Pub/Sub API.
  * `v1` or `v1beta2`: uses the push format defined in the v1 Pub/Sub API.

For example: `attributes { "x-goog-version": "v1" }`




`map<string, string> attributes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAttributesOrDefault(String key, String defaultValue)
    
    
    public abstract String getAttributesOrDefault(String key, String defaultValue)

Optional. Endpoint configuration attributes that can be used to control different aspects of the message delivery.

The only currently supported attribute is `x-goog-version`, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata).

If not present during the `CreateSubscription` call, it will default to the version of the Pub/Sub API used to make such call. If not present in a `ModifyPushConfig` call, its value will not be changed. `GetSubscription` calls will always return a valid version, even if the subscription was created without this attribute.

The only supported values for the `x-goog-version` attribute are:

  * `v1beta1`: uses the push format defined in the v1beta1 Pub/Sub API.
  * `v1` or `v1beta2`: uses the push format defined in the v1 Pub/Sub API.

For example: `attributes { "x-goog-version": "v1" }`




`map<string, string> attributes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAttributesOrThrow(String key)
    
    
    public abstract String getAttributesOrThrow(String key)

Optional. Endpoint configuration attributes that can be used to control different aspects of the message delivery.

The only currently supported attribute is `x-goog-version`, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata).

If not present during the `CreateSubscription` call, it will default to the version of the Pub/Sub API used to make such call. If not present in a `ModifyPushConfig` call, its value will not be changed. `GetSubscription` calls will always return a valid version, even if the subscription was created without this attribute.

The only supported values for the `x-goog-version` attribute are:

  * `v1beta1`: uses the push format defined in the v1beta1 Pub/Sub API.
  * `v1` or `v1beta2`: uses the push format defined in the v1 Pub/Sub API.

For example: `attributes { "x-goog-version": "v1" }`




`map<string, string> attributes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAuthenticationMethodCase()
    
    
    public abstract PushConfig.AuthenticationMethodCase getAuthenticationMethodCase()

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.AuthenticationMethodCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.AuthenticationMethodCase)` |   
  
### getNoWrapper()
    
    
    public abstract PushConfig.NoWrapper getNoWrapper()

Optional. When set, the payload to the push endpoint is not wrapped.

` .google.cloud.bigquery.analyticshub.v1.PushConfig.NoWrapper no_wrapper = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.NoWrapper](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.NoWrapper)` | The noWrapper.  
  
### getNoWrapperOrBuilder()
    
    
    public abstract PushConfig.NoWrapperOrBuilder getNoWrapperOrBuilder()

Optional. When set, the payload to the push endpoint is not wrapped.

` .google.cloud.bigquery.analyticshub.v1.PushConfig.NoWrapper no_wrapper = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.NoWrapperOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.NoWrapperOrBuilder)` |   
  
### getOidcToken()
    
    
    public abstract PushConfig.OidcToken getOidcToken()

Optional. If specified, Pub/Sub will generate and attach an OIDC JWT token as an `Authorization` header in the HTTP request for every pushed message.

` .google.cloud.bigquery.analyticshub.v1.PushConfig.OidcToken oidc_token = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.OidcToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.OidcToken)` | The oidcToken.  
  
### getOidcTokenOrBuilder()
    
    
    public abstract PushConfig.OidcTokenOrBuilder getOidcTokenOrBuilder()

Optional. If specified, Pub/Sub will generate and attach an OIDC JWT token as an `Authorization` header in the HTTP request for every pushed message.

` .google.cloud.bigquery.analyticshub.v1.PushConfig.OidcToken oidc_token = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.OidcTokenOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.OidcTokenOrBuilder)` |   
  
### getPubsubWrapper()
    
    
    public abstract PushConfig.PubsubWrapper getPubsubWrapper()

Optional. When set, the payload to the push endpoint is in the form of the JSON representation of a PubsubMessage (<https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage>).

` .google.cloud.bigquery.analyticshub.v1.PushConfig.PubsubWrapper pubsub_wrapper = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.PubsubWrapper](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.PubsubWrapper)` | The pubsubWrapper.  
  
### getPubsubWrapperOrBuilder()
    
    
    public abstract PushConfig.PubsubWrapperOrBuilder getPubsubWrapperOrBuilder()

Optional. When set, the payload to the push endpoint is in the form of the JSON representation of a PubsubMessage (<https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage>).

` .google.cloud.bigquery.analyticshub.v1.PushConfig.PubsubWrapper pubsub_wrapper = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.PubsubWrapperOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.PubsubWrapperOrBuilder)` |   
  
### getPushEndpoint()
    
    
    public abstract String getPushEndpoint()

Optional. A URL locating the endpoint to which messages should be pushed. For example, a Webhook endpoint might use `<https://example.com/push>`.

`string push_endpoint = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pushEndpoint.  
  
### getPushEndpointBytes()
    
    
    public abstract ByteString getPushEndpointBytes()

Optional. A URL locating the endpoint to which messages should be pushed. For example, a Webhook endpoint might use `<https://example.com/push>`.

`string push_endpoint = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pushEndpoint.  
  
### getWrapperCase()
    
    
    public abstract PushConfig.WrapperCase getWrapperCase()

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.WrapperCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.WrapperCase)` |   
  
### hasNoWrapper()
    
    
    public abstract boolean hasNoWrapper()

Optional. When set, the payload to the push endpoint is not wrapped.

` .google.cloud.bigquery.analyticshub.v1.PushConfig.NoWrapper no_wrapper = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the noWrapper field is set.  
  
### hasOidcToken()
    
    
    public abstract boolean hasOidcToken()

Optional. If specified, Pub/Sub will generate and attach an OIDC JWT token as an `Authorization` header in the HTTP request for every pushed message.

` .google.cloud.bigquery.analyticshub.v1.PushConfig.OidcToken oidc_token = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oidcToken field is set.  
  
### hasPubsubWrapper()
    
    
    public abstract boolean hasPubsubWrapper()

Optional. When set, the payload to the push endpoint is in the form of the JSON representation of a PubsubMessage (<https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage>).

` .google.cloud.bigquery.analyticshub.v1.PushConfig.PubsubWrapper pubsub_wrapper = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pubsubWrapper field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
