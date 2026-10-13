---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/
title: Google.Cloud.GeminiDataAnalytics.V1Beta \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:29.862613+00:00
---

# Google.Cloud.GeminiDataAnalytics.V1Beta  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.GeminiDataAnalytics.V1Beta Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta12 (latest)  1.0.0-beta11 

`Google.Cloud.GeminiDataAnalytics.V1Beta` is a.NET client library for the [Data Analytics API with Gemini API](https://cloud.google.com/gemini/docs/conversational-analytics-api/overview).

Note: This documentation is for version `1.0.0-beta12` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.GeminiDataAnalytics.V1Beta` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages..."). Please ensure you enable pre-release packages (for example, in the Visual Studio NuGet user interface, check the "Include prerelease" box). Some of the following samples might only work with the latest pre-release version (`1.0.0-beta12`) of `Google.Cloud.GeminiDataAnalytics.V1Beta`.

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [DataA2AServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataA2AServiceClient)
  * [DataAgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataAgentServiceClient)
  * [DataChatServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataChatServiceClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. DataA2AServiceClientBuilder for DataA2AServiceClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

### Using the REST (HTTP/1.1) transport

This library defaults to performing RPCs using [gRPC](https://grpc.io/) using the binary [Protocol Buffer](https://protobuf.dev) wire format. However, it also supports HTTP/1.1 and JSON, for situations where gRPC doesn't work as desired. (This is typically due to an incompatible proxy or other network issue.) To create a client using HTTP/1.1, specify a `RestGrpcAdapter` reference for the `GrpcAdapter` property in the client builder. Sample code:
    
    
    var client = new DataA2AServiceClientBuilder
    {
        GrpcAdapter = RestGrpcAdapter.Default
    }.Build();
    

For more details, see the [transport selection](https://cloud.google.com/dotnet/docs/reference/help/transports) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
