---
url: https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads/
title: Migrate to Google Cloud: Assess and discover your workloads \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:29.847636+00:00
---

# Migrate to Google Cloud: Assess and discover your workloads  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate to Google Cloud: Assess and discover your workloads Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-02 UTC

This document can help you plan, design, and implement the assessment phase of your migration to Google Cloud. Discovering your workloads and services inventory, and mapping their dependencies, can help you identify what you need to migrate and in what order. When planning and designing a migration to Google Cloud, you first need a deep knowledge of your current environment and of the workloads to migrate.

This document is part of the following multi-part series about migrating to Google Cloud:

  * [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
  * Migrate to Google Cloud: Assess and discover your workloads (this document)
  * [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation)
  * [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)
  * [Migrate to Google Cloud: Deploy your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads)
  * [Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments](https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments)
  * [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment)
  * [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices)
  * [Migrate to Google Cloud: Minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs)



The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

This document is useful if you're planning a migration from an on-premises environment, a private hosting environment, another cloud provider, or if you're evaluating the opportunity to migrate and exploring what the assessment phase might look like.

In the assessment phase, you determine the requirements and dependencies to migrate your source environment to Google Cloud.

The assessment phase is crucial for the success of your migration. You need to gain deep knowledge about the workloads you want to migrate, their requirements, their dependencies, and about your current environment. You need to understand your starting point to successfully plan and execute a Google Cloud migration.

The assessment phase consists of the following tasks:

  1. Build a comprehensive inventory of your workloads.
  2. Catalog your workloads according to their properties and dependencies.
  3. Train and educate your teams on Google Cloud.
  4. Build experiments and proofs of concept on Google Cloud.
  5. Calculate the total cost of ownership (TCO) of the target environment.
  6. Choose the migration strategy for your workloads.
  7. Choose your migration tools.
  8. Define the migration plan and timeline.
  9. Validate your migration plan.



## Build an inventory of your workloads

To scope your migration, you must first understand how many items, such as workloads and hardware appliances, exist in your current environment, along with their dependencies. Building the inventory is a non-trivial task that requires a significant effort, especially when you don't have any automatic cataloging system in place. To have a comprehensive inventory, you need to use the expertise of the teams that are responsible for the design, deployment, and operation of each workload in your current environment, as well as the environment itself.

The inventory shouldn't be limited to workloads only, but should at least contain the following:

  * Dependencies of each workload, such as databases, message brokers, configuration storage systems, and other components.
  * Services supporting your workload infrastructure, such as source repositories, continuous integration and continuous deployment (CI/CD) tools, and artifact repositories.
  * Servers, either virtual or physical, and runtime environments.
  * Physical appliances, such as network devices, firewalls, and other dedicated hardware.



When compiling this list, you should also gather information about each item, including:

  * Source code location and if you're able to modify this source code.
  * Deployment method for the workload in a runtime environment, for example, if you use an automated deployment pipeline or a manual one.
  * Network restrictions or security requirements.
  * IP address requirements.
  * How you're exposing the workload to clients.
  * Licensing requirements for any software or hardware.
  * How the workload authenticates against your identity and access management system.



For example, for each hardware appliance, you should know its detailed specifications, such as its name, vendor, technologies, and dependencies on other items in your inventory. For example:

  * Name: NAS Appliance
  * Vendor and model: Vendor Y, Model Z
  * Technologies: NFS, iSCSI
  * Dependencies: Network connectivity with Jumbo frames to VM compute hardware.



This list should also include non-technical information, for example, under which licensing terms you're allowed to use each item and any other compliance requirements. While some licenses let you deploy a workload in a cloud environment, others explicitly forbid cloud deployment. Some licenses are assigned based on the number of CPUs or sockets in use, and these concepts might not be applicable when running on cloud technology. Some of your data might have restrictions regarding the geographical region where it's stored. Finally, some sensitive workloads can require sole tenancy.

Along with the inventory, it's useful to provide aids for a visual interpretation of the data you gathered. For example, you can provide a dependency graph and charts to highlight aspects of interest, such as how your workloads are distributed in an automated or manual deployment process.

### How to build your inventory

There are different ways to build a workload inventory. Although the quickest way to get started is to proceed manually, this approach can be difficult for a large production environment. Information in manually built inventories can quickly become outdated, and the resulting migration might fail because you didn't confirm the contents of your inventories.

Building the inventory is not a one-time exercise. If your current environment is highly dynamic, you should also spend effort in automating the inventory creation and maintenance, so you eventually have a consistent view of all the items in your environment at any given time. For information about how to build an inventory of your workloads, see [Migration Center: Start an asset discovery](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery).

### Example of a workload inventory

This example is an inventory of an environment supporting an ecommerce app. The inventory includes workloads, dependencies, services supporting multiple workloads, and hardware appliances.

**Note:** The system resources requirements refer to the current environment. These requirements must be re-evaluated to consider the resources of the target environment. For example, the CPU cores of the target environment might be more performant due to a more modern architecture and higher clock speeds, so your workloads might require fewer cores.

#### Workloads

For each workload in the environment, the following table highlights the most important technologies, its deployment procedure, and other requirements.

Name | Source code location | Technologies | Deployment procedure | Other requirements | Dependencies | System resources requirements  
---|---|---|---|---|---|---  
Marketing website | Corporate repository | Angular frontend | Automated | Legal department must validate content | Caching service | 5 CPU cores   
8 GB of RAM  
Back office | Corporate repository | Java backend, Angular frontend | Automated | N/A | SQL database | 4 CPU cores  
4 GB of RAM  
Ecommerce workload | Proprietary workload | Vendor X  
Model Y  
Version 1.2.0 | Manual | Customer data must reside inside the European Union | SQL database | 10 CPU cores  
32 GB of RAM  
Enterprise resource planning (ERP) | Proprietary workload | Vendor Z, Model C, Version 7.0 | Manual | N/A | SQL database | 10 CPU cores  
32 GB of RAM  
Stateless microservices | Corporate repository | Java | Automated | N/A | Caching service | 4 CPU cores  
8 GB of RAM  
  
#### Dependencies

The following table is an example of the dependencies of the workloads listed in the inventory. These dependencies are necessary for the workloads to correctly function.

Name | Technologies | Other requirements | Dependencies | System resources requirements  
---|---|---|---|---  
SQL database | PostgreSQL | Customer data must reside inside the European Union | Backup and archive system | 30 CPU cores  
512 GB of RAM  
  
#### Supporting services

In your environment, you might have services that support multiple workloads. In this ecommerce example, there are the following services:

Name | Technologies | Other requirements | Dependencies | System resources requirements  
---|---|---|---|---  
Source code repositories | Git | N/A | Backup and archive system | 2 CPU cores   
4 GB of RAM  
Backup and archive system | Vendor G, Model H, version 2.3.0 | By law, long-term storage is required for some items | N/A | 10 CPU cores   
8 GB of RAM  
CI tool | Jenkins | N/A | Source code repositories   
artifact repository   
backup and archive system | 32 CPU cores   
128 GB of RAM  
Artifact repository | Vendor A  
Model N  
Version 5.0.0 | N/A | Backup and archive system | 4 CPU cores   
8 GB of RAM  
Batch processing service | Cron jobs running inside the CI tool | N/A | CI tool | 4 CPU cores   
8 GB of RAM  
Caching service | Memcached  
Redis | N/A | N/A | 12 CPU cores   
50 GB of RAM  
  
#### Hardware

The example environment has the following hardware appliances:

Name | Technologies | Other requirements | Dependencies | System resources requirements  
---|---|---|---|---  
Firewall | Vendor H  
Model V | N/A | N/A | N/A  
Instances of Server j | Vendor K  
Model B | Must be decommissioned because no longer supported | N/A | N/A  
NAS Appliance  | Vendor Y  
Model Z  
NFS  
iSCSI | N/A | N/A | N/A  
  
### Assess your deployment and operational processes

It's important to have a clear understanding of how your deployment and operational processes work. These processes are a fundamental part of the practices that prepare and maintain your production environment and the workloads that run there.

Your deployment and operational processes might build the artifacts that your workloads need to function. Therefore, you should gather information about each artifact type. For example, an artifact can be an operating system package, an application deployment package, an operating system image, a container image, or something else.

In addition to the artifact type, consider how you complete the following tasks:

  * **Develop your workloads**. Assess the processes that development teams have in place to build your workloads. For example, how are your development teams designing, coding, and testing your workloads?
  * **Generate the artifacts that you deploy in your source environment**. To deploy your workloads in your source environment, you might be generating deployable artifacts, such as container images or operating system images, or you might be customizing existing artifacts, such as third-party operating system images by installing and configuring software. Gathering information about how you're generating these artifacts helps you to ensure that the generated artifacts are suitable for deployment in Google Cloud.
  * **Store the artifacts**. If you produce artifacts that you store in an artifact registry in your source environment, you need to make the artifacts available in your Google Cloud environment. You can do so by employing strategies like the following:

    * **Establish a communication channel between the environments** : Make the artifacts in your source environment reachable from the target Google Cloud environment.
    * **Refactor the artifact build process** : Complete a minor refactor of your source environment so that you can store artifacts in both the source environment and the target environment. This approach supports your migration by building infrastructure like an artifact repository before you have to implement artifact build processes in the target Google Cloud environment. You can implement this approach directly, or you can build on the previous approach of establishing a communication channel first.

Having artifacts available in both the source and target environments lets you focus on the migration without having to implement artifact build processes in the target Google Cloud environment as part of the migration.

  * **Scan and sign code**. As part of your artifact build processes, you might be using code scanning to help you guard against common vulnerabilities and unintended network exposure, and code signing to help you ensure that only trusted code runs in your environments.

  * **Deploy artifacts in your source environment**. After you generate deployable artifacts, you might be deploying them in your source environment. We recommend that you assess each deployment process. The assessment helps ensure that your deployment processes are compatible with Google Cloud. It also helps you to understand the effort that will be necessary to eventually refactor the processes. For example, if your deployment processes work with your source environment only, you might need to refactor them to target your Google Cloud environment.

  * **Inject runtime configuration**. You might be injecting runtime configuration for specific clusters, runtime environments, or workload deployments. The configuration might initialize environment variables and other configuration values such as secrets, credentials, and keys. To help ensure that your runtime configuration injection processes work on Google Cloud, we recommend that you assess how you're configuring the workloads that run in your source environment.

  * **Logging, monitoring, and profiling**. Assess the logging, monitoring, and profiling processes that you have in place to monitor the health of your source environment, the metrics of interest, and how you're consuming data provided by these processes.

  * **Authentication**. Assess how you're authenticating against your source environment.

  * **Provision and configure your resources**. To prepare your source environment, you might have designed and implemented processes that provision and configure resources. For example, you might be using [Terraform](https://www.terraform.io/) along with configuration management tools to provision and configure resources in your source environment. If you're using Terraform, you can build your foundations and landing zone on Google Cloud by using the following tools, depending on your preferred starting point:

    * [Resources in the Google Cloud Terraform Provider](https://docs.cloud.google.com/docs/terraform/create-vm-instance): Start from scratch using base building blocks.
    * [Terraform blueprints and modules for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints): Start from a baseline of opinionated Terraform modules. This approach builds on top of resources in the Google Cloud Terraform Provider.
    * [Enterprise Foundations Blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations): Start from an opinionated foundation and landing zones. This approach builds on top of Terraform blueprints and modules for Google Cloud.
    * [Cloud Foundation Fabric](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric): Start from an opinionated foundation and landing zones. Cloud Foundation Fabric is a standalone implementation that uses its own Terraform modules. This approach builds on top of resources in the Google Cloud Terraform Provider.



### Assess your infrastructure

After you assess your deployment and operational processes, we recommend that you assess the infrastructure that is supporting your workloads in the source environment.

To assess that infrastructure, consider the following:

  * How you organized resources in your source environment. For example, some environments support a logical separation between resources using constructs that isolate groups of resources from each others, such as organizations, projects, and namespaces.
  * How you connected your environment to other environments, such as on-premises environments, and other cloud providers.



## Categorize your workloads

After you complete the inventory, you need to organize your workloads into different categories. This categorization can help you prioritize the workloads to migrate according to their complexity and risk in moving to the cloud.

A catalog matrix should have one dimension for each assessment criterion you're considering in your environment. Choose a set of criteria that covers all the requirements of your environment, including the system resources each workload needs. For example, you might be interested to know if a workload has any dependencies, or if it's stateless or stateful. When you design the catalog matrix, consider that for each criteria you add, you are adding another dimension to represent. The resulting matrix might be difficult to visualize. A possible solution to this problem could be to use multiple smaller matrixes, instead of a single, complex one.

Also, next to each workload you should add a migration complexity indicator. This indicator estimates the difficulty rating to migrate each workload. The granularity of this indicator depends on your environment. For a basic example, you might have three categories: easy to migrate, hard to migrate or cannot be migrated. To complete this activity, you need experts for each item in the inventory to estimate its migration complexity. Drivers of this migration complexity are unique to each business.

When the catalog is complete, you can also build visuals and graphs to help you and your team to quickly evaluate metrics of interest. For example, draw a graph that highlights how many components have dependencies or highlight the migration difficulty of each component.

For information about how to build an inventory of your workloads, see [Migration Center: Start an asset discovery](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery).

### Example of a workload catalog

The following assessment criteria is used in this example, one for each matrix axis:

  1. How critical a workload is to the business.
  2. Whether a workload has dependencies, or is a dependency for other workloads.
  3. Maximum allowable downtime for the workload.
  4. How difficult a workload is to be migrated.

Importance to the business | Doesn't have dependencies or dependents | Has dependencies or dependents | Maximum allowable downtime | Difficulty  
---|---|---|---|---  
Mission critical | Stateless microservices |  | 2 minutes | Easy  
|  | ERP | 24 hours | Hard  
|  | Ecommerce workload  | No downtime | Hard  
|  | Hardware firewall | No downtime | Can't move  
|  | SQL database | 10 minutes | Easy  
|  | Source code repositories | 12 hours | Easy  
Non-mission critical | Marketing website  |  | 2 hours | Easy  
| Backup and archive |  | 24 hours | Easy  
| Batch processing service |  | 48 hours | Easy  
| Caching service |  | 30 minutes | Easy  
|  | Back office | 48 hours | Hard  
|  | CI tool  | 24 hours | Easy  
|  | Artifact repository | 30 minutes | Easy  
  
To help you visualize the results in the catalog, you can build visuals and charts. The following chart highlights the migration difficulty:

![Chart that visualizes the difficulty associated with moving workloads to Google Cloud.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-assessing-and-discovering-your-workloads-2-migration-difficulty-chart.svg)

In the preceding chart, most of the workloads are easy to move, three of them are hard to move, and one of them is not possible to move.

## Educate your organization about Google Cloud

To take full advantage of Google Cloud, your organization needs to start learning about the services, products, and technologies that your business can use on Google Cloud. Your staff can begin with [Google Cloud free trial accounts](https://docs.cloud.google.com/free/docs/free-cloud-features) that contain credits to help them experiment and learn. Creating a free environment for testing and learning is critical to the learning experience of your staff.

You have several training options:

  1. Public and open resources: You can get started learning Google Cloud with free [hands-on labs](https://cloud.google.com/training/free-labs/), [video series](https://www.youtube.com/user/googlecloudplatform), [Cloud OnAir webinars](https://cloudonair.withgoogle.com/), and [hands-on training events](https://cloud.google.com/training/cloudonboard).
  2. In-depth courses: If you want a deeper understanding of how Google Cloud works, you can attend [on-demand courses from Google Cloud Skills Boost](https://www.skills.google/catalog) or [Google Cloud Training Specializations from Coursera](https://www.coursera.org/programs/google-specialization) that you can attend online at your own pace or [classroom training](https://cloud.google.com//training/courses) by our world-wide authorized training partners. These courses typically span from one to several days.
  3. [Role-based learning paths](https://www.skills.google/paths): You can train your engineers according to their role in your organization. For example, you can train your [workload developers](https://cloud.google.com/learn/training/application-development) or [infrastructure operators](https://cloud.google.com/learn/training/cloud-infrastructure) how to best use Google Cloud services.



You can also certify your engineers' knowledge of Google Cloud with various certifications, at different levels:

  1. Foundational certifications: Validate broad knowledge of Google Cloud's concepts, products, and use cases. For developers that are new to Google Cloud, certifications like [Cloud Digital Leader](https://cloud.google.com/learn/certification/cloud-digital-leader/) and [Generative AI Leader](https://cloud.google.com/learn/certification/generative-ai-leader) provide a foundational starting point.
  2. Associate certifications: Validate fundamental skills to deploy and maintain cloud projects on Google Cloud. Associate certifications include the [Associate Cloud Engineer Certification](https://cloud.google.com/learn/certification/cloud-engineer) and the [Google Workspace Administrator Certification](https://cloud.google.com/learn/certification/associate-google-workspace-administrator).
  3. Professional certifications: Assess advanced design and implementation skills for Google Cloud from years of experience. Professional certifications include [Professional Cloud Architect](https://cloud.google.com/learn/certification/cloud-architect) and the [Professional Data Engineer](https://cloud.google.com/learn/certification/data-engineer).



For more information, about foundational, associate, and professional Google Cloud certifications, see [Google Cloud certifications](https://cloud.google.com/learn/certification).

In addition to training and certification, one of the best ways to get experience with Google Cloud is to begin using the product to build business proofs-of-concept.

## Experiment and design proofs of concept

To show the value and efficacy of Google Cloud, consider designing and developing one or more proofs of concept (PoCs) for each category of workload in your workload catalog. Experimentation and testing let you validate assumptions and demonstrate the value of cloud to business leaders.

At a minimum, your PoC should include the following:

  * A comprehensive list of the use cases that your workloads support, including uncommon ones and corner cases.
  * All the requirements for each use case, such as performance, scalability, and consistency requirements, failover mechanisms, and network requirements.
  * A potential list of technologies and products that you want to investigate and test.



You should design PoCs and experiments to validate all the use cases on the list. Each experiment should have a precise validity context, scope, expected outputs, and measurable business impact.

For example, if one of your CPU-bound workloads needs to quickly scale to satisfy peaks in demand, you can run an experiment to verify that a zone can create many virtual CPU cores, and how much time it takes to do so. If you experience a significant value-add, such as reducing new workload scale-up time by 95% compared to your current environment, this experiment can demonstrate instant business value.

If you're interested in evaluating how the performance of your on-premises databases compares to [Cloud SQL](https://docs.cloud.google.com/sql), [Spanner](https://docs.cloud.google.com/spanner), [Firestore](https://docs.cloud.google.com/firestore), or [Bigtable](https://docs.cloud.google.com/bigtable), you could implement a PoC where the same business logic uses different databases. This PoC gives you a low-risk opportunity to identify the right managed database solution for your workload across multiple benchmarks and operating costs.

If you want to evaluate the performance of the VM provisioning process in Google Cloud, you can use a third-party tool, such as [PerfKit Benchmarker](http://googlecloudplatform.github.io/PerfKitBenchmarker/), and compare Google Cloud with other cloud providers. You can measure the end-to-end time to provision resources in the cloud, in addition to reporting on standard metrics of peak performance, including latency, throughput, and time-to-complete. For example, you might be interested in how much time and effort it takes to provision many Kubernetes clusters. PerfKit Benchmarker is an open source community effort involving over 500 participants, such as researchers, academic institutions, and companies, including Google.

## Calculate total cost of ownership

When you have a clear view of the resources you need in the new environment, you can build a total cost of ownership model that lets you compare your costs on Google Cloud with the costs of your current environment.

When building this cost model, you should consider not only the costs for hardware and software, but also all the [operational costs of running your own data center,](https://docs.cloud.google.com/docs/compare/data-centers) such as power, cooling, maintenance, and other support services. Consider that it's also typically easier to reduce costs, thanks to the elastic scalability of Google Cloud resources, compared to a more rigid on-premises data center.

A commonly overlooked cost when considering cloud migrations is the use of a cloud network. In a data center, purchasing network infrastructure, such as routers and switches, and then running appropriate network cabling are one-time costs that let you use the entire capacity of the network. In a cloud environment, there are many ways that you might be [billed for network utilization](https://cloud.google.com/pricing/). For data intensive workloads, or those that generate a large amount of network traffic, you might need to consider new architectures and network flows to lower networking costs in the cloud.

Google Cloud also provides a wide range of options for intelligent scaling of resources and costs. For example, in [Compute Engine](https://docs.cloud.google.com/compute) you can rightsize during your migration with [Migrate for Compute Engine](https://docs.cloud.google.com/migrate/compute-engine), or [after VMs are already running](https://docs.cloud.google.com/compute/docs/instances/apply-sizing-recommendations-for-instances), or building [autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler). These options can have a large impact on the costs of running services and should be explored to calculate the total cost of ownership (TCO).

To calculate the total cost of Google Cloud resources, you can use the [price calculator](https://cloud.google.com/products/calculator/).

## Choose the migration strategy for your workloads

For each workload to migrate, evaluate and select a migration strategy that best suits their use case. For example, your workloads might have the following conditions:

  * They don't tolerate any downtime or data loss, such as mission-critical workloads. For these workloads, you can choose zero or near-zero downtime migration strategies.
  * They tolerate downtimes, such secondary or backend workloads. For these workloads, you can choose migration strategies that require a downtime.



When you choose migration strategies, consider that zero and near-zero downtime migration strategies are usually more costly and complex to design and implement than migration strategies that require a downtime.

## Choose your migration tools

After you choose a migration strategy for your workloads, review and decide upon the migration tools.

There are many migration tools available, each optimized for certain migration use cases. Use cases can include the following:

  * Migration strategy
  * Source and target environments
  * Data and workload size
  * Frequency of changes to data and workloads
  * Availability to use managed services for migration



To ensure a seamless migration and cut-over, you can use application deployment patterns, infrastructure orchestration, and custom migration applications. However, specialized tools called managed migration services can facilitate the process of moving data, workloads, or even entire infrastructures from one environment to another. With these capabilities, they encapsulate the complex logic of migration and offer migration monitoring capabilities.

## Define the migration plan and timeline

Now that you have an exhaustive view of your current environment, you need to complete your migration plan by:

  1. Grouping the workloads and data to migrate in _batches_ (also called _sprints_ in some contexts).
  2. Choosing the order in which you want to migrate the batches.
  3. Choosing the order in which you want to migrate the workloads inside each batch.



As part of your migration plan, we recommend that you also produce the following documents:

  * Technical design document
  * RACI matrix
  * Timeline (such as a T-Minus plan)



As you gain experience with Google Cloud, momentum with the migration, and the understanding of your environment, you can do the following:

  * Refine the grouping of workloads and data to migrate.
  * Increase the size of migration batches.
  * Update the order in which you migrate batches and workloads inside batches.
  * Update the composition of the batches.



To group the workloads and data to migrate in batches, and to define migration ordering, you assess your workloads against several criteria, such as the following:

  * Business value of the workload.
  * If the workload is deployed or run in a unique way compared to the rest of your infrastructure.
  * Teams responsible for development, deployment, and operations of the workload.
  * Number, type, and scope of dependencies of the workload.
  * Refactoring effort to make the workload work in the new environment.
  * Compliance and licensing requirements of the workload.
  * Availability and reliability requirements of the workload.



The workloads you migrate first are the ones that let your teams build their knowledge and experience on Google Cloud. Greater cloud exposure and experience from your team can lower the risk of complications during the migration phase of your migration, and make subsequent migrations easier and quicker. For this reason, choosing the right first-movers is crucial for a successful migration.

### Business value

Choosing a workload that isn't business critical protects your main line of business, and decreases the impact on business from undiscovered risks and mistakes while your team is learning cloud technologies. For example, if you choose the component where the main financial transactions logic of your ecommerce workload is implemented as a first-mover, any mistake during the migration might cause an impact on your main line of business. A better choice is the SQL database supporting your workloads, or better yet, the staging database.

You should avoid rarely used workloads. For example, if you choose a workload that's used only a few times per year by a low number of users, although it's a low risk migration, it doesn't increase the momentum of your migration, and it can be hard to detect and respond to problems.

### Edge cases

You should also avoid edge cases, so you can discover patterns that you can apply to other workloads to migrate. A primary goal when selecting a first mover is to gain experience with common patterns in your organization so you can build a knowledge base. You can apply what you learned with these first movers when migrating future workloads later.

For example, if most of your workloads are designed following a [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) methodology and are developed using the [Python programming language](https://www.python.org/), choosing a workload with little test coverage and developed using the [Java programming language](https://en.wikipedia.org/wiki/Java_\(programming_language\)), doesn't let you discover any pattern that you can apply when migrating the Python workloads.

### Teams

When choosing your first-movers, pay attention to the teams responsible for each workload. The team responsible for a first-mover should be highly motivated, and eager to try Google Cloud and its services. Moreover, business leadership should have clear goals for the first-mover teams and actively work to sponsor and support them through the process.

For example, a high performing team that sits in the main office with a proven history of implementing modern development practices such as [DevOps](https://cloud.google.com/devops/) and disciplines such as [site reliability engineering](https://landing.google.com/sre/books/) can be a good candidate. If they also have top-down leadership sponsors and clear goals around each workloads migration, they can be a superb candidate.

### Dependencies

Also, you should focus on workloads that have the fewest number of dependencies, either from other workloads or services. The migration of a workload with no dependencies is easier when you have limited experience with Google Cloud.

If you have to choose workloads that have dependencies on other components, pick the ones that are loosely coupled to their dependencies. If a workload is already designed for the eventual unavailability of its dependencies, it can reduce the friction when migrating the workload to the target environment. For example, loosely coupled candidates are workloads that communicate by using a message broker, or that work offline, or are designed to tolerate the unavailability of the rest of the infrastructure.

Although there are [strategies to migrate data of stateful workloads](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#data_migration_approaches), a stateless workload rarely requires any data migration. Migrating a stateless workload can be easier because you don't need to worry about a transitory phase where data is partially in your current environment and partially in your target environment. For example, stateless microservices are good first-mover candidates, because they don't rely on any local stateful data.

### Refactoring effort

A first-mover should require a minimal amount of refactoring, so you can focus on the migration itself and on Google Cloud, instead of spending a large effort on changes to the code and configuration of your workloads. The refactoring should focus on the necessary changes that allow your workloads to run in the target environment instead of focusing on modernizing and optimizing your workloads, which is tackled in later migration phases.

For example, a workload that requires only configuration changes is a good first-mover, because you don't have to implement any change to codebase, and you can use the existing artifacts.

### Licensing and compliance

Licenses also play a role in choosing the first-movers, because some of your workloads might be licensed under terms that affect your migration. For example, some licenses explicitly forbid running workloads in a cloud environment.

When examining the licensing terms, don't forget the compliance requirements because you might have sole tenancy requirements for some of your workloads. For these reasons, you should choose workloads that have the least amount of licensing and compliance restrictions as first-movers.

For example, your customers might have the legal right to choose in which region you store their data, or your customers' data might be restricted to a particular region.

### Availability and reliability

Good first-movers are the ones that can afford a downtime caused by a cutover window. If you choose a workload that has strict availability requirements, you have to implement a zero-downtime data migration strategy such as [Y (writing and reading)](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#y_writing_and_reading) or by developing a [data-access microservice](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#data-access_microservice). While this approach is possible, it distracts your teams from gaining the necessary experience with Google Cloud, because they have to spend time to implement such strategies.

For example, the availability requirements of a batch processing engine can tolerate a longer downtime than the customer-facing workload of your ecommerce site where your users finalize their transactions.

## Validate your migration plan

Before taking action to start your migration plan, we recommend that you validate its feasibility. For more information, see [Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices).

## What's next

  * Learn how to [plan your migration and build your foundation on Google Cloud](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-02 UTC."],[],[]] 
