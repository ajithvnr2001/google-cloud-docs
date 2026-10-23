---
url: https://docs.cloud.google.com/run/docs/configuring/networking-best-practices/
title: Best practices for Cloud Run networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:54:26.089324+00:00
---

# Best practices for Cloud Run networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/networking-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Best practices for Cloud Run networking Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the best practices for configuring networking options for Cloud Run resources. Before you create your resources, we recommend that you review all the sections on this page to understand the networking options that Cloud Run supports, as well as their implications.

**Best practices** :

Monitor IP address usage.  
Use non-RFC 1918 IP addresses.  
Use IPv4 and IPv6 (dual-stack) subnets.  
Use connection pooling and reuse connections.  
Faster external throughput to the internet.  
Faster internal throughput to a Google API.  


## Monitor IP address usage

If you're using Direct VPC egress, [make sure that you have enough IP addresses for your subnet](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#before_you_begin). The number of IP addresses you use depends on the number of instances that your workloads run, so we recommend monitoring your IP address usage. Be sure that your IP usage over time stays within the bounds supported by the subnet.

To estimate your IP address usage:

  1. In the Google Cloud console, go to the Cloud Monitoring Metrics explorer page:

[Go to Cloud Monitoring Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Look up the number of instances in your project by using the metric type [`run.googleapis.com/container/instance_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run). Cloud Monitoring lets you view this metric's value over time.

  3. Multiply the instance count metric's value by 2 to get an estimate of the number of IP addresses in use.




## IP address exhaustion strategies

Having a large number of Cloud Run workloads can cause IP exhaustion challenges when using the RFC 1918 private IP address space with Direct VPC egress. The following strategies can help you manage IP address exhaustion by using alternative IP address ranges.

### Use non-RFC 1918 IPv4 addresses

Aside from the RFC 1918 IPv4 address ranges, Cloud Run also supports [RFC 6598](https://datatracker.ietf.org/doc/html/rfc6598#section-7) and [Class E/RFC 5735](https://tools.ietf.org/html/rfc5735) ranges. All Google Cloud services and features work with these non-RFC 1918 ranges, including VPC networks, Cloud Load Balancing, and Private Service Connect.

For the best compatibility, we recommend starting with the RFC 6598 (100.64.0.0/10) range. If you're already using this range elsewhere, consider using Class E/RFC 5735 (240.0.0.0/4). Class E is a huge space with over 268 million IP addresses available, so it'll support your growth for a long time. However, Class E has some limitations. For example, it's not supported on Windows and on some on-premises hardware. Read about [leveraging Class E IPv4 Address space to mitigate IPv4 exhaustion issues in GKE](https://cloud.google.com/blog/products/containers-kubernetes/how-class-e-addresses-solve-for-ip-address-exhaustion-in-gke).

### Use Cloud NAT or Private Service Connect

If your Cloud Run workload using a non-RFC 1918 range needs to reach an on-premises destination that accepts only RFC 1918, use one of the following solutions:

  * Use [Hybrid NAT](https://docs.cloud.google.com/nat/docs/private-nat) to perform address translation and egress using a small RFC 1918 range.
  * Expose the on-premises service as a [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) hybrid service.



### Use IPv4 and IPv6 (dual-stack) subnets

Although it won't reduce IPv4 exhaustion, moving your apps to [IPv6](https://docs.cloud.google.com/vpc/docs/ipv6-support) is a good first step. [Set up dual-stack resources](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet) to avoid IPv4 exhaustion problems in the future.

## Port exhaustion reduction strategies

The following section describes strategies for reducing port exhaustion with Cloud Run.

### Use connection pooling and reuse connections

When sending a large number of requests to a single destination IP address, use connection pooling to maintain and reuse connections to the destination. High connection rates to a single IP address can exhaust outbound ports and cause connection refused errors.

## Performance and throughput strategies

This section covers scalable options for improving network performance and throughput towards the internet and Google services.

### Use the second generation execution environment

For the best networking performance for Cloud Run services, use the [second generation execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments) when routing traffic with Direct VPC egress. The second generation environment provides faster network performance, especially in the presence of packet loss.

You can [select the execution environment](https://docs.cloud.google.com/run/docs/configuring/execution-environments) using the Google Cloud console, gcloud CLI, YAML, or Terraform.

### Use Direct VPC egress for faster network egress throughput

To achieve faster throughput across network egress connections, use Direct VPC egress to route traffic through your VPC network. We recommend using this in conjunction with the second generation execution environment as noted previously.

#### Example 1: External traffic to the internet

If you're sending external traffic to the public internet, route all traffic through the VPC network by setting [`--vpc-egress=all-traffic`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress). With this approach, you must set up Cloud NAT to reach the public internet.

To enable Cloud Run to use a Cloud NAT gateway for Public NAT or Private NAT, see [Cloud NAT Direct VPC egress interactions](https://docs.cloud.google.com/nat/docs/nat-product-interactions#interactions-direct-vpc).

#### Example 2: Internal traffic to a Google API

If you're using Direct VPC egress to send traffic to a Google API, such as Cloud Storage, choose one of the following options:

  * Specify [`private-ranges-only`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress) (default) with [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access): 
    1. Set the flag `--vpc-egress=private-ranges-only`.
    2. Enable Private Google Access.
    3. [Configure DNS for Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain). Make sure your target domain (such as `storage.googleapis.com`) maps to one of the following internal IP address ranges: 
       * `199.36.153.8/30`
       * `199.36.153.4/30`
  * Specify [`all-traffic`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress) with [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access): 
    1. Set the flag `--vpc-egress=all-traffic`.
    2. Enable Private Google Access.



## Use the default MTU setting for Cloud Run

Don't change the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) setting of a VPC network when using it with Cloud Run. Use the default MTU of 1,460 bytes instead.

## Cost considerations

When configuring networking options for your resources, consider the following:

  * **Co-locate your resources** : Try to deploy your Cloud Run resources in the same region as your backend databases (like Cloud SQL or Firestore) and Cloud Storage buckets. Data transfer between Google Cloud resources within the same region is free.
  * **Switch to Direct VPC egress** : If you are securely routing traffic to internal VPC network resources, consider switching to [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) from Serverless VPC Access connectors. Direct VPC egress scales to zero, eliminating the baseline compute overhead and idle costs associated with connector instances.
  * **Use Cloud CDN** : Offload static assets and highly cacheable content by placing [Cloud CDN](https://docs.cloud.google.com/cdn/docs) in front of your Cloud Run resources. Serving data from the edge is significantly cheaper than paying for standard internet egress directly from Cloud Run.
  * **Monitor internet egress** : Inbound traffic (ingress) is always free, and you receive 1 GiB of free outbound internet data transfer per month within North America. Focus your monitoring efforts on outbound traffic that crosses region boundaries or exceeds the free tier.



Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information.

## What's next

  * [Compare Direct VPC egress and VPC connectors.](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc)
  * [Use tags for testing, traffic migration and rollbacks.](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
