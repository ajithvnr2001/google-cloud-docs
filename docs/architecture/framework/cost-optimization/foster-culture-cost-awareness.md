---
url: https://docs.cloud.google.com/architecture/framework/cost-optimization/foster-culture-cost-awareness/
title: Foster a culture of cost awareness \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:20.835785+00:00
---

# Foster a culture of cost awareness  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/cost-optimization/foster-culture-cost-awareness/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Foster a culture of cost awareness Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-09-25 UTC

This principle in the cost optimization pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to promote cost awareness across your organization and ensure that team members have the cost information that they need to make informed decisions.

Conventionally, the responsibility for cost management might be centralized to a few select stakeholders and primarily focused on initial project architecture decisions. However, team members across all cloud user roles (analyst, architect, developer, or administrator) can help to reduce the cost of your resources in Google Cloud. By sharing cost data appropriately, you can empower team members to make cost-effective decisions throughout their development and deployment processes.

## Principle overview

Stakeholders across various roles – product owners, developers, deployment engineers, administrators, and financial analysts – need visibility into relevant cost data and its relationship to business value. When provisioning and managing cloud resources, they need the following data:

  * **Projected resource costs** : Cost estimates at the time of design and deployment.
  * **Real-time resource usage costs** : Up-to-date cost data that can be used for ongoing monitoring and budget validation.
  * **Costs mapped to business metrics** : Insights into how cloud spending affects key performance indicators (KPIs), to enable teams to identify cost-effective strategies.



Every individual might not need access to raw cost data. However, promoting cost awareness across all roles is crucial because individual decisions can affect costs.

By promoting cost visibility and ensuring clear ownership of cost management practices, you ensure that everyone is aware of the financial implications of their choices and everyone actively contributes to the organization's cost optimization goals. Whether through a centralized FinOps team or a distributed model, establishing accountability is crucial for effective cost optimization efforts.

## Recommendations

To promote cost awareness and ensure that your team members have the cost information that they need to make informed decisions, consider the following recommendations.

### Provide organization-wide cost visibility

To achieve organization-wide cost visibility, the teams that are responsible for cost management can take the following actions:

  * **Standardize cost calculation and budgeting** : Use a consistent method to determine the full costs of cloud resources, after factoring in discounts and shared costs. Establish clear and standardized budgeting processes that align with your organization's goals and enable proactive cost management.
  * **Use standardized cost management and visibility tools** : Use appropriate tools that provide real-time insights into cloud spending and generate regular (for example, weekly) cost progression snapshots. These tools enable proactive budgeting, forecasting, and identification of optimization opportunities. The tools could be cloud provider tools (like the [Google Cloud Billing dashboard](https://docs.cloud.google.com/billing/docs/how-to/reports)), third-party solutions, or open-source solutions like the [Cost Attribution solution](https://github.com/google/cost-attribution-solution).
  * **Implement a cost allocation system** : Allocate a portion of the overall cloud budget to each team or project. Such an allocation gives the teams a sense of ownership over cloud spending and encourages them to make cost-effective decisions within their allocated budget.
  * **Promote transparency** : Encourage teams to discuss cost implications during the design and decision-making processes. Create a safe and supportive environment for sharing ideas and concerns related to cost optimization. Some organizations use positive reinforcement mechanisms like leaderboards or recognition programs. If your organization has restrictions on sharing raw cost data due to business concerns, explore alternative approaches for sharing cost information and insights. For example, consider sharing aggregated metrics (like the total cost for an environment or feature) or relative metrics (like the average cost per transaction or user).



### Understand how cloud resources are billed

Pricing for Google Cloud resources might vary across [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). Some resources are billed monthly at a fixed price, and others might be billed based on usage. To understand how Google Cloud resources are billed, use the [Google Cloud pricing calculator](https://cloud.google.com/products/calculator) and product-specific pricing information (for example, [Google Kubernetes Engine (GKE) pricing](https://cloud.google.com/kubernetes-engine/pricing)).

### Understand resource-based cost optimization options

For each type of cloud resource that you plan to use, explore strategies to optimize utilization and efficiency. The strategies include rightsizing, autoscaling, and adopting serverless technologies where appropriate. The following are examples of cost optimization options for a few Google Cloud products:

  * Cloud Run lets you configure [always-allocated CPUs](https://docs.cloud.google.com/run/docs/configuring/cpu-allocation) to handle predictable traffic loads at a fraction of the price of the default allocation method (that is, CPUs allocated only during request processing).
  * You can purchase [BigQuery slot commitments](https://docs.cloud.google.com/bigquery/docs/reservations-commitments) to save money on data analysis.
  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics) provides detailed metrics to help you understand cost optimization options.
  * Understand how [network pricing](https://cloud.google.com/vpc/network-pricing) can affect the cost of data transfers and how you can optimize costs for specific networking services. For example, you can reduce the data transfer costs for external Application Load Balancers by using Cloud CDN or Google Cloud Armor. For more information, see [Ways to lower external Application Load Balancer costs](https://docs.cloud.google.com/vpc/network-pricing#ways-to-lower-external-application-load-balancer-costs).



### Understand discount-based cost optimization options

Familiarize yourself with the discount programs that Google Cloud offers, such as the following examples:

  * [**Committed use discounts (CUDs)**](https://docs.cloud.google.com/docs/cuds): CUDs are suitable for resources that have predictable and steady usage. CUDs let you get significant reductions in price in exchange for committing to specific resource usage over a period (typically one to three years). You can also use [CUD auto-renewal](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically) to avoid having to manually repurchase commitments when they expire.
  * [**Sustained use discounts**](https://docs.cloud.google.com/compute/docs/sustained-use-discounts): For certain Google Cloud products like Compute Engine and GKE, you can get automatic discount credits after continuous resource usage beyond specific duration thresholds.
  * [**Spot VMs**](https://cloud.google.com/solutions/spot-vms): For fault-tolerant and flexible workloads, Spot VMs can help to reduce your Compute Engine costs. The cost of Spot VMs is significantly lower than regular VMs. However, Compute Engine might preemptively stop or delete Spot VMs to reclaim capacity. Spot VMs are suitable for batch jobs that can tolerate preemption and don't have high availability requirements.
  * **Discounts for specific product options** : Some managed services like BigQuery offer [discounts](https://docs.cloud.google.com/bigquery/docs/reservations-intro) when you purchase dedicated or autoscaling query processing capacity.



Evaluate and choose the discounts options that align with your workload characteristics and usage patterns.

### Incorporate cost estimates into architecture blueprints

Encourage teams to develop architecture blueprints that include cost estimates for different deployment options and configurations. This practice empowers teams to compare costs proactively and make informed decisions that align with both technical and financial objectives.

### Use a consistent and standard set of labels for all your resources

You can use [labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels) to track costs and to identify and classify resources. Specifically, you can use labels to allocate costs to different projects, departments, or cost centers. Defining a [formal labeling policy](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels#example_labels_table) that aligns with the needs of the main stakeholders in your organization helps to make costs visible more widely. You can also use labels to filter resource cost and usage data based on target audience.

Use automation tools like Terraform to enforce labeling on every resource that is created. To enhance cost visibility and attribution further, you can use the tools provided by the open-source [cost attribution solution](https://github.com/google/cost-attribution-solution).

### Share cost reports with team members

By sharing cost reports with your team members, you empower them to take ownership of their cloud spending. This practice enables cost-effective decision making, continuous cost optimization, and systematic improvements to your cost allocation model.

Cost reports can be of several types, including the following:

  * **Periodic cost reports** : Regular reports inform teams about their current cloud spending. Conventionally, these reports might be spreadsheet exports. More effective methods include automated emails and specialized dashboards. To ensure that cost reports provide relevant and actionable information without overwhelming recipients with unnecessary detail, the reports must be tailored to the target audiences. Setting up tailored reports is a foundational step toward more real-time and interactive cost visibility and management.
  * **Automated notifications** : You can configure cost reports to proactively notify relevant stakeholders (for example, through email or chat) about cost anomalies, budget thresholds, or opportunities for cost optimization. By providing timely information directly to those who can act on it, automated alerts encourage prompt action and foster a proactive approach to cost optimization.
  * **Google Cloud dashboards** : You can use the [built-in billing dashboards](https://docs.cloud.google.com/billing/docs/how-to/reports) in Google Cloud to get insights into cost breakdowns and to identify opportunities for cost optimization. Google Cloud also provides [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub) to help you monitor savings and get recommendations for cost optimization. An AI engine powers the FinOps hub to recommend cost optimization opportunities for all the resources that are currently deployed. To control access to these recommendations, you can implement role-based access control (RBAC).
  * **Custom dashboards** : You can create custom dashboards by exporting cost data to an analytics database, like [BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). Use a visualization tool like [Data Studio](https://cloud.google.com/data-studio) to connect to the analytics database to build interactive reports and enable fine-grained access control through role-based permissions.
  * **Multicloud cost reports** : For multicloud deployments, you need a unified view of costs across all the cloud providers to ensure comprehensive analysis, budgeting, and optimization. Use tools like BigQuery to centralize and analyze cost data from multiple cloud providers, and use Data Studio to build team-specific interactive reports.



[ Previous arrow_back  Align spending with business value  ](https://docs.cloud.google.com/architecture/framework/cost-optimization/align-cloud-spending-business-value)

[ Next Optimize resource usage  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/cost-optimization/optimize-resource-usage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-09-25 UTC."],[],[]] 
