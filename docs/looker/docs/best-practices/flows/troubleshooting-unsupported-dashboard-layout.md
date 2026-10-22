---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-unsupported-dashboard-layout/
title: Troubleshooting unsupported layout errors for dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:37.952639+00:00
---

# Troubleshooting unsupported layout errors for dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-unsupported-dashboard-layout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting unsupported layout errors for dashboards Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This error doesn't occur on instances running Looker 26.6.17 or later.

You may see the following warning message on your [tabbed dashboard](https://docs.cloud.google.com/looker/docs/tabbed-dashboards) regarding an unsupported layout, which typically prevents further editing of the dashboard:
    
    
    This dashboard uses layouts that are not supported for dashboards with tabs. Learn more about updating to a supported layout.
    

To resolve the error, you must update the dashboard to a supported layout. This guide outlines the steps to update the dashboard layout to resolve the error.

**Important:** An unsupported layout does not impact scheduled deliveries or file downloads for existing dashboards. These steps are optional for dashboards that won't be edited further (for example, archived dashboards).

## Updating dashboards to a supported layout

**Caution:** Before performing any of the following actions, duplicate the dashboard that you're trying to update to prevent data loss.

If you don't have access to make API calls, please contact your Looker admin for assistance. If you encounter an issue that is not described here, contact [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

To update dashboards to a supported layout, complete the steps outlined in each of the following sections:

  1. Identify unsupported layouts
  2. Update the layout type
  3. Verify the update
  4. Check for duplicate element IDs



Depending on the outcome of step 4, you may also need to complete the steps to Manually recreate the dashboard.

### 1\. Identify unsupported layouts

Use the [Looker API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) or your preferred API tool to call the [`get_dashboard_layout` API endpoint](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout) with the dashboard's `dashboard_id`.

**Tip:** To get the dashboard ID in Looker, open the dashboard to see the URL in your browser; the ID is the numeric value or string that's directly after `/dashboards/`. For example, in `yourinstance.looker.com/dashboards/123`, the ID is `123`. For LookML dashboards, the ID is typically `model_name::dashboard_name`.

Examine the JSON response to find any layout objects where the `type` is not one of the supported types (`newspaper`, for example). Supported types can be found in the [LookML dashboard parameters documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#layout).

For example, the call `GET /dashboard_layouts/{dashboard_id}` produces the following JSON snippet, which shows an unsupported layout type:
    
    
    {
    "id": "120",
    "dashboard_id": "75",
    "type": "drag", ## IDENTIFIED UNSUPPORTED DASHBOARD TYPE
    "active": true,
    "column_width": 0,
    "width": 0,
    "deleted": false,
    "dashboard_title": "tabbed dash with limit tab",
    "dashboard_layout_components": [
      {
        "id": "224",
        "dashboard_layout_id": "120", ## DASHBOARD LAYOUT ID FOR STEP 2
        "dashboard_element_id": "377",
        "row": 0,
        "column": 0,
        "width": 8,
        "height": 6,
        "deleted": false,
        "element_title": "Untitled",
        "element_title_hidden": false,
        "vis_type": "looker_bar",
        "granular_row": 0,
        "granular_column": 0,
        "granular_width": 24,
        "granular_height": 12,
        "can": {
          "create": true,
          "destroy": true,
          "update": true,
          "index": true,
          "show": true
        }
      }
      ]
    }
    

### 2\. Update the layout type

Call the [`update_dashboard_layout` API endpoint](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/update_dashboard_layout) for each unsupported layout ID (`dashboard_layout_id`). Use the `dashboard_layout_id` and `dashboard_id` from the previous step. Set the `type` to `newspaper`, and provide a clear value for `title`, such as "Legacy Layout".

Expanding on the example from step 1, call `PATCH /dashboard_layouts/{dashboard_layout_id}` and provide the following updates:
    
    
    {
      "dashboard_id": "75",
      "type": "newspaper", ## SUPPORTED LAYOUT TYPE
      "active": false,
      "column_width": 0,
      "width": 0,
      "label": "Legacy Layout", ## NEW TITLE
      "description": "",
      "order": 0
    }
    

### 3\. Verify the update

If the API call from step 2 is successful, refresh the dashboard in the Looker UI. You should see a new tab with the name "Legacy Layout" (or the title that you provided), and the warning banner shouldn't appear.

### 4\. Check for duplicate element IDs

Call the `get_dashboard_layout` API again for the dashboard. Carefully inspect the response to ensure that all `dashboard_element_id` values are unique _across all of the tabs_ on the dashboard.

  * If all values for `dashboard_element_id` are unique, **you can now safely edit the dashboard**. You can delete the "Legacy Layout" tab and save the dashboard. **You can stop here.**

  * If you find any duplicate values for `dashboard_element_id` across different tabs, proceed to step 5.




## Manually recreate the dashboard

If you identified any duplicate `dashboard_element_id`s on the dashboard after completing steps 1-4, you will need to manually recreate the dashboard by following the steps in these sections:

  1. Recreate the dashboard tabs and elements
  2. Remove the old elements
  3. Remove the old tabs

**Caution:** It is critical to **Save the dashboard** after completing each of the following steps and proceeding to the next. If you complete all the three steps without saving in between, more errors can occur.

### 1\. Recreate dashboard tabs and elements

Open the dashboard in the Looker UI and [enter edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards). [Create a new, temporary tab](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#add_tabs_to_user-defined_dashboards). From the existing tabs, manually [duplicate all of the tiles and elements](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_tiles) that you want to keep and [move the duplicates](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#move_tiles_to_different_tabs) to the temporary tab that you just created. **Save the dashboard.**

**Note:** You cannot duplicate Look-linked tiles. You must [re-add Look-linked tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_tiles_from_a_look) to the temporary tabs.

### 2\. Remove the old elements

**Caution:** Skipping this step can lead to an error state.

Edit the dashboard again. Delete all of the _original_ tiles and elements from all of the pre-existing tabs (including the "Legacy Layout" tab). Leave only the duplicated tiles on the new temporary tab. **Save the dashboard.**

**Note:** Deleting an element from one tab removes it from other tabs if the tabs share the same `dashboard_element_id`.

### 3\. Remove the old tabs

Edit the dashboard one final time. [Delete all of the old tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#delete_tabs), leaving only the new tab that contains the duplicated elements. Optionally [rename the new tab](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#rename-tabs). **Save the dashboard.**

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
