---
url: https://docs.cloud.google.com/data-studio/filter-by-email-address/
title: Filter by email address \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:19.786158+00:00
---

# Filter by email address  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/filter-by-email-address/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Filter by email address Stay organized with collections  Save and categorize content based on your preferences. 

Reports can request permission to access a report viewer's email address in order to personalize the data shown to that viewer. When users consent to sharing their email address with that report, the underlying data source can use that to return only the data associated with that email address. This is known as "row-level data security."

## Email filter examples

These examples use a data source that is based on Google Sheets to show how email filtering works.

### Example 1

In this example, the data source is not filtered. All the data appears in the Data Studio report.

![A table chart that is not filtered by a user email displays all the values from a Google sheet that includes columns for Name, Favorite Food, and Favorite Number for all users in the spreadsheet.](https://docs.cloud.google.com/static/data-studio/images/email-filter-1-2020-01-31.png)

### Example 2

In this example, the data source has an email filter. Rick is signed in, so only his data appears when he views a report that is based on the filtered data source.

![The table chart with Google Sheets data is filtered for the email rick@example-pet-store.com, and only the Name, Favorite Food, and Favorite Number values for that email are displayed in the chart.](https://docs.cloud.google.com/static/data-studio/images/email-filter-2-2020-01-31.png)

### Example 3

When Michelle signs in and views the same report, she sees only her data, as shown in example 3.

![User Michelle views a report with the Google Sheets data restricted to email = daisy@example-pet-store.com. Only that user's Name, Favorite Food, and Favorite Number values are displayed in the chart.](https://docs.cloud.google.com/static/data-studio/images/email-filter-4-2020-01-31.png)

### Example 4

In this final example, Bob signs in and views the report. There is no data for his email address (bob@example-pet-store.com), so the Data Studio chart is empty.

![The table chart with Google Sheets data is filtered for the email bob@example-pet-store.com, and no data is displayed in the chart.](https://docs.cloud.google.com/static/data-studio/images/email-filter-3-2020-01-31.png)

## For viewers

When you view a report that includes a data source that uses row-level data security, all components that are based on that data source will ask you to allow them to use your email address.

**Warning:** You must be signed in to a Google Account to view a report that uses email filtering.

![A report displays a dialogue that consent is required to load the data and includes an Allow button for the user to select.](https://docs.cloud.google.com/static/data-studio/images/consent-1-2020-01-31.png)

### If you consent

All components in the report that are based on the data source that is requesting your email address will be able to show data that is relevant to you. You can revoke your consent at any time.

### If you don't consent

All components in the report that are based on the data source that is requesting your email address will show only the consent request. They won't show any data.

## For editors

Filtering by email is available for any kind of data source. If your data is in BigQuery, you can also use the email parameter in a custom query to filter by email address.

To use filtering by email address, your underlying data must contain a field that stores the email address for your report viewers. You can then create an email filter in the data source that uses that field. Data Studio can then return the rows of data that contain the email address of the signed-in user.

For example, say you have a spreadsheet that records the performance of your company's sales representatives. Each row in the spreadsheet contains an email address for one of the sales reps. You can turn on email filtering in the data source that is connected to that spreadsheet. When a signed-in viewer views a report that is based on that data source for the first time, they'll be prompted to give their consent to let that report access their email address. The data source can then query for records that contain that address. Only matching records are shown, ensuring that the viewer only sees the data they're meant to see.

## Create an email filter

  1. [Edit your data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Click **FILTER BY EMAIL**.
  3. Check the **Filter data by viewer email** checkbox.
  4. Select the field in your data source that contains viewer email addresses.
  5. To return to the data source editor, click **ALL FIELDS**.



## Stop filtering by email

  1. [Edit your data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Click **FILTER BY EMAIL**.
  3. Clear the **Filter data by viewer email** checkbox.



## Filter by email in BigQuery

In a BigQuery data source, you can filter by email address using the ```@DS_USER_EMAIL``` parameter in a custom query. For example:

`Select * from Sales WHERE sales-rep-email =``@DS_USER_EMAIL``;`

This provides additional flexibility in your filters. Learn more about [BigQuery parameters](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery).

## Filter by email in scheduled report delivery

You can include email address filters in reports that get delivered by scheduled email and Google Chat. When one or more of the data sources in that report have email filtering enabled, you'll see the **Filter the delivered report data by recipient's email address** option when you're creating or editing your schedule.

Learn more about [scheduled automatic report delivery](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery).

## Revoke access to your email

To stop providing your email address to reports that request it, you can revoke your consent by following these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. In the upper right, click **Settings** ![Settings.](https://docs.cloud.google.com/static/data-studio/images/icsettingsgrey6002xweb48dp-2019-12-03.png).
  3. On the left, select **Revoke Consent**. Next, under **Revoke user email,** click **Revoke all**.



After you revoke your consent, you'll need to grant it again before you can see personalized data in reports.

## Limits of filter by email

  * Your underlying dataset must contain the full email address of the viewers who will be accessing your report.
  * The case of the email addresses in your data must match the case in the users' accounts. For example, if a user's account belongs to "Bob@example-pet-store.com" but your data contains "bob@example-pet-store.com", the filter won't match (and Bob won't see his data).
  * Viewers must sign in to view a report with email filtering applied, even if the report is shared publicly.
  * Viewers must consent to providing their email address.



## Related resources

[Use data blending to filter by multiple email addresses per row](https://docs.cloud.google.com/data-studio/filter-by-multiple-email-addresses-per-row).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
