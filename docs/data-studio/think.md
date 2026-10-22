---
url: https://docs.cloud.google.com/data-studio/think/
title: Think with Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:54.240775+00:00
---

# Think with Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/think/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Think with Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

Learning any new tool requires mastering certain basic concepts and techniques. This page will help you understand how to approach using Data Studio as a new user so that you can get started discovering insights and communicating them to your stakeholders.

## Connect, model, visualize, share, and collaborate

This page describes the basic steps that you'll follow when you work with Data Studio.

### Connect

First, you'll connect Data Studio to an underlying dataset, such as a database, spreadsheet, or Google Analytics account. Connecting to your data creates a data source in Data Studio. Data sources provide the fields (metrics and dimensions) available for you to visualize in your reports.

> #### Definitions
> 
>   * **Connector** : The mechanism by which Data Studio accesses a specific data platform, system, or product.
>   * **Dataset** : The underlying platform or product that contains the data on which you want to report.
>   * **Data source** : A specific instance of a connection to your data.
> 


### Model

Once you've connected to your data, you can fine-tune the data source by applying data modeling features, such as creating calculated fields, changing the way your data is aggregated, or blending data from different sources into a single source that you can use in your visualizations.

> #### Definitions
> 
>   * **Aggregation** : The method that is used to summarize data. For example, sum, average, min, or max.
>   * **Blend** : Data that is derived by joining fields from different data sources, or multiple instances of the same data source.
>   * **Calculated field** : A field that you create in a data source or a chart based on a formula you provide.
> 


### Visualize

You'll visualize your data by creating a report and then adding components to it that display or act upon the data. There are other ways to create reports, such as starting with a template and creating a report using the Linking API.

> #### Definitions
> 
>   * **Component** : Anything you can add to a report that can be styled or associated with a data source.
>   * **Report** : A Data Studio asset that presents information and insights derived from your data.
> 


### Components: The building blocks of your reports

You'll use the visual report editor to build your reports by adding components, such as the following:

  * Charts, tables, maps, and graphs are examples of components that can visualize your data. (You can also call them "visualizations," but for simplicity's sake (and to save on typing), we refer to all of these as "charts.")
  * Controls are components that can filter or refine the data in your charts and turn your reports into interactive experiences for your viewers.
  * Other types of components let you add text annotations, shapes, images, and embedded content from other applications, such as web pages and video.



> #### How Data Studio visualizes your data
> 
> Although different chart types display your data differently, the way Data Studio organizes and summarizes your data is the same for all charts:
> 
>   * Data is grouped by the dimensions in the chart. For example, adding **Country** and **Region** to a chart groups the data first by country and then by region.
>   * Metrics are summarized according to the groupings that are provided by the dimensions in that chart.
> 

> 
> Here's an example:
> 
> The following sample report contains two table charts and a scorecard chart that show data from the same dataset (airline flight information). Note how the metric **# of flights** is summarized according to the dimensions that are shown in the chart.
> 
> ![Three visualizations: A table displays the number of flights grouped by OriginState, a table displays the number of flights grouped by OriginState and Carriername, and a scorecard displays the number of flights.](https://docs.cloud.google.com/static/data-studio/images/grouping-example-numbered-2022-06-22.png)
> 
>   1. In the first table, the number of flights is summarized by the state of origin. The values in the **OriginState** field appear only once in the table. This table has 53 rows.
>   2. In the second table, the number of flights is summarized by the state of origin and the airline name. The combination of **OriginState** and **Carriername** appears only once in the table. This table has 921 rows.
>   3. In the scorecard, the total number of flights is displayed (116,764,823). Scorecards have no dimensions with which to break down the data, so they always display the full value of the metric for the current date range and any filters that are applied to the report.
> 

> 
> Learn more about [working with dimensions and metrics](https://docs.cloud.google.com/data-studio/model-your-data).

## Share and collaborate

When you've found insights in your data that you want others to see, or if you want to collaborate with other Data Studio users, you can share your reports. You can also share the data sources you've created so others can build reports using that data as a source of truth.

When you share a report, you decide who can see the data in that report and whether they can modify the report or only view it. Controlling who can see the data is based on data credentials, while view or edit access is based on permissions.

#### Definitions

  * **Data credentials** : The mechanism by which a data source determines who can see its data. You can apply one of these credentials to any data sources that are added to the report:

    * **Owner's credentials** uses the credentials of the data source owner to authorize access to the dataset. This option lets you share reports that use this data source without requiring report viewers to have their own access to the underlying dataset. Important: Before sharing a report or data source that uses Owner's credentials, be sure that you trust the person or persons with whom you share them.
    * **Viewer's credentials** require anyone who attempts to view the data that is provided by this data source to have their own access to the dataset.
    * **Service account credentials** use a special type of Google Account that is intended to represent a non-human user that can authenticate and be authorized to access your data.
  * **Permissions** : The setting that controls what another person can do with your report. You can apply one of the following permissions to the reports that you share:

    * **Can View** : The other person can only view the report and use interactive controls such as the date picker and filters.
    * **Can Edit** : The other person can modify the report and possibly share it with others.. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
