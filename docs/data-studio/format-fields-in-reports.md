---
url: https://docs.cloud.google.com/data-studio/format-fields-in-reports/
title: Format fields in reports \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:18.929900+00:00
---

# Format fields in reports  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/format-fields-in-reports/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Format fields in reports Stay organized with collections  Save and categorize content based on your preferences. 

Custom value formatting lets you specify how dimension, metric, and calculated field values appear in charts.

**Important:** Data Studio does not support conditional expressions in custom value formatting.

Custom value formatting can be helpful in these use cases:

  * You want to quickly change how dates and number values are displayed in charts and tooltips.
  * You need to display values in a specific way that won't be satisfied by changing the [data type](https://docs.cloud.google.com/data-studio/data-types).
  * You want to provide additional context to report viewers about values in charts and tooltips.



For example, you can choose to display large values as exponents and append text to the values. The following column chart displays **Population** grouped by **Country.** You can use custom formatting to display the large values as exponents with the text "People" appended to provide additional context to report viewers.

![The tooltip for the bar that represents the population of China displays the label China, and the text Population: 1.33E10 People.](https://docs.cloud.google.com/static/data-studio/images/looker-studio-custom-value-format-example.png)

This page provides an overview of custom value formatting. It includes the following sections:

  * Requirements
  * Add or edit chart-specific custom value formatting
  * Things to know about custom value formatting
  * Related resources

**Important:** Custom formatting is chart-specific, and cannot be applied to field values across an entire report. 

## Requirements

If you want to use custom value formatting for charts, these requirements must be met:

  * The [Field Editing in Reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) setting must be enabled in the data source.
  * You must have edit rights to a report.
  * A dimension, metric, or calculated field must be a **Numeric** or **Date & Time** [data type](https://docs.cloud.google.com/data-studio/data-types).



## Add or edit chart-specific custom value formatting

You can apply custom value formatting to dimensions, metrics, or calculated fields.

### Add or edit chart-specific custom value formatting for dimensions and metrics

To add value formatting to dimension or metric values on a chart, follow these steps:

  1. Create or [edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. [Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart.

  3. In the **Setup** tab of the **Properties** panel, click a field's data type icon to open the field's edit menu.

  4. Choose a value format option in the **Display Format** drop-down menu. If you'd like to specify a custom format, choose **Custom value format** to open the **Custom number format** menu.

  5. Enter a custom value format. You can select a predefined format option or build your own using the options that are shown in the **Custom date format** or **Custom number format** dialog.

**Important:** Data Studio does not support conditional expressions in custom value formatting.

A preview of the value format will be displayed under the **Custom number format** text field.

  6. Once you have selected or entered the custom format, click **Apply**.

  7. Click outside of the field's edit menu and return to the chart **Setup** properties.




Repeat steps 3-7 to edit a field's custom value formatting.

### Add or edit chart-specific custom value formatting for calculated fields

To add custom value formatting to calculated field values on a chart, follow these steps:

  1. Create or [edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. [Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart.

  3. In the **Setup** tab of the **Properties** panel, [create a calculated field](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields). Alternatively, edit an existing calculated field by hovering over the calculated field name and clicking field's data type icon.

If you create a new dimension type calculated field, click **Apply** after you enter the desired expression. The calculated field editor will not detect the field type until you click **Apply,**

  4. Choose a value format option in the **Display Format** drop-down menu. If you'd like to specify a custom format, choose **Custom value format** to open the **Custom number format** menu.

  5. Enter a custom value format. You can select a predefined format option or build your own using the options tht are shown in the **Custom date format** or **Custom number format** dialog.

A preview of the value format will display under the **Custom number format** text field.

  6. Once you have selected or entered the custom format, click **Apply**.

  7. Click outside of the calculated field's edit menu and return to the chart **Setup** properties.




Repeat steps 3-7 to edit a calculated field's custom value formatting.

## Custom date format strings

The following table lists common syntax characters that you can use to create a custom date or date and time format.

**Note:** Syntax characters are case-sensitive. For example, `m` represents minutes, while `M` represents the month.Format String | Description | Example (for Tuesday, April 8, 2025 15:05:09)  
---|---|---  
**Day**  
`d` | Day of the month, without a leading zero. | 8  
`dd` | Day of the month, with a leading zero. | 08  
`E` | Day of the week, three-letter abbreviation. | Tue  
`EEEE` | Day of the week, full name. | Tuesday  
**Month**  
`M` | Month of the year, without a leading zero.  | 4  
`MM` | Month of the year, with a leading zero. | 04  
`MMM` | Three-letter month abbreviation. | Apr  
`MMMM` | Full month name. | April  
`MMMMM` | First letter of the month. | A  
**Year**  
`y`, `yyy`, or `yyyy` | 4-digit year. | 2025  
`yy` | 2-digit year. | 25  
**Time Formats**  
`h` | Hour (1-12), without a leading zero. | 3  
`hh` | Hour (1-12), with a leading zero. | 03  
`H` | Hour (0-23). | 15  
`m` | Minute, without a leading zero. | 5  
`mm` | Minute, with a leading zero. | 05  
`s` | Second, without a leading zero. | 9  
`ss` | Second, with a leading zero. | 09  
`a` | AM/PM marker. | PM  
`z` | Time zone. Data Studio reports use only the UTC timezone. | UTC  
  
### Example date formats

The following table provides examples of combined custom date formats:

Format String | Description | Example Output  
---|---|---  
`yyyy-MM-dd` | ISO Date format. | 2025-04-08  
`MM/dd/yyyy` | Common US date format. | 04/08/2025  
`d MMMM yy` | Day, full month name, 2-digit year. | 8 April 25  
`E, MMM dd, yyyy` | Abbreviated day name, month, day number, year. | Tue, Apr 08, 2025  
`EEEE, MMMM d, y, h:mm:ss a` | Full day name, full month name, day number, year, full time with AM/PM marker. | Tuesday, April 8, 2025, 3:05:09 PM  
  
## Custom number format strings

The following table lists common syntax characters that you can use to create a custom number format:

Character | Description | Example (for input 12345.670)   
---|---|---  
0 | A digit in the number. An insignificant 0 will appear in the results.  
# | A digit in the number. An insignificant 0 will not appear in the results.  
. |  Period. Formats numbers with a decimal separator. The [Data Studio locale](https://docs.cloud.google.com/data-studio/change-user-interface-language) determines which character is used as the decimal separator for all numeric values.  
, | Comma. Formats numbers with a thousands separator. The [Data Studio locale](https://docs.cloud.google.com/data-studio/change-user-interface-language) determines which character is used as the thousands separator for all numeric values.  
; | Semicolon. Separates formats for positive and negative numbers.  
% | Formats numbers as percentages.  
E | Formats numbers as exponents.  
'text' | Adds text before or after the number. Enter the text that you want to appear, with or without quotation marks.  
  
### Example number formats

The following table provides examples of custom number formats:

Example Input | Format String | Example Output  
---|---|---  
1235 | `#,##0` | 1,235  
1234.57 | `#,##0.00` | 1,234.57  
123 | `#,##0'%'` | 123%  
123.46 | `#,##0.00'%'` | 123.46%  
1234.57 | `0.##E0` | 1.23E3  
-1234 | `#,##0;(#,##0)` | (1,234)  
-1234.57 | `#,##0.00;(#,##0.00)` | (1,234.57)  
  
## Things to know about custom value formatting

  * Custom formatting that is applied to chart values will be disabled when the **Compact numbers** setting is enabled. The **Compact numbers** setting is available when the **Show data labels** option is enabled on the **Style** tab of a chart's **Properties** panel.

Similarly, the **Compact numbers** setting will be disabled if custom formatting is applied to chart values.

  * Chart-specific value formatting will only exist in the chart in which it is applied. You can't directly reuse chart-specific value formatting.

However, you can copy a chart that uses custom value formatting. The copy will contain any custom value formatting defined in the original.

  * Data Studio does not support conditional expressions in custom value formatting.




## Related resources

  * [Data types](https://docs.cloud.google.com/data-studio/data-types)
  * [Edit fields](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports)
  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Add, edit, and troubleshoot calculated fields](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
