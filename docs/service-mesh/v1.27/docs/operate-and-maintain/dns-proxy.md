---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/dns-proxy/
title: Set up DNS Proxy \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:38.601235+00:00
---

# Set up DNS Proxy  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/dns-proxy/

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up DNS Proxy

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview).

DNS Proxy is a feature for providing the following capabilities:

  1. Propagating DNS entries of `Services` across clusters in a [multi-cluster setup](https://docs.cloud.google.com/service-mesh/v1.27/docs/gke-install-multi-cluster).
  2. Populating DNS entries for `ServiceEntry`.



Kubernetes provides DNS resolution only for `Services` in the local cluster. When you need to provide name resolution for `Services` in a remote clusters or use an internal-only hostname with `ServiceEntry` without having an additional internal-only DNS server, DNS Proxy provides a way to resolve DNS names for such cases.

**Note:** This feature is available from `1.21.5-asm.39` dataplane. 

## Configuring DNS Proxy

### Cluster wide configuration

To configure DNS proxy in the cluster, add `ISTIO_META_DNS_CAPTURE` proxy metadata to the `ConfigMap` for `MeshConfig`. The name of the `ConfigMap` has a format of `istio-<revision_name>`. For the details of revision, refer to [the overview of the revision](https://docs.cloud.google.com/service-mesh/v1.27/docs/revisions-overview)
    
    
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

#### Name resolution for `Service` across clusters

After the [multi-cluster setup](https://docs.cloud.google.com/service-mesh/v1.27/docs/gke-install-multi-cluster), deploy a `Service` only in one of the clusters to verify the cross-cluster name resolution.

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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
