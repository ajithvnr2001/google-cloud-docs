---
url: https://docs.cloud.google.com/service-mesh/legacy/service-routing/observability-proxyless/
title: Observability with proxyless gRPC applications \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:00.109757+00:00
---

# Observability with proxyless gRPC applications  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/service-routing/observability-proxyless/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Observability with proxyless gRPC applications

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

[Microservices observability](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc) tools provide you with the ability to instrument your applications to collect and present telemetry data in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview), [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), and [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) from [gRPC](https://grpc.io/) workloads deployed on Google Cloud, including gRPC workloads in Cloud Service Mesh.

gRPC clients and servers are integrated with [OpenCensus](https://opencensus.io/guides/grpc/) to export metrics and traces to various backends, including Trace and Monitoring. You can do this with the following gRPC languages:

  * C++
  * Go
  * Java



Read the [Microservices observability overview](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc), then use the instructions in [Set up Microservices observability](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability) to instrument your gRPC workloads for the following:

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and viewing metrics.
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) and viewing logs.
  * [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) and viewing traces.



Use the instructions in this document for the following tasks:

  * Viewing traces.
  * Exposing the admin interface.
  * Using the `grpcdebug` tool and other tools to debug your applications.



## View traces on Trace

After you complete the [setup process](https://docs.cloud.google.com/service-mesh/legacy/service-routing/\(/stackdriver/docs/solutions/grpc/set-up-observability\)), your instrumented gRPC clients and servers send traces to Trace. The **Trace Overview** page in the Google Cloud console shows you a list of recent traces. You can select an individual trace to see a breakdown of your traffic, similar to what's described in the following section.

### Trace compatibility with the Envoy proxy

Exporting traces to Trace with Cloud Service Mesh and the Envoy proxy, as described in [Observability with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/observability-envoy), uses Envoy's OpenCensus tracer configuration, which allows traces exported from proxyless gRPC applications and Envoy proxies to be fully compatible within a service mesh. For compatibility with proxyless gRPC, the Envoy bootstrap needs to configure the trace context to include the `GRPC_TRACE_BIN` trace format in its `OpenCensusConfig`. For example:
    
    
    tracing:
      http:
          name: envoy.tracers.opencensus
          typed_config:
            "@type": type.googleapis.com/envoy.config.trace.v2.OpenCensusConfig
            stackdriver_exporter_enabled: "true"
            stackdriver_project_id: "PROJECT_ID"
            incoming_trace_context: ["CLOUD_TRACE_CONTEXT", "GRPC_TRACE_BIN"]
            outgoing_trace_context: ["CLOUD_TRACE_CONTEXT", "GRPC_TRACE_BIN"]
    

## Expose the admin interface

Sometimes, metrics and tracing data are not sufficient for resolving an issue. You might need to look at the configuration or the runtime state of the gRPC library in your application. This information includes resolver information, the state of connectivity to peers, RPC statistics on a channel, and the configuration received from Cloud Service Mesh.

To obtain such information, gRPC applications can expose the admin interface on a particular port. You can then query the application to understand how the services are configured and how they are running. In this section, you can find instructions about how to configure the admin interface for applications written in each supported language.

We recommend that you build a separate gRPC server in your application that listens on a port reserved for this purpose. This lets you access your gRPC applications even when the data ports are inaccessible because of misconfiguration or network issues. We recommend that you expose the admin interface only on `localhost` or on a Unix domain socket.

The following code snippets show how to create an admin interface.

###  C++ 

In C++, use this code to create an admin interface:
    
    
    #include <grpcpp/ext/admin_services.h>
    
    grpc::ServerBuilder builder;
    grpc::AddAdminServices(&builder);
    builder.AddListeningPort(":50051", grpc::ServerCredentials(...));
    std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
    

###  Go 

In Go, use this code to create an admin interface:
    
    
    import "google.golang.org/grpc/admin"
    
    lis, err := net.Listen("tcp", ":50051")
    if err != nil {
            log.Fatalf("failed to listen: %v", err)
    }
    defer lis.Close()
    grpcServer := grpc.NewServer(...opts)
    cleanup, err := admin.Register(grpcServer)
    if err != nil {
            log.Fatalf("failed to register admin services: %v", err)
    }
    defer cleanup()
    
    if err := grpcServer.Serve(lis); err != nil {
            log.Fatalf("failed to serve: %v", err)
    }
    

###  Java 

In Java, use this code to create an admin interface:
    
    
    import io.grpc.services.AdminInterface;
    
    server = ServerBuilder.forPort(50051)
            .useTransportSecurity(certChainFile, privateKeyFile)
            .addServices(AdminInterface.getStandardServices())
            .build()
            .start();
    server.awaitTermination();
    

###  Python 

In Python, use this code to create an admin interface:
    
    
    import grpc_admin
    
    server = grpc.server(futures.ThreadPoolExecutor())
    grpc_admin.add_admin_servicers(server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    

### Use SSH to connect to a VM

The [gRPC Wallet](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples) example already enables the admin interface. You can change the admin interface port by providing the following flag:
    
    
     --admin-port=PORT
    

The default admin port is `localhost:28881`.

To debug your gRPC application, you can use SSH to connect to one of the VMs that serves the `wallet-service`. This gives you access to the `localhost`.
    
    
    # List the Wallet VMs
    $ gcloud compute instances list --filter="zone:(us-central1-a)" --filter="name~'grpcwallet-wallet-v2'"
    NAME                                       ZONE            MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP    EXTERNAL_IP     STATUS
    grpcwallet-wallet-v2-mig-us-central1-ccl1  us-central1-a   n1-standard-1               10.240.0.38    35.223.42.98    RUNNING
    grpcwallet-wallet-v2-mig-us-central1-k623  us-central1-a   n1-standard-1               10.240.0.112   35.188.133.75   RUNNING
    # Pick one of the Wallet VMs to debug
    $ gcloud compute ssh grpcwallet-wallet-v2-mig-us-central1-ccl1 --zone=us-central1-a
    

## Install the `grpcdebug` tool

To access the admin interface, you need a gRPC client that can communicate with the admin services in your gRPC application. In the following examples, you use a tool called `grpcdebug` that you can download and install on the VM or Pod where your gRPC application is running. The repository for `grpcdebug` is located at [grpc-ecosystem/grpcdebug](https://github.com/grpc-ecosystem/grpcdebug).

The minimum support Golang version is 1.12. The official Golang installation guide is at the [Golang site](https://golang.org/doc/install). If you are following the guide to create a Linux VM for the `wallet-service`, you can install Golang 1.16 by using these commands:
    
    
    sudo apt update && sudo apt install -y wget
    wget https://golang.org/dl/go1.16.3.linux-amd64.tar.gz
    sudo rm -rf /usr/local/go
    sudo tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz
    export PATH=$PATH:/usr/local/go/bin
    sudo ln -sf /usr/local/go/bin/go /usr/bin/go
    go version
    # go version go1.16.3 linux/amd64
    

You install the `grpcdebug` tool with the following commands:
    
    
    go install -v github.com/grpc-ecosystem/grpcdebug@latest
    export PATH=$PATH:$(go env GOPATH)/bin
    

You now have access to the `grpcdebug` command-line interface. The help output contains information about supported commands:
    
    
    $ grpcdebug -h
    grpcdebug is a gRPC service admin command-line interface
    
    Usage:
      grpcdebug <target address> [flags]  <command>
    
    Available Commands:
      channelz    Display gRPC states in human readable way.
      health      Check health status of the target service (default "").
      help        Help about any command
      xds         Fetch xDS related information.
    
    Flags:
          --credential_file string        Sets the path of the credential file; used in [tls] mode
      -h, --help                          Help for grpcdebug
          --security string               Defines the type of credentials to use [tls, google-default, insecure] (default "insecure")
          --server_name_override string   Overrides the peer server name if non empty; used in [tls] mode
      -t, --timestamp                     Print timestamp as RFC 3339 instead of human readable strings
      -v, --verbose                       Print verbose information for debugging
    

To obtain more information about a particular command, use the following:
    
    
     grpcdebug <target address> [command] --help
    

## Use the `grpcdebug` tool to debug your applications

You can use the `grpcdebug` tool to debug your applications. The `grpcdebug` tool provides an `ssh_config`-like configuration that supports aliasing, hostname rewriting, and connection security setting (insecure/TLS). For more information about this advanced feature, see [`grpcdebug/Connect&Security`](https://github.com/grpc-ecosystem/grpcdebug#connect--security).

The following sections describe the services exposed by the admin interface and how to access them.

### Use Channelz

The [Channelz](https://github.com/grpc/grpc/blob/master/src/proto/grpc/channelz/channelz.proto) service provides access to runtime information about the connections at different levels in the gRPC library of your application. You can use this for live analysis of applications that might have configuration- or network-related issues. The following examples assume that you deployed the gRPC Wallet example by using the instructions in [Configure advanced traffic management with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management) and that you provided the following flag:
    
    
     --admin-port=PORT
    

After you send some RPCs from a test client, as shown in [Verifying the configuration](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#verify-configuration), use the following commands to access the Channelz data for gRPC services:

  1. Use SSH to connect to a VM that is running the `wallet-service`.
  2. Set up `grpcdebug` to connect to the running gRPC application.



The default output of `grpcdebug` is in a console-friendly table format. If you supply the `--json` flag, the output is encoded as `JSON`.

The `grpcdebug channelz` command is used to fetch and present debugging information from the Channelz service. The command works for both gRPC clients and gRPC servers.

For gRPC clients, the command `grpcdebug channelz channels` provides a list of existing channels and some basic information:
    
    
    $ grpcdebug localhost:28881 channelz channels
    Channel ID   Target                               State     Calls(Started/Succeeded/Failed)   Created Time
    1            xds:///account.grpcwallet.io:10080   READY     0/0/0                             59 seconds ago
    2            trafficdirector.googleapis.com:443   READY     2/0/0                             59 seconds ago
    4            xds:///stats.grpcwallet.io:10080     READY     0/0/0                             59 seconds ago
    

If you need additional information about a particular channel, you can use `grpcdebug channelz channel [CHANNEL_ID]` to inspect detailed information for that channel. The channel identifier can be the channel ID or the target address, if there is only one target address. A gRPC channel can contain multiple subchannels, which is gRPC's abstraction on top of a TCP connection.
    
    
    $ grpcdebug localhost:28881 channelz channel 2
    Channel ID:        2
    Target:            trafficdirector.googleapis.com:443
    State:             READY
    Calls Started:     2
    Calls Succeeded:   0
    Calls Failed:      0
    Created Time:      10 minutes ago
    ---
    Subchannel ID   Target                               State     Calls(Started/Succeeded/Failed)   CreatedTime
    3               trafficdirector.googleapis.com:443   READY     2/0/0                             10 minutes ago
    ---
    Severity   Time             Child Ref                      Description
    CT_INFO    10 minutes ago                                  Channel Created
    CT_INFO    10 minutes ago                                  parsed scheme: ""
    CT_INFO    10 minutes ago                                  scheme "" not registered, fallback to default scheme
    CT_INFO    10 minutes ago                                  ccResolverWrapper: sending update to cc: {[{trafficdirector.googleapis.com:443  <nil> 0 <nil>}] <nil> <nil>}
    CT_INFO    10 minutes ago                                  Resolver state updated: {Addresses:[{Addr:trafficdirector.googleapis.com:443 ServerName: Attributes:<nil> Type:0 Metadata:<nil>}] ServiceConfig:<nil> Attributes:<nil>} (resolver returned new addresses)
    CT_INFO    10 minutes ago                                  ClientConn switching balancer to "pick_first"
    CT_INFO    10 minutes ago                                  Channel switches to new LB policy "pick_first"
    CT_INFO    10 minutes ago   subchannel(subchannel_id:3 )   Subchannel(id:3) created
    CT_INFO    10 minutes ago                                  Channel Connectivity change to CONNECTING
    CT_INFO    10 minutes ago                                  Channel Connectivity change to READY
    

You can also inspect detailed information for a subchannel:
    
    
    $ grpcdebug localhost:28881 channelz subchannel 3
    Subchannel ID:     3
    Target:            trafficdirector.googleapis.com:443
    State:             READY
    Calls Started:     2
    Calls Succeeded:   0
    Calls Failed:      0
    Created Time:      12 minutes ago
    ---
    Socket ID   Local->Remote                           Streams(Started/Succeeded/Failed)   Messages(Sent/Received)
    9           10.240.0.38:60338->142.250.125.95:443   2/0/0                               214/132
    

You can retrieve information about TCP sockets:
    
    
    $ grpcdebug localhost:28881 channelz socket 9
    Socket ID:                       9
    Address:                         10.240.0.38:60338->142.250.125.95:443
    Streams Started:                 2
    Streams Succeeded:               0
    Streams Failed:                  0
    Messages Sent:                   226
    Messages Received:               141
    Keep Alives Sent:                0
    Last Local Stream Created:       12 minutes ago
    Last Remote Stream Created:      a long while ago
    Last Message Sent Created:       8 seconds ago
    Last Message Received Created:   8 seconds ago
    Local Flow Control Window:       65535
    Remote Flow Control Window:      966515
    ---
    Socket Options Name   Value
    SO_LINGER             [type.googleapis.com/grpc.channelz.v1.SocketOptionLinger]:{duration:{}}
    SO_RCVTIMEO           [type.googleapis.com/grpc.channelz.v1.SocketOptionTimeout]:{duration:{}}
    SO_SNDTIMEO           [type.googleapis.com/grpc.channelz.v1.SocketOptionTimeout]:{duration:{}}
    TCP_INFO              [type.googleapis.com/grpc.channelz.v1.SocketOptionTcpInfo]:{tcpi_state:1  tcpi_options:7  tcpi_rto:204000  tcpi_ato:40000  tcpi_snd_mss:1408  tcpi_rcv_mss:1408  tcpi_last_data_sent:8212  tcpi_last_data_recv:8212  tcpi_last_ack_recv:8212  tcpi_pmtu:1460  tcpi_rcv_ssthresh:88288  tcpi_rtt:2400  tcpi_rttvar:3012  tcpi_snd_ssthresh:2147483647  tcpi_snd_cwnd:10  tcpi_advmss:1408  tcpi_reordering:3}
    ---
    Security Model:   TLS
    Standard Name:    TLS_AES_128_GCM_SHA256
    

On the server side, you can use Channelz to inspect your server application's status. For example, you can get the list of servers by using the `grpcdebug channelz servers` command:
    
    
    $ grpcdebug localhost:28881 channelz servers
    Server ID   Listen Addresses    Calls(Started/Succeeded/Failed)   Last Call Started
    5           [127.0.0.1:28881]   9/8/0                             now
    6           [[::]:50051]        159/159/0                         4 seconds ago
    

To obtain more information about a specific server, use the `grpcdebug channelz server` command. You can inspect server sockets the same way that you inspect client sockets.
    
    
    $ grpcdebug localhost:28881 channelz server 6
    Server Id:           6
    Listen Addresses:    [[::]:50051]
    Calls Started:       174
    Calls Succeeded:     174
    Calls Failed:        0
    Last Call Started:   now
    ---
    Socket ID   Local->Remote                            Streams(Started/Succeeded/Failed)   Messages(Sent/Received)
    25          10.240.0.38:50051->130.211.1.39:44904    68/68/0                             68/68
    26          10.240.0.38:50051->130.211.0.167:32768   54/54/0                             54/54
    27          10.240.0.38:50051->130.211.0.22:32768    52/52/0                             52/52
    

### Use the Client Status Discovery Service

The [Client Status Discovery Service](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/status/v3/csds.proto) (CSDS) API is part of the [xDS APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/xds-control-plane-apis). In a gRPC application, the CSDS service provides access to the configuration (also called the xDS configuration) that it receives from Cloud Service Mesh. This lets you identify and resolve configuration-related issues in your mesh.

The following examples assume that you deployed the gRPC Wallet example by using the instructions in [Configure advanced traffic management with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management).

To use CSDS to examine the configuration:

  1. Use SSH to connect to a VM that is running the `wallet-service`. Use the instructions in Use SSH to connect to a VM.
  2. Run the `grpcdebug` client.



To get an overview of configuration status, run the following command:
    
    
    grpcdebug localhost:28881 xds status
    

You see results similar to the following:
    
    
    Name                                                                    Status    Version               Type                                                                 LastUpdated
    account.grpcwallet.io:10080                                             ACKED     1618529574783547920   type.googleapis.com/envoy.config.listener.v3.Listener                3 seconds ago
    stats.grpcwallet.io:10080                                               ACKED     1618529574783547920   type.googleapis.com/envoy.config.listener.v3.Listener                3 seconds ago
    URL_MAP/830293263384_grpcwallet-url-map_0_account.grpcwallet.io:10080   ACKED     1618529574783547920   type.googleapis.com/envoy.config.route.v3.RouteConfiguration         3 seconds ago
    URL_MAP/830293263384_grpcwallet-url-map_1_stats.grpcwallet.io:10080     ACKED     1618529574783547920   type.googleapis.com/envoy.config.route.v3.RouteConfiguration         3 seconds ago
    cloud-internal-istio:cloud_mp_830293263384_3566964729007423588          ACKED     1618529574783547920   type.googleapis.com/envoy.config.cluster.v3.Cluster                  3 seconds ago
    cloud-internal-istio:cloud_mp_830293263384_7383783194368524341          ACKED     1618529574783547920   type.googleapis.com/envoy.config.cluster.v3.Cluster                  3 seconds ago
    cloud-internal-istio:cloud_mp_830293263384_3363366193797120473          ACKED     1618529574783547920   type.googleapis.com/envoy.config.cluster.v3.Cluster                  3 seconds ago
    cloud-internal-istio:cloud_mp_830293263384_3566964729007423588          ACKED     86                    type.googleapis.com/envoy.config.endpoint.v3.ClusterLoadAssignment   2 seconds ago
    cloud-internal-istio:cloud_mp_830293263384_3363366193797120473          ACKED     86                    type.googleapis.com/envoy.config.endpoint.v3.ClusterLoadAssignment   2 seconds ago
    cloud-internal-istio:cloud_mp_830293263384_7383783194368524341          ACKED     86                    type.googleapis.com/envoy.config.endpoint.v3.ClusterLoadAssignment   2 seconds ago
    

You can find the definition of configuration status in [documentation for the Envoy proxy](https://github.com/envoyproxy/envoy/blob/7d36ea50b696de4ae2d8269a94cab78d3058d4db/api/envoy/admin/v3/config_dump.proto#L22). Briefly, the status of an xDS resource is one of `REQUESTED`, `DOES_NOT_EXIST`, `ACKED`, or `NACKED`.

To obtain a raw xDS configuration dump, run the following command:
    
    
    grpcdebug localhost:28881 xds config
    

You see a `JSON` list of the [`PerXdsConfig`](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/status/v3/csds.proto.html?highlight=csds#service-status-v3-perxdsconfig) object:
    
    
    {
      "config":  [
        {
          "node":  {
            "id":  "projects/830293263384/networks/default/nodes/6e98b038-6d75-4a4c-8d35-b0c7a8c9cdde",
            "cluster":  "cluster",
            "metadata":  {
              "INSTANCE_IP":  "10.240.0.38",
              "TRAFFICDIRECTOR_GCP_PROJECT_NUMBER":  "830293263384",
              "TRAFFICDIRECTOR_NETWORK_NAME":  "default"
            },
            "locality":  {
              "zone":  "us-central1-a"
            },
            "userAgentName":  "gRPC Go",
            "userAgentVersion":  "1.37.0",
            "clientFeatures":  [
              "envoy.lb.does_not_support_overprovisioning"
            ]
          },
          "xdsConfig":  [
            {
              "listenerConfig":  {
                "versionInfo":  "1618529930989701137",
                "dynamicListeners":  [
                  {
    ...
    
    

If the raw configuration output is too verbose, `grpcdebug` lets you filter based on specific xDS types. For example:
    
    
    $ grpcdebug localhost:28881 xds config --type=cds
    {
      "versionInfo":  "1618530076226619310",
      "dynamicActiveClusters":  [
        {
          "versionInfo":  "1618530076226619310",
          "cluster":  {
            "@type":  "type.googleapis.com/envoy.config.cluster.v3.Cluster",
            "name":  "cloud-internal-istio:cloud_mp_830293263384_7383783194368524341",
            "altStatName":  "/projects/830293263384/global/backendServices/grpcwallet-stats-service",
            "type":  "EDS",
            "edsClusterConfig":  {
              "edsConfig":  {
                "ads":  {},
                "initialFetchTimeout":  "15s",
    ...
    

You can also dump the configuration of seberal xDS types at the same time:
    
    
    $ grpcdebug localhost:28881 xds config --type=lds,eds
    {
      "versionInfo":  "1618530076226619310",
      "dynamicListeners":  [...]
    }
    {
      "dynamicEndpointConfigs":  [...]
    }
    

## What's next

  * To find related information, see [Observability with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/observability-envoy).
  * To resolve configuration issues when you deploy proxyless gRPC services, see [Troubleshooting deployments that use proxyless gRPC](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
