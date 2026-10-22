---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern/
title: Cloud bursting pattern \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:07.000534+00:00
---

# Cloud bursting pattern  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Cloud bursting pattern Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

Internet applications can experience extreme fluctuations in usage. While most enterprise applications don't face this challenge, many enterprises must deal with a different kind of bursty workload: batch or CI/CD jobs.

This architecture pattern relies on a redundant deployment of applications across multiple computing environments. The goal is to increase capacity, resiliency, or both.

While you can accommodate bursty workloads in a data-center-based computing environment by overprovisioning resources, this approach might not be cost effective. With batch jobs, you can optimize use by stretching their execution over longer time periods, although delaying jobs isn't practical if they're time sensitive.

The idea of the _cloud bursting_ pattern is to use a private computing environment for the baseline load and burst to the cloud temporarily when you need extra capacity.

![Data flowing from an on-premises environment to Google Cloud in burst mode.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/cloud-bursting.svg)

In the preceding diagram, when data capacity is at its limit in an on-premises private environment, the system can gain extra capacity from a Google Cloud environment when needed.

The key drivers of this pattern are saving money and reducing the time and effort needed to respond to scale requirement changes. With this approach, you only pay for the resources used when handling extra loads. That means you don't need to overprovision your infrastructure. Instead you can take advantage of on-demand cloud resources and scale them to fit the demand, and any predefined metrics. As a result, your company might avoid service interruptions during peak demand times.

A potential requirement for cloud bursting scenarios is workload portability. When you allow workloads to be deployed to multiple environments, you must abstract away the differences between the environments. For example, Kubernetes gives you the ability to achieve consistency at the workload level across diverse environments that use different infrastructures. For more information, see [Google Kubernetes Engine (GKE) hybrid environment reference architecture](https://docs.cloud.google.com/anthos/docs/architecture/anthos-hybrid-environment).

## Design considerations

The cloud bursting pattern applies to interactive and batch workloads. When you're dealing with interactive workloads, however, you must determine how to distribute requests across environments:

  * You can route incoming user requests to a load balancer that runs in the existing data center, and then have the load balancer distribute requests across the local and cloud resources.

This approach requires the load balancer or another system that is running in the existing data center to also track the resources that are allocated in the cloud. The load balancer or another system must also initiate the automatic upscaling or downscaling of resources. Using this approach you can decommission all cloud resources during times of low activity. However, implementing mechanisms to track resources might exceed the capabilities of your load balancer solutions, and therefore increase overall complexity.

  * Instead of implementing mechanisms to track resources, you can use Cloud Load Balancing with a hybrid connectivity [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts) backend. You use this load balancer to route [internal client requests](https://docs.cloud.google.com/load-balancing/docs/l7-internal#load_balancing_with_hybrid_connectivity) or [external client requests](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#public_clients) to backends that are located both on-premises and in Google Cloud and that are based on different metrics, like [weight-based traffic splitting](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global#traffic_actions_weight-based_traffic_splitting). Also you can scale backends based on [load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing#scaling_based_on_https_load_balancing_serving_capacity) for workloads in Google Cloud. For more information, see [Traffic management overview for global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).

This approach has several additional benefits, such as taking advantage of Google Cloud Armor [DDoS protection capabilities](https://docs.cloud.google.com/armor/docs/advanced-network-ddos), WAF, and caching content at the cloud edge using [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview). However, you need to size the hybrid network connectivity to handle the additional traffic.

  * As highlighted in [Workload portability](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/other-considerations#workload_portability), an application might be portable to a different environment with minimal changes to achieve workload consistency, but that doesn't mean that the application performs equally the same in both environments. Differences in underlying compute, infrastructure security capabilities, or networking infrastructure, along with proximity to dependent services, typically determine performance. Through testing, you can have more accurate visibility and understand the performance expectations.

  * You can use cloud infrastructure services to build an environment to host your applications without portability. Use the following approaches to handle client requests when traffic is redirected during peak demand times:

    * Use consistent tooling to monitor and manage these two environments.
    * Ensure consistent workload versioning and that your data sources are current.
    * You might need to add automation to provision the cloud environment and reroute traffic when demand increases and the cloud workload is expected to accept client requests for your application.
  * If you intend to shut down all Google Cloud resources during times of low demand, using DNS routing policies primarily for traffic load balancing might not always be optimal. This is mainly because:

    * Resources can require some time to initialize before they can serve users.
    * DNS updates tend to propagate slowly over the internet.

As a result:

    * Users might be routed to the Cloud environment even when no resources are available to process their requests.
    * Users might keep being routed to the on-premises environment temporarily while DNS updates propagate across the internet.



With Cloud DNS, you can choose the [DNS policy and routing policy](https://docs.cloud.google.com/dns/docs/policies-overview) that align with your solution architecture and behavior, such as geolocation DNS routing policies. Cloud DNS also supports health checks for internal passthrough Network Load Balancer, and internal Application Load Balancer. In which case, you could incorporate it with your overall hybrid DNS setup that's based on this pattern.

In some scenarios, you can use Cloud DNS to distribute client requests with health checks on Google Cloud, like when using internal Application Load Balancers or [cross-region internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal#high_availability_and_cross-region_failover). In this scenario, Cloud DNS checks the overall health of the internal Application Load Balancer, which itself checks the health of the backend instances. For more information, see [Manage DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/zones/manage-routing-policies).

You can also use [Cloud DNS split horizon](https://docs.cloud.google.com/dns/docs/zones/zones-overview#split-horizon). Cloud DNS split horizon is an approach for setting up DNS responses or records to the specific location or network of the DNS query originator for the same domain name. This approach is commonly used to address requirements where an application is designed to offer both a private and a public experience, each with unique features. The approach also helps to distribute traffic load across environments.

Given these considerations, cloud bursting generally lends itself better to batch workloads than to interactive workloads.

## Advantages

Key advantages of the cloud bursting architecture pattern include:

  * Cloud bursting lets you reuse existing investments in data centers and private computing environments. This reuse can either be permanent or in effect until existing equipment becomes due for replacement, at which point you might consider a full migration.
  * Because you no longer have to maintain excess capacity to satisfy peak demands, you might be able to increase the use and cost effectiveness of your private computing environments.
  * Cloud bursting lets you run batch jobs in a timely fashion without the need for overprovisioning compute resources.



## Best practices

When implementing cloud bursting, consider the following best practices:

  * To ensure that workloads running in the cloud can access resources in the same fashion as workloads running in an on-premises environment, use the [_meshed_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern) with the least privileged security access principle. If the workload design permits it, you can allow access only from the cloud to the on-premises computing environment, not the other way round.
  * To minimize latency for communication between environments, pick a [Google Cloud region](https://cloud.google.com/about/locations) that is geographically close to your private computing environment. For more information, see [Best practices for Compute Engine regions selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection).
  * When using cloud bursting for batch workloads only, reduce the security attack surface by keeping all Google Cloud resources private. Disallow any direct access from the internet to these resources, even if you're using Google Cloud external load balancing to provide the entry point to the workload.
  * Select the [DNS policy and routing policy](https://docs.cloud.google.com/dns/docs/policies-overview) that aligns with your architecture pattern and the targeted solution behavior.

    * As part of this pattern, you can apply the design of your DNS policies permanently or when you need extra capacity using another environment during peak demand times.
    * You can use geolocation DNS routing policies to have a global DNS endpoint for your regional load balancers. This tactic has many use cases for geolocation DNS routing policies, including hybrid applications that use Google Cloud alongside an on-premises deployment where Google Cloud region exists.
    * If you need to provide different records for the same DNS queries, you can use split horizon DNS—for example, queries from internal and external clients.

For more information, see [reference architectures for hybrid DNS](https://docs.cloud.google.com/dns/docs/best-practices#reference_architectures_for_hybrid_dns)

  * To ensure that DNS changes are propagated quickly, configure your DNS with a reasonably short [time to live value](https://docs.cloud.google.com/dns/docs/overview#propagation_of_changes) so that you can reroute users to standby systems when you need extra capacity using cloud environments.

  * For jobs that aren't highly time critical, and don't store data locally, consider using [Spot VM instances](https://docs.cloud.google.com/compute/docs/instances/spot), which are substantially cheaper than regular VM instances. A prerequisite, however, is that if the VM job is preempted, the system must be able to automatically restart the job.

  * Use containers to achieve workload portability where applicable. Also, GKE can be a key enabling technology for that design. For more information, see [GKE hybrid environment reference architecture](https://docs.cloud.google.com/anthos/docs/architecture/anthos-hybrid-environment).

  * Monitor any traffic sent from Google Cloud to a different computing environment. This traffic is subject to [outbound data transfer charges](https://cloud.google.com/vpc/network-pricing#internet_egress).

  * If you plan to use this architecture long term with high outbound data transfer volume, consider using Cloud Interconnect. Cloud Interconnect can help to optimize the connectivity performance and might reduce outbound data transfer charges for traffic that meets certain conditions. For more information, see [Cloud Interconnect pricing](https://cloud.google.com/network-connectivity/docs/interconnect/pricing).

  * When Cloud Load Balancing is used, you should use its [application capacity optimizations abilities ](https://docs.cloud.google.com/load-balancing/docs/tutorials/about-capacity-optimization-with-global-lb)where applicable. Doing so can help you address some of the capacity challenges that can occur in globally distributed applications.

  * Authenticate the people who use your systems by [establishing common identity](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment) between environments so that systems can securely authenticate across environment boundaries.

  * To protect sensitive information, encrypting all communications in transit is highly recommended. If encryption is required at the connectivity layer, various options are available based on the selected hybrid connectivity solution. These options include VPN tunnels, HA VPN over Cloud Interconnect, and MACsec for Cloud Interconnect.




[ Previous arrow_back  Business continuity hybrid and multicloud patterns  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/business-continuity-patterns)

[ Next What's next  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/whats-next)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
