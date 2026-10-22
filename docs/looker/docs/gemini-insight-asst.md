---
url: https://docs.cloud.google.com/looker/docs/gemini-insight-asst/
title: Use Gemini in Looker to gain insights into your data \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:44.039486+00:00
---

# Use Gemini in Looker to gain insights into your data  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/gemini-insight-asst/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Use Gemini in Looker to gain insights into your data Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [new Explore experience preview feature](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview) series.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** The Gemini Insight Assistant is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, [use this form](https://docs.google.com/forms/d/16LvBDB-ZZ63RjVlo6rmgrt4HsjbUF-yt2KevG8mCeSk/edit) and provide the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



This documentation page describes how to use the Gemini Insight Assistant to ask questions to gain insights into an Explore, and then use the results to build or modify the Explore.

[Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) provides generative AI-powered assistance to help you work with your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

To use the Insight Assistant to work with your data, note the following requirements:

  * Gemini in Looker must be enabled for your Looker instance: 
    * For Looker (original), the instance must be running Looker 26.6 or later, and the instance must be enabled for Gemini in Looker in the **Admin** settings. For detailed enablement instructions, see the [**Admin** settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
    * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview), the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.
  * The **Explore Insight Assistant** must be enabled in the [Gemini in Looker panel](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil#enable-and-disable-gil-original) in the **Admin** settings.
  * You must be assigned a Looker role that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission to access and use the Explore page.
  * You must be assigned the Looker [**Gemini**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini) role.



## Using the Insight Assistant

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

The Gemini Insight Assistant lets you use natural language to ask questions about and analyze the data that's used by a specific Explore. To use the Gemini Insight Assistant to ask questions about and generate queries for your data, follow these steps:

  1. Open the **Insight Assistant** panel by either clicking tips_and_updates **Insight Assistant** button or by clicking the **Ask Insight Assistant** tile in a blank Explore:

![](https://docs.cloud.google.com/static/looker/docs/images/insight-asst-tile-2606.png)

  2. Ask a question in the **Ask a data question** field. The Insight Assistant will return the answer to your question, describing the process the assistant is using to generate the response, showing key details in your data that it used to generate the response, and listing the fields from your Explore that it used.

![The Insight Assistant response when asked What are the most delayed flights?](https://docs.cloud.google.com/static/looker/docs/images/insight-asst-results-2612.png)

  3. Once the Insight Assistant returns the response, it hides the process it used to generate the response. But, if you click **Show thinking** , the Insight Assistant will display the process it used to generate the response.

  4. If you click the **Insert** button at this point, the Insight Assistant will create an Explore by using the fields that are listed in the response.

  5. You can ask further questions in the **Ask a data question** field to refine or update your results. You can also click  edit **Edit** button to edit your original question, or click the edit_square **New Chat** button to remove your question and the results, and start over with new question.




## Tips for using the Insight Assistant

Here are some tips for using the Insight Assistant:

  * For best results, write your prompts in American English. See the [Gemini for Google Cloud limitations](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai#gemini-limitations) documentation for more information.
  * When you use a response that was suggested by Gemini, always test your new fields in the Explore.



## Provide feedback

You can provide feedback for the Insight Assistant in the **Insight Assistant** panel. If the response looks correct, click the thumb_up thumbs-up icon. If the Insight Assistant response looks incorrect or isn't what you expected, click the thumb_down thumbs-down icon.

**Note:** Gemini in Looker is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) and be sure to include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



## Related resources

  * [Learn more about Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview).
  * [Learn more about Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
