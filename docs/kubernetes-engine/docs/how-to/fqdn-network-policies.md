---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies/
title: Control Pod egress traffic using FQDN network policies \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:28.526026+00:00
---

# Control Pod egress traffic using FQDN network policies  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Control Pod egress traffic using FQDN network policies Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to control egress communication between Pods and resources outside of the Google Kubernetes Engine (GKE) cluster using fully qualified domain names (FQDN). The custom resource that you use to configure FQDNs is the `FQDNNetworkPolicy` resource.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements and limitations

`FQDNNetworkPolicy` resources have the following requirements and limitations:

  * You must have a GKE cluster running one of the following versions: 
    * 1.26.4-gke.500 or later
    * 1.27.1-gke.400 or later
  * Your cluster must use [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#technical_specifications). 
    * You must use one of the DNS providers in your GKE cluster, kube-dns or Cloud DNS. Custom kube-dns or Core DNS deployments are not supported.
  * Google Cloud CLI version 462.0.0 or later.
  * Windows node pools are not supported.
  * Cloud Service Mesh is not supported.
  * If you have hard-coded IP addresses in your application, use the [`IPBlock` field of Kubernetes `NetworkPolicy`](https://kubernetes.io/docs/concepts/services-networking/network-policies/#networkpolicy-resource) instead of a `FQDNNetworkPolicy`.
  * Results returned by non-cluster DNS name servers such as alternate name servers in `resolv.conf` are not considered valid to be programmed in the allowlist in the GKE data plane.
  * The maximum number of IPv4 and IPv6 IP addresses that a `FQDNNetworkPolicy` can resolve to is 50.
  * You cannot allow traffic to a ClusterIP or Headless Service as an egress destination in a `FQDNNetworkPolicy` because GKE translates the Service virtual IP address (VIP) to backend Pod IP addresses before evaluating network policy rules. Instead, use a Kubernetes label-based `NetworkPolicy`.
  * There is a maximum quota of 100 IP addresses per hostname.
  * Inter-node transparent encryption is not supported with FQDN Network Policies.
  * FQDN network policies using the pattern match only match subdomains at the same level as the wild-card. For example, `pattern: *.company.com` matches `api.company.com` or `store.company.com`, but not `eu.api.company.com` or `company.com`.



## Enable FQDN Network Policy

You can enable FQDN Network Policy on a new or an existing cluster.

### Enable FQDN Network Policy in a new cluster

Create your cluster using the `--enable-fqdn-network-policy` flag:
    
    
    gcloud container clusters create CLUSTER_NAME  \
        --enable-fqdn-network-policy
    

Replace `CLUSTER_NAME` with the name of your cluster.

**Note:** You can only enable FQDN network policy by updating an existing Autopilot cluster. You can't enable this feature when you create a new Autopilot cluster.

### Enable FQDN Network Policy in an existing cluster

  1. For both Autopilot and Standard clusters, update the cluster using the `--enable-fqdn-network-policy` flag:
         
         gcloud container clusters update CLUSTER_NAME  \
             --enable-fqdn-network-policy
         

Replace `CLUSTER_NAME` with the name of your cluster.

**Note:** Updating the cluster and installing the FQDN network policy CRDs might take several minutes to complete. A regional GKE cluster takes more time to successfully update than a zonal cluster.
  2. For Standard clusters **only** , restart the GKE Dataplane V2 `anetd` DaemonSet:
         
         kubectl rollout restart ds -n kube-system anetd
         

**Note:** In Autopilot clusters, GKE control plane automatically restarts the nodes after enabling the FQDN Network Policy feature. It may take up to a few hours to trigger the node restart and for the new nodes to enforce policies. To verify that nodes were restarted, use the `kubectl get nodes` and check the `AGE` field of each node.



## Create a `FQDNNetworkPolicy`

  1. Save the following manifest as `fqdn-network-policy.yaml`:
         
         apiVersion: networking.gke.io/v1alpha1
         kind: FQDNNetworkPolicy
         metadata:
           name: allow-out-fqdnnp
         spec:
           podSelector:
             matchLabels:
               app: curl-client
           egress:
           - matches:
             - pattern: "*.yourdomain.com"
             - name: "www.google.com"
             ports:
             - protocol: "TCP"
               port: 443
         

This manifest has the following properties:

     * `name: www.google.com`: the fully qualified domain name. IP addresses provided by the name server associated with www.google.com are allowed. You must specify either `name` or `pattern`, or both.
     * `pattern: "*.yourdomain.com"`: IP addresses provided by name servers matching this pattern are allowed. You can use the following regular expressions for the pattern key: `^([a-zA-Z0-9*]([-a-zA-Z0-9_*]*[a-zA-Z0-9*])*\.?)*$`. Match criteria are additive. You can use multiple `pattern` fields. You must specify either `name` or `pattern`, or both.
     * `protocol: "TCP"` and `port: 443`: specifies a protocol and port. If a Pod tries to establish a connection to IP addresses using this protocol and port combination, the name resolution works, but the data plane blocks the outbound connection. This field is optional.
  2. Verify that the network policy is selecting your workloads:
         
         kubectl describe fqdnnp
         

The output is similar to the following:
         
         Name:         allow-out-fqdnnp
         Labels:       <none>
         Annotations:  <none>
         API Version:  networking.gke.io/v1alpha1
         Kind:         FQDNNetworkPolicy
         Metadata:
         ...
         Spec:
           Egress:
             Matches:
               Pattern:  *.yourdomain.com
               Name:     www.google.com
             Ports:
               Port:      443
               Protocol:  TCP
           Pod Selector:
             Match Labels:
               App: curl-client
         Events:     <none>
         




## Delete a `FQDNNetworkPolicy`

You can delete a `FQDNNetworkPolicy` using the `kubectl delete fqdnnp` command:
    
    
    kubectl delete fqdnnp FQDN_POLICY_NAME
    

Replace `FQDN_POLICY_NAME` with the name of your `FQDNNetworkPolicy`.

GKE deletes the rules from policy enforcement, but existing connections remain active until they close following the conntrack standard protocol guidelines.

## How FQDN network policies work

`FQDNNetworkPolicies` are egress-only policies which control which endpoints selected Pods can send traffic to. Similar to Kubernetes `NetworkPolicy`, a `FQDNNetworkPolicy` that selects a workload creates an implicit deny rule to endpoints not specified as allowed egress destinations. `FQDNNetworkPolicies` can be used with Kubernetes `NetworkPolicies` as described in FQDNNetworkPolicy and NetworkPolicy.

`FQDNNetworkPolicies` are enforced on the IP address and port level. They are not enforced using any Layer 7 protocol information (e.g. the `Request-URI` in a HTTP request). The specified domain names are translated to IP addresses using the DNS information provided by the GKE cluster's DNS provider.

### DNS requests

An active `FQDNNetworkPolicy` that selects workloads does not affect the ability of workloads to make DNS requests. Commands such as `nslookup` or `dig` work on any domains without being affected by the policy. However, subsequent requests to the IP address backing domains not in the allowist would be dropped.

For example, if a `FQDNNetworkPolicy` allows egress to `www.github.com`, then DNS requests for all domains are allowed but traffic sent to an IP address backing `twitter.com` is dropped.

### TTL expiration

`FQDNNetworkPolicy` honors the TTL provided by a DNS record. If a Pod attempts to contact an expired IP address after the TTL of the DNS record has elapsed, new connections are rejected. Long lived connections whose duration exceeds the TTL of the DNS record shouldn't experience traffic disruption while conntrack considers the connection still active.

### FQDNNetworkPolicy and NetworkPolicy

When both a `FQDNNetworkPolicy` and a `NetworkPolicy` apply to the same Pod, meaning the Pod's labels match what is configured in the policies, egress traffic is allowed as long as it matches one of the policies. There is no hierarchy between egress `NetworkPolicies` specifying IP addresses or label-selectors and `FQDNNetworkPolicies`.

### Shared IP Address Endpoints (Load Balancers, CDN, VPN Gateway, etc)

Many domains don't have dedicated IP addresses backing them and are instead exposed using shared IP addresses. This is especially common when the application is served by a Load Balancer or CDN. For example, Google Cloud APIs (`compute.googleapis.com`, `container.googleapis.com`, etc.) don't have unique IP addresses for each API. Instead all APIs are exposed using a shared range.

When configuring `FQDNNetworkPolicies`, it is important to consider whether the allowed domains are using dedicated IP addresses or shared IP addresses. Because `FQDNNetworkPolicies` are enforced at the IP address and port level, they can't distinguish between multiple domains served by the same IP address. Allowing access to a domain that is backed by a shared IP address will allow your Pod to communicate with all other domains served by that IP address. For example, allowing traffic to `compute.googleapis.com` will also allow the Pod to communicate with other Google Cloud APIs.

### CNAME Chasing

If the FQDN object in the `FQDNNetworkPolicy` includes a domain that has CNAMEs in the DNS record, you must configure your `FQDNNetworkPolicy` with all domain names that your Pod can query directly, including all potential aliases, in order to ensure a reliable `FQDNNetworkPolicy` behavior.

If your Pod queries `example.com`, then `example.com` is what you should write in the rule. Even if you get back a chain of aliases from your upstream DNS servers (e.g. `example.com` to `example.cdn.com` to `1.2.3.4`), the FQDN Network Policy will still allow your traffic through.

## Known Issues

This section lists all known issues for the fully qualified domain names (FQDN).

### Specifying `protocol: ALL` causes policy to be ignored

_This known issue has been fixed for GKE versions 1.27.10-gke.1055000+ and 1.28.3-gke.1055000+_

If you create a `FQDNNetworkPolicy` which specifies `protocol: ALL` in the `ports` section, GKE does not enforce the policy. This issue occurs because of an issue with parsing the policy. Specifying `TCP` or `UDP` does not cause this issue.

As a workaround, if you don't specify a `protocol` in the `ports` entry, the rule matches all protocols by default. Removing the `protocol: ALL` bypasses the parsing issue and GKE enforces the `FQDNNetworkPolicy`.

In GKE version 1.27.10-gke.1055000+ and 1.28.3-gke.1055000+, policies with `protocol: ALL` are correctly parsed and enforced.

### NetworkPolicy Logging causes incorrect or missing logs

_This known issue has been fixed for GKE versions 1.27.10-gke.1055000+ and 1.28.2-gke.1157000+_

If your cluster is using [Network Policy Logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) and FQDN network policies, there is a bug which can cause missing or incorrect log entries.

When using network policy logging _without delegate_ , the policy logs for DNS connections leaving a workload incorrectly claim that the traffic was dropped. The traffic itself was allowed (per the `FQDNNetworkPolicy`), but the logs were incorrect.

When using network policy logging _with delegation_ , policy logs are missing. The traffic itself is unaffected.

In GKE version 1.27.10-gke.105500+ and 1.28.2-gke.1157000+, this bug has been fixed. DNS connections will now be correctly logged as ALLOWED, when the traffic is selected by a `NetworkPolicy` or a `FQDNNetworkPolicy`.

## What's next

  * [Read the Kubernetes documentation about network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
  * [Use security insights to explore other ways to harden your infrastructure](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
