---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern/
title: Partitioned multicloud pattern \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:45.580891+00:00
---

# Partitioned multicloud pattern  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Partitioned multicloud pattern Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The _partitioned multicloud_ architecture pattern combines multiple public cloud environments that are operated by different cloud service providers. This architecture provides the flexibility to deploy an application in an optimal computing environment that accounts for the multicloud drivers and considerations discussed in the first part of this series.

The following diagram shows a partitioned multicloud architecture pattern.

![Data flow from an application in Google Cloud to an application in a different cloud environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/partitioned.svg)

This architecture pattern can be built in two different ways. The first approach is based on deploying the application components in different public cloud environments. This approach is also referred to as a [composite architecture](https://services.google.com/fh/files/misc/google-cloud-oci-guide.pdf) and is the same approach as the [_tiered hybrid_ architecture pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern). Instead of using an on-premises environment with a public cloud, however, it uses at least two cloud environments. In a composite architecture, a single workload or application uses components from more than one cloud. The second approach deploys different applications on different public cloud environments. The following non-exhaustive list describes some of the business drivers for the second approach:

  * To fully integrate applications hosted in disparate cloud environments during a merger and acquisition scenario between two enterprises.
  * To promote flexibility and cater to diverse cloud preferences within your organization. Adopt this approach to encourage organizational units to choose the cloud provider that best suits their specific needs and preferences.
  * To operate in a multi-regional or global-cloud deployment. If an enterprise is required to adhere to data residency regulations in specific regions or countries, then they need to choose from among the available cloud providers in that location if their primary cloud provider does not have a cloud region there.



With the partitioned multicloud architecture pattern, you can optionally maintain the ability to shift workloads as needed from one public cloud environment to another. In that case, the portability of your workloads becomes a key requirement. When you deploy workloads to multiple computing environments, and want to maintain the ability to move workloads between environments, you must abstract away the differences between the environments. By using Google Kubernetes Engine (GKE), you can design and build a solution to solve multicloud complexity with consistent governance, operations, and security postures. For more information, see [GKE Multi-Cloud](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud).

As previously mentioned, there are some situations where there might be both business and technical reasons to combine Google Cloud with another cloud provider and to partition workloads across those cloud environments. [Multicloud solutions](http://cloud.google.com/multicloud) offer you the flexibility to migrate, build, and optimize applications portability across multicloud environments while minimizing lock-in, and helping you to meet your regulatory requirements. For example, you might [connect Google Cloud with Oracle Cloud Infrastructure (OCI)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/connectivity-overview), to build a multicloud solution that harnesses the capabilities of each platform using a private Cloud Interconnect to combine components running in OCI with resources running on Google Cloud. For more information, see [Google Cloud and Oracle Cloud Infrastructure – making the most of multicloud](https://services.google.com/fh/files/misc/google-cloud-oci-guide.pdf). In addition, [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) facilitates high-bandwidth dedicated connectivity between Google Cloud and other [supported cloud service providers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#supported-cloud-service-providers), enabling you to architect and build multicloud solutions to handle high inter-cloud traffic volume.

## Advantages

While using a multicloud architecture offers several business and technical [benefits](https://cloud.google.com/learn/what-is-multicloud#section-5), as discussed in [Drivers, considerations, strategy, and approaches](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/drivers), it's essential to perform a detailed feasibility assessment of each potential benefit. Your assessment should carefully consider any associated direct or indirect [challenges](https://cloud.google.com/learn/what-is-multicloud#section-6) or potential roadblocks, and your ability to navigate them effectively. Also, consider that the long-term growth of your applications or services can introduce complexities that might outweigh the initial benefits.

Here are some key advantages of the partitioned multicloud architecture pattern:

  * In scenarios where you might need to minimize committing to a single cloud provider, you can distribute applications across multiple cloud providers. As a result, you could relatively reduce vendor lock-in with the ability to change plans (to some extent) across your cloud providers. [Open Cloud](https://cloud.google.com/open-cloud) helps to bring Google Cloud capabilities, like GKE, to different physical locations. By extending Google Cloud capabilities on-premises, in multiple public clouds, and on the edge, it provides flexibility, agility, and [drives transformation](http://cloud.google.com/multicloud).

  * For regulatory reasons, you can serve a certain segment of your user base and data from a country where Google Cloud doesn't have a cloud [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).

  * The _partitioned multicloud_ architecture pattern can help to reduce latency and improve the overall quality of the user experience in locations where the primary cloud provider does not have a cloud region or a [point of presence](https://peering.google.com/#/infrastructure). This pattern is especially useful when using high-capacity and low latency multicloud connectivity, such as [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) and [CDN Interconnect](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect) with a distributed CDN.

  * You can deploy applications across multiple cloud providers in a way that lets you choose among the best services that the other cloud providers offer.

  * The _partitioned multicloud_ architecture pattern can help facilitate and accelerate merger and acquisition scenarios, where the applications and services of the two enterprises might be hosted in different public cloud environments.




## Best practices

  * Start by deploying a non-mission-critical workload. This initial deployment in the secondary cloud can then serve as a pattern for future deployments or migrations. However, this approach probably isn't applicable in situations where the specific workload is legally or regulatorily required to reside in a specific cloud region, and the primary cloud provider doesn't have a region in the required territory.
  * Minimize dependencies between systems that are running in different public cloud environments, particularly when communication is handled synchronously. These dependencies can slow performance, decrease overall availability, and potentially incur additional outbound data transfer charges.
  * To abstract away the differences between environments, consider using containers and Kubernetes where supported by the applications and feasible.
  * Ensure that CI/CD pipelines and tooling for deployment and monitoring are consistent across cloud environments.
  * Select the optimal network architecture pattern that provides the most efficient and effective communication solution for the applications you're using. 
    * Communication must be fine-grained and controlled. Use secure APIs to expose application components.
    * Consider using either the [_meshed_ architecture pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern) or one of the [_gated_ networking patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-patterns), based on your specific business and technical requirements.
  * To meet your availability and performance expectations, design for end-to-end high availability (HA), low latency, and appropriate throughput levels.
  * To protect sensitive information, we recommend encrypting all communications [in transit](https://docs.cloud.google.com/architecture/landing-zones/decide-security#encrypt-transit).

    * If encryption is required at the connectivity layer, various options are available, based on the selected hybrid connectivity solution. These options include VPN tunnels, HA VPN over Cloud Interconnect, and [MACsec for Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#encryption).
  * If you're using multiple CDNs as part of your multicloud partitioned architecture pattern, and you're populating your other CDN with large data files from Google Cloud, consider using [CDN Interconnect](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect) links between Google Cloud and [supported providers](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect#cdn-interconnect-providers) to optimize this traffic and, potentially, its [cost](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect#pricing).

  * [Extend your identity management solution](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment) between environments so that systems can authenticate securely across environment boundaries.

  * To effectively balance requests across Google Cloud and another cloud platform, you can use Cloud Load Balancing. For more information, see [Routing traffic to an on-premises location or another cloud](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#use-case_routing_traffic_to_an_on-premises_location_or_another_cloud).

    * If the outbound data transfer volume from Google Cloud toward other environments is high, consider using [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).
  * To overcome inconsistencies in protocols, APIs, and authentication mechanisms across diverse backends, we recommend, where applicable, to deploy an API gateway or proxy as a unifying [facade](https://cloud.google.com/apigee/resources/ebook/api-facade-pattern-register). This gateway or proxy acts as a centralized control point and performs the following measures:

    * Implements additional security measures.
    * Shields client apps and other services from backend code changes.
    * Facilitates audit trails for communication between all cross-environment applications and its decoupled components.
    * Acts as an [intermediate communication layer](https://docs.cloud.google.com/solutions/unlocking-legacy-applications#section-3) between legacy and modernized services. 
      * Apigee and [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/what-is-hybrid) lets you host and manage enterprise-grade and hybrid gateways across on-premises environments, edge, other clouds, and Google Cloud environments.
  * In some of the following cases, using [Cloud Load Balancing with an API gateway](https://docs.cloud.google.com/api-gateway/docs/gateway-serverless-neg) can provide a robust and secure solution for managing, securing, and distributing API traffic at scale across multiple regions:

    * Deploying multi-region failover for Apigee API runtimes in different regions.
    * Increasing performance [with Cloud CDN](https://cloud.google.com/blog/products/api-management/api-performance-and-availability-with-apigee-x-and-cloud-cdn).

    * Providing WAF and DDoS protection through Google Cloud Armor.

  * Use consistent tools for logging and monitoring across cloud environments where possible. You might consider using open source monitoring systems. For more information, see [Hybrid and multicloud monitoring and logging patterns](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-monitoring-and-logging-patterns).

  * If you're deploying application components in a distributed manner where the components of a single application are deployed in more than one cloud environment, see the [best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern#best-practices) for the _tiered hybrid_ architecture pattern.




[ Previous arrow_back  Tiered hybrid pattern  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern)

[ Next Analytics hybrid and multicloud patterns  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/analytics-hybrid-multicloud-pattern)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
