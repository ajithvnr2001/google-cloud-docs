---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ambient-egress-swp/
title: Route ambient egress traffic through Secure Web Proxy \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:22.049488+00:00
---

# Route ambient egress traffic through Secure Web Proxy  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ambient-egress-swp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Route ambient egress traffic through Secure Web Proxy Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note** : Before using GKE ambient networking, you must be added to an allowlist. Request access by filling out the [sign-up form](https://forms.gle/HhretawUX6GFFxq87). Allow 2 to 3 business days for your request to be processed. 

This page shows you how to configure egress routing for workloads running on Google Kubernetes Engine (GKE) ambient networking to a Secure Web Proxy (SWP) gateway.

By routing outbound traffic through a Secure Web Proxy gateway, you can enforce centralized egress security policies—such as URL filtering, domain allowlists, and TLS inspection—without modifying your application code. The Layer 4 node proxy intercepts outbound traffic outside the application Pod, providing out-of-Pod security isolation even if a workload container is compromised.

## Architecture and traffic flow

In this deployment model, you maintain ownership of the infrastructure, including the GKE cluster, the Secure Web Proxy instance, and any Private Service Connect (PSC) endpoints (for cross-VPC deployments).

The egress traffic flow operates as follows:

  1. A workload Pod initiates outbound traffic to an external endpoint or internet destination.
  2. The local Layer 4 ambient node proxy intercepts the outbound request on the node.
  3. The node proxy establishes an HTTP CONNECT tunnel to the egress gateway.
  4. If the Secure Web Proxy resides in the same VPC network, traffic connects directly to the gateway. If the Secure Web Proxy resides in a different VPC network, traffic traverses a PSC Service Attachment.
  5. The Secure Web Proxy terminates the tunnel, enforces configured egress security policies, and forwards authorized requests to the destination.



## Limitations

Before setting up Secure Web Proxy egress routing, review the following limitations in preview:

  * **Namespace-wide policies:** Egress routing policies apply at the namespace level only. Granular Pod selection by using label selectors is not supported.
  * **Hostname filtering requires TLS inspection:** Secure Web Proxy policies can only filter egress traffic by IP address unless TLS inspection is enabled.
  * **Workload Identity:** GKE ambient networking supports standard Workload Identity. Managed Agent Identity pools are not supported for this preview.
  * **Authentication:** The connection between the ambient node proxy and the Secure Web Proxy skips server certificate verification. The CONNECT request includes an unbounded token alongside the client certificate.
  * **Resource recreation on configuration updates:** Changes made to an existing Secure Web Proxy instance or PSC configuration are not automatically propagated. If you update your Secure Web Proxy or PSC configuration, you must delete and recreate the `GCPEgressPolicy` resource and Secure Web Proxy instance to apply the changes.
  * **TLS inspection trust anchor:** GKE does not automatically inject the Secure Web Proxy private CA certificate into workload containers. If you use TLS inspection, you must manually install the trust certificate into your container images.



## Prerequisites

Before configuring egress routing, verify that you have the following:

  * A GKE cluster with ambient networking enabled. For instructions, see [Prepare GKE ambient networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking).
  * A deployed [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp) instance with a `serverTlsPolicy` configured with `clientValidationMode: ALLOW_INVALID_OR_MISSING_CLIENT_CERT` in your Google Cloud project or shared VPC.
  * If the Secure Web Proxy is located in a different VPC network than your GKE cluster: 
    * A PSC Service Attachment created for the Secure Web Proxy.
    * A PSC Consumer Endpoint configured in your GKE cluster VPC network.



To complete these steps, you must have the following roles:

  * Secure Web Proxy / Network Services: `networkservices.gateways.*` (or `roles/networkservices.admin`) to configure Secure Web Proxy gateway resources.
  * PSC Management (cross-VPC deployments only): `compute.networkAttachments.list` (or `roles/compute.networkAdmin`) to manage Private Service Connect connections.
  * GKE Management: `roles/container.clusterAdmin` to deploy custom resources (`GCPBackend`, `GCPEgressPolicy`).



## Configure trust for TLS inspection

If your Secure Web Proxy policy uses TLS inspection to inspect encrypted outbound traffic, the proxy generates certificates signed by its private Certificate Authority (CA) to impersonate external destinations.

Your workload application must trust the private CA certificate presented by the Secure Web Proxy. Because GKE does not inject this certificate automatically, you must install the SWP CA certificate (trust anchor) into your container's trust store.

To add the CA certificate to your container image, include the following lines in your Dockerfile:
    
    
    COPY swp-ca-cert.pem /usr/local/share/ca-certificates/swp-ca-cert.crt
    RUN update-ca-certificates
    

## Define the gateway endpoint

The first step in configuring ambient egress routing is to create a gateway endpoint, which defines the Secure Web Proxy endpoint within your GKE cluster and informs ambient networking of the proxy's location.

To specify the URI of your Secure Web Proxy or Private Service Connect (PSC) Service Attachment, create a `GCPBackend` custom resource in your GKE cluster:

### Same VPC

  1. Save the following manifest as `swp-backend.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: GCPBackend
         metadata:
           name: swp-backend
           namespace: ambient-test
         spec:
           serviceUris:
           - //networkservices.googleapis.com/projects/PROJECT_ID/locations/REGION/gateways/SWP_NAME
         

Replace the following:

     * `ambient-test`: the namespace enrolled in ambient networking.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region where your Secure Web Proxy is deployed.
     * `SWP_NAME`: the name of your Secure Web Proxy.
  2. Apply the `GCPBackend` resource:
         
         kubectl apply -f swp-backend.yaml
         




### Cross-VPC

  1. Save the following manifest as `swp-backend.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: GCPBackend
         metadata:
           name: swp-backend
           namespace: ambient-test
         spec:
           serviceUris:
           - //compute.googleapis.com/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Replace the following:

     * `ambient-test`: the namespace enrolled in ambient networking.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region where your PSC Service Attachment is deployed.
     * `ATTACHMENT_NAME`: the name of your PSC Service Attachment, if your Secure Web Proxy is in a different VPC network.
  2. Apply the `GCPBackend` resource:
         
         kubectl apply -f swp-backend.yaml
         




## Configure egress traffic redirection

Create a `GCPEgressPolicy` custom resource to route outbound traffic from the namespace to the Secure Web Proxy gateway. This provides the signaling necessary for the ambient node proxy to establish an HTTP CONNECT tunnel to the Secure Web Proxy, which is necessary for egress routing.

  1. Save the following manifest as `swp-egress-policy.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: GCPEgressPolicy
         metadata:
           name: swp-egress-policy
           namespace: ambient-test
         spec:
           to:
             excludeCIDRRanges:
             - "CLUSTER_CONTROL_PLANE_CIDR"
           proxyRef:
             group: networking.gke.io
             kind: GCPBackend
             name: swp-backend
         

Replace the following:

     * `ambient-test`: The namespace enrolled in ambient networking.
     * `CLUSTER_CONTROL_PLANE_CIDR`: The CIDR range for internal communications that should bypass the Secure Web Proxy (such as the GKE control plane address range or internal VPC subnets).
  2. Apply the `GCPEgressPolicy` resource:
         
         kubectl apply -f swp-egress-policy.yaml
         

After the policy is applied, outbound traffic from workloads in the namespace is redirected to the Secure Web Proxy.




## Troubleshooting

Use the following guidance to diagnose and resolve issues with ambient egress routing:

  * **Traffic not reaching the Secure Web Proxy:**
    * For same-VPC deployments, verify that the `GCPBackend` resource points to the correct Secure Web Proxy gateway URI.
    * For cross-VPC deployments:
    * Verify that the `GCPBackend` resource points to the correct PSC Service Attachment URI.
    * Verify that the PSC endpoint is established and accepted in the producer VPC.
    * Check that `excludeCIDRRanges` in `GCPEgressPolicy` is not inadvertently matching your destination traffic.
  * **mTLS connection failures:**
    * Verify that the Secure Web Proxy is configured to accept connections from the node proxy.
  * **TLS inspection certificate errors:**
    * If client requests fail with certificate validation errors (such as `x509: certificate signed by unknown authority`), verify that the Secure Web Proxy CA certificate is properly installed in the workload container's system certificate store.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
