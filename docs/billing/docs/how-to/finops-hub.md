---
url: https://docs.cloud.google.com/billing/docs/how-to/finops-hub/
title: Optimize costs with FinOps hub \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:30:46.483447+00:00
---

# Optimize costs with FinOps hub  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/finops-hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Optimize costs with FinOps hub Stay organized with collections  Save and categorize content based on your preferences. 

With the FinOps hub, you can monitor and communicate your current savings, explore new recommended opportunities to optimize costs, and plan your optimization goals. The FinOps hub presents all of your active savings and optimization opportunities in one dashboard. The FinOps hub automatically generates the dashboard based on historical usage metrics gathered by Cloud Billing and [Recommender](https://docs.cloud.google.com/recommender/docs/overview), including recent usage and current commitments.

## Permissions required to access the FinOps hub

The FinOps hub uses Cloud Billing to retrieve cost data, and various Google Cloud cost recommenders for optimization and utilization metrics.

To access the FinOps hub for a Cloud Billing account, you need Cloud Billing permissions.

Depending on your level of Cloud Billing access, you can view the FinOps hub for a _Cloud Billing account_ (to view _all_ available recommendations, the FinOps score, CUDs optimization metrics, and utilization insights), or you can view the FinOps hub and recommendations limited to the Google Cloud projects for which you have cost view access.

Depending on the _type of recommendation_ , you might also need project permissions to view the details and apply a recommendation.

### Full billing account permissions

#### Access the FinOps hub

To access the FinOps hub for a Cloud Billing account, and view all available recommendations, the FinOps score, CUDs optimization metrics, and utilization insights, you need one of the following predefined [ Cloud Billing IAM roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on your Cloud Billing account:

  * Billing Account Viewer
  * Billing Account Administrator



If you prefer to use a custom role to access the FinOps hub, you need a role with the following [permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * `billing.accounts.get`
  * `billing.accounts.getSpendingInformation`
  * `billing.finOpsBenchmarkInformation.get`
  * `billing.finOpsHealthInformation.get`
  * `recommender.costRecommendations.listAll`



#### View details of a recommendation and apply the recommendation

To view the details and apply a recommendation, you need [ recommender-specific permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender) on the billing account or project. Depending on the  type of recommendation, you might need the following permissions:

  * [ Project Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role for each of the projects that you want to see recommendations for.
  * [ Recommender Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.viewer) on your Cloud Billing account.
  * See the  list of FinOps hub cost recommenders for the recommenders that contribute to hub metrics.
  * To learn how to grant permissions to view recommendation updates, see [ Recommender overview](https://docs.cloud.google.com/recommender/docs/whatis-activeassist#grant_permissions_to_view_and_update_recommendations_and_insights).



### Project-scoped billing permissions

If you have multi-project cost view access to a Cloud Billing account, you can access the FinOps hub and view all available FinOps recommendations for the projects where you have been granted cost view permissions, including the FinOps utilization insights and wasted usage dashboard.

#### Access the FinOps hub

To access the FinOps hub for all of your authorized projects, you need cost view permissions on _each Google Cloud project_ , and you need permissions on the _Cloud Billing account_ that is linked to your authorized projects.

**Project permissions**

_Project permissions_ are granted using roles on the Google Cloud project. To access Cloud Billing to view costs for a project, you need a role on each _Google Cloud project_ that includes the following [ permissions](https://docs.cloud.google.com/resource-manager/docs/access-control-proj):

  * `billing.resourceCosts.get`
  * `resourcemanager.projects.get`



To gain these permissions using a [ predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles), ask your administrator to grant you one of the following [ basic IAM roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on your Google Cloud projects:

  * Project Viewer
  * Project Editor
  * Project Owner



**Billing account permissions** ([Preview](https://cloud.google.com/products/#product-launch-stages)) 

_Cloud Billing account permissions_ are granted using roles on the billing account. To access a billing account to view the FinOps recommendations for _all_ of your authorized Google Cloud projects that are linked to the billing account, ask your [ Cloud Billing administrator](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator) to grant you the following [ predefined Cloud Billing IAM role](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on the Cloud Billing account that is linked to your authorized projects:

  * [ **Project Billing Costs Manager**](https://docs.cloud.google.com/billing/docs/how-to/billing-access#ba-project-costs)



Learn more about the [ permissions required for _multi-project-scoped access_ to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access#required-permissions).

#### View details of a recommendation and apply the recommendation

To view the details and apply a recommendation, you need [ recommender-specific permissions](https://docs.cloud.google.com/iam/docs/understanding-roles#recommender-roles) on the billing account or project. Depending on the  type of recommendation, you might need the following permissions:

  * [ Project Viewer](https://docs.cloud.google.com/iam/docs/understanding-roles#basic) role for each of the projects that you want to see recommendations for.
  * [ Recommender Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#recommender.viewer) on your Cloud Billing account.
  * See the  list of FinOps hub cost recommenders for the recommenders that contribute to hub metrics.
  * To learn how to grant permissions to view recommendation updates, see [ Recommender overview](https://docs.cloud.google.com/recommender/docs/whatis-activeassist#grant_permissions_to_view_and_update_recommendations_and_insights).

**Note** : If you are viewing the FinOps hub using _project-level permissions_ only, some of the _billing-account-level_ FinOps hub features aren't available, such as CUD recommendations and FinOps score.

For more information about _Cloud Billing permissions_ , see:

  * [ Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [ Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles)
  * [ Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)

|  For more information about Google Cloud _project permissions_ , see:

  * [ Access control for projects with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-proj)
  * [ IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-overview#basic)

  
---|---  
  
## Explore the FinOps hub

To view the FinOps hub, follow the process that matches your level of access to Cloud Billing accounts:

### Full billing account permissions

If you have full Cloud Billing account permissions, you can select from a list of billing accounts that you have permissions to access.

  1. In the Google Cloud console, go to the FinOps hub.

[ Go to the FinOps hub](https://console.cloud.google.com/billing/optimize)
  2. At the prompt, choose the Cloud Billing account for which you want to view the FinOps hub.

The Billing **FinOps hub** page opens for the selected billing account.

With full billing account permissions, you can access all of The FinOps hub features.




### Multi-project cost view permissions

If you have multi-project access to Cloud Billing accounts, you can select from a list of billing accounts that you have permissions to access.

  1. In the Google Cloud console, go to the FinOps hub.

[ Go to the FinOps hub](https://console.cloud.google.com/billing/optimize)
  2. At the prompt, choose the Cloud Billing account for which you want to view the FinOps hub.

The Billing **FinOps hub** page opens for the selected billing account.


![Example of the finops hub page, scoped by the number of projects available for users with multi-project access to the billing account.](https://docs.cloud.google.com/static/billing/docs/images/finops-hub-multi-projects.png)Click image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/finops-hub-multi-projects.png)

When you access the FinOps hub using multi-project permissions, the FinOps hub is scoped to all of your authorized projects that are linked to the Cloud Billing account that you are viewing. Click the **Scope** to open the **Account management** page to view the list of projects that are in scope.

With multi-project billing account permissions, certain FinOps hub features aren't available, such as the [FinOps score](https://docs.cloud.google.com/billing/docs/how-to/finops-hub#finops_score) and the [ Carbon footprint dashboard](https://docs.cloud.google.com/billing/docs/how-to/finops-hub#carbon-footprint-dashboard).

## The FinOps hub dashboard

The **FinOps hub** dashboard summarizes your current cost optimizations and introduces Google Cloud-recommended optimizations. Information on the FinOps hub reflects historical data collected.

![Example of the FinOps hub dashboard with each widget visible.](https://docs.cloud.google.com/static/billing/docs/images/finops-hub-dashboard.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-hub-dashboard.png)

### How potential savings are determined

The FinOps hub considers four optimization practices to create cost-saving recommendations:

  * Turning off idle resources
  * Right-sizing instances
  * Other configuration changes for certain resources
  * Purchasing committed use discounts (CUDs)



Metrics throughout the hub reflect how well you're using those optimizations and identify additional optimization opportunities to reduce costs and improve FinOps practices.

  * In a recommendation, the estimated savings for a resource is calculated using either a custom contract price or a list price. The pricing type used to [calculate the estimated cost savings](https://docs.cloud.google.com/recommender/docs/understand-cost-recs) is based on the contract type you might have with Google Cloud and your specific role and cost view permissions on the Cloud Billing account.
  * The estimated savings in a recommendation doesn't consider existing committed use discounts that you have purchased that might apply to the resource.



### Optimization summary

![Example of the Optimization summary.](https://docs.cloud.google.com/static/billing/docs/images/finops-optimization-summary.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-optimization-summary.png)

The **Optimization summary** is a snapshot of how much you're saving with optimizations, current recommendations from Google Cloud, and how much more you could save by adopting additional optimizations. The **Optimization summary** includes:

  * **Last month's realized savings** : The total savings related to CUDs, right-sizing instances, and deleting unattended projects.

**Note:** Realized savings don't include savings from turning off idle resources, such as VMs, disks, or IP addresses. Additionally, you might see a negative total if you've underutilized CUDs.
  * **Active recommendations** : The total number of Google Cloud-recommended optimizations available to you. Recommendations include suggestions to turn off idle resources, right-size instances or other configuration changes, and purchase CUDs.

  * **Potential savings per month** : The estimated amount of money you can save by applying all available recommendations. If there are multiple potential opportunities to save on the same Compute Engine resource, such as purchasing a resource-based CUD and a Compute flexible CUD, the FinOps hub de-duplicates the opportunities and only includes the recommendation that brings you the higher savings.

  * **CUD optimization rate** : The percentage of how much of your CUD-eligible usage is covered by committed use discounts. We determine your CUD optimization rate by calculating how much of your usage across all products over the last 30 days can be converted to CUDs. For example, in the past 30 days, you might have spent $10,000 on Google Cloud products eligible for CUDs, and received $4,500 worth of CUDs. In this example, you are using $4,500 out of $10,000 in CUDs opportunities, so your _CUD optimization rate_ is 45%.

  * **Insights provided by Gemini Cloud Assist** : The Gemini-generated key optimization and utilization insights shown in the _Optimization summary_ widget:

![Example of the Finops hub insights provided by Gemini Cloud Assist.](https://docs.cloud.google.com/static/billing/docs/images/finops-hub-gemini-insights.png)




### FinOps score

**Note:** The FinOps score and the peer benchmark score are only available when viewing the FinOps hub with [full billing account permissions](https://docs.cloud.google.com/billing/docs/how-to/finops-hub#required-permissions).

![Example of the Finops score widget.](https://docs.cloud.google.com/static/billing/docs/images/finops-score.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-score.png)

The **FinOps score** can help you gauge how well you're using Google Cloud tools to monitor and save costs, and how you can continue to optimize costs. The score is a calculation based on how you follow optimization best practices, including the following:

  * Monitoring spend by actively logging in and using Cloud Billing tools.
  * Using tools such as tags and labels to allocate costs for your resources.
  * Optimizing resources by turning off idle resources and right-sizing instances.
  * Purchasing CUDs, including CUDs opportunities recommended by Google Cloud.
  * Creating and monitoring budgets frequently.
  * Automating your cost management by using tools such as the billing BigQuery export and using the Budgets API.



Select **Improve your score** to review Google Cloud recommended cost-saving actions based on three stages of the cloud FinOps journey: inform, operate, and optimize.

![Example of the FinOps score details page.](https://docs.cloud.google.com/static/billing/docs/images/finops-score-details.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-score-details.png)

The FinOps score also provides a peer benchmark score as a view of your optimization performance in the context of industry verticals based on aggregated usage data. All customers are automatically opted into peer benchmarking aggregation, but you can choose to opt out at any time. If you choose to opt out, you no longer see CUD recommendations, the FinOps score, or the peer benchmark score in the FinOps hub.

The FinOps and peer benchmark scores are based on data collected two days prior, and are updated daily. Your score might change depending on factors such as new customers joining the peer benchmark score.

#### Opt in or out of participating in the peer benchmark score

To opt in or out of participating in peer benchmarking, you must have the Billing Account Administrator role on your Cloud Billing account, and the `dataprocessing.groupcontrols.update` permission on your Cloud Billing account, which is part of the Data Processing Controls Resource Admin role.

  1. In the Google Cloud console, open the Identity and Access Management (IAM) Transparency and Control Center for your Cloud Billing account.

[Go to Transparency and Control Center](https://console.cloud.google.com/iam-admin/privacy/transparency-and-control/billing-account)

  2. Select your Cloud Billing account from the menu.

  3. To opt out of participating in peer benchmarking, in the **Data processing groups** table, for the **Billing** group, click **Disable**.

If you want to opt in, select **Enable**.


**Note:** When you disable permissions, you're opted out from peer benchmark participation, but you might still see the peer benchmark metric for several days. If you re-enable participation, it might take two to four days to view the peer benchmark metric again.

### Potential savings/month

![Example of the Potential savings per month widget.](https://docs.cloud.google.com/static/billing/docs/images/finops-potential-savings-per-month.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-potential-savings-per-month.png)

With the **Potential savings/month** chart, you can focus on savings by **service** or by **project**. The chart shows the total potential monthly savings from all cost optimization opportunities broken down by the associated service or project.

#### Recommendations dashboard

From the _Potential savings/month_ chart, you can access the **Recommendations** dashboard, where you can review all of the FinOps recommendations, view the recommendation details, send recommendations to others to review, and apply recommendations to optimize your cloud costs.

To open the [**Recommendations** dashboard](https://docs.cloud.google.com/billing/docs/how-to/finops-recommendations-dashboard), select **View all recommendations**.

### Top recommendations

![Example of the Top recommendations widget.](https://docs.cloud.google.com/static/billing/docs/images/finops-top-recs.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-top-recs.png)

The **Top recommendations** widget shows you the top 10 recommendations by potential cost savings. Each recommendation displays the estimated monthly savings, the associated services with the savings, and a brief description of the recommendation.

If you have the [Recommender Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.viewer) on your Cloud Billing account, you can select a recommendation to get further details and to apply the recommendation. Depending on the type of recommendation, you might also need project permissions to view the details and apply a recommendation.

### Potential wasted usage

![Example of the Potential wasted usage widget in the FinOps hub.](https://docs.cloud.google.com/static/billing/docs/images/finops-potential-wasted-usage.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-potential-wasted-usage.png)

[(Preview)](https://cloud.google.com/products/#product-launch-stages) Gain insights on resource utilization and the cost of potential waste. For resources that provide utilization metrics (such as Compute Engine, Google Kubernetes Engine, Cloud SQL, and Cloud Run), the chart shows the costs of provisioned resources with potentially wasted usage.

To determine waste, utilization insights uses various recommenders to help you identify idle resources, right-sizing opportunities of over- or underprovisioned resources, and suboptimal configurations, and then summarizes the cost of the potential wasted usage for each service that returns utilization metrics.

To view the details of the insights and access cost optimization recommendations, click **View utilization insights** to open the [**Utilization insights** dashboard](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights).

### Last month's realized savings

![Example of the Last month's realized savings widget.](https://docs.cloud.google.com/static/billing/docs/images/finops-realized-savings.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-realized-savings.png)

For a high-level view of your savings from commitments, use the **Last month's realized savings** widget, which breaks down your savings by the services that you have purchased commitments for.

### Carbon Footprint dashboard

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" of the Google Cloud [Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).**Note:** The Carbon footprint dashboard is only available when viewing the FinOps hub with [full billing account permissions](https://docs.cloud.google.com/billing/docs/how-to/finops-hub#required-permissions).

![Example of the Carbon footprint widget.](https://docs.cloud.google.com/static/billing/docs/images/finops-carbon-footprint.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-carbon-footprint.png)

The **Carbon Footprint dashboard** presents the estimated greenhouse gas emissions from your Google Cloud usage, helping you optimize cloud spend while reducing carbon impact. For more information, visit the [Carbon Footprint documentation](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data).

When you view the **Recommendations** dashboard, in the list of recommendations, the **Region** column displays a green leaf next to locations that have the lowest carbon impact. For more information, see ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker).

## Apply recommendations

Continue to optimize costs by taking advantage of Google's cost-saving recommendations. To access and apply recommendations, take any of the following actions:

  * On the **FinOps score** widget, click **Improve your score** to access and apply recommended actions.
  * On the **Potential savings/month** widget, click **View all recommendations** to access the [**Recommendations** dashboard](https://docs.cloud.google.com/billing/docs/how-to/finops-recommendations-dashboard), then click any of the recommendations to view the details of the recommendation and take action.
  * On the **Potential wasted usage** widget, click **View utilization insights** to access the [**Utilization insights** dashboard](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights).
  * On the **Top recommendations** widget, click any of the recommendations to view the details of the recommendation and take action.



## FinOps hub cost recommenders

The **FinOps hub** dashboard receives metrics from various Google Cloud cost recommenders. Use the following table to learn more about each recommender.

**Name** | **Recommender ID** | **Short Description**  
---|---|---  
**Committed Use Discounts (CUDs) recommenders**  
[Committed use discount recommender](https://docs.cloud.google.com/recommender/docs/committed-use-discount-recommender) |  `google.compute.commitment.UsageCommitmentRecommender` | Reduce costs through purchasing resource-based commitments  
[Committed use discount recommender](https://docs.cloud.google.com/recommender/docs/committed-use-discount-recommender) |  `google.cloudbilling.commitment.SpendBasedCommitmentRecommender` | Reduce costs through purchasing spend-based and Compute flexible commitments  
**Compute Engine recommenders**  
[Idle custom image recommender](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations) | `google.compute.image.IdleResourceRecommender` | Remove unused images  
[Idle IP address recommender](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations) | `google.compute.address.IdleResourceRecommender` | Remove unused IPs  
[Idle persistent disk recommender](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations) | `google.compute.disk.IdleResourceRecommender` | Backup and remove unused disks  
[Idle VM recommender](https://docs.cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview) | `google.compute.instance.IdleResourceRecommender` | Remove unused VMs  
[Idle reservations recommender](https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview) | `google.compute.IdleResourceRecommender` | Remove unused reservations  
[Managed instance group machine type recommender](https://docs.cloud.google.com/compute/docs/instance-groups/apply-machine-type-recommendations-managed-instance-groups) |  `google.compute.instanceGroupManager.MachineTypeRecommender` | Right-size MIG machine types  
[Underutilized reservations recommender](https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview) | `google.compute.RightSizeResourceRecommender` | Right-size underutilized reservations  
[VM machine type recommender](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances) | `google.compute.instance.MachineTypeRecommender` **Note:** Recommendations of this type indicating an _underutilized VM_ (those with a negative costs savings or cost increase) are shown on the [ Utilization insights](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights) dashboard but not on the FinOps [Recommendations](https://docs.cloud.google.com/billing/docs/how-to/finops-recommendations-dashboard) dashboard. | Right-size VM machine types  
**Google Kubernetes Engine (GKE) recommenders**  
[GKE idle cluster recommender](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/idle-clusters) | `google.container.DiagnosisRecommender`  
subtype: CLUSTER_IDLE | Remove unused GKE clusters  
[GKE overprovisioned cluster recommender](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-cluster-utilization) | `google.container.DiagnosisRecommender`  
subtype: CLUSTER_OVERPROVISIONED | Right-size overprovisioned GKE clusters  
[GKE underprovisioned cluster recommender](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-cluster-utilization) | `google.container.DiagnosisRecommender`  
subtype: CLUSTER_UNDERPROVISIONED **Note:** Underprovisionsed cluster recommendations are shown on the [ Utilization insights](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights) dashboard but aren't included on the FinOps [Recommendations](https://docs.cloud.google.com/billing/docs/how-to/finops-recommendations-dashboard) dashboard. | Optimize underprovisioned GKE clusters  
[GKE overprovisioned workload recommender](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization) | `google.container.DiagnosisRecommender`  
subtype: WORKLOAD_OVERPROVISIONED | Right-size overprovisioned GKE workloads  
[GKE underprovisioned workload recommender](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization) | `google.container.DiagnosisRecommender`  
subtype: WORKLOAD_UNDERPROVISIONED | Optimize underprovisioned GKE workloads  
**Cloud SQL recommenders**  
[Cloud SQL idle instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle) | `google.cloudsql.instance.IdleRecommender` | Remove unused SQL instances  
[Cloud SQL overprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned) | `google.cloudsql.instance.OverprovisionedRecommender` | Right-size overprovisioned SQL instances  
[Cloud SQL underprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-underprovisioned) | `google.cloudsql.instance.UnderprovisionedRecommender` **Note:** Underprovisionsed instance recommendations are shown on the [ Utilization insights](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights) dashboard but aren't included on the FinOps [Recommendations](https://docs.cloud.google.com/billing/docs/how-to/finops-recommendations-dashboard) dashboard. | Optimize underprovisioned SQL instances  
**Cloud Run recommenders**  
[Cloud Run CPU allocation recommender](https://docs.cloud.google.com/run/docs/recommender) | `google.run.service.CostRecommender` | Switch to CPU always-allocated  
**Project recommender - all services**  
[Unattended project recommender](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender) | `google.resourcemanager.projectUtilization.Recommender` | Reclaim or remove unused projects  
  
## Resources

  * [Google Cloud Well-Architected Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization)
  * [Optimize costs with committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [Purchasing spend-based committed use discounts](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing)
  * [Purchasing resource-based committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
