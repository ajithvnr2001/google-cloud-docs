---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/other-considerations/
title: Other considerations \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:44.519007+00:00
---

# Other considerations  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/other-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Other considerations Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

This document highlights the core design considerations that play a pivotal role in shaping your overall hybrid and multicloud architecture. Holistically analyze and assess these considerations across your entire solution architecture, encompassing all workloads, not just specific ones.

## Refactor

In a refactor migration, you modify your workloads to take advantage of cloud capabilities, not just to make them work in the new environment. You can improve each workload for performance, features, cost, and user experience. As highlighted in [Refactor: move and improve](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#refactor_move_and_improve), some refactor scenarios let you modify workloads before migrating them to the cloud. This refactoring approach offers the following benefits, especially if your goal is to build a hybrid architecture as a long term targeted architecture:

  * You can improve the deployment process.
  * You can help speed up the release cadence and shorten feedback cycles by investing in continuous integration/continuous deployment (CI/CD) infrastructure and tooling.
  * You can use refactoring as a foundation to build and manage hybrid architecture with application portability.



To work well, this approach typically requires certain investments in on-premises infrastructure and tooling. Combining Google Kubernetes Engine (GKE) with Google Distributed Cloud can be useful in this approach for hybrid environments. More information about GKE is covered in the following section. You can also refer to the [GKE hybrid environment reference architecture](https://docs.cloud.google.com/anthos/docs/architecture/anthos-hybrid-environment) for more details.

## Workload portability

With hybrid and multicloud architectures, you might want to be able to shift workloads between the computing environments that host your data. To help enable the seamless movement of workloads between environments, consider the following factors:

  * You can move an application from one computing environment to another without significantly modifying the application and its operational model: 
    * Application deployment and management are consistent across computing environments.
    * Visibility, configuration, and security are consistent across computing environments.
  * The ability to make a workload portable shouldn't conflict with the workload being cloud-first.



## Infrastructure automation

Infrastructure automation is essential for portability in hybrid and multicloud architectures. One common approach to automating infrastructure creation is through infrastructure as code (IaC). IaC involves managing your infrastructure in files instead of manually configuring resources—like a VM, a security group, or a load balancer—in a user interface. [Terraform](https://www.terraform.io/) is a popular IaC tool to define infrastructure resources in a file. Terraform also lets you automate the creation of those resources in heterogeneous environments.

For more information about Terraform core functions that can help you automate provisioning and managing Google Cloud resources, see [Terraform blueprints and modules for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints).

You can use configuration management tools such as [Ansible](https://www.ansible.com/), [Puppet](https://www.puppet.com/), or [Chef](https://www.chef.io/) to establish a common deployment and configuration process. Alternatively, you can use an image-baking tool like [Packer](https://www.packer.io/) to create VM images for different platforms. By using a single, shared configuration file, you can use [Packer and Cloud Build](https://docs.cloud.google.com/build/docs/building/build-vm-images-with-packer) to create a VM image for use on Compute Engine. Finally, you can use solutions such as Prometheus and Grafana to help ensure consistent monitoring across environments.

Based on these tools, you can assemble a common tool chain as illustrated in the following logical diagram. This common tool chain abstracts away the differences between computing environments. It also lets you unify provisioning, deployment, management, and monitoring.

![A tool chain enables application portability.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns/architectures-infrastructure-automation.svg)

Although a common tool chain can help you achieve portability, it's subject to several of the following shortcomings:

  * Using VMs as a common foundation can make it difficult to implement true cloud-first applications. Also, using VMs only can prevent you from using cloud-managed services. You might miss opportunities to reduce administrative overhead.
  * Building and maintaining a common tool chain incurs overhead and operational costs.
  * As the tool chain expands, it can develop unique complexities tailored to the specific needs of your company. This increased complexity can contribute to rising training costs.



Before deciding to develop tooling and automation, explore the managed services your cloud provider offers. When your provider offers managed services that support the same use case, you can abstract away some of its complexity. Doing so lets you focus on the workload and the application architecture rather than the underlying infrastructure.

For example, you can use the [Kubernetes Resource Model](https://cloud.google.com/blog/topics/developers-practitioners/build-platform-krm-part-2-how-kubernetes-resource-model-works) to automate the creation of Kubernetes clusters using a declarative configuration approach. You can use [Deployment Manager convert](https://docs.cloud.google.com/deployment-manager/docs/dm-convert) to convert your Deployment Manager configurations and templates to other declarative configuration formats that Google Cloud supports (like Terraform and the Kubernetes Resource Model) so they're portable when you publish.

You can also consider [automating](https://docs.cloud.google.com/deployment-manager/docs/best-practices#automation) the creation of projects and the creation of resources within those projects. This automation can help you adopt an infrastructure-as-code approach for project provisioning.

## Containers and Kubernetes

Using cloud-managed capabilities helps to reduce the complexity of building and maintaining a custom tool chain to achieve workload automation and portability. However, only using VMs as a common foundation makes it difficult to implement truly cloud-first applications. One solution is to use containers and Kubernetes instead.

Containers help your software to run reliably when you move it from one environment to another. Because containers decouple applications from the underlying host infrastructure, they facilitate the deployment across computing environments, such as hybrid and multicloud.

Kubernetes handles the orchestration, deployment, scaling, and management of your containerized applications. It's open source and governed by the [Cloud Native Computing Foundation](https://www.cncf.io/). Using Kubernetes provides the services that form the foundation of a cloud-first application. Because you can install and run Kubernetes on many computing environments, you can also use it to establish a common runtime layer across computing environments:

  * Kubernetes provides the same services and APIs in a cloud or private computing environment. Moreover, the level of abstraction is much higher than when working with VMs, which generally translates into less required groundwork and improved developer productivity.
  * Unlike a custom tool chain, Kubernetes is widely adopted for both development and application management, so you can tap into existing expertise, documentation, and third-party support.
  * Kubernetes supports all container implementations that: 
    * Support the Kubernetes [Container Runtime Interface (CRI)](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md)
    * Are industry-adopted for application
    * Aren't tied to any specific vendor



When a workload is running on Google Cloud, you can avoid the effort of installing and operating Kubernetes by using a managed Kubernetes platform such as GKE. Doing so can help operations staff shift their focus from building and maintaining infrastructure to building and maintaining applications.

You can also use [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), a GKE mode of operation that manages your cluster configuration, including your nodes, scaling, security, and other preconfigured settings. When using GKE Autopilot, consider your scaling requirements and its [scaling limits](https://docs.cloud.google.com/kubernetes-engine/quotas#limits_per_cluster).

Technically, you can install and run Kubernetes on many computing environments to establish a common runtime layer. Practically, however, building and operating such an architecture can create complexity. The architecture gets even more complex when you require container-level security control (service mesh).

To simplify managing multi-cluster deployments, you can use [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) to run modern applications anywhere at scale. GKE includes powerful managed open source components to secure workloads, enforce compliance policies, and provide deep network observability and troubleshooting.

As illustrated in the following diagram, using GKE means you can [operate multi-cluster applications as fleets](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview).

![Stack diagram showing the fleet-management opportunities offered by GKE.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns/architectures-containers-kubernetes.svg)

GKE helps with the following design options to support hybrid and multicloud architectures:

  * Design and build cloud-like experiences on-premises or unified solutions for transitioning applications to GKE hybrid environment. For more information, see the [GKE hybrid environment reference architecture](https://docs.cloud.google.com/anthos/docs/architecture/anthos-hybrid-environment).

  * Design and build a solution to solve multicloud complexity with a consistent governance, operations, and security posture with GKE Multi-Cloud. For more information, see the [GKE Multi-Cloud](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud) documentation.




GKE also provides logical groupings of similar environments with consistent security, configuration, and service management. For example, GKE and related products allow you to create a [zero trust distributed architecture](https://docs.cloud.google.com/architecture/network-hybrid-multicloud#zero_trust_distributed_architecture). In a zero trust distributed architecture, services that are deployed on-premises or in another cloud environment can communicate across environments through end-to-end mTLS secure service-to-service communications.

## Workload portability considerations

Kubernetes and GKE provide a layer of abstraction for workloads that can hide the many intricacies and differences between computing environments. The following list describes some of those abstractions:

  * An application might be portable to a different environment with minimal changes, but that doesn't mean that the application performs equally well in both environments. 
    * Differences in underlying compute, infrastructure security capabilities, or networking infrastructure, along with proximity to dependent services, might lead to substantially different performance.
  * Moving a workload between computing environments might also require you to move data. 
    * Different environments can have different data storage and management services and facilities.
  * The behavior and performance of load balancers provisioned with Kubernetes or GKE might differ between environments.



## Data movement

Because it can be complex to move, share, and access data at scale between computing environments, enterprise-level companies might hesitate to build a hybrid or multicloud architecture. This hesitation might increase if they are already storing most of their data on-premises or in one cloud.

However, the various [data movement options](https://cloud.google.com/data-movement) offered by Google Cloud, provide enterprises with a comprehensive set of solutions to help move, integrate, and transform their data. These options help enterprises to store, share, and access data across different environments in a way that meets their specific use cases. That ability ultimately makes it easier for business and technology decision-makers to adopt hybrid and multicloud architectures.

Data movement is an important consideration for hybrid and multicloud strategy and architecture planning. Your team needs to identify your different business use cases and the data that powers them. You should also think about storage type, capacity, accessibility, and movement options.

If an enterprise has a data classification for regulated industries, that classification can help to identify storage locations and cross-region data movement restrictions for certain data classes. For more information, see [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). Sensitive Data Protection is a fully managed service designed to help you discover, classify, and protect your data assets.

To explore the process, from planning a data transfer to using best practices in implementing a plan, see [Migration to Google Cloud: Transferring your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets).

## Security

As organizations adopt hybrid and multicloud architectures, their attack surface can increase depending on the way their systems and data are distributed across different environments. Combined with the constantly evolving threat landscape, increased attack surfaces can lead to an increased risk of unauthorized access, data loss, and other security incidents. Carefully consider security when planning and implementing hybrid or multicloud strategies.

For more information, see [Attack Surface Management for Google Cloud](https://cloud.google.com/blog/products/identity-security/mandiants-attack-surface-management-now-works-with-google-cloud).

When architecting for a hybrid architecture, it's not always technically feasible or viable to extend on-premises security approaches to the cloud. However, many of the networking security capabilities of hardware appliances are cloud-first features and they operate in a distributed manner. For more information about the cloud-first network security capabilities of Google Cloud, see [Cloud network security](https://cloud.google.com/learn/what-is-cloud-network-security).

Hybrid and multicloud architectures can introduce additional security challenges, such as consistency and observability. Every public cloud provider has its own approach to security, including different models, best practices, infrastructure and application security capabilities, compliance obligations, and even the names of security services. These inconsistencies can increase security risk. Also, the [shared responsibility model](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) of each cloud provider can differ. It's essential to identify and understand the exact demarcation of responsibilities in a multicloud architecture.

Observability is key to gaining insights and metrics from the different environments. In a multicloud architecture, each cloud typically provides tools to monitor for [security posture](https://docs.cloud.google.com/software-supply-chain-security/docs/assess) and misconfigurations. However, using these tools results in siloed visibility, which prevents building advanced threat intelligence across the entire environment. As a result, the security team must switch between tools and dashboards to keep the cloud secure. Without an overarching end-to-end security visibility for the hybrid and multicloud environments, it's difficult to prioritize and mitigate vulnerabilities.

To obtain the full visibility and posture of all your environments, prioritize your vulnerabilities, and mitigate the vulnerabilities you identify. We recommend a centralized visibility model. A centralized visibility model avoids the need for manual correlation between different tools and dashboards from different platforms. For more information, see [Hybrid and multicloud monitoring and logging patterns](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-monitoring-and-logging-patterns).

As part of your planning to mitigate security risks and deploy workloads on Google Cloud, and to help you plan and design your cloud solution for meeting your security and compliance objectives, explore the Google Cloud [security best practices center](https://cloud.google.com/security/best-practices) and the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations).

Compliance objectives can vary, as they are influenced by both industry-specific regulations and the varying regulatory requirements of different regions and countries. For more information, see the Google Cloud [compliance resource center](https://cloud.google.com/compliance). The following are some of the primary recommended approaches for architecting secure hybrid and multicloud architecture:

  * Develop a unified tailored cloud security strategy and architecture. Hybrid and multicloud security strategies should be tailored to the specific needs and objectives of your organization.

It's essential to understand the targeted architecture and environment before implementing security controls, because each environment can use different features, configurations, and services.

  * Consider a unified security architecture across hybrid and multicloud environments.

  * Standardize cloud design and deployments, especially security design and capabilities. Doing so can improve efficiency and enable unified governance and tooling.

  * Use multiple security controls.

Typically, no single security control can adequately address all security protection requirements. Therefore, organizations should use a combination of security controls in a layered defense approach, also known as defense-in-depth.

  * Monitor and continuously improve security postures: Your organization should monitor its different environments for security threats and vulnerabilities. It should also try to continuously improve its security posture.

  * Consider using cloud security posture management (CSPM) to identify and remediate security misconfigurations and cybersecurity threats. CSPM also provides vulnerability assessments across hybrid and multicloud environments.




[Security Command Center](https://docs.cloud.google.com/security-command-center) is a built-in security and risk management solution for Google Cloud that helps to identify misconfigurations and vulnerabilities and more. [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics) is a managed vulnerability assessment scanning tool. It's a feature of Security Command Center that identifies security risks and vulnerabilities in your Google Cloud environment and provides recommendations for remediating them.

[Mandiant Attack Surface Management for Google Cloud](https://www.mandiant.com/resources/blog/cloud-visibility-attack-surface-management) lets your organization better see their multicloud or hybrid cloud environment assets. It automatically discovers assets from multiple cloud providers, DNS, and the extended external attack surface to give your enterprise a deeper understanding of its ecosystem. Use this information to prioritize remediation on the vulnerabilities and exposures that present the most risk.

  * Cloud security information and event management (SIEM) solution: Helps to collect and analyze security logs from hybrid and multicloud environments to detect and respond to threats. [Google Security Operations SIEM](https://cloud.google.com/security/products/security-information-event-management) from Google Cloud helps to provide security Information and event management by collecting, analyzing, detecting, and investigating all of your security data in one place.



[ Previous arrow_back  Architectural approaches to adopt a hybrid or multicloud architecture  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/adopt)

[ Next What's next  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/whats-next)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
