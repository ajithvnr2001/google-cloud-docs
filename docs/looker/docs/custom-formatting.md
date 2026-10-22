---
url: https://docs.cloud.google.com/looker/docs/custom-formatting/
title: Adding custom formatting to fields \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:16.033096+00:00
---

# Adding custom formatting to fields  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/custom-formatting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Adding custom formatting to fields Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/retrieve-and-chart-data) learning series.

> For Looker developers: The formatting shown on this page is the same as formatting used with the [`value_format` LookML parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format), except that the `value_format` parameter requires the formatting string to be enclosed in double quotes.

Custom formatting gives you greater control over how numeric data appears in a Looker result set. With custom formatting, you can apply Excel-style formatting options to numeric data shown in [visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations), or produced by [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) or [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations).

**Caution:** Custom formatting is supported only for [dimensions of `type: number`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#number) or [measures of `type: number`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number). Users who do not have `develop` permissions can view a field's data type by selecting the [**Info** icon](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#info_icon) next to a field's name in the Explore [field picker](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#field-specific_information_and_actions).

## Using custom formatting in visualizations

For visualizations with a **Values** tab in the gear menu:

![](https://docs.cloud.google.com/static/looker/docs/images/explore-value-format-2310.png)

  1. Select the **Edit** menu on the **Visualization** bar.
  2. Select the **Values** tab.
  3. In the **Value Format** field, enter the custom formatting string.



For example, to add custom formatting for a [table visualization](https://docs.cloud.google.com/looker/docs/table-options):

![](https://docs.cloud.google.com/static/looker/docs/images/explore-table-next-format-2310.png)

  1. Select the **Edit** menu on the **Visualization** bar.
  2. Select the **Series** tab.
  3. In the **Customizations** section, select the **Format** drop-down and choose **Custom...**.



A new blank field appears when you select **Custom...**. Enter the custom formatting string in the blank field.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-table-next-format-custom-2308.png)

## Using custom formatting with table calculations and custom fields

When you create or edit a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations#creating-table-calculations) or [custom field](https://docs.cloud.google.com/looker/docs/custom-fields), select the **Custom** option in the **Format** drop-down and enter the custom format in the blank field.

## Custom formatting examples

You can reference Excel's complete guide to specifying these formats [on their Number format codes documentation page](https://support.office.com/en-us/article/number-format-codes-5026bbd6-04bc-48cd-bf33-80f18b4eae68), or you can use a third-party tool to build a custom format, such as [Custom Formats Builder](https://customformats.com/).

**Warning:** Date formatting, color formatting, and hexadecimal conversion are not supported in Looker.

Some of the most common formatting options are listed in the following table. A format code that uses `0` requires that non-significant zeros be displayed if the number contains fewer digits than specified in the code. A format code that uses `#` displays only the significant digits, even if there are fewer digits than specified in the code.

Some special characters, such as international currency symbols, must be treated as strings and enclosed in double quotes.

**Caution:** Excel-style formatting does not support many international number formats, such as 1.234,56 or 1 234,56. Looker does support several international formats through the localization function. For information about localizing number formats, see the [Localizing number formatting](https://docs.cloud.google.com/looker/docs/localizing-number-formatting) documentation page.Format| Result  
---|---  
`0`| Integer (123)  
`00#`| Integer zero-padded to 3 places (001)  
`0 "String"`| Integer followed by a string (123 String)("String" can be replaced with any text string)  
`0.##`| Number up to 2 decimals (1. or 1.2 or 1.23)  
`0.00`| Number with exactly 2 decimals (1.23)  
`00#.00`| Number zero-padded to 3 places and exactly 2 decimals (001.23)  
`#,##0`| Number with comma between thousands (1,234)  
`#,##0.00`| Number with comma between thousands and 2 decimals (1,234.00)  
`0.000,, "M"`| Number in millions with 3 decimals (1.234 M)Division by 1 million happens automatically  
`0.000, "K"`| Number in thousands with 3 decimals (1.234 K)Division by 1 thousand happens automatically  
`$0`| Dollars with 0 decimals ($123)  
`$0.00`| Dollars with 2 decimals ($123.00)  
`"€"0`| Euros with 0 decimals (€123)  
`$#,##0.00`| Dollars with comma between thousands and 2 decimals ($1,234.00)  
`$#.00;($#.00)`| Dollars with 2 decimals, positive values displayed normally, negative values wrapped in parentheses  
`0\%`| Display as percent with 0 decimals (1 becomes 1%)  
`0.00\%`| Display as percent with 2 decimals (1 becomes 1.00%)  
`0%`| Convert to percent with 0 decimals (.01 becomes 1%)  
`0.00%`| Convert to percent with 2 decimals (.01 becomes 1.00%)  
  
### Custom thousands separators and conditional formatting

Looker uses Excel-style formatting rules. Although Looker recognizes a comma as a thousands separator, it treats other characters, such as apostrophes that are used for the Swiss franc (CHF), as literal characters.

If you use an apostrophe directly as a thousands separator (for example, `"CHF "#'##0.00`), the formatting engine treats the apostrophe as a literal character and forces it into the output string even for values under 1,000 (such as `CHF '20.00` instead of `CHF 20.00`).

To apply a custom thousands separator exclusively to numbers 1,000 and greater, use conditional formatting within your format string. You can specify different formatting rules for numbers greater than or equal to 1,000 versus numbers less than 1,000, separated by a semicolon:
    
    
    [>=1000]"CHF "#'##0.00;[<1000]"CHF "0.00
    

For Looker developers using the [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) parameter in LookML, enclose the format string in double quotes and escape the inner double quotes:
    
    
    value_format: "[>=1000]\"CHF \"#'##0.00;[<1000]\"CHF \"0.00"
    

## Time formatting for charts

If your chart has a time dimension on the x-axis, you can change the formatting of the x-axis label by using the **Time Label Format** setting in the **X** tab of the visualization options. You can format time values by using the syntax on the [Time formatting for charts](https://docs.cloud.google.com/looker/docs/time-formatting-for-charts) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
