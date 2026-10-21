---
url: https://docs.cloud.google.com/looker/docs/gemini-quick-starts/
title: Generate Quick Start analyses for an Explore using Gemini \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:32:13.713360+00:00
---

# Generate Quick Start analyses for an Explore using Gemini  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/gemini-quick-starts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Generate Quick Start analyses for an Explore using Gemini Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This documentation page describes how to use Gemini in Looker to generate [Quick Start analyses](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#quick_start_analyses) for an Explore.

**Note:** The ability to use Gemini in Looker to generate Quick Start analyses for an Explores is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, [use this form](https://docs.google.com/forms/d/16LvBDB-ZZ63RjVlo6rmgrt4HsjbUF-yt2KevG8mCeSk/edit) and provide the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



[Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) provides generative AI-powered assistance to help you work with your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

To use Gemini in Looker to generate Quick Start analyses, note the following requirements:

  * Gemini in Looker must be enabled for your Looker instance: 
    * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must be enabled for Gemini in Looker in the Admin settings. For detailed enablement instructions, see the [Admin settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
    * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/gemini-overview-looker), the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.
  * The **AI-Assisted Quick Starts** Trusted Tester Features option must be enabled: 
    * For Looker (original), [enable the AI-Assisted Quick Starts option on the **Platform > Gemini in Looker** panel](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil#enable-and-disable-gil-original) in the Looker Admin settings.
    * For Looker (Google Cloud core), [enable the AI-Assisted Quick Starts option in the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini#enable-and-disable-gil-core).
  * You must be assigned a Looker role that contains the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a LookML project.
  * You must be assigned the Looker [**Gemini**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini) role.



## Generating Quick Start analyses

When generated Quick Start analyses are enabled, and you select an Explore that doesn't contain [modeled queries](https://docs.cloud.google.com/looker/docs/reference/param-explore-query), Gemini in Looker can generate them from the Looker Explore interface.

### Generating Quick Start analyses from a classic Explore

If you're using the [classic Explore experience](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), when you select an Explore from the Explore menu that doesn't already have [Quick Start analyses](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#quick_start_analyses) defined, Gemini in Looker will give you an option to **Try AI Quick Starts**. Click **Add** , and Gemini will analyze the Explore and generate Quick Start analyses.

![ ](https://docs.cloud.google.com/static/looker/docs/images/generated-quickstarts-2602.png)

When you're editing an Explore, you can also generate new Quick Start analyses by clicking the bolt**Quick Start** button next to the Explore name.

### Generating Quick Start analyses from the new Explore experience

If you're using the [new Explore experience](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview), when you select an Explore from the **Explore** menu, click the [**Browse quick starts** card](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#choosing_a_quick_start_option_from_a_blank_explore_in_the_new_explore_experience). If the Explore doesn't already have Quick Start analyses defined, Gemini in Looker will analyze the Explore and generate Quick Start analyses.

You can also generate Quick Start analyses any time by clicking the dynamic_form [**Quick Start** button](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#choosing-a-quick-start-option-once-an-explore-has-run).

## Running a Quick Start analysis

After generating Quick Start analyses, click the analysis card that you want to Explore. The query will automatically run and display results, including the visualization.

Once the Quick Start analysis has finished running, you can modify it like any other Explore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
