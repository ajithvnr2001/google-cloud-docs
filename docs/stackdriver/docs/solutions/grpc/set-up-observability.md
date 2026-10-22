---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability/
title: Set up Microservices observability \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:45.870182+00:00
---

# Set up Microservices observability  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Set up Microservices observability Stay organized with collections  Save and categorize content based on your preferences. 

This document contains the information you need to set up the Microservices observability plugin, instrument your gRPC applications, and obtain information from Cloud Monitoring, Cloud Logging, and Cloud Trace.

## Before you begin

Microservices observability works with any deployment that has been granted permission to access Cloud Monitoring, Cloud Logging, and Cloud Trace by enabling the Microservices API. This guide provides an example setup of Microservices observability using a Compute Engine example.

At a high level, you do the following:

  1. As a **service developer** , you opt in and control the Microservices observability plugin.
  2. As a **service operator** , you consume the collected data in various ways.



The gRPC repositories (C++, Go, and Java) include examples for demonstrating Microservices observability.

Before you configure observability, complete the following tasks:

  1. Read the [Microservices observability overview](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc).
  2. Make sure that you have an existing project or [create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  3. Make sure that you have an existing service account or [create a new one](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).
  4. Read about the two supported environment variables, decide which to use, and determine the values required by the environment variable.
  5. Enable the Microservices API.



### Choose a configuration environment variable

When you opt in to the Microservices observability plugin, which is described in [Instrument your applications for the observability plugin](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability#instrument-apps), you must provide configuration information using an environment variable. By default, no observability features are enabled. You set the environment variable on the VM or container where the gRPC application or workload is running.

The following are the environment variables:

  * `GRPC_GCP_OBSERVABILITY_CONFIG_FILE`: the value is a path pointing to a JSON encoded config file.
  * `GRPC_GCP_OBSERVABILITY_CONFIG`: the value is the body of the config encoded in JSON.



If both environment variables are set, `GRPC_GCP_OBSERVABILITY_CONFIG_FILE` takes precedence over `GRPC_GCP_OBSERVABILITY_CONFIG`.

To apply the configuration, you must restart the gRPC application. You cannot set or view the values of the environment variables in the Google Cloud console.

In the configuration, you can set a destination project to which logging, tracing, and metrics data are uploaded. You set the project ID in the `project_id` field.

  * If this field is left empty, the observability plugin automatically fills the value of the project ID based on the [application default credentials](https://docs.cloud.google.com/docs/authentication/production#automatically).

  * If the [application default credentials](https://docs.cloud.google.com/docs/authentication/production#automatically) cannot be identified and the `project_id` field is empty, the `INIT/START` method raises or returns an error to your application. The application must then handle the error.




Use the information in [Configuration data](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference#configuration-data) to set the values in the environment variable you choose.

### Enable the Microservices API

You can use the gcloud CLI or the Google Cloud console to enable the Microservices API in your projects. Enabling the Microservices API automatically enables the Cloud Logging API, Cloud Monitoring API, and Cloud Trace API.

To enable the API:
    
    
    gcloud services enable microservices.googleapis.com
    

### Set service account permissions

If you are using a non-default service account, grant the required permissions for the service account. Set the following values:

  * PROJECT_ID: Substitute your project ID.
  * SERVICE_ACCOUNT_NAME: Substitute the service account name of your project.


    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
      --role=roles/logging.logWriter
    
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID> \
      --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
      --role=roles/monitoring.metricWriter
    
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
      --role=roles/cloudtrace.agent
    

## Instrument your applications for the observability plugin

To instrument your applications so that they can use the Microservices observability plugin, use the following instructions for C++, Java, and Go.

**Note:** Microservices observability, which utilizes OpenCensus for instrumentation, is incompatible with the direct use of OpenCensus due to its global memory consumption. If you are using Stackdriver exporters with OpenCensus, you can take advantage of Microservices observability to automatically configure Stackdriver exporters. However, the simultaneous use of non-Stackdriver exporters alongside Microservices observability is not supported.

### C++

You can use C++ with Microservices observability as of gRPC C++ v1.54. The [example repository](https://github.com/grpc/grpc/tree/v1.54.0/examples/cpp/gcp_observability/helloworld) is in GitHub.

#### Build changes

Observability support is only available through the Bazel build system. Add the target `grpcpp_gcp_observability` as a dependency.

#### Required code changes

Opting in Microservices observability requires an additional dependency (an observability module) and the following code changes to existing gRPC clients, servers, or both:
    
    
    #include <grpcpp/ext/gcp_observability.h>
    
    int main(int argc, char** argv) {
      auto observability = grpc::GcpObservability::Init();
      assert(observability.ok());
      …
      // Observability data flushed when object goes out of scope
    }
    

Before any gRPC operations, including creating a channel, server, or credentials, invoke the following:
    
    
    grpc::GcpObservability::Init();
    

This returns `absl::StatusOr<GcpObservability>` which should be saved. The status helps determine whether observability was successfully initialized. The accompanying `GcpObservability` object controls the lifetime of observability, and automatically closes and flushes observability data when it goes out of scope.

### Go

Microservices observability plugins are supported for gRPC Go versions `v1.54.0` and later. The [example repository](https://github.com/grpc/grpc-go/tree/master/examples/features/observability) is in GitHub.

With the Go module, opting in Microservices observability requires an observability module and the following code:
    
    
    import "google.golang.org/grpc/gcp/observability"
    
    func main() {
           ctx, cancel := context.WithTimeout(context.Background(), time.Second)
           defer cancel()
           if err := observability.Start(ctx); err != nil {
                  log.Warning("Unable to start gRPC observability:", err)
           }
           defer observability.End()
           …
    }
    

The `observability.Start` call parses the configuration from environment variables, creates exporters accordingly, and injects collection logic to client connections and servers created after the call. The deferred `observability.End` call cleans up resources and ensures that buffered data is flushed before the application closes.

After the application code is updated, run the following command to update the `go.mod` file.
    
    
    go mod tidy
    

### Java

To use Microservices observability with Java applications, modify your build to include the `grpc-gcp-observability` artifact. Use gRPC version 1.54.1 or later.

In the build snippets in the Gradle and Maven build tool sections, `grpcVersion` is set to the value 1.54.1.

The [example repository](https://github.com/grpc/grpc-java/tree/v1.54.1/examples/example-gcp-observability) is in GitHub.

#### Required Java code changes

To successfully instrument your Java applications for Microservices observability, add the following code to `main()`.
    
    
    ...
    import io.grpc.gcp.observability.GcpObservability;
    ...
    
    // Main application class
    ...
    
    public static void main(String[] args) {
    ...
       // call GcpObservability.grpcInit() to initialize & get observability
       GcpObservability observability = GcpObservability.grpcInit();
    
    ...
       // call close() on the observability instance to shutdown observability
       observability.close();
    ...
    }
    

Note that you must call `GcpObservability.grpcInit()` before any gRPC channels or servers are created. The `GcpObservability.grpcInit()` function reads the Microservices observability configuration and uses that to set up the global interceptors and tracers that are required for the logging, metrics, and trace functionality in each channel and server created. `GcpObservability.grpcInit()` is thread safe and must be called exactly once. It returns an instance of `GcpObservability` that you must save in order to call `close()` later.

`GcpObservability.close()` de-allocates resources. Any channel or servers created afterwards don't perform any logging.

`GcpObservability` implements `java.lang.AutoCloseable`, which is closed automatically if you use `try-with-resource`s as follows:
    
    
    ...
    import io.grpc.gcp.observability.GcpObservability;
    ...
    
    // Main application class
    ...
    
    public static void main(String[] args) {
    ...
       // call GcpObservability.grpcInit() to initialize & get observability
       try (GcpObservability observability = GcpObservability.grpcInit()) {
    
    ...
       } // observability.close() called implicitly
    ...
    }
    

#### Use the Gradle build tool

If you are using the Gradle build tool, then include the following:
    
    
    def grpcVersion = '1.54.1'
    
    ...
    
    dependencies {
    ...
       implementation "io.grpc:grpc-gcp-observability:${grpcVersion}"
    ...
    }
    

#### Use the Maven build tool (pom.xml)

If you are using the Maven build tool, then include the following:
    
    
    <properties>
    ...
      <grpc.version>1.54.1</grpc.version>
    ...
    </properties>
    
    ...
    
    <dependencies>
    ...
     <dependency>
       <groupId>io.grpc</groupId>
       <artifactId>grpc-gcp-observability</artifactId>
       <version>${grpc.version}</version>
     </dependency>
    ...
    </dependencies>
    

## Enable metrics, tracing, and logging data collection

The following sections contain instructions for enabling data collection in your configuration and an example showing the configuration information in an environment variable.

### Enable metrics

To enable metrics, add the `cloud_monitoring` object to the configuration and set its value to `{}`.

For more information about metrics, see [Metrics definitions](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference#metrics-def).

### Enable tracing

If you plan to enable tracing across services, ensure that the services support the propagation of trace context received from upstream (or started by itself) to downstream.

To enable tracing, do the following:

  1. Add the `cloud_trace` object to the configuration.
  2. Set the `cloud_trace.sampling_rate` to a probability that you want your application to observe to start new traces. 
     * For example, `1.0` means tracing every RPC.
     * `0.0` means don't start any new traces.
     * `0.5` means that 50% of RPCs are randomly traced.



If a positive sampling decision is made upstream, your services upload spans regardless of the sampling rate setting.

For more information about tracing, see [Trace definitions](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference#trace-def).

### Enable logging

To enable logging, do the following:

  1. Add the `cloud_logging` object to the configuration.
  2. Add a pattern to either or both of `client_rpc_events` and `server_rpc_events` specifying the set of services or methods for which you want to generate transport-level event logging and the number of bytes to log for headers and messages.



For more information about logging, see [Log record definitions](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference#log-record-defs).

### Environment variable example

The following example sets the observability variables in the environment variable `GRPC_GCP_OBSERVABILITY_CONFIG`:
    
    
    export GRPC_GCP_OBSERVABILITY_CONFIG='{
         "project_id": "your-project-here",
         "cloud_logging": {
             "client_rpc_events": [
             {
                 "methods": ["google.pubsub.v1.Subscriber/Acknowledge", "google.pubsub.v1.Publisher/CreateTopic"],
                 "exclude": true
             },
             {
                 "methods": ["google.pubsub.v1.Subscriber/*", "google.pubsub.v1.Publisher/*"],
                 "max_metadata_bytes": 4096,
                 "max_message_bytes": 4096
             }],
             "server_rpc_events": [{
                 "methods": ["*"],
                 "max_metadata_bytes": 4096,
                 "max_message_bytes": 4096
             }],
         },
         "cloud_monitoring": {},
         "cloud_trace": {
             "sampling_rate": 1.00
         },
         "labels": {
             "SOURCE_VERSION": "J2e1Cf",
             "SERVICE_NAME": "payment-service-1Cf",
             "DATA_CENTER": "us-west1-a"
         }
    }'
    

## Create the observability example

Use these instructions to create and connect to a Compute Engine VM instance and then set up the observability example.

  1. Create a VM instance:
         
         gcloud compute instances create grpc-observability-vm \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         

  2. Connect to the VM instance:
         
         gcloud compute ssh --project=PROJECT_ID grpc-observability-vm
         




Continue with the instructions for Java, C++, or Go, depending on the language of your gRPC applications.

###  Java 

  1. After you connect to the VM instance, make sure that you have Java 8 or later installed.
         
         sudo apt update
         sudo apt upgrade
         sudo apt install git
         sudo apt-get install -y openjdk-11-jdk-headless
         

  2. Clone the `grpc-java` repository.
         
         export EXAMPLES_VERSION=v1.54.1
         git clone -b $EXAMPLES_VERSION --single-branch --depth=1 \
         https://github.com/grpc/grpc-java.git
         

  3. Go to the examples directory.
         
         cd grpc-java/examples/example-gcp-observability
         

  4. In the examples directory, open the README file and follow the instructions in the file.

  5. When the instructions tell you to open another terminal window, issue this command:
         
         gcloud compute ssh --project=PROJECT_ID grpc-observability-vm
         




###  C++ 

  1. After you connect to the VM instance, run a `hello-world` server binary in a terminal window.
         
         sudo apt-get update -y
         sudo apt-get install -y git build-essential clang
         git clone -b v1.54.0 https://github.com/grpc/grpc.git --depth=1
         cd grpc
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID
         export GRPC_GCP_OBSERVABILITY_CONFIG_FILE="$(pwd)/examples/cpp/gcp_observability/helloworld/server_config.json"
         tools/bazel run examples/cpp/gcp_observability/helloworld:greeter_server
         

  2. From another terminal window, connect to the VM again by using SSH, and then run the following commands, which run the `hello-world` client binary.
         
         cd grpc
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID
         export GRPC_GCP_OBSERVABILITY_CONFIG_FILE="$(pwd)/examples/cpp/gcp_observability/helloworld/client_config.json"
         tools/bazel run examples/cpp/gcp_observability/helloworld:greeter_client
         




###  Go 

  1. Make sure that you have Go installed.
         
         sudo apt-get install -y git
         sudo apt install wget
         wget https://go.dev/dl/go1.20.2.linux-amd64.tar.gz
         sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf \
         go1.20.2.linux-amd64.tar.gz
         export PATH=$PATH:/usr/local/go/bin
         

  2. Clone the `gRPC-Go` examples.
         
         git clone https://github.com/grpc/grpc-go.git
         cd grpc-go/
         git checkout -b run-observability-example
         875c97a94dca8093bf01ff2fef490fbdd576373d
         

  3. Go to the `gRPC-Go` directory clone:
         
         cd examples/features/observability
         

  4. Run the server.
         
         export GRPC_GCP_OBSERVABILITY_CONFIG_FILE=./server/serverConfig.json
         go run ./server/main.go
         

  5. In a separate terminal window, run the following commands.
         
         export PATH=$PATH:/usr/local/go/bin
         cd grpc-go/examples/features/observability
         export GRPC_GCP_OBSERVABILITY_CONFIG_FILE=./client/clientConfig.json
         go run ./client/main.go
         




## View traces, metrics, and log entries

Use the instructions in this section to view traces, metrics, and log entries.

### View traces on Cloud Trace

After you set up the examples or you have instrumented your workloads, you should see traces generated by your gRPC clients and gRPC servers in the Google Cloud console listed as recent traces.

[ ![Microservices observability trace list.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/trace-ss.png)](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/trace-ss.png) Microservices observability trace list (click to enlarge)

#### View logs for traces

If you enable both logging and tracing, you can view log entries for traces alongside the [Cloud Trace waterfall graph](https://docs.cloud.google.com/trace/docs/trace-log-integration#viewing_logs) or in Logs Explorer.

### View metrics on the dashboard

Microservices observability provides a monitoring dashboard called **Microservices (gRPC) Monitoring** for the metrics defined in [Metrics definitions](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference#metrics-def). The dashboard is displayed in Google Cloud console only when the Microservices API is enabled. The Google Cloud console calls the Service Usage API to verify whether the Microservices API is enabled in a project. The user must have the `serviceusage.services.list` permission to view the dashboard.

The **Microservices (gRPC) Monitoring** dashboard is a Google Cloud dashboard and you cannot directly modify it. To customize the dashboard, you must copy the dashboard to a custom dashboard. You can then update the custom dashboard, for example by adding, deleting, or re-arranging the charts.

### View metrics on Metrics Explorer

After you set up the gRPC example or you instrument your workload, you should see metrics generated by your gRPC clients and gRPC servers in the Google Cloud console.

To view and chart metrics, use the instructions in [Select metrics when using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector)

### Inspect log entries on Logs Explorer

Suggested query is a Cloud Logging feature in which Google Cloud suggests a set of queries based on the ingested logs. You can click and use the prepared filters.

[ ![Suggested queries in Logs Explorer.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/suggested-query.svg)](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/suggested-query.svg) Suggested queries in Logs Explorer. (click to enlarge)

After the log entries matching suggested queries appear in Cloud Logging, you can expect to see new suggested queries in approximately 6 minutes. In most cases, you see new suggested queries sooner. If there are log entries that match a suggestion in the previous 15 minutes, any suggested queries continue to be displayed. They continue to appear as a suggestion until there haven't been any matching log entries in the previous 15 minutes.

You can create customized queries. See the [Logging query language guide](https://docs.cloud.google.com/logging/docs/view/logging-query-language) for instructions. For example, in the Query pane of the Logs Explorer, you can try to show all the gRPC debug logs with the following code:
    
    
    log_id("microservices.googleapis.com/observability/grpc")
    

You can use all fields in the gRPC log record for filtering. Here is an example log entry:
    
    
    {
      "insertId": "17kh8vafzuruci",
      "jsonPayload": {
        "authority": "10.84.1.15:50051",
        "sequenceId": "6",
        "serviceName": "helloworld.Greeter",
        "peer": {
          "ipPort": 50051,
          "address": "10.84.1.10",
          "type": "IPV4"
        },
        "callId": "d9577780-c608-4bff-9e12-4d9cdea6b298",
        "type": "SERVER_TRAILER",
        "methodName": "SayHello",
        "payload": {},
        "logger": "CLIENT"
      },
      "resource": {
        "type": "k8s_container",
        "labels": {
          "pod_name": "grpc-client-deployment-155-6967959544-x8ndr",
          "container_name": "grpc-client-container-155",
          "cluster_name": "o11y-cluster",
          "namespace_name": "grpc-client-namespace-155",
          "location": "us-west1-b",
          "project_id": "grpc-greeter"
        }
      },
      "timestamp": "2023-04-05T23:33:41.718523Z",
      "severity": "DEBUG",
      "labels": {
        "environment": "example-client"
      },
      "logName": "projects/grpc-greeter/logs/microservices.googleapis.com%2Fobservability%2Fgrpc",
      "receiveTimestamp": "2023-04-05T23:33:42.712682457Z"
    }
    

### Suggested queries

Microservices observability provides the following [suggested queries](https://docs.cloud.google.com/logging/docs/view/building-queries#suggested_queries) to Cloud Logging:

#### Header or trailer log records for gRPCs

This query gives a basic view of RPCs, yielding peer information and RPC results.
    
    
    log_id("microservices.googleapis.com/observability/grpc") AND
    jsonPayload.type=("CLIENT_HEADER" OR "SERVER_TRAILER")
    

#### Failed gRPC calls

This query finds the RPCs that end with non-OK status.
    
    
    log_id("microservices.googleapis.com/observability/grpc") AND
    jsonPayload.type="SERVER_TRAILER" AND
    jsonPayload.payload.statusCode!="OK"
    

#### Log records for canceled or deadline-exceeded gRPCs

Excessive gRPC cancellation or deadline-exceeds can provide useful information about performance loss or unexpected application behavior.
    
    
    log_id("microservices.googleapis.com/observability/grpc") AND
    ((jsonPayload.type="SERVER_TRAILER" AND jsonPayload.payload.statusCode=("CANCELLED" OR "DEADLINE_EXCEEDED")) OR (jsonPayload.type="CANCEL"))
    

## Use logs and tracing for troubleshooting

If you see an RPC event that indicates bad behavior, you can find the `callId` in the event. Use the following query to display all the events that happened in one RPC, regardless of whether it's a unary or streaming RPC. The previous log entry is used as an example:
    
    
    log_id("microservices.googleapis.com/observability/grpc")
    jsonPayload.callId="a358c7b80-3548-4bc8-a33f-b93ba1514904"
    

To determine the scope of the issue, you can find all RPC events for the same method or location. The following query shows all of the debug logs related to a specific RPC method, using the Greeter service as an example:
    
    
    log_id("microservices.googleapis.com/observability/grpc")
    jsonPayload.serviceName="helloworld.Greeter"
    jsonPayload.methodName="SayHello"
    

To check the failed RPCs of a specific status code, you can add the status code as one of the filtering conditions. The following query shows the trailer events that end with non-OK status:
    
    
    log_id("microservices.googleapis.com/observability/grpc")
    jsonPayload.payload.statusCode!="OK"
    

[ ![Query results: deadline exceeded status code.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/deadline-exceeded.svg)](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/deadline-exceeded.svg) Query results: deadline exceeded status code (click to enlarge)

## Observability options

Microservices observability includes the following optional features.

### Define custom labels

You can define _custom labels_ , which add user-provided information to the observability data. Custom labels consist of key-value pairs. Each key-value pair is attached to tracing data as span labels, to metrics data as metric tags, and to logging data as log entry labels.

Custom labels are defined in the configuration with a list of key-value pairs in the `labels` field. All keys and values for custom labels are STRING types. The implementation reads the configuration and creates a separate label for each key-value pair, then attaches the labels to the observability data.

For example, this is a label definition:
    
    
    "labels": {
        "DATACENTER": "SAN_JOSE_DC",
        "APP_ID": "24512"
      }
    

Each log entry has the following additional labels:
    
    
    {
       "DATACENTER" : "SAN_JOSE_DC"
       "APP_ID" : "24512"
    }
    

[ ![Querying labels in a log entry.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/tag-query.svg)](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/tag-query.svg) Querying labels in a log entry (click to enlarge)[ ![Line chart showing custom and resource labels.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/custom-location-tags.png)](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/custom-location-tags.png) Line chart showing custom and resource labels (click to enlarge)

### Enable payload logging

You enable payload logging using the environment variables that you supply to the workload. To turn on payload logging for HelloWorld messages and headers, update the value of the configuration files `gcp_observability_server_config.json`, `gcp_observability_client_config.json` or both in the gRPC examples as follows:
    
    
    {
       "cloud_monitoring":{
       },
       "cloud_trace":{
          "sampling_rate":1.0
       },
       "cloud_logging":{
          "client_rpc_events":[
             {
                "methods":[
                   "helloworld.Greeter/*"
                ],
                "max_metadata_bytes":4096,
                "max_message_bytes":4096
             }
          ],
          "server_rpc_events":[
             {
                "methods":[
                   "helloworld.Greeter/*"
                ],
                "max_metadata_bytes":4096,
                "max_message_bytes":4096
             }
          ]
       }
    }
    

### Set up cross-project observability

You can set the destination project explicitly using the configuration set in the environment variable `GRPC_GCP_OBSERVABILITY_CONFIG`. For cross-project observability, you also have to set the appropriate service account permissions. Assuming the destination project ID is `core-platform-stats`, you can set up cross-project observability using the following example configuration:
    
    
    {
       "project_id":"core-platform-stats",
       "cloud_monitoring":{
       },
       "cloud_trace":{
          "sampling_rate":1.0
       },
       "cloud_logging":{
          "client_rpc_events":[
             {
                "methods":[
                   "helloworld.Greeter/*"
                ]
             }
          ],
          "server_rpc_events":[
             {
                "methods":[
                   "helloworld.Greeter/*"
                ]
             }
          ]
       }
    }
    
    

### Estimate log volume

This section gives you information you can use to optionally estimate log ingestion volume. You can make an estimate before you subscribe to the RPC events of your services.

**Item** | **Detail**  
---|---  
Events generated for an OK unary call | 6 events  
  
An OK unary call RPC generates the following 6 events for client or server:  
  


  * CLIENT_HEADER


  * SERVER_HEADER


  * CLIENT_MESSAGE


  * SERVER_MESSAGE


  * CLIENT_HALF_CLOSE


  * SERVER_TRAILER

  
Average size of log entry | 500 bytes by default  
  
A log entry maps to one RPC event, the RPC event includes the detailed debugging information for that event, resource labels, and custom labels.  
Payload logging size | 0 by default, can be configured  
  
Maximum payload size is configurable in the observability configuration. By default, no payload is logged.  
Custom labels size | 0 by default, can be configured  
  
Custom labels are provided to the application using environment variables. If none specified, there will be no custom labels  
  
Total size of log ingestion per month estimation formula:

`Monthly Log Ingestion = QPS * 6 * (500B + Payload Logging Size + Custom Labels Size) * 2592000`

For example, if the QPS of a unary call method is 1 and no extra features are enabled, the estimated log ingestion size is approximately 7.24 GiB.

## What's next

  * For detailed information about configuration data, trace definitions, metrics definitions, and log definitions see [Microservices observability reference](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
