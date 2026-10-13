---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:33.027754+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/latest/)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.5.0/)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.4.0/)
  * [ 1.3.1 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.3.1/)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.2.0/)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.1.0/)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Console/1.0.0/)



# Google.Cloud.Logging.Console

`Google.Cloud.Logging.Console` is a package providing a [custom console formatter](https://docs.microsoft.com/en-us/dotnet/core/extensions/console-log-formatter) designed to be used with [Cloud Logging](https://cloud.google.com/logging/docs).

## Installation

Install the `Google.Cloud.Logging.Console` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Registering the formatter

After installing the NuGet package, the formatter can be installed using the `AddGoogleCloudConsole` extension method:
    
    
    using Google.Cloud.Logging.Console;
    ...
    var builder = WebApplication.CreateBuilder(args);
    builder.Logging.AddGoogleCloudConsole();
    

Additional options can be provided either in appsettings.json or in the extension method call. For example, to enable scopes to be logged, you could change the above code to:
    
    
    using Google.Cloud.Logging.Console;
    ...
    var builder = WebApplication.CreateBuilder(args);
    builder.Logging.AddGoogleCloudConsole(options => options.IncludeScopes = true);
    

## Log trace correlation

The console formatter supports [log correlation](https://cloud.google.com/logging/docs/view/correlate-logs) and [Google Cloud Trace log integration](https://cloud.google.com/trace/docs/trace-log-integration) via trace IDs. This requires a number of conditions to be met:

  * Your application needs to be exporting log entries to Google Cloud Logging via an agent that reads from stdout. This happens automatically when running on Google Cloud, and is presumably the reason you're using this console formatter.
  * Your application needs to be exporting traces to Google Cloud Trace. This could be performed automatically by the runtime, or via explicit code or instrumentation. Google Cloud runtimes export some traces automatically. (For example, Cloud Run will [export traces for received requests](https://cloud.google.com/run/docs/trace) by default, but you would need to export traces for any additional information.) Please refer to the documentation for the runtime you're using for more details.
  * When writing a server application, the current .NET [Activity](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.activity) needs to be initialized with the trace context included in the current request. ASP.NET Core does this for you automatically based on HTTP headers. Alternatively, if your application is starting traces itself (for example, if it's responding to Pub/Sub messages instead of HTTP requests), it needs to initialize the current Activity explicitly, as described in the [Distributed Tracing guide](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/distributed-tracing).
  * The console formatter needs to be configured with the Google Cloud Project ID where the traces are beeing exported to. When running in Google Cloud, that's usually the same project in which the code is running.



Configuring the formatter involves specifying the `TraceGoogleCloudProjectId` properties in the `GoogleCloudConsoleFormatterOptions` used to create the formatter, as shown below:
    
    
    using Google.Cloud.Logging.Console;
    ...
    var builder = WebApplication.CreateBuilder(args);
    builder.Logging.AddGoogleCloudConsole(options => options.TraceGoogleCloudProjectId = "google-project-id");
    

## Formatter output

The formatter writes JSON entries in the format expected by Cloud Logging. In particular, it uses the following JSON property names:

  * `message`: the formatted log message
  * `severity`: the log entry severity
  * `category`: the logger category
  * `exception`: the exception stack trace, if any
  * `format_parameters`: the format parameters for the message, if any
  * `scopes`: the scope information for the log entry, if the `IncludeScopes` option is enabled and there is scope information available



No timestamp is included in the JSON, as this is automatically picked up by the logging agent.

Most log entry severity mappings are obvious, but the ASP.NET Core `LogLevel.Trace` level maps to `DEBUG` in Cloud Logging.

When viewing the log entries in the Logs Explorer, the severity is shown in the root of the entry. Other aspects are within the `jsonPayload` property.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
