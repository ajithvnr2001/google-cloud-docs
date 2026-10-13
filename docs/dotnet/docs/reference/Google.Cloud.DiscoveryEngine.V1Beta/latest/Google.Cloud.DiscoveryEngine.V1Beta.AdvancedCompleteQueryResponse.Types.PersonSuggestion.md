---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion
title: Discovery Engine v1beta API - Class AdvancedCompleteQueryResponse.Types.PersonSuggestion (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:41.402905+00:00
---

# Discovery Engine v1beta API - Class AdvancedCompleteQueryResponse.Types.PersonSuggestion (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class AdvancedCompleteQueryResponse.Types.PersonSuggestion (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class AdvancedCompleteQueryResponse.Types.PersonSuggestion : IMessage<AdvancedCompleteQueryResponse.Types.PersonSuggestion>, IEquatable<AdvancedCompleteQueryResponse.Types.PersonSuggestion>, IDeepCloneable<AdvancedCompleteQueryResponse.Types.PersonSuggestion>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class AdvancedCompleteQueryResponse.Types.PersonSuggestion.

Suggestions as people.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AdvancedCompleteQueryResponse.Types.PersonSuggestion

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AdvancedCompleteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types)[PersonSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AdvancedCompleteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types)[PersonSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AdvancedCompleteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types)[PersonSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### PersonSuggestion()
    
    
    public PersonSuggestion()

### PersonSuggestion(PersonSuggestion)
    
    
    public PersonSuggestion(AdvancedCompleteQueryResponse.Types.PersonSuggestion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AdvancedCompleteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types)[PersonSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion)`  
  
  
## Properties 

### DataStore
    
    
    public string DataStore { get; set; }

The name of the dataStore that this suggestion belongs to.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DataStoreAsDataStoreName
    
    
    public DataStoreName DataStoreAsDataStoreName { get; set; }

[DataStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStoreName)-typed view over the [DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion#Google_Cloud_DiscoveryEngine_V1Beta_AdvancedCompleteQueryResponse_Types_PersonSuggestion_DataStore) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DataStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStoreName)` |   
  
### DestinationUri
    
    
    public string DestinationUri { get; set; }

The destination uri of the person suggestion.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayPhotoUri
    
    
    public string DisplayPhotoUri { get; set; }

The photo uri of the person suggestion.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Document
    
    
    public Document Document { get; set; }

The document data snippet in the suggestion. Only a subset of fields is populated.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` |   
  
### PersonType
    
    
    public AdvancedCompleteQueryResponse.Types.PersonSuggestion.Types.PersonType PersonType { get; set; }

The type of the person.

**Property Value**  
---  
**Type** | **Description**  
`[AdvancedCompleteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types)[PersonSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion.Types)[PersonType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse.Types.PersonSuggestion.Types.PersonType)` |   
  
### Score
    
    
    public double Score { get; set; }

The score of each suggestion. The score is in the range of [0, 1].

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### Suggestion
    
    
    public string Suggestion { get; set; }

The suggestion for the query.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
