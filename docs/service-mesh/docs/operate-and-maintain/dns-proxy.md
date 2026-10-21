---
url: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/dns-proxy/
title: Set up DNS Proxy \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:02.494509+00:00
---

# Set up DNS Proxy  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/dns-proxy/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up DNS Proxy

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Kubernetes natively resolves DNS names only for `Services` in the local cluster. DNS Proxy lets you resolve Kubernetes `Services` across remote clusters in a [multi-cluster setup](https://docs.cloud.google.com/service-mesh/docs/gke-install-multi-cluster) and generate DNS records for `ServiceEntry` resources. This helps you route traffic to internal hostnames without maintaining additional internal DNS servers.

**Note:** DNS Proxy requires data plane version `1.21.5-asm.39` or later, and is available in the Rapid release channel.

## Configuring DNS Proxy

To configure DNS proxy, configure ISTIO_META_DNS_CAPTURE flag as follows. You can choose either the cluster or per-proxy wide configuration.

### Cluster wide configuration

To configure DNS proxy in the cluster, add `ISTIO_META_DNS_CAPTURE` proxy metadata to the `ConfigMap` for `MeshConfig`. The name of the `ConfigMap` has a format of `istio-<revision_name>`. For the details of revision, refer to [the overview of the revision](https://docs.cloud.google.com/service-mesh/docs/revisions-overview)
    
    
    apiVersion: v1
    data:
      mesh: |-
        ...
        defaultConfig:
          proxyMetadata:
            ISTIO_META_DNS_CAPTURE: "true"        
        ...
    kind: ConfigMap
    metadata:
      name: istio-<revision_name>
      namespace: istio-system
    

### Per-proxy configuration

To configure DNS proxy for a proxy, add the `ISTIO_META_DNS_CAPTURE` proxy metadata annotation as follows:
    
    
    kind: Deployment
    metadata:
      name: app1
      namespace: ns1
    spec:
    ...
      template:
        metadata:
          annotations:
            proxy.istio.io/config: |
              proxyMetadata:
                ISTIO_META_DNS_CAPTURE: "true"
    ...
    

### Verifying

To verify everything is configured correctly, run the steps.

#### Name resolution for `Service` across clusters

After the [multi-cluster setup](https://docs.cloud.google.com/service-mesh/docs/gke-install-multi-cluster), deploy a `Service` only in one of the clusters to verify the cross-cluster name resolution.

When you have the following example `Service` `ns1/svc1`, you can find `ClusterIP` in `Service`.
    
    
    $ kubectl get -n ns1 svc1
    kind: Service
    metadata:
      name: svc1
      namespace: ns1
    spec:
    ...
      ClusterIP: 210.200.1.1
    ...
    

Then, when using `curl` from the _other_ cluster to the `Service`, it should show the `ClusterIP` as follows.
    
    
    curl -sS -v svc1.ns1.svc.cluster.local
    *   Trying 210.200.1.1:80...
    

#### Name resolution for `ServiceEntry`

Add a `ServiceEntry` with a hostname not registered in your DNS. To verify the name resolution the following example has explicit address `192.168.123.123`.
    
    
    $ kubectl apply -f - <<EOF
    apiVersion: networking.istio.io/v1beta1
    kind: ServiceEntry
    metadata:
      name: test-service-entry
    spec:
      addresses:
      - "192.168.123.123"
      hosts:
      - not-existing-hostname.internal
      ports:
      - name: http
        number: 80
        protocol: HTTP
    EOF
    

Then, try DNS resolution in a Pod where DNS Proxy is enabled. For example, if you run a `curl` in the Pod, it should display the IP address as follows:
    
    
    curl -sS -v not-existing-hostname.internal
    *   Trying 192.168.123.123:80...
    

## IP auto-allocation for ServiceEntry

When using `ServiceEntry` with DNS Proxy, you can optionally enable IP auto-allocation. When enabled, internal IP addresses (from the `240.240.0.0/16` range) are automatically allocated for `ServiceEntry` hosts that don't specify explicit IP addresses in `spec.addresses`.

### Enabling IP auto-allocation

To enable IP auto-allocation, follow the instructions for your control plane implementation:

### TRAFFIC_DIRECTOR

For the `TRAFFIC_DIRECTOR` control plane implementation, configure IP auto-allocation in the `asm-options` `ConfigMap` within the `istio-system` namespace by setting `ip_auto_allocation: "true"`.

**Note:** For `TRAFFIC_DIRECTOR` implementations, IP auto-allocation is supported only in the **Rapid** release channel.

The following example shows an `asm-options` `ConfigMap` with IP auto-allocation enabled:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: asm-options
      namespace: istio-system
    data:
      # Enable IP auto-allocation for ServiceEntry (Rapid channel)
      ip_auto_allocation: "true"
    

You can also apply this configuration using `kubectl patch`:
    
    
    kubectl patch configmap/asm-options -n istio-system --type merge \
      -p '{"data":{"ip_auto_allocation":"true"}}'
    

### ISTIOD

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). **Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

For clusters using the `ISTIOD` control plane implementation (in-cluster or managed `ISTIOD`), configure IP auto-allocation by adding `ISTIO_META_DNS_AUTO_ALLOCATE: "true"` to your proxy metadata within `MeshConfig`:
    
    
    apiVersion: v1
    data:
      mesh: |-
        defaultConfig:
          proxyMetadata:
            ISTIO_META_DNS_CAPTURE: "true"
            ISTIO_META_DNS_AUTO_ALLOCATE: "true"
    kind: ConfigMap
    metadata:
      name: istio-<revision_name>
      namespace: istio-system
    

### Verifying IP auto-allocation

You can verify the IP auto-allocation works using the following steps.

Before the verification, create a `ServiceEntry` without specifying `spec.addresses`:
    
    
    $ kubectl apply -f - <<EOF
    apiVersion: networking.istio.io/v1beta1
    kind: ServiceEntry
    metadata:
      name: auto-allocated-service-entry
      namespace: ns1
    spec:
      hosts:
      - auto-allocated.internal
      ports:
      - name: http
        number: 80
        protocol: HTTP
      resolution: DNS
    EOF
    

**Note:** that the first step is only possible to check when you are using `TRAFFIC_DIRECTOR` implementation. If you are using `ISTIOD`, move to the second step.

#### 1\. Check allocated address in `status.addresses` (`TRAFFIC_DIRECTOR` only)

In the `TRAFFIC_DIRECTOR` implementation, the controller allocates a VIP and populates the `status.addresses` field of the `ServiceEntry`:
    
    
    $ kubectl get serviceentry auto-allocated-service-entry -n ns1 -o yaml
    

The output displays the allocated address under `status.addresses`:
    
    
    status:
      addresses:
      - host: auto-allocated.internal
        value: 240.240.0.1
    

#### 2\. Test DNS resolution from a Pod (`TRAFFIC_DIRECTOR` and `ISTIOD`)

In both `TRAFFIC_DIRECTOR` and `ISTIOD` implementations, send a request from a Pod where DNS Proxy is enabled to verify that name resolution resolves to the allocated VIP:
    
    
    $ kubectl exec deploy/curl -n ns1 -- curl -sS -v http://auto-allocated.internal
    

The connection attempt should resolve to the automatically allocated VIP (for example, `240.240.0.1:80`):
    
    
    *   Trying 240.240.0.1:80...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
