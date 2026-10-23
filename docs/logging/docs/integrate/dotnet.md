---
url: https://docs.cloud.google.com/logging/docs/integrate/dotnet/
title: Using .NET logging frameworks or calling the API \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:50.533897+00:00
---

# Using .NET logging frameworks or calling the API  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/integrate/dotnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Using .NET logging frameworks or calling the API Stay organized with collections  Save and categorize content based on your preferences. 

There are several ways to use Cloud Logging from your .NET application:

  * Use a Google logging provider for .NET's standard logging framework
  * Use a Google Log4Net provider
  * Use `Google.Cloud.Logging.V2` to directly call the Logging API



## Use a Google logging provider for .NET's standard logging framework

You can enable Cloud Logging for .NET applications by using the `Google.Cloud.Diagnostics` libraries for .NET.

  * For applications that target ASP.NET Core 3 or later, use the `Google.Cloud.Diagnostics.AspNetCore3` library. See the [ `Google.Cloud.Diagnostics.AspNetCore3` documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore3/latest#configuration-1) for more information and examples.
  * For applications that target earlier versions of ASP.NET Core, use the `Google.Cloud.Diagnostics.AspNetCore` library. See the [ `Google.Cloud.Diagnostics.AspNetCore` documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/latest#configuration-1) for more information and examples.
  * For applications that target non ASP.NET Core platforms, use the `Google.Cloud.Diagnostics.Common` library. See the [ `Google.Cloud.Diagnostics.Common` documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest#configuration-1) for more information and examples.



## Use a Google Log4Net provider

The `Google.Cloud.Logging.Log4Net` library implements a Log4Net provider for Cloud Logging. For examples that show how to configure and use this library, see the [ `Google.Cloud.Logging.Log4Net` documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Log4Net/latest).

## Use `Google.Cloud.Logging.V2` to directly call the Logging API

You can also write logs by calling the Cloud Logging API using the `Google.Cloud.Logging.V2` client library. You can install this library from [NuGet](https://www.nuget.org/packages/Google.Cloud.Logging.V2/).

After the `Google.Cloud.Logging.V2` client library is installed, you can start sending your application's logs to Cloud Logging. For example, you might customize the following method and add it to your application code. To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    private void WriteLogEntry(string logId)
    {
        var client = LoggingServiceV2Client.Create();
        LogName logName = new LogName(s_projectId, logId);
        var jsonPayload = new Struct()
        {
            Fields =
            {
                { "name", Value.ForString("King Arthur") },
                { "quest", Value.ForString("Find the Holy Grail") },
                { "favorite_color", Value.ForString("Blue") }
            }
        };
        LogEntry logEntry = new LogEntry
        {
            LogNameAsLogName = logName,
            Severity = LogSeverity.Info,
            JsonPayload = jsonPayload
        };
        MonitoredResource resource = new MonitoredResource { Type = "global" };
        IDictionary<string, string> entryLabels = new Dictionary<string, string>
        {
            { "size", "large" },
            { "color", "blue" }
        };
        client.WriteLogEntries(logName, resource, entryLabels,
            new[] { logEntry }, _retryAWhile);
        Console.WriteLine($"Created log entry in log-id: {logId}.");
    }
    

Write some logging code that calls `WriteLogEntry()`. The resulting log entry will be in the Logs Explorer under the **Global** resource.

In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

## Resources

  * For details on the Logs Explorer, see [Using the Logs Explorer][view-ui].
  * For ASP.NET Core 3+ applications 
    * [Documentation: `Google.Cloud.Diagnostics.AspNetCore3`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore3/latest#configuration-1)
    * [NuGet: `Google.Cloud.Diagnostics.AspNetCore3` package](https://www.nuget.org/packages/Google.Cloud.Diagnostics.AspNetCore3/)
  * For earlier ASP.NET Core applications 
    * [Documentation: `Google.Cloud.Diagnostics.AspNetCore`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/latest#configuration-1)
    * [NuGet: `Google.Cloud.Diagnostics.AspNetCore` package](https://www.nuget.org/packages/Google.Cloud.Diagnostics.AspNetCore/)
  * For non ASP.NET Core applications 
    * [Documentation: `Google.Cloud.Diagnostics.Common`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest#configuration-1)
    * [NuGet: `Google.Cloud.Diagnostics.Common` package](https://www.nuget.org/packages/Google.Cloud.Diagnostics.Common/)
  * Log4Net Provider 
    * [Documentation: `Google.Cloud.Logging.Log4Net`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Log4Net/latest)
    * [NuGet: `Google.Cloud.Logging.Log4Net` package](https://www.nuget.org/packages/Google.Cloud.Logging.Log4Net/)
  * [GitHub: googleapis/google-cloud-dotnet](https://github.com/googleapis/google-cloud-dotnet)
  * [GitHub issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
