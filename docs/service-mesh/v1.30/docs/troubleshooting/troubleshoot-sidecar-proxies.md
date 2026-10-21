---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-sidecar-proxies/
title: Resolving sidecar proxies issues in Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:25:34.640846+00:00
---

# Resolving sidecar proxies issues in Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-sidecar-proxies/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving sidecar proxies issues in Cloud Service Mesh

This section explains common Cloud Service Mesh sidecar proxies problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.30/docs/getting-support).

## The `istio-proxy` container is killed because of a OOM event

In this section we assume that the `istio-proxy` container is not killed by a `SystemOOM` event, and the kubernetes node is not in `MemoryPressure` condition. The `istio-proxy` sidecar container has by default [resource limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits). If the istio-proxy container gets killed with `Reason: OOMKilled` it is necessary to understand why Envoy is consuming the memory.

If you are facing a production outage, a quick workaround is to raise the limits for all containers using `IstioOperator`:
    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      values:
        global:
          proxy:
            resources:
              requests:
                   memory: 128Mi
              limits:
                   memory: 1Gi
    

If you are facing this issue with specific workloads, you can change the limit just on those workloads by adding the following [annotations](https://istio.io/v1.30/docs/reference/config/annotations/).

  * `sidecar.istio.io/proxyMemory`
  * `sidecar.istio.io/proxyMemoryLimit`



Please make sure you don't have limits that are lower of the default values.

**Note:** because this container is injected at the Pod creation, this setting will be effective only for newly created Pods.

The long term solution is to reduce the memory footprint of your `istio-proxy` sidecar containers. By default all sidecar proxies are programmed with the necessary configuration to reach any other workload instance in the mesh. Istio provides the [custom resource definition `Sidecar`](https://istio.io/v1.30/docs/reference/config/networking/sidecar/) to limit the number of endpoints programmed to sidecar proxies, and therefore reduce the memory consumption of the `istio-proxy` container.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
