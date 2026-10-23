---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/cluster-dns/
title: Configure DNS for a cluster \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:22.717875+00:00
---

# Configure DNS for a cluster  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/cluster-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure DNS for a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to configure Domain Name System (DNS) provider options for Google Distributed Cloud. The DNS configuration for a cluster is held in a ClusterDNS custom resource named `default`. This resource is cluster-wide, which means that it isn't namespaced. The ClusterDNS custom resource applies to all cluster types.

## Create the ClusterDNS resource

Create a manifest for a ClusterDNS resource named `default`. Fill in the `spec` to configure the resource settings that you want. For example:
    
    
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
        - serverIP: 198.51.100.1
      - name: my-own-personal-domain.com
        nameservers:
        - serverIP: 203.0.113.1
        - serverIP: 203.0.113.2
          serverPort: 54
      googleAccess: default
    

To save the manifest to a file named `my-dns.yaml` and apply the resource to the cluster, run the following command:
    
    
    kubectl --kubeconfig KUBECONFIG apply -f my-dns.yaml

Replace `KUBECONFIG` with the path to the cluster kubeconfig file.

## View the ClusterDNS resource

To view the ClusterDNS resource, run the following command:
    
    
    kubectl --kubeconfig KUBECONFIG get clusterdns default --output yaml

Replace `KUBECONFIG` with the path to the cluster kubeconfig file.

## The ClusterDNS spec

The following sections describe the parts of the ClusterDNS custom resource definition you use to configure DNS for your clusters. You can update the ClusterDNS resource for a cluster at any time.

### `spec.upstreamNameservers`

Use the `spec.upstreamNameservers` field to specify your default upstream name servers with an array of objects. Each object has a server IP address and optionally a server port. The default value for the server port is 53. Requests for non-cluster domains are forwarded to this set of servers by default.

Here's an example `upstreamNameservers` configuration:
    
    
    spec:
      upstreamNameservers:
      - serverIP: 8.8.8.8
      - serverIP: 1.2.3.4
        serverPort: 54
    

If you don't specify any values for `upstreamNameservers`, then the DNS provider uses the `/etc/resolv.conf` file on the node to find the list of upstream name servers.

### `spec.domains`

Use the `spec.domains` field to configure different upstream name servers for particular domains. These domain-specific name server settings override the configuration in `upstreamNameservers`.

You can also turn on query logging for a domain. You can turn on query logging for any specified domain or the cluster domain, `cluster.local`.

Here's an example `spec.domains` configuration:
    
    
    spec:
      domains:
      - name: altostrat.com
        nameservers:
        - serverIP: 198.51.100.1
      - name: my-own-personal-domain.com
        nameservers:
        - serverIP: 203.0.113.1
        - serverIP: 203.0.113.2
          serverPort: 50000
      - name: cluster.local
        queryLogging: true
    

### `spec.googleAccess`

The `spec.googleAccess` field is a string that configures DNS resolution for domains used by global Google APIs and services. This field accepts the following values:

  * `default`: By default, DNS resolution maps global Google API domains to the default IP addresses. The cluster doesn't customize the DNS resolution for global Google API domains. For more information, see [IP addresses for the default domains](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip#ip-addr-defaults). If you don't specify a value in the `googleAccess` field, the system uses `default`.

  * `private`: maps DNS resolution for global Google API domains to the IP addresses used by `private.googleapis.com`.

  * `restricted`: maps DNS resolution for global Google API domains to the IP addresses used by `restricted.googleapis.com`.




The following example shows how to set DNS resolution to use `private.googleapis.com`:
    
    
    spec:
      googleAccess: private
    

For more information, see [Configure Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

### `spec.orderPolicy`

The `spec.orderPolicy` field is a string. Use this field to specify the ordering policy by which upstream servers are selected.

  * The default value is `random`.
  * Supported types are `random`,`round_robin`, and `sequential`.
  * This ordering policy applies to defined domains as well.



For more information about `policy` and what each configuration does, See the [coredns](https://coredns.io/plugins/forward/) documentation.

Here's an example `spec.orderPolicy` configuration:
    
    
    spec:
      orderPolicy: sequential
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
