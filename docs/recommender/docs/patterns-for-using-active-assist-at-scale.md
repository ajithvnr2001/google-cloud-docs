---
url: https://docs.cloud.google.com/recommender/docs/patterns-for-using-active-assist-at-scale/
title: Patterns for using Active Assist at scale \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:50.150638+00:00
---

# Patterns for using Active Assist at scale  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/patterns-for-using-active-assist-at-scale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Patterns for using Active Assist at scale

This document is the first part in a series that introduces architectural patterns that enterprises can use to optimize their cloud footprint at scale using [Active Assist](https://docs.cloud.google.com/solutions/active-assist). This document is intended for people in the following roles:

  * Enterprise architects
  * Engineering leads
  * People who work in security and create automation to optimize cloud security, performance, and manageability



This document discusses the following:

  * The benefits of using Active Assist in an organization.
  * The challenges that organizations might encounter when they adopt Active Assist at enterprise-scale.
  * How to design automation pipelines using Active Assist.



The series consists of the following parts:

  * Patterns for using Active Assist at scale (this document)
  * [Using serverless pipelines with Active Assist](https://docs.cloud.google.com/recommender/docs/using-serverless-pipelines-with-active-assist)
  * [Using the GKE Enterprise toolchain with Active Assist ](https://docs.cloud.google.com/recommender/docs/using-anthos-toolchain-with-active-assist)



## Active Assist

Active Assist is a portfolio of tools that use data, intelligence, and machine learning to reduce cloud complexity and administrative work, helping enterprises to optimize the security, performance, manageability, and cost of their cloud.

Many enterprises have a mandate to ensure that [the principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege) is applied to their business applications and infrastructure. Enterprises also want to minimize resource waste and maximize the performance of business applications while also reducing administrative work and cost. As a consequence, IT departments often face scrutiny and pressure to meet these requirements with speed and agility. Active Assist gives them tools that they can use to help meet these goals.

## Cloud optimization for enterprises

Because workloads, infrastructure, security needs, and processes are unique to each enterprise, you must adapt cloud optimization strategies to meet your specific needs.

In the context of this document, cloud optimization strategies for your Google Cloud footprint focus on how you can leverage the Active Assist portfolio when you plan and design optimization strategies.

### Defining a vision and understanding drivers

It's important for enterprises to define the issues that they want to use to inform their approach for cloud footprint optimization. The following are common issues:

  * Security
  * Performance
  * Cost optimization
  * Agility



### Enterprise goals

When you begin to architect an automation pipeline for Active Assist recommendations, you should start by defining the goals for your enterprise and assigning priorities to each objective. You can then map these priorities to a roadmap for rolling out and scaling Active Assist in your Google Cloud organization.

For example, an enterprise might want to use Active Assist recommendations for security and cost optimization. However, the enterprise might initially choose to invest in building an automation pipeline for the security-related recommendations that Active Assist generates. At a later stage, as the enterprise gains more experience in using the Active Assist portfolio and matures in their automation journey, it might automate other types of [recommendations](https://docs.cloud.google.com/recommender/docs/recommenders), for example, [VM rightsizing](https://docs.cloud.google.com/compute/docs/instances/apply-sizing-recommendations-for-instances) and [Idle VM Recommender](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations).

## Designing a strategy

Enterprises must have a clearly defined process for how they want to review and actuate the recommendations that Active Assist generates. We recommend a phased approach that incorporates an increasing degree of automation in a measured manner. An iterative approach that enterprises can take when adopting Active Assist in their Google Cloud organization is as follows:

  * **Phase one** : 
    * Review Active Assist recommendations in the [Google Cloud console](https://docs.cloud.google.com/cloud-console).
    * Export the recommendations to [BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).
  * **Phase two** : 
    * Use Recommender APIs.
  * **Phase three** : 
    * Integrate recommendations review into DevOps pipelines.



This approach lets you iteratively incorporate more automation into your Active Assist recommendations pipelines.

### Phase one: Reviewing Active Assist recommendations in Google Cloud console

In the first phase, you review Active Assist recommendations in the Google Cloud console using [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist). You use a console-based approach to review and implement recommendations. This approach helps you gain familiarity with Active Assist recommendations while assessing their suitability. It also helps you to decide which recommendation categories you want to prioritize. As shown in the following image, Active Assist lets you review recommendations for each resource category that recommendations are available for and drill into the relevant details for each resource within the group.

![Recommendations by resource category.](https://docs.cloud.google.com/static/recommender/docs/images/recommendation-hub.png)

Enterprise teams can export recommendations to BigQuery. Exporting recommendations to BigQuery lets you review recommendations at scale across the organization. It also lets you run queries in specific areas of interest for your enterprise. You can also consider [building a dashboard](https://cloud.google.com/blog/topics/cost-management/manage-cloud-costs-with-new-oss-recommendations-dashboard) to help your team better view and manage your recommendations. 

### Phase two: Using the Recommender APIs

In the second phase, you combine automation with manual reviews and validations to implement recommendations generated by Active Assist. This approach helps you to gain agility. It also lets you make the most of platform-generated recommendations at scale, while retaining tight control on how recommendations are implemented.

You learn how this approach can be realized in [Using Serverless pipelines with Active Assist](https://docs.cloud.google.com/architecture/using-serverless-pipelines-with-active-assist).

### Phase three: Integration recommendations into DevOps pipelines

In the third phase, you bring the review of recommendations into your DevOps pipeline. You inject recommendations management and analysis into the DevOps pipeline, enabling a streamlined process for resource and recommendations management. This approach also enables the development of an approvals process that your teams might already be using as part of the continuous integration and continuous deployment (CI/CD) process. This step relies more heavily on automation and code-based analysis of recommendations than phase two.

Because this approach needs an initial investment of effort to develop the automation framework, we recommend that you don't implement this phase until you have a well-established DevOps strategy.

When you have a defined strategy for the adoption of Active Assist, the next step is to execute and roll out your phased approach.

## What's next

  * Read how Active Assist can [help you to optimize Google Cloud resources](https://cloud.google.com/blog/products/management-tools/optimize-google-cloud-resources-with-active-assist).
  * Learn about [modern CI/CD with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-user-guide).
  * See how you can [achieve least privilege access using Policy Intelligence](https://www.youtube.com/watch?v=LYUVnvRovIM&feature=youtu.be).
  * Read about [using IAM Recommender to bulk-apply least privilege principles](https://cloud.google.com/blog/products/identity-security/using-iam-recommender-to-bulk-apply-least-privilege-principles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
