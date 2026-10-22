---
url: https://docs.cloud.google.com/data-studio/create-a-report-from-a-template/
title: Create a report from a template \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:28.466721+00:00
---

# Create a report from a template  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-a-report-from-a-template/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create a report from a template Stay organized with collections  Save and categorize content based on your preferences. 

Templates let you visualize your data in a finished report. Use these reports "as is" or customize them to fit your unique requirements. You can also create your own templates for others to use.

## Template gallery

Visit the [Template Gallery](https://datastudio.google.com/navigation/templates) to access templates built by Google. You'll find templates that support the following products:

  * BigQuery
  * Google Analytics
  * Google Ads
  * Google Sheets
  * YouTube Analytics
  * Search Console
  * Display & Video 360
  * Search Ads 360
  * Apigee



> **Note** : Even though Google templates are available only in English, your data will appear in the language in which it was collected.

## How templates work

A template is a special kind of report, created by appending `/preview` to the report's URL. You can interact with a template in view mode just as you would any report. However, before you can modify or share the template, you must copy it to a new report by clicking **Edit and share**.

The data in a template comes either from a data source that's been shared with you, or from a [data control](https://docs.cloud.google.com/data-studio/data-control) placed on the template. Data controls let you select the data set you want to use in a report. If the template is based on a shared data source, you may want to replace that with your own data source to make the report more relevant to you.

## See your data in a template

To see your own data in a template you can either replace the default data source with a reusable data source to which you have access, or you can create a new embedded data source. [What's the difference?](https://docs.cloud.google.com/data-studio/embedded-data-sources)

![](https://docs.cloud.google.com/static/data-studio/images/template-add-data-2-2022-03-17.png)

### Select an existing data source

  1. Open a template.
  2. In the upper right, click **Use my own data** , then click **Replace data**.  
**Note** : If the template has multiple data sources, you'll see multiple **Replace data** buttons. Repeat these instructions for each data source you want to replace.
  3. In the upper left, click ![Return arrow icon](https://docs.cloud.google.com/static/data-studio/images/return-arrow-icon-2015-09-18.png)**Add data to report**.
  4. On the left, click **My data sources**.
  5. Select the data source; then, in the lower right, click **Add**.



### Create a new data source

  1. Open a template.
  2. In the upper right, click **Use my own data**.  
**Note** : If the template has multiple data sources, you'll see multiple **Replace data** buttons. Repeat these instructions for each data source you want to replace.
  3. Select the account or project configuration for the [data set](https://docs.cloud.google.com/data-studio/dataset) that you want to use, and then click **ADD**.



> ### Data source status
> 
> An orange dot to the right of the Add data button means that you only have view access to the default data source. If you copy the template to your own report, then the report will have errors. We recommend replacing the data source with one to which you have full access.
> 
> ![An orange dot next to the Use my own data button indicates that a user has only view access to a data source.](https://docs.cloud.google.com/static/data-studio/images/add-data-orange-2022-03-15.png)
> 
> After replacing a data source in the template, a green dot to the right of the Add data button means that you have full access to the new data source.
> 
> ![A green dot next to the Use my own data button indicates that a user has full access to a data source.](https://docs.cloud.google.com/static/data-studio/images/add-data-green-2022-03-16.png)

## Edit and share a template

You can save a template as your own report. In the upper right, click **Edit and share**. You can then modify the report and share it with others, just like any other report.

## Create your own template

Any report in Data Studio can be a template: just view the report, and then edit the URL in the location bar by adding " `/preview` " at the end.

**Example** :

This is the URL of the Data Studio "Instructions" report, with "/preview" appended to turn it into a template:

[https://datastudio.google.com/reporting/0B5FF6JBKbNJxOWItcWo2SVVVeGc/page/DjD/preview](https://datastudio.google.com/c/reporting/0B5FF6JBKbNJxOWItcWo2SVVVeGc/page/DjD/preview)

## Submit a template to the gallery

Got a Data Studio report you'd like to share as a template for others to use? [Submit it to the report gallery](https://docs.cloud.google.com/data-studio/the-report-gallery).

## Related resources

  * See featured reports, additional templates, data connectors, and community visualizations in the [Data Studio Report Gallery](https://datastudio.google.com/gallery?category=marketing)
  * [Copy a report](https://docs.cloud.google.com/data-studio/copy-a-report)
  * [Add data to a report](https://docs.cloud.google.com/data-studio/add-data-to-a-report)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
