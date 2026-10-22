---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases/
title: Resolve and close cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:28.104143+00:00
---

# Resolve and close cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolve and close cases

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how to close cases in Google Security Operations using various interface options, including the case details page, the case queue (side-by-side and list views), and the **Search** page. It also explains how to view the contents of closed cases. You can close a case once it's resolved. For information on what details to enter when closing a case, see [Use custom fields](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/custom-fields-in-case-closure).

## Ways to close a case

You can close a case once it's resolved. You can do this from the following locations:

  * For a single case, use the case details page (top menu).
  * For multiple cases, use bulk actions from one of the following locations: 
    * Side-by-Side or List views on the **Cases** page
    * The **Search** page
    * The Tools integration job

**Note:** Cases can also be closed automatically using playbook actions. 

## Close a single case from the case details page

  1. Open the case you want to close, then click ![closecaseicon](https://docs.cloud.google.com/static/chronicle/images/soar/closecaseicon.png)**Close Case**.
[ ![closecases1](https://docs.cloud.google.com/static/chronicle/images/soar/closecases1.png)](https://docs.cloud.google.com/static/chronicle/images/soar/closecases1.png)
  2. In the **Close Case** dialog, select a valid reason and a root cause for closing the case, and enter any additional comments. You must select a reason before you can select a root cause. These comments will be posted on the Case Wall. If you create a custom **Siemplify - Close Case** action in the IDE, you must select one of the parameter types to be **Close case reason**.
[ ![closecases2](https://docs.cloud.google.com/static/chronicle/images/soar/closecases2.png)](https://docs.cloud.google.com/static/chronicle/images/soar/closecases2.png)
  3. Click **Close**.



## Close multiple cases at once

When you manage a high volume of cases, choose a method that matches your workflow and the number of cases you want to close.

The following guidelines are based on the approximate number of open cases in your case queue.

### For 1-50 cases

If you have 1-50 cases to close, you can use these methods directly within the platform from the **Cases** page views or the **Search** page.

#### From the cases queue (side-by-side view)

  1. In the cases queue, click ![multipleselecticon](https://docs.cloud.google.com/static/chronicle/images/soar/multipleselecticon.png)**Select multiple cases**.
[ ![closecases3](https://docs.cloud.google.com/static/chronicle/images/soar/closecases3.png)](https://docs.cloud.google.com/static/chronicle/images/soar/closecases3.png)
  2. Select the relevant cases you want to close in the cases queue.
  3. Click  format_list_bulleted  **Close Cases/Merge Cases** and select **Close Cases**. 
[ ![closecases3](https://docs.cloud.google.com/static/chronicle/images/soar/closecases4.png)](https://docs.cloud.google.com/static/chronicle/images/soar/closecases4.png)
  4. In the **Close Case** dialog, select a valid reason and a root cause. Optionally, enter comments to post on the Case Wall.
  5. Click **Close**.



#### From the cases queue (list view)

  1. Select the checkboxes for the cases you want to close in the case list grid.
  2. In the top right toolbar, click **Actions** and select **Close cases** (or click the ![closecaseicon](https://docs.cloud.google.com/static/chronicle/images/soar/closecaseicon.png)**Close cases** icon in the legacy experience toolbar).
[ ![closecases6](https://docs.cloud.google.com/static/chronicle/images/soar/closecases6.png)](https://docs.cloud.google.com/static/chronicle/images/soar/closecases6.png)
  3. In the **Close Case** dialog, select a valid reason and a root cause for closing the case and enter any additional comments. These comments will be posted on the Case Wall.
  4. Click **Close**.



#### From the Search page

  1. Go to the **Search** page.
  2. Apply filters to find the relevant cases you want to close.
  3. From the search results, select the cases you want to close (up to 50 cases).
  4. Click  format_list_bulleted  **Menu** and select **Close case**.
  5. In the **Close Case** dialog, choose a valid reason and a root cause. Optionally, enter comments to post on the Case Wall. Click **Close** when finished.



### For cases higher than 50

For volumes higher than 50 cases, rely on the **Close Cases Based On Search** job in the Tools integration. For more information, see [Jobs - Close Cases Based On Search](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/tools#close-cases-based-on-search).

**Important:** When configuring filters for the search query, "non-Custom" relative timerange filters (such as Last 24 Hours) may or will cause accidental closure of newly ingested cases as the job runs. You should use a "Custom" timerange filter to stay between specific fixed dates to ensure that no new cases are closed. 

Contact [Google Support](https://console.cloud.google.com/support) if the two preceding options fail.

### View the contents of a closed case

To view the contents of closed cases, follow these steps:

  1. Go to the **SOAR Search** page (or filter by status directly in the **Cases** queue).
  2. In the **Filter** section, select **Status > Closed**.
  3. Click **Apply**.
  4. In the list of closed cases, click the ID number of the selected case; you're redirected to the original case contents.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
