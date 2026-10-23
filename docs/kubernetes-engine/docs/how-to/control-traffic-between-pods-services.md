---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-traffic-between-pods-services/
title: Set up multi-network network policies \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:22.862955+00:00
---

# Set up multi-network network policies  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-traffic-between-pods-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Set up multi-network network policies Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how you can enhance network security and traffic control within your cluster by configuring multi-network network policies that apply specifically to a designated Pod network. These multi-network network policies control traffic by using firewall rules at the Pod level, and they control traffic flow between Pods and Services.

To understand how multi-network network policies work, see [how Network Policies work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-networking-policies#how-it-works) with Pod networks.

## Requirements

To use multi-network network policies, consider the following requirements:

  * Google Cloud CLI version 459 and later.
  * You must have a GKE cluster running one of the following versions: 
    * 1.28.5-gke.1293000 or later
    * 1.29.0-gke.1484000 or later
  * Your cluster must use [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).



## Limitations

**FQDN network policy and CiliumClusterWide network policy are not supported** : If you use an FQDN network policy and a CiliumClusterWide network policy on a Pod that's connected to multiple networks, the policies affect all the Pod's connections, including connections where the policies aren't applied.

## Configure multi-network network policies

To use multi-network network policies, do the following:

  1. Create a cluster with [multi-network enabled GKE ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-a-gke-cluster).
  2. Create a [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-gke-node-pool) and a [Pod network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-pod-network).
  3. [Reference the Pod network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#reference-the-prepared-network).
  4. Create a network policy to be enforced that references the same Pod network utilized by the workload.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Create network policy

  1. To create a network policy that enforces rules on the same Pod network as your workload, reference the specific Pod network in the network policy definition.

  2. To define the selected ingress traffic rules and target Pods based on labels or other selectors, create a standard Network Policy.

Save the following sample manifest as `sample-ingress-network-policy1.yaml`:
         
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           name: sample-network-policy
           namespace: default
           annotations:
             networking.gke.io/network: blue-pod-network  # GKE-specific annotation for network selection
         spec:
           podSelector:
             matchLabels:
               app: test-app-2  # Selects pods with the label "app: test-app-2"
           policyTypes:
           - Ingress  # Specifies the policy applies only to incoming traffic
           ingress:
           - from:  # Allow incoming traffic only from...
             - podSelector:
                 matchLabels:
                   app: test-app-1  # ...pods with the label "app: test-app-1"
         

  3. Apply the `sample-ingress-network-policy1.yaml` manifest:
         
         kubectl apply -f sample-ingress-network-policy1.yaml
         

  4. To define the selected egress traffic rules and target Pods based on labels or other selectors, create a standard network policy.

Save the following sample manifest as `sample-egress-network-policy2.yaml`:
         
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           name: sample-network-policy-2
           namespace: default
           annotations:
             networking.gke.io/network: blue-pod-network  # GKE-specific annotation (optional)
         spec:
           podSelector:
             matchLabels:
               app: test-app-2
           policyTypes:
             - Egress  # Only applies to outgoing traffic
           egress:
             - to:
                 - podSelector:
                     matchLabels:
                       app: test-app-3
         

  5. Apply the `sample-egress-network-policy2.yaml` manifest:
         
         kubectl apply -f sample-egress-network-policy2.yaml
         




## Troubleshoot multi-network network policies

If you experience issues with network policies, whether they are applied to specific Pod networks or not, you can diagnose and troubleshoot the problem by running the following commands:

  1. `kubectl get networkpolicy`: lists all network policy objects and information about them.
  2. `iptables-save`: retrieves and lists all IP address tables chains for a particular node. You must run this command on the node as root.
  3. `cilium bpf policy get <endpoint-id>`: retrieves and lists allowed IP addresses from each endpoint's policy map.
  4. `cilium policy selectors`: prints out the [identities](https://docs.cilium.io/en/latest/gettingstarted/terminology/#identity) and the associated policies that have selected them.
  5. `cilium identity list`: shows mappings from identity to IP address.



## What's next

  * Read [About multi-network network policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-networking-policies)
  * Read [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-persistent-ip-addresses-on-gke-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
