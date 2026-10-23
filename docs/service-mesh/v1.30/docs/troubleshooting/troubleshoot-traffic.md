---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-traffic/
title: Resolving traffic management issues in Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:51.677399+00:00
---

# Resolving traffic management issues in Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-traffic/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving traffic management issues in Cloud Service Mesh

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.30/docs/getting-support).

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

## Envoy proxy hanging on initialization

If debug logs indicate that the Envoy proxy is hanging during initialization, you can use the following command to identify what is blocking the process:
    
    
    kubectl -n <ns> -c istio-proxy exec -it POD_NAME -- /usr/local/bin/pilot-agent request POST /init_dump
    

## Troubleshooting 5xx HTTP response errors

You may encounter 5xx HTTP response errors when accessing applications through the Istio Ingress Gateway. Follow these steps to diagnose and resolve the issue.

  1. Identify the control plane
  2. Verify potential misconfigurations
  3. Verify pod discovery
  4. Analyze access logs



### Identify the control plane

Determine the control plane version and configuration because different versions may influence diagnostic processes. To verify the state of the managed control plane, run the following command:
    
    
    gcloud container fleet mesh describe --project PROJECT_ID
    

An `ACTIVE` state indicates the managed control plane is running normally.

### Verify potential misconfigurations

Common misconfigurations can lead to routing failures:

  * **Namespace Mismatch** : The `VirtualService` must be in the same namespace as the backend GKE service.
  * **Gateway Reference Mismatch** : The `VirtualService` must explicitly reference the correct `Gateway`. For example, if the `VirtualService` references `istio-system/istio-ingressgateway` but the gateway is in the `default` namespace, traffic won't route correctly.



### Verify pod discovery

Ensure the application pod is correctly discovered by the mesh:
    
    
    istioctl proxy-config endpoints POD_NAME
    

### Analyze access logs

Enable access logs to determine if errors originate from the backend application or the proxy. Key fields include `RESPONSE_FLAGS`, `UPSTREAM_LOCAL_ADDRESS`, and `RESPONSE_CODE`.

If logs indicate upstream errors, perform a direct `curl` test to the GKE service from a pod in the same namespace. If the `curl` request returns the same 5xx error, the issue originates from the backend application itself.

## Troubleshooting SSL certificate issues

SSL certificate errors at the Istio Ingress Gateway can be caused by expired certificates, protocol mismatches, or incorrect secret configurations.

### Identify SSL errors

Review the logs from the Istio Ingress Gateway pod:
    
    
    kubectl logs -l app=istio-ingressgateway -n GATEWAY_NAMESPACE
    

### Verify certificates and keys

Ensure the certificate and private key are valid and match using MD5 hashes:
    
    
    openssl x509 -noout -modulus -in CERTIFICATE.CRT | openssl md5
    openssl rsa -noout -modulus -in PRIVATE_KEY | openssl md5
    

Confirm the certificate is not expired and that the Common Name (CN) or Subject Alternative Name (SAN) matches the domain.

### Check TLS protocol and secret configuration

Verify the TLS version and cipher suites in the `Gateway` CRD. Ensure the Kubernetes secret containing the certificate and key is in the same namespace as the Ingress Gateway and that the `credentialName` matches the secret name.

## Troubleshooting intermittent timeouts to external endpoints

Intermittent timeouts may occur when requests are made to external endpoints (like Third party NLB) that resolve to multiple IP addresses.

### Potential cause: ServiceEntry resolution

If `spec.resolution` is set to `DNS`, Istio uses "strict DNS," which load balances over all resolved IP addresses. Some NLBs don't support this.

### Resolution

To resolve this, set the resolution on the `ServiceEntry` to `DNS_ROUND_ROBIN`.

## Troubleshooting uneven traffic distribution

If traffic is not distributed evenly across application pods, check the following:

  * **Pod Health** : Ensure all application pods were healthy during the imbalance.
  * **Load Balancing Algorithm** : Review the `DestinationRule` configuration for the `loadBalancer` setting (e.g., `consistentHash` or `ROUND_ROBIN`).
  * **Locality Load Balancing** : Verify if `localityLbSetting` is enabled. Note that this is not supported with the `TRAFFIC_DIRECTOR` control plane.



## Troubleshooting service propagation and quota issues

**Note:** This is only applicable to Cloud Service Mesh with Traffic Director implementation.

If new services or networking configurations are not being reflected in the mesh, it may be due to resource quotas being reached in the fleet project.

### Symptoms

  * Networking configurations (such as `VirtualService` or `DestinationRule`) are not being pushed to sidecar proxies.
  * New services appear "invisible" to the mesh despite being correctly defined.



### Steps to identify and resolve

  1. **Check resource quotas** : Verify if the fleet project has reached its quota for `BackendService` resources by checking the **Global internal traffic director backend services** quota in the fleet project. Cloud Service Mesh typically creates one `BackendService` per Kubernetes service port.
  2. **Review scale limitations** : Ensure that your configuration remains within the [supported scale limitations for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/supported-features-managed#limitations).
  3. **Increase quotas** : If quotas have been reached, request an increase for the affected resource in the fleet project to restore normal service propagation.



## Troubleshooting VirtualService evaluation

If a `VirtualService` is not behaving as expected, remember that routes are evaluated in the order they are listed. When you have multiple Virtual Services for the same host, their routes are merged. The routes from "older" Virtual Services get prioritized, therefore placed before routes from "newer" ones in the merged list. This reinforces the "first match" rule.

## Troubleshooting locality load balancing

By default, locality load balancing directs client traffic to endpoints in the same zone (the primary zone, or Priority 0). Envoy only routes traffic to failover zones (Priority 1 or higher) when endpoints in the primary zone are unhealthy or unavailable.

If you don't scale your endpoints to handle the entire zonal load or if you prefer to split traffic across zones, do one of the following:

  * Scale the pods in the respective zones to handle the local traffic load.
  * Disable the locality load balancing setting.



### Identify locality load balancing settings

Locality load balancing relies on node topology labels to group endpoints. To verify node labels and check settings, use the following commands:

  * Verify node topology labels:
        
        kubectl get nodes -o custom-columns=NAME:.metadata.name,\
            REGION:.metadata.labels."topology\\.kubernetes\\.io/region",\
            ZONE:.metadata.labels."topology\\.kubernetes\\.io/zone"
        

  * For GKE DestinationRules, inspect the locality settings:
        
        kubectl get destinationrule DESTINATION_RULE_NAME -o yaml
        

Look for `localityLbSetting: enabled: true` in the output.

  * To check Envoy proxy endpoints, priorities, and health:
        
        istioctl proxy-config endpoints POD_NAME.NAMESPACE \
            --cluster "outbound|PORT||SERVICE_FQDN" -o json
        

Look for the `priority` field in the endpoint configuration.

  * To view detailed active clusters configuration:
        
        istioctl proxy-config cluster POD_NAME.NAMESPACE \
            --fqdn SERVICE_FQDN -o json
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
