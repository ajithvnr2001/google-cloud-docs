---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest
title: Google Cloud Security Command Center v1p1beta1 API - Class UpdateNotificationConfigRequest (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:52.816383+00:00
---

# Google Cloud Security Command Center v1p1beta1 API - Class UpdateNotificationConfigRequest (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1p1beta1 API - Class UpdateNotificationConfigRequest (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/3.0.0-beta05/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/2.0.0-beta07/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest)


    
    
    public sealed class UpdateNotificationConfigRequest : IMessage<UpdateNotificationConfigRequest>, IEquatable<UpdateNotificationConfigRequest>, IDeepCloneable<UpdateNotificationConfigRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center v1p1beta1 API class UpdateNotificationConfigRequest.

Request message for updating a notification config.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateNotificationConfigRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V1P1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1)

## Assembly

Google.Cloud.SecurityCenter.V1P1Beta1.dll

## Constructors 

### UpdateNotificationConfigRequest()
    
    
    public UpdateNotificationConfigRequest()

### UpdateNotificationConfigRequest(UpdateNotificationConfigRequest)
    
    
    public UpdateNotificationConfigRequest(UpdateNotificationConfigRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest)`  
  
  
## Properties 

### NotificationConfig
    
    
    public NotificationConfig NotificationConfig { get; set; }

Required. The notification config to update.

**Property Value**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfig)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

The FieldMask to use when updating the notification config.

If empty all mutable fields will be updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
