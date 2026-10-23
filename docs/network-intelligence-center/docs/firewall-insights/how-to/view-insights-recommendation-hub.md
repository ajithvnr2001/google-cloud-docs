---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-insights-recommendation-hub/
title: View insights in Active Assist dashboard \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:40.722680+00:00
---

# View insights in Active Assist dashboard  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-insights-recommendation-hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  View insights in Active Assist dashboard Stay organized with collections  Save and categorize content based on your preferences. 

The Active Assist is a feature of the Recommender product that provides usage recommendations for Google Cloud products and services.

The Google Cloud console for the Active Assist shows the following firewall rule insights:

  * Shadowed firewall rules
  * Overly permissive rules



For general information about Active Assist, see [Getting started with Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

Within Active Assist, the names of the cards differ from those used on the Firewall Insights page. For details, review the following sections.

## View shadowed firewall rules

To learn about this insight, see [Shadowed rules](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states#shadowed-firewall-rules) in _Firewall Insights categories and states_.

###  Console 

  1. In the Google Cloud console, go to the **Active Assist**.

[Go to Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. On the card named **Simplify firewall configuration** , click **View all**. The Active Assist displays a page that lists shadowed rules. The **Insight** column for each rule provides a summary of why the rule was identified as a shadowed rule.

  3. To view more details about the shadowed rule and the rules that shadow it, click the insight.




## View overly permissive rule insights

To learn about these insights, see the following sections in [overly permissive rules](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states#overly-permissive-rules) in _Firewall Insights categories and states_ :

  * Allow rules with no hits
  * Allow rules with unused attributes
  * Allow rules with overly permissive IP address or port ranges




###  Console 

  1. In the Google Cloud console, go to the **Active Assist**.

[Go to Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. On the card named **Review overly permissive firewall rules** , click **View all**.

  3. To toggle between the insight types, use the tabs at the top of the page.

You can click the insight for any rule listed to understand why the rule was included in the list. The insight detail shows more information about the hit count and attributes for a rule.




## Mark an insight as dismissed

If any insight isn't meaningful, or if you want to hide it for any other reason, you can dismiss it. After you dismiss an insight, the Google Cloud console no longer displays the insight to you or other users unless you restore it.

###  Console 

  1. In the Google Cloud console, go to the **Active Assist**.

[Go to Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. Find the appropriate card and click **View all**.

  3. If you want to dismiss an insight about an overly permissive rule, use the tabs at the top of the page to navigate to the appropriate insight category.

  4. Select the insights that you want to dismiss, and then click **Dismiss**.

  5. In the confirmation dialog, click **Yes, dismiss**.




## Restore a dismissed insight

If you dismissed an insight that you later think is relevant, you or a user can restore it and make it visible in the Google Cloud console by following these steps.

###  Console 

  1. In the Google Cloud console, go to the **Active Assist**.

[Go to Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. Find the appropriate card and click **View all**.

  3. If you want to dismiss an insight about an overly permissive rule, use the tabs at the top of the page to navigate to the appropriate insight category.

  4. At the top of the page, click **History**.

  5. Click the **Dismissed** tab, which shows dismissed recommendations and insights for the project.

  6. Select the insights that you want to restore.

  7. Click **Restore**.

  8. In the confirmation dialog, click **Restore**.




## What's next

  * [View Firewall Insights metrics](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
