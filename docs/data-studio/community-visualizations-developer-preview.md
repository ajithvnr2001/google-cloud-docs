---
url: https://docs.cloud.google.com/data-studio/community-visualizations-developer-preview/
title: Community visualizations (Developer Preview) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:34.988821+00:00
---

# Community visualizations (Developer Preview)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/community-visualizations-developer-preview/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Community visualizations (Developer Preview) Stay organized with collections  Save and categorize content based on your preferences. 

You can use community visualizations created by third-party developers to expand your charting options in Data Studio. These custom charts connect directly to your data and configure just like built-in charts. You can use community visualizations to build specialized visual reports tailored to your team's unique analytical requirements.

**Warning:** Community visualizations display data from your data source. Although the community visualization can't access your data directly, you should still be sure you trust the developer of any community visualizations you add to your reports.

This feature is in [Beta](http://developers.google.com/looker-studio/visualization/developer-preview) and is intended to let you try out community visualizations and give us feedback. Learn more about the Community Visualization Program in the [developer documentation](https://developers.google.com/looker-studio/visualization/). Available visualizations can be found in the [Community Visualizations Gallery](https://datastudio.google.com/visualization).

## Add a community visualization to your report

**Note:** To use third-party community visualizations in your report, the data source must use [Owner's credentials](https://docs.cloud.google.com/data-studio/data-credentials).

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the toolbar, click ![](https://docs.cloud.google.com/static/data-studio/images/iconcommunityviz24px-2020-01-28-.svg)**Community visualizations and components**.
  3. Select a visualization.

You can select from featured visualization, visualizations you've already added to the report, or click **\+ Explore more** to select a visualization from the Community Gallery.

  4. If prompted, grant your consent to allow the visualization to show data.




### If you consent

All components in the report based on the community visualization are able to show data. You can revoke your consent at any time.

### If you don't consent

All components in the report based on the community visualization show only the consent request. They won't show any data.

### Add a community visualization to your report by ID

You can test your own community visualization by entering a manifest path.

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the toolbar, click ![](https://docs.cloud.google.com/static/data-studio/images/iconcommunityviz24px-2020-01-28-.svg)**Community visualizations and components**.
  3. Click **\+ Explore more** to open the Community Gallery.
  4. In the top left, click **Build your own visualization.**
  5. Under _Test and add your community visualization_ , enter the **Manifest Path** and then click **Submit.**
  6. Click a visualization to add it to your report.



Once you've added a community visualization, you can copy it within the report, or copy and paste it to another report.

## Manage visualizations resources

When you add a new community visualization, Data Studio adds a resource for that visualization to the report. The individual community components that you place on the canvas are instances of the resource for that particular visualization.

### Delete community visualizations from a report

To delete a community visualization component from the report canvas, select that component and press **Delete**.

Deleting a selected community component from the canvas deletes only that particular component. Deleting the component doesn't remove the resource or revoke consent to use that resource.

### Revoke consent from a community visualization

To completely remove the community visualization resource:

  1. Click **Resource > Manage community visualizations**.
  2. Locate the visualization resource, then click ![](https://docs.cloud.google.com/static/data-studio/images/gmdeletegrey60048dp-2020-03-09.png)**Revoke**.
  3. In the upper right, click **X CLOSE**.
  4. Delete any visualizations that use the revoked resource.

**Tip:** If you change your mind, you can restore the resource by clicking **Allow** in any broken components.

## Turn off community visualizations in your data source

Community visualizations are turned on by default in data sources that use Owner's credentials. To turn off community visualizations:

  1. Edit your data source.
  2. In the top right, click **Community visualizations access**.
  3. Select **Community visualization access: OFF**.



## Copy a report with community visualizations

Copying a report with community visualizations also copies those visualizations to the new report. You'll need to provide consent for community visualizations in the new report before they can show data.

## Community visualizations built by Google

Several of the available community visualizations are built by Google, using the same process as other community visualizations. These include the Gauge, Waterfall, and Candlestick charts. Because these visualizations are built by Google, you don't need to provide consent to use them. In addition, Community visualizations built by Google may use either Viewer's credentials or Owner's credentials to access the data.

## Related resources

[Community connectors](https://docs.cloud.google.com/data-studio/about-community-connectors)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
