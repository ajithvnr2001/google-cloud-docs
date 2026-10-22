---
url: https://docs.cloud.google.com/architecture/framework/sustainability/continuously-measure-improve/
title: Continuously measure and improve sustainability \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:41.414588+00:00
---

# Continuously measure and improve sustainability  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/sustainability/continuously-measure-improve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Continuously measure and improve sustainability Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-28 UTC

This principle in the sustainability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability) provides recommendations to help you measure and continuously improve the sustainability of your workloads in Google Cloud.

## Principle overview

To ensure that your cloud workloads remain sustainable, you need accurate and transparent metrics. Verifiable metrics let you translate sustainability goals to actions. Every resource that you create in the cloud has an associated carbon footprint. To build and maintain sustainable cloud architectures, you must integrate the measurement of carbon data into your operational feedback loop.

The recommendations in this section provide a framework for using [Carbon Footprint](https://cloud.google.com/carbon-footprint) to quantify carbon emissions, identify carbon hotspots, implement targeted workload optimizations, and verify the outcomes of the optimization efforts. This framework lets you efficiently align your cost optimization goals with verifiable carbon reduction targets.

### Carbon Footprint reporting methodology

Carbon Footprint provides a transparent, auditable, and globally-aligned report of your cloud-related emissions. The report adheres to international standards, primarily the [Greenhouse Gas (GHG) Protocol](https://ghgprotocol.org/standards) for carbon reporting and accounting. The Carbon Footprint report uses location-based and market-based accounting methods. Location-based accounting is based on the local grid's emissions factor. Market-based accounting considers Google's purchases of carbon-free energy (CFE). This dual approach helps you understand both the physical-grid impact and the carbon benefit of your workloads in Google Cloud.

For more information about how the Carbon Footprint report is prepared, including the data sources used, Scope-3 inclusions, and the customer allocation model, see [Carbon Footprint reporting methodology](https://docs.cloud.google.com/carbon-footprint/docs/methodology).

## Recommendations

To use carbon measurement for continuous improvement, consider the recommendations in the following sections. The recommendations are structured as phases of maturity for implementing sustainable-by-design cloud operations:

  * Phase 1: Establish a baseline
  * Phase 2: Identify hotspots
  * Phase 3: Implement targeted optimization
  * Phase 4: Institutionalize sustainability practices and reporting



### Phase 1: Establish a baseline

In this phase, you set up the necessary tools and ensure that data is accessible and correctly integrated.

  1. **Grant permissions** : Grant permissions to teams like FinOps, SecOps and platform engineering so that they can access the Carbon Footprint dashboard in the Google Cloud console. Grant the [Carbon Footprint Viewer role](https://docs.cloud.google.com/carbon-footprint/docs/iam#standard-roles) (`roles/billing.carbonViewer`) in Identity and Access Management (IAM) for the appropriate billing account.
  2. **Automate data export** : Before you export data, ensure that your Google Cloud [resource hierarchy (folders and projects)](https://docs.cloud.google.com/architecture/blueprints/security-foundations/organization-structure) and your [resource annotations (tags and labels)](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels) accurately reflect the organization of your business units. Because Carbon Footprint data is aggregated at the project level, a well-defined hierarchy is essential for correctly attributing emissions. Configure automated [export of Carbon Footprint data](https://docs.cloud.google.com/carbon-footprint/docs/export) to BigQuery. The exported data lets you perform deep analysis, correlate carbon data with cost and usage data, and produce custom reports.
  3. **Define carbon-related key performance indicators (KPIs)** : Establish metrics that connect carbon emissions to business value. For example, carbon intensity is a metric for the number of kilograms of [CO2 equivalent](https://en.wikipedia.org/wiki/Global_warming_potential) per customer, transaction, or revenue unit.



### Phase 2: Identify carbon hotspots

Identify the areas that have the largest environmental impact by analyzing the granular data in the Carbon Footprint report. Use the following techniques for this analysis:

  * **Prioritize by scope** : To quickly identify the largest gross carbon emitters, analyze the data in the dashboard by project, region, and service.
  * **Use dual-accounting** : When you evaluate the carbon impact in a region, consider both location-based emissions (the environmental impact of the local electrical grid) and market-based emissions (the benefit of Google's CFE investments).
  * **Correlate with cost** : Join the carbon data in BigQuery with your billing data and assess the impact of optimization actions on sustainability _and_ cost. Although cost and carbon often trend together, you can only use cost as an initial indicator. For example, in high-cost regions that have high [Carbon-Free Energy (CFE) scores](https://cloud.withgoogle.com/region-picker/), workloads might have high cost but low market-based emissions. Always validate optimization assumptions against real location-based metrics and market-based metrics.
  * **Annotate data to measure return on effort (ROE)** : Annotate the carbon data in BigQuery with specific events, like right-sizing a resource or decommissioning a large service. The annotations let you attribute reductions in carbon emission and cost to specific optimization initiatives, so that you can measure and demonstrate the outcome of each initiative.



### Phase 3: Implement targeted optimization

This is the execution phase for implementing sustainable-by-design cloud operations. Use the following strategies to optimize specific resources that you identify as significant drivers of cost and carbon emissions:

  * **Decommission unattended projects** : As part of your IT service management (ITSM) workflows, regularly check the [unattended project recommender](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender) that's integrated with the Carbon Footprint data. To achieve immediate, verified reductions in carbon emissions and cost, automate the review and eventual removal of unused projects through tracked engineering tickets.
  * **Right-size resources** : Match the provisioned resource capacity to actual utilization by using Active Assist right-sizing [recommenders](https://docs.cloud.google.com/recommender/docs/recommenders) like [machine type recommendations for Compute Engine VMs](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances). For compute-intensive tasks and AI workloads, use the most efficient machine types and AI models.
  * **Adopt carbon-aware scheduling** : For batch workloads that aren't time-critical, integrate regional CFE data into the scheduling logic. Where feasible, limit the creation of new resources to low-carbon regions by using the [resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) constraint in Organization Policy Service.
  * **Reduce data sprawl** : Implement data governance policies to ensure that infrequently accessed data is transitioned to an appropriate cold storage class (Nearline, Coldline, or Archive) or is permanently deleted. This strategy helps to reduce the energy cost of your storage resources.
  * **Refine application code** : Fix code-level inefficiencies that cause excessive resource usage or unnecessary computation.



For more information, see the following:

  * [Use regions that consume low-carbon energy](https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions)
  * [Optimize AI and ML workloads](https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency)
  * [Optimize resource usage](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-resource-usage)
  * [Develop energy-efficient software](https://docs.cloud.google.com/architecture/framework/sustainability/energy-efficient-software)
  * [Optimize data and storage for sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-storage)



### Phase 4: Institutionalize your sustainability practices and reporting

In this phase, you embed carbon measurement into your governance framework. This approach helps to ensure that your organization has the capabilities and controls that are necessary for continuous sustainability improvements and verifiable reporting.

  * **Implement _GreenOps_ governance**: Establish a formal [GreenOps](https://en.wikipedia.org/wiki/Green_computing#Cloud_computing) function or working group to integrate Carbon Footprint data with Cloud Billing data. Integrate your [monthly BigQuery carbon exports](https://docs.cloud.google.com/carbon-footprint/docs/export) directly into your existing FinOps dashboards, such as Looker. Presenting carbon and cost data in a single interface helps to ensure that sustainability is part of your standard operational review cycle. This function must define accountability for carbon reduction targets across projects, align cost optimization with sustainability goals, and implement reporting to track carbon efficiency against spending.
  * **Use Carbon Footprint data for reporting and compliance** : Use the verified, auditable Carbon Footprint data in BigQuery to create formal environmental, social, and governance (ESG) disclosures. This approach lets you meet stakeholder demands for transparency and helps to ensure compliance with mandatory and voluntary regulations.
  * **Invest in training and awareness** : Implement mandatory sustainability training for relevant technical and non-technical teams. Your teams need to know how to access and interpret the Carbon Footprint data and how to apply optimization recommendations in their daily workflows and design choices. For more information, see [Provide role-based sustainability training](https://docs.cloud.google.com/architecture/framework/sustainability/culture#provide_role-based_sustainability_training).
  * **Define carbon requirements** : Incorporate carbon emission metrics as non-functional requirements (NFR) in your application's acceptance criteria for new deployments. This practice helps to ensure that architects and developers prioritize low-carbon design options from the start of the application development lifecycle.
  * **Automate GreenOps** : Automate the implementation of Active Assist recommendations by using scripts, templates, and infrastructure-as-code (IaC) pipelines. This practice ensures that teams apply recommendations consistently and rapidly across the organization.



[ Previous arrow_back  Optimize data and storage  ](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-storage)

[ Next Promote a culture of sustainability  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/sustainability/culture)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-28 UTC."],[],[]] 
