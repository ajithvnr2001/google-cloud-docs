---
url: https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs/
title: Migrate to Google Cloud: Minimize costs \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:07.875663+00:00
---

# Migrate to Google Cloud: Minimize costs  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate to Google Cloud: Minimize costs Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-11-20 UTC

This document helps you minimize costs of your single- and multi-region Google Cloud environments, and of migrations across Google Cloud [regions](https://docs.cloud.google.com/docs/geography-and-regions). This document is useful if you're planning to any of these types of migrations, or if you're evaluating the opportunity to do so in the future and want to explore what it might look like.

This document is part of the following multi-part series about migrating to Google Cloud:

  * [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
  * [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads)
  * [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation)
  * [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)
  * [Migrate to Google Cloud: Deploy your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads)
  * [Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments](https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments)
  * [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment)
  * [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices)
  * Migrate to Google Cloud: Minimize costs (this document)



This document provides guidance about the following topics:

  * Assessing your current costs and projecting the growth of your Google Cloud footprint.
  * Establishing your cost reduction requirements and goals.
  * Implementing cost governance and reduction processes.
  * Adopting the cloud FinOps framework.



This document assumes that you've read and are familiar with [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment). That document describes the steps to design and implement an _optimization loop_ (a continuing and ongoing optimization process) after a migration to Google Cloud. Those optimization steps are largely applicable to minimizing costs as well.

## Assess your costs

Assessing the current and projected costs of your Google Cloud environments is essential to develop a comprehensive understanding of your resource consumption, and where potential growth opportunities might lie.

To assess your current and projected costs, you can do the following:

  * Assess the cost of your current Google Cloud environments.
  * Assess the cost of future migrations across Google Cloud regions.
  * Project the growth of your Google Cloud footprint.



### Assess the cost of your current environments

To gather a comprehensive understanding of the costs of your environments, consider the following:

  * **Google Cloud billing model**. Google Cloud uses a transparent and efficient model to bill resource usage. To fully understand how the model works and how Google Cloud bills you for resource consumption, we recommend that you learn how the [Google Cloud billing model](https://cloud.google.com/pricing) and [product pricing](https://cloud.google.com/pricing/list) work.
  * **Cloud Billing**. To assess the current and projected costs of your environments, we recommend that you use [Cloud Billing](https://docs.cloud.google.com/billing/docs/concepts), a collection of tools that help you track your current and projected Google Cloud spending, pay your bill, and optimize your costs. For example, you can create [budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets) and [budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets-notification-recipients).
  * **Discounts**. Google Cloud [offers discounted prices](https://docs.cloud.google.com/docs/cuds) in exchange for your commitment to use a minimum level of resources for a specified term. When assessing the cost of your current environments, we recommend that you gather information about the committed use discounts that you purchased and the products, services, and resources to which they apply.
  * **Carbon footprint**. Google Cloud supports [measuring and reporting the carbon footprint of your current environments](https://docs.cloud.google.com/carbon-footprint). Gathering this information is useful to establish a baseline from which you can reduce your carbon footprint as part of your cost minimization efforts.



For more information about how to set up resources for access control and cost management, see [Guide to Cloud Billing resource organization & access management](https://docs.cloud.google.com/billing/docs/onboarding-checklist).

### Assess the cost of future migrations across regions

If you're considering a migration across Google Cloud regions, we recommend that you assess how this migration might affect your costs. To assess how much a migration across regions might cost, consider the following:

  * **The price of Google Cloud resources in the target region**. When migrating your workloads, data, and processes across Google Cloud regions, you will likely need to provision resources in the target region. You can use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator) to assess how much it might cost to provision new resources and migrate data to a new Google Cloud region.
  * **The cost of multi-region Google Cloud resources**. To meet your reliability requirements, you might need to use multi-region resources. We recommend that you consider how those resources might affect the migration and its costs. For example, you're using [dual- or multi-region Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/locations), and one of these buckets is in the same region as your target migration region. In this case, you might not need to migrate data in those buckets because Cloud Storage handles data replication for you.
  * **The egress network traffic**. Besides the cost of provisioning and maintaining Google Cloud resources, transferring data from one region to another might incur [network egress costs](https://cloud.google.com/vpc/network-pricing). We recommend assessing these projected costs to avoid unanticipated billings.
  * **The time, training, and other collateral costs**. The cost of migrating across regions involves more than the costs related to resource provisioning and data transfers. There are also collateral costs, such as the time and training needed for your teams to design a migration plan and complete the migration. When assessing your migration costs, we recommend that you account for your collateral costs as well.



On top of these recommendations, Google Cloud offers the [Google Cloud rapid assessment and migration program](https://docs.cloud.google.com/solutions/cloud-migration-program). This program provides you with free migration cost assessments, and guides you through the whole migration process with the support of Google Cloud professional services and partners.

### Project the growth of your Google Cloud footprint

As part of regular environment maintenance, we recommend that you continuously monitor the costs of your environments. This type of monitoring provides the information that you need to establish cost governance processes. Such monitoring also keeps you informed of the current costs of your environments and their short-term projection.

In addition to regularly maintaining your environments, we also recommend that you develop a long-term growth strategy. Such a strategy lets you better plan your budgets and the resources that are required for your Google Cloud footprint to grow organically with your business needs. To develop a long-term growth strategy, consider the following:

  * **Business requirements**. Evaluate whether your environments are still inline with the business requirements that they are designed to support. For example, if you foresee an increase in demand in certain business areas, you might consider your options to grow the environments that support those areas.
  * **Trends and patterns**. Use the [Google Cloud Observability](https://cloud.google.com/products/operations) to evaluate the monitoring, logging, and performance profiling data that are associated with your workloads, data, and processes. From this evaluation, you can discover trends, derive demand and traffic patterns, and gather useful insights about these trends.
  * **Sustainable growth**. Evaluate how much growth your current environments can sustain, and at what point you might need to design, provision, and configure additional environments. For example, if the costs of growing an existing environment outweigh the benefits to gain from that growth, you might consider provisioning a new environment instead. When evaluating how much growth your current environments can sustain, consider the affect of this growth on the carbon footprint of your environments. To learn more, see [Carbon Footprint](http://cloud.google.com/carbon-footprint/).



## Establish your cost reduction requirements and goals

After projecting the growth of your Google Cloud footprint, we recommend that you establish the following:

  1. **Cost reduction requirements**. A _requirement_ expresses a need for improvement and doesn't necessarily have to be measurable. By establishing these requirements, you indicate the areas where you want to focus your cost reduction efforts.
  2. **Cost reduction goals**. A _goal_ is a measurable property that might contribute to one or more requirements. By establishing measurable goals, you make your cost reduction efforts measurable themselves, and you can continuously evaluate your current stance against those goals.



For more information about requirements and goals and their definition, see [Establishing your optimization requirements and goals](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment#establishing_your_optimization_requirements_and_goals).

To establish your cost reduction requirements, we recommend that you start by defining what types of costs need to be improved in your environments. For example, a cost reduction requirement might be to reduce the cost of computing services.

After establishing your cost reduction requirements and validating their feasibility, you define measurable cost reduction goals for each requirement. The set of goals relevant to a requirement should let you completely define all the characteristics of that requirement, and should let you measure your progress towards meeting that requirement. For example, consider the previous cost reduction requirement about reducing the cost of computing services. For this requirement, you might define a cost reduction goal of reducing the costs of your Compute Engine instances by 5%.

After establishing your cost reduction requirements and goals, we recommend that you evaluate the feasibility of each requirement by relying on data gathered during the cost assessment phase. For example, you can use assessment data to evaluate the feasibility of the previous cost reduction goal to reduce the costs of Compute Engine instances by 5%. That is, use the assessment data to evaluate whether you can hit that goal by small refactorings to your environments and processes, or whether you need to heavily modify their design instead.

## Implement cost governance and reduction processes

During the cost assessment phase, you gathered information about your current and short term spending. Then, by establishing your cost reduction requirements and goals, you outlined the way forward to reduce costs. Both activities are necessary to develop long-term strategies to reduce costs, and to grow your Google Cloud footprint and the business it supports. However, those activities alone don't address implementation. To implement those strategies, you also need cost governance and reduction processes.

You should approach these cost governance and reduction processes in the following order:

  1. Monitor costs.
  2. Control resource provisioning.
  3. Reduce costs.



### Monitor costs

To maintain control over your costs, it's essential to continuously monitor the billing and cost trends of your environments. We recommend that you do the following:

  1. **Regularly review billing reports**. Cloud Billing [provides built-in reports](https://docs.cloud.google.com/billing/docs/reports) about your usage costs, the details about your invoices and statements, cost breakdowns, and pricing tables. To maintain a current and comprehensive understanding of your costs, we recommend that you regularly review these billing reports. If you need to gather further insights beyond what the built-in Cloud Billing reports provide, you can [export billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) for further analysis.
  2. **Configure labels and tags**. [_Labels_](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) and [_tags_](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) are key-value pairs that you can attach to your Google Cloud resources. You can use these key-value pairs to implement your own cost tracking and analysis reports on top of what Cloud Billing provides. For example, you can [break down costs by label](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-with-labels), or perform [chargebacks, audits, and other costs allocation analysis by tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags). For more information about how labels and tags compare, see [Tags and labels](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels).
  3. **Configure budget alerts**. [Budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) can help you track your actual costs and how they compare against planned costs. To avoid unanticipated costs, we recommend that you set up budget and budget alerts to provide you with enough time to promptly act.



### Control resource provisioning

Google Cloud supports various resource provisioning tools, such as [Google Cloud console](https://docs.cloud.google.com/cloud-console), [Google Cloud SDK](https://docs.cloud.google.com/sdk), [Cloud APIs](https://docs.cloud.google.com/apis), and [Terraform providers, modules, and resources](https://docs.cloud.google.com/docs/terraform). Users in your organization can use these tools to provision resources in your environments. Provisioning additional Google Cloud resources or scaling existing ones up or down might incur changes in your spending. For more information, see the [pricing for each resource](https://cloud.google.com/pricing/list).

To avoid uncontrolled and unanticipated spending, we recommend that you design and implement processes to control resource provisioning. To implement these processes, consider the following:

  * **Adopt infrastructure as code**. By managing your infrastructure as code, you can manage the provisioning and configuration of your Google Cloud resources as you would handle application code. You can also take advantage of your existing continuous integration, continuous deployment, and audit processes. For example, you can [manage your infrastructure as code with Terraform](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code), and you can [enforce policy compliance as part of your continuous integration pipeline](https://docs.cloud.google.com/docs/terraform/policy-validation).
  * **Review changes before applying them**. To avoid unanticipated changes in spending, we recommend that you implement processes to review changes to your environments before applying them, regardless of the tool that you use to provision and scale Google Cloud resources. For example, if you adopt infrastructure as code, you can add a mandatory human review step before applying any substantial change to the Google Cloud resources that support your environments.
  * **Document your environments and detect drift**. When provisioning and configuring your Google Cloud environments, we recommend that you document the following for each environment:

    * The environment's characteristics.
    * The Google Cloud resources that you provision and configure in that environment.
    * The preferred state for each of those resources.

Documenting the characteristics of your environments makes auditing the current state of your environments easier. Documentation also lets you design and implement processes to detect any drift from the preferred state, and take corrective actions as soon as possible. For example, you can use [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory) to analyze all your Google Cloud assets across projects and services. You can then compare that analysis against the preferred state of each environment, proactively decommission any unmanaged resources, and bring managed resources back to their preferred state.

  * **Configure Organizational policies**. To configure controls and restrictions on how your organization's resources can be used, and to avoid misuse that might lead to unintended charges, you can use the [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to enforce [constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints). For example, you might restrict the usage of certain Google Cloud products, or you might restrict the creation of certain resources. For more information about the constraints that Google Cloud supports, refer to [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

  * **Configure quotas**. Google Cloud uses [quotas](https://docs.cloud.google.com/docs/quotas/overview) to restrict how much of a shared Google Cloud resource that you can use. To limit the use of particular resources, you can [set your own quota limits up to a cap](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage). For example, you can prevent creating Compute Engine instances over a certain number by limiting how many [Compute Engine instances can exist in a given region](https://docs.cloud.google.com/compute/resource-usage#vm_instance_quota).

  * **Adopt least privilege access methods**. To avoid privilege escalation issues where users of your Google Cloud resources elevate their privileges and bypass reviews, we recommend that you grant the least amount of privileges to users and service accounts. For example, you can [grant the minimum privileges necessary to users and service accounts using IAM](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).




### Reduce costs

Monitoring the costs of your environments and implementing processes to control resource provisioning help you with the following:

  * Controlling the current and projected costs of your environments.
  * Avoiding unanticipated and uncontrolled costs.
  * Providing a cost basis that you can use when trying to reduce costs.



In this document, _reducing costs_ means designing and implementing processes and mechanisms to meet your cost reduction goals. You can design these processes to be _reactive_ (act as a consequence of another action or status change), or _proactive_ (act anticipating other actions or status changes). Often, the recommendations in this section are applicable to both reactive and proactive processes. Also, many cost reduction processes can be both.

To design and implement cost reduction processes, consider the following recommendations:

  * **Evaluate usage discounts**. Google Cloud offers several options to reduce your costs based on your usage patterns of Google Cloud resources. For example, you can get access to discounted prices in exchange for your commitment to use a minimum level of resources for a specified term with [committed use discounts](https://docs.cloud.google.com/docs/cuds). Some Google Cloud services offer discounts on resources that you use for a certain amount of time or level. For example, Compute Engine offers [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) on resources that are used for more than a certain period of the billing cycle.
  * **Decommission unneeded resources**. As your business requirements change over time, the environments that support those business requirements evolve as well. As part of this evolution, your environments might end up with unneeded resources, or resources that scale to unnecessary levels. To reduce usage costs associated with unneeded resources, we recommend that you both assess the affect of each unneeded resource on your costs and how decommissioning those resources might affect your environments. For example, you can view and apply [idle resources recommendations](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations) and [idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations) to identify unused resources and Compute Engine instances, and eventually decommission them.
  * **Rightsize over provisioned resources**. To avoid underutilizing the Google Cloud resource that you provisioned and configured, we recommend that you both assess your environments to evaluate whether there are resources that you might need to rightsize. Rightsizing resources might lead to cost reductions. For example, you can use the data that Google Cloud Observability provides to assess how much of a particular resource that you're using and whether there's room to rightsize those resources. Another example of rightsizing resources would be to [apply machine type recommendations for Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances).
  * **Configure automatic scaling**. Many Google Cloud services support automatically scaling resources up and down according to demand. Automatic scaling (also known as autoscaling) helps you reduce costs by scaling Google Cloud resources to match your current demand. For example, Compute Engine offers [autoscaling](https://docs.cloud.google.com/compute/docs/load-balancing-and-autoscaling) to automatically add and remove instances to [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) based on load.
  * **Migrate to managed services**. To help you reduce operational costs and [eliminate toil](https://landing.google.com/sre/sre-book/chapters/eliminating-toil/), consider migrating from self-managed services to Google-managed services. Google accumulated decades of experience in running planet-scale, globally distributed systems, and makes this expertise available to Google Cloud customers when they use managed Google Cloud services. For example, if you're running a self-managed Kubernetes cluster on Compute Engine, you might consider [migrating to Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/architecture/migrating-containers-kubernetes-gke). Migrating to GKE might free up resources that your operations teams can direct to other efforts, such as increasing the efficiency of your environments and reducing their costs.
  * **Derive patterns**. On top of the autoscaling features that Google Cloud offers, you can also assess the data that Google Cloud Observability provides to derive usage and traffic patterns that help you build resource demand models. Building these models might help you design and implement proactive cost reduction processes that take advantage of the insights provided by these models. For example, you might find out that some of your environments receive heavy demand only during certain periods of the day or the week. Thus, you can proactively scale up those environments in anticipation of those periods, and scale them down when they aren't needed.
  * **Schedule low-priority workloads efficiently**. Usually, not every workload running in your environments is high-priority and business-critical. To reduce costs, you can take advantage of the non-critical nature of those workloads. For example, you can shut down those workloads and their related resources when they are not needed. Alternatively, you can run them in more affordable runtime environments, such as [Spot VMs](https://cloud.google.com/solutions/spot-vms), instead of running them in Compute Engine or GKE.
  * **Manage the data lifecycle**. Data stored in your environments can grow to significant amounts in short periods of time. To help you reduce costs, we recommend that you design and implement processes to automatically manage the lifecycle of your data just as you do with your Google Cloud resources. For example, you can design and implement processes to delete unneeded data. Or you might generate aggregate data from more detailed data and move only the aggregate data into long-term storage. Or you might even consider moving data that you need less frequently to less expensive systems designed for infrequent access. Also, some Google Cloud services support automated object lifecycle management. For example, Cloud Storage offers [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to automate typical lifecycle management actions on objects and the [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass) to automatically transition objects to appropriate storage classes based on each object's access pattern.
  * **Reduce costs of specific Google Cloud services**. Google Cloud provides guidance to reduce and optimize your costs when using specific Google Cloud services such as Compute Engine, GKE, and Cloud Storage. For more information about optimizing costs of specific Google Cloud products, see [Google Cloud Well-Architected Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization).



The previous recommendations are applicable regardless of how your Google Cloud resources are distributed across regions and zones. To learn about how to reduce costs of your single-region and multi-region environments, continue reading this document.

#### Reduce costs of single-region environments

In single-region environments, Google Cloud resources are typically distributed across multiple zones in only that region. Distributing resources across multiple zones in a region helps you to reduce the effects of zonal outages, and thereby, help minimize the affect that these outages can have on your business. For example, if you run a workload on a Compute Engine instance, and there's a zonal outage that affects the zone where you provisioned that instance, that workload might be affected by the outage. If you have multiple replicas of that workload running on Compute Engine instances in different regions, that workload is less likely to suffer due to a zonal outage. Usually, replicating resources across multiple zones costs more than provisioning resources in a single zone but potentially helps provide better reliability.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

For more information, see [Migrate across Google Cloud regions: Design resilient single-region environments on Google Cloud](https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments).

When designing your single-region environments, we recommend that you assess the reliability requirements of your workloads, processes, and data. This assessment can help you decide which Google Cloud resources you need to replicate and distribute across multiple zones in a region, and which ones tolerate zonal outages and are fine in a single zone. For example, you might consider a zonal deployment for non-business critical batch workloads, and a multi-zone replication and distribution for more critical workloads, processes, and data.

#### Reduce the costs of multi-region environments

In multi-region environments, Google Cloud resources are typically distributed across multiple regions. Distributing resources across multiple regions helps reduce the affect of regional outages. For example, if you use a [multi-region Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/locations#considerations), your data is replicated across multiple regions, and has a better availability compared to regional buckets.

In addition to the recommendations in this section, consider the ones described in Reduce costs of single-region environments because they are applicable for multi-region environments as well.

To reduce the costs of multi-region environments, consider the following:

  * **Multi-region resources**. Several Google Cloud products support replicating and distributing resources across multiple regions to increase the reliability of your environments. For example, Cloud Storage supports [dual-region and multi-region buckets](https://docs.cloud.google.com/storage/docs/locations#considerations) to replicate your data across multiple regions. Usually, replicating and distributing resources across regions costs more than provisioning resources in a single region. For example, Google Cloud bills dual- and multi-region Cloud Storage buckets with [different prices](https://cloud.google.com/storage/pricing) compared to single-region buckets, and charges for [inter-region replication](https://cloud.google.com/storage/pricing#inter-region-replication).

To minimize product costs, we recommend that you consider using multi-region replication and distribution only when needed to meet the reliability requirements of your workloads, data, and processes. For example, you've determined that the data to be stored in a specific Cloud Storage bucket doesn't need to be distributed across multiple regions to mitigate the effects of a regional outage. For this data, you can save costs by provisioning a single-region bucket to store this data instead of provisioning a dual- or a multi-region bucket. Another cost savings example would be if you have a non-business critical workload that doesn't need the increased reliability provided by a multi-region deployment. You could consider deploying that workload to a single-region or even single zone.

  * **Region-specific prices**. You can provision Google Cloud resources in several regions. Prices for these resources can vary by region. For example, [Compute Engine instance prices](https://cloud.google.com/compute/vm-instance-pricing) differ from region to region. You might be able to deploy some of your workloads, data, and processes to a region where they are the cheapest if those resources meet these requirements:

    * Those workloads, data, and processes can tolerate the added latency that incurs when provisioning resources on which they depend in other regions.
    * Those workloads, data, and processes aren't subject to regulatory requirements that force you to provision these resources in particular regions.

Before trying to reduce costs by provisioning resources in other regions, assess whether or not the cost of the resulting inter-region network traffic negates the cost reduction of using region-specific pricing.

  * **Network egress costs**. Google Cloud charges for [network traffic between regions as egress traffic](https://cloud.google.com/vpc/network-pricing). To reduce costs, we recommend that you minimize the inter-region network traffic by concentrating closely-related Google Cloud resources that need to exchange data in the same region. For example, the workload that you have deployed on a Compute Engine instance needs access to the data stored in a Cloud Storage bucket. You can avoid inter-region traffic if you provision that Compute Engine instance in a region where the bucket replicates data.




### Minimize the costs of migrations across Google Cloud regions

Migrating your environments and Google Cloud resources across regions helps you expand your environments to multiple regions, and also help you achieve compliance with regulatory requirements that mandate resource locality.

For more information about migrating across regions, see [Migrate across Google Cloud regions: Get started](https://docs.cloud.google.com/architecture/migrate-across-regions)

In addition to the recommendations in this section, consider the ones described in Reduce costs of multi-region environments because they are applicable to reduce the costs of migrations across Google Cloud regions as well.

To reduce the costs of a migration across Google Cloud regions, consider the following:

  * **Data replication**. When evaluating your options to migrate data from one region to another, we recommend that you consider both a self-managed migration and the replication features that several Google Cloud products support. For example, you need to migrate data stored in a regional Cloud Storage bucket across regions. You can assess and compare the costs of [migrating that data in another single-region bucket in the target region](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#options_available_from_google) to those of migrating that data in a multi-region bucket and having Cloud Storage handle the data replication across regions.
  * **Data migration strategy**. When evaluating a [data migration strategy](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#data_migration_approaches) to migrate data across Google Cloud regions, we recommend that you consider the strategies that let you minimize migration costs. For example, your workloads might start writing data to both the source region and to the target migration region by adopting a [Y (writing and reading) strategy](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#y_writing_and_reading). With this strategy, you'll need to only transfer historical data during the migration.



For more information about migrating data across Google Cloud regions, see [Migration to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets). That document is about migrating data from other cloud providers and on premises environments to Google Cloud but it's also applicable to migrating data across regions.

## Adopt the cloud FinOps framework

The guidance in this document aims at designing and implementing mechanisms and processes to monitor and govern costs, and to reduce expenditure inefficiencies, and it's designed so that you incrementally follow it to bring your cloud expenditure under control.

When you're ready, you can adopt the cloud FinOps framework. Adopting this framework is a transformational change that brings technology, finance, and business together to drive financial accountability and accelerate business value realization.

For more information about the cloud FinOps framework, see [Getting Started with FinOps on Google Cloud](https://services.google.com/fh/files/misc/cloud_finops_getting_started.pdf).

## What's next

  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-11-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-11-20 UTC."],[],[]] 
