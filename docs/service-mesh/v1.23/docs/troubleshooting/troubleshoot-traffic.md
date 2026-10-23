---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/troubleshooting/troubleshoot-traffic/
title: Resolving traffic management issues in Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:26.642083+00:00
---

# Resolving traffic management issues in Cloud Service Mesh  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/troubleshooting/troubleshoot-traffic/

You are viewing archived v1.23 Service Mesh documentation.

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
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving traffic management issues in Cloud Service Mesh

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.23/docs/getting-support).

## API server connection errors in `istiod` logs

Istiod cannot contact the `apiserver` if you see errors similar to the following:
    
    
    error k8s.io/client-go@v0.18.0/tools/cache/reflector.go:125: Failed to watch *crd.IstioSomeCustomResource`…dial tcp 10.43.240.1:443: connect: connection refused

You can use the regular expression string `/error.*cannot list resource/` to find this error in the logs.

This error is usually transient and if you reached the proxy logs using `kubectl`, the issue might be resolved already. This error is usually caused by events that make the API server temporarily unavailable, such as when an API server that is not in a high availability configuration reboots for an upgrade or autoscaling change.

## The `istio-init` container crashes

This problem can occur when the pod iptables rules are not applied to the pod network namespace. This can be caused by:

  * An incomplete istio-cni installation
  * Insufficient workload pod permissions (missing `CAP_NET_ADMIN` permission)



If you use the Istio CNI plugin, verify that you followed the instructions completely. Verify that the `istio-cni-node` container is ready, and check the logs. If the problem persists, establish a secure shell (SSH) into the host node and search the node logs for `nsenter` commands, and see if there are any errors present.

If you don't use the Istio CNI plugin, verify that the workload pod has `CAP_NET_ADMIN` permission, which is automatically set by the sidecar injector.

## Connection refused after pod starts

When a Pod starts and gets `connection refused` trying to connect to an endpoint, the problem might be that the application container started before the `isto-proxy` container. In this case, the application container sends the request to `istio-proxy`, but the connection is refused because `istio-proxy` isn't listening on the port yet.

In this case, you can:

  * Modify your application's startup code to make continuous requests to the `istio-proxy` health endpoint until the application receives a 200 code. The `istio-proxy` health endpoint is:
        
        http://localhost:15020/healthz/ready
        

  * Add a retry request mechanism to your application workload.




## Listing gateways returns empty

**Symptom:** When you list Gateways using `kubectl get gateway --all-namespaces` after successfully creating a Cloud Service Mesh Gateway, the command returns `No resources found`.

This problem can happen on GKE 1.20 and later because the GKE Gateway controller automatically installs the GKE `Gateway.networking.x-k8s.io/v1alpha1` resource in clusters. To workaround the issue:

  1. Check if there are multiple gateway custom resources in the cluster:
         
         kubectl api-resources | grep gateway
         

Example output: 
         
         gateways                          gw           networking.istio.io/v1beta1            true         Gateway
         gatewayclasses                    gc           networking.x-k8s.io/v1alpha1           false        GatewayClass
         gateways                          gtw          networking.x-k8s.io/v1alpha1           true         Gateway

  2. If the list shows entries other than Gateways with the `apiVersion` `networking.istio.io/v1beta1`, use the full resource name or the distinguishable short names in the `kubectl` command. For example, run `kubectl get gw` or `kubectl get gateways.networking.istio.io` instead of `kubectl get gateway` to make sure istio Gateways are listed.




For more information on this issue, see [Kubernetes Gateways and Istio Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#istio-gateways).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
