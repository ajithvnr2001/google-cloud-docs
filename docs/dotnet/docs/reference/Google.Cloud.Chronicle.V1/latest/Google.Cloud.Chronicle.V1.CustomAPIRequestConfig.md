---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig
title: Chronicle v1 API - Class CustomAPIRequestConfig (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:54.029967+00:00
---

# Chronicle v1 API - Class CustomAPIRequestConfig (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class CustomAPIRequestConfig (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class CustomAPIRequestConfig : IMessage<CustomAPIRequestConfig>, IEquatable<CustomAPIRequestConfig>, IDeepCloneable<CustomAPIRequestConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class CustomAPIRequestConfig.

Configuration for the outgoing API request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CustomAPIRequestConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CustomAPIRequestConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CustomAPIRequestConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CustomAPIRequestConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### CustomAPIRequestConfig()
    
    
    public CustomAPIRequestConfig()

### CustomAPIRequestConfig(CustomAPIRequestConfig)
    
    
    public CustomAPIRequestConfig(CustomAPIRequestConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CustomAPIRequestConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig)`  
  
  
## Properties 

### CustomHeaders
    
    
    public RepeatedField<HeaderKeyValue> CustomHeaders { get; }

Optional. Define specialized key-value pairs sent with the request, often used for custom API versioning or specific vendor requirements.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[HeaderKeyValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.HeaderKeyValue)` |   
  
### EndpointPath
    
    
    public string EndpointPath { get; set; }

Required. Enter the specific API route appended to the Base URL to fetch the data (e.g., /v1/alerts).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HttpMethod
    
    
    public CustomAPIRequestConfig.Types.HttpMethod HttpMethod { get; set; }

Required. Select the type of action to perform on the API endpoint (usually GET to retrieve data or POST to submit a query).

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPIRequestConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig.Types)[HttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIRequestConfig.Types.HttpMethod)` |   
  
### MaxRequestsPerMinute
    
    
    public int MaxRequestsPerMinute { get; set; }

Optional. Set a safety limit to ensure the connector does not exceed the third-party vendor's API rate limits.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### QueryParameters
    
    
    public RepeatedField<HeaderKeyValue> QueryParameters { get; }

Optional. Add extra filters or settings appended to the end of the URL (e.g., ?status=critical).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[HeaderKeyValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.HeaderKeyValue)` |   
  
### RequestBody
    
    
    public string RequestBody { get; set; }

Optional. Provide the data payload sent to the API to specify what information you want, typically formatted in JSON.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
