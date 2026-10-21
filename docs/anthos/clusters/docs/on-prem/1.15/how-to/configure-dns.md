---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-dns/
title: Configure DNS for a cluster \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:59.271359+00:00
---

# Configure DNS for a cluster  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-dns/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Configure DNS for a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/configure-dns)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/configure-dns)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to configure DNS for an admin cluster or user cluster.

The DNS configuration for a cluster is held in a ClusterDNS custom resource named `default`. This is a cluster-wide resource; that is, it is not namespaced.

## View the ClusterDNS resource

To view the ClusterDNS resource:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get clusterdns default --output yaml
    

Replace CLUSTER_KUBECONFIG with the path of the cluster kubeconfig file.

The DNS configuration is in the `spec` section. If the `spec` section is empty or missing, then the cluster uses a default Kubernetes CoreDNS configuration.

## Change the DNS configuration

Create a manifest for a ClusterDNS resource named `default`. Fill in the `spec` as desired. For example:
    
    
    apiVersion: networking.gke.io/v1alpha1
    kind: ClusterDNS
    metadata:
      name: default
    spec:
      upstreamNameservers:
      - serverIP: 8.8.8.8
      - serverIP: 8.8.4.4
      domains:
      - name: altostrat.com
        nameservers:
        - serverIP: 198.51.100.0.1
      - name: my-own-personal-domain.com
        nameservers:
        - serverIP: 203.0.113.1
        - serverIP: 203.0.113.2
          serverPort: 54
      googleAccess: private
    

Save the manifest to a file named `my-dns.yaml` and apply the resource to the cluster:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f my-dns.yaml
    

## The ClusterDNS spec

### `spec.upstreamNameservers`

An array of objects, each of which has a server IP address and optionally a server port. The default value for the server port is 53.

The default upstream name servers. Requests for non-cluster domains are forwarded to this set of servers by default. For example:
    
    
    spec:
      upstreamNameservers:
      - serverIP: 8.8.8.8
      - serverIP: 1.2.3.4
        serverPort: 54
    

If you do not specify any values for `upstreamNameservers`, then the DNS provider uses the `/etc/resolve.conf` file on the node to find the list of upstream name servers.

### `spec.domains`

Configuration for specific domains. This allows overriding of the configuration in `upstreamNameservers`.

You can use this section to configure different upstream name servers for particular domains, separately from the default upstream name servers.

You can also turn on query logging for a domain. You can do this for any specified domain or the cluster domain, cluster.local.

For example:
    
    
    spec:
      domains:
      - name: altostrat.com
        nameservers:
        - serverIP: 203.0.113.1
      - name: my-own-personal-domain.com
        nameservers:
        - serverIP: 198.51.100.1
        - serverIP: 198.51.100.2
          serverPort: 50000
      - name: cluster.local
        queryLogging: true
    

### `spec.googleAccess`

String. If you want Google domains to resolve to private-access IP addresses, set this to `"private"`. If you want Google domains to resolve to restricted-access IP addresses, set this to `restricted`. If you want no special treatment for Google domains, set this to `default` or remove it. For more information, see [Configuring Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

For example:
    
    
    spec:
      googleAccess: private
    

### `spec.orderPolicy`

String. If you want to specify the ordering policy by which upstream servers are selected. Default is `"random"`. Supported types are `"random"`,`"round_robin"` and `"sequential"`. Note that this ordering policy will apply to defined domains as well. See the [coredns](https://coredns.io/plugins/forward/) docs for more info about `policy` and what each configuration does.

For example: 
    
    
    spec:
      orderPolicy: sequential
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
