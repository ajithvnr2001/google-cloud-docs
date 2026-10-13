---
url: https://docs.cloud.google.com/looker/docs/gemini-quick-starts/
title: Generate starter questions for an Explore using Gemini \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:38.138057+00:00
---

# Generate starter questions for an Explore using Gemini  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/gemini-quick-starts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Generate starter questions for an Explore using Gemini Stay organized with collections  Save and categorize content based on your preferences. 

This documentation page describes how to use Gemini in Looker to generate [starter questions](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#quick_start_analyses) for an Explore, or if you are using the classic Explore, [how to generate AI Quick Starts](https://docs.cloud.google.com/looker/docs/gemini-quick-starts#generating_quick_start_analyses_from_a_classic_explore).

[Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) provides generative AI-powered assistance to help you work with your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

To use Gemini in Looker to generate starter question analyses, note the following requirements:

  * Gemini in Looker must be enabled for your Looker instance: 
    * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must be enabled for Gemini in Looker in the Admin settings. For detailed enablement instructions, see the [Admin settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
    * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/gemini-overview-looker), the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.
  * You must be assigned a Looker role that contains the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a LookML project.
  * You must be assigned the Looker [**Gemini**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini) role or be assigned a role that includes the [`gemini_in_looker` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_in_looker).



## Generating starter question analyses from the new Explore experience

When you select an Explore that doesn't contain [modeled queries](https://docs.cloud.google.com/looker/docs/reference/param-explore-query), Gemini in Looker can generate them from the Looker Explore interface.

Select an Explore from the **Explore** menu, and then click the [**Starter Questions** drop-down field](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#choosing_a_starter_question_from_a_blank_explore_in_the_new_explore_experience). If the Explore doesn't already have starter questions defined, Gemini in Looker will analyze the Explore and generate starter questions.

![A blank Explore with the Starter questions drop-down field displayed.](https://docs.cloud.google.com/static/looker/docs/images/blank-explore-starter-questions-2616.png)

You can also generate starter question analyses any time by clicking the dynamic_form [**Show starter questions** button](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#choosing-a-starter-question-once-an-explore-has-run), which will open the **Starter Questions** panel.

![The Starter questions panel with a list of starter questions.](https://docs.cloud.google.com/static/looker/docs/images/starter-questions-panel-2616.png)

### Generating Quick Start analyses from a classic Explore

If you're using the [classic Explore experience](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), when you select an Explore from the Explore menu that doesn't already have [Quick Start analyses](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#quick_start_analyses) defined, Gemini in Looker will give you an option to **Try AI Quick Starts**. Click **Add** , and Gemini will analyze the Explore and generate Quick Start analyses.

![A classic Explore with quick starts displayed.](https://docs.cloud.google.com/static/looker/docs/images/generated-quickstarts-2602.png)

When you're editing an Explore, you can also generate new Quick Start analyses by clicking the bolt**Quick Start** button next to the Explore name.

## Running a starter question analysis

After you've generated starter questions (or AI Quick Starts on the classic Explore experience), click the analysis card that you want to explore. The query will automatically run and display results, including the visualization.

Once the starter question analysis has finished running, you can modify it like any other Explore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
