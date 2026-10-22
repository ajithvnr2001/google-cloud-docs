---
url: https://docs.cloud.google.com/data-studio/share-reusable-data-sources/
title: Share reusable data sources \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:37.281038+00:00
---

# Share reusable data sources  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/share-reusable-data-sources/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Share reusable data sources Stay organized with collections  Save and categorize content based on your preferences. 

> This article applies to reusable data sources. Embedded data sources are shared when you share the report in which they are embedded. Learn more about the [types of data sources](https://docs.cloud.google.com/data-studio/about-data-sources).

**Tip:** You don't need to share a report's data source for other people to view the report. Authorization to see the data in a report is governed by [data credentials](https://docs.cloud.google.com/data-studio/data-credentials). Viewers of a report can see the data they are authorized to see whether or not the data source is shared with them.

To share a reusable data source, use the Data Studio home page:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. In the top, select **Data sources**.
  3. Locate the data source you want to share, then on the right, click More ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png).
  4. Click ![Share icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png)**Share**. The _Share with others_ dialog appears.
  5. Under **Add people** , enter the names or email addresses of the people with whom you want to share. You can also share with [Google Groups](https://groups.google.com/).
  6. Select the [access permission](https://docs.cloud.google.com/data-studio/roles-and-permissions) for the people and groups you've specified:

     * **Can edit** : Users can edit the asset and share it with others.

     * **Can view** : Users can see the asset and share it with others, but can't edit it.

  7. To set different permissions for different people, click **Manage access**.

  8. By default, people you invite receive an email with a link to the asset you're sharing. Uncheck **Notify people** to not send that email.

  9. Click **Send**.




## How sharing data sources works

  * Sharing a data source never grants access to the underlying [data set](https://docs.cloud.google.com/data-studio/dataset).
  * A Google login is required to view or edit a data source.
  * Sharing a data source with view permission allows the viewer to see the schema (structure) of the data source, but not change it.
  * Sharing a data source with edit permission allows editors to change the schema: they can rename and disable fields, add calculated fields, change data type and default aggregation, and add descriptions.
  * Only the data source owner can [edit the data source connection](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
