---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.HttpTargetOrBuilder
title: Interface HttpTargetOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:58.457110+00:00
---

# Interface HttpTargetOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.HttpTargetOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HttpTargetOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.HttpTargetOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.scheduler.v1.HttpTargetOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.scheduler.v1.HttpTargetOrBuilder)


    
    
    public interface HttpTargetOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsHeaders(String key)
    
    
    public abstract boolean containsHeaders(String key)

HTTP request headers. This map contains the header field names and values. The user can specify HTTP request headers to send with the job's HTTP request. Repeated headers are not supported, but a header value can contain commas. The following headers represent a subset of the headers that accompany the job's HTTP request. Some HTTP request headers are ignored or replaced. A partial list of headers that are ignored or replaced is below:

  * Host: This will be computed by Cloud Scheduler and derived from uri.
  * `Content-Length`: This will be computed by Cloud Scheduler.
  * `User-Agent`: This will be set to `"Google-Cloud-Scheduler"`.
  * `X-Google-*`: Google internal use only.
  * `X-AppEngine-*`: Google internal use only.
  * `X-CloudScheduler`: This header will be set to true.
  * `X-CloudScheduler-JobName`: This header will contain the job name.
  * `X-CloudScheduler-ScheduleTime`: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339. If the job has a body and the following headers are not set by the user, Cloud Scheduler sets default values:
  * `Content-Type`: This will be set to `"application/octet-stream"`. You can override this default by explicitly setting `Content-Type` to a particular media type when creating the job. For example, you can set `Content-Type` to `"application/json"`. The total size of headers must be less than 80KB.



`map<string, string> headers = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAuthorizationHeaderCase()
    
    
    public abstract HttpTarget.AuthorizationHeaderCase getAuthorizationHeaderCase()

**Returns**  
---  
**Type** | **Description**  
`[HttpTarget.AuthorizationHeaderCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.HttpTarget.AuthorizationHeaderCase)` |   
  
### getBody()
    
    
    public abstract ByteString getBody()

HTTP request body. A request body is allowed only if the HTTP method is POST, PUT, or PATCH. It is an error to set body on a job with an incompatible HttpMethod.

`bytes body = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The body.  
  
### getHeaders()
    
    
    public abstract Map<String,String> getHeaders()

Use [#getHeadersMap()](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.HttpTargetOrBuilder#com_google_events_cloud_scheduler_v1_HttpTargetOrBuilder_getHeadersMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getHeadersCount()
    
    
    public abstract int getHeadersCount()

HTTP request headers. This map contains the header field names and values. The user can specify HTTP request headers to send with the job's HTTP request. Repeated headers are not supported, but a header value can contain commas. The following headers represent a subset of the headers that accompany the job's HTTP request. Some HTTP request headers are ignored or replaced. A partial list of headers that are ignored or replaced is below:

  * Host: This will be computed by Cloud Scheduler and derived from uri.
  * `Content-Length`: This will be computed by Cloud Scheduler.
  * `User-Agent`: This will be set to `"Google-Cloud-Scheduler"`.
  * `X-Google-*`: Google internal use only.
  * `X-AppEngine-*`: Google internal use only.
  * `X-CloudScheduler`: This header will be set to true.
  * `X-CloudScheduler-JobName`: This header will contain the job name.
  * `X-CloudScheduler-ScheduleTime`: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339. If the job has a body and the following headers are not set by the user, Cloud Scheduler sets default values:
  * `Content-Type`: This will be set to `"application/octet-stream"`. You can override this default by explicitly setting `Content-Type` to a particular media type when creating the job. For example, you can set `Content-Type` to `"application/json"`. The total size of headers must be less than 80KB.



`map<string, string> headers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeadersMap()
    
    
    public abstract Map<String,String> getHeadersMap()

HTTP request headers. This map contains the header field names and values. The user can specify HTTP request headers to send with the job's HTTP request. Repeated headers are not supported, but a header value can contain commas. The following headers represent a subset of the headers that accompany the job's HTTP request. Some HTTP request headers are ignored or replaced. A partial list of headers that are ignored or replaced is below:

  * Host: This will be computed by Cloud Scheduler and derived from uri.
  * `Content-Length`: This will be computed by Cloud Scheduler.
  * `User-Agent`: This will be set to `"Google-Cloud-Scheduler"`.
  * `X-Google-*`: Google internal use only.
  * `X-AppEngine-*`: Google internal use only.
  * `X-CloudScheduler`: This header will be set to true.
  * `X-CloudScheduler-JobName`: This header will contain the job name.
  * `X-CloudScheduler-ScheduleTime`: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339. If the job has a body and the following headers are not set by the user, Cloud Scheduler sets default values:
  * `Content-Type`: This will be set to `"application/octet-stream"`. You can override this default by explicitly setting `Content-Type` to a particular media type when creating the job. For example, you can set `Content-Type` to `"application/json"`. The total size of headers must be less than 80KB.



`map<string, string> headers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getHeadersOrDefault(String key, String defaultValue)
    
    
    public abstract String getHeadersOrDefault(String key, String defaultValue)

HTTP request headers. This map contains the header field names and values. The user can specify HTTP request headers to send with the job's HTTP request. Repeated headers are not supported, but a header value can contain commas. The following headers represent a subset of the headers that accompany the job's HTTP request. Some HTTP request headers are ignored or replaced. A partial list of headers that are ignored or replaced is below:

  * Host: This will be computed by Cloud Scheduler and derived from uri.
  * `Content-Length`: This will be computed by Cloud Scheduler.
  * `User-Agent`: This will be set to `"Google-Cloud-Scheduler"`.
  * `X-Google-*`: Google internal use only.
  * `X-AppEngine-*`: Google internal use only.
  * `X-CloudScheduler`: This header will be set to true.
  * `X-CloudScheduler-JobName`: This header will contain the job name.
  * `X-CloudScheduler-ScheduleTime`: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339. If the job has a body and the following headers are not set by the user, Cloud Scheduler sets default values:
  * `Content-Type`: This will be set to `"application/octet-stream"`. You can override this default by explicitly setting `Content-Type` to a particular media type when creating the job. For example, you can set `Content-Type` to `"application/json"`. The total size of headers must be less than 80KB.



`map<string, string> headers = 3;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getHeadersOrThrow(String key)
    
    
    public abstract String getHeadersOrThrow(String key)

HTTP request headers. This map contains the header field names and values. The user can specify HTTP request headers to send with the job's HTTP request. Repeated headers are not supported, but a header value can contain commas. The following headers represent a subset of the headers that accompany the job's HTTP request. Some HTTP request headers are ignored or replaced. A partial list of headers that are ignored or replaced is below:

  * Host: This will be computed by Cloud Scheduler and derived from uri.
  * `Content-Length`: This will be computed by Cloud Scheduler.
  * `User-Agent`: This will be set to `"Google-Cloud-Scheduler"`.
  * `X-Google-*`: Google internal use only.
  * `X-AppEngine-*`: Google internal use only.
  * `X-CloudScheduler`: This header will be set to true.
  * `X-CloudScheduler-JobName`: This header will contain the job name.
  * `X-CloudScheduler-ScheduleTime`: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339. If the job has a body and the following headers are not set by the user, Cloud Scheduler sets default values:
  * `Content-Type`: This will be set to `"application/octet-stream"`. You can override this default by explicitly setting `Content-Type` to a particular media type when creating the job. For example, you can set `Content-Type` to `"application/json"`. The total size of headers must be less than 80KB.



`map<string, string> headers = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getHttpMethod()
    
    
    public abstract HttpMethod getHttpMethod()

Which HTTP method to use for the request.

`.google.events.cloud.scheduler.v1.HttpMethod http_method = 2;`

**Returns**  
---  
**Type** | **Description**  
`[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.HttpMethod)` | The httpMethod.  
  
### getHttpMethodValue()
    
    
    public abstract int getHttpMethodValue()

Which HTTP method to use for the request.

`.google.events.cloud.scheduler.v1.HttpMethod http_method = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for httpMethod.  
  
### getOauthToken()
    
    
    public abstract OAuthToken getOauthToken()

If specified, an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) will be generated and attached as an `Authorization` header in the HTTP request. This type of authorization should generally only be used when calling Google APIs hosted on *.googleapis.com.

`.google.events.cloud.scheduler.v1.OAuthToken oauth_token = 5;`

**Returns**  
---  
**Type** | **Description**  
`[OAuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.OAuthToken)` | The oauthToken.  
  
### getOauthTokenOrBuilder()
    
    
    public abstract OAuthTokenOrBuilder getOauthTokenOrBuilder()

If specified, an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) will be generated and attached as an `Authorization` header in the HTTP request. This type of authorization should generally only be used when calling Google APIs hosted on *.googleapis.com.

`.google.events.cloud.scheduler.v1.OAuthToken oauth_token = 5;`

**Returns**  
---  
**Type** | **Description**  
`[OAuthTokenOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.OAuthTokenOrBuilder)` |   
  
### getOidcToken()
    
    
    public abstract OidcToken getOidcToken()

If specified, an [OIDC](https://developers.google.com/identity/protocols/OpenIDConnect) token will be generated and attached as an `Authorization` header in the HTTP request. This type of authorization can be used for many scenarios, including calling Cloud Run, or endpoints where you intend to validate the token yourself.

`.google.events.cloud.scheduler.v1.OidcToken oidc_token = 6;`

**Returns**  
---  
**Type** | **Description**  
`[OidcToken](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.OidcToken)` | The oidcToken.  
  
### getOidcTokenOrBuilder()
    
    
    public abstract OidcTokenOrBuilder getOidcTokenOrBuilder()

If specified, an [OIDC](https://developers.google.com/identity/protocols/OpenIDConnect) token will be generated and attached as an `Authorization` header in the HTTP request. This type of authorization can be used for many scenarios, including calling Cloud Run, or endpoints where you intend to validate the token yourself.

`.google.events.cloud.scheduler.v1.OidcToken oidc_token = 6;`

**Returns**  
---  
**Type** | **Description**  
`[OidcTokenOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.scheduler.v1.OidcTokenOrBuilder)` |   
  
### getUri()
    
    
    public abstract String getUri()

Required. The full URI path that the request will be sent to. This string must begin with either "http://" or "https://". Some examples of valid values for uri are: `<http://acme.com>` and `<https://acme.com/sales:8080>`. Cloud Scheduler will encode some characters for safety and compatibility. The maximum allowed URL length is 2083 characters after encoding.

`string uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uri.  
  
### getUriBytes()
    
    
    public abstract ByteString getUriBytes()

Required. The full URI path that the request will be sent to. This string must begin with either "http://" or "https://". Some examples of valid values for uri are: `<http://acme.com>` and `<https://acme.com/sales:8080>`. Cloud Scheduler will encode some characters for safety and compatibility. The maximum allowed URL length is 2083 characters after encoding.

`string uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uri.  
  
### hasOauthToken()
    
    
    public abstract boolean hasOauthToken()

If specified, an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) will be generated and attached as an `Authorization` header in the HTTP request. This type of authorization should generally only be used when calling Google APIs hosted on *.googleapis.com.

`.google.events.cloud.scheduler.v1.OAuthToken oauth_token = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oauthToken field is set.  
  
### hasOidcToken()
    
    
    public abstract boolean hasOidcToken()

If specified, an [OIDC](https://developers.google.com/identity/protocols/OpenIDConnect) token will be generated and attached as an `Authorization` header in the HTTP request. This type of authorization can be used for many scenarios, including calling Cloud Run, or endpoints where you intend to validate the token yourself.

`.google.events.cloud.scheduler.v1.OidcToken oidc_token = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oidcToken field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
