---
url: https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types
title: Package budgets_v1.types (1.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:11.850442+00:00
---

# Package budgets_v1.types (1.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package budgets_v1.types (1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.21.0  1.20.0  1.19.0  1.18.0  1.17.2  1.16.0  1.15.1  1.14.5  1.13.0  1.12.0  1.11.1  1.10.0  1.9.1  1.8.0  1.7.3  1.6.2  1.5.1  1.4.4  1.3.0  1.2.0  1.1.1  1.0.1  0.4.2  0.3.0  0.2.0  0.1.0 

API documentation for `budgets_v1.types` package.

## Classes 

### [Budget](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.Budget)

A budget is a plan that describes what you expect to spend on Cloud projects, plus the rules to execute as spend is tracked against that plan, (for example, send an alert when 90% of the target spend is met). The budget time period is configurable, with options such as month (default), quarter, year, or custom time period.

### [BudgetAmount](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.BudgetAmount)

The budgeted amount for each usage period.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CalendarPeriod](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.CalendarPeriod)

A `CalendarPeriod` represents the abstract concept of a time period that has a canonical start. Grammatically, "the start of the current `CalendarPeriod`". All calendar times begin at 12 AM US and Canadian Pacific Time (UTC-8).

### [CreateBudgetRequest](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.CreateBudgetRequest)

Request for CreateBudget

### [CustomPeriod](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.CustomPeriod)

All date times begin at 12 AM US and Canadian Pacific Time (UTC-8).

### [DeleteBudgetRequest](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.DeleteBudgetRequest)

Request for DeleteBudget

### [Filter](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.Filter)

A filter for a budget, limiting the scope of the cost to calculate.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetBudgetRequest](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.GetBudgetRequest)

Request for GetBudget

### [LastPeriodAmount](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.LastPeriodAmount)

Describes a budget amount targeted to the last Filter.calendar_period spend. At this time, the amount is automatically 100% of the last calendar period's spend; that is, there are no other options yet. LastPeriodAmount cannot be set for a budget configured with a Filter.custom_period.

### [ListBudgetsRequest](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.ListBudgetsRequest)

Request for ListBudgets

### [ListBudgetsResponse](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.ListBudgetsResponse)

Response for ListBudgets

### [NotificationsRule](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.NotificationsRule)

NotificationsRule defines notifications that are sent based on budget spend and thresholds.

### [ThresholdRule](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.ThresholdRule)

ThresholdRule contains the definition of a threshold. Threshold rules define the triggering events used to generate a budget notification email. When a threshold is crossed (spend exceeds the specified percentages of the budget), budget alert emails are sent to the email recipients you specify in the `NotificationsRule <#notificationsrule>`__.

Threshold rules also affect the fields included in the `JSON data object <https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#notification_format>`__ sent to a Pub/Sub topic.

Threshold rules are _required_ if using email notifications.

Threshold rules are _optional_ if only setting a ``pubsubTopic` NotificationsRule <#NotificationsRule>`__, unless you want your JSON data object to include data about the thresholds you set.

For more information, see `set budget threshold rules and actions <https://cloud.google.com/billing/docs/how-to/budgets#budget-actions>`__.

### [UpdateBudgetRequest](https://docs.cloud.google.com/python/docs/reference/billingbudgets/latest/google.cloud.billing.budgets_v1.types.UpdateBudgetRequest)

Request for UpdateBudget

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
