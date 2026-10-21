---
url: https://docs.cloud.google.com/service-mesh/docs/security/configuring-mtls/
title: Configure transport security \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:38.697151+00:00
---

# Configure transport security  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/security/configuring-mtls/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure transport security

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

You can secure inter-service traffic in Cloud Service Mesh with Istio APIs by enforcing strict mutual TLS (mTLS). In Kubernetes workloads, auto mTLS is enabled by default: client sidecar proxies automatically send mTLS traffic to sidecars, but destination services still accept both plaintext and encrypted requests.

`PeerAuthentication` policies let you restrict services to only accept mTLS. You can apply a policy mesh-wide, to a specific namespace, or to an individual workload. For supported fields across platforms, see [Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features).

## Enable mutual TLS per namespace

To enable mTLS for all workloads within a particular namespace, use a namespace-wide authentication policy. You specify the namespace it applies to under `metadata`.
    
    
    kubectl apply -f - <<EOF
    apiVersion: "security.istio.io/v1beta1"
    kind: "PeerAuthentication"
    metadata:
      name: "AUTH_POLICY_NAME"
      namespace: "NAMESPACE"
    spec:
      mtls:
        mode: STRICT
    EOF
    

Expected output: 
    
    
    peerauthentication.security.istio.io/AUTH_POLICY_NAME created

## Enable mutual TLS per workload

To set a `PeerAuthentication` policy for a specific workload, you must configure the `selector` section and specify the labels that match the targeted workload. However, Cloud Service Mesh can't aggregate workload-level policies for outbound mTLS traffic to a service. You need to configure a destination rule to manage that behavior.

  1. Apply an authentication policy to a specific workload in your namespace:
         
         cat <<EOF | kubectl apply -n NAMESPACE -f -
         apiVersion: "security.istio.io/v1beta1"
         kind: "PeerAuthentication"
         metadata:
           name: "AUTH_POLICY_NAME"
           namespace: "NAMESPACE"
         spec:
           selector:
             matchLabels:
               app: WORKLOAD
           mtls:
             mode: STRICT
         EOF
         

Expected output:
         
         peerauthentication.security.istio.io/AUTH_POLICY_NAME created

  2. Configure a matching destination rule:
         
         cat <<EOF | kubectl apply -n NAMESPACE -f -
         apiVersion: "networking.istio.io/v1alpha3"
         kind: "DestinationRule"
         metadata:
           name: "DEST_RULE_NAME"
         spec:
           host: "WORKLOAD.NAMESPACE.svc.cluster.local"
           trafficPolicy:
             tls:
               mode: ISTIO_MUTUAL
         EOF
         

Expected output:
         
         destinationrule.networking.istio.io/WORKLOAD created




## Enforce mesh-wide mTLS

To prevent all your services in the mesh from accepting plain-text traffic, set a mesh-wide `PeerAuthentication` policy with the mTLS mode set to `STRICT` (the default is `PERMISSIVE`). The mesh-wide `PeerAuthentication` policy shouldn't have a selector and must be applied in the root namespace, `istio-system`. When you deploy the policy, the control plane automatically provisions TLS certificates so that workloads can authenticate with each other.

To enforce mesh-wide mTLS:
    
    
    kubectl apply -f - <<EOF
    apiVersion: "security.istio.io/v1beta1"
    kind: "PeerAuthentication"
    metadata:
      name: "AUTH_POLICY_NAME"
      namespace: "istio-system"
    spec:
      mtls:
        mode: STRICT
    EOF
    

Expected output: 
    
    
    peerauthentication.security.istio.io/AUTH_POLICY_NAME created

### Disabling mTLS for Managed CSM

Cloud Service Mesh does not support the `mtls.mode: DISABLE` value in a `PeerAuthentication` resource.

To successfully disable mTLS in Cloud Service Mesh, you must explicitly define the client's behavior with the server's requirements by using the `DestinationRule` API.

#### Conceptual Overview

  1. **Server-Side** : You use a `PeerAuthentication` resource to set the server-side proxy default value.
  2. **Client-Side Approach** : You use a `DestinationRule` resource to explicitly tell the client-side proxies to use plaintext when communicating with that specific server.



#### Examples

**Step 1: Configure PeerAuthentication**

In this example we will use the default policy of PERMISSIVE and so don't need to explicitly define the policy.

**Step 2: Configure Client-Side DestinationRule**

This configuration tells clients to use plaintext when calling `httpbin`.
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: DestinationRule
    metadata:
      name: "DEST_RULE_NAME"
      namespace: sample-namespace
    spec:
      host: "WORKLOAD.NAMESPACE.svc.cluster.local"
      trafficPolicy:
        tls:
          mode: DISABLE
    

## Find and delete `PeerAuthentication` policies

For a list of all the `PeerAuthentication` policies in the service mesh:
    
    
    kubectl get peerauthentication --all-namespaces
    

If there is a `PeerAuthentication` policy in force, you can delete it with `kubectl delete`:
    
    
    kubectl delete peerauthentication -n NAMESPACE AUTH_POLICY_NAME
    

## What's next

  * [Cloud Service Mesh by example: mTLS](https://docs.cloud.google.com/service-mesh/docs/tutorials/mtls)
  * [Learn about security in Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/security/security-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
