---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/distributed-patterns/
title: Distributed architecture patterns \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:44.598211+00:00
---

# Distributed architecture patterns  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/distributed-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Distributed architecture patterns Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-10-29 UTC

When migrating from a non-hybrid or non-multicloud computing environment to a hybrid or multicloud architecture, first consider the constraints of your existing applications and how those constraints could lead to application failure. This consideration becomes more important when your applications or application components operate in a distributed manner across different environments. After you have considered your constraints, develop a plan to avoid or overcome them. Make sure to consider the unique capabilities of each computing environment in a distributed architecture.

**Note:** You can apply different architecture patterns to different applications, based on their use cases and requirements. This means that you might have multiple applications with different hybrid and multicloud architecture patterns operating at the same time.

## Design considerations

The following design considerations apply to distributed deployment patterns. Depending on the target solution and business objectives, the priority and the effect of each consideration can vary.

### Latency

In any architecture pattern that distributes application components (frontends, backends, or microservices) across different computing environments, communication latency can occur. This latency is influenced by the hybrid network connectivity (Cloud VPN and Cloud Interconnect) and the geographical distance between the on-premises site and the cloud [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones), or between cloud regions in a multicloud setup. Therefore, it's crucial to assess the latency requirements of your applications and their sensitivity to network delays. Applications that can tolerate latency are more suitable candidates for initial distributed deployment in a hybrid or multicloud environment.

### Temporary versus final state architecture

To specify the expectations and any potential implications for cost, scale, and performance, it's important to analyze what type of architecture you need and the intended duration as part of the planning stage. For example, if you plan to use a hybrid or multicloud architecture for a long time or permanently, you might want to consider using [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview). To reduce outbound data transfer costs and to optimize hybrid connectivity network performance, Cloud Interconnect discounts the outbound data transfer charges that meet the [discounted data transfer rate conditions](https://cloud.google.com/network-connectivity/docs/interconnect/pricing).

### Reliability

Reliability is a major consideration when architecting IT systems. [Uptime availability](https://cloud.google.com/blog/products/gcp/available-or-not-that-is-the-question-cre-life-lessons) is an essential aspect of system reliability. In Google Cloud, you can increase the resiliency of an application by deploying redundant components of that application across multiple zones in a single region1, or across multiple regions, with switchover capabilities. Redundancy is one of the key elements to improve the overall availability of an application. For applications with a distributed setup across hybrid and multicloud environments, it's important to maintain a consistent level of availability.

To enhance the availability of a system in an on-premises environment, or in other cloud environments, consider what hardware or software redundancy—with failover mechanisms—you need for your applications and their components. Ideally, you should consider the availability of a service or an application across the various components and supporting infrastructure (including [hybrid connectivity availability](https://cloud.google.com/network-connectivity/docs/interconnect/sla)) across all the environments. This concept is also referred to as the composite availability of an application or service.

Based on the dependencies between the components or services, the composite availability for an application might be higher or lower than for an individual service or component. For more information, see [Composite availability: calculating the overall availability of cloud infrastructure](https://cloud.google.com/blog/products/devops-sre/composite-cloud-availability).

To achieve the level of system reliability that you want, define clear reliability metrics and design applications to self-heal and endure disruptions effectively across the different environments. To help you define appropriate ways to measure the customer experience of your services, see [Define reliability based on user-experience goals](https://docs.cloud.google.com/architecture/framework/reliability/define-reliability-based-on-user-experience-goals).

### Hybrid and multicloud connectivity

The requirements of the communication between the distributed applications components should influence your selection of a hybrid network connectivity option. Each connectivity option has its advantages and disadvantages, as well as specific drivers to consider, such as cost, traffic volume, security, and so forth. For more information, see the [connectivity design considerations](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/design-considerations) section.

### Manageability

Consistent and unified management and monitoring tools are essential for successful hybrid and multicloud setups (with or without workload portability). In the short term, these tools can add development, testing, and operations costs. Technically, the more cloud providers you use, the more complex [managing your environments](https://cloud.google.com/learn/what-is-multicloud#section-4) becomes. Most public cloud vendors not only have different features, but also have varying tools, SLAs, and APIs for managing cloud services. Therefore, weigh the strategic advantages of your selected architecture against the potential short-term complexity versus the long-term benefits.

### Cost

Each cloud service provider in a multicloud environment has its own billing metrics and tools. To provide better visibility and unified dashboards, consider using multicloud cost management and optimization tooling. For example, when building cloud-first solutions across multiple cloud environments each provider's products, pricing, discounts, and management tools can create cost inconsistencies between those environments.

We recommend having a single, well-defined method for calculating the full costs of cloud resources, and to provide cost visibility. Cost visibility is essential for cost optimization. For example, by combining billing data from the cloud providers you use and using Google Cloud [Looker Cloud Cost Management Block](https://marketplace.looker.com/marketplace/detail/multicloud-billing-dashboard), you can create a centralized view of your multicloud costs. This view can help provide a consolidated reporting view of your spend across multiple clouds. For more information, see [The strategy for effectively optimizing cloud billing cost management](https://cloud.google.com/blog/products/data-analytics/cloud-cost-management).

We also recommend using FinOps practice to make costs visible. As a part of a strong FinOps practice, a central team can delegate the decision making for resource optimization to any other teams involved in a project to encourage individual accountability. In this model, the central team should standardize the process, the reporting, and the tooling for cost optimization. For more information about the different cost optimization aspects and recommendations that you should consider, see [Google Cloud Well-Architected Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization).

### Data movement

[Data movement](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/other-considerations#data_movement) is an important consideration for hybrid and multicloud strategy and architecture planning, especially for distributed systems. Enterprises need to identify their different business use cases, the data that powers them, and how the data is classified (for regulated industries). They should also consider how data storage, sharing, and access for distributed systems across environments might affect application performance and data consistency. Those factors might influence the application and the data pipeline architecture. Google Cloud's comprehensive set of [data movement options](https://cloud.google.com/data-movement) makes it possible for businesses to meet their specific needs and adopt hybrid and multicloud architectures without compromising simplicity, efficiency, or performance.

### Security

When migrating applications to the cloud, it's important to consider cloud-first security capabilities like consistency, observability, and unified security visibility. Each public cloud provider has its own approach, best practices, and capabilities for security. It's important to analyze and align these capabilities to build a standard, functional security architecture. Strong IAM controls, data encryption, vulnerability scanning, and compliance with industry regulations are also important aspects of cloud security.

When planning a migration strategy, we recommend that you analyze the previously mentioned considerations. They can help you minimize the chances of introducing complexities to the architecture as your applications or traffic volumes grow. Also, designing and building a landing zone is almost always a prerequisite to deploying enterprise workloads in a cloud environment. A landing zone helps your enterprise deploy, use, and scale cloud services more securely across multiple areas and includes different elements, such as identities, resource management, security, and networking. For more information, see [Landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones).

The following documents in this series describe other distributed architecture patterns:

  * [Tiered hybrid pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern)
  * [Partitioned multicloud pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern)
  * [Analytics hybrid and multicloud pattern ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/analytics-hybrid-multicloud-pattern)
  * [Edge hybrid pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/edge-hybrid-pattern)



* * *

  1. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). ↩




[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices)

[ Next Tiered hybrid pattern  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-10-29 UTC."],[],[]] 
