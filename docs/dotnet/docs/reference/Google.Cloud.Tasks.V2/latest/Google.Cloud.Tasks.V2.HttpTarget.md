---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget
title: Google Cloud Tasks v2 API - Class HttpTarget (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:40.405169+00:00
---

# Google Cloud Tasks v2 API - Class HttpTarget (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2 API - Class HttpTarget (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class HttpTarget : IMessage<HttpTarget>, IEquatable<HttpTarget>, IDeepCloneable<HttpTarget>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Tasks v2 API class HttpTarget.

HTTP target.

When specified at the [Queue][google.cloud.tasks.v2.Queue] level, all tasks with [HttpRequest][google.cloud.tasks.v2.HttpRequest] are overridden according to the target.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > HttpTarget

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[HttpTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[HttpTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[HttpTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2)

## Assembly

Google.Cloud.Tasks.V2.dll

## Constructors 

### HttpTarget()
    
    
    public HttpTarget()

### HttpTarget(HttpTarget)
    
    
    public HttpTarget(HttpTarget other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[HttpTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget)`  
  
  
## Properties 

### AuthorizationHeaderCase
    
    
    public HttpTarget.AuthorizationHeaderOneofCase AuthorizationHeaderCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[HttpTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget)[AuthorizationHeaderOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget.AuthorizationHeaderOneofCase)` |   
  
### HeaderOverrides
    
    
    public RepeatedField<HttpTarget.Types.HeaderOverride> HeaderOverrides { get; }

HTTP target headers.

This map contains the header field names and values. Headers will be set when running the [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask] and/or [BufferTask][google.cloud.tasks.v2.CloudTasks.BufferTask].

These headers represent a subset of the headers that will be configured for the task's HTTP request. Some HTTP request headers will be ignored or replaced.

A partial list of headers that will be ignored or replaced is:

  * Several predefined headers, prefixed with "X-CloudTasks-", can be used to define properties of the task.
  * Host: This will be computed by Cloud Tasks and derived from [HttpRequest.url][google.cloud.tasks.v2.Target.HttpRequest.url].
  * Content-Length: This will be computed by Cloud Tasks.



`Content-Type` won't be set by Cloud Tasks. You can explicitly set `Content-Type` to a media type when the [task is created][google.cloud.tasks.v2.CloudTasks.CreateTask]. For example, `Content-Type` can be set to `"application/octet-stream"` or `"application/json"`. The default value is set to `"application/json"`.

  * User-Agent: This will be set to `"Google-Cloud-Tasks"`.



Headers which can have multiple values (according to RFC2616) can be specified using comma-separated values.

The size of the headers must be less than 80KB. Queue-level headers to override headers of all the tasks in the queue.

Do not put business sensitive or personally identifying data in the HTTP Header Override Configuration or other similar fields in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[HttpTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget.Types)[HeaderOverride](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget.Types.HeaderOverride)` |   
  
### HttpMethod
    
    
    public HttpMethod HttpMethod { get; set; }

The HTTP method to use for the request.

When specified, it overrides [HttpRequest][google.cloud.tasks.v2.HttpTarget.http_method] for the task. Note that if the value is set to [HttpMethod][GET] the [HttpRequest][body] of the task will be ignored at execution time.

**Property Value**  
---  
**Type** | **Description**  
`[HttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpMethod)` |   
  
### OauthToken
    
    
    public OAuthToken OauthToken { get; set; }

If specified, an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) is generated and attached as the `Authorization` header in the HTTP request.

This type of authorization should generally be used only when calling Google APIs hosted on *.googleapis.com. Note that both the service account email and the scope MUST be specified when using the queue-level authorization override.

**Property Value**  
---  
**Type** | **Description**  
`[OAuthToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.OAuthToken)` |   
  
### OidcToken
    
    
    public OidcToken OidcToken { get; set; }

If specified, an [OIDC](https://developers.google.com/identity/protocols/OpenIDConnect) token is generated and attached as an `Authorization` header in the HTTP request.

This type of authorization can be used for many scenarios, including calling Cloud Run, or endpoints where you intend to validate the token yourself. Note that both the service account email and the audience MUST be specified when using the queue-level authorization override.

**Property Value**  
---  
**Type** | **Description**  
`[OidcToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.OidcToken)` |   
  
### UriOverride
    
    
    public UriOverride UriOverride { get; set; }

URI override.

When specified, overrides the execution URI for all the tasks in the queue.

**Property Value**  
---  
**Type** | **Description**  
`[UriOverride](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UriOverride)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
