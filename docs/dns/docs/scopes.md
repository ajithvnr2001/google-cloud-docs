---
url: https://docs.cloud.google.com/dns/docs/scopes/
title: Scopes and hierarchies \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:48.845339+00:00
---

# Scopes and hierarchies  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/scopes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Scopes and hierarchies Stay organized with collections  Save and categorize content based on your preferences. 

Cloud DNS scopes are a flexible way of attaching private DNS resources to Google Cloud objects. Originally, you could only attach private DNS resources such as private DNS zones, policies, and peering zones to Virtual Private Cloud (VPC) networks. By using DNS scopes, you can attach resources not only to multiple Google Cloud networks, but also to a smaller grouping, such as a Google Kubernetes Engine (GKE) cluster. Instead of attaching private DNS resources to networks, you can attach private DNS resources to scopes.

Cloud DNS scopes let you attach a private DNS resource to a VPC network and a GKE cluster. Within the boundaries of a particular scope, like in a network, you can create a custom view of DNS. For example, multiple GKE clusters in a single network can have their own `cluster.local` DNS hierarchy.

You can create a VPC-scoped or a GKE cluster-scoped DNS zone depending on whether you want DNS names to be visible to the entire VPC network or limit them to a GKE cluster:

  * **VPC scope**. Use this scope when DNS names have to be resolved VPC network-wide. A VPC-scoped DNS zone lets DNS names be available globally to the entire VPC network.

  * **GKE cluster scope**. Cloud DNS lets you create a scope for a single GKE cluster. You can then create one or more private managed zones for each cluster, just like you can for networks. Queries from within that cluster first check to see if the query can be answered by a resource scoped to that specific GKE cluster. If not, queries fall back to normal matching, which starts by checking if the query can be answered by any network-scoped resources.




## Scopes hierarchy

DNS resolution occurs at the most specific scope available, walking up the hierarchy when a zone is not found in a lower scope. The cluster is the most specific scope, and Cloud DNS checks it first for a match.

Scopes also let [managed zones](https://docs.cloud.google.com/dns/docs/key-terms#dns-managed-zones) and [response policies](https://docs.cloud.google.com/dns/docs/key-terms#response-policy) bind to one or more selectors within the same scope (when applicable). You can configure a network and a scope to bind in the following ways:

  * Between multiple networks
  * Between a GKE cluster and a network
  * Between multiple networks and multiple GKE clusters



After you bind a managed zone or response policy to a selector, it is visible to clients within the scope.

To learn how to configure a cluster-scoped Cloud DNS zone, see [Configure a GKE cluster scope](https://docs.cloud.google.com/dns/docs/zones/configure-scopes).

## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To learn more about Cloud DNS response policies, see [Manage response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies).
  * To learn more about zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
