---
url: https://docs.cloud.google.com/looker/docs/gemini-expression-asst/
title: Write Looker expressions with Gemini assistance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:34.533441+00:00
---

# Write Looker expressions with Gemini assistance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/gemini-expression-asst/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Write Looker expressions with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

This documentation page describes how to use Gemini assistance to write [Looker expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) for [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) and [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields).

[Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) provides generative AI-powered assistance to help you work with your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

To use Gemini to write expressions, note the following requirements:

  * Gemini in Looker must be enabled for your Looker instance: 
    * For Looker (original), the instance must be running Looker 26.4 or later, and the instance must be enabled for Gemini in Looker in the **Admin** settings. For detailed enablement instructions, see the [**Admin** settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
    * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/gemini-overview-looker), the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.
  * **Looker Assistants** must be enabled in the [Gemini in Looker panel](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil#enable-and-disable-gil-original) in the **Admin** settings.
  * You must be assigned a Looker role that contains the [`create_table_calculations`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) permission to use Gemini to write a table calculation expression, or a role that contains the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission to write a custom field expression.
  * You must be assigned the Looker [**Gemini**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini) role.



## Use Gemini to write an expression

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To use Gemini for assistance in creating a Looker expression, follow these steps:

  1. When creating a table calculation or custom dimension, click **Help me write an expression with Gemini**.

![The table calculation dialog showing the Help me write an expression link.](https://docs.cloud.google.com/static/looker/docs/images/expression-asst-2604.png)

  2. In the **Help me write an expression** dialog, describe the table calculation or custom dimension that you want to write using natural language.

  3. Click **Create**.

  4. Gemini will display the expression that's created based on your description. You can click **Refine** to add to or modify your description, or **Apply** to add the expression to your table calculation or custom dimension definition.




## Tips for using the Gemini Expression Assistant

Here are some tips for using Gemini to write table calculations or custom dimensions:

  * For best results, write your prompts in American English. See the [Gemini for Google Cloud limitations](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai#gemini-limitations) documentation for more information.
  * The **Help me write an expression** panel does not retain context from a previous prompt in the conversation and does not retain prompts across logins and refreshes.
  * When you use an expression that was suggested by Gemini, always test your new fields in an Explore.



## Sample prompts

Here is an example using the **Help me write an expression** option that asks Gemini to create a table calculation that shows the percentage change from one row to the next. Then this example further refines the table calculation to include formatting.

Enter the first prompt in the **Describe your expression** field:

`Add a field that shows percentage change from one row to the next`

Gemini returns a suggested expression:

![Gemini returns a suggested expression to show percentage change from one row to the next.](https://docs.cloud.google.com/static/looker/docs/images/percent-change-row-table-calc-2604.png)

Then, click **Refine** to ask Gemini to add formatting:

`Now format the output in percentages and append an up arrow when the percentage is above zero or a down arrow when the percentage is below zero`

Gemini updates the suggested expression:

![Gemini returns a new expression that adds formatting.](https://docs.cloud.google.com/static/looker/docs/images/percent-change-formatting-table-calc-2604.png)

Click **Apply** , and the new table calculation is created:

![The new table calculation is added to the Explore.](https://docs.cloud.google.com/static/looker/docs/images/explore-with-generated-table-calc-2604.png)

## Provide feedback

You can provide feedback for the generated expression in the **Help me write an expression** panel. If the generated expression looks correct, click the thumb_up thumbs-up icon. If the generated expression looks incorrect or isn't what you expected, click the thumb_down thumbs-down icon.

**Note:** Gemini in Looker is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) and be sure to include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



## Related resources

  * [Learn more about Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview)
  * [Learn more about Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
