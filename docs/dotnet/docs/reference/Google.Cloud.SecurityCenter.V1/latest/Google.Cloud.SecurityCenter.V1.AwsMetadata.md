---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata
title: Google Cloud Security Command Center v1 API - Class AwsMetadata (3.28.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:55.290898+00:00
---

# Google Cloud Security Command Center v1 API - Class AwsMetadata (3.28.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1 API - Class AwsMetadata (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class AwsMetadata : IMessage<AwsMetadata>, IEquatable<AwsMetadata>, IDeepCloneable<AwsMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center v1 API class AwsMetadata.

AWS metadata associated with the resource, only applicable if the finding's cloud provider is Amazon Web Services.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AwsMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AwsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AwsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AwsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1)

## Assembly

Google.Cloud.SecurityCenter.V1.dll

## Constructors 

### AwsMetadata()
    
    
    public AwsMetadata()

### AwsMetadata(AwsMetadata)
    
    
    public AwsMetadata(AwsMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AwsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata)`  
  
  
## Properties 

### Account
    
    
    public AwsMetadata.Types.AwsAccount Account { get; set; }

The AWS account associated with the resource.

**Property Value**  
---  
**Type** | **Description**  
`[AwsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata.Types)[AwsAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata.Types.AwsAccount)` |   
  
### Organization
    
    
    public AwsMetadata.Types.AwsOrganization Organization { get; set; }

The AWS organization associated with the resource.

**Property Value**  
---  
**Type** | **Description**  
`[AwsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata.Types)[AwsOrganization](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata.Types.AwsOrganization)` |   
  
### OrganizationalUnits
    
    
    public RepeatedField<AwsMetadata.Types.AwsOrganizationalUnit> OrganizationalUnits { get; }

A list of AWS organizational units associated with the resource, ordered from lowest level (closest to the account) to highest level.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AwsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata.Types)[AwsOrganizationalUnit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.AwsMetadata.Types.AwsOrganizationalUnit)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
