---
url: https://docs.cloud.google.com/data-studio/add-slides-gemini/
title: Add Data Studio content to your Google Slides presentation using Gemini assistance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:17.230664+00:00
---

# Add Data Studio content to your Google Slides presentation using Gemini assistance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-slides-gemini/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add Data Studio content to your Google Slides presentation using Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** While in preview, Gemini in Data Studio features are available at no additional cost. At the end of this Preview period, usage of Gemini in Data Studio features may require an additional fee.

This documentation page describes how to use [Gemini in Data Studio](https://docs.cloud.google.com/data-studio/gemini-overview) to help you generate Google Slides presentations from your Data Studio reports. Data Studio inserts the report charts as images, generates a textual summary of each chart, and inserts the summaries as text elements.

Gemini in Data Studio is a product in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This page is intended for users who are working with reports in Data Studio.

## Before you begin

To use this Gemini in Data Studio feature, the following requirements must be fulfilled:

  * You must be a user under a [Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/pro-subscription-overview). Data Studio Pro licenses are [available at no cost](https://docs.cloud.google.com/looker/docs/admin-panel-platform-lsp) to Looker users.
  * Gemini in Data Studio must be [enabled](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio) for your Data Studio project.
  * The [Gemini for Google Cloud API](https://console.cloud.google.com/marketplace/product/google/cloudaicompanion.googleapis.com) must be enabled in your Google Cloud project.
  * You must be a viewer or an editor of the Data Studio report that you want to generate Google Slides from.
  * If you are a viewer of the Data Studio report, the **Disable viewers from generating Google Slides with Gemini in Data Studio** [sharing option](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports) must not be selected.
  * You must be an [editor of the Google Slides presentation](https://support.google.com/docs/answer/2494822) that you want to import content into.
  * If you want to add Data Studio content to an existing Google Slides presentation, you must install the Data Studio [add-on for Google Workspace](https://workspace.google.com/marketplace/app/looker_studio/771955699012).



## Generate a Google Slides presentation from all visualizations in a Data Studio report

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To create a Google Slides presentation that includes all the visualizations in a Data Studio report, follow these steps:

  1. Open a Data Studio report in either view mode or edit mode.
  2. In the panel manager, select the **Gemini** panel.
  3. Select **Generate Slides**.
  4. Select **All visualizations**.
  5. Data Studio generates a Google Slides presentation and saves it to your Google Drive. The presentation contains the following slides: 
     * A title slide with the title of the Data Studio report, your name, the date that the presentation was generated, and a link to the Data Studio report
     * One slide for every chart including the chart title, if available, and a textual summary of the chart
     * A closing slide



After you generate a presentation using this method, you won't be able to edit it in Data Studio. To view or edit the presentation, click the link in the **Gemini** panel. To finish, click **Done** or close the **Gemini** panel.

## Generate a Google Slides presentation from selected visualizations in a Data Studio report

To create a Google Slides presentation that includes a subset of visualizations from a Data Studio report, follow these steps:

  1. Open a Data Studio report in either view mode or edit mode.
  2. In the panel manager, select the **Gemini** panel.
  3. Select **Generate Slides**.
  4. Select **Let me choose**.
  5. Click the component(s) that you want to add to the presentation. 
     * To select multiple components, either Shift-click each component, or drag a selection area over the canvas.
     * Charts, titles, and filters are all separate components. You may want to add each of them to the slide. However, Gemini in Data Studio only generates text summaries for visualizations.
  6. Select whether to add this set of components to a new slide or to the current slide.
  7. Click **Done** in the top banner.
  8. Data Studio adds the selected component(s) to the **Gemini** panel. 
     * To disable the textual summary for a visualization, click the **Summary on** icon on the slide.
     * To remove a visualization from the **Gemini** panel, click the **Delete** icon on the slide.
  9. To add more components, repeat steps 5 through 8.

**Important:** Data Studio deletes slide previews after 24 hours, or if you close the **Gemini** panel. To save your work, make sure to finish generating the presentation.
  10. Once you're finished adding components, select **Generate Slides** in the **Gemini** panel.

  11. Data Studio generates a Google Slides presentation and saves it to your Google Drive. The presentation contains the following slides:

     * A title slide with the title of the Data Studio report, your name, the date that the presentation was generated, and a link to the Data Studio report
     * The slides that you created in steps 5 through 10
     * A closing slide



After you generate a presentation using this method, you won't be able to further edit it in Data Studio. To view or edit the presentation, click the link in the **Gemini** panel. To finish, click **Done** or close the **Gemini** panel.

## Add Data Studio content to a Google Slides presentation

To add Data Studio content to an existing Google Slides presentation, follow these steps:

  1. Install the [Data Studio add-on for Google Workspace](https://workspace.google.com/marketplace/app/looker_studio/771955699012).

     * This add-on will work only if you are a Data Studio Pro user and if Gemini in Data Studio is enabled for your Data Studio project.
  2. In a Google Slides presentation, click the **Data Studio** icon on the right-hand toolbar to open the **Data Studio** panel.

  3. Click **Import**. Data Studio opens in a new browser tab.

  4. In Data Studio, select a report to import visualizations from.

  5. Click the component(s) that you want to add to the presentation.

     * To select multiple components, either Shift-click each component, or drag a selection area over the canvas.
     * Charts, titles, and filters are all separate components. You may want to add each of them to the slide. However, Gemini in Data Studio only generates text summaries for visualizations.
  6. Click **Done**. Data Studio adds the selected component(s) to the **Gemini** panel.

     * To disable the textual summary for a visualization, click the **Summary on** icon on the slide.
     * To remove a visualization from the **Gemini** panel, click the **Delete** icon on the slide.
  7. To add more components, repeat steps 4-5.

  8. To add all the previewed slides to your presentation, click **Add to Slides**. The Data Studio browser tab is closed, and you will be returned to the Google Slides browser tab. The components that you selected will appear in the **Data Studio** panel.

  9. To add a slide preview to your presentation, click **Insert** under the slide preview.

**Important:** Data Studio deletes slide previews after 24 hours, or if you close the **Gemini** panel. To save your work, make sure to finish generating the presentation.
  10. Data Studio inserts the components into your presentation as images. Data Studio then generates a text summary of each visualization and inserts the summaries into your presentation.




When you're finished adding components, click **Done** in the **Data Studio** panel.

## Update Data Studio data in a Google Slides presentation

To update Data Studio data in an existing Google Slides presentation, follow these steps:

  1. In a Google Slides presentation, click the **Data Studio** icon on the right-hand toolbar to open the **Data Studio** panel.
  2. Select the components that you want to update data for.
  3. Click the **Update** icon. Data Studio will refresh each of the selected components with updated data.



When you're finished, close the **Data Studio** panel.

## Troubleshooting and limitations

The following limitations apply when adding Data Studio content to Google Slides presentations:

  * Summaries won't be generated for non-visualization report components, such as filters, controls, or text boxes.
  * Summaries won't be generated for visualizations with fewer than three data rows, such as single-value visualizations.
  * Summaries won't be generated for visualizations that are based on [blends](https://docs.cloud.google.com/data-studio/how-blends-work).
  * Google Slides generation may time out if the Data Studio report has more than 75 visualizations.
  * Google Slides generation is not supported in [Looker reports](https://docs.cloud.google.com/looker/docs/report-feature-availability).



If you encounter issues when adding Data Studio content to Google Slides presentations, refer to the following table for potential solutions.

Error message  |  Possible cause  |  Possible solution   
---|---|---  
Connection to the data source was lost.  |  Data Studio could not connect to your data source.  |  Try generating the presentation again.   
Connection to the data source was lost / Some summaries could not be generated as the data source connection was temporarily lost.  |  The `cloudaicompanion.googleapis.com` API on your Google Cloud project associated with your Data Studio Pro subscription might be disabled.  |  To fix this, administrators must enable the Gemini for Google Cloud API in their Google Cloud project. Go to the Google Cloud console API Library and enable the API here: `https://console.developers.google.com/apis/api/cloudaicompanion.googleapis.com/overview?project=<YOUR_PROJECT_ID>`.   
Not enough rows to generate summary.  |  Data Studio requires at least four rows of data to generate a summary.  |  Add more rows to the visualization.   
Blended data sources aren't supported.  |  Data Studio doesn't support generating summaries from visualizations that are based on blended data sources.  |  Try using a data source that is not blended.   
Slides generation failed due to an error.  |  Data Studio encountered an unspecified error.  |  Wait for a few minutes and then try generating the presentation again.   
Slides generation timed out.  |  Summary generation may time out for reports with more than 75 visualizations.  |  Try removing some visualizations from the report.   
Slides generation timed out due to server error.  |  Data Studio may be overloaded with requests.  |  Wait for a few minutes and then try generating the presentation again.   
  
## Provide feedback

You can provide feedback for the generated presentation in the **Gemini** panel of Data Studio. If the generated presentation looks correct, click the thumb_up thumbs-up icon. If the generated presentation looks incorrect or isn't what you expected, click the thumb_down thumbs-down icon. If you downvote the results, Data Studio will prompt you for a category for your feedback. You can then opt to provide more detailed feedback, capture a screenshot, and collect the generated chart summary data.

**Note:** Gemini in Data Studio features are in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [data-studio-ca AT google.com](mailto:data-studio-ca@google.com) and include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



## Related resources

  * [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview)
  * [Gemini in Data Studio overview](https://docs.cloud.google.com/data-studio/gemini-overview)
  * [Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
