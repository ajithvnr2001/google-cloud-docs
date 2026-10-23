---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/observability-envoy/
title: Observability with Envoy \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:49.270533+00:00
---

# Observability with Envoy  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/observability-envoy/

You are viewing archived v1.25 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Observability with Envoy

This document demonstrates how to generate tracing and logging for the Envoy proxy. It also shows you how to export the information to [Cloud Trace](https://docs.cloud.google.com/trace/docs) and [Cloud Logging](https://docs.cloud.google.com/logging/docs).

Using a service mesh gives you the ability to observe traffic to and from services, which allows for richer monitoring and debugging without code changes in the service itself. In the sidecar proxy architecture that Cloud Service Mesh uses, the proxy is the component that processes requests and provides the necessary telemetry information. Telemetry information must be collected and stored in a centralized location for further use, such as data analysis, alerting, and troubleshooting.

**Note:** Depending on the volume of requests handled by the application, enabling logging and/or tracing of the requests can affect sidecar proxy performance. For more information, see the documentation for your xDS API-compatible proxy.

## Demonstration setup

This document uses the following configuration to demonstrate tracing and logging:

  * A single application that listens on the HTTP port and returns the hostname of the virtual machine (VM) instance that served the request. In the diagram, this application is in the upper-right corner, labeled **HTTP service(s) (10.10.10.10:80)**. One or more VMs can provide this service.
  * A single Compute Engine VM running a consumer of this service. In the diagram, this is labeled **Demo Compute Engine VM**.
  * An Envoy sidecar proxy installed and configured by Cloud Service Mesh. In the diagram, this is labeled **envoy**.
  * A service consumer application, shown in the box on the left, is the consumer of the HTTP service running on `10.10.10.10:80`.

[ ![Demonstration application for logging and monitoring for Envoy.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/td-stackdriver-envoy.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/td-stackdriver-envoy.svg) Demonstration application for logging and monitoring for Envoy (click to enlarge)

The following steps correspond to the numbered labels in the diagram:

  1. Cloud Service Mesh configures the Envoy proxy to do the following:

     * Load balance traffic for the `10.10.10.10:80` service.
     * Store access log information for each request issued for this service.
     * Generate tracing information for the service.
  2. After the consumer sends a request to `10.10.10.10`, the sidecar proxy routes the request to the correct destination.

  3. The sidecar proxy also generates the necessary telemetry information:

     1. Adds an entry to the access log on the local disk with additional information about the request.
     2. Generates a trace entry and sends it to Trace by using OpenCensus Envoy tracing.
  4. The Logging agent exports this data to the Cloud Logging API so that the data becomes available in the Cloud Logging interface.




## Prerequisites

Before you complete the setup steps, ensure that the following is done:

  1. The Traffic Director API is enabled and other prerequisites are met, as described in [Prepare to set up with VM and proxyless workloads](https://docs.cloud.google.com/service-mesh/v1.25/docs/onboarding/vm-and-proxyless-workloads).
  2. The [Cloud Trace API](https://docs.cloud.google.com/trace/docs/setup#gcp-config) is enabled.
  3. The service account that the Compute Engine VM uses has the following Identity and Access Management (IAM) roles configured: 
     * [Cloud Trace Agent role](https://docs.cloud.google.com/trace/docs/iam#roles) (`roles/cloudtrace.agent`)
     * [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.logWriter`)
  4. The [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) allow traffic to the VM that you configure as part of this setup.



## Set up the demonstration service and Cloud Service Mesh

This document uses several shell scripts to perform the steps required to configure the demonstration service. Review the scripts to understand the specific steps that they perform.

  1. Start a Compute Engine VM and configure the HTTP service on the VM:
         
         curl -sSO https://storage.googleapis.com/traffic-director/demo/observability/setup_demo_service.sh
         chmod 755 setup_demo_service.sh && ./setup_demo_service.sh
         

The `setup_demo_service.sh` script creates a VM template that launches apache2 when a VM starts and a managed instance group that uses this template. The script launches a single instance without autoscaling enabled.

  2. Use Cloud Service Mesh to configure routing for the `10.10.10.10` service:
         
         curl -sSO https://storage.googleapis.com/traffic-director/demo/observability/setup_demo_trafficdirector.sh
         chmod 755 setup_demo_trafficdirector.sh && ./setup_demo_trafficdirector.sh
         

The `setup_demo_trafficdirector.sh` script configures the necessary parameters for the Cloud Service Mesh managed service.

  3. Start a Compute Engine VM that runs a consumer of the HTTP service, with the sidecar proxy installed and configured on the VM. In the following command, replace `PROJECT_ID` with the project ID to which Trace information should be sent. This is typically the same Google Cloud project to which your VM belongs.
         
         curl -sSO https://storage.googleapis.com/traffic-director/demo/observability/setup_demo_client.sh
         chmod 755 setup_demo_client.sh && ./setup_demo_client.sh PROJECT_ID
         

The `setup_demo_client.sh` script creates a Compute Engine VM that has an Envoy proxy preconfigured to use Cloud Service Mesh.




The following additional configuration settings enable tracing and logging:

  * The `TRAFFICDIRECTOR_ACCESS_LOG_PATH` and `TRAFFICDIRECTOR_ENABLE_TRACING` bootstrap node metadata variables enable logging and tracing, as described in [Configure Envoy bootstrap attributes for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/per-proxy-config).
  * Static bootstrap configuration enables export of trace information to Trace by using OpenCensus.

**Note:** You can add and modify additional tracing parameters by using the [Envoy runtime](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/runtime#config-http-conn-man-runtime-random-sampling) configuration.

After running these scripts, you can sign in to the `td-observability-demo-client` VM and access the HTTP service available at `10.10.10.10`:
    
    
    curl http://10.10.10.10
    

At this point, Envoy generates access logging and tracing information. The following section describes how to export logs and tracing information.

## Set up trace export to Cloud Trace

The Envoy bootstrap configuration that you created when you ran the `setup-demo-client.sh` script is sufficient to generate tracing information. All other configuration is optional. If you want to configure additional parameters, see the [OpenCensus Envoy configuration page](https://www.envoyproxy.io/docs/envoy/v1.29.12/api-v3/config/trace/v3/opencensus.proto.html) and modify the tracing options in the Envoy bootstrap configuration.

After you issue a sample request to the demonstration server (`curl 10.10.10.10`), in the Google Cloud console, go to the Trace interface ([Trace > Trace list](https://console.cloud.google.com/traces/traces)). You see a trace record that corresponds to the request that you issued.

For more information about how to use Trace, see the [Cloud Trace documentation](https://docs.cloud.google.com/trace/docs/setup).

## Set up access log export to Logging

At this stage, Envoy should be recording access log information to the local disk of the VM where it is running. To [export these records to Logging](https://docs.cloud.google.com/logging/docs/export), you must install the Logging agent locally. This requires installing and configuring the Logging agent.

### Install the Logging agent

Install the Logging agent on the VM from which logging information is exported. For this example configuration, the VM is `td-observability-demo-vm`.
    
    
    curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.sh
    sudo bash add-logging-agent-repo.sh --also-install
    

For more information, see [Install the Cloud Logging agent on a single VM](https://docs.cloud.google.com/logging/docs/agent/logging/installation).

### Configure the Logging agent

You can export the Envoy logs as either unstructured or structured text.

#### Export the Envoy logs as unstructured text

This option exports log records from the access log to Cloud Logging as raw text. Each entry in the access log is exported as a single entry to Logging. This configuration is easier to install because it relies on a parser that is distributed with the current version of the Logging agent. However, it is more difficult to filter and process raw text log entries when using this option.

  1. Download and install the Envoy access log unstructured export configuration file:
         
         curl -sSO https://storage.googleapis.com/traffic-director/demo/observability/envoy_access_fluentd_unstructured.conf
         sudo cp envoy_access_fluentd_unstructured.conf /etc/google-fluentd/config.d/envoy_access.conf
         

  2. Restart the agent; the changes take effect when the agent starts up:
         
         sudo service google-fluentd restart
         




#### Export the Envoy logs as structured text

  1. [Install the Envoy access log parser](https://github.com/salrashid123/fluent-plugin-envoy-parser) from GitHub:
         
         sudo /opt/google-fluentd/embedded/bin/gem install fluent-plugin-envoy-parser
         

  2. Download and install the configuration file for exporting Envoy access logs in a structured format:
         
         curl -sSO https://storage.googleapis.com/traffic-director/demo/observability/envoy_access_fluentd_structured.conf
         sudo cp envoy_access_fluentd_structured.conf /etc/google-fluentd/config.d/envoy_access.conf
         

  3. Restart the agent; the changes take effect when the agent starts up:
         
         sudo service google-fluentd restart
         




For more information, see [Configure the Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/configuration).

### Verify the configuration

  1. From the sidecar proxy VM, generate a request to the demonstration service. This creates a new local log record. For example, you can run `curl 10.10.10.10`.
  2. In the Google Cloud console, go to [Logging > Logs Explorer](https://console.cloud.google.com/logs/query). In the drop-down menu, select the **envoy-access** log type. You see a log entry for the most recent request in the unstructured or structured format, depending on the configuration type that you chose earlier.



## Troubleshooting

Read the following sections for information about how to troubleshoot different issues with observability with Envoy.

### Configure tracing across multiple projects

If you would like to trace requests across Envoys deployed in multiple projects, note the following:

  * Each Envoy must be configured with the credentials of the project where it is running.
  * Each Envoy sends trace data to the project that corresponds to the credentials it is running with.
  * You can see tracing spans for cross-project requests if your applications preserve the value of the `X-Cloud-Trace-Context` HTTP header when requests are made.



### Trace compatibility with proxyless gRPC applications

Envoy's OpenCensus tracer configuration allows traces exported from proxyless gRPC applications and Envoy proxies to be fully compatible within a service mesh. For compatibility, the Envoy bootstrap must configure the trace context to include the `GRPC_TRACE_BIN` trace format in its `OpenCensusConfig`, as follows:
    
    
    tracing:
      http:
          name: envoy.tracers.opencensus
          typed_config:
            "@type": type.googleapis.com/envoy.config.trace.v2.OpenCensusConfig
            stackdriver_exporter_enabled: "true"
            stackdriver_project_id: "PROJECT_ID"
            incoming_trace_context: ["CLOUD_TRACE_CONTEXT", "GRPC_TRACE_BIN"]
            outgoing_trace_context: ["CLOUD_TRACE_CONTEXT", "GRPC_TRACE_BIN"]
    

If configuration is complete, but you don't see trace or logging entries available, verify the following:

  1. The service accounts for the Compute Engine VM have the necessary Trace and Logging IAM permissions, as specified in the prerequisites. For information about Trace IAM permissions, see [Access control](https://docs.cloud.google.com/trace/docs/iam). For information about Logging permissions, see [Access control](https://docs.cloud.google.com/logging/docs/access-control).
  2. For logging: Ensure that there are no errors in `/var/log/google-fluentd/google-fluentd.log`.
  3. For logging: Ensure that new entries appear in the local access log file when requests are issued.



## What's next

  * To find related information, see [Observability with proxyless gRPC applications](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability-proxyless).
  * To find general Cloud Service Mesh troubleshooting information, see [Troubleshooting deployments that use Envoy](https://docs.cloud.google.com/service-mesh/v1.25/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
