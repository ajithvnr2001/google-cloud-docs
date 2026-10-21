---
url: https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-resources/
title: Resolving resource limit issues in Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:47.087742+00:00
---

# Resolving resource limit issues in Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-resources/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving resource limit issues in Cloud Service Mesh

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/docs/getting-support).

Cloud Service Mesh resource limit problems can be caused by any of the following:

  * `LimitRange` objects created in the `istio-system` namespace or any namespace with automatic sidecar injection enabled.
  * User-defined limits that are set too low.
  * Nodes run out of memory or other resources.



Potential symptoms of resource problems:

  * Cloud Service Mesh repeatedly not receiving configuration from the control plane indicated by the error, `Envoy proxy NOT ready`. Seeing this error a few times at startup is normal, but otherwise it is a concern.
  * Networking problems with some pods or nodes that become unreachable.
  * `istioctl proxy-status` showing `STALE` statuses in the output.
  * `OOMKilled` messages in the logs of a node.
  * Memory usage by containers: `kubectl top pod POD_NAME --containers`.
  * Memory usage by pods inside a node: `kubectl top node my-node`.
  * Envoy out of memory: `kubectl get pods` shows status `OOMKilled` in the output.



## Sidecars take a long time to receive configuration

Slow configuration propagation can occur due to insufficient resources allocated to `istiod` or an excessively large cluster size.

There are several possible solutions to this problem:

  1. For in-cluster Cloud Service Mesh, if your monitoring tools (prometheus, stackdriver, etc.) show high utilization of a resource by `istiod`, increase the allocation of that resource, for example increase the CPU or memory limit of the `istiod` deployment. This is a temporary solution and we recommended that you investigate methods for reducing resource consumption.

  2. If you encounter this issue in a large cluster or deployment, reduce the amount of configuration state pushed to each proxy by configuring [Sidecar resources](https://istio.io/v1.31/docs/reference/config/networking/sidecar/).

  3. For in-cluster Cloud Service Mesh, if the problem persists, try horizontally scaling `istiod`.

  4. If all other troubleshooting steps fail to resolve the problem, report a bug detailing your deployment and the observed problems. Follow [these steps](https://github.com/istio/istio/wiki/Analyzing-Istio-Performance) to include a CPU/Memory profile in the bug report if possible, along with a detailed description of cluster size, number of pods, and number of services.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
