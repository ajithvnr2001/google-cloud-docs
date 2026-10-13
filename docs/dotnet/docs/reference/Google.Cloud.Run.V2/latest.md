---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:27.385537+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.19.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/)
  * [ 2.18.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.18.0/)
  * [ 2.17.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.17.0/)
  * [ 2.16.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.16.0/)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.15.0/)
  * [ 2.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.14.0/)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.13.0/)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.12.0/)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.11.0/)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.10.0/)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.9.0/)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.8.0/)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.7.0/)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.6.0/)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.5.0/)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.4.0/)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.3.0/)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.2.0/)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.1.0/)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/2.0.0/)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/1.0.0-beta02/)



# Google.Cloud.Run.V2

`Google.Cloud.Run.V2` is a.NET client library for the [Cloud Run Admin API](https://cloud.google.com/run/docs).

Note: This documentation is for version `2.18.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Run.V2` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [BuildsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.BuildsClient)
  * [ExecutionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ExecutionsClient)
  * [JobsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.JobsClient)
  * [RevisionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.RevisionsClient)
  * [ServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ServicesClient)
  * [TasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.TasksClient)
  * [WorkerPoolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.WorkerPoolsClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. BuildsClientBuilder for BuildsClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

### Using the REST (HTTP/1.1) transport

This library defaults to performing RPCs using [gRPC](https://grpc.io/) using the binary [Protocol Buffer](https://protobuf.dev) wire format. However, it also supports HTTP/1.1 and JSON, for situations where gRPC doesn't work as desired. (This is typically due to an incompatible proxy or other network issue.) To create a client using HTTP/1.1, specify a `RestGrpcAdapter` reference for the `GrpcAdapter` property in the client builder. Sample code:
    
    
    var client = new BuildsClientBuilder
    {
        GrpcAdapter = RestGrpcAdapter.Default
    }.Build();
    

For more details, see the [transport selection](https://cloud.google.com/dotnet/docs/reference/help/transports) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
