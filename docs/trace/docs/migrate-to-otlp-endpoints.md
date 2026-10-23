---
url: https://docs.cloud.google.com/trace/docs/migrate-to-otlp-endpoints/
title: Migrate from the Trace exporter to the OTLP endpoint \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:32.372177+00:00
---

# Migrate from the Trace exporter to the OTLP endpoint  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/migrate-to-otlp-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Migrate from the Trace exporter to the OTLP endpoint Stay organized with collections  Save and categorize content based on your preferences. 

You can migrate manually instrumented Java, Go, Python, and Node.js applications from a Google Cloud trace exporter to an in-process OpenTelemetry OTLP exporter. The OTLP exporter sends trace data directly to the Telemetry (OTLP) API in your Google Cloud project by using [supported export protocols](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#specify-protocol) (`gRPC` or `http/protobuf`).

This configuration exports only trace data and applies only to in-process exporters. If your application uses an OpenTelemetry collector, see [Collector-based instrumentation samples](https://docs.cloud.google.com/trace/docs/setup/sample-overview) and [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel).

## Why you should migrate

The [OpenTelemetry SDKs](https://opentelemetry.io/docs/languages/) generate log, metric, and trace data in a format that is generally consistent with the proto files defined by the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp). However, fields might be converted from an OpenTelemetry-specific data type to a JSON data type before storage.

When an application exports that data to a Google Cloud project by using a Google Cloud exporter, that exporter performs the following steps:

  1. Transforms the recorded data from OTLP format into a proprietary format defined by the Cloud Logging API, the Cloud Monitoring API, or the Cloud Trace API.
  2. Sends the transformed data to the appropriate API, which is then stored in your Google Cloud project.



For trace data, we recommend that you migrate your application to use the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) to export data, because this export doesn't require a data transformation. Data transformation might cause loss of some data. For example, the proprietary format might have lower limits for certain fields, or some OTLP fields might not map to a field in the proprietary format.

## Available samples

The sample applications referenced on this page are available in GitHub. Most applications are configured to export trace data by using gRPC, which means that they send protobuf-encoded data in the gRPC wire format over HTTP/2 connections. Example code is also provided for applications that are configured to export trace data as protobuf-encoded data over HTTP connections:

  * [Java application](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/java/otlptrace/)

The sample application is configured to export traces as protobuf-encoded data over HTTP connections. If you prefer to use gRPC, then the instrumentation in this sample is applicable. However, you need to modify the system properties that the autoconfiguration module consumes. The sample application specifies the `http/protobuf` exporter. To use gRPC, change this setting to `grpc`.

We recommend that your Java applications, like the sample application, use the [OpenTelemetry SDK Autoconfigure module](https://opentelemetry.io/docs/languages/java/configuration/) to configure the SDK.

  * [Go application that uses gRPC](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/golang/trace/otlpgrpc/) and [Go application that uses HTTP](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/golang/trace/otlphttp/)

There are two Go repositories. In one repository, the sample application uses gRPC. The sample in the other repository uses protobuf-encoded data over HTTP connections.

  * [Python repository](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/python/otlptrace/)

This repository contains two samples, one for gRPC and one that uses protobuf-encoded data over HTTP connections.

  * [Node.js application](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/javascript/otlptraceexport/)

This repository contains two samples, one for gRPC and one that uses protobuf-encoded data over HTTP connections.




## Before you begin

Before you migrate your application to send trace data to the OTLP endpoint, enable the Telemetry API and make sure that you have been granted the required Identity and Access Management (IAM) roles. You might also need to grant IAM roles to a service account.

### Enable billing and the Telemetry API

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Telemetry, Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=telemetry.googleapis.com,logging.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Telemetry, Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=telemetry.googleapis.com,logging.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com)




### Configure permissions

  * To ensure that the service account your application uses has the necessary permissions to write log, metric, and trace data, ask your administrator to grant the following IAM roles to the service account your application uses: 

**Important:** You must grant these roles to the service account your application uses, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 
    * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on your project
    * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on your project
    * [Cloud Telemetry Traces Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.tracesWriter) (`roles/telemetry.tracesWriter`) on your project
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your quota project

To learn how to configure a quota project, see [Set the quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project).

To learn about Application Default Credentials (ADC), see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials) and [Set up Application Default Credentials (ADC) for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).



  * To get the permissions that you need to view your log, metric, and trace data, ask your administrator to grant you the following IAM roles on your project: 

    * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
    * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
    * [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Migration guide for manual instrumentation

This section describes how to modify your application so that it sends your trace data to your Google Cloud project by using the [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview). You can't send metric or log data to this endpoint.

### Add dependencies

The first step is to add dependencies for OpenTelemetry's OTLP trace exporter in your application. Select the dependency versions appropriate for your application and build system.

###  Java 

**Note:** We recommend that you use the [OpenTelemetry SDK Autoconfigure module](https://opentelemetry.io/docs/languages/java/configuration/) to configure the SDK. The sample application uses this module.

For a Java application, in your `build.gradle` script, add the following dependencies:
    
    
    implementation("io.opentelemetry:opentelemetry-exporter-otlp:1.62.0")
    implementation("io.opentelemetry:opentelemetry-sdk-extension-autoconfigure:1.62.0")

###  Go 

This section illustrates changes that you need to make to your dependencies when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then include the `otlptracehttp` package as a dependency. For more information, see [Go application that uses HTTP](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/golang/trace/otlphttp/).

For a Go application that uses gRPC for export, update the `go.mod` file to include the following dependency:
    
    
    require (
    	// ...
    	go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc v1.44.0
    )
    

###  Python 

This section illustrates changes that you need to make to your dependencies when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then include the `opentelemetry-exporter-otlp-proto-http` package as a requirement. For more information, see the [Python repository](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/python/otlptrace/).

For a Python application that uses gRPC for export, install the following dependencies or update the `requirements.txt` file:
    
    
    opentelemetry-exporter-otlp-proto-grpc==1.42.1
    grpcio==1.80.0

###  Node.js 

This section illustrates changes that you need to make to your dependencies when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then include the `@opentelemetry/exporter-trace-otlp-proto` package as a dependency. For more information, see [Node.js application](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/javascript/otlptraceexport/).

For a Node.js application that exports trace data using gRPC, add the following dependencies:
    
    
    "@opentelemetry/exporter-trace-otlp-grpc": "0.221.0",
    "@grpc/grpc-js": "1.14.4"
    

### Replace the use of Google Cloud exporters with OTLP exporters

Update your application code such that the OpenTelemetry SDK is configured to use the OpenTelemetry OTLP exporters instead of a Google Cloud trace exporter. The required changes are language-specific.

###  Java 

For a Java application, do the following:

  1. Add the following import statements:
         
         import io.opentelemetry.sdk.OpenTelemetrySdk;
         import io.opentelemetry.sdk.autoconfigure.AutoConfiguredOpenTelemetrySdk;

  2. Update the application code to use the [OpenTelemetry SDK Autoconfigure module](https://opentelemetry.io/docs/languages/java/configuration/) to configure the SDK:
         
         public static void main(String[] args) {
           // Configure the OpenTelemetry pipeline with Auto configuration
           openTelemetrySdk = AutoConfiguredOpenTelemetrySdk.initialize().getOpenTelemetrySdk();
         
           // ...
         }

  3. Configure the system properties that the autoconfigure module consumes at runtime. That module uses those properties to bootstrap the SDK. You can also use environment variables instead of system properties. For more information, see [Environment variables and system properties](https://opentelemetry.io/docs/languages/java/configuration/#environment-variables-and-system-properties).

The sample application defines the system properties in the `build.gradle` script:
         
         // You can switch the desired protocol here by changing `otel.exporter.otlp.protocol`.
         def autoconf_config = [
         	'-Dotel.exporter.otlp.endpoint=https://telemetry.googleapis.com',
         	'-Dotel.traces.exporter=otlp',
         	'-Dotel.logs.exporter=none',
         	'-Dotel.metrics.exporter=none',
         	'-Dotel.service.name=otlptrace-example',
         	'-Dotel.exporter.otlp.protocol=http/protobuf',
         	'-Dotel.java.global-autoconfigure.enabled=true',
         ]

Also, pass the configuration as JVM arguments:
         
         application {
         	mainClassName = 'com.google.cloud.opentelemetry.samples.otlptrace.OTLPTraceExample'
         	// Pass the config as JVM arguments to the Java application
         	applicationDefaultJvmArgs = autoconf_config
         }

If you prefer to export trace data by using gRPC, then set the OTLP protocol to `grpc` instead of setting it to `http/protobuf`.




###  Go 

This section illustrates changes that you need to make when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then you must import the `otlptracehttp` package and also configure the exporter with corresponding options. For more information, see [Go application that uses HTTP](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/golang/trace/otlphttp/).

For a Go application that uses gRPC for export, add the following import statements:
    
    
    import (
    	"context"
    	"go.opentelemetry.io/otel"
    	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    	sdktrace "go.opentelemetry.io/otel/sdk/trace"
    
    	// ...
    )
    

Also, update the initialization code to configure the `TraceProvider` with the gRPC exporter:
    
    
    // Initializes OpenTelemetry with OTLP exporters
    ctx := context.Background()
    
    // Configure gRPC client with Google Application Default Credentials
    creds, err := oauth.NewApplicationDefault(ctx)
    if err != nil {
    	panic(err)
    }
    
    // set OTEL_RESOURCE_ATTRIBUTES="gcp.project_id=<project_id>"
    // set endpoint with OTEL_EXPORTER_OTLP_ENDPOINT=https://<endpoint>
    // set OTEL_EXPORTER_OTLP_HEADERS="x-goog-user-project=<project_id>"
    // Configure exporter to use the credentials
    exporter, err := otlptracegrpc.New(ctx, otlptracegrpc.WithDialOption(grpc.WithPerRPCCredentials(creds)))
    if err != nil {
    	panic(err)
    }
    
    tp := sdktrace.NewTracerProvider(
    	// For this example code we use sdktrace.AlwaysSample sampler to sample all traces.
    	// In a production application, use sdktrace.TraceIDRatioBased with a desired probability.
    	sdktrace.WithSampler(sdktrace.AlwaysSample()),
    	sdktrace.WithBatcher(exporter))
    
    otel.SetTracerProvider(tp)

###  Python 

This section illustrates changes that you need to make when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then you must import from the `opentelemetry.exporter.otlp.proto.http` package and also configure the exporter with the corresponding options. For more information, see the [Python repository](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/python/otlptrace/).

For a Python application that uses gRPC for export, add the following imports:
    
    
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
        OTLPSpanExporter,
    )
    

Also, update the initialization code to configure the `TraceProvider` with the gRPC exporter:
    
    
    # Initialize OpenTelemetry with OTLP exporters
    # channel_creds: configure Application Default Credentials
    trace_provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(
        OTLPSpanExporter(
            credentials=channel_creds,
            endpoint="https://telemetry.googleapis.com:443/v1/traces",
        )
    )
    trace_provider.add_span_processor(processor)
    trace.set_tracer_provider(trace_provider)
    tracer = trace.get_tracer("my.tracer.name")

###  Node.js 

This section illustrates changes that you need to make when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then import the `@opentelemetry/exporter-trace-otlp-proto` package. For more information, see [Node.js application](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/javascript/otlptraceexport/).

For a Node.js application that uses gRPC for export, add the following imports:
    
    
    import {OTLPTraceExporter} from '@opentelemetry/exporter-trace-otlp-grpc';

Also, update the initialization code to configure the `TraceProvider` with the gRPC exporter:
    
    
    const sdk = new NodeSDK({
      traceExporter: new OTLPTraceExporter({
        credentials: credentials.combineChannelCredentials(
          credentials.createSsl(),
          credentials.createFromGoogleCredential({
            async getRequestHeaders(
              url?: string,
            ): Promise<{[index: string]: string}> {
              const rawHeaders = await authenticatedClient.getRequestHeaders(url);
              return Object.fromEntries(rawHeaders.entries());
            },
          }),
        ),
      }),
    });
    sdk.start();

### Configure authentication

With the previous changes to the OpenTelemetry SDK configuration, your application is configured to export traces with the OpenTelemetry OTLP exporters by using either gRPC or HTTP. Next, you need to configure the exporters to send those traces to your Google Cloud project.

To configure authentication, do the following:

  1. Configure authentication headers for the export calls.
  2. Configure the required OpenTelemetry resource attributes and OTLP headers.
  3. Configure the exporter endpoint.



This section details each of these steps.

#### Configure authentication headers for the export calls

To configure the exporter with your Google Cloud [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc), add a language-specific Google Auth Library.

###  Java 

For a Java application that uses the [OpenTelemetry SDK Autoconfigure module](https://opentelemetry.io/docs/languages/java/configuration/), we recommend that you also use the [Google Cloud Authentication Extension](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/gcp-auth-extension/README.md).
    
    
    implementation("io.opentelemetry.contrib:opentelemetry-gcp-auth-extension:1.56.0-alpha")

###  Go 

For a Go application that uses gRPC for export, update the `go.mod` file to include the following dependency:
    
    
    // When using gRPC based OTLP exporter, the auth is built in.
    google.golang.org/grpc v1.82.1

For a Go application that uses HTTP for export, update the `go.mod` file to include the following dependency:
    
    
    // When using http based OTLP exporter, use explicit auth library
    golang.org/x/oauth2 v0.36.0

###  Python 

For a Python application, add the following dependencies to your `requirements.txt` file:
    
    
    # Google Auth Library
    google-auth==2.53.0

###  Node.js 

For a Node.js application, add the following dependency:
    
    
    "google-auth-library": "10.5.0"
    

Next, update the application code that constructs the OTLP span exporter so that it adds the authorization tokens retrieved from the library to the headers. This step is language-specific, but the implementation is similar for all languages.

###  Java 

When you have a Java application that uses the [OpenTelemetry SDK Autoconfigure module](https://opentelemetry.io/docs/languages/java/configuration/) and the [Google Cloud Authentication Extension](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/gcp-auth-extension/README.md), you don't need to perform any special steps during your application's initialization. The autoconfigure module automatically performs the steps necessary to configure ADC.

###  Go 

This section illustrates changes that you need to make when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then you must import the `otlptracehttp` package and configure the exporter to be an `otlptracehttp` object. For more information, see [Go application that uses HTTP](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/golang/trace/otlphttp/).

For a Go application that uses gRPC for export, add the following import statements:
    
    
    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials/oauth"

Also, update the initialization code to configure ADC before you instantiate the gRPC exporter:
    
    
    // Initializes OpenTelemetry with OTLP exporters
    ctx := context.Background()
    
    // Configure gRPC client with Google Application Default Credentials
    creds, err := oauth.NewApplicationDefault(ctx)
    if err != nil {
    	panic(err)
    }
    
    // set OTEL_RESOURCE_ATTRIBUTES="gcp.project_id=<project_id>"
    // set endpoint with OTEL_EXPORTER_OTLP_ENDPOINT=https://<endpoint>
    // set OTEL_EXPORTER_OTLP_HEADERS="x-goog-user-project=<project_id>"
    // Configure exporter to use the credentials
    exporter, err := otlptracegrpc.New(ctx, otlptracegrpc.WithDialOption(grpc.WithPerRPCCredentials(creds)))
    if err != nil {
    	panic(err)
    }
    
    tp := sdktrace.NewTracerProvider(
    	// For this example code we use sdktrace.AlwaysSample sampler to sample all traces.
    	// In a production application, use sdktrace.TraceIDRatioBased with a desired probability.
    	sdktrace.WithSampler(sdktrace.AlwaysSample()),
    	sdktrace.WithBatcher(exporter))
    
    otel.SetTracerProvider(tp)

###  Python 

This section illustrates changes that you need to make when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then use the default credentials. You must also pass these credentials when you instantiate the `BatchSpanProcessor`. For more information, see the [Python repository](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/python/otlptrace/).

For a Python application that uses gRPC for export, add the following imports:
    
    
    import google.auth
    import google.auth.transport.grpc
    import google.auth.transport.requests
    import grpc
    from google.auth.transport.grpc import AuthMetadataPlugin
    

Also, update the initialization code to configure ADC before you instantiate the gRPC exporter:
    
    
    credentials, _ = google.auth.default()
    request = google.auth.transport.requests.Request()
    resource = Resource.create(attributes={SERVICE_NAME: "otlp-gcp-grpc-sample"})
    
    auth_metadata_plugin = AuthMetadataPlugin(credentials=credentials, request=request)
    channel_creds = grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(),
        grpc.metadata_call_credentials(auth_metadata_plugin),
    )

###  Node.js 

This section illustrates changes that you need to make when using gRPC for export. If you use protobuf-encoded data over HTTP connections for export, then the changes you need to make are slightly different from those described here. To learn more, see the `app-http-proto-export.ts` file that is included in the [Node.js application](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/javascript/otlptraceexport/).

For a Node.js application that uses gRPC for export, add the following imports:
    
    
    import {AuthClient, GoogleAuth} from 'google-auth-library';
    import {credentials} from '@grpc/grpc-js';

Also, update the initialization code to configure ADC before you instantiate the gRPC exporter:
    
    
    async function getAuthenticatedClient(): Promise<AuthClient> {
      const auth: GoogleAuth = new GoogleAuth({
        scopes: 'https://www.googleapis.com/auth/cloud-platform',
      });
      return await auth.getClient();
    }
    
    // Express App that exports traces via gRPC with protobuf
    async function main() {
      const authenticatedClient: AuthClient = await getAuthenticatedClient();
    
      // ...
    }

#### Configure the required OpenTelemetry resource attributes

Add to the `OTEL_RESOURCE_ATTRIBUTES` environment variable the key-value pair that specifies your project. For the key, use `gcp.project_id`. For the value, use the ID of your Google Cloud project.

Example:
    
    
    export OTEL_RESOURCE_ATTRIBUTES="gcp.project_id=PROJECT_ID"
    

If you use Java and configure your application to use the [Google Cloud Authentication Extension](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/gcp-auth-extension/README.md), as the sample Java application does, then you don't need to set the project ID as part of the OpenTelemetry resource attributes. However, setting this attribute isn't harmful.

For more information about OpenTelemetry environment variables, see [General SDK Configuration](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration).

#### Set the quota project ID

The [quota project](https://docs.cloud.google.com/docs/quotas/quota-project) is the Google Cloud project that tracks your usage of API requests. Because the Telemetry API is a client-based API, how you authenticate determines whether the quota project is automatically identified. For example, you don't need to specify the quota project when you use a service account for authentication. However, you do need to specify the quota project when user credentials are used for authentication.

You can set a quota project by using an environment variable. To determine which environment variable to set for your programming language, see [Set the quota project using an environment variable](https://docs.cloud.google.com/docs/quotas/set-quota-project#set-project-variable).

For example, for Go, you can set the quota project as follows:
    
    
    export GOOGLE_CLOUD_QUOTA_PROJECT="QUOTA_PROJECT_ID"
    

For information about how to resolve authentication errors, see [User credentials not working](https://docs.cloud.google.com/docs/authentication/troubleshoot-adc#user-creds-client-based).

**Note:** Don't update the `OTEL_EXPORTER_OTLP_HEADERS` environment variable with a key-value pair that uses the key `x-goog-user-project`. This configuration can result in duplicate values in the request, and that causes API commands to fail.

#### Configure the exporter endpoint

Set the value of the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable to the OTLP endpoint for Google Cloud.

Example:
    
    
    export OTEL_EXPORTER_OTLP_ENDPOINT=https://telemetry.googleapis.com
    

If you use Java and the autoconfigure module, then you can set the exporter endpoint by using system properties, as the sample Java application does. You don't need to set the exporter environment variable for that configuration.

For more information about OpenTelemetry environment variables, see [General SDK Configuration](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
