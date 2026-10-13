---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest/
title: .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:48.665039+00:00
---

# .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 5.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/latest/)
  * [ 5.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/5.2.0/)
  * [ 5.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/5.1.0/)
  * [ 5.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/5.0.0/)
  * [ 4.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/4.4.0/)
  * [ 4.3.1 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.Common/4.3.1/)



# Google.Cloud.Diagnostics.Common

`Google.Cloud.Diagnostics.Common` is a .NET Core instrumentation library for Google Logging, Error Reporting and Tracing. It allows for simple integration of Google observability components into .NET Standard 2.0+ applications with minimal custom code.

[`Google.Cloud.Diagnostics.AspNetCore`](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore/latest) and [`Google.Cloud.Diagnostics.AspNetCore3`](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Diagnostics.AspNetCore3/latest) are the recommended instrumentation libraries if you are writing ASP.NET Core 2.1 or ASP.NET Core 3.1+ applications respectively.

Note: This documentation is for version `5.3.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Diagnostics.Common` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

See [API Permissions for `entries.write`](https://cloud.google.com/logging/docs/access-control#api-permissions) for the permissions needed for Logging and Error Reporting.

See [API Permissions for PatchTraces](https://cloud.google.com/trace/docs/iam#api_permissions) for the permissions needed for Tracing.

> **Note**  
>  The `Google.Cloud.Diagnostics.Common` package attempts to collect the filename and line number when error entries are collected. However, to be able to collect this information PDBs must be included with the deployed code.
> 
> **Note**  
>  Some environments limit or disable CPU usage for background activities, while some others allow you to configure CPU allocation for request processing only. When running on environments with limited CPU for background activities, take care not to use the timed buffer options for any of Logging, Tracing or Error Reporting. Take into account that the timed buffer is used for the Logging and Tracing components by default so you will need to explicitly configure the buffers by using the `Google.Cloud.Diagnostics.Common.LoggerOptions` and `Google.Cloud.Diagnostics.Common.TraceOptions` classes. The Error Reporting component does not buffer entries by default. Below you'll find examples of how to configure the buffers. Here you can read more about [CPU allocation in Google Cloud Run](https://cloud.google.com/run/docs/tips/general#background-activity).
> 
> **Note** Using `Google.Cloud.Diagnostics.Common` for non ASP.NET Core applications relies heavily on .NET's Dependency Injection mechanism. You can read more about .NET dependency injection in non ASP.NET Core applications in the [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-usage).

## Getting started

The easiest way to configure Google Cloud Diagnostics is using the `AddGoogleDiagnostics` extension methods on `IServiceCollection`. This configures the Logging, Tracing and Error Reporting components.

If your application is running on Google App Engine, Google Kubernetes Engine, Google Cloud Run or Google Compute Engine, you don't need to provide a value for `ProjectId`, `Service` and `Version` since they can be automatically obtained by the `AddGoogleDiagnostics` methods as far as they make sense for the environment. (Not every environment has the concept of a "service" or "version".) The values used will be the ones associated with the running application.

If your application is running outside of GCP, including when it runs locally, then you'll need to provide the `ProjectId` of the Google Cloud Project in which to store the diagnostic information as well as the `Service` and `Version` with which to identify your application.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                // Replace Service with a name or identifier for the service.
                // Replace Version with a version for the service.
                services.AddGoogleDiagnostics(ProjectId, Service, Version);
                // Register other services here if you need them.
            });
    

Don't forget to start the host.
    
    
    host = CreateHostBuilder().Build();
    await host.StartAsync();
    

You can still initialize the separate components using the extension methods described below. This can be useful if you only need to use some of the observability components.

Optional parameters on `AddGoogleDiagnostics` are also available to specify options for each of the components (logging, tracing and error reporting).

### Buffers and buffer configuration

The Diagnostics instrumentation library supports different buffering strategies that may be configured individually for each of the Logging, Tracing and Error Reporting components, i.e. you don't need to use the same buffering strategy for each of the components and even if you do, each buffer may be configured differently for each of the components. For instance, a timed buffer may be configured for Logging with a 5 second period at the same time as a timed buffer with a 7 second period is configured for Tracing.

These strategies are:

  * Timed buffers: Written entries are stored in a buffer that is flushed periodically to the backend service. This is the buffering strategy used by default by the Tracing and Logging components. Since the service calls are performed in the background, this buffering strategy won't affect your application's performance, in particular it won't affect external requests or user interactions. Depending on the amount of entries your application is generating, you may want to fine tune the timed buffer period, which defaults to 5 seconds, to flush more or less frequently by taking into account application memory comsumption and how soon you need entries to appear on the backend. As stated earlier in this documentation, it is important to note that some environments do limit CPU usage for background operations, and in such cases, using timed buffers may result in delayed backend entry recording, lost entries or even thread starvation scenarios.
  * Sized buffers: Written entries are stored in a buffer that is flushed to the backend service when it reaches a given size. Service calls are not performed in the background, so the sized buffer may affect performance of certain external requests or user interactions, in particular those who make the buffer reach the flushing size. In general you'll need to fine tune the buffer size so that flushing occurs as little as possible while keeping memory comsumption at appropriate levels. Adjustments will depend on the amount of entries your application is generating.
  * No buffer: Entries are sent to the backend service as soon as they are generated by your application. This is the buffering strategy used by default by the Error Reporting component. A service call will be made whenever an entry is generated by your application which may affect performance greatly, depending on the amount of entries your code is generating.



Below you can see sample code that forces all three components to use no buffering.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                // Replace Service with a name or identifier for the service.
                // Replace Version with a version for the service.
                services.AddGoogleDiagnostics(ProjectId, Service, Version,
                    // Configure the three components to use no buffer.
                    traceOptions: TraceOptions.Create(bufferOptions: BufferOptions.NoBuffer()),
                    loggingOptions: LoggingOptions.Create(bufferOptions: BufferOptions.NoBuffer()),
                    errorReportingOptions: ErrorReportingOptions.Create(bufferOptions: BufferOptions.NoBuffer()));
                // Register other services here if you need them.
            });
    

#### Exceptions thrown in timed buffers' timer thread

Rethrowing exceptions thrown in timed buffers' timer thread may immediately crash the application. These exceptions are not propagated by default, even if the library has been configured to propagate all other exceptions. If you need to handle these exceptions, for diagnostic or other purposes, you can provide your own exception handler when configuring a timed buffer.

Below you can see sample code that configures all three components to use timed buffers that will write timer thread exceptions to the console.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                // Replace Service with a name or identifier for the service.
                // Replace Version with a version for the service.
                services.AddGoogleDiagnostics(ProjectId, Service, Version,
                    // Configure the three components so that exceptions thrown in the timer thread
                    // of timed buffers are handled by the given handler.
                    traceOptions: TraceOptions.Create(bufferOptions: BufferOptions.TimedBuffer().WithTimerExceptionHandler(ex => Console.WriteLine(ex))),
                    loggingOptions: LoggingOptions.Create(bufferOptions: BufferOptions.TimedBuffer().WithTimerExceptionHandler(ex => Console.WriteLine(ex))),
                    errorReportingOptions: ErrorReportingOptions.Create(bufferOptions: BufferOptions.TimedBuffer().WithTimerExceptionHandler(ex => Console.WriteLine(ex))));
                // Register other services here if you need them.
            });
    

## Error reporting

The error reporting component allows you to create error reports from exceptions thrown in your application.

## Configuration

The first step is to configure the error reporting component for dependency injection.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                services.AddGoogleErrorReporting(new ErrorReportingServiceOptions
                {
                    // Replace ProjectId with your Google Cloud Project ID.
                    ProjectId = ProjectId,
                    // Replace Service with a name or identifier for the service.
                    ServiceName = Service,
                    // Replace Version with a version for the service.
                    Version = Version
                });
                // Register other services here if you need them.
            });
    

And then start the host. This will probably be done in your `Main` method.
    
    
    host = CreateHostBuilder().Build();
    await host.StartAsync();
    

## Logging exceptions

Now you can log exceptions whenever they are thrown. Meaningful error reports will be created and sent to Google Cloud Error Reporting.
    
    
    IContextExceptionLogger exceptionLogger = host.Services.GetRequiredService<IContextExceptionLogger>();
    try
    {
        // This method call throws an exception.
        ThrowsException();
    }
    catch (Exception e)
    {
        // The logger may receive an IContextWrapper as a second parameter
        // with information about the HTTP operation, if any, that produced
        // the error. It may be null in which case it will be ignored.
        exceptionLogger.Log(e, null);
    }
    

## Logging

The logging component allows you to store the logs generated by your application in Google Cloud Logger. The `GoogleLogger` implements `Microsoft.Extensions.Logging.ILogger` and so it integrates seamlessly with .NET's logging infrastructure.

## Configuration

For configuring the logging component you use the `AddGoogle` extension method on a `Microsoft.Extensions.Logging.ILoggingBuilder`.

You can onfigure logging when configuring your host builder.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureLogging(builder => builder.AddGoogle(new LoggingServiceOptions
            {
                // Replace ProjectId with your Google Cloud Project ID.
                ProjectId = ProjectId,
                // Replace Service with a name or identifier for the service.
                ServiceName = Service,
                // Replace Version with a version for the service.
                Version = Version
            }));
    

As an alternative, you can configure logging when you are configuring services for your application. This approach is useful if you are configuring services in a `Startup` class or similar.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddLogging(builder => builder.AddGoogle(new LoggingServiceOptions
                {
                    // Replace ProjectId with your Google Cloud Project ID.
                    ProjectId = ProjectId,
                    // Replace Service with a name or identifier for the service.
                    ServiceName = Service,
                    // Replace Version with a version for the service.
                    Version = Version
                }));
                // Register other services here if you need them.
            });
    

And then start the host. This will probably be done in your `Main`.
    
    
    host = CreateHostBuilder().Build();
    await host.StartAsync();
    

## Log

For logging, youuse the configured Google Cloud Logger as you would any other `Microsoft.Extensions.Logging.ILogger`.
    
    
    ILogger logger = host.Services.GetRequiredService<ILogger<Program>>();
    logger.LogInformation($"User {userName} logged in.");
    

## Troubleshooting Logging

Sometimes it is necessary to diagnose log operations. It might be that logging is failing or that you simply cannot find where the logs are being stored in Google Cloud Logging. What follows are a couple of code samples that can be useful to find out what might be wrong with logging operations.

### Propagating Exceptions

By default the Google Logger won't propagate any exceptions thrown during logging. This is to protect the application from crashing if logging is not possible. But logging is an important aspect of most applications so at times we need to know if it's failing and why. The following example shows how to configure Google Logger so that it propagates exceptions thrown during logging.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                //Explicitly create logger options that will propagate any exceptions thrown
                // during logging.
                RetryOptions retryOptions = RetryOptions.NoRetry(ExceptionHandling.Propagate);
                // Also set the no buffer option so that writing the logs is attempted immediately.
                BufferOptions bufferOptions = BufferOptions.NoBuffer();
    
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddLogging(builder => builder.AddGoogle(new LoggingServiceOptions
                {
                    // Replace ProjectId with your Google Cloud Project ID.
                    ProjectId = ProjectId,
                    // Replace Service with a name or identifier for the service.
                    ServiceName = Service,
                    // Replace Version with a version for the service.
                    Version = Version,
                    Options = LoggingOptions.Create(retryOptions: retryOptions, bufferOptions: bufferOptions)
                })); ;
                // Register other services here if you need them.
            });
    

### Finding out the URL where logs are written

Depending on where your code is running and the options you provided for creating a Google Logger, it might be hard to find your logs in the Google Cloud Logging Console. We have provided a way for you to obtain the URL where your logs can be found.

As the following code sample shows, you only need to pass a `System.IO.TextWriter` (typically `Console.Out` or `Console.Error`) as part of the options when configuring logging. When the `GoogleLoggerProvider` is initialized, the URL where its logs can be found will be written to the given text writer.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddLogging(builder => builder.AddGoogle(new LoggingServiceOptions
                {
                    // Replace ProjectId with your Google Cloud Project ID.
                    ProjectId = ProjectId,
                    // Replace Service with a name or identifier for the service.
                    ServiceName = Service,
                    // Replace Version with a version for the service.
                    Version = Version,
                    // Set a TextWriter to which you want yout logs URL to be written to.
                    LoggerDiagnosticsOutput = Console.Out
                })); ;
                // Register other services here if you need them.
            });
    

Please note that since this is a Google Logger diagnostics feature, we don't respect settings for exception handling, i.e. we propagate any exception thrown while writing the URL to the given text writer so you know what might be happening. This feature should only be activated as a one off, if you are having trouble finding your logs in the GCP Console, and not as a permanent feature in production code. To deactivate this feature simply stop passing a `System.IO.TextWriter` as part of the options when configuring Google Logger.

## Tracing

The tracing component allows you to trace your application and send traces to Google Cloud Trace.

## Configuration

The first step is to configure the tracing component for dependency injection.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddGoogleTrace(new TraceServiceOptions { ProjectId = ProjectId });
                // Register other services here if you need them.
            });
    

And then start the host. This will probably be done in your `Main` method.
    
    
    host = CreateHostBuilder().Build();
    await host.StartAsync();
    

## Starting a trace

How to start a trace will depend on how you want to trace, and what type of application you want to trace.

  * You want to trace all activity of your application in one trace (within potentially different spans). This is best suited for scheduled services or user facing applications (like desktop applications) where you want to have one trace per usage session.
  * Your application is a service reacting to requests/events (for instance it's a subscriber on a publisher/subscriber architectured system). You want a trace per request/event; the trace may have even be initialized by the emitter of said request/event.



### One trace per usage session

If you want to have one trace per usage session, then right after starting the host, probably on your `Main` method you would create the trace.
    
    
    ITraceContext traceContext = new SimpleTraceContext(null, null, true);
    var tracerFactory = host.Services.GetRequiredService<Func<ITraceContext, IManagedTracer>>();
    IManagedTracer tracer = tracerFactory(traceContext);
    ContextTracerManager.SetCurrentTracer(tracer);
    

Note that when you create the tracing context, you don't need to specify trace ID or span ID (although you may), `Google.Cloud.Diagnostics.Common` will create a trace ID for you. Each span you create will be created with it's own span ID.

Note that you should specify `true` for the `shouldTrace`parameter to make sure tha tracing happens regardless of tracing rates/qps, etc.

### One trace per request/event

If your application reacts to requests/events, then on the method that receives each of those (your listener method) you need to extract the trace context information from the request and ser it on the tracer.
    
    
    ITraceContext traceContext = GetTraceContextFromIncomingRequest(request);
    var tracerFactory = host.Services.GetRequiredService<Func<ITraceContext, IManagedTracer>>();
    IManagedTracer tracer = tracerFactory(traceContext);
    ContextTracerManager.SetCurrentTracer(tracer);
    

Note that we can't go into detail here as to how extract trace context information from a request/event, as that's dependent on the emitter of said request/event.

If the emitter of requests/events is not attaching trace context information, then you can start your own trace for each request/event. On your listener method, you would have code similar to the one in the [One trace per usage sesion](### One trace per usage session). But consider in this case not forcing the trace, instead specify `null` for the `shouldTrace` parameter. The tracer will decide whether to trace each request based on tracing rates/qps, etc.

## Starting a span

For any traces to be sent to Google Cloud Trace, a span needs to be started.
    
    
    IManagedTracer currentTracer = host.Services.GetRequiredService<IManagedTracer>();
    using (currentTracer.StartSpan("testing_tracing"))
    {
        Console.WriteLine("Using Cloud Trace from a non ASP.NET Core app");
    }
    

Or alternatively, using the `RunInSpan` methods.
    
    
    ----- Snippet Configure -----
    // <Configure>
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddGoogleTrace(new TraceServiceOptions { ProjectId = ProjectId });
                // Register other services here if you need them.
            });
    // </Configure>
    
    ----- Snippet Troubleshooting -----
    // <Troubleshooting>
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Explicitly create trace options that will propagate any exceptions thrown during tracing.
                RetryOptions retryOptions = RetryOptions.NoRetry(ExceptionHandling.Propagate);
                // Also set the no buffer option so that tracing is attempted immediately.
                BufferOptions bufferOptions = BufferOptions.NoBuffer();
                TraceOptions traceOptions = TraceOptions.Create(bufferOptions: bufferOptions, retryOptions: retryOptions);
    
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddGoogleTrace(new TraceServiceOptions { ProjectId = ProjectId, Options = traceOptions });
                // Register other services here if you need them.
            });
    // </Troubleshooting>
    
    ----- Snippet ConfigureHttpClient -----
    // <ConfigureHttpClient>
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddGoogleTrace(new TraceServiceOptions { ProjectId = ProjectId });
    
                // Register an HttpClient for outgoing requests.
                services.AddHttpClient("tracesOutgoing")
                    // The next call guarantees that trace information is propagated for outgoing
                    // requests that are already being traced.
                    .AddOutgoingGoogleTraceHandler();
    
                // Register other services here if you need them.
            });
    // </ConfigureHttpClient>
    
    ----- Snippet CustomConfigureHttpClient -----
    // <CustomConfigureHttpClient>
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddGoogleTrace(new TraceServiceOptions { ProjectId = ProjectId });
    
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
    
                // Register other services here if you need them.
            });
    // </CustomConfigureHttpClient>
    
    ----- Snippet Start -----
    // <Start>
    host = CreateHostBuilder().Build();
    await host.StartAsync();
    // </Start>
    
    ----- Snippet IncomingContext -----
    // <IncomingContext>
    ITraceContext traceContext = GetTraceContextFromIncomingRequest(request);
    var tracerFactory = host.Services.GetRequiredService<Func<ITraceContext, IManagedTracer>>();
    IManagedTracer tracer = tracerFactory(traceContext);
    ContextTracerManager.SetCurrentTracer(tracer);
    // </IncomingContext>
    
    ----- Snippet Trace -----
    // <Trace>
    IManagedTracer currentTracer = host.Services.GetRequiredService<IManagedTracer>();
    using (currentTracer.StartSpan("testing_tracing"))
    {
        Console.WriteLine("Using Cloud Trace from a non ASP.NET Core app");
    }
    // </Trace>
    
    ----- Snippet SingleContext -----
    // <SingleContext>
    ITraceContext traceContext = new SimpleTraceContext(null, null, true);
    var tracerFactory = host.Services.GetRequiredService<Func<ITraceContext, IManagedTracer>>();
    IManagedTracer tracer = tracerFactory(traceContext);
    ContextTracerManager.SetCurrentTracer(tracer);
    // </SingleContext>
    
    ----- Snippet RunIn -----
    // <RunIn>
    IManagedTracer currentTracer = host.Services.GetRequiredService<IManagedTracer>();
    currentTracer.RunInSpan(
        () => Console.WriteLine("Using Cloud Trace from a non ASP.NET Core app"),
        "testing_tracing");
    // </RunIn>
    
    ----- Snippet TraceOutgoingClientFactory -----
    // <TraceOutgoingClientFactory>
    IHttpClientFactory clientFactory = host.Services.GetRequiredService<IHttpClientFactory>();
    var httpClient = clientFactory.CreateClient("tracesOutgoing");
    // Any code that makes outgoing requests.
    var response = await httpClient.GetAsync(OutgoingUrl);
    // </TraceOutgoingClientFactory>
    
    

## Troubleshooting Tracing

Failures in tracing are most easily diagnosed by removing buffering and propagating exceptions immediately.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Explicitly create trace options that will propagate any exceptions thrown during tracing.
                RetryOptions retryOptions = RetryOptions.NoRetry(ExceptionHandling.Propagate);
                // Also set the no buffer option so that tracing is attempted immediately.
                BufferOptions bufferOptions = BufferOptions.NoBuffer();
                TraceOptions traceOptions = TraceOptions.Create(bufferOptions: bufferOptions, retryOptions: retryOptions);
    
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddGoogleTrace(new TraceServiceOptions { ProjectId = ProjectId, Options = traceOptions });
                // Register other services here if you need them.
            });
    

These options may be specified wherever you are configuring tracing.

## Trace Outgoing HTTP Requests

If your application itself performs HTTP requests to other services you may want to propagate trace context information. The [recommended way of creating `HttpClient`](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/http-requests?view=aspnetcore-3.1) in .NET Standard 2.0+ and upwards is to use the `System.Net.Http.IHttpClientFactory` defined in the `Microsoft.Extensions.Http` package. The following example demonstrates how to register and use an `HttpClient` using Google Trace so that it propagates trace context information for outgoing requests.

### Configuration
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddGoogleTrace(new TraceServiceOptions { ProjectId = ProjectId });
    
                // Register an HttpClient for outgoing requests.
                services.AddHttpClient("tracesOutgoing")
                    // The next call guarantees that trace information is propagated for outgoing
                    // requests that are already being traced.
                    .AddOutgoingGoogleTraceHandler();
    
                // Register other services here if you need them.
            });
    

### Usage
    
    
    IHttpClientFactory clientFactory = host.Services.GetRequiredService<IHttpClientFactory>();
    var httpClient = clientFactory.CreateClient("tracesOutgoing");
    // Any code that makes outgoing requests.
    var response = await httpClient.GetAsync(OutgoingUrl);
    

### Custom trace context for outgoing HTTP requests

If you configure the trace component for outgoing requests, it will, by default, set on them [Google's own trace header](https://cloud.google.com/trace/docs/setup#force-trace). If you want to propagate trace context information in a format other than Google's trace header, you can use dependency injection to register an action `System.Action<System.Net.Http.HttpRequestMessage, Google.Cloud.Diagnostics.Common.ITraceContext>` that will be used to set trace context information on outgoing HTTP requests. A few things to notice:

  * The format in which you propagate trace context information to external requests doesn't have to be the same as the format in which trace context information is received by your application.

  * The trace context information propagated to outgoing requests will be the information available at the time the request is made, which may or may not be the same as the information you received. For instance, your code may have created several trace spans before making the outgoing request, in which case the span ID that will be propagated is the one of the innermost span that remains open at the moment of sending the outgoing request.




Here's an example of how your configuration may look like. You then use `System.Net.Http.IHttpClientFactory` as shown in [Usage](### Usage).

Note that the following is for demonstration purposes only. We assume that trace context information contains a trace ID only that is propagated in a `custom_trace_id` header. This is of no use in the real world.
    
    
    public static IHostBuilder CreateHostBuilder() =>
        new HostBuilder()
            .ConfigureServices(services =>
            {
                // Replace ProjectId with your Google Cloud Project ID.
                services.AddGoogleTrace(new TraceServiceOptions { ProjectId = ProjectId });
    
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
    
                // Register other services here if you need them.
            });
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
