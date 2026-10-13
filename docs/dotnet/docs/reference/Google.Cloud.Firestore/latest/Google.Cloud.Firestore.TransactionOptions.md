---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.TransactionOptions
title: Firestore API - Class TransactionOptions (4.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:56.658531+00:00
---

# Firestore API - Class TransactionOptions (4.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.TransactionOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Firestore API - Class TransactionOptions (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.1 
    
    
    public sealed class TransactionOptions

Reference documentation and code samples for the Firestore API class TransactionOptions.

Immutable class representing options for executing transactions.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TransactionOptions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore)

## Assembly

Google.Cloud.Firestore.dll

## Properties 

### Default
    
    
    public static TransactionOptions Default { get; }

The transaction options that are used if nothing is specified by the caller.

**Property Value**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.TransactionOptions)` |   
  
### MaxAttempts
    
    
    public int MaxAttempts { get; }

The number of times the transaction will be attempted before failing. This is equivalent to [MaxAttempts](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html#Google_Api_Gax_Grpc_RetrySettings_MaxAttempts).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### RetrySettings
    
    
    public RetrySettings RetrySettings { get; }

The settings to control the timing of retries within the transaction. The [RetryFilter](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html#Google_Api_Gax_Grpc_RetrySettings_RetryFilter) property is ignored. This property is never null.

**Property Value**  
---  
**Type** | **Description**  
`[RetrySettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html)` |   
  
## Methods 

### ForMaxAttempts(int)
    
    
    public static TransactionOptions ForMaxAttempts(int maxAttempts)

Creates an instance with the given maximum number of attempts. The default retry timing will be used.

**Parameter**  
---  
**Name** | **Description**  
`maxAttempts` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The number of times a transaction will be attempted before failing. Must be positive.  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.TransactionOptions)` | A new options object.  
  
### ForRetrySettings(RetrySettings)
    
    
    public static TransactionOptions ForRetrySettings(RetrySettings retrySettings)

Creates an instance with the given retry settings, including maximum number of attempts. The [RetryFilter](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html#Google_Api_Gax_Grpc_RetrySettings_RetryFilter) property is not used.

**Parameter**  
---  
**Name** | **Description**  
`retrySettings` | `[RetrySettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html)`  
The retry settings to use. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.TransactionOptions)` | A new options object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
