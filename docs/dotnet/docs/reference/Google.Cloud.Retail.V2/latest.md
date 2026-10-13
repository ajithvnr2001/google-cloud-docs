---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:49.282670+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.15.0/)
  * [ 2.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.14.0/)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.13.0/)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.12.0/)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.11.0/)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.10.0/)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.9.0/)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.8.0/)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.7.0/)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.6.0/)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.5.0/)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.4.0/)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.3.0/)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.2.0/)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.1.0/)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.0.0/)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.6.0/)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.5.0/)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.4.0/)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.3.0/)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.2.0/)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.1.0/)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.0.0/)



# Google.Cloud.Retail.V2

`Google.Cloud.Retail.V2` is a.NET client library for the [Retail API](https://cloud.google.com/retail/docs).

## Note: early access users only

Some features exposed by this package are currently protected by an allow-list, and will not work for customers who are not registered in the early access programme.

Please use the [contact page](https://cloud.google.com/contact) to apply for access.

Note: This documentation is for version `2.16.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Retail.V2` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [AnalyticsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AnalyticsServiceClient)
  * [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.CatalogServiceClient)
  * [CompletionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.CompletionServiceClient)
  * [ControlServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.ControlServiceClient)
  * [ConversationalSearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.ConversationalSearchServiceClient)
  * [GenerativeQuestionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.GenerativeQuestionServiceClient)
  * [ModelServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.ModelServiceClient)
  * [PredictionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.PredictionServiceClient)
  * [ProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.ProductServiceClient)
  * [SearchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.SearchServiceClient)
  * [ServingConfigServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.ServingConfigServiceClient)
  * [UserEventServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.UserEventServiceClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. AnalyticsServiceClientBuilder for AnalyticsServiceClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

### Using the REST (HTTP/1.1) transport

This library defaults to performing RPCs using [gRPC](https://grpc.io/) using the binary [Protocol Buffer](https://protobuf.dev) wire format. However, it also supports HTTP/1.1 and JSON, for situations where gRPC doesn't work as desired. (This is typically due to an incompatible proxy or other network issue.) To create a client using HTTP/1.1, specify a `RestGrpcAdapter` reference for the `GrpcAdapter` property in the client builder. Sample code:
    
    
    var client = new AnalyticsServiceClientBuilder
    {
        GrpcAdapter = RestGrpcAdapter.Default
    }.Build();
    

For more details, see the [transport selection](https://cloud.google.com/dotnet/docs/reference/help/transports) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
