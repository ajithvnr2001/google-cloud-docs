---
url: https://docs.cloud.google.com/chronicle/docs/reports/import-export-dashboards/
title: Import and export dashboards \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:55:31.285606+00:00
---

# Import and export dashboards  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/import-export-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Import and export dashboards

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

You can share a dashboard file between instances or within an instance between different users. The dashboard can be shared without manually creating copies. With this functionality you can do the following:

  * Export a dashboard configuration

  * Import a dashboard exported through Google Security Operations




## Export dashboards

You can export personal and shared dashboards. Default dashboards cannot be exported. The exported file includes the dashboard layout and the filter settings. The scheduled delivery settings are not exported. 

### Export dashboards from Google SecOps

To export a dashboard from Google SecOps, do the following:

  1. [Log in](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui) to your Google SecOps instance.

  2. In the navigation bar, click **Dashboards**.

  3. From the list of personal or shared dashboards, click  more_vert **Menu** next to the dashboard that you want to export.

  4. Select **Export** from the list.

The **Export dashboard** dialog appears.

  5. Click **Export**.

The YAML file is downloaded to the browser's Downloads directory.




### Export dashboards from Looker

To export a dashboard from Looker, do the following:

  1. Get the dashboard's LookML content from enterprise Looker.

     1. Open the dashboard that you want to export.
     2. Click more_vert **Menu** in the top right corner and select **Get LookML**. A window showing the LookML code for the dashboard elements appears.
  2. Copy the LookML file content to a `.yaml` file.

  3. Add a new line with the text `lookml:` before the existing content.

For example, if the LookML content from the enterprise Looker is:
         
         - dashboard: example_dashboard
           description: ""
           layout: newspaper
           title: Example Dashboard
         

To import it to Google SecOps, modify it to:
         
         lookml:
         - dashboard: example_dashboard
           description: ""
           layout: newspaper
           title: Example Dashboard
         

The modified YAML file is ready to be imported to Google SecOps.




## Import dashboards

To import a dashboard, you need a dashboard file exported through Google SecOps or Looker. When you import a dashboard, the dashboard's layout and the filter settings are imported too. The scheduled delivery settings are not imported. You can import a dashboard to personal or shared dashboards by doing the following:

  1. [Log in](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui) to your Google SecOps instance.

  2. In the navigation bar, click **Dashboards**.

  3. On the Dashboards page, click the arrow next to **\+ New dashboard** and select **Import from JSON** from the drop-down menu.

  4. Browse and select your JSON file.

  5. Click **Edit** to update the name, description, and access settings.

  6. Click **Save** > **Import**.




The imported dashboard is added to the existing dashboards list.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
