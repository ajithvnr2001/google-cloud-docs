---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-ambient-networking/
title: Troubleshoot ambient networking \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:11.312669+00:00
---

# Troubleshoot ambient networking  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-ambient-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot ambient networking Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note** : Before using GKE ambient networking, you must be added to an allowlist. Request access by filling out the [sign-up form](https://forms.gle/HhretawUX6GFFxq87). Allow 2 to 3 business days for your request to be processed. 

This page shows you how to troubleshoot and verify Google Kubernetes Engine (GKE) ambient networking. It provides instructions for checking the health of in-cluster ambient components, diagnosing traffic authentication and authorization issues, verifying certificate issuance, and inspecting metrics and logs.

## Verify components are installed and healthy

In-cluster components for Cloud Service Mesh ambient mode are installed in the `gke-managed-ambient` namespace. You can see the status of all relevant Pods with the following command:
    
    
    kubectl get pods -n gke-managed-ambient
    

## Verify traffic is authenticated and authorized

Using [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) in Google Cloud console, check the access logs that correspond to the connections of interest:
    
    
    resource.type="k8s_container"
    resource.labels.location="CLUSTER_LOCATION"
    resource.labels.cluster_name="CLUSTER_NAME"
    logName="projects/PROJECT_ID/logs/gke-ambient-node-proxy-accesslog"
    

The access logs display connection details, including authentication and authorization status.

### Log format

The following fields are present in the `jsonPayload` of the access log entry:

Field | Type | Description  
---|---|---  
`connection` | struct | Connection information.  
`connection.src_ip` | string | Source IP of the connection.  
`connection.src_port` | int | Source port of the connection.  
`connection.dest_ip` | string | Destination IP of the connection.  
`connection.dest_port` | int | Destination port of the connection.  
`connection.direction` | string | Direction of the connection: `{ingress, egress}`  
`src` | struct | Endpoint information of the source.  
`src.spiffe_id` | string | The SPIFFE identity of the Pod. Empty if the Pod does not have a SPIFFE identity.  
`dst` | struct | Endpoint information of the destination.  
`dst.spiffe_id` | string | The SPIFFE identity of the Pod. Empty if the Pod does not have a SPIFFE identity.  
`error_details` | string | Details about the error that occurred (or `-` if no error occurred).  
`timestamp` | string | Time when the connection was observed (UTC).  
`tls_failure_reason` | string | TLS handshake [failure reason](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/ssl#trouble-shooting). `-` if the connection is not TLS.  
  
## Verify certificates are successfully issued

Use the following command to inspect the status of `CertificateSigningRequests` for workload Pods in your cluster:
    
    
    kubectl get csr
    

You should see "Approved,Issued" conditions similar to the following:
    
    
    NAME                           AGE   SIGNERNAME                 CONDITION
    gke-ambient-spiffe-csr-q8kqh   2s    spiffe.gke.io/fleet-svid   Approved,Issued
    gke-ambient-spiffe-csr-t5px2   7s    spiffe.gke.io/fleet-svid   Approved,Issued
    

## Network Services Monitoring metrics

In addition to standard Cloud Observability metrics, Cloud Service Mesh ambient networking integrates with Network Services Monitoring to provide detailed Layer 4 network telemetry.

For more information, see the [Network Services Monitoring overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/overview) and the [Network Services Monitoring metrics reference](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/metrics-reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
