---
url: https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards/
title: Manage and configure dashboards \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:05:25.311544+00:00
---

# Manage and configure dashboards  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage and configure dashboards

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for security analysts and administrators who want to manage their visualization workspace within Google SecOps. It explains how to view, create, edit, and share dashboards to monitor security metrics. By following this method, you can maintain an organized reporting environment and collaborate across security teams. Successful completion provides streamlined access to critical data and secure sharing of internal security visualizations.

This document explains how to manage dashboards. The Dashboards page shows a list of both curated and custom dashboards. When you access it for the first time, only curated dashboards are visible.

## Common use cases

Use these use cases to understand how dashboard management supports your operational workflows and improves team collaboration.

### Centralize security monitoring

  * **Objective:** Organize multiple dashboards into a single, filtered view.
  * **Value:** Improves triage efficiency by surfacing the most relevant dashboards through pinning and searching.



### Collaborate on custom visualizations

  * **Objective:** Share private dashboards with the broader SOC team or export them to other instances.
  * **Value:** Standardizes reporting across the organization and prevents redundant dashboard creation.



### Export dashboard data

  * **Objective:** Extract dashboard data into portable formats for offline analysis.
  * **Value:** Improves collaboration and efficiency among colleagues and customers.



## Key terminology

  * **Curated dashboard:** A built-in, predefined visualization provided by Google SecOps.
  * **Custom dashboard:** A user-created visualization that can be blank, a duplicate, or an imported JSON.
  * **Shared access:** A setting that makes a dashboard visible to all users within the Google SecOps instance.
  * **Private Access:** A setting that restricts dashboard visibility to only the owner.



## Before you begin

Confirm you have the following IAM permissions before attempting these tasks:

  * **View dashboards:** `chronicle.nativeDashboards.list`
  * **Create dashboards:** `chronicle.nativeDashboards.create`
  * **Edit/Share dashboards:** `chronicle.nativeDashboards.update`
  * **Delete dashboards:** `chronicle.nativeDashboards.delete`
  * **Export/Download:** `chronicle.nativeDashboards.get`
  * **Duplicate dashboards:** `chronicle.nativeDashboards.duplicate`



For more details about roles and permissions, see [Explore curated dashboards and threat detections](https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards-overview).

## Organize the dashboard list

The **Dashboards** page displays both curated and custom dashboards. Use the following interface actions to customize how you view and access your security data:

  * **Sort:** Click a column heading to sort in ascending or descending order.
  * **Search:** Enter a value (like an owner ID) in the search field to find specific dashboards.
  * **Pin:** Click push_pin**Pin** to move a dashboard to the top of the list.
  * **Refresh:** Click refresh**Refresh** to update the list with current data.



### Filter the dashboard list

**Note:** You must have the `chronicle.nativeDashboards.list` IAM permission to filter the dashboard list.

To find specific metrics or owners by applying logical filters to the list, narrow your view as follows:

  1. Click filter_alt**Filter**.
  2. Select a logical operator and select a column.
  3. Select a value in the **Show only** list, and then select the appropriate values.
  4. Optional: Click **Add Filter** to add multiple filters.
  5. Click **Apply** to apply the selected filters and filter the list of dashboards. 
     * Anticipated failure: The list doesn't update or display an error.
     * Corrective step: Verify you have the `chronicle.nativeDashboards.list` permission.



### Delete filters

Remove active filters to return to the full list of available dashboards or to apply new criteria, as follows:

  1. Click filter_alt**Filter**.
  2. Click delete**Delete** next to the specific filter you want to remove.
  3. Click **Apply** to remove the filter and update the dashboard list based on the selected filters. 
     * Anticipated failure: The dashboard list remains filtered after you click delete**Delete**.
     * Corrective step: Click **Apply** after you remove the filter_alt**Filter** to trigger the list refresh.



## View a dashboard

Access the full visualization of your ingested telemetry to begin data analysis, as follows:

  1. Go to the **Dashboards** page.
  2. Click a dashboard name to open the view. 
     * Anticipated failure: The dashboard name isn't clickable or results in a permission error.
     * Corrective step: Confirm you have the `chronicle.nativeDashboards.get` IAM permission.



## Create a new dashboard

You can create a dashboard by starting with a blank canvas, copying an existing built-in dashboard, or importing a JSON file.

### Build from a blank template

To build a specialized view for unique monitoring requirements, follow these steps:

  1. On the **Dashboards** page, click **Create Dashboard**.
  2. In the **Create Dashboard** window, enter a name and description.
  3. In the **Start with Existing Dashboard** list, select **Blank Dashboard**.
  4. Under **Access settings** , set the access to either **private** or **shared**. 
     * **Private:** Visible only to you. These remain hidden from all other users, including Google SecOps and Google Cloud project administrators.
     * **Shared:** Accessible to all users within your Google SecOps instance.
  5. Click **Create**. To begin adding data, you can [add a chart to the dashboard](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#add-a-chart) or [add a chart from the chart library](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#add-a-chart-from-the-chart-library).



### Copy an existing dashboard

To save time, you can copy a predefined curated dashboard or an existing shared dashboard as a starting point.

**Note:** You must have the `chronicle.nativeDashboards.duplicate` IAM permission to make a copy of the dashboard.

To make a copy of an existing dashboard, do the following:

  1. On the **Dashboards** page, click more_vert**Menu** next to the dashboard name.
  2. Click **Duplicate**. 
     * Anticipated failure: The **Duplicate** option is missing from the menu.
     * Corrective step: Confirm you have the `chronicle.nativeDashboards.duplicate` permission.



## Edit an existing dashboard

Control the metadata and filter settings of your visualizations. After creation, the **Edit Dashboard** page opens automatically.

  1. On the **Dashboards** page, click more_vert**Menu** , and then click **Edit Dashboard**.
  2. Click **Edit Details** to update the dashboard name, description, or access settings.
  3. Click **Save**.
  4. Click filter_alt**Filter** to edit dashboard-level filters. For more information, see [Filters in dashboard](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters).
  5. On the **Manage filters** screen, click edit **Edit** to modify a specific chart. 
     * Anticipated failure: The edit icons are non-responsive. Corrective step: Confirm you have the `chronicle.nativeDashboards.update` IAM permission.



## Change dashboard access

By default, new dashboards are private. Shared dashboards are visible to all members of the team who can view dashboards in Google SecOps. Only the dashboard owner can change this setting.

  1. Select the dashboard you want to share.
  2. Click more_vert**Menu** next to the dashboard name.
  3. Click **Share** > **Save**. 
     * Anticipated failure: The **Share** option is disabled.
     * Corrective step: Make sure you're the original owner of the dashboard and have the `chronicle.nativeDashboards.update` permission.



## Delete a dashboard

**Note:** You must have the `chronicle.nativeDashboards.delete` IAM permission to delete the dashboard.

To delete a dashboard, do the following:

  1. On the **Dashboards** page, click more_vert**Menu** next to the dashboard name.
  2. Click **Delete**.
  3. Click **Confirm**. 
     * Anticipated failure: You can't delete a shared dashboard created by another user.
     * Corrective step: Contact the owner or an administrator with `chronicle.nativeDashboards.delete` permissions.



## Import or export a dashboard

Use JSON specifications to move dashboard configurations between instances or to back up complex layouts.

### Export to JSON

Download your dashboard configuration, including layout and filter settings, to a local file.

  1. On the **Dashboards** page, click more_vert**Menu** next to the dashboard name.
  2. Click **Export**. The file downloads to your machine. 
     * **Note:** Do not modify the exported JSON file manually. Altering the code prevents successful re-importing.



### Import from JSON

Create a dashboard instantly by uploading a valid JSON configuration file.

  1. On the **Dashboards** page, click **Create Dashboard** > **Import from JSON**.
  2. Browse and select your JSON file. **Note:** Dashboards built using Looker capabilities aren't supported to import.
  3. Click **Edit** to update the name, description, and access settings.
  4. Click **Save** > **Import**.



## Download reports

**Note:** The **Download report** button is initially disabled and becomes available once all charts have finished loading.

Extract dashboard data into portable formats for offline analysis once all charts have finished loading. Use the following guidelines to select the appropriate format for your needs:

  * **PDF and PNG** : These formats capture only the data visible on your screen. They don't include the full chart dataset if the data extends beyond the viewable area.

  * **CSV (dashboard level)** : This generates a ZIP file containing a separate CSV file for every chart on the dashboard.

  * **CSV (Cchart level)** : You can download a report for a specific chart as a CSV file independently to capture its full dataset.




### Download a dashboard report

  1. On the **Dashboards** page, click more_vert**Menu** next to the dashboard or chart name.
  2. Click **Download report**.
  3. Select the file type: **CSV** , **PDF** , or **PNG**.



## Troubleshooting

Resolve common interface issues, permission errors, or data loading delays.

### Error remediation

Use this table to identify and fix common issues encountered during dashboard management.

Error | Issue | Fix  
---|---|---  
**Download disabled** | The **Download report** button remains disabled. | Wait for all charts to finish loading. The button activates only after the full dataset renders.  
**Import failed** | JSON file fails to upload or displays a schema error. | Verify the file was not edited. Dashboards with Looker-specific capabilities are unsupported.  
**Dashboard missing** | A dashboard shared by a teammate isn't visible. | Check the **Dashboards** list filters. Verify the "Shared" view is active and clear search criteria.  
**No results when filtering dasboards** | Unable to filter dashboards using fields structured as key-value pairs in built-in dashboards. | To filter by key-value pairs, apply two filters: 1. Filter on the field's `.key` (for example, `detection.detection.rule_labels.key`) with the specific key name. 2. Filter on the field's `.value` (for example, `detection.detection.rule_labels.value`) with the required value.  
  
### Validation and testing

Follow these steps to confirm your dashboard is correctly configured and accessible to the intended audience:

  1. Open the newly created or imported dashboard to verify all charts load.
  2. Check the **Access settings** on the **Edit Details** menu to confirm visibility (**Private** or **Shared**).
  3. Test the **Download report** feature to confirm that the resulting file contains the expected datasets.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
