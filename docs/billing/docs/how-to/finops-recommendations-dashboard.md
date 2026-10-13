---
url: https://docs.cloud.google.com/billing/docs/how-to/finops-recommendations-dashboard/
title: Review and apply FinOps hub Recommendations \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:17.810782+00:00
---

# Review and apply FinOps hub Recommendations  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/finops-recommendations-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Review and apply FinOps hub Recommendations Stay organized with collections  Save and categorize content based on your preferences. 

With the FinOps hub Recommendations dashboard, you can access the **Recommendations** list, then click any of the recommendations to view the details of the recommendation and take action.

## Permissions required to access the FinOps hub Recommendations

To access the FinOps hub and view available recommendations, the FinOps score and CUDs optimization metrics, you need either the _Billing Account Administrator_ or the _Billing Account Viewer_ role for your Cloud Billing account.

To view the recommendation detail panels, you need the _Project Viewer_ role for each of the projects that you want to see recommendations for, and recommender-specific permissions. See the [list of FinOps hub cost recommenders](https://docs.cloud.google.com/billing/docs/how-to/finops-hub#recommender-table) for the recommenders that contribute to hub metrics. To learn how to grant permissions to view recommendation updates, see [Recommender overview](https://docs.cloud.google.com/recommender/docs/overview#granting_permissions_to_view_and_update_recommendations_and_insights).

To access the FinOps hub and Recommendations dashboard using a custom role, you need the following [permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * `billing.accounts.get`
  * `billing.accounts.getSpendingInformation`
  * `billing.finOpsBenchmarkInformation.get`
  * `billing.finOpsHealthInformation.get`
  * `recommender.costRecommendations.listAll`



## Open the Recommendations dashboard

![Example of the Potential savings per month widget in the FinOps hub.](https://docs.cloud.google.com/static/billing/docs/images/finops-potential-savings-per-month.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops-potential-savings-per-month.png)

To view the **Recommendations** dashboard:

  1. In the Google Cloud console, go to the FinOps hub.

[Go to FinOps hub](https://console.cloud.google.com/billing/optimize)

  2. At the prompt, choose the Cloud Billing account for which you want to view the FinOps hub.

  3. In the **FinOps hub** , from the **Potential savings/month** chart, click **View all recommendations**.




## Explore the Recommendations dashboard

![Example of the FinOps Recommendations list.](https://docs.cloud.google.com/static/billing/docs/images/finops_top_recommendations_list.png)![](https://docs.cloud.google.com/static/billing/docs/images/finops_top_recommendations_list.png)

In the **Recommendations** dashboard, you can review all of the FinOps recommendations, view the recommendation details, send recommendations to others to review, and apply recommendations to optimize your cloud costs.

  * When you first open the **Recommendations** dashboard, by default, the page shows all savings recommendations, for all services and projects, including _Savings not specific to a project_.
  * You can use the **Services** and **Projects** dropdowns to focus the page on a smaller set of recommendations.
  * The options available in the **Services** and **Projects** dropdowns are limited to the services and projects with _active recommendations_.
  * If you select an individual service, or opt to view only some of the projects, the values in the summary (such as _Last month's realized savings_ or _Potential savings/month_) and the recommendations in the list update based on the selections.
  * The project option of _Savings not specific to a project_ applies to costs and credits that are calculated at the billing account level, such as commitment fees.
  * CUDs savings are calculated with costs and credits applied at both the billing account level and the project level. If you limit your recommendations view to _Savings not specific to a project_ , you might see negative amounts in the savings summary. To view the most accurate CUD recommendations and _realized CUD savings_ , select all projects.
  * Use the _optimization category_ tabs to focus your list of recommendations to a specific savings category, such as switching off idle resources, right-sizing instances, or purchasing additional CUDs.
  * Use the filter_list **Filter** feature to select list properties to narrow your results.
  * If you have the [Recommender Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.viewer) on your Cloud Billing account, you can select a recommendation to get further details and to apply the recommendation. Depending on the type of recommendation, you might also need project permissions to view the details and apply a recommendation.



## Resources

  * [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub)
  * [Google Cloud Well-Architected Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization)
  * [Optimize costs with committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [Purchasing spend-based committed use discounts](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing)
  * [Purchasing resource-based committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
