---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-nat-packet-loss/
title: Troubleshoot Cloud NAT packet loss from a cluster \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:17.713406+00:00
---

# Troubleshoot Cloud NAT packet loss from a cluster  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-nat-packet-loss/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot Cloud NAT packet loss from a cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

In [VPC-native Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips), nodes without external IP addresses enhance security. These nodes use Cloud NAT for outbound internet connections. Packet loss can occur if a Node VM exhausts its allocated Cloud NAT ports and IP addresses, often under high outbound load, disrupting egress traffic.

Use this document to learn how to log and monitor for dropped packets, investigate your Cloud NAT configuration, and implement measures to reduce future packet loss.

This information is important for Platform admins and operators and Network administrators who manage GKE clusters with nodes without internet access and rely on Cloud NAT for external connectivity. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Diagnose packet loss

The following sections explains how to log dropped packets using Cloud Logging, and diagnose the cause of dropped packets using Cloud Monitoring.

### Log dropped packets

You can log dropped packets with the following query in Cloud Logging:
    
    
    resource.type="nat_gateway"
    resource.labels.region=REGION
    resource.labels.gateway_name=GATEWAY_NAME
    jsonPayload.allocation_status="DROPPED"
    

Replace the following:

  * `REGION`: the name of the region that the cluster is in.
  * `GATEWAY_NAME`: the name of the Cloud NAT gateway.



This command returns a list of all packets dropped by a Cloud NAT gateway, but does not identify the cause.

### Monitor causes for packet loss

To identify causes for dropped packets, query the [Metrics observer](https://console.cloud.google.com/monitoring/metrics-explorer) in Cloud Monitoring. Packets drop for one of three reasons:

  * `OUT_OF_RESOURCES`
  * `ENDPOINT_INDEPENDENT_CONFLICT`
  * `NAT_ALLOCATION_FAILED`



To identify packets dropped due to `OUT_OF_RESOURCES` or `ENDPOINT_ALLOCATION_FAILED` error codes, use the following query:
    
    
    fetch nat_gateway
      metric 'router.googleapis.com/nat/dropped_sent_packets_count'
      filter (resource.gateway_name == GATEWAY_NAME)
      align rate(1m)
      every 1m
      group_by [metric.reason],
        [value_dropped_sent_packets_count_aggregate:
           aggregate(value.dropped_sent_packets_count)]
    

If you identify packets that drop because of these reasons, see [Packets dropped with reason: out of resources](https://docs.cloud.google.com/nat/docs/troubleshooting#insufficient-ports) and [Packets dropped with reason: endpoint independent conflict](https://docs.cloud.google.com/nat/docs/troubleshooting#endpoint-independent-conflict) for troubleshooting advice.

To identify packets dropped due to the `NAT_ALLOCATION_FAILED` error code, use the following query:
    
    
    fetch nat_gateway
      metric 'router.googleapis.com/nat/nat_allocation_failed'
      group_by 1m,
        [value_nat_allocation_failed_count_true:
           count_true(value.nat_allocation_failed)]
      every 1m
    

If you identify packets that dropped for this reason, see [Need to allocate more IP addresses](https://docs.cloud.google.com/nat/docs/troubleshooting#allocate-more-IPs).

### Investigate Cloud NAT configuration

If the previous queries return empty results, and GKE Pods are unable to communicate to external IP addresses, use the following table to help you troubleshoot your configuration:

**Configuration** | **Troubleshooting**  
---|---  
Cloud NAT configured to apply only to the subnet's primary IP address range.  |  When Cloud NAT is configured only for the subnet's primary IP address range, packets sent from the cluster to external IP addresses must have a source node IP address. In this Cloud NAT configuration: 

  * Pods can send packets to external IP addresses if those external IP address destinations are subject to [IP masquerading](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent). When deploying the `ip-masq-agent`, verify that the `nonMasqueradeCIDRs` list doesn't contain the destination IP address and port. Packets sent to those destinations are first converted to source node IP addresses before being processed by Cloud NAT.
  * To allow the Pods to connect to all external IP addresses with this Cloud NAT configuration, ensure the `ip-masq-agent` is deployed and that the `nonMasqueradeCIDRs` list contains only the node and Pod IP address ranges of the cluster. Packets sent to destinations outside of the cluster are first converted to source node IP addresses before being processed by Cloud NAT.
  * To prevent Pods from sending packets to some external IP addresses, you need to explicitly block those addresses so they are not masqueraded. When the `ip-masq-agent` is deployed, add the external IP addresses you want to block to the `nonMasqueradeCIDRs` list. Packets sent to those destinations leave the node with their original Pod IP address sources. The Pod IP addresses come from a secondary IP address range of the cluster's subnet. In this configuration, Cloud NAT won't operate on that secondary range.

  
Cloud NAT configured to apply only to the subnet's secondary IP address range used for Pod IPs.  |  When Cloud NAT is configured only for the subnet's secondary IP address range used by the cluster's Pod IPs, packets sent from the cluster to external IP addresses must have a source Pod IP address. In this Cloud NAT configuration:

  * Using an [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent) causes packets to lose their source Pod IP address when processed by Cloud NAT. To keep the source Pod IP address, specify destination IP address ranges in a [`nonMasqueradeCIDRs`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) list. With the `ip-masq-agent` deployed, any packets sent to destinations on the `nonMasqueradeCIDRs`list retain their source Pod IP addresses before being processed by Cloud NAT.
  * To allow the Pods to connect to all external IP addresses with this Cloud NAT configuration, ensure the `ip-masq-agent` is deployed and that the `nonMasqueradeCIDRs` list is as large as possible (`0.0.0.0/0` specifies all IP address destinations). Packets sent to all destinations retain source Pod IP addresses before being processed by Cloud NAT.

  
  
## Reduce packet loss

After you have diagnosed the cause of your packet loss, consider using the following recommendations to reduce the likelihood of the issue from recurring in the future:

  * Configure the Cloud NAT gateway to use [dynamic port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#dynamic-port) and [increase the maximum number of ports per VM](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#change-dynamic-port).

  * If you're using [static port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#static-port), [increase the number of minimum ports per VM](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#change-min-port).

  * Reduce your application's outbound packet rate. When an application makes multiple outbound connections to the same destination IP address and port, it can quickly consume all connections Cloud NAT can make to that destination using the number of allocated NAT source addresses and source port tuples.

For details about how Cloud NAT uses NAT source addresses and source ports to make connections, including limits on the number of simultaneous connections to a destination, refer to [Ports and connections](https://docs.cloud.google.com/nat/docs/ports-and-addresses#ports-and-connections).

To reduce the rate of outbound connections from the application, reuse open connections. Common methods of reusing connections include connection pooling, multiplexing connections using protocols such as [HTTP/2](https://datatracker.ietf.org/doc/html/rfc7540), or establishing persistent connections reused for multiple requests. For more information, see [Ports and Connections](https://docs.cloud.google.com/nat/docs/ports-and-addresses#ports-and-connections).




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
