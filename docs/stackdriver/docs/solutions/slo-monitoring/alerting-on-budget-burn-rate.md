---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate/
title: Alerting on your burn rate \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:13.655331+00:00
---

# Alerting on your burn rate  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Alerting on your burn rate Stay organized with collections  Save and categorize content based on your preferences. 

You can create alerting policies on your service-level objectives (SLOs) to let you know whether you are in danger of violating an SLO. You select the SLO that you want to monitor, and then configure an alerting policy to monitor that SLO. The condition is typically expressed by selecting a threshold value that constitutes a violation, and a period for which the violation is permitted. If the threshold is exceeded for more than the allowable period, the alerting policy is triggered.

This page describes alerting on the burn rate of your error budget. It does not cover alerting policies in detail; it assumes you already know the basic concepts of conditions and notification channels.

For general information about alerting policies and how to create them, see [Using alerting policies](https://docs.cloud.google.com/monitoring/alerts).

For specific steps in creating a SLO-based alert policy, see the following:

  * [Creating an alerting policy](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert) by using the Google Cloud console.
  * [Creating an alerting policy](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/create-policy-api) by using the Cloud Monitoring API.



## Burn rate of error budget

Your error budget for a compliance period is (1 − _SLO goal_) × (_eligible events in compliance period_). If your SLO goal is 95%, then it is acceptable for 5% of the events measured by your SLI to fail before your SLO goal is missed.

The _burn rate_ tells you how fast you are consuming your error budget for a compliance period. The burn rate is dependent upon the number of eligible events and the number of error events received in the compliance period. For example, if there are no error events occurring, then the error budget isn't being consumed and the burn rate is zero. For an example that illustrates how you can compute the maximum down time for a service, see [Alert on Burn Rate](https://sre.google/workbook/alerting-on-slos/#4-alert-on-burn-rate).

The burn-rate metric is normalized such that a burn rate of greater than one indicates that if the measured error rate is sustained over any future compliance period, then the service will be out of SLO for that period. For more information, see [Error budgets](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#defn-error-budget).

The burn-rate metric is retrieved by the time-series selector `select_slo_burn_rate`. A burn-rate alerting policy notifies you when your error budget is consumed faster than a threshold you define, measured over the alert's compliance period. There are other time-series selectors; see [Retrieving SLO data](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/timeseries-selectors) for more information. You can create alerting policies that use some of these other time-series selectors, but you must create them by using the Cloud Monitoring API.

## Overview of creating an alerting policy on an SLO

Creating an alerting policy for an SLO is similar to creating an alerting policy for metrics. This section reviews the general steps for creating an alerting policy.

To create an alerting policy for an SLO, you take the following steps:

  1. Identify the SLO you want to base the alerting policy on.

  2. Construct a condition for your alerting policy that uses the chosen SLO. In the condition, you specify a time-series selector to use in retrieving SLO data. You also specify a duration, a threshold and a comparison that determine when the SLO is out of compliance.

For example, if you use the time-series selector for burn rate, the retrieved data reflects the burn rate of the error budget for the chosen SLO.

The condition is also where you specify the threshold and duration of violations of the SLO before triggering an alert. For example, you want the burn rate to be some amount over the desired rate for some period before triggering an alert. The value for “some amount over” is the condition's threshold, and the value for “some period” is the condition's duration.

  3. Identify or create a notification channel to use in your alerting policy.

  4. Provide documentation that explains to users what triggered the alerting policy.




For general information about alerting policies and how to create them, see [Using alerting policies](https://docs.cloud.google.com/monitoring/alerts).

### Alerting policies and lookback periods

When you retrieve the SLO data for an alerting policy, you specify an identifier for the SLO and a lookback period. The lookback period determines how far back in time to retrieve data. Critically, the lookback period is also used as the compliance period for calculating the SLO performance and error budget.

It is not currently possible to base alerts on the error budget consumption rate of an SLO using a compliance period of greater than 24 hours. In many cases, approximating your long-term (for example, 28- or 30-day) compliance period with one of less than 24 hours is sufficient for the purpose of detecting outages and driving your short-term operational response to them.

Shorter compliance periods provide faster detection of problems, but with the caveat that large changes in traffic and error rates over the course of a day may result in overly-sensitive alerting during low-traffic periods. Consider using a burn-rate threshold significantly larger than 1 to reduce alert sensitivity during these times.

### Types of error-budget alerts

When setting up alerting policies to monitor your error budget, it's a good idea to set up two related alerting policies:

  * **Fast-burn** alert, which warns you of a sudden, large change in consumption that, if uncorrected, will exhaust your error budget very soon. _“At this rate, we'll burn through the whole month's error budget in two days!”_

For a fast-burn alert, use a shorter lookback period so you are notified quickly if a potentially disastrous condition has emerged and persisted, even briefly. If it is truly disastrous, you don't want to wait long to notice it.

The threshold for the rate of consumption you alert on here is much higher than the baseline ideal for the lookback period.

**Key Point:** A good starting point for a fast-burn threshold policy is **10x the baseline** with a short (1- or 2-hour) lookback period.
  * **Slow-burn** alert, which warns you of a rate of consumption that, if not altered, exhausts your error budget before the end of the compliance period. This type of condition is less urgent than a fast-burn condition. _“We are slightly exceeding where we'd like to be at this point in the month, but we aren't in big trouble yet.”_

For a slow-burn alert, use a longer lookback period to smooth out variations in shorter-term consumption.

The threshold you alert on in a slow-burn alert is higher than the ideal performance for the lookback period, but not significantly higher. A policy based on a shorter lookback period with high threshold might generate too many alerts, even if the longer-term consumption levels out. But if the consumption stays even a little too high for a longer period, it eventually consumes all of your error budget.

**Key Point:** A good starting point for a slow-burn threshold is **2x the baseline** with a 24-hour lookback period.



## Next steps

  * To create a SLO-based alerting policy by using the Google Cloud console, see [Creating an alerting policy (Google Cloud console)](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert).
  * To create a SLO-based alerting policy by using the Monitoring API, see [Creating an alerting policy (API)](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/create-policy-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
