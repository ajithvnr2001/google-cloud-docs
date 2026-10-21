---
url: https://docs.cloud.google.com/dns/docs/vpc-name-res-order/
title: Name resolution order \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:58.137276+00:00
---

# Name resolution order  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/vpc-name-res-order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Name resolution order Stay organized with collections  Save and categorize content based on your preferences. 

Cloud DNS uses the following procedure to answer queries from Compute Engine virtual machine (VM) instances and Google Kubernetes Engine (GKE) nodes.

For Compute Engine VMs other than GKE nodes, Cloud DNS follows the VPC network resolution order to process queries it receives. Each VM must be configured to use the metadata server IP address (`169.254.169.254`) as its name server.

For GKE nodes:

  1. Cloud DNS first attempts to match a query using cluster-scoped response policies and private zones.

  2. Cloud DNS continues by following the VPC network resolution order.




## Cluster-scoped response policies and private zones

  1. **Match using rules in GKE cluster-scoped response policies**. Cloud DNS scans all applicable GKE cluster-scoped response policies for a rule where the DNS name attribute matches as much of the query as possible. Cloud DNS uses longest-suffix matching to scan cluster-scoped response policies.

     1. If Cloud DNS finds a matching response policy rule _and_ the rule serves local data, then Cloud DNS returns the local data as its response, completing the name resolution process.

     2. If Cloud DNS finds a matching response policy rule _and_ the rule's behavior bypasses the response policy, then Cloud DNS continues to the next step.

     3. If Cloud DNS fails to find a matching response policy _or_ if there isn't an applicable cluster-scoped response policy for the node, then Cloud DNS continues to the next step.

  2. **Match records in cluster-scoped private zones**. Cloud DNS scans all cluster-scoped managed private zones for a record that matches as much of the query as possible. Cloud DNS uses longest-suffix matching to find records in cluster-scoped private zones.

     1. If the most specific match for the query is the zone name of a cluster-scoped private zone, Cloud DNS uses that zone's record data to resolve the request.

        * If the zone contains a record that exactly matches the query, Cloud DNS returns that record's data.
        * If the zone doesn't contain a matching record, Cloud DNS returns `NXDOMAIN`.
     2. If the most specific match for the query is the zone name of a cluster-scoped forwarding zone, then Cloud DNS forwards the query to one of the forwarding zone's forwarding targets to complete the name resolution process. Cloud DNS returns one of the following responses.

        * The response received from the forwarding target.
        * A `SERVFAIL` response, if the forwarding target doesn't respond to Cloud DNS.
     3. If the query doesn't match any cluster-scoped private zone, Cloud DNS continues to the VPC network resolution order.




## VPC network resolution order

  1. **Match using VPC network alternative name server**. If the VPC network has an [outbound server policy](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-out), Google Cloud forwards the query to one of the [alternative name servers](https://docs.cloud.google.com/dns/docs/server-policies-overview#altns-targets) defined in that policy to complete the name resolution process. 

If two or more alternative name servers exist in the outbound server policy, Cloud DNS ranks the alternative name servers using an internal algorithm. Beginning with equal ranks, alternative name servers increase in rank based on higher rates of successful responses (including `NXDOMAIN` responses) _and_ based on the shortest round-trip time (the lowest response latency).

Cloud DNS sends queries to alternative name servers and returns responses using the following process.

     * If two or more alternative name servers exist in the outbound server policy, Cloud DNS first sends the query to the highest-ranked alternative name server, then to the next-ranked alternative name server if Cloud DNS does _not_ receive _any_ response from the highest-ranked alternative name server. If Cloud DNS doesn't receive any response from the next-ranked alternative name server, Cloud DNS continues to query alternative name servers by descending rank until it exhausts the list of alternative name servers.

     * If Cloud DNS receives a response from an alternative name server, Cloud DNS returns that response. Responses include `NXDOMAIN` responses.

     * If Cloud DNS does _not_ receive a response from _all_ alternative name servers in the outbound server policy, Cloud DNS synthesizes a `SERVFAIL` response. To troubleshoot alternative name server connectivity, see [Alternative name server network requirements](https://docs.cloud.google.com/dns/docs/server-policies-overview#altns-net-req).

If the VPC network does _not_ have an outbound server policy, Cloud DNS continues to the next step.

  2. **Match using rules in VPC network-scoped response policies**. Cloud DNS scans all applicable VPC network response policies for a rule where the DNS name attribute matches as much of the query as possible. Cloud DNS uses longest-suffix matching to scan VPC network-scoped response policies.

     1. If Cloud DNS finds a matching response policy rule _and_ the rule serves local data, then Cloud DNS returns the local data as its response, completing the name resolution process.

     2. If Cloud DNS finds a matching response policy rule _and_ the rule's behavior bypasses the response policy, then Cloud DNS continues to the next step.

     3. If Cloud DNS fails to find a matching response policy _or_ if there isn't an applicable VPC network-scoped response policy for the VM or node, then Cloud DNS continues to the next step.

  3. **Match records in VPC network-scoped managed private zones**. Cloud DNS scans all managed private zones authorized for the VPC network for a record that matches as much of the query as possible. Cloud DNS uses longest-suffix matching to find records.

     1. If the most specific match for the query is the zone name of a VPC network-scoped private zone, Cloud DNS uses that zone's record data to resolve the request.

        * If the zone contains a record that exactly matches the query, Cloud DNS returns the record's data.
        * If the zone doesn't contain a matching record, Cloud DNS returns `NXDOMAIN`.
     2. If the most specific match for the query is the zone name of a VPC network-scoped forwarding zone, then Cloud DNS forwards the query to one of the forwarding zone's forwarding targets to complete the name resolution process. Cloud DNS returns one of the following responses.

        * The response received from the forwarding target.
        * A `SERVFAIL` response, if the forwarding target doesn't respond to Cloud DNS.
     3. If the most specific match for the query is the name of a VPC network-scoped peering zone, Cloud DNS stops the current name resolution process and begins a new name resolution process from the perspective of the peering zone's target VPC network.

If the query doesn't match a private zone, forwarding zone, or peering zone, Cloud DNS continues to the next step.

  4. **Match records in Compute Engine internal zones**. Cloud DNS scans all applicable [Compute Engine internal DNS zones](https://docs.cloud.google.com/compute/docs/internal-dns) for a record that matches as much of the query as possible. Cloud DNS uses longest-suffix matching to find records.

     1. If the most specific match for the query is a Compute Engine internal DNS name, Cloud DNS returns the internal IP address of the VM's network interface or its reverse lookup pointer as its response, completing the name resolution process.
  5. **Match record using public DNS query**. Google Cloud follows the start of authority (SOA) record to query publicly available zones, including Cloud DNS public zones. Cloud DNS returns one of the following responses.

     * The response received from an authoritative name server.
     * An `NXDOMAIN` response, if the record doesn't exist.



## Example

Suppose that you have two VPC networks, `vpc-a` and `vpc-b`, and a GKE cluster, `cluster-a`, along with the following scoped resources:

  1. `vpc-a` is authorized to query the following private zones. Note the trailing dot in each entry:

     * `static.example.com.`
     * `10.internal.`
  2. `peer.com.` is a peering zone that can query the VPC name resolution order of `vpc-b`.

  3. `vpc-a` is not associated with any outbound server or response policies.

  4. `cluster-a` is authorized to query a private zone called `example.com`. `cluster-a` is also not associated with any outbound server or response policies.

  5. A VM in `cluster-a` can query:

     * `example.com` and children (including `static.example.com`), answered by the private zone called `example.com`, authorized to `cluster-a`.
     * `10.internal` on `vpc-a`.
     * `peer.com` by using the peering zone.
  6. A VM that is _not_ in `cluster-a` can query:

     * `static.example.com` and children, answered by the private zone called `static.example.com` authorized to `vpc-a`. Queries for `example.com` return internet responses.
     * `10.internal` on `vpc-a`.
     * `peer.com` by using the peering zone.



## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).
  * To learn how to configure response policies, see [Manage response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
