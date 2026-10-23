---
url: https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-intro/
title: Troubleshoot Cloud Service Mesh step-by-step \u00a0|\u00a0 Cloud Service Mesh v1.20 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:55.029816+00:00
---

# Troubleshoot Cloud Service Mesh step-by-step  |  Cloud Service Mesh v1.20  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-intro/

You are viewing archived v1.20 Service Mesh documentation.

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
  * [ v1.20 ](https://docs.cloud.google.com/service-mesh/v1.20/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.20/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Cloud Service Mesh step-by-step

This section explains how to troubleshoot and resolve problems when using Cloud Service Mesh. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.20/docs/getting-support).

## Troubleshooting steps

Follow these general steps to troubleshoot Cloud Service Mesh:

  1. Use the automated configuration validation tools.
  2. Check if you have a common problem with a known solution.
  3. Narrow the scope of the problem.
  4. Review relevant logs and information.
  5. Gather diagnostic logs and seek help.

**Note:** If you are unable to troubleshoot manually, see [Gather diagnostic logs and seek help](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-collect-logs) for next steps.

## Use automated validation tools

Cloud Service Mesh includes automated diagnostic and configuration validation tools that can resolve problems and help you avoid them in the future. The following sections explain how to use these tools.

### `istioctl analyze`

The `istioctl analyze` diagnostic tool can detect common configuration problems. Install `istioctl` using these [instructions](https://docs.cloud.google.com/service-mesh/v1.20/docs/downloading-istioctl).

`istioctl analyze` reads a cluster configuration and if it finds a problem, provides informational messages and suggests remedies. It can run against a live cluster or a set of local configuration files. It can also run against a combination of the two, allowing you to find problems before you apply changes to a cluster. For more information, see [Diagnose your Configuration with `istioctl analyze`](https://istio.io/latest/docs/ops/diagnostic-tools/istioctl-analyze). For more information about the errors that `istioctl analyze` detects, see [Configuration Analysis Messages](https://istio.io/latest/docs/reference/config/analysis/).

#### Analyze a live cluster

Analyze a live cluster by using the following command.
    
    
    istioctl analyze -A

If `istioctl analyze` detects a problem with your configuration, it will display a message with helpful information to resolve it, if known. For example, if you made the common mistake to not label your namespace correctly to enable Istio sidecar injection, it would generate the following message:
    
    
    Warn [IST0102] (Namespace default) The namespace is not enabled for Istio injection.
    Run 'kubectl label namespace default istio-injection=enabled' to enable it,
    or 'kubectl label namespace default istio-injection=disabled'
    to explicitly mark it as not needing injection

If the problem persists, see the next section to check if your problem is already known.

## Check for common problems and solutions

You can save time by checking if your symptoms match an issue in these common problems and resolutions sections, grouped by Cloud Service Mesh functional area:

  * [Installation issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-installation)
  * [Managed control plane issues](https://docs.cloud.google.com/service-mesh/docs/managed/troubleshoot-managed-anthos-service-mesh)
  * [Observability issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-observability)
  * [Off-Google Cloud deployment issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-off-gcp)
  * [Proxy issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-proxy)
  * [Resource issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-resources)
  * [Scaling issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-scaling)
  * [Security issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-security)
  * [Traffic management issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-traffic)
  * [Webhook issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-webhook)
  * [Sidecar proxies issues](https://docs.cloud.google.com/service-mesh/v1.20/docs/troubleshooting/troubleshoot-sidecar-proxies)



If this does not resolve your issue, see the next section.

## Narrow the scope of the problem

Cloud Service Mesh consists of several technologies working together, which means that certain types of problems are associated with particular functional areas or components. Each of these components generate helpful logs of their own. Before you attempt to manually analyze the volume of information they provide, narrow the scope of your troubleshooting by answering the following questions:

  * Does the issue occur within the control plane or the data plane, for example `istiod` or Envoy proxies?
  * In which functional area are you experiencing the issue, for example Networking, Telemetry, Security, etc.?
  * Is there service-mesh wide traffic loss or in a specific deployment?
  * Does the problem appear or worsen due to lack of ability to scale traffic in service mesh?
  * Does the issue cause latency or other performance issues?
  * Can you reproduce the issue on demand?
  * Did the problem begin after a recent configuration change in Istio, GKE, etc.?
  * Is there an increase or spike in traffic within the service mesh?
  * Does this cluster have any noticeable features enabled or non-typical deployments?
  * Do you observe high CPU or memory utilization? If so, what is the expected usaged at scale?
  * Are there quota restrictions to consider?



### View control plane status

The following commands can help you understand the status of the Cloud Service Mesh control plane:

  * `kubectl get pods -n istio-system`
  * `kubectl describe -n istio-system`
  * For all pods in istio-system: `kubectl logs -n istio-system -l istio --all-containers`
  * `istioctl version`
  * `istioctl proxy-status`
  * `kubectl get configmap istio -o yaml && kubectl get configmap istio-sidecar-injector -o yaml`
  * `kubectl top pods -n istio-system`



Use the following commands to understand the scale of the deployment:

  * `kubectl get nodes`
  * `kubectl get services --all-namespaces`
  * `kubectl get pods --all-namespaces`



## Review relevant logs and information

After you narrow the scope of the problem, you can focus on certain logs and information more effectively. To learn about the logs that Cloud Service Mesh generates and how to interpret the information they contain, see [Interpreting Cloud Service Mesh logs](https://docs.cloud.google.com/service-mesh/v1.20/docs/observability/accessing-logs#interpret_anthos_service_mesh_logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
