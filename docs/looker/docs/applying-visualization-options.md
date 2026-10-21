---
url: https://docs.cloud.google.com/looker/docs/applying-visualization-options/
title: Applying visualization options \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:30:38.202669+00:00
---

# Applying visualization options  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/applying-visualization-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Applying visualization options Stay organized with collections  Save and categorize content based on your preferences. 

You can apply your data visualization's settings to data deliveries in the **Format options** section of the schedule or send dialog box.

  * Select **Apply visualization options** for your data delivery to appear similar to a [table chart](https://docs.cloud.google.com/looker/docs/legacy-table-options). Any of the following settings in the [Plot](https://docs.cloud.google.com/looker/docs/legacy-table-options#plot_menu_options), [Series](https://docs.cloud.google.com/looker/docs/legacy-table-options#series_menu_options), and [Formatting](https://docs.cloud.google.com/looker/docs/legacy-table-options#formatting_menu_options) menus that are configured for the visualization will be applied:

    * [Show Row Numbers](https://docs.cloud.google.com/looker/docs/legacy-table-options#show_row_numbers)
    * [Hide Totals](https://docs.cloud.google.com/looker/docs/legacy-table-options#hide_totals)
    * [Hide Row Totals](https://docs.cloud.google.com/looker/docs/legacy-table-options#hide_row_totals)
    * [Limit Displayed Rows](https://docs.cloud.google.com/looker/docs/legacy-table-options#limit_displayed_rows) to a maximum of 500 rows shown or hidden
    * [Show Full Field Name](https://docs.cloud.google.com/looker/docs/legacy-table-options#show_full_field_name)
    * [Custom labels](https://docs.cloud.google.com/looker/docs/legacy-table-options#customizations) for each column (the **JSON — Detail, Inline** format always uses raw field names, not the field [label](https://docs.cloud.google.com/looker/docs/reference/param-field-label) — see the [Change in JSON formatting](https://discuss.google.dev/t/change-in-json-render-formatting-6-22/111501) Community post for more information about how Looker renders fields in JSON format)
    * [Conditional Formatting](https://docs.cloud.google.com/looker/docs/legacy-table-options#conditional_formatting) for deliveries of table chart visualizations in Excel format
**Note:** Conditional formatting is displayed in Excel deliveries of Looks and Explores with table chart visualizations only if the **Along a scale** rule is applied. In addition, row-level highlighting in conditional formatting is not supported for Excel exports. If your dashboard requires row-level highlighting, use the PDF or image export formats instead, as they fully support this feature.
  * Unselect **Apply visualization options** for Looker to send the data as it appears in the **Data** section of the Look or a dashboard tile's **Explore from Here** window. **JSON — Label** uses the field [label](https://docs.cloud.google.com/looker/docs/reference/param-field-label), even if **Apply visualization options** is unselected.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-12 UTC."],[],[]] 
