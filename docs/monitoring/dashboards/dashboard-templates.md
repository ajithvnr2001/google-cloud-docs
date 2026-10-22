---
url: https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates/
title: Install a dashboard template \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:57.432871+00:00
---

# Install a dashboard template  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Install a dashboard template Stay organized with collections  Save and categorize content based on your preferences. 

Dashboard templates in Cloud Monitoring let you quickly set up custom dashboards with preconfigured charts for Google Cloud services such as Compute Engine, Cloud Storage, and BigQuery. You can install JSON templates from the template library in the Google Cloud console. You can also install templates from the GitHub [`monitoring-dashboard-samples` repository](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples) by using the Google Cloud console, the Google Cloud CLI, or the Cloud Monitoring API.

## Install a dashboard template

**Note:** Some of the dashboard templates stored in the GitHub [`monitoring-dashboard-samples` repository](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples) display custom metric data. To install these dashboards successfully, you must create the necessary user-defined metrics. For more information, consult the per-service documentation in the repository.

###  Google Cloud console 

To install a dashboard template by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 

  3. Do one of the following:

     * To install a template from the library available in the Google Cloud console, do the following:

       1. Click **Dashboard Templates**.
       2. Find the dashboard that you want to install.
       3. Optional: To preview the dashboard, select it.
       4. Click _playlist_add_ **Add dashboard to your list** and then complete the dialog.

The dialog lets you select the name of the dashboard, and add labels to the dashboard.

     * To install a dashboard by uploading a JSON file, do the following:

       1. Optional: To install a curated dashboard template, download the GitHub repository:
    
    git clone https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples.git

       1. Click **Create Dashboard**.
       2. In the dashboard toolbar, click _settings_ **Settings** , select **JSON** , and then select **JSON Editor**.

For a new dashboard, the displayed code is similar to the following:
    
    {
        "displayName": "New Dashboard",
        "mosaicLayout": {
          "columns": 12,
          "tiles": []
        },
        "dashboardFilters": [],
        "labels": {}
    }
    

       1. In the editor's toolbar, click upload **File Upload**.
       2. Select the file that contains the template and then click **Open**.

After the file is uploaded, the dashboard's JSON is updated.

If you see the following message, "Unable to save dashboard: Field mosaicLayout.tiles[0] has an invalid value", then select **Grid** in the dashboard toolbar.

       1. Optional: Customize the dashboard. For example, you can update the title, add a text widget that indicates the dashboard source, delete unwanted charts, or add charts.
       2. To save your modified dashboard, in the toolbar, click **Save**.



###  gcloud CLI 

To install a dashboard definition by using the Google Cloud CLI, do the following:

  1. Ensure the dashboard definition is accessible to your local system.

For dashboards stored in the GitHub repository, you can save specific dashboards, or you can download the entire repository:
         
         git clone https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples.git
         

  2. Identify the dashboards you want to install.

For example, in the GitHub repository, the directory `monitoring-dashboard-samples/dashboards/compute` contains a file named `gce-vm-instance-monitoring.json`.

  3. Issue the [`gcloud monitoring dashboards create`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create) command and provide the JSON representation of the dashboard.

For example, to install the dashboard `gce-vm-instance-monitoring.json`, issue the following command:
         
         gcloud monitoring dashboards create --config-from-file=gce-vm-instance-monitoring.json --project=PROJECT_ID
         

Before you run the previous command, replace the following:

     * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.



###  REST 

To install a dashboard definition by using the Cloud Monitoring API, do the following:

  1. Ensure the dashboard definition is accessible to your local system.

For dashboards stored in the GitHub repository, you can save specific dashboards, or you can download the entire repository:
         
         git clone https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples.git
         

  2. Identify the dashboards you want to install.

For example, in the GitHub repository, the directory `monitoring-dashboard-samples/dashboards/compute` contains a file named `gce-vm-instance-monitoring.json`.

  3. Call [`dashboards.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create) and provide the JSON representation of the dashboard. In the API call, the parent is the project in which to create the dashboard. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. This field has the following format:
         
         projects/PROJECT_ID
         




For more information, see [Create and manage dashboards](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

## View the installed dashboard

Each file in the repository creates a new custom dashboard. For example, the file `gce-vm-instance-monitoring.json` creates a dashboard with the title "GCE VM Instance Monitoring". To view this dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the list of dashboards, click "GCE VM Instance Monitoring". If you have a lot of dashboards, then you might want to filter for custom dashboards or for the name of the new dashboard.



The following screenshot shows part of the installed dashboard:

![Example of the Compute Engine VM Instance Monitoring dashboard.](https://docs.cloud.google.com/static/monitoring/images/gce-vm-monitoring-db.png)

## Add or remove user-defined labels

Labels can help you locate dashboards based on the type of content they display. For example, you might add the label `prod` to dashboards that display information about production systems. Similarly, you might add the label `staging` to indicate the dashboard displays information about staging systems.

You can add labels only to custom dashboards. When a dashboard displays the sell **Add labels to dashboard** button, then you can configure which labels are applied to the dashboard.

To add or remove user-defined labels on a custom dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the list of dashboards, locate the dashboard and then click sell **Add labels to dashboard**.
  3. Do one of the following: 
     * To create a label and add it to your dashboard, in the **Create a new label** section, enter the name of the label in the textbox and then click **Create and apply**.

     * To configure which labels are added to your dashboard, click _arrow_drop_down_ **Select labels to apply** , select the labels, and then click **Ok**.
  4. To save your changes, click **Confirm**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
