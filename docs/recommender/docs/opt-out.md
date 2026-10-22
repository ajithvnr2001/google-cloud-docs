---
url: https://docs.cloud.google.com/recommender/docs/opt-out/
title: Opt out of data processing \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:05.922951+00:00
---

# Opt out of data processing  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/opt-out/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Opt out of data processing

Google Cloud collects data when customers use its services. This data does not include customer data. Google Cloud uses the data it collects to provide insights and recommendations in [Recommender](https://docs.cloud.google.com/recommender/docs) and specific reports in the Google Cloud console. These insights, recommendations, and reports help you use Google Cloud services more securely and efficiently.

At any time, you can stop the processing of this data for the purpose of providing these recommendations. You can also view any personal data used to generate these recommendations. To learn how to view personal data, refer to the [export data documentation](https://docs.cloud.google.com/recommender/docs/transparency-and-control-center/exporting-data).

By default, Google Cloud processes data and generates insights and recommendations for all organizations and projects. To opt out of insights and recommendations for an organization or project, you must have one of the following Identity and Access Management (IAM) roles on the organization or project:

  * Owner (`roles/owner`)
  * Data Processing Controls Resource Admin (`roles/dataprocessing.admin`), or an equivalent custom IAM role

**Note:** Starting or stopping recommendations can take up to 3 business days.

To opt out of insights and recommendations, or to prevent specific services from consuming logs, follow these steps:

  1. In the Google Cloud console, go to the **Privacy & Security** page.

[Go to the Privacy & Security page](https://console.cloud.google.com/iam-admin/privacy)

  2. Click on the **Transparency & control** tab.

  3. In the **Organization** or **Billing account** tabs, select all data processing groups you want to stop, then click the **Disable** button next to the table heading. The selected groups' data will no longer be processed for insights and recommendations.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
