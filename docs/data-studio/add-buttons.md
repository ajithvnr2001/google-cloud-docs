---
url: https://docs.cloud.google.com/data-studio/add-buttons/
title: Add buttons \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:06:34.450721+00:00
---

# Add buttons  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-buttons/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add buttons Stay organized with collections  Save and categorize content based on your preferences. 

You can add buttons to your Data Studio reports to let users filter data, access report actions, and navigate to linked content in a streamlined and convenient way. For example, you can let users filter a table with **Country** and **Population** by preset country values or navigate to a related page, and you can also provide them with quick ways to download or share a report.

**Important:** When users click an external link, Data Studio displays a redirect notice.

![Report with filter buttons for a table with Country and Population fields, and buttons linking to a main report and for downloading and sharing the report.](https://docs.cloud.google.com/static/data-studio/images/buttons-example.png)

## Add buttons to a report

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select the **Button** option from the **Add a control** drop-down menu.
  3. Label your button by typing in the button field.
  4. Rearrange your button to position it in the desired location on your report.



Next, customize the button using the **Setup** and **Style** options in the **Properties** menu.

## Button setup options

The options in a button's **Setup** panel determine how a button is configured.

### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the button's data source, select the current data source name.
  * To view or edit the data source, select the **Edit data source** pencil icon ![Edit](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png). You must have at least view permissions to see this icon.



This option applies to the **Filter** action type.

### Button action type

These options control the ways a dashboard user can interact with a report using buttons. Each option has additional configuration options.

There are several types of button actions:

  * Navigation
  * Report actions
  * Filter



#### Navigation

The **Navigation** option lets dashboard editors create a button for users to quickly navigate to [internal or external linked content](https://docs.cloud.google.com/data-studio/link-to-a-page).

**Important:** When users click an external link, Data Studio displays a redirect notice.**Note:** This feature is being released gradually. You might not see it right away.

There are two types of navigation you can choose from:

  * Static link — A preset link that users can select to navigate to a specific page.
  * Dynamic link — A link that users can select that changes based on the dimension value that they select when [cross-filtering is enabled](https://docs.cloud.google.com/data-studio/chart-cross-filtering) on a chart.

**Warning:** [Cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering) must be enabled for a chart for **Dynamic** navigation buttons to function as expected. If cross-filtering is not enabled, dynamic link navigation uses the value of the first row of the dataset by default.

To add a **Static** link navigation button to your report, follow these steps:

  1. Select the **Navigation** option.
  2. Select the **Static link** option from the **Button link URL** drop-down menu.
  3. Select the **Insert link** button in the **Button link URL** section to open the **Insert link** menu.
  4. Input the URL.
  5. Select or deselect the **Open link in new tab** option, as desired.
  6. Select **Apply** to save the navigation options or **Cancel** to close the pop-up menu without saving.



To add a **Dynamic** link navigation button to your report, follow these steps:

  1. Select the **Navigation** option.

  2. Select the **Dynamic link (from dimension)** option from the **Button link URL** drop-down menu.

  3. Select **Add a new dimension** in the **Button Link URL** section to choose a dimension that includes URL values.

     * Alternatively, select **ADD FIELD** to open the calculated field menu and [create an expression](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields) that concatenates dimension values to a URL.

For example, to create a dynamic link that performs a Google Search for a value from a dimension called **Country** , you can use the following expression:

`concat("http://www.google.com/search?q=",Country)`

When a user selects a **Country** value in a chart, the button link will change to include that value.

  4. If you select **ADD FIELD** to create a dynamic URL, select the **URL** option from the **Data** **Type** drop-down menu, and then click **Apply** in the calculated field menu.

  5. Select or deselect the **Open link in new tab** option, as desired.




#### Report actions

The **Report actions** option lets dashboard editors create a button for users to quickly access report actions such as sharing and downloading.

To add a **Report action** button to a report, follow these steps:

  1. Select the **Report actions** option.
  2. Choose one of the following options from the **Choose a report action for the button** drop-down menu: 
     1. **Invite people** — Lets users quickly [invite other users](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports) to view or collaborate on a report.
     2. **Get report link** — Lets users quickly [access a URL](https://docs.cloud.google.com/data-studio/get-a-link-to-your-report) for sharing a report with others or for using a report in web pages.
     3. **Download report** — Lets users quickly [download a report as a PDF](https://docs.cloud.google.com/data-studio/download-a-report-as-pdf).
     4. **Reset filters** — Lets users quickly reset [filters](https://docs.cloud.google.com/data-studio/about-filter-properties) on a report.
     5. **Refresh data** — Lets users [refresh data](https://docs.cloud.google.com/data-studio/manage-data-freshness#refresh-report-data-manually) in the report. By default, this action refreshes all data sources in the report. To refresh only specific components, [group the button](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components#group_ungroup) with those components.



#### Filter

The **Filter** option lets dashboard editors create preset filters for dashboard viewers to quickly and conveniently apply complex filter logic to charts and reports.

See the [Preset filter control page](https://docs.cloud.google.com/data-studio/preset-filter-control) to learn more about configuring preset filter controls.

## Button style options

A button's **Style** properties control its overall presentation and appearance.

### Button font options

These options control the appearance of button font styling.

  * **Font color:** Specifies the color of button text from a color palette pop-up. 
  * **Font size:** Specifies the size of button text in pixels from a series of drop-down menu options. 
  * **Font family:** Specifies the font family of button text from a series of drop-down menu options. 



### Background and border options

These options control the appearance of the button background container.

  * **Background:** Sets the button background color. 
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. Border radius of 100° produces a circular shape. 
  * **Opacity:** Sets the button's opacity. 100% opacity completely hides objects behind the button. 60% is the lowest opacity setting. 
  * **Border color:** Sets the button border color. 
  * **Border weight:** Sets the button border line thickness. 
  * **Border style:** Sets the button border line style. 
  * **Add border shadow:** Adds a shadow to the button's lower and right borders. 



## Related resources

  * Use [report theme](https://docs.cloud.google.com/data-studio/themes) and [layout](https://docs.cloud.google.com/data-studio/report-and-page-layout) settings to adjust the appearance of the page navigation.
  * [Preset filter control](https://docs.cloud.google.com/data-studio/preset-filter-control)
  * [Download a Data Studio report as PDF](https://docs.cloud.google.com/data-studio/download-a-report-as-pdf)
  * [Invite others to your reports](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports)
  * [Get a link to your report](https://docs.cloud.google.com/data-studio/get-a-link-to-your-report)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
