---
url: https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini/
title: Create visualizations with Gemini assistance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:38.450175+00:00
---

# Create visualizations with Gemini assistance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create visualizations with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

This documentation page describes how to use Gemini assistance to generate JSON formatting options from text-based prompts and then apply that formatting to customize a Looker visualization. Customizing visualizations with the **Visualization Assistant** is a Gemini in Looker feature that is available in Looker (original) and Looker (Google Cloud core) instances.

The **Visualization Assistant** is available for visualizations that use the HighCharts API, which includes most [Cartesian charts](https://docs.cloud.google.com/looker/docs/visualization-types#cartesian_charts), such as the [column chart](https://docs.cloud.google.com/looker/docs/column-options), [bar chart](https://docs.cloud.google.com/looker/docs/bar-options), and [line chart](https://docs.cloud.google.com/looker/docs/line-options), among others.

Gemini in Looker is a product in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This page is intended for users who are exploring data in a Looker instance.

## Before you begin

To customize visualizations with Gemini assistance, note the following requirements:

  * Gemini in Looker must be enabled for your Looker instance: 
    * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must be enabled for Gemini in Looker in the Admin settings. For detailed enablement instructions, see the [Admin settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
    * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.
  * You must be assigned a Looker role that contains the [`gemini_in_looker`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_in_looker) and [`can_override_vis_config`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config) permissions.



## Using the Visualization Assistant

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To customize a visualization with the **Visualization Assistant** , follow these steps:

  1. View a supported visualization in an Explore, or edit a visualization in a Look or dashboard.
  2. Open the **Edit** menu in the visualization.
  3. Click pen_spark **Visualization Assistant** to open the prompt menu.



![](https://docs.cloud.google.com/static/looker/docs/images/advanced-vis-assistant-2410.png)

Within the pen_spark **Visualization Assistant** prompt menu, you can do the following:

  * Type out a plain text prompt of changes for the visualization in the **Ask anything** field. To send send_spark your prompt, press return (Mac) or Enter (PC).
  * Apply generated **Suggestions** to the visualization.
  * Open the **Edit Chart Config** to manually write and edit JSON formatting options.
  * **Clear Chart Overrides** to clear all custom changes applied to the visualization. You will be prompted to **Confirm** removing all changes before proceeding. If you cleared the changes by accident it is possible to retrieve them by navigating back in your browser history.



Once the prompt has run a preview window will open with the options to:

![](https://docs.cloud.google.com/static/looker/docs/images/apply-advanced-vis-config.png)

  * Manually write and edit the generated JSON formatting options: Click **Edit Chart Config** to open the chart configuration editor. Click **Visualization Assistant** to return to the prompt menu.
  * Start a new prompt: Click **Start Over** to begin a new prompt from the pen_spark **Visualization Assistant** menu. All unapplied changes will be lost.
  * Apply the previewed changes to the visualization: Click **Apply**. If changes are made in the **Chart Config** menu, this option will change to **Revalidate and Apply**.
  * Provide feedback about the helpfulness of the prompt response: Select thumb_up to indicate that the prompt response was helpful, or select thumb_down to indicate that the response was not what was expected.



An `Invalid JSON detected` error message will appear if you try to preview code containing invalid JSON. You can clean up invalid JSON using the **Autofix code** edit_fix_auto option at the bottom of the **Chart Config** pane.

**Caution:** Use caution when editing the default visualization options after making changes with the **Visualization Assistant**. Editing the default visualization options may cause unexpected behavior, including blank visualizations.

## Creating successful prompts

Writing successful prompts can take practice. Try some of the following suggestions to write prompts that successfully accomplish your goal.

### Break prompts into multiple parts

Prompts are more successful when they focus on one change at a time. For example, if you want to change both the font family and the type of visualization, it's better to make these separate prompts. Once you approve of the generated changes apply them and then begin writing the next prompt.

**Prompt** : Change the last series into a line

![The Visualization Assistant menu shows a preview of a prompt that changes one of the three series in a visualization from a column to a line.](https://docs.cloud.google.com/static/looker/docs/images/vis-assistant-line.png)

**Prompt** : Change the font to Arial and make it bold

![The Visualization Assistant menu shows a preview of a prompt that changes the font of the graph to the Arial font family, and makes text bold.](https://docs.cloud.google.com/static/looker/docs/images/vis-assistant-arial-font.png)

### Try writing a prompt multiple ways

If you're not seeing the results that you expect from your prompt, try rewording the prompt. When you apply conditional formatting, try making your prompt as unambiguous as possible. Setting specific value ranges and providing hex codes can create a more successful output. See the following examples:

**Good prompt** : Make the first series #F4B400 if it is over 350000

**Poor prompt** : Highlight the top values in yellow

![The Visualization Assistant menu shows a preview of a prompt that changes the color of the first series of values over 350,000.](https://docs.cloud.google.com/static/looker/docs/images/vis-assistant-hex.png)

If you have multiple series in a visualization, try referring to the series by name rather than by its position in the chart.

**Prompt** : Make the middle series a column

**Better prompt** : Make the users series a column

![The Visualization Assistant menu shows a preview of a prompt that changes the second of three series, called users, to a column chart](https://docs.cloud.google.com/static/looker/docs/images/vis-assistant-series-name.png)

### Use prompts as a starting point

Particularly complex customizations may require making edits directly to the JSON. Try using the **Visualization Assistant** prompts to create templates and patterns for complex customizations, and then use the **Edit Chart Config** to manually write and edit JSON formatting options. Visit the [Customizing visualizations using the Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor) documentation for more on using HighCharts JSON.

### Sample prompts

Try the following sample prompts to get ideas on how the **Visualization Assistant** can help you get started customizing your visualizations:

  * "Make this chart a column chart"
  * "Add data labels to the chart"
  * "Set the chart margin as 100px"
  * "Set the line color as Red"
  * "Set the chart background color as pink"
  * "Set the line series marker shape as triangle"



## Provide feedback

You can provide feedback for the visualization preview in the **Visualization Assistant** prompt menu. If the generated preview looks correct, click the thumb_up thumbs-up icon. If the generated preview looks incorrect or isn't what you expected, click the thumb_down thumbs-down icon.

## Related resources

  * [Learn more about Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview)
  * [Learn more about Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
