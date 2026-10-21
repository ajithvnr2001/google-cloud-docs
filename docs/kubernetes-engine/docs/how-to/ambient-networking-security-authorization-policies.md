---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ambient-networking-security-authorization-policies/
title: Ambient networking security and authorization policies \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:03.666202+00:00
---

# Ambient networking security and authorization policies  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ambient-networking-security-authorization-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Ambient networking security and authorization policies Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note** : Before using GKE ambient networking, you must be added to an allowlist. Request access by filling out the [sign-up form](https://forms.gle/HhretawUX6GFFxq87). Allow 2 to 3 business days for your request to be processed. 

This page shows you how to create authorization policies on ambient networking.

## Prerequisites

Before you can complete the steps in this document, you must meet the following conditions:

  * A running GKE cluster with Cloud Service Mesh ambient networking enabled.
  * A [namespace enrolled in ambient networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking#enroll_a_namespace_for_ambient_networking) (for example, `ambient-test`) with sample client and server workloads deployed.
  * [Mutual TLS (mTLS) enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking#enable_mtls_for_a_service) between the client and server workloads by using a `GCPServerTLSPolicy` (with `mtlsMode: Strict`) and a `GCPClientTLSPolicy`. Identity-based `GCPAuthzPolicy` rules that match `CLIENT_CERT_URI_SAN` require active mTLS to extract the client's SPIFFE identity.



For a detailed environment setup, see [Prepare GKE ambient networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking).

## Deny-by-default policy

By default, the GKE Ambient Authorization Policy API permits all traffic unless restricted by policy, matching standard Kubernetes `NetworkPolicy` behavior.

The `DENY_BY_DEFAULT` action lets you change this default behavior. When applied to a namespace, this policy blocks all traffic to workloads in that namespace unless explicitly allowed by an `ALLOW` policy.

This page shows you how to configure and use `DENY_BY_DEFAULT` in Cloud Service Mesh to establish a secure-by-default posture for your workloads.

### Limitations

Before applying a `DENY_BY_DEFAULT` policy, take note of the following limitations:

  * You can only create one `DENY_BY_DEFAULT` policy per namespace.
  * A policy with the `DENY_BY_DEFAULT` action cannot have any rules defined.
  * Use this action to set a namespace-wide baseline `matchLabels: {}` to target all Pods. You can't use `DENY_BY_DEFAULT` for per-Pod restrictions.



### Set up a deny-by-default authorization policy

To establish a deny-by-default baseline across a namespace and selectively allow access to specific workloads, follow these steps:

  1. Create and apply a `GCPAuthzPolicy` with the action set to `DENY_BY_DEFAULT` to your namespace.
         
         cat <<EOF > deny-by-default-policy.yaml && kubectl apply -f deny-by-default-policy.yaml
         apiVersion: networking.gke.io/v1
         kind: GCPAuthzPolicy
         metadata:
           name: deny-by-default-authz
           namespace: ambient-test
         spec:
           action: DENY_BY_DEFAULT
           enforcementLevel: L4
           targetRefs:
           - group: ""
             kind: Pod
             selector:
               matchLabels: {}
         EOF
         

The output is similar to:
         
         gcpauthzpolicy.networking.gke.io/deny-by-default-authz created
         

This policy blocks all inbound (East-West and ingress) traffic to workloads in the `ambient-test` namespace by default. It does not restrict outbound traffic originating from workloads in the namespace.

  2. To selectively allow traffic, create and apply an `ALLOW` policy:

**Important:** `GCPAuthzPolicy` rules matching `CLIENT_CERT_URI_SAN` strictly require mTLS (`GCPServerTLSPolicy` with `Strict` mode and `GCPClientTLSPolicy`) to be [configured beforehand](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking#enable_mtls_for_a_service). If mTLS is not active, the proxy cannot extract the client's SPIFFE identity, causing SPIFFE-based `ALLOW` rules to never match and all traffic to be dropped by `DENY_BY_DEFAULT`.
         
         cat <<EOF > allow-policy.yaml && kubectl apply -f allow-policy.yaml
         apiVersion: networking.gke.io/v1
         kind: GCPAuthzPolicy
         metadata:
           name: allow-client-to-server
           namespace: ambient-test
         spec:
           action: ALLOW
           enforcementLevel: L4
           targetRefs:
           - group: ""
             kind: Pod
             selector:
               matchLabels:
                 app: server
           rules:
           - from:
               sources:
               - principals:
                 - principalSelector: CLIENT_CERT_URI_SAN
                   principal:
                     type: Exact
                     value: spiffe://PROJECT_ID.svc.id.goog/ns/ambient-test/sa/client
         EOF
         

Replace PROJECT_ID with your project ID.

Policy propagation can take up to three minutes after controller acceptance. Wait three minutes before proceeding.

  3. Test connectivity from the client to the server. It should succeed because it matches the `ALLOW` policy.
         
         kubectl exec -it deploy/client -n ambient-test -- /bin/curl -fsLS server.ambient-test.svc.cluster.local
         

  4. Test connectivity from the server to itself (or any other workload without an explicit allow policy). It should fail because of the `DENY_BY_DEFAULT` policy.
         
         kubectl exec -it deploy/server -n ambient-test -- /bin/curl -fsLS server.ambient-test.svc.cluster.local
         

The output is similar to:
         
         curl: (52) Empty reply from server.
         




### Logging

When a request is denied by an authorization policy, the node proxy writes an access log entry to Cloud Logging under the `gke-ambient-node-proxy-accesslog` log name. The entry contains the following field in the JSON payload:

  * `jsonPayload.error_details`: `- rbac_access_denied_matched_policy[none]`



You can use Logs Explorer in Google Cloud console to view the access log entries for denied connections:
    
    
    resource.type="k8s_container"
    logName="projects/PROJECT_ID/logs/gke-ambient-node-proxy-accesslog"
    jsonPayload.error_details=~"rbac_access_denied"
    

For more information, see [Verify traffic is authenticated and authorized](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-ambient-networking#verify_traffic_is_authenticated_and_authorized).

## Egress security policies

To inspect and control outbound traffic from ambient networking workloads to external endpoints or the internet, you can route egress traffic through Secure Web Proxy (SWP).

For instructions on configuring `GCPBackend` and `GCPEgressPolicy` resources, see [Route ambient egress traffic through Secure Web Proxy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ambient-egress-swp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
