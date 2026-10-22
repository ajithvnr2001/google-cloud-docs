---
url: https://docs.cloud.google.com/data-studio/get-a-personal-report-link/
title: Get a personal report link \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:18.076483+00:00
---

# Get a personal report link  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/get-a-personal-report-link/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Get a personal report link Stay organized with collections  Save and categorize content based on your preferences. 

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

To share an editable report with someone while preventing changes to your original report, give them a personal report link. A personal report link creates a copy of your report that is only accessible to the person who opens the link. Changes made to either the original or the private report won't affect the other report.

For example, say you've created a report with sales figures for the last quarter. You want to share this information with your CFO so she can analyze the data and make forecasts for the next quarter. However, other people also rely on the data, so changes to the original report could cause confusion. Instead of manually creating a separate copy of the report and data sources for the CFO, you can give her a personal report link. When she opens the link, she will have her own copy of the report that she can explore and modify. Any changes she makes won't affect the original, so other users can continue to rely on the numbers from last quarter.

## Get a personal report link

To get a personal link to your report, follow these steps:

  1. View or edit the report.
  2. Set any filters, date ranges, or other refinements you want your users to see in their copy of the report.
  3. Click the down arrow next to **Share** ![](https://docs.cloud.google.com/static/data-studio/images/gmarrowdropdowngmgrey60024dp-2023-06-21.png) and then select **Get personal report link** ![](https://docs.cloud.google.com/static/data-studio/images/gmvisibilitygmgrey60024dp-2023-06-12.png).
  4. Click Copy ![](https://docs.cloud.google.com/static/data-studio/images/gmcontentcopygmgrey24dp-2023-06-12.png)**.**



You can now share that link with other users through, for example, email or chat, or by adding it to a document or website.

**Important:** Before you give someone a personal report link, be sure to share the original report and grant that person at least a Viewer role on the report.**Important:** If the original report gets its data from a [reusable data source](https://docs.cloud.google.com/data-studio/data-source-embedded-vs-reusable), you must also grant any recipients of the personal report link at least a Viewer role on that data source.

## How personal report links work

Clicking a personal report link creates a new report that is based on the original. The person who creates the personal report by clicking the link becomes the owner of the new report. The personal report is not connected to the original report. Any modifications made to the personal report don't impact the original report. Conversely, changes made to the original report don't affect existing personal reports.

**Note:** Personal reports are created by using the [Data Studio Linking API](https://developers.google.com/looker-studio/integrate/linking-api). When someone saves or shares a report that was created by the API, they'll see a list of the data sources that were added to the report, along with the credential types that were used by those data sources. [Learn more about sharing reports that are created by the Linking API](https://docs.cloud.google.com/data-studio/share-reports-created-with-the-linking-api).

### Configure your original report view

**Tip:** Be sure that your original report is configured to show recipients of the link the selected view of your data.

The personal report is based on the original report's current view.

**Note:** The current report view includes any changes you've made that limit or refine the data displayed in the report, such as: 

  * Applying filters
  * Applying quick filters
  * Changing the date range
  * Using a data control

The current report view also includes chart interactions, such as: 
  * Setting table pagination
  * Applying a cross filter
  * Selecting optional metrics
  * Drilling down



### Report access

The newly created report is only accessible to the user who opens the personal report link. The personal report does not retain any of the sharing settings from the original report. The person who opens a personal report link is the owner of the new report, with full access. The new owner can view, edit, share, and delete that report. If a second person opens the personal report link, a new report is created, and only that second person has access to that report.

### Data sources

Data sources in the personal report are added according to the following rules:

  * If the original report contains an **embedded data source** , the personal report creates a copy of that data source.
  * If the original report references a **reusable data source** , the personal report references the same data source.
  * If the original report contains a **blend that is based on embedded data sources** , the personal report creates a new blend that is based on the copies of the embedded data sources.
  * If the original report contains a **blend that is based on reusable data sources** , the personal report contains a new blend that is based on the same data sources.



[Learn more about data sources](https://docs.cloud.google.com/data-studio/about-data-sources).

### Data credentials

Access to the data in the personal report depends on how data credentials are configured in the original report's data sources:

  * **Reusable data source credentials** remain unchanged.
  * For **embedded data sources** , the credentials remain as either viewer's or owner's. However, for embedded data sources that use owner's credentials, the new data source uses the credentials of the owner of the personal report.



[Learn more about data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article).

## Use a personal report

**Note:** Personal reports can only be opened by Data Studio Pro users.

Personal report links open in edit mode. You can modify the report and explore the data freely, but before you can view or share the report, you must save it.

To save the report, follow these steps:

  1. In the upper right of the report, click **Save and share**.

  2. The **Review data sources before saving** dialog opens.

**Tip:** The **Review data access before saving** dialog helps you understand where the data in the report is coming from and who will be able to see it. Before saving the report, double-check the connection details and credentials to ensure that they meet your data security requirements.
  3. To make any changes to the data source(s) in the report, click ![Edit icon.](https://docs.cloud.google.com/static/data-studio/images/gmcreategrey60048dp-2020-03-12.png)**Edit**.

  4. To save the report, click **Acknowledge and save**.




## Limits of personal reports

  * Personal reports can be opened only by Data Studio Pro users.
  * A personal report is a copy of the entire original report, including pages that are hidden from view mode. If you want to prevent other people from seeing certain charts or pages in the personal report, remove those from the original report before getting the personal report link.
  * The owner of a personal report must have at least the Viewer role on the original report.
  * If the personal report includes a reusable data source, then the owner of the personal report must have at least the Viewer role on that data source.
  * If a data source in the original report uses viewer's data credentials, then the owner of the personal report must have their own credentials to that data.



## Related resources

  * [Get a link to your report](https://docs.cloud.google.com/data-studio/get-a-link-to-your-report)
  * [Roles and permissions](https://docs.cloud.google.com/data-studio/roles-and-permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
