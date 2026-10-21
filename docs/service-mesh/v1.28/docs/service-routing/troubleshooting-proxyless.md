---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/troubleshooting-proxyless/
title: Troubleshoot proxyless gRPC deployments \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:06.426012+00:00
---

# Troubleshoot proxyless gRPC deployments  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/troubleshooting-proxyless/

You are viewing v1.28 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot proxyless gRPC deployments

This document provides information to help you resolve configuration issues when you deploy proxyless gRPC services with Cloud Service Mesh. For information about how to use the Client Status Discovery Service (CSDS) API to help you investigate issues with Cloud Service Mesh, see [Understanding Cloud Service Mesh client status](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/client-status).

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview).

## Troubleshooting RPC failures in a gRPC application

There are two common ways to troubleshoot remote procedure call (RPC) failures in a gRPC application:

  1. **Review the status returned when an RPC fails.** Usually, the status contains enough information to help you understand the cause of an RPC failure.

     * Status error handling in gRPC is explained in the [gRPC error handling documentation](https://grpc.io/docs/guides/error/).

     * [Example status error handling in gRPC-Java](https://github.com/saturnism/grpc-by-example-java/tree/master/error-handling-example). An exception might have other exceptions as its cause, which might provide additional information.

     * [Example status error handling in gRPC-Go](https://jbrandhorst.com/post/grpc-errors/).

  2. **Enable logging in gRPC runtime.** Sometimes you need to review the gRPC runtime logs to understand a failure that might not get propagated back to an RPC return status. For example, when an RPC fails with a status indicating that the deadline has been exceeded, the logs can help you to understand the underlying failure that caused the deadline to be exceeded.

Different language implementations of gRPC have different ways to enable logging in the gRPC runtime:

     * **gRPC in Java:** gRPC uses `java.util.logging` for logging. Set `io.grpc.level` to the `FINE` level to enable sufficient verbose logging in gRPC runtime. A typical way to enable logging in Java is to load the logging config from a file and provide the file location to JVM by using a command-line flag. For example:
           
           # Create a file called logging.properties with the following contents:
           handlers=java.util.logging.ConsoleHandler
           io.grpc.level=FINE
           io.grpc.xds.level=FINEST
           java.util.logging.ConsoleHandler.level=ALL
           java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter
           
           # Pass the location of the file to JVM by using this command-line flag:
           -Djava.util.logging.config.file=logging.properties
           

To enable logging specific to xDS modules, set `io.grpc.xds.level` to `FINE`. To see more detailed logging, set the level to `FINER` or `FINEST`.

     * **gRPC in Go:** Turn on logging by [setting environment variables](https://github.com/grpc/grpc-go/blob/master/README.md#how-to-turn-on-logging).
           
           GRPC_GO_LOG_VERBOSITY_LEVEL=99 GRPC_GO_LOG_SEVERITY_LEVEL=info
           

     * **gRPC in C++:** To enable logging with gRPC in C++, see the instructions in [Troubleshooting gRPC](https://github.com/grpc/grpc/blob/master/TROUBLESHOOTING.md). To enable logging specific to xDS modules, enable the following tracers by using the `GRPC_TRACE` [environment variable](https://github.com/grpc/grpc/blob/master/doc/environment_variables.md) for `xds_client`, `xds_resolver`, `cds_lb`, `eds_lb`, `priority_lb`, `weighted_target_lb`, and `lrs_lb`.

     * **gRPC in Node.js:** To enable logging with gRPC in Node.js, see the instructions in [Troubleshooting gRPC-JS](https://github.com/grpc/grpc-node/blob/master/TROUBLESHOOTING.md). To enable logging specific to xDS modules, enable the following tracers by using the `GRPC_TRACE` [environment variable](https://github.com/grpc/grpc-node/blob/master/doc/environment_variables.md) for `xds_client`, `xds_resolver`, `cds_balancer`, `eds_balancer`, `priority`, and `weighted_target`.




Depending on the error in the RPC status or in the runtime logs, your issue might fall in one of the following categories.

### Unable to connect to Cloud Service Mesh

To troubleshoot connection issues, try the following:

  * Check that the server_uri value in the bootstrap file is `trafficdirector.googleapis.com:443`.
  * Ensure that the environment variable `GRPC_XDS_BOOTSTRAP` is defined and pointing to the bootstrap file.
  * Ensure that you are using `xds` scheme in the URI when you create a gRPC channel.
  * Make sure that you granted the [required IAM permissions](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/prepare-service-routing-envoy-proxyless#grant-permissions) for creating compute instances and modifying a network in a project.
  * Make sure that you [Enable the service account to access the Traffic Director API](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/prepare-service-routing-envoy-proxyless#enable-service-account). Under the [Google Cloud console APIs & services](https://console.cloud.google.com/project/_/apis/library) for your project, look for errors in the Traffic Director API.
  * Confirm that the [service account has the correct permissions](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/prepare-for-envoy-setup#enable-service-account). The gRPC applications running in the VM or the Pod use the service account of the Compute Engine VM host or the Google Kubernetes Engine (GKE) node instance.
  * Confirm that the API access scope of the Compute Engine VMs or GKE clusters is set to allow full access to the Compute Engine APIs. Do this by specifying the following when you create the VMs or cluster:
        
        --scopes=https://www.googleapis.com/auth/cloud-platform
        

  * Confirm that you can access `trafficdirector.googleapis.com:443` from the VM. If there are access issues, the possible reasons include a firewall preventing access to `trafficdirector.googleapis.com` over TCP port `443` or DNS resolution issues for the `trafficdirector.googleapis.com` hostname.




### Hostname specified in the URI cannot be resolved

You might encounter an error message like the following one in your logs:
    
    
    [Channel<1>: (xds:///my-service:12400)] Failed to resolve name. status=Status{code=UNAVAILABLE, description=NameResolver returned no usable address. addrs=[], attrs={}
    

To troubleshoot hostname resolution issues, try the following:

  * Ensure that you are using a [supported gRPC version and language](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/prepare-service-routing-envoy-proxyless#supported-grpc-versions-languages).
  * Ensure that the port used in the URI to create a gRPC channel matches the port value in the forwarding rule used in your configuration. If a port is not specified in the URI, then the value `80` is used to match a forwarding rule.
  * Ensure that the hostname and port used in the URI to create a gRPC channel exactly matches a host rule in the URL map used in your configuration.
  * Ensure that the same host rule is not configured in more than one URL map.
  * Ensure that no wildcards are in use. Host rules containing a `*` wildcard character are ignored.



### RPC fails because the service isn't available

To troubleshoot RPC failures when a service isn't available, try the following:

  * Check the overall status of Cloud Service Mesh and the status of your backend services in the [Google Cloud console](https://console.cloud.google.com/net-services/trafficdirector/):

    * In the **Associated routing rule maps** column, ensure that the correct URL maps reference the backend services. Click the column to check that the backend services specified in the host matching rules are correct.
    * In the **Backends** column, check that the backends associated with your backend services are healthy.
    * If the backends are unhealthy, click the corresponding backend service and ensure that the correct health check is configured. Health checks commonly fail because of incorrect or missing firewall rules or a mismatch in the tags specified in the VM and in the firewall rules. For more information, see [Creating health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).
  * For gRPC health checks to work correctly, the gRPC backends must implement the [gRPC health checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). If this protocol is not implemented, use a TCP health check instead. Don't use an HTTP, HTTPS, or HTTP/2 health check with gRPC services.

  * When you use instance groups, ensure that the named port specified in the instance group matches the port used in the health check. When you use network endpoint groups (NEGs), ensure that the GKE service spec has the correct NEG annotation, and the health check is configured to use the NEG serving port.

  * Check that the endpoint protocol is configured as `GRPC`.




### RPC fails because the load balancing policy is not supported

You might encounter an error message like one of the following in your logs:
    
    
    error parsing "CDS" response: resource "cloud-internal-istio:cloud_mp_248715":
    unexpected lbPolicy RING_HASH in response
    
    
    
    error={"description":"errors parsing CDS response",
    "file":"external/com_github_grpc_grpc/src/core/ext/xds/xds_api.cc", "file_line":3304,
    "referenced_errors":[{"description":"cloud-internal-istio:cloud_mp_248715: LB policy is not supported."
    
    
    
    WARNING: RPC failed: Status{code=INTERNAL, description=Panic! This is a bug!, cause=java.lang.NullPointerException: provider
    at com.google.common.base.Preconditions.checkNotNull(Preconditions.java:910)
    at io.grpc.internal.ServiceConfigUtil$PolicySelection.<init>(ServiceConfigUtil.java:418)
    at io.grpc.xds.CdsLoadBalancer2$CdsLbState.handleClusterDiscovered(CdsLoadBalancer2.java:190)
    

This is because RING_HASH is not supported by the particular language and version of the client being used. To fix the problem, update the backend service configuration to use only supported load balancing policies, or upgrade the client to a supported version. For supported client versions, see [xDS features in gRPC](https://github.com/grpc/grpc/blob/master/doc/grpc_xds_features.md).

## Security configuration is not generated as expected

If you are configuring service security and the security configuration is not generated as expected, examine the endpoint policies in your deployment.

Cloud Service Mesh does not support scenarios where there are two or more endpoint policy resources that match equally to an endpoint, for example, two policies with the same labels and ports, or two or more policies with different labels that match equally with an endpoint's labels. For more information on how endpoint policys are matched to an endpoint's labels, see the [APIs for EndpointPolicy.EndpointMatcher.MetadataLabelMatcher](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#EndpointMatcher). In such situations, Cloud Service Mesh does not generate security configuration from any of the conflicting policies.

## Troubleshoot the health of your service mesh

This guide provides information to help you resolve Cloud Service Mesh configuration issues.

### Cloud Service Mesh behavior when most endpoints are unhealthy

For better reliability, when 99% of endpoints are unhealthy, Cloud Service Mesh configures the data plane to disregard the health status of the endpoints. Instead, the data plane balances traffic among all of the endpoints because it is possible that the serving port is still functional.

### Unhealthy backends cause suboptimal distribution of traffic

Cloud Service Mesh uses the information in the `HealthCheck` resource attached to a backend service to evaluate the health of your backends. Cloud Service Mesh uses this health status to route traffic to the closest healthy backend. If some of your backends are unhealthy, traffic might continue to be processed, but with suboptimal distribution. For example, traffic might flow to a region where healthy backends are still present, but which is much farther from the client, introducing latency. To identify and monitor the health status of your backends, try the following steps:

  * Check the health status of your backend service in the Google Cloud console.   
[Go to Cloud Service Mesh services](https://console.cloud.google.com/net-services/trafficdirector/services/list)
  * Make sure that [logging is enabled](https://docs.cloud.google.com/load-balancing/docs/health-check-logging) for the `HealthCheck` resource.
  * If the health checks started failing recently, inspect [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) to determine whether your `HealthCheck` configuration has changed recently.



## What's next

  * To learn how Cloud Service Mesh works, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/overview).
  * To learn how Cloud Service Mesh works with proxyless gRPC services, see the [Cloud Service Mesh with proxyless gRPC services overview](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/proxyless-overview).
  * To find general Cloud Service Mesh troubleshooting information, see [Troubleshooting deployments that use Envoy](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/troubleshooting).
  * To find additional support for using Cloud Service Mesh, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
