---
url: https://docs.cloud.google.com/billing/docs/how-to/budget-api-overview/
title: Get started with the Cloud Billing Budget API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:08.523410+00:00
---

# Get started with the Cloud Billing Budget API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/budget-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Get started with the Cloud Billing Budget API Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud customers can plan, monitor, and control costs using [budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets). Monitoring and controlling costs effectively is important, especially as you scale your business in the cloud. When you're using Google Cloud, our [budgets and alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) features are a powerful part of your cost monitoring toolkit, letting you set your target spending and notify key stakeholders if you're getting off track.

## About budgets

Cloud Billing offers two types of budgets:

  * [**Alerts-only budgets**](https://docs.cloud.google.com/billing/docs/how-to/budgets) – Available for _all_ services. Alerts-only budgets let you track your _actual spend_ relative to your planned budget, then generate alerts when your spend exceeds any threshold amounts you've set. Calculating _actual spend_ typically takes up to 24 hours.

After you set your budget scope (filters) and a budget amount, you set budget alert threshold rules that are used to trigger email notifications. Budget alert emails help you stay informed about how your spend is tracking against your alerts-only budget. You can also use alerts-only budgets to automate cost control responses using [Pub/Sub topics for programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications) (for example, to forward your budget messages to other mediums such as Slack, or to automate cost management tasks).

  * [**Spend-cap budgets**](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps) – Available for _limited_ services. Spend-cap budgets let you set a maximum amount to spend on an [eligible service](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#eligible-services) in a specified project. When your _gross, estimated_ spend exceeds your budget amount, the spend cap is enforced, which pauses _new_ usage of the service in the specified project until the spend cap is lifted. Since spend caps are enforced using estimated, gross costs, spend caps are triggered much faster than alerts-only budgets, which use _actual spend_ calculations.




In the Google Cloud console, you can manage one Google Cloud budget at a time. Using the Cloud Billing Budget API, you can view, create, and manage budgets programmatically at scale, up to 50,000 budgets for each Cloud Billing account. [Learn how to check your budget quota](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-quota).

Examples for using the Cloud Billing Budget API include the following:

  * Create a separate alerts-only budget for each of your Google Cloud projects so you know which areas of your Google Cloud environment are spending more than expected.
  * Create a spend-cap budget for each of your Google Cloud projects to prevent overspending on a specific service.
  * Bulk update all of your budgets after quarterly financial planning.
  * Integrate with your company's deployment manager to add the creation of budgets to your cloud provisioning workflow.



## Prerequisites

Read through the [prerequisites](https://docs.cloud.google.com/billing/docs/how-to/budget-api-prereqs) before you start coding your first Cloud Billing budget application.

## Setup

Complete these [setup steps](https://docs.cloud.google.com/billing/docs/how-to/budget-api-setup) to get ready to start using the Cloud Billing Budget API.

## Using the API

To get up and running with the Cloud Billing Budget API, refer to the instructions in the user guide for the type of budget you want to manage:

  * Using the Cloud Billing Budget API for [**alerts-only budgets**](https://docs.cloud.google.com/billing/docs/how-to/budget-api).
  * Using the Cloud Billing Budget API for [**spend cap budgets**](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap).



## Reference

For a full list of methods, see the reference documentation.

  * [REST API](https://docs.cloud.google.com/billing/docs/reference/budget/rest)



[ Next Prerequisites  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/budget-api-prereqs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
