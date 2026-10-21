---
url: https://docs.cloud.google.com/architecture/framework/reliability/set-targets/
title: Set realistic targets for reliability \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:18.791052+00:00
---

# Set realistic targets for reliability  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/reliability/set-targets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Set realistic targets for reliability Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-30 UTC

This principle in the reliability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) helps you define reliability goals that are technically feasible for your workloads in Google Cloud.

This principle is relevant to the _scoping_ [focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas) of reliability.

## Principle overview

Design your systems to be just reliable enough for user happiness. It might seem counterintuitive, but a goal of 100% reliability is often not the most effective strategy. Higher reliability might result in a significantly higher cost, both in terms of financial investment and potential limitations on innovation. If users are already happy with the current level of service, then efforts to further increase happiness might yield a low return on investment. Instead, you can better spend resources elsewhere.

You need to determine the level of reliability at which your users are happy, and determine the point where the cost of incremental improvements begin to outweigh the benefits. When you determine this level of _sufficient reliability_ , you can allocate resources strategically and focus on features and improvements that deliver greater value to your users.

## Recommendations

To set realistic reliability targets, consider the recommendations in the following subsections.

### Accept some failure and prioritize components

Aim for high availability such as 99.99% uptime, but don't set a target of 100% uptime. Acknowledge that some failures are inevitable.

The gap between 100% uptime and a 99.99% target is the allowance for failure. This gap is often called the _error budget_. The error budget can help you take risks and innovate, which is fundamental to any business to stay competitive.

Prioritize the reliability of the most critical components in the system. Accept that less critical components can have a higher tolerance for failure.

### Balance reliability and cost

To determine the optimal reliability level for your system, conduct thorough cost-benefit analyses.

Consider factors like system requirements, the consequences of failures, and your organization's risk tolerance for the specific application. Remember to consider your [disaster recovery metrics](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning), such as the recovery time objective (RTO) and recovery point objective (RPO). Decide what level of reliability is acceptable within the budget and other constraints.

Look for ways to improve efficiency and reduce costs without compromising essential reliability features.

[ Previous arrow_back  Define reliability based on user-experience goals  ](https://docs.cloud.google.com/architecture/framework/reliability/define-reliability-based-on-user-experience-goals)

[ Next Build high availability through redundancy  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/reliability/build-highly-available-systems)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-30 UTC."],[],[]] 
