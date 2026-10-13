---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:33.904313+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 4.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/)
  * [ 4.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.4.0/)
  * [ 4.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.3.0/)
  * [ 4.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.2.0/)
  * [ 4.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.1.0/)
  * [ 4.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.0.0/)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.6.0/)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.5.0/)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.4.0/)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.3.0/)



# Google.Cloud.Logging.V2

`Google.Cloud.Logging.V2` is a.NET client library for the [Google Cloud Logging API](https://cloud.google.com/logging/).

Note: This documentation is for version `4.5.0` of the library. Some samples may not work with other versions.

  * Integration with [log4net](https://logging.apache.org/log4net/) is provided by the [Google.Cloud.Logging.Log4Net](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Log4Net/latest) package.
  * Integration with [NLog](https://nlog-project.org/) is provided by the [Google.Cloud.Logging.NLog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.NLog/latest) package.



## Installation

Install the `Google.Cloud.Logging.V2` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

If you wish to use the log4net integration, install the `Google.Cloud.Logging.Log4Net` package in the same way.

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Support from third party libraries

  * [Logary](https://github.com/logary/logary) supports Google Stackdriver logging. Install the [NuGet package](https://www.nuget.org/packages/Logary.Targets.Stackdriver) and see [instructions on the project homepage](https://github.com/logary/logary#stackdriver-target).
  * [Serilog](https://serilog.net/) supports Google Stackdriver Logging. Install the [NuGet package](https://www.nuget.org/packages/Serilog.Sinks.GoogleCloudLogging/) `Serilog.Sinks.GoogleCloudLogging` and [configure options](https://github.com/manigandham/serilog-sinks-googlecloudlogging).



## Raw RPC API

If required, this package provides a low-level abstraciton over the raw RPC API.

All operations are performed through the following client classes:

  * [ConfigServiceV2Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.ConfigServiceV2Client)
  * [LoggingServiceV2Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LoggingServiceV2Client)
  * [MetricsServiceV2Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.MetricsServiceV2Client)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. ConfigServiceV2ClientBuilder for ConfigServiceV2Client) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
