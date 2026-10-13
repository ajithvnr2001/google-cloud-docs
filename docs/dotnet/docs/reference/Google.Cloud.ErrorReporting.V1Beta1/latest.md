---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:27.055909+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/3.0.0-beta05/)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/2.0.0-beta05/)



# Google.Cloud.ErrorReporting.V1Beta1

`Google.Cloud.ErrorReporting.V1Beta1` is a.NET client library for the [Google Cloud Error Reporting API](https://cloud.google.com/error-reporting/).

Note: This documentation is for version `3.0.0-beta06` of the library. Some samples may not work with other versions.

Support for automatic error reporting can be found in the [`Google.Cloud.Diagnostics.AspNetCore`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/latest) and [`Google.Cloud.Diagnostics.AspNetCore3`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore3/latest) NuGet packages.

Those packages are generally preferred over using the Error Reporting API directly.

## Installation

Install the `Google.Cloud.ErrorReporting.V1Beta1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages..."). Please ensure you enable pre-release packages (for example, in the Visual Studio NuGet user interface, check the "Include prerelease" box). Some of the following samples might only work with the latest pre-release version (`3.0.0-beta06`) of `Google.Cloud.ErrorReporting.V1Beta1`.

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [ErrorGroupServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorGroupServiceClient)
  * [ErrorStatsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ErrorStatsServiceClient)
  * [ReportErrorsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsServiceClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. ErrorGroupServiceClientBuilder for ErrorGroupServiceClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

### Using the REST (HTTP/1.1) transport

This library defaults to performing RPCs using [gRPC](https://grpc.io/) using the binary [Protocol Buffer](https://protobuf.dev) wire format. However, it also supports HTTP/1.1 and JSON, for situations where gRPC doesn't work as desired. (This is typically due to an incompatible proxy or other network issue.) To create a client using HTTP/1.1, specify a `RestGrpcAdapter` reference for the `GrpcAdapter` property in the client builder. Sample code:
    
    
    var client = new ErrorGroupServiceClientBuilder
    {
        GrpcAdapter = RestGrpcAdapter.Default
    }.Build();
    

For more details, see the [transport selection](https://cloud.google.com/dotnet/docs/reference/help/transports) page.

## Sample code using the Error Reporting API directly

## Report an error
    
    
    ReportErrorsServiceClient client = ReportErrorsServiceClient.Create();
    ProjectName projectName = new ProjectName(projectId);
    ReportedErrorEvent error = new ReportedErrorEvent
    {
        Context = new ErrorContext
        {
            ReportLocation = new SourceLocation
            {
                FilePath = "SampleApp.BusinessLogic/ComplexLogic.cs",
                FunctionName = "ComputeTrickyAnswer",
                LineNumber = 100
            },
            User = "userid"
        },
    
        // If this is a stack trace, the service will parse it.
        Message = "Computation failed",
    
        EventTime = Timestamp.FromDateTime(DateTime.UtcNow),
        ServiceContext = new ServiceContext
        {
            Service = "SampleApp",
            Version = "1.0.0"
        }
    };
    client.ReportErrorEvent(projectName, error);
    

## List error groups with statistics
    
    
    ErrorStatsServiceClient client = ErrorStatsServiceClient.Create();
    ProjectName projectName = new ProjectName(projectId);
    PagedEnumerable<ListGroupStatsResponse, ErrorGroupStats> groupStats = client.ListGroupStats(
        projectName,
        new QueryTimeRange { Period = Period._30Days });
    foreach (ErrorGroupStats item in groupStats)
    {
        // Sample output: Group: 8002882452986879952; Count: 6; Services: SampleApp/1.0.0
        IEnumerable<string> services = item.AffectedServices.Select(s => $"{s.Service}/{s.Version}");
        Console.WriteLine($"Group: {item.Group.GroupId}; Count: {item.Count}; Services: {string.Join(", ", services)}");
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
