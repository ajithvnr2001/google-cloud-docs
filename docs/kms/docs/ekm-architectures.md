---
url: https://docs.cloud.google.com/kms/docs/ekm-architectures/
title: Reference architectures for Cloud External Key Manager \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:34.852352+00:00
---

# Reference architectures for Cloud External Key Manager  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/ekm-architectures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Reference architectures for Cloud External Key Manager Stay organized with collections  Save and categorize content based on your preferences. 

When you enable Cloud Key Management Service (Cloud KMS) with [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm), you can use keys that you manage with an external key management partner to help protect data in Google Cloud. This document describes architectures for Google Cloud customers who want to deploy a highly available external key manager (EKM) service with Cloud KMS and Cloud EKM.

Using Cloud EKM with your EKM service involves an explicit risk tradeoff between cloud workload reliability and data protection controls. Encrypting data-at-rest in the cloud with off-cloud encryption keys adds new failure risks that might result in Google Cloud services data becoming inaccessible. To address these risks, you must incorporate high availability and fault tolerance into the Cloud EKM architecture.

## Overview

Cloud EKM lets you use key material that remains outside of Google Cloud to control access to your data that is stored in [supported Google Cloud services](https://docs.cloud.google.com/kms/docs/compatible-services#cmek_integrations). Cloud EKM keys are [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek). Cloud EKM lets you create and manage Cloud KMS key resources using the `EXTERNAL` and `EXTERNAL_VPC` protection levels. When you enable Cloud EKM, every cryptographic operation request results in a cryptographic operation on the external key. The success of the initial request operation critically depends on the result of the cryptographic operation on the external key.

Cloud KMS requests operations on external keys using a [special-purpose API](https://docs.cloud.google.com/kms/docs/reference/rest) that integrates with your external key management system. This document refers to a service that provides this API as an _EKM service_.

If an EKM service becomes unavailable, reads and writes from the data planes for integrated Google Cloud services might fail. These failures appear in a similar way as failures do when the dependent Cloud KMS key is in an unusable state, for example, when it is disabled. The error message describes the source of the error and a course of action. Furthermore, Cloud KMS data access audit logs include a record of these error messages together with descriptive error types. For more information, see [Cloud EKM error reference](https://docs.cloud.google.com/kms/docs/reference/ekm_errors).

## Best practices for Cloud EKM architectures

Google's [Site Reliability Engineering book](https://sre.google/sre-book/table-of-contents/) describes best practices to help guide the development and maintenance of reliable systems. This section describes some of these practices in the context of how your EKM service integrates with Google Cloud. The following best practices apply to the Cloud EKM reference architectures:

  * Configure low latency, reliable network connectivity
  * Enable high availability
  * Detect and mitigate failures quickly



### Configure low-latency, reliable network connectivity

Cloud KMS connects to EKM services using a Virtual Private Cloud (VPC) network or the internet. VPC solutions often use [hybrid connectivity](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product) to host the EKM service in an on-premises data center. The connection between Google Cloud and the data center must be fast and reliable. When using the internet, you require stable, uninterrupted reachability and fast, reliable DNS resolution. From the point of view of Google Cloud, any interruption can result in the unavailability of the EKM service and the potential inability to access EKM-protected data.

When a Google Cloud service's data plane communicates with the EKM service, each EKM service-bound call has a defined timeout period (150 milliseconds). The timeout is measured from the Cloud KMS service in the Google Cloud location of the Cloud KMS key. If the Google Cloud location is a multi-region, then the timeout begins in the region where Cloud KMS receives the request, which is typically where the operation on the CMEK-protected data resource occurred. This timeout is adequate to allow an EKM service to handle requests in a nearby Google Cloud region that the requests originate from.

The timeout helps prevent cascading failures in downstream services that depend on the external key. Tail latency issues that might normally cause a poor user experience in higher level applications can actually manifest as failed accesses to the external key resulting in the failure of the higher-level logical operation.

To minimize latency and create reliable networks, consider the following:

  * **Minimize latency of round-trip communication with Cloud KMS:** Configure the EKM service to serve requests as geographically close as possible to the Google Cloud locations that correspond to the Cloud KMS keys that are configured to use the EKM service. For more information, see [Best practices for Compute Engine regions selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection) and [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * **Use Cloud Interconnect when possible:** [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) creates a highly available, low-latency connection between Google Cloud and your data center using a VPC network and helps remove dependencies on the internet.
  * **Deploy Google Cloud networking solutions in the region closest to the EKM service, when necessary:** Ideally, Cloud KMS keys are stored in the region that is closest to the EKM service. If there is a Google Cloud region that is closer to the EKM service than the region holding the Cloud KMS keys, use Google Cloud networking solutions, such as [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview), in the region closest to the EKM service. This option helps ensure that network traffic uses Google infrastructure when possible, which reduces dependence on the internet.
  * **Use Premium Tier networks when EKM traffic transits through the internet:** [Premium Tier](https://docs.cloud.google.com/network-tiers) routes traffic through the internet using Google's infrastructure where possible to improve reliability and reduce latency.
  * **Use an appropriate client deadline:** If you call the Cloud KMS API API directly for Cloud EKM keys, configure a client deadline of at least 10 seconds to allow sufficient time for external key operations to complete.



### Enable high availability

The existence of a single point of failure in the EKM service reduces the availability of dependent Google Cloud resources to that of the single point of failure. Such points of failure might live in critical dependencies of the EKM service as well as the underlying compute and network infrastructure.

To enable high availability, consider the following:

  * **Deploy replicas across independent failure domains:** Deploy at least two replicas of the EKM service. If you're using multi-regional Google Cloud locations, deploy EKM in a minimum of two separate geographical locations with a minimum of two replicas each. Ensure that each replica doesn't only represent a replicated data plane of the EKM service by minimizing and hardening the cross-replica failure vectors. Consider the following examples: 
    * Configure production changes, including server binary and configuration pushes, to modify only one replica at a time. Verify that all changes are carried out under supervision, with tested rollbacks readily available.
    * Understand and minimize the cross-replica failure modes from the underlying infrastructure. For example, ensure that replicas depend on independent and redundant power feeds.
  * **Make replicas resilient to single machine outages:** Verify that each replica of the service consists of at least three appliances, machines, or VM hosts. This configuration lets the system serve traffic while one machine is down for updates or during an unexpected outage (N+2 provisioning). 

**Note:** External keys in a Cloud KMS multi-regional location must use the internet because the EKM service can't access multi-regional locations using Virtual Private Cloud. For more information, see [External key managers and regions](https://docs.cloud.google.com/kms/docs/ekm#regions).
  * **Limit the affected area of control plane issues:** Configure the control plane (for example, key creation or deletion) of the EKM service to replicate configuration or data across replicas. These operations are generally more complex because these operations require synchronization and affect all replicas. Issues can quickly propagate to affect the entire system. Some strategies to reduce the impact of issues include the following:

    * **Control propagation speed:** By default, ensure that changes propagate as slowly as is acceptable for usability and security. Set up exceptions where necessary—for example, when permitting access to a key to propagate quickly to let a user undo a mistake.
    * **Partition the system into shards:** If many users share the EKM, partition them into logical shards that are completely independent, so that issues triggered by a user in one shard cannot affect users in another.
    * **Preview the effect of changes:** If possible, let users see the effect of changes before applying them. For example, when modifying a key access policy, the EKM could confirm the number of recent requests that would have been rejected under the new policy.
    * **Implement data canarying:** First push data only to a small subset of the system. If the subset remains healthy, push the data to the rest of the system.
  * **Implement holistic health checks:** Create health checks that measure whether the full system is functioning. For example, health checks that only validate network connectivity are not helpful in responding to many application-level issues. Ideally, the health check closely mirrors the dependencies for real traffic.

  * **Set up failover across replicas:** Set up load balancing in your EKM service components such that it consumes the health checks and actively drains traffic from unhealthy replicas and safely fails over to healthy replicas.

  * **Include safety mechanisms to manage overload and avoid cascading failures:** Systems might become overloaded for a variety of reasons. For example, when some replicas become unhealthy, traffic redirected to the healthy replicas could overload them. When faced with more requests than it can serve, the system should attempt to serve what it can safely and quickly, while rejecting excess traffic.

  * **Ensure a robust durability story:** Data in Google Cloud that is encrypted with an external key in the EKM service is unrecoverable without the external key. Therefore, key durability is one of the central design requirements of the EKM service. Configure the EKM service to securely back up redundant copies of key material in multiple physical locations. Configure additional protection measures, such as offline backups, for high value keys. Ensure that your deletion mechanisms permit time for recovery in cases of accidents and bugs.




### Detect and mitigate failures quickly

For every minute the EKM service suffers an outage, dependent Google Cloud resources might be inaccessible, which can further increase the likelihood of a cascading failure of other dependent components of your infrastructure.

To detect and mitigate failures quickly, consider the following:

  * **Configure the EKM service to report metrics that signal reliability-threatening incidents:** Set up metrics such as response error rates and response latencies to catch issues quickly.
  * **Set up operational practices for timely notification and mitigation of incidents:** Quantify the effectiveness of operational practices by tracking the mean time to detect (MTTD) and mean time to restore (MTTR) metrics, and define objectives that are measured by these metrics. Using these metrics, you can find patterns and deficiencies in the current processes and systems so that you can quickly respond to incidents.



## Reference architectures for Cloud EKM

The following architectures describe a few ways to deploy the EKM service using Google Cloud networking and load balancing products.

### Direct connection over Cloud VPN or Cloud Interconnect

A direct connection between Google Cloud and your on-premises data center is recommended when you are running high-throughput applications on Google Cloud and the EKM service runs in a single data center. The following diagram shows this architecture.

![Architecture for a direct connection over Cloud VPN or Cloud Interconnect.](https://docs.cloud.google.com/static/kms/images/cloudekm-direct-connect.svg)

In this architecture, Cloud EKM accesses the EKM service located in an on-premises data center through [hybrid connectivity](https://cloud.google.com/hybrid-connectivity) in the region without any intermediate load balancing in Google Cloud.

When possible, deploy the Cloud EKM to EKM service connection using the [99.9% availability configuration for single region applications](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/non-critical-overview). The [99.99% availability configuration](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview) requires using Cloud Interconnect in multiple Google Cloud regions, which might not meet your needs if your business requires regional isolation. If the connection to the on-premises data center uses the internet, use [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) instead of Cloud Interconnect.

The primary advantage of this architecture is that there are no intermediate hops in Google Cloud, which reduces latency and potential bottlenecks. If you want to set up a direct connection when your EKM service is hosted across multiple data centers, you must configure load balancers in all data centers that use the same (anycast) IP address. If you use this configuration, load balancing and failover among data centers is limited to route availability only.

If you set up a VPC network, external keys accessed over the VPC network must use a regional location in Cloud KMS. The keys cannot use a multi-regional location. For more information, see [External key managers and regions](https://docs.cloud.google.com/kms/docs/ekm#regions).

### Load balanced from internet in Google Cloud

Using a load-balancer in Google Cloud with an internet connection is recommended when you require multi-regional Cloud KMS keys. The following diagram shows this architecture.

![Architecture for a load-balanced connection from the internet.](https://docs.cloud.google.com/static/kms/images/cloudekm-internet-loadbalanced.svg)

In this architecture, the EKM has replicas in two on-premises sites. Each backend is represented in Google Cloud using a [hybrid connectivity network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs#hybrid-neg). The deployment uses an [external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp) to forward traffic directly to one of the replicas. Unlike the other approaches, which rely on VPC networking, the external proxy Network Load Balancer has an external IP address, and traffic comes from the internet.

Each hybrid connectivity NEG might contain multiple IP addresses, which allows the external proxy Network Load Balancer to balance traffic directly to instances of the EKM service. An additional load balancer in the on-premises data center isn't necessary.

The external proxy Network Load Balancer isn't tied to a specific region. It can direct incoming traffic to the nearest healthy region, which makes it suitable for multi-regional Cloud KMS keys. However, the load balancer doesn't allow configuration of primary and failover backends. Traffic is distributed evenly across multiple backends in a region.

### Load balanced in a VPC network in Google Cloud

Using a load-balancer in Google Cloud with a VPC network is recommended for most EKM services where you deploy your EKM. The following diagram shows this architecture.

![Architecture for a load-balanced connection from a VPC network.](https://docs.cloud.google.com/static/kms/images/cloudekm-vpc-loadbalanced.svg)

In this architecture, Cloud EKM accesses the EKM service that is replicated between two on-premises data centers through [hybrid connectivity](https://cloud.google.com/hybrid-connectivity) with layers of intermediate load balancing in the Google Cloud region. If the connection to the on-premises data center uses the internet, you can use [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) instead of Cloud Interconnect.

The [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) provides a single IP address that resources can use to send traffic using [virtual networking](https://docs.cloud.google.com/load-balancing/docs/internal#how_ilb_works). The load balancer [fails over](https://docs.cloud.google.com/load-balancing/docs/internal#failover) to the backup data center based on the [health](https://docs.cloud.google.com/load-balancing/docs/internal#health-checking) of the backends.

The [VM instance group](https://docs.cloud.google.com/compute/docs/instance-groups) is necessary to proxy traffic, because the internal load balancer cannot route traffic directly to on-premises backends. You can deploy load balancer proxies to run Nginx Docker images from [Cloud Marketplace](https://console.cloud.google.com/marketplace/product/google/nginx1) in instance groups. You can use Nginx as a [TCP load balancer](https://docs.nginx.com/nginx/admin-guide/load-balancer/tcp-udp-load-balancer/).

Because this approach uses load balancers in Google Cloud, you don't require an on-premises load balancer. The Google Cloud load balancers can connect directly to instances of the EKM service and balance the load among them. Eliminating the on-premises load balancer results in simpler configuration but reduces the flexibility that is available in the EKM service. For example, an on-premises L7 load balancer could automatically retry requests if one EKM instance returns an error.

If you set up a VPC network, external keys accessed over the VPC network must use a regional location in Cloud KMS. The keys cannot use a multi-regional location. For more information, see [External key managers and regions](https://docs.cloud.google.com/kms/docs/ekm#regions).

### Reference architecture comparison

The following table compares the reference architecture options for Cloud EKM. The table also includes a column for [partner-managed EKM architecture](https://docs.cloud.google.com/kms/docs/ekm#partner-managed). In this scenario, the partner is responsible for deploying and managing the EKM and provides the EKM as a service to customers.

Option | Direct connection | Load balanced from internet | Load balanced in a VPC network | Fully-managed EKM provided by partner  
---|---|---|---|---  
Internet or VPC network | VPC | Internet | VPC | Internet  
Load balancer in Google Cloud | No | Yes | Yes | No  
On-premises load balancer required | Yes | No | No | Yes (managed by partner)  
Supports multi-regional Cloud KMS locations | No | Yes | No | Yes  
Recommended for | High throughput applications where the EKM service runs in a single site. | When multi-regional Cloud KMS keys are required. | Most EKM services where you deploy your own EKM. | You can use a partner's EKM instead of deploying your own.  
  
## What's next

  * Read more about [Cloud KMS security](https://docs.cloud.google.com/docs/security/key-management-deep-dive).
  * [Create an EKM connection over a VPC network](https://docs.cloud.google.com/kms/docs/create-ekm-connection).
  * [Set up Cloud EKM over the internet](https://docs.cloud.google.com/kms/docs/set-up-ekm-internet).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
