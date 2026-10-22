---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/manage-costs-attributions/
title: Manage costs and attributions for the developer platform \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:09.593412+00:00
---

# Manage costs and attributions for the developer platform  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/manage-costs-attributions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Manage costs and attributions for the developer platform Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

To manage costs in GKE, you must plan, continuously monitor, and optimize your environment. This section describes how you can manage the GKE costs that are associated with the blueprint.

## Proactive costs planning

To plan your costs proactively, you must set clear cost expectations for your GKE workloads. Requirements can include many factors, such as the number and type of VMs used, the level of network traffic, the rate of logging, and the frequency of builds. After you set your cost expectations, you can [set budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) on your projects, as described in the enterprise foundation blueprint.

To attribute costs between workloads, you must consider how different resource types have different granularities of cost attribution. For example, consider the following:

  * **Project costs:** Some projects contain resources that are associated with a single tenant. The cost of a single project is attributed to a cost center using metadata labels in billing exports.
  * **Multi-tenant cluster costs:** Some projects contain GKE clusters that are shared by multiple tenants. [GKE cost allocation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations) provides a granular breakdown of costs in billing exports for each namespace or label on Kubernetes resources.
  * **Shared costs:** Some projects include shared resources that support many tenants, but billing reports can't granularly attribute usage to individual tenants. We recommend that you treat these as a shared cost of the developer platform. Depending on your internal processes for cost attribution, you might assign this to a shared IT cost center or split the cost proportionally among cost centers based on the number of workloads that use the platform.



The following shows which projects are associated with which type of cost attribution.

Project | Description | Types of charges  
---|---|---  
`eab-infra-cicd` | Automation workflow project | Shared costs  
`eab-app-factory` | Application factory project | Shared costs  
`eab-gke-{env}` | Virtual machines and persistent disks for GKE | Multi-tenant cluster costs  
Network load balancer and traffic charges incurred by applications on GKE | Shared costs  
Logging and monitoring | Shared costs  
`eab-{tenant}` | CI/CD and application-owned resources, such as AlloyDB for PostgreSQL | Project costs  
  
## Continuous resource monitoring

After you set a cost baseline for your GKE clusters, use Cloud Monitoring to monitor the use of your GKE clusters and look for underutilized resources as areas for [potential optimization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics). In this blueprint, all costs are billed to a centralized billing account. To export your costs and do detailed analysis of your GKE billing usage, you can use [Cloud Billing BigQuery exports](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup), as described in the enterprise foundation blueprint.

## Optimization techniques

After you create an operating baseline for your applications, you can apply different [optimization techniques](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke) to the environment. These optimization techniques are designed to help reduce your costs.

## What's next

  * Read about [deployment methodology](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
