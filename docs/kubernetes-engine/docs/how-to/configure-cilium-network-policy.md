---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cilium-network-policy/
title: Control cluster-wide communication using network policies \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:12.665152+00:00
---

# Control cluster-wide communication using network policies  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cilium-network-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Control cluster-wide communication using network policies Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to configure cluster-wide network policies for Google Kubernetes Engine (GKE).

Network policies and FQDN network policies help you define communication traffic rules between Pods. Network policies control how Pods communicate with each other within their applications and with external endpoints.

As a cluster administrator, you can configure Cilium cluster-wide network policies (CCNP), which overcome the network policy limitations for managing cluster-wide administrative traffic. Cilium cluster-wide network policies enforce network rules for all workloads across the entire cluster. In the GKE policy evaluation hierarchy, these policies reside in the `NetworkPolicy` tier. Although explicit **Deny** rules in a CCNP override allow rules in namespace-scoped policies, CCNP **Allow** rules have the same precedence as standard namespace policies. All CCNP rules are subordinate to policies in the Admin tier.

**Note:** `CiliumClusterwideNetworkPolicy` is a proprietary API. For new deployments, use the Kubernetes-native, standardized [`ClusterNetworkPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cluster-network-policy) instead. 

Cilium cluster-wide network policy for GKE is a cluster-scoped CustomResourceDefinition (CRD) that specifies policies enforced by GKE. By enabling Cilium cluster-wide network policy in GKE, you can centrally manage network rules for your entire cluster. You can control basic Layer 3 (IP-level) and Layer 4 (port-level) access for traffic entering and leaving the cluster.

## Benefits

With Cilium cluster-wide network policy you can:

  * **Enforce centralized security** : with CCNP, you can define network access rules that apply to your entire cluster. These rules override any potentially conflicting policies at the namespace level if they are explicit **Deny** rules. CCNP **Allow** rules reside in the same tier as standard namespace policies. For mandates, use the Admin tier in `ClusterNetworkPolicy`.
  * **Protect multi-tenancy** : if your cluster hosts multiple teams or tenants, you can secure isolation within a shared cluster by implementing CCNP rules, which focus on network traffic control. You can enforce network-level separation by assigning namespaces or groups of namespaces to specific teams.
  * **Define flexible default policies** : with CCNP, you can define default network rules for the entire cluster. You can customize these rules when necessary without compromising your overall cluster security.



To implement CCNP, enable GKE Dataplane V2 on your cluster. Ensure that the CCNP CustomResourceDefinition is enabled, then create policies that define network access rules for your cluster.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

Cilium cluster-wide network policies have the following requirements:

  * Google Cloud CLI version 465.0.0 or later.
  * You must have a GKE cluster running one of the following versions: 
    * 1.28.6-gke.1095000 or later
    * 1.29.1-gke.1016000 or later
  * Your cluster must [use GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2).
  * You must enable Cilium cluster-wide network policy CustomResourceDefinition.



### Limitations

Cilium cluster-wide network policies have the following limitations:

  * Layer 7 policies are not supported.
  * Node selectors are not supported.
  * The maximum number of `CiliumClusterwideNetworkPolicy` per cluster is 1000.



## Enable Cilium cluster-wide network policy in a new cluster

You can enable Cilium cluster-wide network policy in a new cluster by using the Google Cloud CLI or the Kubernetes Engine API.

### gcloud

To enable Cilium cluster-wide network policy in a new cluster, create a new cluster with `--enable-cilium-clusterwide-network-policy` flag.

**Autopilot**
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location COMPUTE_LOCATION \
        --enable-cilium-clusterwide-network-policy
    

Replace the following:

  * `CLUSTER_NAME` with the name of your cluster.
  * `COMPUTE_LOCATION` with the location of your cluster.



**Standard**
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location COMPUTE_LOCATION \
        --enable-cilium-clusterwide-network-policy \
        --enable-dataplane-v2
    

Replace the following:

  * `CLUSTER_NAME` with the name of your cluster.
  * `COMPUTE_LOCATION` with the location of your cluster.



### API

To enable the Cilium cluster-wide network policy, you must specify the following options while creating a new cluster:

[`datapathProvider` field](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#datapathprovider) in the [`networkConfig` object](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#networkconfig).
    
    
    {
      "cluster": {
        ...
        "networkConfig": {
          "datapathProvider": "ADVANCED_DATAPATH",
          "enableCiliumClusterwideNetworkPolicy": true
        }
      }
    }
    

Verify that the `ciliumclusterwidenetworkpolicies.cilium.io` CustomResourceDefinition is present in the output of the following command:
    
    
    kubectl get crds ciliumclusterwidenetworkpolicies.cilium.io
    

The output should be similar to the following:
    
    
    ciliumclusterwidenetworkpolicies.cilium.io     2023-09-19T16:54:48Z
    

## Enable Cilium cluster-wide network policy in an existing cluster

You can enable Cilium cluster-wide network policy in an existing cluster by using the Google Cloud CLI or the Kubernetes Engine API.

### gcloud

  1. Confirm the cluster has [GKE Dataplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#create-cluster).
         
         gcloud container clusters describe CLUSTER_NAME \
             --location COMPUTE_LOCATION \
             --format="value(networkConfig.datapathProvider)" \
         

Replace the following:

     * `CLUSTER_NAME` with the name of your cluster.
     * `COMPUTE_LOCATION` with the location of your cluster.
  2. Update the cluster using the `--enable-cilium-clusterwide-network-policy` flag.
         
         gcloud container clusters update CLUSTER_NAME \
             --location COMPUTE_LOCATION \
             --enable-cilium-clusterwide-network-policy
         

  3. Restart the anetd DaemonSet.
         
         kubectl rollout restart ds -n kube-system anetd && \
             kubectl rollout status ds -n kube-system anetd
         

**Note:** Restarting the DaemonSet will cause temporary downtime for your cluster. Downtime can vary depending on the size and complexity of your cluster. We recommend that you plan your deployments accordingly.



### API

Confirm that the cluster is enabled for GKE Dataplane V2:
    
    
    {
      "update": {
        "desiredEnableCiliumClusterwideNetworkPolicy": true
      },
      "name": "cluster"
    }
    To update an existing cluster, run the following update cluster command:
    {
      "update": {
        "desiredEnableCiliumClusterwideNetworkPolicy": true
      }
      "name": "cluster"
    }
    

Verify that the `ciliumclusterwidenetworkpolicies.cilium.io` CustomResourceDefinition is present in the output of the following command:
    
    
    kubectl get crds ciliumclusterwidenetworkpolicies.cilium.io
    

The output should be similar to the following:
    
    
    ciliumclusterwidenetworkpolicies.cilium.io     2023-09-19T16:54:48Z
    

## Using Cilium cluster-wide network policy

This section lists examples for configuring Cilium cluster-wide network policy.

### Example 1: Control ingress traffic to a workload

The following example enables all endpoints with the label `role=backend` to accept ingress connections on port 80 from endpoints with the label `role=frontend`. Endpoints with the label `role=backend` will reject all ingress connection that are not allowed by this policy.

  1. Save the following manifest as `l4-rule-ingress.yaml`:
         
         apiVersion: "cilium.io/v2"
         kind: CiliumClusterwideNetworkPolicy
         metadata:
           name: "l4-rule-ingress"
         spec:
           endpointSelector:
             matchLabels:
               role: backend
           ingress:
             - fromEndpoints:
                 - matchLabels:
                     role: frontend
               toPorts:
                 - ports:
                     - port: "80"
                       protocol: TCP
         

  2. Apply the manifest:
         
         kubectl apply -f l4-rule-ingress.yaml
         




### Example 2: Restrict egress traffic from a workload on a given port

The following rule limits all endpoints with the label `app=myService` to only be able to emit packets using TCP on port 80, to any Layer 3 destination:

  1. Save the following manifest as `l4-rule-egress.yaml`:
         
         apiVersion: "cilium.io/v2"
         kind: CiliumClusterwideNetworkPolicy
         metadata:
           name: "l4-rule-egress"
         spec:
           endpointSelector:
             matchLabels:
               app: myService
           egress:
             - toPorts:
                 - ports:
                     - port: "80"
                       protocol: TCP
         

  2. Apply the manifest:
         
         kubectl apply -f l4-rule-egress.yaml
         




### Example 3: Restrict egress traffic from a workload on a given port and CIDR

The following example limits all endpoints with the label `role=crawler` to only be able to send packets on port 80, protocols TCP, to a destination CIDR `192.10.2.0/24`.

  1. Save the following manifest as `cidr-l4-rule.yaml`:
         
         apiVersion: "cilium.io/v2"
          kind: CiliumClusterwideNetworkPolicy
          metadata:
            name: "cidr-l4-rule"
          spec:
            endpointSelector:
              matchLabels:
                role: crawler
            egress:
              - toCIDR:
                  - 192.0.2.0/24
                toPorts:
                  - ports:
                      - port: "80"
                        protocol: TCP
         

  2. Apply the manifest:
         
         kubectl apply -f cidr-l4-rule.yaml
         




## Monitoring and troubleshooting network traffic

You can monitor and troubleshoot the network traffic affected by cilium cluster-wide network policies by [Network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) and [GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability).

### Attempt to use Layer 7 policies or node selectors

**Symptom**

If you are using GKE with GKE Dataplane V2 and you attempt to define CCNP policies that include Layer 7 rules (for example: HTTP filtering) and node selectors, you might see an error message similar to the following:

**Error**
    
    
    Error from server (GKE Warden constraints violations): error when creating
    "ccnp.yaml": admission webhook
    "warden-validating.common-webhooks.networking.gke.io" denied the request: GKE
    Warden rejected the request because it violates one or more constraints.
    Violations details: {"[denied by gke-cilium-network-policy-limitation]":["L7
    rules are not allowed in CiliumClusterwideNetworkPolicy"]} Requested by user:
    'user@example.com', groups: 'system:authenticated'.
    

**Potential cause**

GKE has specific limitations on CCNPs. Layer 7 policies, which allow filtering based on application-level data (like HTTP headers), and node selectors are not supported within GKE's Cilium integration.

**Resolution**

If you need advanced Layer 7 filtering capabilities in your GKE cluster, consider using Cloud Service Mesh. This provides more granular application-level traffic control.

### Cilium cluster-wide network policy not enabled

**Symptom**

When you try to configure Cilium cluster-wide network policies (CCNP) in a cluster where the feature has not been explicitly enabled, you won't be able to configure it and might see an error message similar to the following:

**Error**
    
    
    error: resource mapping not found for name: "l4-rule" namespace: "" from
    "ccnp.yaml": no matches for kind "CiliumClusterwideNetworkPolicy" in version
    "cilium.io/v2" ensure CRDs are installed first
    

**Potential cause**

Cilium cluster-wide network policies rely on a Custom Resource Definition (CRD). The error message indicates that the CustomResourceDefinition is missing in the cluster.

**Resolution**

Enable Cilium cluster-wide network policy CustomResourceDefinition before using CCNPs.

## What's next

  * Read [Kubernetes documentation about network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

  * Learn how to [enforce cluster-wide security guardrails using ClusterNetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cluster-network-policy).

  * Read [CiliumClusterwideNetworkPolicy](https://docs.cilium.io/en/latest/network/kubernetes/policy/#ciliumclusterwidenetworkpolicy)

  * [Configure network policies for applications](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
