---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher
title: Network Services v1beta1 API - Class EndpointMatcher.Types.MetadataLabelMatcher (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:50.780724+00:00
---

# Network Services v1beta1 API - Class EndpointMatcher.Types.MetadataLabelMatcher (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1beta1 API - Class EndpointMatcher.Types.MetadataLabelMatcher (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class EndpointMatcher.Types.MetadataLabelMatcher : IMessage<EndpointMatcher.Types.MetadataLabelMatcher>, IEquatable<EndpointMatcher.Types.MetadataLabelMatcher>, IDeepCloneable<EndpointMatcher.Types.MetadataLabelMatcher>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Services v1beta1 API class EndpointMatcher.Types.MetadataLabelMatcher.

The matcher that is based on node metadata presented by xDS clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EndpointMatcher.Types.MetadataLabelMatcher

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[EndpointMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types)[MetadataLabelMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[EndpointMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types)[MetadataLabelMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[EndpointMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types)[MetadataLabelMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1)

## Assembly

Google.Cloud.NetworkServices.V1Beta1.dll

## Constructors 

### MetadataLabelMatcher()
    
    
    public MetadataLabelMatcher()

### MetadataLabelMatcher(MetadataLabelMatcher)
    
    
    public MetadataLabelMatcher(EndpointMatcher.Types.MetadataLabelMatcher other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[EndpointMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types)[MetadataLabelMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher)`  
  
  
## Properties 

### MetadataLabelMatchCriteria
    
    
    public EndpointMatcher.Types.MetadataLabelMatcher.Types.MetadataLabelMatchCriteria MetadataLabelMatchCriteria { get; set; }

Specifies how matching should be done.

Supported values are: MATCH_ANY: At least one of the Labels specified in the matcher should match the metadata presented by xDS client. MATCH_ALL: The metadata presented by the xDS client should contain all of the labels specified here.

The selection is determined based on the best match. For example, suppose there are three EndpointPolicy resources P1, P2 and P3 and if P1 has a the matcher as MATCH_ANY <A:1, B:1>, P2 has MATCH_ALL <A:1,B:1>, and P3 has MATCH_ALL <A:1,B:1,C:1>.

If a client with label <A:1> connects, the config from P1 will be selected.

If a client with label <A:1,B:1> connects, the config from P2 will be selected.

If a client with label <A:1,B:1,C:1> connects, the config from P3 will be selected.

If there is more than one best match, (for example, if a config P4 with selector <A:1,D:1> exists and if a client with label <A:1,B:1,D:1> connects), an error will be thrown.

**Property Value**  
---  
**Type** | **Description**  
`[EndpointMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types)[MetadataLabelMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher.Types)[MetadataLabelMatchCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher.Types.MetadataLabelMatchCriteria)` |   
  
### MetadataLabels
    
    
    public RepeatedField<EndpointMatcher.Types.MetadataLabelMatcher.Types.MetadataLabels> MetadataLabels { get; }

The list of label value pairs that must match labels in the provided metadata based on filterMatchCriteria This list can have at most 64 entries. The list can be empty if the match criteria is MATCH_ANY, to specify a wildcard match (i.e this matches any client).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EndpointMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types)[MetadataLabelMatcher](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher.Types)[MetadataLabels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointMatcher.Types.MetadataLabelMatcher.Types.MetadataLabels)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
