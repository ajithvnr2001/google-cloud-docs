---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.OrderingKeyInErrorStateException
title: Cloud Pub/Sub v1 API - Class OrderingKeyInErrorStateException (3.39.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:57.048728+00:00
---

# Cloud Pub/Sub v1 API - Class OrderingKeyInErrorStateException (3.39.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.OrderingKeyInErrorStateException

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Pub/Sub v1 API - Class OrderingKeyInErrorStateException (3.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.39.0 (latest)  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.1  3.9.1  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public class OrderingKeyInErrorStateException : InvalidOperationException, ISerializable

Reference documentation and code samples for the Cloud Pub/Sub v1 API class OrderingKeyInErrorStateException.

Exception thrown when publishing a message with an ordering key that is in an error state.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [Exception](https://learn.microsoft.com/dotnet/api/system.exception) > [SystemException](https://learn.microsoft.com/dotnet/api/system.systemexception) > [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception) > OrderingKeyInErrorStateException

## Implements

[ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)

## Inherited Members

[Exception.GetBaseException()](https://learn.microsoft.com/dotnet/api/system.exception.getbaseexception)

[Exception.GetObjectData(SerializationInfo, StreamingContext)](https://learn.microsoft.com/dotnet/api/system.exception.getobjectdata)

[Exception.GetType()](https://learn.microsoft.com/dotnet/api/system.exception.gettype)

[Exception.ToString()](https://learn.microsoft.com/dotnet/api/system.exception.tostring)

[Exception.Data](https://learn.microsoft.com/dotnet/api/system.exception.data)

[Exception.HelpLink](https://learn.microsoft.com/dotnet/api/system.exception.helplink)

[Exception.HResult](https://learn.microsoft.com/dotnet/api/system.exception.hresult)

[Exception.InnerException](https://learn.microsoft.com/dotnet/api/system.exception.innerexception)

[Exception.Message](https://learn.microsoft.com/dotnet/api/system.exception.message)

[Exception.Source](https://learn.microsoft.com/dotnet/api/system.exception.source)

[Exception.StackTrace](https://learn.microsoft.com/dotnet/api/system.exception.stacktrace)

[Exception.TargetSite](https://learn.microsoft.com/dotnet/api/system.exception.targetsite)

[Exception.SerializeObjectState](https://learn.microsoft.com/dotnet/api/system.exception.serializeobjectstate)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

## Namespace

[Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1)

## Assembly

Google.Cloud.PubSub.V1.dll

## Constructors 

### OrderingKeyInErrorStateException(string)
    
    
    public OrderingKeyInErrorStateException(string orderingKey)

Construct an [OrderingKeyInErrorStateException](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.OrderingKeyInErrorStateException) instance.

**Parameter**  
---  
**Name** | **Description**  
`orderingKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The ordering key that is in an error state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
