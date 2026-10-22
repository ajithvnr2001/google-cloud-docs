---
url: https://docs.cloud.google.com/data-studio/use-conditional-formatting-rules/
title: Use conditional formatting rules in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:52.681151+00:00
---

# Use conditional formatting rules in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/use-conditional-formatting-rules/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Use conditional formatting rules in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

You can set the font and background colors to be used in your charts based on the data. For example, you can highlight an entire table row font color to green if the value for a field called **Campaign** is "Summer Sale"; or you can set a scorecard chart background to red if the value for a field called **Clicks** is less than 100.

**Important:** You can apply conditional formatting rules only to [table charts](https://docs.cloud.google.com/data-studio/table-reference), [pivot table charts](https://docs.cloud.google.com/data-studio/pivot-table-reference), [scorecard charts](https://docs.cloud.google.com/data-studio/scorecard-reference), [bar charts](https://docs.cloud.google.com/data-studio/bar-reference), and [query result variables](https://docs.cloud.google.com/data-studio/query-result-variables).

## Single color conditional formatting

Single color conditional formatting lets you apply a specific font color and background color to your data. Single color conditions can include the following:

  * Dimensions
  * Metrics
  * Multiple conditions using AND/OR logic



You can use single color formatting in the following types of charts:

  * Table charts
  * Pivot table charts
  * Scorecard charts
  * Bar charts



### Use single color formatting on a table chart

To apply single color formatting to a table chart, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. Select a table chart.

  3. In the **Properties** panel, open the **STYLE** tab.

  4. In the **Conditional formatting** section, click **\+ Add formatting** to open the **Create rules** menu.

  5. In the **Color type** section, select **Single color**.

  6. In the **Format rules** section, use the **Select a field** menu to choose a field for comparison. Depending on your chart configuration, the options can include the following field types:

     * **Dimension:** Compare to a dimension value.
     * **Metric:** Compare to a metric value.
     * **Select any field:** Compare to any value in the chart (see the Select any field section on this page for more information).
  7. From the **Select a condition** menu, select a comparison condition. For example, you can choose an option like **Contains** , **Equal to** , or **Empty**.

  8. In the **Input value** field, enter a value.  
  
For metrics, you can enter a literal value or specify another metric in the chart. For example, "Summer Sale" or **Forecasted Sales**.

  9. Choose the colors in the **Color and style** section to apply when the format rules are met.

  10. Click **Save**.




### Use single color formatting on a pivot table chart

To apply single color formatting to a pivot table chart, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a pivot table chart.
  3. In the **Properties** panel, open the **STYLE** tab.
  4. In the **Conditional formatting** section, click **\+ Add formatting** to open the **Create rules** menu.
  5. In the **Color type** section, select **Single color**.
  6. In the **Format rules** section, choose one of the following comparison options: 
     * **Metric** : Compare to a metric value.
     * **Row** : Compare to a row dimension value.
     * **Column** : Compare to a column dimension value.
     * **Any** : Compare to any value in the chart (see the Select any field section on this page for more information).
  7. Select a comparison condition from the **Select a condition** menu. For example, you can choose an option like **Contains** , **Equal to** , or **Empty**.
  8. Enter a value in the **Input value** field.  
  
For metrics, you enter a literal value or specify another metric in the chart. For example, "Summer Sale" or **Forecasted Sales**.
  9. Optionally, click the **Apply when collapsed** checkbox in the **Format rules** section to apply the formatting to pivot tables that are [collapsed](https://docs.cloud.google.com/data-studio/pivot-table-reference). Conditional formatting will apply to the visible row when a collapsed value meets the applied conditions.
  10. Choose the colors in the **Color and style** section to apply when the format rules are met.
  11. Click **Save**.



### Use single color formatting on a scorecard or bar chart

You can highlight values in scorecard and bar charts based on specific conditions. To apply single color formatting to a scorecard or bar chart, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a scorecard chart.
  3. In the **Properties** panel, open the **STYLE** tab.
  4. In the **Conditional formatting** section, click **\+ Add formatting** to open the **Create rules** menu.
  5. In the **Color type** section, select **Single color**.
  6. In the **Format rules** section, the **Values** option is selected and can't be changed. The **Values** option automatically uses the current scorecard metric as the basis of the formatting rule.
  7. Choose a comparison condition from the **Select a condition** menu. For example, you can choose an option like **Contains** , **Equal to** , or **Empty**.
  8. Enter a value in the **Input value** field.
  9. Choose the colors in the **Color and style** section to apply when the format rules are met.
  10. Click **Save**.



### Select any field

The **Select any field** option in the **Format rules** section lets you define a single color format rule based on any field in the chart.

To use the **Select any field** option, click **Select any field** from the comparison options in the **Format rules** section.

## Color scale conditional formatting

Color scale conditions let you evaluate a single metric against its percentage or absolute numeric value.

You can use color scale formatting on the following types of charts:

  * Table charts and pivot table charts
  * Scorecard charts
  * Bar charts



### Use color scale formatting on a table chart or pivot table chart

To use color scale formatting on a table or pivot table chart, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a table chart or pivot table chart.
  3. In the **Properties** panel, open the **STYLE** tab.
  4. In the **Conditional formatting** section, click **\+ Add formatting** to open the **Create rules** menu.
  5. In the **Color type** section, select **Color scale**.
  6. In the **Format based on** section, choose a field in the **Select a field** menu. You can select only a single metric as the basis for a color scale.
  7. In the **Color and style** section, select a part of the chart to format. 
     1. For table charts, you can format individual fields or the entire row.
     2. For pivot table charts, you can format only one of the metrics in the chart.
  8. Select a color gradient. Click the ![Reverse](https://docs.cloud.google.com/static/data-studio/images/gmcomparearrowsgrey60048dp-2020-03-10-.png)**Reverse color scale** arrow button to change the direction of the gradient.
  9. For each data **Point** , enter a value into the **Input value** field, and click the **Background color** button to customize the background color for each data point.
  10. Click **Save**.



### Use color scale formatting on a scorecard or bar chart

To use color scale formatting o a scorecard or bar chart, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a scorecard chart.
  3. In the **Properties** panel, open the **STYLE** tab.
  4. In the **Conditional formatting** section, click **\+ Add formatting** to open the **Create rules** menu.
  5. In the **Color type** section, select **Color scale**.
  6. In the **Format rules** section, the **Values** option is selected and can't be changed. The **Values** option automatically uses the current scorecard metric as the basis of the formatting rule.
  7. In the **Color and style** section, choose a color gradient. Click the **Reverse color scale** arrow button ![Reverse](https://docs.cloud.google.com/static/data-studio/images/gmcomparearrowsgrey60048dp-2020-03-10-.png) to change the direction of the gradient.
  8. For each **Point,** enter a value into the **Input value** field and click the **Background color** button to customize the background color.
  9. Click **Save**.



## Compound format rules

Conditional formatting rules can include multiple conditions using `AND` or `OR` logic.

In the following example, a table chart will format rows that match the condition when the value for a dimension called **Source** is **EQUAL TO** to "(direct)", or when the value for a dimension called **Sessions** is **GREATER THAN** 2000.

![The Format rules section on the Create rules panel displays the conditions Source is equal to \(direct\) OR Sessions is greater than 2000.](https://docs.cloud.google.com/static/data-studio/images/conditional-formatting-or-2019-12-16.png)

In this example, a table chart will format rows that match the condition when the value for a dimension called **Source** is **EQUAL TO** "(direct)" **AND** when the value for a dimension called **Sessions** is **GREATER THAN** 2000\. Both conditions must be met to be formatted.

![The Format rules section on the Create rules panel displays the conditions Source is equal to \(direct\) AND Sessions is greater than 2000.](https://docs.cloud.google.com/static/data-studio/images/conditional-formatting-and-2019-12-16.png)

**Important:** You can have up to five **AND** clauses. Each clause can have up to five **OR** conditions. 

## Format rule order

The order in which you specify format rules can be important. Multiple rules in a chart are evaluated in sequential order, and the last set of true conditions found is the rule that is applied. For example, there are three rules in a table:

  * Rule 1 sets both a font color and a background color.
  * Rule 2 sets a font color.
  * Rule 3 sets a background color.



When all three rules are true, the font color from Rule 2 and the background color from Rule 3 are applied. Rule 1 will be ignored.

![Conditional format rules menu with three rules defined to change the text and background color when certain conditions are met.](https://docs.cloud.google.com/static/data-studio/images/conditional-formatting-rule-order-1-2019-10-25.png)

You can reorder rules by clicking the rule in the **Conditional format rules** menu and then dragging and dropping the rule into position.

When Rule 3 from the previous example is moved to the first rule position, its background color setting is carried through the rule hierarchy and is applied to the table.

![Conditional format rules menu displaying Rule 3 rearranged to the first rule position.](https://docs.cloud.google.com/static/data-studio/images/conditional-formatting-rule-2-2019-10-25.png)

## What you can format

You can apply conditional formatting to the following portions of your charts:

  * The entire row of a table
  * A specific field, or _cell_
  * Drill-down dimensions and optional metrics



### Format the entire row

The **Entire row** option applies the colors that you select to every row in the table that matches the condition.

### Format a specific field

To format a specific field in a table, select that field from the menu.

For scorecards, or for tables that use the **Select any field** format rule, this option appears as **Cells** , and it is the only option available.

![The Color and style section on the Create rules conditional formatting panel for a table chart displays field and style options.](https://docs.cloud.google.com/static/data-studio/images/conditional-formatting-1-2019-10-07.png)

### Format drill-down dimensions and optional metrics

You can apply formatting rules to drill-down dimensions and optional metrics. The formatting rules will only take effect when those fields are selected in the chart.

## How to select colors

You can use single colors or a color scale to format your charts.

### Single colors

Use the color pickers to select the font color and background color to the values specified for each condition. An example of how the colors will appear in the chart is displayed next to the color selection in the **Create rules** menu.

### Color scale

Data points determine the minimum, middle, and maximum values of your color scale. By default, a new color scale defines three data points that are based on percentages, with preset colors (red, yellow, green). You can base the scale on absolute numbers and select different colors for each data point.

You can have a maximum of five data points and a minimum of two data points.

  * To add more data points, hover your cursor over an existing data point, and click **Add** ![Add icon](https://docs.cloud.google.com/static/data-studio/images/gmaddcircleoutlinegrey60048dp-2020-03-09.png).
  * To remove a data point, hover your cursor over an existing data point, and click **Delete** ![Remove](https://docs.cloud.google.com/static/data-studio/images/gmdeletegrey60048dp-2020-03-09.png).



![The Create rules conditional formatting panel displays default formatting rules for three data points.](https://docs.cloud.google.com/static/data-studio/images/color-scale-lang-neutral-2020-03-10.png)

### Use preset colors based on your current theme

Click the down arrow on a color scale preview to choose a new preset color scale. These preset scales are based on your report theme, which lets you keep your report visually consistent. The last two color scales are optimized specifically for visually impaired users.  
![A user selects the color scale drop-down menu in the Color and style section of the Create rules panel to display preset color scale options.](https://docs.cloud.google.com/static/data-studio/images/color-scale-presets-cropped-2020-03-10.png)

### Reverse the color scale

To swap the order of the minimum and maximum colors, click the **Reverse color scale** arrow button ![Reverse](https://docs.cloud.google.com/static/data-studio/images/gmcomparearrowsgrey60048dp-2020-03-10-.png).

## Format rules, percentages, and decimal precision

When building rules that compare numbers, use the actual value in the data, rather than the value that is displayed in charts. For example, to build a format rule that selects values greater than 51.2%, use the decimal value: `Bounce rate >.512` Similarly, numbers that are displayed in your charts may be rounded up or down. Include as many digits as necessary in your rule to properly match the underlying data. For example, a rule such as `Bounce rate =.512` wouldn't apply if the actual value was.5119, even though that number appears as.512 when rounded to three decimal places. You can adjust metric decimal precision in the **STYLE** tab of the chart's **Properties** panel. 

## Edit and delete conditional formatting rules

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select the chart with the rule that you want to edit.
  3. In the **Properties** panel, open the **STYLE** tab.
  4. In the **Conditional formatting** section, click **Edit** ![Edit](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png) to open the **Conditional format rules** menu.
  5. Click **Edit** ![Edit](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png) or **Delete** ![Remove](https://docs.cloud.google.com/static/data-studio/images/gmdeletegrey60048dp-2020-03-09.png) for the rule that you want to change **.**



## Copy conditional formatting rules

There are two methods for copying conditional formatting rules.

To copy conditional formatting rules from one existing chart to another existing chart, follow these steps:

  1. Copy a chart with conditional formatting applied
  2. From the report menu toolbar, open the **Edit** menu.
  3. Click the **Paste special** option.
  4. Click the **Paste style only** option.



To create a _new_ chart with the same conditional formatting rules as an existing chart, copy and paste the existing chart.

## Limits of conditional formatting

Conditional formatting has the following limits:

  * Single color conditional formatting is available only for table charts, pivot table charts, scorecard charts, bar charts, and query result variables.
  * Color scale conditional formatting is available only for table charts, scorecard charts, bar charts, and query result variables.
  * Conditional formatting isn't available for combo charts.
  * Conditional formatting rules don't apply to subtotals or grand totals.
  * Dimension-based compound conditions in pivot table charts must use the same field in each `OR` condition.
  * Format rules can only use fields that are selected in the chart.
  * You can apply up to 20 format rules per chart.
  * Switching between chart visualization types (for example, switching from a table chart to a scorecard chart, or a pivot table chart to a table chart) may require you to update conditional formatting rules, depending on the type of chart and the fields that are used in the rule.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
