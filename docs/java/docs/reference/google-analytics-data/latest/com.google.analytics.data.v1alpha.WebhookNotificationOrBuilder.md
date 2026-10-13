---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.WebhookNotificationOrBuilder
title: Interface WebhookNotificationOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:23.211514+00:00
---

# Interface WebhookNotificationOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.WebhookNotificationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WebhookNotificationOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface WebhookNotificationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChannelToken()
    
    
    public abstract String getChannelToken()

Optional. The channel token is an arbitrary string value and must have a maximum string length of 64 characters. Channel tokens allow you to verify the source of a webhook notification. This guards against the message being spoofed. The channel token will be specified in the `X-Goog-Channel-Token` HTTP header of the webhook POST request.

A channel token is not required to use webhook notifications.

`optional string channel_token = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The channelToken.  
  
### getChannelTokenBytes()
    
    
    public abstract ByteString getChannelTokenBytes()

Optional. The channel token is an arbitrary string value and must have a maximum string length of 64 characters. Channel tokens allow you to verify the source of a webhook notification. This guards against the message being spoofed. The channel token will be specified in the `X-Goog-Channel-Token` HTTP header of the webhook POST request.

A channel token is not required to use webhook notifications.

`optional string channel_token = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for channelToken.  
  
### getUri()
    
    
    public abstract String getUri()

Optional. The web address that will receive the webhook notification. This address will receive POST requests as the state of the long running operation resource changes. The POST request will contain both a JSON version of the long running operation resource in the body and a `sentTimestamp` field. The sent timestamp will specify the unix microseconds since the epoch that the request was sent; this lets you identify replayed notifications.

An example URI is `<https://us-central1-example-project-id.cloudfunctions.net/example-function-1>`.

The URI must use HTTPS and point to a site with a valid SSL certificate on the web server. The URI must have a maximum string length of 128 characters & use only the allowlisted characters from [RFC 1738](https://www.rfc-editor.org/rfc/rfc1738).

When your webhook server receives a notification, it is expected to reply with an HTTP response status code of 200 within 5 seconds.

A URI is required to use webhook notifications.

Requests to this webhook server will contain an ID token authenticating the service account `google-analytics-audience-export@system.gserviceaccount.com`. To learn more about ID tokens, see <https://cloud.google.com/docs/authentication/token-types#id>. For Google Cloud Functions, this lets you configure your function to require authentication. In Cloud IAM, you will need to grant the service account permissions to the Cloud Run Invoker (`roles/run.invoker`) & Cloud Functions Invoker (`roles/cloudfunctions.invoker`) roles for the webhook post request to pass Google Cloud Functions authentication. This API can send webhook notifications to arbitrary URIs; for webhook servers other than Google Cloud Functions, this ID token in the authorization bearer header should be ignored if it is not needed.

`optional string uri = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uri.  
  
### getUriBytes()
    
    
    public abstract ByteString getUriBytes()

Optional. The web address that will receive the webhook notification. This address will receive POST requests as the state of the long running operation resource changes. The POST request will contain both a JSON version of the long running operation resource in the body and a `sentTimestamp` field. The sent timestamp will specify the unix microseconds since the epoch that the request was sent; this lets you identify replayed notifications.

An example URI is `<https://us-central1-example-project-id.cloudfunctions.net/example-function-1>`.

The URI must use HTTPS and point to a site with a valid SSL certificate on the web server. The URI must have a maximum string length of 128 characters & use only the allowlisted characters from [RFC 1738](https://www.rfc-editor.org/rfc/rfc1738).

When your webhook server receives a notification, it is expected to reply with an HTTP response status code of 200 within 5 seconds.

A URI is required to use webhook notifications.

Requests to this webhook server will contain an ID token authenticating the service account `google-analytics-audience-export@system.gserviceaccount.com`. To learn more about ID tokens, see <https://cloud.google.com/docs/authentication/token-types#id>. For Google Cloud Functions, this lets you configure your function to require authentication. In Cloud IAM, you will need to grant the service account permissions to the Cloud Run Invoker (`roles/run.invoker`) & Cloud Functions Invoker (`roles/cloudfunctions.invoker`) roles for the webhook post request to pass Google Cloud Functions authentication. This API can send webhook notifications to arbitrary URIs; for webhook servers other than Google Cloud Functions, this ID token in the authorization bearer header should be ignored if it is not needed.

`optional string uri = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uri.  
  
### hasChannelToken()
    
    
    public abstract boolean hasChannelToken()

Optional. The channel token is an arbitrary string value and must have a maximum string length of 64 characters. Channel tokens allow you to verify the source of a webhook notification. This guards against the message being spoofed. The channel token will be specified in the `X-Goog-Channel-Token` HTTP header of the webhook POST request.

A channel token is not required to use webhook notifications.

`optional string channel_token = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the channelToken field is set.  
  
### hasUri()
    
    
    public abstract boolean hasUri()

Optional. The web address that will receive the webhook notification. This address will receive POST requests as the state of the long running operation resource changes. The POST request will contain both a JSON version of the long running operation resource in the body and a `sentTimestamp` field. The sent timestamp will specify the unix microseconds since the epoch that the request was sent; this lets you identify replayed notifications.

An example URI is `<https://us-central1-example-project-id.cloudfunctions.net/example-function-1>`.

The URI must use HTTPS and point to a site with a valid SSL certificate on the web server. The URI must have a maximum string length of 128 characters & use only the allowlisted characters from [RFC 1738](https://www.rfc-editor.org/rfc/rfc1738).

When your webhook server receives a notification, it is expected to reply with an HTTP response status code of 200 within 5 seconds.

A URI is required to use webhook notifications.

Requests to this webhook server will contain an ID token authenticating the service account `google-analytics-audience-export@system.gserviceaccount.com`. To learn more about ID tokens, see <https://cloud.google.com/docs/authentication/token-types#id>. For Google Cloud Functions, this lets you configure your function to require authentication. In Cloud IAM, you will need to grant the service account permissions to the Cloud Run Invoker (`roles/run.invoker`) & Cloud Functions Invoker (`roles/cloudfunctions.invoker`) roles for the webhook post request to pass Google Cloud Functions authentication. This API can send webhook notifications to arbitrary URIs; for webhook servers other than Google Cloud Functions, this ID token in the authorization bearer header should be ignored if it is not needed.

`optional string uri = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the uri field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
