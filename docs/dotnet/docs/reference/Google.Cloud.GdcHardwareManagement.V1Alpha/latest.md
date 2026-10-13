---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/
title: Google.Cloud.GdcHardwareManagement.V1Alpha \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:29.036806+00:00
---

# Google.Cloud.GdcHardwareManagement.V1Alpha  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.GdcHardwareManagement.V1Alpha Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-alpha08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/)
  * [ 1.0.0-alpha07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/1.0.0-alpha07/)



`Google.Cloud.GdcHardwareManagement.V1Alpha` is a.NET client library for the [GDC Hardware Management API](https://cloud.google.com/distributed-cloud/edge/latest/docs).

Note: This documentation is for version `1.0.0-alpha08` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.GdcHardwareManagement.V1Alpha` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages..."). Please ensure you enable pre-release packages (for example, in the Visual Studio NuGet user interface, check the "Include prerelease" box). Some of the following samples might only work with the latest pre-release version (`1.0.0-alpha08`) of `Google.Cloud.GdcHardwareManagement.V1Alpha`.

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through [GDCHardwareManagementClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.GDCHardwareManagementClient).

Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. GDCHardwareManagementClientBuilder for GDCHardwareManagementClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

### Using the REST (HTTP/1.1) transport

This library defaults to performing RPCs using [gRPC](https://grpc.io/) using the binary [Protocol Buffer](https://protobuf.dev) wire format. However, it also supports HTTP/1.1 and JSON, for situations where gRPC doesn't work as desired. (This is typically due to an incompatible proxy or other network issue.) To create a client using HTTP/1.1, specify a `RestGrpcAdapter` reference for the `GrpcAdapter` property in the client builder. Sample code:
    
    
    var client = new GDCHardwareManagementClientBuilder
    {
        GrpcAdapter = RestGrpcAdapter.Default
    }.Build();
    

For more details, see the [transport selection](https://cloud.google.com/dotnet/docs/reference/help/transports) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
