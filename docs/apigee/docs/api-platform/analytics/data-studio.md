---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/data-studio/
title: Data Studio Integration \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:03.948277+00:00
---

# Data Studio Integration  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/data-studio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Data Studio Integration Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Data Studio Integration**

This feature is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA features may have limited support, and changes to pre-GA features may not be compatible with other pre-GA versions. For more information, see the [ launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

Support for the Preview launch of Advanced API Security Abuse Detection is available through the [ Apigee - Google Cloud Community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee) forum.

**Note:** Data Studio Integration is currently not supported for organizations with [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) enabled.

In addition to viewing Apigee Analytics and monetization data in the Apigee UI, you can also view them using Data Studio Integration, which connects Apigee data to Google's [ Data Studio](https://cloud.google.com/data-studio). Data Studio is a powerful and flexible tool that you can use to display Apigee data in fully customizable dashboards and reports.

**Note:** If your organization uses [VPC service controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc), you must add [ egress and ingress rules](https://cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the Data Studio service account to allow services for the following APIs: 

  * `bigquery.googleapis.com`
  * `bigquerydatatransfer.googleapis.com`



The following sections explain how to create an Analytics data report in Data Studio.

## Required role

To use Data Studio, you first need to connect it to a data source—in this case, Apigee. To make the connection, you need to have the role `roles/apigee.analyticsEditor`.

See [Apigee roles](https://cloud.google.com/iam/docs/roles-permissions/apigee) for more information.

## Connect to the Apigee data source

To connect to the Apigee data source, do the following steps:

  1. Open [Data Studio](https://datastudio.google.com). The main Data Studio page is shown below: 

![Main Data Studio page.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/looker-studio.png)

  2. Click the **\+ Create** button at the top of the page.
  3. Select **Data source** to display an untitled **Data Source** page.
  4. Scroll down and click the **Apigee** button: 

![Apigee button in the Data Studio report page.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/looker-studio-apigee-button.png)

  5. Click the **Authorize** button to allow Data Studio to connect to the Apigee data. 
  6. In the **Apigee Organization Name** field, enter the organization ID. **Note:** The organization ID is the same as the Google Cloud project ID for the organization.
  7. Click **Connect** at the top-right of the window.

**Note:** You must have the role `roles/apigee.analyticsEditor` to perform this step.

When the connection to Apigee is made, Data Studio displays the page shown below, where you can create a report:

![Apigee Analytics page in Data Studio.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apigee-analytics-in-looker.png)




The next section explains how to view an Analytics data report in Data Studio using the Apigee API Platform template.

## Use the Apigee API Platform template

The following sections describe how to view a predefined report using the Apigee API Platform template.

  * Open the Apigee API Platform template from Data Studio
  * Open the Apigee API Platform template from the Apigee UI



### Open the Apigee API Platform template from Data Studio

To open the Apigee API Platform template from Data Studio:

  1. In the Data Studio page, select **Templates** in the navigation pane.
  2. In the **Category** menu in **Template Gallery** , select **Apigee**.
  3. Under **Apigee** , select **Apigee API Analytics**. This displays the **Apigee API Platform** template: 

![Apigee API Platform template.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apigee-api-platform-template.png)

  4. Click **Use my own data** at the top-right of the page to open the **Add data to report** dialog.
  5. In the **Apigee Organization Name** field, enter the organization ID. **Note:** The organization ID is the same as the Google Cloud project ID for the organization.
  6. Click **Add** at the lower right.



### Open the Apigee API Platform template from the Apigee UI

To open the Apigee API Platform template from the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Analytics > Custom Reports** page.

[Go to Custom Reports](https://console.cloud.google.com/apigee/analytics/custom-reports)

  2. Click **Create More Reports Using Data Studio** at the top-right. This displays the **Apigee API Platform** template: 

![Apigee API Platform template.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apigee-api-platform-template.png)

  3. Click **Use my own data** at the top-right of the page to open the **Add data to report** dialog.
  4. In the **Apigee Organization Name** field, enter the organization ID. **Note:** The organization ID is the same as the Google Cloud project ID for the organization.
  5. Click **Add** at the lower right.

**Note:** In the **Developer Adoption** chart, the number below **Application** is the number of active applications within the selected date range, shown at the top right of the template. This differs from the total number of applications (shown, for example, in the **Traffic growth** chart above), which includes inactive applications.

You can view a number of different charts in the report, including:

  * API product growth
  * Traffic growth
  * Latency performance
  * Error code improvements



See the Data Studio [ Quick start guide](https://support.google.com/looker-studio/answer/9171315#zippy=%2Cinstructions) to learn more.

## Create an Analytics data report

You can also create an Analytics data report directly in Data Studio, without using the Apigee API Platform template:

  1. In the Data Studio page, click **\+ Create**.
  2. Select **Report**.
  3. Under **Add data to report** , select **My data sources**.
  4. Select **Apigee - Analytics**.
  5. Click **Add** at the lower right.
  6. In the confirmation dialog, click **Add to Report**. This displays the Report page with Apigee Analytics data available to add to the report, as shown below: 

![Report page ready to create report.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ready-to-create-report.png)




You can now create an Analytics report. Here's an example that creates a graph of API traffic over time:

  1. Select the **Insert** menu at the top of the Report page.
  2. Select **Time series chart**.
  3. In the **Metric** pane on the right side of the Report page, select **\+ Add metric**.
  4. Scroll down through the **Available Fields** and select **Traffic**.



This displays a time series chart of recent traffic. An example is shown below. (Your data will vary.)

![Time series chart of recent API traffic.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/time-series-graph-traffic.png)

If you want to view a different time range for the data, return to the **Insert** menu and select **Date range control**. You can then use the control to select a time range for the data to display.

The Data Studio documentation describes how to create many kinds of reports. For more information, see the following:

  * [ Data Studio Quick start guide](https://support.google.com/looker-studio/answer/9171315#zippy=%2Cinstructions)
  * [Explore new ways to visualize your data ](https://datastudio.google.com/visualization)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
