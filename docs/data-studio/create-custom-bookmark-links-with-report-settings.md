---
url: https://docs.cloud.google.com/data-studio/create-custom-bookmark-links-with-report-settings/
title: Create custom bookmark links with report settings \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:22:01.305162+00:00
---

# Create custom bookmark links with report settings  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-custom-bookmark-links-with-report-settings/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create custom bookmark links with report settings Stay organized with collections  Save and categorize content based on your preferences. 

You can configure a report to include the viewer's filter settings in the URL of the report. This lets your viewers bookmark the current settings for future use. You can also use these links to set default values for multi-select filters.

## How custom bookmark links work

The [filter control](https://docs.cloud.google.com/data-studio/about-controls) lets viewers refine the data displayed in a report. By default, any changes made by the viewer are preserved, so if they reload the report, the original filter settings are restored.

When you enable custom bookmark links for a report, the viewer's filter settings are added as parameters to the report's URL. This gives your viewers an easy way to get back to their preferred view of the data by bookmarking the link.

### Enable custom bookmark links

To enable custom bookmark links for a report:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  3. Select **File > Report Settings**.
  4. Under _Custom Bookmark Links_ , click **Enable viewer settings in report link**.



## How to use custom bookmark links

Here are some ways you can use custom bookmark links.

### Create a customized report bookmark

When custom bookmark links are enabled for a report, viewers can create and save personalized views of the data. For example, if Chen is interested in seeing performance metrics for China, while François prefers to see the data for France, each can use the same report containing a country filter to display their respective geographies, then create a browser bookmark and use it to get back to the report with those settings applied.

You can also preconfigure reports for your viewers and send them custom bookmarks via email.

### Set default values for multi-select filters

While you can set default values for single select filters in the report editor, you can't do the same for multi-select filters. However, you can use custom bookmarks to accomplish this:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. Add or edit a multi-select filter control.

> Multi-select filters are the default. They have the **Single Select** option **unchecked** in their _STYLE_ properties panel.

  3. View the report.

  4. Use the filter control to select the default values you want.

  5. Create a bookmark for the current page.

  6. Share the bookmark via email or create a link inside your report using the bookmark URL.




## Limits of custom bookmark links

  * Custom bookmark links are only available in View Mode.
  * Browsers typically support URLs up to 2K characters in length. If a custom bookmark link is longer than your browser can support, all of the configuration parameters in the bookmark will be discarded, and you'll see the default settings for that report.
  * Don't use custom bookmark links to restrict access to your data. Viewers can easily override the URL parameters by editing them in the browser's URL bar. If you want to restrict viewers to seeing only certain data, use [filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties) instead.

**Important:** Adding or removing controls on a report changes the configuration parameters in the URL. If you add or remove filter controls in a report, you should update your bookmark to include the new URL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
