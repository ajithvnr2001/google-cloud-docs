---
url: https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-faq/
title: Risk analytics FAQ \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:33:04.885711+00:00
---

# Risk analytics FAQ  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Risk analytics FAQ 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

## What is Risk Analytics?

The [Risk Analytics dashboard](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard) helps you identify unusual behavior and potential risks posed by entities within an enterprise. It consists of two main sections: Behavioral Analytics and [Watchlists](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#navigate_to_the_watchlists_tab).

## Who can access Risk Analytics?

Only users with the relevant privileges can access Risk Analytics. If your organization uses [data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact#ueba_risk_analytics), you need to have global scope to access risk analytics.

## What is Behavioral Analytics?

The **Behavioral Analytics** section lists entities based on their Google Security Operations [entity risk scores](https://docs.cloud.google.com/chronicle/docs/detection/metrics-functions).

The section offers these key components:

  * **Summary metrics** : Shows a top-level view of entities based on Google SecOps entity risk modeling. This visualization displays up to [10,000 entities with the highest risk scores](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#entity_count_risk_score_and_entities_table).

  * **Entities table** : Tracks an entity's risk over time and provides context for investigations.


**Note:** All entities are continuously tracked, and their risk score is available for use in rules (for example, within the rule engine).

## How does the Risk Calculation Window work?

The [Risk Calculation Window](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#adjust_the_risk_calculation_window) lets users change the timeframe for the dashboard, enabling the analysis of data over different periods. Shorter timeframes, such as 24 hours, help uncover events like brute force login attempts, while longer timeframes, such as 7 days, help in examining long-term malicious activity.

## Can I view historical risk scores?

Yes, you can view historical risk scores by selecting a specific date and time, which displays risks calculated for the selected 24-hour or 7-day window.

## What is a normalized risk score?

Normalized scores are set between 1 and 1,000 to distinguish entities with detections from those without.

## What are base risk scores?

Base scores are calculated by adding the risk scores across findings (alerts and detections) for an entity during the risk window, with weighting applied.

## How is weighting applied to risk scores?

[Risk score weighting](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#score-weighting) defines how alert and detection risk scores contribute to entity risk score calculations, with values ranging from `0` to `1`, where a weighting of `1` has no impact on the risk score. The default weighting value is `0.2` and can be modified in **Settings**. 

## How is the base entity risk score calculated?

The formula for the base entity risk score is: (Maximum risk score for the finding) + (Weighting * (Sum of the remaining risk scores for the findings)).

## What are default risk scores for alerts and detections?

The default risk score for alerts is 40 and for detections is 15. You can modify these defaults in **Settings** or within rules.

## What is the closed alert coefficient?

If a security analyst marks an alert as _closed_ , its risk score is multiplied by a coefficient that ranges from 0 to 1 .

## How do Risk Score modifications with TTL and without TTL work?

The Base entity risk score is modified by a multiplying factor for the time range, and the detection risk score is modified with a multiplying factor. These factors are specified by Google SecOps.

## How are normalized risk scores calculated?

Base entity risk scores are normalized using min-max normalization and range from 1 to 1,000. Entities with a 0 risk score are excluded.

## What is the Entity Analytics page?

Clicking an entity name in the Entities table leads to the **Entity Analytics** page, which displays an Event range window, a Findings Timeline, and a detailed Findings table. The Event range window allows filtering up to 90 days.

## What are some examples of how Risk Analytics can be used?

You can use Risk Analytics to identify high data download volumes, suspicious numbers of failed login attempts, or dialog messages that may indicate malware.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
