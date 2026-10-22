---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters/
title: Filter case and alert data \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:33.512541+00:00
---

# Filter case and alert data  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Filter case and alert data

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how filters can help narrow your search in the case queue to target only the cases you want to review. Case queue filters help streamline your workflow by surfacing only the cases you need to act on. Whether you're triaging high-priority alerts, reviewing cases in a specific environment, or collaborating with a SOC team, filters offer flexible control using `AND`, `OR`, `IS`, and `IS_NOT` conditions. 

The following filters are available: Timeframe, Alert names, Analysts, Environments, Priorities, Products, Stages, Tags, and Playbook Status.

**Note:** When filtering cases by SOC roles (such as `Tier2`), select **Include users associated with selected roles** to include both direct role assignments and individual users assigned to that role. To do this, select the **Include users associated with selected roles** checkbox. When this option is selected, the system displays all cases assigned directly to the role or to any user within that role. For example, if "Alex Smith" is a member of `Tier2`, any case assigned to them will appear when you filter by `Tier2`. 

## Add a filter

Define custom filters to customize your case queue view. 

To add a new filter, follow these steps: 

  1. Click ![filtericon](https://docs.cloud.google.com/static/chronicle/images/soar/filtericon.png)**Cases Filter**. 
  2. In the **Case Queue Filter** dialog, fill in the required filter conditions. For example, to display high-priority cases that are _not_ in the investigation stage in the past 24 hours: 
     * Set the **Time Frame** to `Last 24 hours`.
     * Set the first condition to `Priorities` `IS` `High`.
     * Set the second condition `Stages` `IS_NOT` `Investigation`. 
  3. Optional: To save the filter for future use, click **Save Filter** and enter a name. The filter is saved under  keyboard_arrow_down **Saved Filters** in the case queue header for future use.
  4. Click **Apply**.



## Share case queue filters

You can share your case queue filters with other individual users, specific SOC roles (like Tier 1 analysts), or all users. 

Filters shared with you or by you display a **Shared** icon next to their name.

To share a filter, your permission group must have the **Allow sharing case queue filters** permission enabled. This permission is enabled by default for the **Admin** group. For more information about enabling permissions, see [Edit a permission group](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups#edit-a-permission-group). 

To share your case queue filters, follow these steps:

  1. Add a new filter by following the steps in Add a filter.
  2. Click **Save Filter**.
  3. In the **Save filter** dialog, enter a name for the filter and then choose one of the three sharing options: 
     * **Private (only me):** This is the default setting. The filter remains private and visible only to you.
     * **Public (all users):** The filter is visible to all users who have access to cases.
     * **Specify users & roles:** Select this option to search for and add specific users or predefined SOC roles.
  4. Click **Save**.



## Manage your saved filters

You can edit, rename, change sharing settings, or delete filters you've created. Changes to shared filters apply to everyone they're shared with.

**Note:** You can only manage filters you create. You can't edit or delete filters shared with you. Any changes to shared filters are temporary. 

### Edit a filter

To edit a filter you created, follow these steps:

  1. In the case queue header, click  keyboard_arrow_down **Saved Filters**.
  2. Hold your pointer over the filter you want to manage and click  edit **Edit**.
  3. If the filter is shared, a confirmation dialog appears. Click **Yes** to continue to the **Edit filter** dialog.
  4. Modify the filter criteria or change its sharing configuration.
  5. Click **Save**.



### Temporarily modify a shared filter

To temporarily modify a shared filter, follow these steps:

  1. In the case queue header, click  keyboard_arrow_down **Saved Filters**.
  2. Click the shared filter you want to modify.
  3. In the case queue header, click filter_alt  **Cases Filter** to modify the filter, and apply changes.

**Note:** These changes are temporary and won't be saved. 

### Delete a filter

You can delete any filter you created. If the filter is shared, it will also be removed from other users' filter lists.

To delete a filter, follow these steps:

  1. Hold your pointer over the filter you want to delete and click  delete  **Delete**.
  2. In the confirmation dialog, click **Yes** to delete the filter.

**Note:** You can also delete the filter from the **Edit filter** dialog. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
