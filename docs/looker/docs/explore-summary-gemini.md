---
url: https://docs.cloud.google.com/looker/docs/explore-summary-gemini/
title: Generate a summary of an Explore using Gemini assistance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:01.228395+00:00
---

# Generate a summary of an Explore using Gemini assistance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/explore-summary-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Generate a summary of an Explore using Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This documentation page describes how to use Gemini in Looker to generate a summary of an [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores).

**Note:** The ability to use Gemini in Looker to provide summaries of Explores is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, [use this form](https://forms.gle/Mu2JTanqzXAUiN9x8) and provide the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



[Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) provides generative AI-powered assistance to help you work with your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

To use Gemini in Looker to generate Explore summaries, note the following requirements:

  * Gemini in Looker must be enabled for your Looker instance: 
    * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must be enabled for Gemini in Looker in the Admin settings. For detailed enablement instructions, see the [Admin settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
    * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/gemini-overview-looker), the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.
  * The **Trusted Tester Features** option must be enabled: 
    * For Looker (original), [enable the Trusted Tester Features option on the **Platform > Gemini in Looker** panel](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil#enable-and-disable-gil-original) in the Looker Admin settings.
    * For Looker (Google Cloud core), [enable Trusted Tester features in the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini#enable-and-disable-gil-core).
  * You must be assigned a Looker role that contains the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a LookML project.
  * You must be assigned the Looker [**Gemini**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini) role.



## Viewing the summary of an Explore

When enabled, Gemini in Looker will generate a summary of an Explore by using the [description parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore-description) in the LookML model for any Explore where the LookML developer hasn't already defined a summary.

To view the summary from a Looker [classic Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores), open the Explore, and click the info **Explore Summary** info button next to the Explore name.

To view the summary from the [new Explore experience](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview), click the info **Explore Summary** info button on the [**Configure** panel](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#navigating_the_configure_panel).

Gemini in Looker will display a summary of the Explore, including the suggested purpose of the Explore and the types of data that are used in the query.

At the bottom of the summary, Gemini in Looker displays both a  thumb_up **Like** icon and a thumb_down **Dislike** icon, which let you indicate whether the summary was useful.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
