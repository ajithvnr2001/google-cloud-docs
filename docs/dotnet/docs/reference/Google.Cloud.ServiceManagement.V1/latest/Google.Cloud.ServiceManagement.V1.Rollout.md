---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout
title: Service Management v1 API - Class Rollout (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:41.937376+00:00
---

# Service Management v1 API - Class Rollout (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Management v1 API - Class Rollout (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.4.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.3.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.2.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.1.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.0.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.5.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.4.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.3.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.2.0/Google.Cloud.ServiceManagement.V1.Rollout)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.1.0/Google.Cloud.ServiceManagement.V1.Rollout)


    
    
    public sealed class Rollout : IMessage<Rollout>, IEquatable<Rollout>, IDeepCloneable<Rollout>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Management v1 API class Rollout.

A rollout resource that defines how service configuration versions are pushed to control plane systems. Typically, you create a new version of the service config, and then create a Rollout to push the service config.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Rollout

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1)

## Assembly

Google.Cloud.ServiceManagement.V1.dll

## Constructors 

### Rollout()
    
    
    public Rollout()

### Rollout(Rollout)
    
    
    public Rollout(Rollout other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Creation time of the rollout. Readonly.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### CreatedBy
    
    
    public string CreatedBy { get; set; }

The user who created the Rollout. Readonly.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DeleteServiceStrategy
    
    
    public Rollout.Types.DeleteServiceStrategy DeleteServiceStrategy { get; set; }

The strategy associated with a rollout to delete a `ManagedService`. Readonly.

**Property Value**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types)[DeleteServiceStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types.DeleteServiceStrategy)` |   
  
### RolloutId
    
    
    public string RolloutId { get; set; }

Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed.

If not specified by client, the server will generate one. The generated id will have the form of <date><revision number>, where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceName
    
    
    public string ServiceName { get; set; }

The name of the service associated with this Rollout.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Status
    
    
    public Rollout.Types.RolloutStatus Status { get; set; }

The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.

**Property Value**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types)[RolloutStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)` |   
  
### StrategyCase
    
    
    public Rollout.StrategyOneofCase StrategyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout)[StrategyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.StrategyOneofCase)` |   
  
### TrafficPercentStrategy
    
    
    public Rollout.Types.TrafficPercentStrategy TrafficPercentStrategy { get; set; }

Google Service Control selects service configurations based on traffic percentage.

**Property Value**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types)[TrafficPercentStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types.TrafficPercentStrategy)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
