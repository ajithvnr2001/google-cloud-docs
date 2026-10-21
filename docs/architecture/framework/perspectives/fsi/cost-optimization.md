---
url: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/cost-optimization/
title: Financial services perspective: Cost optimization \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:23.991327+00:00
---

# Financial services perspective: Cost optimization  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/cost-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Financial services perspective: Cost optimization Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-28 UTC

This document in the [Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi) provides an overview of principles and recommendations to optimize the cost of your FS workloads in Google Cloud. The recommendations in this document align with the [cost optimization pillar](https://docs.cloud.google.com/architecture/framework/cost-optimization) of the Well-Architected Framework.

Robust cost optimization for financial services workloads requires the following fundamental elements:

  * The ability to identify wasteful versus value-driving resource utilization.
  * An embedded culture of financial accountability.



To optimize cost, you need a comprehensive understanding of the cost drivers and resource needs across your organization. In some large organizations, especially those that are early in the cloud journey, a single team is often responsible for optimizing spend across a large number of domains. This approach assumes that a central team is best placed to identify high-value opportunities to improve efficiency.

The centralized approach might yield some success during the initial stages of cloud adoption or for non-critical workloads. However, a single team can't drive cost optimization across an entire organization. When the resource usage or the level of regulatory scrutiny increases, the centralized approach isn't sustainable. Centralized teams face scalability challenges particularly when dealing with a large number of financial products and services. The project teams that own the products and services might resist changes that are made by an external team.

For effective cost optimization, spend-related data must be highly visible, and engineers and other cloud users who are close to the workloads must be motivated to take action to optimize cost. From an organizational standpoint, the challenge for cost optimization is to identify what areas should be optimized, identify the engineers who are responsible for those areas, and then convince them to take the required optimization action. This document provides recommendations to address this challenge.

The cost optimization recommendations in this document are mapped to the following core principles:

  * Identify waste by using Google Cloud tools
  * Identify value by analyzing and enriching spend data
  * Allocate spend to drive accountability
  * Drive accountability and motivate engineers to take action
  * Focus on value and TCO rather than cost



## Identify waste by using Google Cloud tools

Google Cloud provides several products, tools, and features to help you identify waste. Consider the following recommendations.

### Use automation and AI to systematically identify what to optimize

[Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist) provides intelligent recommendations across services such as [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) for microservices, [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) for data analytics, [Compute Engine](https://docs.cloud.google.com/compute/docs/overview) for core applications, and [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) for relational databases. Active Assist recommendations are provided at no cost and without any configuration by you. The recommendations help you to identify idle resources and underutilized commitments.

### Centralize FinOps monitoring and control through a unified interface

[Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports) and the [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub) let you implement comprehensive cost monitoring. This comprehensive view is vital for financial auditors and internal finance teams to track cloud spend, assess the financial posture, evaluate FinOps maturity across various business units or cost centers, and provide a consistent financial narrative.

## Identify value by analyzing and enriching spend data

Active Assist is effective at identifying obvious waste. However, pinpointing value can be more challenging, particularly when workloads are on unsuitable products or when the workloads lack clear alignment with business value. For FS workloads, business value extends beyond cost reduction. The value includes risk mitigation, regulatory adherence, and gaining competitive advantages.

To understand cloud spend and value holistically, you need a complete understanding at multiple levels: where the spend is coming from, what business function the spend is driving, and the technical feasibility of refactoring or optimizing the workload in question.

The following diagram shows how you can apply the [data-information-knowledge-wisdom (DIKW) pyramid](https://en.wikipedia.org/wiki/DIKW_pyramid) and Google Cloud tools to get a holistic understanding of cloud costs and value.

![The data-information-knowledge-wisdom \(DIKW\) pyramid shows how to use cloud spending data to inform decisions.](https://docs.cloud.google.com/static/architecture/framework/perspectives/fsi/images/gcwaf-fsi-cost-optimization-dikw-pyramid.svg)

The preceding diagram shows how you can use the DIKW approach to refine raw cloud spending data into actionable insights and decisions that drive business value.

  * **Data** : In this layer, you collect raw, unprocessed streams of usage and cost data for your cloud resources. Your central FinOps team uses tools like Cloud Billing invoices, billing exports, and Cloud Monitoring to get granular, detailed data. For example, a data point could be that a VM named `app1-test-vmA` ran for 730 hours in the `us-central1` region and cost USD 70.
  * **Information** : In this layer, your central FinOps team uses tools like Cloud Billing reports and the FinOps Hub to structure the raw data to help answer questions like "What categories of resources are people spending money on?" For example, you might find out that a total of USD 1,050 was spent on VMs of the machine type n4-standard-2 across two regions in the US.
  * **Knowledge** : In this layer, your central FinOps team enriches information with appropriate business context about _who_ spent money and for _what purpose_. You use mechanisms like tagging, labeling, resource hierarchy, billing accounts, and custom Looker dashboards. For example, you might determine that the `app1` testing team in the US spent USD 650 during the second week of July as part of a stress testing exercise.
  * **Wisdom** : In this layer, your product and application teams use the contextualized knowledge to assess the business value of cloud spending and to make informed, strategic decisions. Your teams might answer questions like the following: 
    * Is the USD 5,000 that was spent on a data analytics pipeline generating business value?
    * Could we re-architect the pipeline to be more efficient without reducing performance?



Consider the following recommendations for analyzing cloud spend data.

### Analyze spend data that's provided by Google Cloud

Start with detailed Cloud Billing data that's [exported to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) and data that's available in [Monitoring](https://cloud.google.com/products/observability) logs. To derive actionable insights and make decisions, you need to structure this data and enrich it with business context.

### Visualize data through available tooling

Augment the built-in Google Cloud dashboards with custom reporting by using tools like [Data Studio](https://cloud.google.com/looker/docs/studio) on top of BigQuery exports. Finance teams can build custom dashboards that contextualize cloud spend against financial metrics, regulatory reporting requirements, and business unit profitability. They can then provide a clear financial narrative for analysis and decision making by executive stakeholders.

## Allocate spend to drive accountability

After you understand what's driving the cloud spend, you need to identify who is spending money and why. This level of understanding requires a robust cost-allocation practice, which involves attaching business-relevant metadata to cloud resources. For example, if a particular resource is used by the Banking-AppDev team, you can attach a tag like `team=banking_appdev` to the resource to track the cost that the team incurs on that resource. Ideally, you should allocate 100% of your cloud costs to the source of the spending. In practice, you might start with a lower target because building a metadata structure to support 100% cost allocation is a complex effort.

Consider the following recommendations to develop a metadata strategy to support cost allocation:

  * **Validity** : Ensure that the tags help to identify business-related key performance indicators (KPIs) and regulatory requirements. This association is critical for internal chargebacks, regulatory reporting, and aligning cloud spend with business-unit goals. For example, the following tags clearly identify a spending team, their region, and the product that they work on: `team=banking_appdev`, `region=emea`, `product=frontend`.
  * **Automation** : To achieve a high level of tagging compliance, enforce tagging through automation. Manual tagging is prone to errors and inconsistency, which are unacceptable in FS environments where auditability and financial accuracy are paramount. Automated tagging ensures that resources are correctly categorized when they're created.
  * **Simplicity** : Measure simple, uncorrelated factors. FS environments are complex. To ensure that cost-allocation rules in such an environment are easy to understand and enforce, the rules must be as simple as possible. Avoid overengineering the rules for highly specific (_edge_) cases. Complex rules can lead to confusion and resistance from operational teams.



After you define an allocation strategy by using tags, you need to decide the level of granularity at which the strategy should be implemented. The required granularity depends on your business needs. For example, some organizations might need to track cost at the product level, some might need cost data for each cost center, and others might need cost data per environment (development, staging, and production).

Consider the following approaches to achieve the appropriate level of cost-allocation granularity for your organization:

  * Use the [project hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) in Google Cloud as a natural starting point for cost allocation. Projects represent points of policy enforcement in Google Cloud. By default, IAM permissions, security policies, and cost are attributed to projects and folders. When you review cost data that's exported from Cloud Billing, you can view the folder hierarchy and the projects that are associated with the cost data. If your Google Cloud resource hierarchy reflects your organization's accountability structure for spend, then this is the simplest way to implement cost allocation.
  * Use [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) and [labels](https://docs.cloud.google.com/compute/docs/labeling-resources) for additional granularity. They provide flexible ways to categorize resources in billing exports. Tags and labels facilitate detailed cost breakdowns by application and environment.



Often, you might need to use the project hierarchy combined with tagging and labeling for effective cost allocation. Regardless of the cost-allocation approach that you choose, follow the recommendations that were described earlier for developing a robust metadata strategy: validitation, automation, and simplicity.

## Drive accountability and motivate engineers to take action

The cloud FinOps team is responsible for driving an organization to be conscious of costs and value. The individual product teams and engineering teams must take the required actions for cost optimization. These teams are also accountable for the cost behavior of the financial services workloads and for ensuring that their workloads provide the required business value.

Consider the following recommendations to drive accountability and motivate teams to optimize cost.

### Establish a centralized FinOps team for governance

Cloud FinOps practices don't grow organically. A dedicated FinOps team must define and establish FinOps practices by doing the following:

  * Build the required processes, tools, and guidance.
  * Create, communicate, and enforce the necessary policies, such as mandatory tagging, budget reviews, and optimization processes.
  * Encourage engineering teams to be accountable for cost.
  * Intervene when the engineering teams don't take on ownership for costs.



### Get executive sponsorship and mandates

Senior leadership, including the CTO, CFO, and CIO, must actively champion an organization-wide shift to a FinOps culture. Their support is crucial for prioritizing cost accountability, allocating resources for the FinOps program, ensuring cross-functional participation, and driving compliance with FinOps requirements.

### Incentivize teams to optimize cost

Engineers and engineering teams might not be self-motivated to focus on cost optimization. It's important to align team and individual goals with cost efficiency by implementing incentives such as the following:

  * Reinvest a portion of the savings from cost optimization in the teams that achieved the optimization.
  * Publicly recognize and celebrate cost optimization efforts and successes.
  * Use gamification techniques to reward teams that effectively optimize cost.
  * Integrate efficiency metrics into performance goals.



### Implement showback and chargeback techniques

Ensure that teams have clear visibility into the cloud resources and costs that they own. Assign financial responsibility to the appropriate individuals within the teams. Use formal mechanisms to enforce rigorous tagging and implement transparent rules for allocating shared costs.

## Focus on value and TCO rather than cost

When you evaluate cloud solutions, consider the long-term total cost of ownership (TCO). For example, self-hosting a database for an application might seem to be cheaper than using a managed database service like [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction). However, to assess the long-term value and TCO, you must consider the hidden costs that are associated with self-hosted databases. Such costs include the dedicated engineering effort for patching, scaling, security hardening, and disaster recovery, which are critical requirements for FS workloads. Managed services provide significantly higher long-term value, which offsets the infrastructure costs. Managed services provide robust compliance capabilities, have built-in reliability features, and can help to reduce your operational overhead.

Consider the following recommendations to focus on value and TCO.

### Use product-specific techniques and tools for resource optimization

Leverage cost-optimization tools and features that are provided by Google Cloud products, such as the following:

  * Compute Engine: [Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler), [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), and [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  * GKE: [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
  * Cloud Storage: [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) and [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass)
  * BigQuery: [Capacity-based pricing](https://cloud.google.com/bigquery/pricing#capacity_compute_analysis_pricing) and [cost-optimization techniques](https://docs.cloud.google.com/bigquery/docs/best-practices-costs)
  * Google Cloud VMware Engine: committed use discounts (CUDs), optimized storage, and other [cost optimization strategies](https://docs.cloud.google.com/vmware-engine/docs/best-practices-costs)



### Take advantage of discounts

Ensure that the billing rate for your cloud resources is as low as possible by using discounts that Google offers. The individual product and engineering teams typically manage resource optimization. The central FinOps team is responsible for optimizing billing rates because they have visibility into resource requirements across the entire organization. Therefore, they can aggregate the requirements and maximize the commitment-based discounts.

You can take advantage of the following types of discounts for Google Cloud resources:

  * Enterprise discounts are negotiated discounts based on your organization's commitment to a minimum total spend on Google Cloud at a reduced billing rate.
  * [Resource-based CUDs](https://docs.cloud.google.com/docs/cuds#resource_based_commitments) are in exchange for a commitment to use a minimum quantity of Compute Engine resources over a one-year period or a three-year period. Resource-based CUDs are applicable to the resources that are in a specific region. For most Cloud Billing accounts, Google Cloud enables [resource-based CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#cud-scope-configuration) and shares CUDs across all projects that are associated with that account.
  * [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds#spend_based_commitments) are in exchange for a commitment to spend a minimum amount of money on a particular product over a one-year period or a three-year period. Spend-based discounts are applicable at the billing account level. The discounts are applied regionally or globally depending on the product.



You can achieve significant savings by using CUDs on top of enterprise discounts.

In addition to CUDs, use the following approaches to reduce billing rates:

  * Use [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) for fault-tolerant and flexible workloads. Spot VMs are more than 80% cheaper than regular VMs.
  * BigQuery offers multiple pricing models, which include [on-demand pricing](https://cloud.google.com/bigquery/pricing#on_demand_pricing) and [edition-based pricing](https://docs.cloud.google.com/bigquery/docs/editions-intro) that's based on commitments and autoscaling requirements. If you use a significant volume of BigQuery resources, choose an appropriate edition to reduce the cost per slot for analytics workloads.
  * Carefully evaluate the available Google Cloud regions for the services that you need to use. Choose regions that align with your cost objectives and factors like latency and compliance requirements. To understand the trade-offs between cost, sustainability, and latency, use the [Google Cloud Region Picker](https://cloud.withgoogle.com/region-picker/).



[ Previous arrow_back  Reliability  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/reliability)

[ Next Performance optimization  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/performance-optimization)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
