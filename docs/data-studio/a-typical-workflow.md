---
url: https://docs.cloud.google.com/data-studio/a-typical-workflow/
title: A typical Data Studio workflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:04.065609+00:00
---

# A typical Data Studio workflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/a-typical-workflow/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  A typical Data Studio workflow Stay organized with collections  Save and categorize content based on your preferences. 

You can follow an end-to-end workflow in Data Studio to transform raw data into interactive visual reports. By connecting to data sources, building visualizations, and refining data models, you convert complex information into actionable insights. You can then share these dynamic reports across your organization to support data-driven decisions.

A typical workflow covers six core stages:

  * **Create** a report
  * **Connect** to your data
  * **Visualize** the data
  * **Transform** the data
  * **Share** your insights
  * **Update** and refine the report



## Scenario

![Avatar for a Data Studio Data Analyst.](https://docs.cloud.google.com/static/data-studio/images/persona-analyst-2022-07-08.png) Aqsa is a data analyst for a travel company. She wants to explore and visualize data on flight arrival and departure delays in order to see if there are valuable insights her company can provide to their customers to improve their travel experience. The data is stored in BigQuery.

## Create

Aqsa signs into Data Studio, then clicks **Create > Report**. The Data Studio report editor opens and the **Add data** panel appears.

![A user selects the + Create button on the Data Studio home page left navigation panel to create new content in Data Studio.](https://docs.cloud.google.com/static/data-studio/images/how-to-use-ds-create-report-new-ui.png)>

## Connect

The **Add data** panel lets Aqsa create a new [data source](https://docs.cloud.google.com/data-studio/data-source) or select an existing one. She doesn't yet have a data source for the flight data she wants to visualize, so she clicks the BigQuery [connector](https://docs.cloud.google.com/data-studio/connector) to create a new data source.

![](https://docs.cloud.google.com/static/data-studio/images/select-bq-connector-2022-07-07.png)

Aqsa enters the information needed to connect to the BigQuery table containing the flight data, and then adds the new data source to her report.

![A user selects the Add button on the Add data to report panel to finish adding the new data source to the report.](https://docs.cloud.google.com/static/data-studio/images/configure-bq-connection-2022-07-07.png)

The **Add data** panel closes and a table appears on the editor canvas, with the airline carrier field and the record count for each unique carrier.

![A user selects a table visualization on a report canvas to open the Data and Chart option menus.](https://docs.cloud.google.com/static/data-studio/images/new-report-editor-2022-07-07.png)

## Visualize

Aqsa adds more fields to the table by dragging them from the properties panel to the table. She adds an **Arrival Delay** metric, which contains the number of minutes each flight was delayed past its scheduled arrival time.

Aqsa knows that tables are great for seeing the details in data, but she wants to get a higher level overview, so she adds a horizontal bar chart and a pie chart to the report. Now she can immediately see which airlines had the most delays of their arriving flights and their relationship to the other airlines' performances.

## Transform

![A list of the Metric fields on a chart Setup tab displays that the ArrDelay metric aggregation type is set to Sum.](https://docs.cloud.google.com/static/data-studio/images/metric-sum-2022-07-07.png) Aqsa notices that the arrival delay field is summing the data but it should instead be averaging it. She could fix this by changing the aggregation for the field as it appears in each chart, but it's more efficient to edit the data source.

When you want to modify a field that appears in a report, you have the following options:

  * **Modify the field In a chart**. When you do this, you're just changing that specific instance of the field. The change only applies to the field in that chart. Other charts that use the field will have the field's default configuration, as set in the data source.

  * **Modify the field In the data source**. When you do this, the change will appear the next time you use that field. For example, new charts you create will use the changed field, as will existing chart to which you add another instance of the field. Components that used the field before you made the change won't be affected.




![](https://docs.cloud.google.com/static/data-studio/images/edit-faa-data-source-2022-07-07-image-rge.png)

To edit the data source, at the top of the properties panel, Aqsa clicks the pencil next to the data source name. She locates the `ArrDelay` field and changes its **Default aggregation** to **Average**. Aqsa clicks **DONE** to save her change and return to the report editor.

Now when anyone with access to edit the report uses this field, it will have the selected aggregation by default.

![A user selects Average from the Default Aggregation drop-down menu for the ArrDelay field on the Edit Connection panel Dimensions list.](https://docs.cloud.google.com/static/data-studio/images/change-agg-2022-07-07.png)

## Share and collaborate

![Avatar for a Data Studio Designer.](https://docs.cloud.google.com/static/data-studio/images/persona-developer-2022-07-08.png) Aqsa asks her colleague Lauren to help apply their design skills to the report. Aqsa shares the report with Lauren's email address, giving them **Can edit** permission. Lauren sets to work, adding text and images, and crafting the report appearance to match their company's style guidelines. Lauren suggests they add a page that provides more context by embedding the current marketing plan, which is stored as a Google Doc. Together, Aqsa and Lauren create an attractive, compelling report that highlights the insights they've found in the flight data.

![](https://docs.cloud.google.com/static/data-studio/images/sample-report-2022-07-08.png)

When the report is finished, Asqa shares it with the senior management team's group email address, giving them **Can view** permission. Because the data source has [Owner's data credentials](https://docs.cloud.google.com/data-studio/data-credentials), the management team can see the data in the report, even if they don't have direct access to the underlying BigQuery dataset.

## Update and refine

![Avatar for a Data Studio Viewer.](https://docs.cloud.google.com/static/data-studio/images/persona-viewer-2022-07-08.png)

The company CEO loves the report, and asks Aqsa if she can add their marketing analytics data to get even deeper insights. Aqsa edits the report and adds data sources for their Google Ads and Google Analytics accounts. She uses community connectors to access data from Facebook and other social media channels as well. Aqsa uses some of Data Studio's more advanced features, such as [data blending](https://docs.cloud.google.com/data-studio/how-blends-work) and [calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields), to reveal opportunities and challenges she'd never have discovered without being able to see all the available data in one place.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
