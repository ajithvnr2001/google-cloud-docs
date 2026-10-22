---
url: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/reliability/
title: Financial services perspective: Reliability \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:27.351049+00:00
---

# Financial services perspective: Reliability  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/reliability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Financial services perspective: Reliability Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-28 UTC

This document in the [Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi) provides an overview of the principles and recommendations to design, deploy, and operate reliable FS workloads in Google Cloud. The document explores how to integrate advanced reliability practices and observability into your architectural blueprints. The recommendations in this document align with the [reliability pillar](https://docs.cloud.google.com/architecture/framework/reliability) of the Well-Architected Framework.

For financial institutions, reliable and resilient infrastructure is both a business need and a regulatory imperative. To ensure that FS workloads in Google Cloud are reliable, you must understand and mitigate potential failure points, deploy resources redundantly, and plan for recovery. Operational resilience is an outcome of reliability. It's the ability to absorb, adapt to, and recover from disruptions. Operational resilience helps FS organizations meet strict regulatory requirements. It also helps avoid [intolerable harm](https://blog.bcm-institute.org/operational-resilience/categorizing-level-of-harm-for-impact-tolerance#:%7E:text=Intolerable%20harm%20is%20%22harm%22%20that,organization%20providing%20critical%20business%20services.) to customers.

The key [building blocks of reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks) in Google Cloud are regions, zones, and the various location scopes of cloud resources: zonal, regional, multi-regional, global. You can improve availability by using managed services, distributing resources, implementing high-availability patterns, and automating processes.

## Regulatory requirements

FS organizations operate under strict reliability mandates by regulatory agencies such as the [Federal Reserve System](https://www.federalreserve.gov/aboutthefed.htm) in the US, the [European Banking Authority](https://www.eba.europa.eu/homepage) in the EU, and the [Prudential Regulation Authority](https://www.bankofengland.co.uk/explainers/what-is-the-prudential-regulation-authority-pra) in the UK. Globally, regulators emphasize operational resilience, which is vital for financial stability and consumer protection. Operational resilience is the ability to withstand disruptions, recover effectively, and maintain critical services. This requires a harmonized approach for managing technological risks and dependencies on third parties.

The regulatory requirements across most jurisdictions have the following common themes:

  * **Cybersecurity and technological resilience** : Strengthening defenses against cyber threats and ensuring the resilience of IT systems.
  * **Third-party risk management** : Managing the risks associated with outsourcing services to providers of information and communication technology (ICT).
  * **Business continuity and incident response** : Robust planning to maintain critical operations during disruptions and to recover effectively.
  * **Protecting financial stability** : Ensuring the soundness and stability of the broader financial system.



The reliability recommendations in this document are mapped to the following core principles:

  * Prioritize multi-zone and multi-region deployments
  * Eliminate single points of failure (SPOFs)
  * Understand and manage aggregate availability
  * Implement a robust DR strategy
  * Leverage managed services
  * Automate the infrastructure provisioning and recovery processes



## Prioritize multi-zone and multi-region deployments

For critical financial services applications, we recommend that you use a multi-region topology that's distributed across at least two regions and across three zones within each region. This approach is important for resilience against zone and region outages. Regulations often prescribe this approach, because if a failure occurs in one zone or region, most jurisdictions consider a severe disruption to a second zone to be a plausible consequence. The rationale is that when one location fails, the other location might receive an exceptionally high amount of additional traffic.

Consider the following recommendations to build resilience against zone and region outages:

  * Prefer resources that have a wider locational scope. Where possible, use regional resources instead of zonal resources, and use multi-regional or global resources instead of regional resources. This approach helps to avoid the need to restore operations by using backups.
  * In each region, leverage three zones rather than two. To handle failovers, overprovision capacity by a third more than the estimate.
  * Minimize manual recovery steps by implementing active-active deployments like the following examples: 
    * Distributed databases like Spanner provide built-in redundancy and synchronisation across regions.
    * The [HA feature](https://docs.cloud.google.com/sql/docs/postgres/configure-ha) of Cloud SQL provides a topology that's near active-active, with read replicas across zones. It provides a recovery point objective (RPO) between regions that's close to 0.
  * Distribute user traffic across regions by using Cloud DNS, and deploy a [regional load balancer](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#multi-region-deployment-with-regional-load-balancing) in each region. A global load balancer is another option that you can consider depending on your requirements and criticality. For more information, see [Benefits and risks of global load balancing for multi-region deployments](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#benefits-and-risks-of-global-load-balancing-for-multi-region-deployments).
  * To store data, use multi-region services like [Spanner](https://docs.cloud.google.com/spanner/docs) and [Cloud Storage](https://docs.cloud.google.com/storage/docs/locations).



## Eliminate single points of failure

Distribute resources across different locations and use redundant resources to prevent any single point of failure (SPOF) from affecting the entire application stack.

Consider the following recommendations to avoid SPOFs:

  * Avoid deploying just a single application server or database.
  * Ensure automatic recreation of failed VMs by using [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups).
  * Distribute traffic evenly across the available resources by implementing [load balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).
  * Use HA configurations for databases such as [Cloud SQL](https://docs.cloud.google.com/sql/docs/availability).
  * Improve data availability by using [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk) with synchronous replication.



For more information, see [Design reliable infrastructure for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#avoid_single_points_of_failure).

## Understand and manage aggregate availability

Be aware that the overall or _aggregate_ availability of a system is affected by the availability of each tier or component of the system. The number of tiers in an application stack has an inverse relationship with the aggregate availability of the stack. Consider the following recommendations for managing aggregate availability:

  * Calculate the aggregate availability of a multi-tier stack by using the formula _tier1_availability × tier2_availability × tierN_availability_.

The following diagram shows the calculation of aggregate availability for a multi-tier system that consists of four services:

![The aggregate availability formula for a multi-tier service that has four services.](https://docs.cloud.google.com/static/architecture/framework/perspectives/fsi/images/gcwaf-fsi-reliability-aggregate-availability.svg)

In the preceding diagram, the service in each tier provides 99.9% availability, but the aggregate availability of the system is lower at 99.6% (0.999 × 0.999 × 0.999 × 0.999). In general, the aggregate availability of a multi-tier stack is lower than the availability of the tier that provides the least availability.

  * Where feasible, choose _parallelization_ over _chaining_. With parallelized services, the end-to-end availability is higher than the availability of each individual service.

The following diagram shows two services, A and B, that are deployed by using the chaining and parallelization approaches:

![The aggregate availability formulas for chained services compared to parallelized services.](https://docs.cloud.google.com/static/architecture/framework/perspectives/fsi/images/gcwaf-fsi-reliability-chained-vs-parallelized.svg)

In the preceding examples, both services have an SLA of 99%, which results in the following aggregate availability depending on the implementation approach:

    * **Chained services** yield an aggregate availability of only 98% (.99 × .99).
    * **Parallelized services** yield a higher aggregate availability at 99.99% because each service runs independently and individual services aren't affected by the availability of the other services. The formula for aggregated parallelized services is _1 − (1 − A) × (1 − B)_.
  * Choose Google Cloud services with uptime SLAs that can help meet the required level of overall uptime for your application stack.

  * When you design your architecture, consider the trade-offs between availability, operational complexity, latency, and cost. Increasing the number of nines of availability generally costs more, but doing so helps you meet regulatory requirements.

For example, 99.9% availability (three nines) means a potential downtime of 86 seconds in a 24-hour day. In contrast, 99% (two nines) means a downtime of 864 seconds over the same period, which is 10 times more downtime than with three nines of availability.

For critical financial services, the architecture options might be limited. However, it's critical to identify the availability requirements and accurately calculate availability. Performing such an assessment helps you to assess the implications of your design decisions on your architecture and budget.




## Implement a robust DR strategy

Create well-defined plans for different disaster scenarios, including zonal and regional outages. A well-defined disaster recovery (DR) strategy lets you recover from a disruption and resume normal operations with minimal impact.

DR and high availability (HA) are different concepts. With cloud deployments, in general, DR applies to multi-region deployments and HA applies to regional deployments. These [deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes) support different replication mechanisms.

  * **HA** : Many managed services provide synchronous replication between zones within a single region by default. Such services support a zero or near-zero recovery time objective (RTO) and recovery point objective (RPO). This support lets you create an active-active deployment topology that doesn't have any SPOF.
  * **DR** : For workloads that are deployed across two or more regions, if you don't use multi-regional or global services, you must define a replication strategy. The replication strategy is typically asynchronous. Carefully assess how such replication affects the RTO and RPO for critical applications. Identify the manual or semi-automated operations that are necessary for failover.



For financial institutions, your choice of failover region might be limited by regulations about data sovereignty and data residency. If you need an active-active topology across two regions, we recommend that you choose managed multi-regional services, like Spanner and Cloud Storage, especially when data replication is critical.

Consider the following recommendations:

  * Use managed multi-regional storage services for data.
  * Take snapshots of data in persistent disks and store the snapshots in [multi-region locations](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings#storage_location_options).
  * When you use regional or zonal resources, set up data replication to other regions.
  * Validate that your DR plans are effective by testing the plan regularly.
  * Be aware of the RTO and RPO and their correlation to the impact tolerance that's stipulated by financial regulations in your jurisdiction.



For more information, see [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/architecture/disaster-recovery).

## Leverage managed services

Whenever possible, use managed services to take advantage of the built-in features for backups, HA, and scalability. Consider the following recommendations for using managed services:

  * Use managed services in Google Cloud. They provide HA that's backed by SLAs. They also offer built-in backup mechanisms and resilience features.
  * For data management, consider services like [Cloud SQL](https://docs.cloud.google.com/sql/docs/availability), [Cloud Storage](https://docs.cloud.google.com/storage/docs/locations), and [Spanner](https://docs.cloud.google.com/spanner/docs),
  * For compute and application hosting, consider [Compute Engine managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups) and [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). Regional MIGs and GKE regional clusters are resilient to zone outages.
  * To improve resilience against region outages, use managed multi-regional services.
  * Identify the need for _exit plans_ for services that have unique characteristics and define the required plans. Financial regulators like the FCA, PRA, and EBA require firms to have strategies and contingency plans for data retrieval and operational continuity if the relationship with a cloud provider ends. Firms must assess the exit feasibility before entering into cloud contracts and they must maintain the ability to change providers without operational disruption.
  * Verify that the services that you choose support exporting data to an open format like CSV, Parquet, and Avro. Verify whether the services are based on open technologies, like GKE support for the [Open Container Initiative (OCI) format](https://docs.cloud.google.com/artifact-registry/docs/supported-formats#oci) or [Managed Service for Apache Airflow built on Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview).



## Automate the infrastructure provisioning and recovery processes

Automation helps to minimize human errors and helps to reduce the time and resources that are necessary to respond to incidents. The use of automation can help to ensure faster recovery from failures and more consistent results. Consider the following recommendations to automate how you provision and recover resources:

  * Minimize human errors by using infrastructure as code (IaC) tools like Terraform.
  * Reduce manual intervention by automating failover processes. Automated responses can also help to reduce the impact of failures. For example, you can use [Eventarc](https://docs.cloud.google.com/eventarc/docs) or [Workflows](https://docs.cloud.google.com/workflows/docs/overview) to automatically trigger remedial actions in response to issues observed through audit logs.
  * Increase the capacity of your cloud resources during failover by using autoscaling.
  * Automatically apply policies and guardrails for regulatory requirements across your cloud topology during service deployment by adopting [platform engineering](https://github.com/GoogleCloudPlatform/platform-engineering).



[ Previous arrow_back  Security  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security)

[ Next Cost optimization  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/cost-optimization)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
