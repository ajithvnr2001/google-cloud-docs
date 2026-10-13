---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateServiceRequest
title: App Engine v1 API - Class UpdateServiceRequest (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:45.709585+00:00
---

# App Engine v1 API - Class UpdateServiceRequest (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateServiceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Engine v1 API - Class UpdateServiceRequest (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.4.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.3.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.2.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.1.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.0.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.4.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.3.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.2.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.1.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.0.0/Google.Cloud.AppEngine.V1.UpdateServiceRequest)


    
    
    public sealed class UpdateServiceRequest : IMessage<UpdateServiceRequest>, IEquatable<UpdateServiceRequest>, IDeepCloneable<UpdateServiceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the App Engine v1 API class UpdateServiceRequest.

Request message for `Services.UpdateService`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateServiceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateServiceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateServiceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateServiceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AppEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1)

## Assembly

Google.Cloud.AppEngine.V1.dll

## Constructors 

### UpdateServiceRequest()
    
    
    public UpdateServiceRequest()

### UpdateServiceRequest(UpdateServiceRequest)
    
    
    public UpdateServiceRequest(UpdateServiceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateServiceRequest)`  
  
  
## Properties 

### MigrateTraffic
    
    
    public bool MigrateTraffic { get; set; }

Set to `true` to gradually shift traffic to one or more versions that you specify. By default, traffic is shifted immediately. For gradual traffic migration, the target versions must be located within instances that are configured for both [warmup requests](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#InboundServiceType) and [automatic scaling](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AutomaticScaling). You must specify the [`shardBy`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#ShardBy) field in the Service resource. Gradual traffic migration is not supported in the App Engine flexible environment. For examples, see [Migrating and Splitting Traffic](https://cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic).

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Name
    
    
    public string Name { get; set; }

Name of the resource to update. Example: `apps/myapp/services/default`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Service
    
    
    public Service Service { get; set; }

A Service resource containing the updated service. Only fields set in the field mask will be updated.

**Property Value**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Service)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. Standard field mask for the set of fields to be updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
