---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.DisposeBehavior
title: Google.Cloud.Spanner.Data - Enum DisposeBehavior (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:20.717454+00:00
---

# Google.Cloud.Spanner.Data - Enum DisposeBehavior (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.DisposeBehavior

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Spanner.Data - Enum DisposeBehavior (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public enum DisposeBehavior

Reference documentation and code samples for the Google.Cloud.Spanner.Data enum DisposeBehavior.

Defines the behavior of [SpannerTransaction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerTransaction) when Dispose is called. [DisposeBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerTransaction#Google_Cloud_Spanner_Data_SpannerTransaction_DisposeBehavior) for more information.

## Namespace

[Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data)

## Assembly

Google.Cloud.Spanner.Data.dll

## Fields   
  
---  
**Name** | **Description**  
`CloseResources` | Automatically closes resources when [Dispose(bool)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerTransaction#Google_Cloud_Spanner_Data_SpannerTransaction_Dispose_System_Boolean_) is called.  
`Default` | For transactions with pooled resources, releases transactional resources back to the pool when [Dispose(bool)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerTransaction#Google_Cloud_Spanner_Data_SpannerTransaction_Dispose_System_Boolean_) is called. Otherwise calling [Dispose(bool)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerTransaction#Google_Cloud_Spanner_Data_SpannerTransaction_Dispose_System_Boolean_) has no effect on the transaction resources.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
