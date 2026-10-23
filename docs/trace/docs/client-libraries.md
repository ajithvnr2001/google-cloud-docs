---
url: https://docs.cloud.google.com/trace/docs/client-libraries/
title: Client libraries \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:33.879393+00:00
---

# Client libraries  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Reference ](https://docs.cloud.google.com/trace/docs/reference)



Send feedback 

#  Client libraries Stay organized with collections  Save and categorize content based on your preferences. 

To collect trace data from your applications and send it to Cloud Trace, you can instrument your code with [OpenTelemetry](https://opentelemetry.io) or language-specific Cloud Client Libraries. You can use the setup guides and library resources in this document to instrument C++, Go, Java, Node.js, Python, Ruby, and .NET applications.

## When to instrument your application

**Note:** Trace data is automatically captured for some configurations and for some Google Cloud services, so you might not need to instrument your application. For more information, see [Configurations with automatic tracing](https://docs.cloud.google.com/trace/docs/overview#configurations_with_automatic_tracing). 

Instrument your application to collect specific information that helps you understand its performance and troubleshoot failures. Several open-source instrumentation frameworks collect log, metric, and trace data, and can send that data to any vendor, including Google Cloud. For your agentic applications, some frameworks can collect your prompts and responses or pass context that allows tracing of some remote [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) calls.

To instrument your application, we recommend that you use an open-source, vendor-neutral instrumentation framework, such as [OpenTelemetry](https://opentelemetry.io/), instead of vendor- and product-specific APIs or client libraries. For information about these frameworks, see [ Observability for application developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/application-developers) and [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

## OpenTelemetry setup

For information about setting up OpenTelemetry, see the following guides:

  * [C++](https://docs.cloud.google.com/trace/docs/setup/cpp-ot)
  * [Go](https://docs.cloud.google.com/trace/docs/setup/go-ot)
  * [Java](https://docs.cloud.google.com/trace/docs/setup/java-ot)
  * [Node.js](https://docs.cloud.google.com/trace/docs/setup/nodejs-ot)
  * [Python](https://docs.cloud.google.com/trace/docs/setup/python-ot)



## Cloud Client Libraries

For information about the Cloud Client Libraries, see the following resources:

  * Ruby:

**Note:** We recommend that you use OpenTelemetry for Ruby. For more information, see the [Ruby SDK](https://opentelemetry.io/docs/instrumentation/ruby/).

GitHub: [`googleapis/google-cloud-trace`](https://github.com/googleapis/google-cloud-ruby/tree/master/google-cloud-trace)

  * ASP.NET:

    * Library: [`Google.Cloud.Diagnostics.AspNet`](https://googleapis.dev/dotnet/Google.Cloud.Diagnostics.AspNet/latest/index.html)
    * NuGet package: [`Google.Cloud.Diagnostics.AspNet`](https://www.nuget.org/packages/Google.Cloud.Diagnostics.AspNet/)
    * GitHub: [`Google.Cloud.Diagnostics.AspNet version 4.0.0`](https://github.com/googleapis/google-cloud-dotnet/releases/tag/Google.Cloud.Diagnostics.AspNet-4.0.0)
  * ASP.NET Core:

    * Libraries: [`Google.Cloud.Diagnostics.AspNetCore3`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore3/latest) and [`Google.Cloud.Diagnostics.AspNetCore`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/latest)
    * NuGet packages: [`Google.Cloud.Diagnostics.AspNetCore3`](https://www.nuget.org/packages/Google.Cloud.Diagnostics.AspNetCore3/) and [`Google.Cloud.Diagnostics.AspNetCore`](https://www.nuget.org/packages/Google.Cloud.Diagnostics.AspNetCore/)
    * GitHub: [`googleapis/google-cloud-dotnet`](https://github.com/googleapis/google-cloud-dotnet)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
