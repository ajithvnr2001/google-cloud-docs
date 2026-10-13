---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:48.583193+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 4.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/latest/)
  * [ 4.3.1 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/4.3.1/)



# Google.Cloud.Diagnostics.AspNetCore

`Google.Cloud.Diagnostics.AspNetCore` is an ASP.NET Core instrumentation library for Google Logging, Error Reporting and Tracing. It allows for simple integration of Google observability components into ASP.NET Core 2.1+ applications with minimal custom code.

Note: ASP.NET Core 2.1 is the long-term support release of ASP.NET Core 2.x.

[`Google.Cloud.Diagnostics.Common`](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest) and [`Google.Cloud.Diagnostics.AspNetCore3`](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore3/latest) are the recommended instrumentations libraries if you are writing non ASP.NET Core .NET Standard 2.0+ or ASP.NET Core 3.1+ applications respectively.

`Google.Cloud.Diagnostics.Common` documentation is still relevant when using `Google.Cloud.Diagnostics.AspNetCore`, as tracing, logging and error reporting is done in the same manner when using either of the packages. Configuration of `Google.Cloud.Diagnostics.AspNetCore` and some aspects related to ASP.NET Core applications being web applications are covered in this document.

Note: This documentation is for version `4.4.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Diagnostics.AspNetCore` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud Platform, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to download a service account JSON file then set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to refer to it. The credentials will automatically be used to authenticate. See the [Getting Started With Authentication](https://cloud.google.com/docs/authentication/getting-started) guide for more details.

See [API Permissions for `entries.write`](https://cloud.google.com/logging/docs/access-control#api-permissions) for the permissions needed for Logging and Error Reporting.

See [API Permissions for PatchTraces](https://cloud.google.com/trace/docs/iam#api_permissions) for the permissions needed for Tracing.

> **Note**  
>  The `Google.Cloud.Diagnostics.AspNetCore` package attempts to collect the filename and line number when error entries are collected. However, to be able to collect this information PDBs must be included with the deployed code.
> 
> **Note**  
>  Some environments limit or disable CPU usage for background activities, while some others allow you to configure CPU allocation for request processing only. When running on environments with limited CPU for background activities, take care not to use the timed buffer options for any of Logging, Tracing or Error Reporting. Take into account that the timed buffer is used for the Logging and Tracing components by default so you will need to explicitly configure the buffers by using the `Google.Cloud.Diagnostics.Common.LoggerOptions` and `Google.Cloud.Diagnostics.Common.TraceOptions` classes. The Error Reporting component does not buffer entries by default. See the [`Google.Cloud.Diagnostics.Common` documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest) documentation for more information on buffers. Here you can read more about [CPU allocation in Google Cloud Run](https://cloud.google.com/run/docs/tips/general#background-activity).

## Getting started

The easiest way to configure Google Cloud Diagnostics is using the `AddGoogleDiagnosticsForAspNetCore` overloaded extension method on `IServiceCollection`. This configures the Logging, Tracing and Error Reporting components, including neccesarry middlewares.

If your application is running on Google App Engine, Google Kubernetes Engine, Google Cloud Run or Google Compute Engine, you don't need to provide a value for `ProjectId`, `Service` and `Version` since they can be automatically obtained by the `AddGoogleDiagnosticsForAspNetCore` methods as far as they make sense for the environment. (Not every environment has the concept of a "service" or "version".) The values used will be the ones associated with the running application.

If your application is running outside of GCP, including when it runs locally, then you'll need to provide the `ProjectId` of the Google Cloud Project in which to store the diagnostic information as well as the `Service` and `Version` with which to identify your application.
    
    
    public void ConfigureServices(IServiceCollection services)
    {
        // Replace ProjectId with your Google Cloud Project ID.
        // Replace Service with a name or identifier for the service.
        // Replace Version with a version for the service.
        services.AddGoogleDiagnosticsForAspNetCore(ProjectId, Service, Version);
    
        // Add any other services your application requires, for instance,
        // depending on the version of ASP.NET Core you are using, you may
        // need one of the following:
    
        // services.AddMvc();
    
        // services.AddControllersWithViews();
    }
    

You can still initialize the separate components using the extension methods described below. This can be useful if you only need to use some of the observability components.

Optional parameters on `AddGoogleDiagnosticsForAspNetCore` are also available to specify options for each of the components (logging, tracing and error reporting).

## Error Reporting

The error reporting component allows you to create error reports from exceptions thrown in your application. You can explicitly log exceptions you have caught, but the component will also log exceptions that haven't been caught/handled by your code.

## Configuration

You only need to use the `AddGoogleErrorReportingForAspNetCore` extension method on an `IServiceCollection`. You usually do this on the `ConfigureServices` method of your `Startup` class.
    
    
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddGoogleErrorReportingForAspNetCore(new Common.ErrorReportingServiceOptions
        {
            // Replace ProjectId with your Google Cloud Project ID.
            ProjectId = ProjectId,
            // Replace Service with a name or identifier for the service.
            ServiceName = Service,
            // Replace Version with a version for the service.
            Version = Version
        });
    
        // Add any other services your application requires, for instance,
        // depending on the version of ASP.NET Core you are using, you may
        // need one of the following:
    
        // services.AddMvc();
    
        // services.AddControllersWithViews();
    }
    

Error reports will be automatically created from uncaught exceptions and sent to Google Cloud Error Reporting.

## Log Exceptions

You can also log exceptions explicitly.
    
    
    /// <summary>
    /// This method catches an exception thrown by another method and explicitly
    /// logs that exception.
    /// The <see cref="IExceptionLogger"/> is populated by dependency injection 
    /// thanks to the use of the <see cref="FromServicesAttribute"/> attribute.
    /// </summary>
    public void CatchesAndLogsException(string id, [FromServices]IExceptionLogger exceptionLogger)
    {
        try
        {
            // This method call throws an exception.
            ThrowsException(id);
        }
        catch (Exception e)
        {
            exceptionLogger.Log(e);
        }
    }
    

## Logging

Configuring and using Google Cloud Logging in ASP.NET Core applications is very similar to doing so in a non ASP.NET Core application. See the [`Google.Cloud.Diagnostics.Common`](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest) documentation for more information.

## Configuration

Configuration of Google Cloud Logging in ASP.NET Core applications is almost the same as for non ASP.NET Core applications. You just build the Host as recommended for ASP.NET Core applications instead of using the general purpose host builder.
    
    
    return new WebHostBuilder()
        .ConfigureLogging(
            // Replace projectId with your Google Cloud Project ID.
            builder => builder.AddGoogle(new LoggingServiceOptions { ProjectId = projectId }))
        .UseStartup<Startup>();
    

As an alternative, you can configure logging when you are configuring services for your application. This approach is useful if you are configuring services in a `Startup` class or similar. This alternative is used in the same way for ASP.NET Core and non ASP.NET Core applications alike.

## Log

When logging, the main difference between ASP.NET Core and non ASP.NET Core applications is how you obtain a logger in container activated classes, like controllers, pages, etc. Your code does not have to explicitly resolve the dependency, instead the logger will get injected on construction.
    
    
    public class LoggingSamplesController : Controller
    {
        private ILogger _logger;
    
        public LoggingSamplesController(ILogger<LoggingSamplesController> logger) =>
            _logger = logger;
    
        /// <summary>
        /// This method logs an Information level message.
        /// </summary>
        public void LogInformation(string id)
        {
            // Log whatever message you want to log.
            _logger.LogInformation($"Id received: {id}");
        }
    }
    

## Tracing

The tracing component allows you to trace your application and send traces to Google Cloud Trace.

## Configuration

You only need to use the `AddGoogleTraceForAspNetCore` extension method on an `IServiceCollection`. You usually do this on the `ConfigureServices` method of your `Startup` class.
    
    
    public void ConfigureServices(IServiceCollection services)
    {
        // Replace ProjectId with your Google Cloud Project ID.
        services.AddGoogleTraceForAspNetCore(new AspNetCoreTraceOptions
        {
            ServiceOptions = new Common.TraceServiceOptions
            {
                ProjectId = ProjectId
            }
        });
    
        // Add any other services your application requires, for instance,
        // depending on the version of ASP.NET Core you are using, you may
        // need one of the following:
    
        // services.AddMvc();
    
        // services.AddControllersWithViews();
    }
    

## Tracing in Controllers

To use the `IManagedTracer` in controllers you can either inject the singleton instance of `IManagedTracer` into the controller's constructor (see `TraceSamplesConstructorController`) or you can inject the `IManagedTracer` into the action method using the `[FromServices]` attribute (see `TraceSamplesMethodController`).
    
    
    public class TraceSamplesConstructorController : Controller
    {
        private readonly IManagedTracer _tracer;
    
        /// <summary>
        /// The <see cref="IManagedTracer"/> is populated by dependency injection.
        /// </summary>
        public TraceSamplesConstructorController(IManagedTracer tracer)
        {
            _tracer = tracer;
        }
    
        public void TraceHelloWorld(string id)
        {
            // Change the name of the span to what makese sense in your context.
            using (_tracer.StartSpan(id))
            {
                // The code whose execution is to be included in the span goes here.
                ViewData["Message"] = "Hello World.";
            }
        }
    }
    
    
    
    public class TraceSamplesMethodController : Controller
    {
        /// <summary>
        /// Manually trace a set of operations.
        /// The <see cref="IManagedTracer"/> is populated by dependency injection
        /// thanks to the use of the <see cref="FromServicesAttribute"/> attribute.
        /// </summary>
        public void TraceHelloWorld(string id, [FromServices] IManagedTracer tracer)
        {
            // Change the name of the span to what makese sense in your context.
            using (tracer.StartSpan(id))
            {
                // The code whose execution is to be included in the span goes here.
                ViewData["Message"] = "Hello World.";
            }
        }
    }
    

## Using Tracing with other than Google's own trace header

The `Google.Cloud.Diagnostics` packages have been coupled to [Google's own trace header](https://cloud.google.com/trace/docs/setup#force-trace) from their initial release up to, and including, version 4.2.0. Starting on version 4.3.0-beta01 and upwards it is possible to consume and emit trace context information in a format other than Google's own trace header.

The default behaviour of the libraries is still to consume and emit trace context information using Google's trace header.

### Custom trace context for incoming HTTP requests

If the HTTP requests that your application handles contain trace context information in a custom format you need to use dependency injection to register:

  * A `Google.Cloud.Diagnostics.Common.ITraceContext`, which will probably be scoped, and that you can create from information obtained from any other services available via dependency injection, including `Microsoft.AspNetCore.Http.IHttpContextAccessor`. The trace context will be obtained per request and used as the parent context for all trace spans, either implicit or explicit, initiated from within the code handling the request.
  * A `System.Action<Micorosft.AspNetCore.Http.HttpResponse, Google.Cloud.Diagnostics.Common.ITraceContext>` that will be used to set trace context information on the HTTP response to each request. This will be called before returning a response with the updated (as modified by the request handling code) trace context information.



### Custom trace context for outgoing HTTP requests

See also [`Google.Cloud.Diagnostics.Common`](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest) documentation for Outgoing HTTP Requests.

If your application itself performs HTTP requests to other services and you want to propagate trace context information in a format other than Google's trace header, you can use dependency injection to register a `System.Action<System.Net.Http.HttpRequestMessage, Google.Cloud.Diagnostics.Common.ITraceContext>` that will be used to set trace context information on outgoing HTTP requests. A few things to notice:

  * The format in which you propagate trace context information to external requests doesn't have to be the same as the format in which trace context information is received by your application. You might even be accepting Google's trace header, but the service you are calling is not.
  * The trace context information propagated to outgoing requests will be the information available at the time the request is made, which may or may not be the same as the information you received. For instance, your code may have created several trace spans before making the outgoing request, in which case the span ID that will be propagated is the one of the innermost span that remains open at the moment of sending the outgoing request.



### Custom trace context: example

The following is for demonstration purposes only. We assume that trace context information contains a trace ID only that is propagated in a `custom_trace_id` header. This is of no use in the real world.
    
    
    public void ConfigureServices(IServiceCollection services)
    {
    
        // Register a trace context provider method that inspects the request and
        // extracts the trace context information.
        services.AddScoped(CustomTraceContextProvider);
        static ITraceContext CustomTraceContextProvider(IServiceProvider sp)
        {
            var accessor = sp.GetRequiredService<IHttpContextAccessor>();
            string traceId = accessor.HttpContext?.Request?.Headers["custom_trace_id"];
            return new SimpleTraceContext(traceId, null, null);
        }
    
        // Register a method that sets the updated trace context information on the response.
        services.AddSingleton<Action<HttpResponse, ITraceContext>>(
            (response, traceContext) => response.Headers.Add("custom_trace_id", traceContext.TraceId));
    
        // Now you can register Google Trace normally.
    
        // Replace ProjectId with your Google Cloud Project ID.
        services.AddGoogleTraceForAspNetCore(new AspNetCoreTraceOptions
        {
            ServiceOptions = new Common.TraceServiceOptions
            {
                ProjectId = ProjectId
            }
        });
    
        // If your application is making outgoing HTTP requests then you configure
        // your HTTP client for trace propagation as you normally would.
        // If the trace context information should be propagated in a custom format
        // then you register a method that sets the trace context information on the
        // outgoing request.
        services.AddSingleton<Action<HttpRequestMessage, ITraceContext>>(
            (request, traceContext) => request.Headers.Add("custom_trace_id", traceContext.TraceId));
    
        // Register an HttpClient for outgoing requests.
        services.AddHttpClient("tracesOutgoing")
            // The next call guarantees that trace information is propagated for outgoing
            // requests that are already being traced.
            .AddOutgoingGoogleTraceHandler();
    
        // Add any other services your application requires, for instance,
        // depending on the version of ASP.NET Core you are using, you may
        // need one of the following:
    
        // services.AddMvc();
    
        // services.AddControllersWithViews();
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
