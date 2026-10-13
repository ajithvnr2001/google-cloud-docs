---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount
title: Cloud Billing Budget v1beta1 API - Class LastPeriodAmount (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:50.127317+00:00
---

# Cloud Billing Budget v1beta1 API - Class LastPeriodAmount (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Billing Budget v1beta1 API - Class LastPeriodAmount (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/2.0.0-beta06/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/1.0.0-beta05/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount)


    
    
    public sealed class LastPeriodAmount : IMessage<LastPeriodAmount>, IEquatable<LastPeriodAmount>, IDeepCloneable<LastPeriodAmount>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Billing Budget v1beta1 API class LastPeriodAmount.

Describes a budget amount targeted to the last [Filter.calendar_period][google.cloud.billing.budgets.v1beta1.Filter.calendar_period] spend. At this time, the amount is automatically 100% of the last calendar period's spend; that is, there are no other options yet. Future configuration options will be described here (for example, configuring a percentage of last period's spend). LastPeriodAmount cannot be set for a budget configured with a [Filter.custom_period][google.cloud.billing.budgets.v1beta1.Filter.custom_period].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LastPeriodAmount

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[LastPeriodAmount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[LastPeriodAmount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[LastPeriodAmount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Billing.Budgets.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1)

## Assembly

Google.Cloud.Billing.Budgets.V1Beta1.dll

## Constructors 

### LastPeriodAmount()
    
    
    public LastPeriodAmount()

### LastPeriodAmount(LastPeriodAmount)
    
    
    public LastPeriodAmount(LastPeriodAmount other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[LastPeriodAmount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.LastPeriodAmount)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
