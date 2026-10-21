---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/using-the-gemini-case-summary-widget/
title: Summarize cases with Gemini \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:13:56.686632+00:00
---

# Summarize cases with Gemini  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/using-the-gemini-case-summary-widget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Summarize cases with Gemini 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

The **Gemini Summary** widget generates an AI-based assessment of how much attention a case might require. It analyzes findings from the Triage and Investigation Agent (TIN), including automated verdicts and reasoning, alongside the following case data:

  * Raw JSON of the event
  * Involved entities
  * Graph data for involved entities (to determine if they have appeared in previous malicious cases)
  * Similar cases



The widget summarizes alert data and investigation findings into three sections: **What Actually Happened?** , **Case Activity** , and **Next and Pending Actions** , which provides recommended steps for remediation.

**Note:** The widget considers entities, but doesn't automatically regenerate the summary when entity enrichment is updated. Manually refresh the widget to include the new data.

You can provide feedback on the accuracy and usefulness of the AI-generated classification, summary, and remediation recommendations.

The **Gemini Summary** widget appears in the **Case Overview** tab on the **Cases** page. For cases with only one alert, you must manually click the **Case Overview** tab to view the widget.

**Note:** The **Gemini Summary** widget isn't displayed for manually created cases, or request cases that are initiated from **Your Workdesk**.

### Provide feedback for Gemini Summary

To submit feedback on the Gemini Summary, follow these steps:

  1. Choose one of the following: 
     * Click thumb_up **Thumb up** if the summary is accurate and helpful. Optionally, enter comments in the **Additional Feedback** field.
     * Click thumb_down **Thumb down** if the summary is inaccurate or unhelpful. Select a reason from the list and enter any relevant context in the **Additional Feedback** field.
  2. Click **Send Feedback** to submit your response.



### Remove the Gemini Summary widget

The **Gemini Summary** widget is included, by default, in the case view layout.

To remove it from the default view, follow these steps:

  1. Go to **SOAR Settings > Case Data > Views**.

  2. Select **Default Case View**.

  3. Locate the **Gemini Summary** widget and click delete **Delete**.


**Note:** On average, this feature supports case summary generation at a rate of 2 cases per minute, with a maximum of 100 cases per hour and is subject to Vertex capacity constraints.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
