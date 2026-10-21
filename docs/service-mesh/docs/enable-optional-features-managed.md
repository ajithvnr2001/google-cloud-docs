---
url: https://docs.cloud.google.com/service-mesh/docs/enable-optional-features-managed/
title: Enable optional features on managed control plane \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:23.927416+00:00
---

# Enable optional features on managed control plane  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/enable-optional-features-managed/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable optional features on managed control plane

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Managed Cloud Service Mesh lets you enable optional mesh features by customizing `ConfigMap` resources in your cluster. You can configure security hardening such as distroless proxy images, restrict external egress with outbound traffic policies, and customize trace sampling while Google manages control plane maintenance and upgrades.

**Caution:** If your cluster uses the `TRAFFIC_DIRECTOR` implementation, apply customizations to the `istio-asm-managed-rapid` configmap regardless of your configured release channel.

Feature availability varies by control plane implementation and release channel. For more information, see [Supported features using Istio APIs (managed control plane)](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp) and [Enable optional features on an in-cluster control plane](https://docs.cloud.google.com/service-mesh/docs/unified-install/options/enable-optional-features).

## Distroless proxy image

  * **Directly onboarded clusters** (clusters directly onboarded to the managed `TRAFFIC_DIRECTOR` [control plane](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed#identify_control_plane_implementation)): Only the `distroless` image type is supported. You cannot change this. The `default` image is not supported.

  * **Migrated clusters** (clusters migrated from the `ISTIOD` to `TRAFFIC_DIRECTOR` control plane): The image type defaults to the `default` image (which contains debug binaries). You can explicitly opt-in to `distroless` images yourself to improve security.




Distroless is the recommended image type for improved security. As a best practice, you should restrict the contents of a container runtime to only the necessary packages. This approach improves security and the signal-to-noise ratio of Common Vulnerabilities and Exposures (CVE) scanners. Istio provides proxy images based on [distroless base images](https://github.com/GoogleContainerTools/distroless).

The distroless proxy image does not contain any binaries other than the proxy. It is therefore not possible to `exec` a shell or use `curl`, `ping`, or other debug utilities inside the container. However, you can use ephemeral containers to attach to a running workload Pod to be able to inspect it and run custom commands. For example, see [Collecting Cloud Service Mesh logs](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-collect-logs#configure_envoy_proxy).

The following configuration enables distroless images for the entire Cloud Service Mesh. An image type change requires each pod to restart and get re-injected to take effect.
    
    
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: istio-release-channel
           namespace: istio-system
         data:
           mesh: |-
             defaultConfig:
               image:
                 imageType: distroless
    

You may override the `imageType` by using the following pod annotation. Note that for clusters with the managed `TRAFFIC_DIRECTOR` control plane, only `distroless` is supported as an explicit override value (`debug` or other non-distroless image types are not allowed).
    
    
    sidecar.istio.io/proxyImageType: distroless
    

After changing the image type of a deployment using the annotation, the deployment should be restarted. To revert to the default image, remove the `sidecar.istio.io/proxyImageType` annotation or the `imageType` field from your `MeshConfig`, and then restart the deployment.
    
    
    kubectl rollout restart deployment -n NAMESPACE DEPLOYMENT_NAME

Because it does not require a debug base image, most types of proxy debugging should use `gcloud beta container fleet mesh debug proxy-status / proxy-config` ([details](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-intro)).

## Outbound Traffic Policy

By default `outboundTrafficPolicy` is set to `ALLOW_ANY`. In this mode, all traffic to any external service is allowed. To control and restrict the traffic to only the external services for which [service entries](https://istio.io/latest/docs/reference/config/networking/service-entry/) are defined you can change the default behavior of `ALLOW_ANY` to `REGISTRY_ONLY`.

**Warning:** You can overwrite your own changes. If you already have an existing configmap, you must include all previous customization settings within the `mesh:` section to preserve your changes.

  1. The following configuration configures the `outboundTrafficPolicy` to `REGISTRY_ONLY`:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: istio-release-channel
           namespace: istio-system
         data:
           mesh: |-
             outboundTrafficPolicy:
               mode: REGISTRY_ONLY
         

where release-channel is your [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) (`asm-managed`, `asm-managed-stable`, or `asm-managed-rapid`).

  2. You can make the previous necessary config changes in the configmap using the following command:
         
         kubectl edit configmap istio-release-channel -n istio-system -o yaml
         

  3. Run the following command to view the configmap:
         
         kubectl get configmap istio-release-channel -n istio-system -o yaml
         

  4. To verify that `outboundTrafficPolicy` is enabled with `REGISTRY_ONLY`, ensure the following lines appear in the `mesh:` section.
         
         ...
         apiVersion: v1
         data:
           mesh: |
             outboundTrafficPolicy:
              mode: REGISTRY_ONLY
         ...
         




## End user authentication

You can configure managed Cloud Service Mesh user authentication for browser-based end-user authentication and access control to your deployed workloads. For more information, see [Configuring Cloud Service Mesh user authentication](https://docs.cloud.google.com/service-mesh/docs/security/end-user-auth).

## Configure the minimum TLS version for your workloads

If you directly onboarded to Cloud Service Mesh with a managed `TRAFFIC_DIRECTOR` [control plane implementation](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed#identify_control_plane_implementation), then you cannot change this setting.

You can use the `minProtocolVersion` field to specify the minimum TLS version for the TLS connections among your workloads. For more information on setting the minimum TLS version and checking the TLS configuration of your workloads, see [Istio Workload Minimum TLS Version Configuration](https://preliminary.istio.io/latest/docs/tasks/security/tls-configuration/workload-min-tls-version/).

**Warning:** The Istio guide linked in the preceding paragraph uses `IstioOperator`, which is not supported by managed Cloud Service Mesh. You must convert the `IstioOperator` to an equivalent `ConfigMap`, such as the following example.

The following example shows a `ConfigMap` setting the minimum TLS version for workloads to 1.3:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: istio-release-channel
      namespace: istio-system
    data:
      mesh: |-
        meshMTLS:
          minProtocolVersion: TLSV1_3
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
