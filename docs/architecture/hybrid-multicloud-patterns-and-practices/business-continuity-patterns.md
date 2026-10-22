---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/business-continuity-patterns/
title: Business continuity hybrid and multicloud patterns \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:02.677817+00:00
---

# Business continuity hybrid and multicloud patterns  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/business-continuity-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Business continuity hybrid and multicloud patterns Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The main driver of considering [business continuity](https://en.wikipedia.org/wiki/Business_continuity_planning) for mission-critical systems is to help an organization to be resilient and continue its business operations during and following failure events. By replicating systems and data over multiple geographical [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) and avoiding single points of failure, you can minimize the risks of a natural disaster that affects local infrastructure. Other failure scenarios include severe system failure, a cybersecurity attack, or even a system configuration error.

Optimizing a system to withstand failures is essential for establishing effective business continuity. System reliability can be influenced by several factors, including, but not limited to, performance, resilience, [uptime availability](https://cloud.google.com/blog/products/gcp/available-or-not-that-is-the-question-cre-life-lessons), security, and [user experience](https://docs.cloud.google.com/architecture/framework/reliability/define-reliability-based-on-user-experience-goals). For more information on how to architect and operate reliable services on Google Cloud, see the [reliability](https://docs.cloud.google.com/architecture/framework/reliability) pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) and [building blocks of reliability in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks).

This architecture pattern relies on a redundant deployment of applications across multiple computing environments. In this pattern, you deploy the same applications in multiple computing environments with the aim of increasing reliability. Business continuity can be defined as the ability of an organization to continue its key business functions or services at predefined acceptable levels following a disruptive event.

[Disaster recovery (DR)](https://cloud.google.com/learn/what-is-disaster-recovery) is considered a subset of business continuity, explicitly focusing on ensuring that the IT systems that support critical business functions are operational as soon as possible after a disruption. In general, DR strategies and plans often help form a broader business continuity strategy. From a technology point of view, when you start creating disaster recovery strategies, your business impact analysis should define two key metrics: the [recovery point objective (RPO)](https://en.wikipedia.org/wiki/Recovery_point_objective) and the [recovery time objective (RTO)](https://en.wikipedia.org/wiki/Recovery_time_objective). For more guidance on using Google Cloud to address disaster recovery, see the [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

The smaller the RPO and RTO target values are, the faster services might recover from an interruption with minimal data loss. However, this implies higher cost because it means building redundant systems. Redundant systems that are capable of performing near real-time data replication and that operate at the same scale following a failure event, increase complexity, administrative overhead, and cost.

The decision to select a [DR strategy ](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#dr_patterns)or pattern should be driven by a business impact analysis. For example, the financial losses incurred from even a few minutes of downtime for a financial services organization might far exceed the cost of implementing a DR system. However, businesses in other industries might sustain hours of downtime without a significant business effect.

When you run mission-critical systems in an on-premises data center, one DR approach is to maintain standby systems in a second data center in a different region. A more cost-effective approach, however, is to use a public cloud–based computing environment for failover purposes. This approach is the main driver of the _business continuity hybrid_ pattern. The cloud can be especially appealing from a cost point of view, because it lets you turn off some of your DR infrastructure when it's not in use. To achieve a lower cost DR solution, a cloud solution lets a business accept the potential increase in RPO and RTO values.

![Data flowing from an on-premises environment to a disaster recovery instance hosted in Google Cloud.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/business.svg)

The preceding diagram illustrates the use of the cloud as a failover or disaster recovery environment to an on-premises environment.

A less common (and rarely required) variant of this pattern is the _business continuity multicloud_ pattern. In that pattern, the production environment uses one cloud provider and the DR environment uses another cloud provider. By deploying copies of workloads across multiple cloud providers, you might increase availability beyond what a multi-region deployment offers.

Evaluating a DR across multiple clouds versus using one cloud provider with different regions requires a thorough analysis of several considerations, including the following:

  * Manageability
  * Security
  * Overall feasibility.
  * Cost 
    * The potential outbound data transfer charges from more than one cloud provider could be costly with continuous inter-cloud communication.
    * There can be a high volume of traffic when replicating databases.
    * TCO and the cost of managing inter-cloud network infrastructure.

**Note:** For more information about how Cross-Cloud Interconnect might help you to lower TCO and reduce complexity, see [Announcing Cross-Cloud Interconnect: seamless connectivity to all your clouds](https://cloud.google.com/blog/products/networking/announcing-google-cloud-cross-cloud-interconnect).

If your data needs to stay in your country to meet regulatory requirements, using a second cloud provider that's also in your country as a DR can be an option. That use of a second cloud provider assumes that there's no option to use an on-premises environment to build a hybrid setup. To avoid rearchitecting your cloud solution, ideally your second cloud provider should offer all the required capabilities and services you need in-region.

## Design considerations

  * **DR expectation** : The RPO and the RTO targets your business wants to achieve should drive your DR architecture and build planning.
  * **Solution architecture** : With this pattern, you need to replicate the existing functions and capabilities of your on-premises environment to meet your DR expectations. Therefore, you need to assess the feasibility and viability of rehosting, refactoring, or rearchitecting your applications to provide the same (or more optimized) functions and performance in the cloud environment.
  * **Design and build** : Building a landing zone is almost always a prerequisite to deploying enterprise workloads in a cloud environment. For more information, see [Landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones).
  * **DR invocation** : It's important for your DR design and process to consider the following questions:

    * What triggers a DR scenario? For example, a DR might be triggered by the failure of specific functions or systems in the primary site.
    * How is the failover to the DR environment invoked? Is it a manual approval process, or can it be automated to achieve a low RTO target?
    * How should system failure detection and notification mechanisms be designed to invoke failover in alignment with the expected RTO?
    * How is traffic rerouted to the DR environment after the failure is detected?

Validate your answers to these questions through testing.

  * **Testing** : Thoroughly test and evaluate the failover to DR. Ensure that it meets your RPO and RTO expectations. Doing so could give you more confidence to invoke DR when required. Any time a new change or update is made to the process or technology solution, conduct the tests again.

  * **Team skills** : One or more technical teams must have the skills and expertise to build, operate, and troubleshoot the production workload in the cloud environment, unless your environment is managed by a third party.




## Advantages

Using Google Cloud for business continuity offers several advantages:

  * Because Google Cloud has [many regions](https://cloud.google.com/about/locations) across the globe to choose from, you can use it to back up or replicate data to a different site within the same continent. You can also back up or replicate data to a site on a different continent.
  * Google Cloud offers the ability to store data in Cloud Storage in a [dual-region or multi-region](https://docs.cloud.google.com/storage/docs/locations#key-concepts) bucket. Data is stored redundantly in at least two separate geographic regions. Data stored in dual-region and multi-region buckets are replicated across geographic regions using default replication. 
    * Dual-region buckets provide geo-redundancy to support business continuity and DR plans. Also, to replicate faster, with a [lower RPO](https://cloud.google.com/storage/sla), objects stored in dual-regions can optionally use [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) across those regions.
    * Similarly multi-region replication provides redundancy across multiple regions, by storing your data within the geographic boundary of the multi-region.
  * Provides one or more of the following options to reduce capital expenses and operating expenses to build a DR: 
    * Stopped VM instances only incur storage costs and are substantially cheaper than running VM instances. That means you can minimize the cost of maintaining cold standby systems.
    * The pay-per-use model of Google Cloud means that you only pay for the storage and compute capacity that you actually use.
    * Elasticity capabilities, like autoscaling, let you automatically scale or shrink your DR environment as needed.



For example, the following diagram shows an application running in an on-premises environment (production) that uses recovery components on Google Cloud with Compute Engine, Cloud SQL, and Cloud Load Balancing. In this scenario, the database is pre-provisioned using a VM-based database or using a Google Cloud managed database, like Cloud SQL, for faster recovery with continuous data replication. You can launch Compute Engine VMs from pre-created snapshots to reduce cost during normal operations. With this setup, and following a failure event, DNS needs to point to the Cloud Load Balancing external IP address.

![An application running in an on-premises production environment using recovery components on Google Cloud with Compute Engine, Cloud SQL, and Cloud Load Balancing.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/onprem-prod.svg)

To have the application operational in the cloud, you need to provision the web and application VMs. Depending on the targeted RTO level and company policies, the entire process to invoke a DR, provision the workload in the cloud, and reroute the traffic, can be completed manually or automatically.

To speed up and automate the provisioning of the infrastructure, consider managing the infrastructure as code. You can use Cloud Build, which is a continuous integration service, to automatically apply Terraform manifests to your environment. For more information, see [Managing infrastructure as code with Terraform, Cloud Build, and GitOps](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code).

## Best practices

When you're using the business continuity pattern, consider the following best practices:

  * Create a [disaster recovery plan](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) that documents your infrastructure along with failover and recovery procedures.
  * Consider the following actions based on your business impact analysis and the identified required RPO and RTO targets: 
    * Decide whether backing up data to Google Cloud is sufficient, or whether you need to consider another DR strategy (cold, warm, or hot standby systems).
    * Define the services and products that you can use as [building blocks](https://docs.cloud.google.com/architecture/dr-scenarios-building-blocks) for your DR plan.
    * Frame the applicable DR scenarios for your [applications](https://docs.cloud.google.com/architecture/dr-scenarios-for-applications) and [data](https://docs.cloud.google.com/architecture/dr-scenarios-for-data) as part of your selected DR strategy.
  * Consider using the [_handover_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/handover-pattern) when you're only backing up data. Otherwise, the [_meshed_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern) might be a good option to replicate the existing environment network architecture.
  * Minimize dependencies between systems that are running in different environments, particularly when communication is handled synchronously. These dependencies can slow performance and decrease overall availability.
  * Avoid the spilt-brain problem. If you replicate data bidirectionally across environments, you might be exposed to the split-brain problem. The split-brain problem occurs when two environments that replicate data bidirectionally lose communication with each other. This split can cause systems in both environments to conclude that the other environment is unavailable and that they have exclusive access to the data. This can lead to conflicting modifications of the data. There are two common ways to avoid the split-brain problem:

    * Use a third computing environment. This environment allows systems to check for a quorum before modifying data.
    * Allow conflicting data modifications to be reconciled after connectivity is restored.

With SQL databases, you can avoid the split-brain problem by making the original primary instance inaccessible before clients start using the new primary instance. For more information, see [Cloud SQL database disaster recovery](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#avoiding_a_split-brain_state).

  * Ensure that CI/CD systems and artifact repositories don't become a single point of failure. When one environment is unavailable, you must still be able to deploy new releases or apply configuration changes.

  * Make all workloads portable when using standby systems. All workloads should be portable (where supported by the applications and feasible) so that systems remain consistent across environments. You can achieve this approach by considering containers and Kubernetes. By using Google Kubernetes Engine (GKE), you can simplify the build and operations.

  * Integrate the deployment of standby systems into your CI/CD pipeline. This integration helps ensure that application versions and configurations are consistent across environments.

  * Ensure that DNS changes are propagated quickly by configuring your DNS with a reasonably short [time to live value](https://docs.cloud.google.com/dns/docs/overview#propagation_of_changes) so that you can reroute users to standby systems when a disaster occurs.

  * Select the [DNS policy and routing policy](https://docs.cloud.google.com/dns/docs/policies-overview) that align with your architecture and solution behavior. Also, you can combine multiple regional load balancers with DNS routing policies to create global load-balancing architectures for different use cases, including hybrid setup.

  * Use multiple DNS providers. When using multiple DNS providers, you can:

    * Improve the availability and resiliency of your applications and services.
    * Simplify the deployment or migration of hybrid applications that have dependencies across on-premises and cloud environments with a multi-provider DNS configuration.

Google Cloud offers an open source solution based on octoDNS to help you set up and operate an environment with multiple DNS providers. For more information, see [Multi-provider public DNS using Cloud DNS](https://docs.cloud.google.com/dns/docs/best-practices#multi-provider-dns).

  * Use load balancers when using standby systems to create an automatic failover. Keep in mind that load balancer hardware can fail.

  * Use [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#use-case_routing_traffic_to_an_on-premises_location_or_another_cloud) instead of hardware load balancers to power some scenarios that occur when using this architecture pattern. [Internal client requests](https://docs.cloud.google.com/load-balancing/docs/l7-internal#load_balancing_with_hybrid_connectivity) or [external client requests](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-ext-global-https-hybrid) can be redirected to the primary environment or the DR environment based on different metrics, such as [weight-based traffic splitting](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global#traffic_actions_weight-based_traffic_splitting). For more information, see [Traffic management overview for global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).

  * Consider using Cloud Interconnect or Cross-Cloud Interconnect if the outbound data transfer volume from Google Cloud toward the other environment is high. Cloud Interconnect can help to optimize the connectivity performance and might reduce outbound data transfer charges for traffic that meets certain conditions. For more information, see [Cloud Interconnect pricing](https://cloud.google.com/network-connectivity/docs/interconnect/pricing).

  * Consider using your preferred partner solution on [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace) to help facilitate the data backups, replications, and other tasks that meet your requirements, including your RPO and RTO targets.

  * Test and evaluate DR invocation scenarios to understand how readily the application can recover from a disaster event when compared to the target RTO value.

  * Encrypt communications in transit. To protect sensitive information, we recommend encrypting all communications in transit. If encryption is required at the connectivity layer, various options are available based on the selected hybrid connectivity solution. These options include VPN tunnels, HA VPN over Cloud Interconnect, and MACsec for Cloud Interconnect.




[ Previous arrow_back  Environment hybrid pattern  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/environment-hybrid-pattern)

[ Next Cloud bursting pattern  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
