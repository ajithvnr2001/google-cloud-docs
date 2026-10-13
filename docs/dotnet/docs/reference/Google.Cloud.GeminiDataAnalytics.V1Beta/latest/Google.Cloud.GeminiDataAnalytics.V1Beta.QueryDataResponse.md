---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.QueryDataResponse
title: Data Analytics API with Gemini v1beta API - Class QueryDataResponse (1.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:39.023043+00:00
---

# Data Analytics API with Gemini v1beta API - Class QueryDataResponse (1.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.QueryDataResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1beta API - Class QueryDataResponse (1.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta12 (latest)  1.0.0-beta11 
    
    
    public sealed class QueryDataResponse : IMessage<QueryDataResponse>, IEquatable<QueryDataResponse>, IDeepCloneable<QueryDataResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1beta API class QueryDataResponse.

Response containing the generated query and related information.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QueryDataResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[QueryDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.QueryDataResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QueryDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.QueryDataResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[QueryDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.QueryDataResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1Beta.dll

## Constructors 

### QueryDataResponse()
    
    
    public QueryDataResponse()

### QueryDataResponse(QueryDataResponse)
    
    
    public QueryDataResponse(QueryDataResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QueryDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.QueryDataResponse)`  
  
  
## Properties 

### DisambiguationQuestion
    
    
    public RepeatedField<string> DisambiguationQuestion { get; }

If ambiguity was detected in the natural language query and options.generate_disambiguation_question was true, this field contains a question to the user for clarification. The returned represents the service's best effort based on the ambiguous input.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GeneratedQuery
    
    
    public string GeneratedQuery { get; set; }

Generated query for the given user prompt.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IntentExplanation
    
    
    public string IntentExplanation { get; set; }

A natural language explanation of the generated query. Populated if options.generate_explanation was true in the request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NaturalLanguageAnswer
    
    
    public string NaturalLanguageAnswer { get; set; }

A natural language answer to the query, based on the query_result. Populated if options.generate_natural_language_answer was true in the request and query execution was successful based in the response from executeSql API.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PipelineDebugInfo
    
    
    public Struct PipelineDebugInfo { get; set; }

Detailed step-by-step pipeline execution information. Populated only if generation_options.generate_debug_info was true. Provided for debugging and transparency purposes only. The structure and content of this object is not guaranteed and may change at any time without notice. Do not write production code or business logic depending on the fields in this object.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### QueryResult
    
    
    public ExecutedQueryResult QueryResult { get; set; }

The result of executing the query. Populated if options.generate_query_result or options.generate_natural_language_answer was true in the request, and execution was successful or attempted.

**Property Value**  
---  
**Type** | **Description**  
`[ExecutedQueryResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.ExecutedQueryResult)` |   
  
### TokenUsage
    
    
    public TokenUsage TokenUsage { get; set; }

Overall token usage for the request.

**Property Value**  
---  
**Type** | **Description**  
`[TokenUsage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.TokenUsage)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
