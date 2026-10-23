---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/limitations/
title: Cloud Service Mesh limitations with Envoy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:43.905586+00:00
---

# Cloud Service Mesh limitations with Envoy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/limitations/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh limitations with Envoy

This document describes limitations that apply to Cloud Service Mesh with the Google Cloud APIs, including advanced traffic management limitations. It does not apply to Cloud Service Mesh with the Istio APIs.

For information about _limits_ , see [Quotas and limits](https://docs.cloud.google.com/service-mesh/quotas).

## General limitations

The limitations of Cloud Service Mesh include the following:

  * Cloud Service Mesh with the service routing APIs only supports Google Cloud APIs.
  * You can use Cloud Service Mesh to configure the following request protocols: HTTP (HTTP/1.1 or HTTP/2), HTTPS, TCP, and gRPC.
  * When you use Envoy as the dataplane proxy, the [`stream_idle_timeout` value](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto) defaults to 5 minutes. This is not configurable through Cloud Service Mesh.
  * When you use the `TCPRoute` resource to configure the TCP request protocol, you cannot use the [advanced traffic management features](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/advanced-traffic-management). Advanced traffic management is only available when you configure the data plane to handle HTTP or gRPC requests.
  * Cloud Service Mesh supports [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) with the [service routing APIs](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/service-routing-overview).
  * Cloud Service Mesh does not support server-first protocols.
  * You cannot use Cloud Service Mesh with services running in [Knative](https://docs.cloud.google.com/knative) or [Google Cloud Serverless Computing](https://docs.cloud.google.com/serverless).
  * This document discusses Envoy proxies, but you can use any [open standard API (xDS) proxy](https://www.envoyproxy.io/docs/envoy/latest/api/api) with Cloud Service Mesh. However, Google has tested Cloud Service Mesh only with the Envoy proxy.
  * To ensure that all known security vulnerabilities are mitigated, we recommend that you use the most recent Envoy version. For information about Envoy security advisories, see [Envoy Security Advisories](https://github.com/envoyproxy/envoy/security/advisories).
  * The Google Cloud console does not support hybrid connectivity network endpoint groups (NEGs). To create or delete hybrid connectivity NEGs, use the Google Cloud CLI.
  * Because your data plane handles health checks, you cannot use the Google Cloud console, API, or gcloud CLI to retrieve health check status.
  * Check `iptables` and ensure that it is set up correctly. For more information about how to configure `iptables`, see Envoy's notes about configuring [HTTP filtering](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/original_src_filter#extra-setup).

    * If you use the Google Cloud console to create virtual machine (VM) instances, some `ipv6`-related modules are not installed and available before a restart. As a result, `iptables.sh` fails due to missing dependencies. In such a case, restart the VM and rerun the `run.sh` script.
    * If you use the gcloud CLI to create Compute Engine VMs, you are not expected to have this problem.



## Advanced traffic management limitations

The limitations of advanced traffic management include the following:

  * If the value of `BackendService.sessionAffinity` is not NONE, and `BackendService.localityLbPolicy` is set to a load-balancing policy other than `MAGLEV` or `RING_HASH`, the session affinity settings don't take effect.
  * The `gcloud import` command doesn't delete top-level fields of the resource, such as the backend service and the URL map. For example, if a backend service is created with settings for `circuitBreakers`, you can use a subsequent `gcloud import` command to update those settings. However, you cannot delete those settings from the backend service. You can delete and recreate the resource itself without the `circuitBreakers` settings.



## Limitations with Service Directory

  * Service Directory and Cloud Service Mesh don't guarantee network reachability for clients.
  * A backend service can only reference one of the following:

    * Managed instance group or unmanaged instance group
    * Network endpoint group
    * Service bindings
  * Service Directory services can only be used with global backend services with `load-balancing-scheme=INTERNAL_SELF_MANAGED`.

  * A Service Directory service that is referenced by a service binding can be deleted. If the underlying Service Directory service to which the backend service is attached is deleted, applications that use Cloud Service Mesh cannot send traffic to this service, therefore, requests fail. See [Observability and debugging](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-directory-observability) for best practices.

  * When you bind a Service Directory service to a backend service, you cannot configure a health check on that backend service.




## What's next

  * To learn about limitations that apply to Cloud Service Mesh with proxyless gRPC applications, see [Proxyless gRPC limitations](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/limitations-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
