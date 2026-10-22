---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cluster-network-policy/
title: Configure cluster network policies \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:19.157170+00:00
---

# Configure cluster network policies  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cluster-network-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure cluster network policies Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Alpha:** The ClusterNetworkPolicy API is in **preview** and is at the **alpha** level. The CustomResourceDefinition is subject to change in future versions. 

ClusterNetworkPolicy lets you define global GKE security postures across the entire cluster. This document is intended for cluster administrators who need to enforce mandatory security guardrails or establish zero-trust baselines.

This resource relies on a strict evaluation hierarchy that operates at a higher precedence than standard, namespace-scoped `NetworkPolicy` resources. You can use the `ClusterNetworkPolicy` resource to implement explicit **Deny** , **Accept** , or **Pass** actions. These actions let you configure global allow or deny policies, delegate traffic control to specific namespaces, and restrict egress traffic to CIDR blocks.

## Before you begin

Before you configure a cluster network policy, ensure that you meet the following requirements:

  1. Ensure your GKE cluster runs version 1.36.0-gke.4447000 or later.
  2. Ensure your cluster uses GKE Dataplane V2.



## Supported protocols and ports

ClusterNetworkPolicy rules can match traffic based on the TCP, UDP, or SCTP protocols. You can specify destination ports in the following ways:

  * **Specific port number** : use the `destinationPort.number` setting to target a single port (for example, `80`).
  * **Port range** : use the `destinationPort.range` setting to target a range of ports (for example, `8000` to `9000`).
  * **Named port** : use the `destinationNamedPort` setting to target a symbolic name defined in a Pod specification.



## Policy evaluation hierarchy

Unlike standard, additive NetworkPolicies, a ClusterNetworkPolicy (CNP) relies on a strict evaluation hierarchy where the first matching rule wins. Traffic flows sequentially through a three-layer pipeline:

  * **The tier** : Admin rules execute first, cascading down to NetworkPolicy, then Baseline.
  * **CNP priority** : within a tier, policies are evaluated based on their explicit numeric priority.
  * **CNP rule order** : inside a single policy, rules are processed top-to-bottom like an access control list (ACL).



![Diagram showing the GKE network policy evaluation hierarchy](https://docs.cloud.google.com/static/kubernetes-engine/images/cnp-hierarchy.png)

The preceding diagram illustrates the decision flow of the CNP evaluation hierarchy:

  1. **Admin Tier** : traffic is first evaluated against the `ClusterNetworkPolicy` rules in the `Admin` tier. If there is an Allow or Deny match, evaluation stops. If there is no match or a Pass action, traffic proceeds to the `NetworkPolicy` tier.
  2. **NetworkPolicy Tier** : traffic is evaluated against standard namespace policies. If there is a match, traffic is allowed. If there is no match, traffic proceeds to the Baseline tier.
  3. **Baseline Tier** : traffic is evaluated against the `ClusterNetworkPolicy` rules in the Baseline tier. If there is an Allow or Deny match, evaluation stops. If there is no match, traffic proceeds to the default behavior.
  4. **Default GKE Behavior** : if no policies match in any tier, traffic is subjected to an implicit allow behavior.



### Verdict actions: Allow, Deny, and Pass

Upon matching a packet, every rule triggers one of three strict actions:

  * **Deny** : immediately blocks the traffic.
  * **Accept** : permits the traffic. Both actions instantly short-circuit the pipeline, which ignores all remaining policies.
  * **Pass** : transfers control down to the next tier, allowing platform engineers to delegate specific traffic decisions to standard namespace-level policies without giving up overarching administrative control.



## Configure a global deny policy

To isolate a sensitive namespace from all other cluster internal traffic, apply a non-overridable deny rule. This default-deny policy helps ensure that any traffic to or from the sensitive namespace is blocked at the administrative level. This policy acts as a protective baseline that cannot be accidentally bypassed by namespace-level rules.

  1. Save the following manifest as `global-deny.yaml`:
         
         apiVersion: policy.networking.k8s.io/v1alpha2
         kind: ClusterNetworkPolicy
         metadata:
           name: cluster-wide-deny-sensitive
         spec:
           tier: Admin
           priority: 10
           subject:
             namespaces:
               matchLabels:
                 kubernetes.io/metadata.name: sensitive-ns
           ingress:
           - action: Deny
             name: deny-all-ingress
             from:
             - namespaces:
                 matchLabels: {}
           egress:
           - action: Deny
             name: deny-all-egress
             to:
             - namespaces:
                 matchLabels: {}
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f global-deny.yaml
         




## Configure a global allow policy

A global allow policy can help ensure that all Pods can reach the cluster DNS service, regardless of any developer-created network policies.

  1. Save the following manifest as `global-allow-dns.yaml`:
         
         apiVersion: policy.networking.k8s.io/v1alpha2
         kind: ClusterNetworkPolicy
         metadata:
           name: allow-kube-dns-admin
         spec:
           tier: Admin
           priority: 20
           subject:
             namespaces: {}
           egress:
           - action: Accept
             name: allow-dns-egress
             to:
             - pods:
                 namespaceSelector:
                   matchLabels:
                     kubernetes.io/metadata.name: kube-system
                 podSelector:
                   matchLabels:
                     k8s-app: kube-dns
             protocols:
             - udp:
                 destinationPort:
                   number: 53
             - tcp:
                 destinationPort:
                   number: 53
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f global-allow-dns.yaml
         




## Delegate traffic to namespace policies

Delegate specific traffic patterns to standard namespace-scoped NetworkPolicy objects.

  1. Save the following manifest as `delegate-policy.yaml`:
         
         apiVersion: policy.networking.k8s.io/v1alpha2
         kind: ClusterNetworkPolicy
         metadata:
           name: delegate-to-netpol
         spec:
           tier: Admin
           priority: 30
           subject:
             namespaces: {}
           egress:
           - action: Pass
             name: delegate-web-traffic
             to:
             - namespaces:
                 matchLabels:
                   app: web-backend
             protocols:
             - tcp:
                 destinationPort:
                   number: 8080
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f delegate-policy.yaml
         

  3. To permit the delegated traffic within the target namespace, save the following standard `NetworkPolicy` manifest as `allow-web-backend.yaml` :
         
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           name: allow-web-backend
           namespace: backend-ns
         spec:
           podSelector:
             matchLabels:
               app: web-backend
           ingress:
           - from:
             - namespaceSelector:
                 matchLabels:
                   app: web-frontend
             ports:
             - protocol: TCP
               port: 8080
         

  4. Apply the standard `NetworkPolicy` manifest to your cluster:
         
         kubectl apply -f allow-web-backend.yaml
         




## Configure baseline guardrails

Establish a default GKE security posture that namespace administrators can override using standard network policies.

  1. Save the following baseline manifest as `baseline-deny.yaml`:
         
         apiVersion: policy.networking.k8s.io/v1alpha2
         kind: ClusterNetworkPolicy
         metadata:
           name: default-deny-baseline
         spec:
           tier: Baseline
           priority: 100
           subject:
             namespaces: {}
           ingress:
           - action: Deny
             name: baseline-deny-all
             from:
             - namespaces: {}
         

  2. Apply the baseline manifest to your cluster:
         
         kubectl apply -f baseline-deny.yaml
         

  3. Save the following developer override manifest as `developer-allow.yaml`:
         
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           name: allow-frontend-access
           namespace: my-app-ns
         spec:
           podSelector:
             matchLabels:
               app: frontend
           ingress:
           - from:
             - namespaceSelector:
                 matchLabels:
                   kubernetes.io/metadata.name: ingress-nginx
         

  4. Apply the override manifest to your cluster:
         
         kubectl apply -f developer-allow.yaml
         




## Configure policies using named ports

To abstract port numbers from your security policies, reference named ports defined in your Pod specifications.

  1. Save the following deployment manifest as `app-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-webapp
         spec:
           template:
             spec:
               containers:
               - name: web-container
                 image: nginx
                 ports:
                 - name: http-web
                   containerPort: 8080
         

  2. Apply the deployment manifest to your cluster:
         
         kubectl apply -f app-deployment.yaml
         

  3. Save the following policy manifest as `named-port-policy.yaml`:
         
         apiVersion: policy.networking.k8s.io/v1alpha2
         kind: ClusterNetworkPolicy
         metadata:
           name: allow-web-named-port
         spec:
           tier: Admin
           priority: 40
           subject:
             namespaces: {}
           egress:
           - action: Accept
             to:
             - namespaces:
                 matchLabels:
                   app: my-webapp
             protocols:
             - tcp:
                 destinationNamedPort: http-web
         

  4. Apply the policy manifest to your cluster:
         
         kubectl apply -f named-port-policy.yaml
         




## Restrict egress to CIDR blocks

Control access to external resources or corporate intranets by specifying CIDR blocks.

  1. Save the following manifest as `cidr-policy.yaml`:
         
         apiVersion: policy.networking.k8s.io/v1alpha2
         kind: ClusterNetworkPolicy
         metadata:
           name: allow-egress-to-intranet
         spec:
           tier: Admin
           priority: 60
           subject:
             namespaces: {}
           egress:
           - action: Accept
             name: allow-intranet
             to:
             - networks:
               - 10.0.0.0/8
               - 192.168.0.0/16
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f cidr-policy.yaml
         




## Configure priority precedence

To control evaluation order when multiple policies apply to the same Pods, specify a priority. Priorities range from 0 to 1000, where lower numbers indicate higher precedence. A single `ClusterNetworkPolicy` object can contain a maximum of 100 ingress rules and 100 egress rules.

  1. Save the following manifest as `priority-policies.yaml`:
         
         apiVersion: policy.networking.k8s.io/v1alpha2
         kind: ClusterNetworkPolicy
         metadata:
           name: deny-beta
         spec:
           tier: Admin
           priority: 10
           subject:
             namespaces:
               matchLabels:
                 team: alpha
           ingress:
           - action: Accept
             name: allow-beta-monitoring
             from:
             - pods:
                 namespaceSelector:
                   matchLabels:
                     team: beta
                 podSelector:
                   matchLabels:
                     app: monitoring
           - action: Deny
             name: deny-all-other-ingress-from-beta
             from:
             - namespaces:
                 matchLabels:
                   team: beta
         ---
         apiVersion: policy.networking.k8s.io/v1alpha2
         kind: ClusterNetworkPolicy
         metadata:
           name: allow-beta
         spec:
           tier: Admin
           priority: 50
           subject:
             namespaces:
               matchLabels:
                 team: alpha
           ingress:
           - action: Accept
             name: allow-all-ingress-from-beta
             from:
             - namespaces:
                 matchLabels:
                   team: beta
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f priority-policies.yaml
         




## Troubleshoot

To find methods for diagnosing and resolving policy errors, use the following commands.

List all cluster network policies in your cluster:
    
    
    kubectl get clusternetworkpolicies
    

Describe a specific policy to inspect its status and evaluation tier:
    
    
    kubectl describe clusternetworkpolicy/<policy-name>
    

The `status.conditions` field in the output provides information about whether the policy has been successfully reconciled by your cluster's networking implementation.

To monitor traffic flows and policy decisions, use [GKE Dataplane V2 Observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic).

## What's next

  * Learn more about [GKE Dataplane V2 Observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability).
  * Refer to the [Kubernetes Network Policy API](https://kubernetes.io/docs/concepts/services-networking/network-policies/) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
