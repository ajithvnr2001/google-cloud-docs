---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet
title: Oracle Database@Google Cloud v1 API - Class OdbSubnet (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:42.853777+00:00
---

# Oracle Database@Google Cloud v1 API - Class OdbSubnet (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class OdbSubnet (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class OdbSubnet : IMessage<OdbSubnet>, IEquatable<OdbSubnet>, IDeepCloneable<OdbSubnet>, IBufferMessage, IMessage

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class OdbSubnet.

Represents OdbSubnet resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OdbSubnet

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### OdbSubnet()
    
    
    public OdbSubnet()

### OdbSubnet(OdbSubnet)
    
    
    public OdbSubnet(OdbSubnet other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet)`  
  
  
## Properties 

### CidrRange
    
    
    public string CidrRange { get; set; }

Required. The CIDR range of the subnet.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The date and time that the OdbNetwork was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. Labels or tags associated with the resource.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The name of the OdbSubnet resource in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OdbSubnetName
    
    
    public OdbSubnetName OdbSubnetName { get; set; }

[OdbSubnetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnetName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet#Google_Cloud_OracleDatabase_V1_OdbSubnet_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OdbSubnetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnetName)` |   
  
### Purpose
    
    
    public OdbSubnet.Types.Purpose Purpose { get; set; }

Required. Purpose of the subnet.

**Property Value**  
---  
**Type** | **Description**  
`[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet.Types)[Purpose](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet.Types.Purpose)` |   
  
### State
    
    
    public OdbSubnet.Types.State State { get; set; }

Output only. State of the ODB Subnet.

**Property Value**  
---  
**Type** | **Description**  
`[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet.Types.State)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
