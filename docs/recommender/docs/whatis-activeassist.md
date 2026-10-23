---
url: https://docs.cloud.google.com/recommender/docs/whatis-activeassist/
title: What is Active Assist \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:06.778644+00:00
---

# What is Active Assist  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/whatis-activeassist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# What is Active Assist

Active Assist refers to the portfolio of tools used in Google Cloud to generate recommendations and insights to help you optimize your Google Cloud projects. This includes recommenders that generate recommendations and insights and analysis tools.

## Recommenders and Recommendations

Recommenders generate recommendations that fall into six value categories that can help you optimize your cloud in a variety of ways.

![Recommendation Categories](https://docs.cloud.google.com/static/recommender/docs/images/valuepillars.png)

See [Recommendations](https://docs.cloud.google.com/recommender/docs/key-concepts#recommendations) and [Recommenders](https://docs.cloud.google.com/recommender/docs/overview) for a detailed explanation of these concepts.

## Grant permissions to view and update recommendations and insights

Each [recommender](https://docs.cloud.google.com/recommender/docs/recommenders) and [insight type](https://docs.cloud.google.com/recommender/docs/insights/insight-types) has specific roles and permissions to control access to its recommendations and insights. In order to enable users to review and assess these recommendations and insights, they will include some metadata about resources. Granting these permissions provides users with a partial view of the resource's metadata. This partial view of data is particularly important to consider if you are using custom roles to grant permissions.

For example, the Identity and Access Management recommender provides recommendations about permissions. Members that have the `recommender.iamPolicyRecommendations.get` and `recommender.iamPolicyRecommendations.list` permissions can also see information about your IAM policy bindings.

Ensure that you have the [necessary roles and permissions](https://docs.cloud.google.com/recommender/docs/active-assist/find-active-assist#before_you_begin) to view recommendations.

## Find recommendations and insights

Each recommender lets you view and manage its recommendations and insights using the REST API and Google Cloud CLI. Some recommenders also let you view and manage their recommendations and insights using one or more of the following options:

  * Active Assist
  * [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub), which provides cost-optimization recommendations for billing account managers.
  * The Optimization page in [Cloud Hub](https://docs.cloud.google.com/hub/docs/optimize), which provides cost-optimization recommendations for developers and platform administrators.
  * _In context_ using the service's user interface (UI) in the Google Cloud console



For details about recommenders and supported clients, see [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders).

### View recommendations in Active Assist

[View your recommendations](https://console.cloud.google.com/home/recommendations)

Certain recommendations such as the IAM Recommendation require different levels of permissions to view. For more information, see the guide for the specific Recommendation that you are looking for.

## Manage recommendations and insights

In Active Assist, you can choose to apply or dismiss the recommendations. Some recommendations can be applied automatically, while other recommendations require additional steps to complete. Any additional steps will appear in the details panel.

## Apply recommendations

**Warning:**

Before applying recommendations in the Google Cloud console or using the API, ensure that impacts are assessed by a reviewer within your organization. The reviewer should have the knowledge to assess impacts identified in recommendations, as well as impacts specific to your infrastructure and business. Applying recommendations without proper assessment could result in unexpected changes, such as issues with system performance, poor reliability, or loss of required permissions. If you choose to apply recommendations without human review, ensure that you have set up a rollback process before making any changes.

Recommender provides information on direct [impacts](https://docs.cloud.google.com/recommender/docs/key-concepts#impact) in areas such as cost, performance, or security. Recommendation reviewers should have a holistic understanding of your infrastructure and processes so that other business-specific impacts are considered.

## Get started with recommendations

Recommendations are an easy way to optimize your cloud to help you maintain a secure and cost effective workspace. Use the [Active Assist quickstart guide](https://docs.cloud.google.com/recommender/docs/quickstart-active-assist) to get started with the Active Assist.

Alternatively, you can follow the [In Context quickstart guide](https://docs.cloud.google.com/recommender/docs/quickstart-incontext) to find recommendations directly in your service pages. Recommendations can also be reviewed and applied or dismissed using the [Google Cloud CLI or REST API](https://docs.cloud.google.com/recommender/docs/using-api).

## Intelligence Centers and Tools

Active Assist offers intelligent tools that helps you proactively monitor and manage your cloud. We offer tools such as the Network Intelligence Center and Policy Simulator to simplify and automate your management experience on Google Cloud. Read the following documentation pages for more information on how our products can help you optimize your cloud experience.

  * [Network Intelligence Centers](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [Policy Simulator](https://docs.cloud.google.com/iam/docs/simulating-access)
  * [Policy Analyzer](https://docs.cloud.google.com/asset-inventory/docs/analyzing-iam-policy)
  * [Policy Troubleshooter](https://docs.cloud.google.com/iam/docs/troubleshooting-access)
  * [Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
