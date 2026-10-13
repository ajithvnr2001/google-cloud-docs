---
url: https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console/
title: Inspect assets that are monitored by Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:51.800597+00:00
---

# Inspect assets that are monitored by Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Inspect assets that are monitored by Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how to view, query, and inspect cloud assets, helping to improve your security posture, remediate security issues, and respond to threats.

In Security Command Center, some of the actions that you can perform on assets include the following:

  * View all assets
  * Search for assets
  * Inspect asset details
  * View high-value resources



For the Premium and Enterprise (Deprecated) service tiers, you can edit asset queries and view high-value resource sets.

## Obtain the required permissions

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

This section lists the IAM roles that you need to work with assets in the console.

### Google Cloud console IAM roles

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To work with assets in the Google Cloud console, you need the following IAM roles.

Make sure that you have the following role or roles on the project: 

  * **Security Center Assets Viewer** (`roles/securitycenter.assetsViewer`) 



#### Check for the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### Grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. Click **Select a role** , then search for the role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



For more information about Security Command Center roles and permissions, see [IAM for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org).

### Security Operations console IAM roles

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

If you are a Security Command Center Enterprise customer, then you can work with assets in the Security Operations console. You need any of the following IAM roles:

  * **Chronicle SOAR Admin** (`roles/chronicle.soarAdmin`)
  * **Chronicle SOAR Threat Manager** (`roles/chronicle.soarThreatManager`)
  * **Chronicle SOAR Vulnerability Manager** (`roles/chronicle.soarVulnerabilityManager`)



For information about granting the role to a user, see [Map and authorize users using IAM](https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops).

## List of assets in Security Command Center

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Assets are listed in the query results of the **Assets** page in the Google Cloud console.

If Security Command Center is activated at the [organization level](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation), then you can view assets for your entire organization or you can filter assets by specific projects, resource types, and location.

If Security Command Center is activated at the [project level](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_project-level_activation), then you can filter assets by resource type and location in the Google Cloud console.

The list of assets is provided by Cloud Asset Inventory. In most cases, Cloud Asset Inventory updates the list within minutes after assets are created, modified, or removed in your Google Cloud environment.

Because Cloud Asset Inventory data is global and not subject to [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) controls, the **Assets** page shows all assets in your selected organization or project, regardless of whether data residency is enabled or which jurisdictional Google Cloud console you are using.

For more information about Cloud Asset Inventory, see [Introduction to Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview).

## View all assets

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Select your Google Cloud organization or project.



## Sort assets

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To sort assets, click the column heading for the value that you want to sort by. Columns are sorted by numeric and then alphabetical order.

## Search for assets

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

By default, all assets in the organization or project are displayed in the query results. To search for specific assets in Security Command Center, you can use quick filters or specify custom filters.

### Perform a high-level search using quick filters

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To perform a high-level search of your assets, you can use quick filters. For example, you can search by project, resource type, or location. For more information, click the tab for your service tier.

### Standard-legacy, Standard, or Premium

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. In the **Quick filters** section, select one or more attribute filters to add them to a query.



### Enterprise

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Click one of the following tabs to filter resources: 
     * **Google Cloud resources**
     * **AWS resources**
     * **Azure resources**
     * **AI resources**
     * **High value resource set**
  3. For the **AI resources** tab only: This tab displays your organization's discovered AI asset inventory, including Gemini models, fine-tuned models, custom models, data sources (such as Gemini Enterprise Agent Platform datasets), endpoints, pipelines, AI agents, Model Context Protocol (MCP) servers, and notebooks. **Note:** Shadow AI resources (unsanctioned or unmanaged AI assets and workloads) are not supported in the Security Command Center in the Google Cloud console. 

Use the **AI resources** tab to monitor the security posture of your AI workloads, investigate potential AI security risks or threats, verify compliance of AI deployments, or examine assets associated with AI Protection findings.

To view and filter AI resources on the tab, follow these steps:

     1. To view a specific collection of AI assets, select a category tab: **Models** , **Endpoints** , **Data sources** , **Pipelines** , **Agents** , **MCP servers** , or **Notebooks**. The default view displays Gemini models. Discovery of MCP servers requires the App Hub API (`apphub.googleapis.com`) to be enabled in each project that hosts an MCP server.
     2. Use the quick filters in the sidebar to narrow results by project, location, or specific attribute values.
     3. Click an asset's name in the results table to inspect its full metadata, related findings, change history, and associated IAM policies.
  4. To filter for resources that have specific attribute values, follow these steps: 
     1. In the **Filters** section, click an attribute value and click **Show only**. The query is updated accordingly. 
     2. To add another attribute value to the query, click the attribute value and click **and show only**.
     3. To remove an attribute value from the query, click the attribute value and click **Do not show only**.
  5. To copy an attribute value, click the attribute value and click **Copy**.



### Edit asset queries

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To learn how to edit asset queries, click the tab for your service tier.

### Premium

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Click the **Asset query** tab.
  3. Edit the query in any of the following ways: 
     * On the **Query library** subtab, click **Apply query** next to a prebuilt query to select it. The query in the **Edit query** section updates.
     * On the **Query library** subtab, select a prebuilt query. Click **Apply**. The query in the **Edit query** section updates.
     * In the **Select table** section, click the asset type that you want to query on. On the **Schema** subtab, find the attribute that you want to add to the query. The attribute is added to the **Edit query** section.
     * Edit the query directly in the **Edit query** section.
  4. Click **Run**. The query results update.



### Enterprise

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets in the Enterprise tier](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Make sure you are on the **Google Cloud Resources** tab.
  3. Click **Asset query**.
  4. Edit the query in any of the following ways: 
     * On the **Query library** subtab, click **Apply query** next to a prebuilt query to select it. The query in the **Edit query** section updates.
     * On the **Query library** subtab, select a prebuilt query. Click **Apply**. The query in the **Edit query** section updates.
     * In the **Select table** section, click the asset type that you want to query on. On the **Schema** subtab, find the attribute that you want to add to the query. The attribute is added to the **Edit query** section.
     * Edit the query directly in the **Edit query** section.
  5. Click **Run**. The query results update.



### Filter assets

For information about how to filter assets, click the tab for your service tier.

### Standard-legacy, Standard, or Premium

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. On the **Google Cloud** subtab, click in the field next to filter_list**Filter**. A menu of filtering options opens.
  3. To filter the list, select a property and enter a value. Press `Enter` to filter assets or to add additional filtering properties.
  4. To add another filter, follow these steps: 
     1. Click in the field next to filter_list**Filter**.
     2. You can set the logical relationship between the properties. You can select `OR`. Otherwise, Security Command Center defaults to `AND` as the logical operator.
     3. Select an attribute and enter a value.
     4. Repeat these steps to continue filtering.
  5. Press `Enter` to filter assets.



### Enterprise

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets in the Enterprise tier](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Click one of the following tabs to filter resources: 
     * **Google Cloud resources**
     * **AWS resources**
     * **Azure resources**
     * **AI resources**
     * **High value resource set**
  3. Click filter_alt **Add filter**. The **Filters** dialog appears. This dialog lets you choose supported resource attributes and values.
  4. For **Filter** , select an attribute to filter.
  5. Set the filter evaluation option and attribute value. The available evaluation options differ depending on the attribute that you selected. 
     * To filter for resources that have a specific attribute value, select **Show only**. In the **Value** list, select the attribute value.
     * To filter for resources that have an attribute value containing a specific string, select **Contains**. In the **Value** field, enter the string. 

The **Contains** evaluation option follows the query syntax for the [text partial match operator](https://docs.cloud.google.com/asset-inventory/docs/query-syntax#text_partial_match_colon_operator). It converts your search term into one or more tokens, using special characters as delimiters, and requires an entire token to match. To match only a portion of a token, use an asterisk (`*`) as a [token prefix match indicator](https://docs.cloud.google.com/asset-inventory/docs/query-syntax#examples_token_prefix_match).

     * To filter for resources based on a timestamp, select **Before** or **After**. In the **Value** field, enter the timestamp.
  6. To add another filter, follow these steps: 
     1. Click **Add filter**.
     2. Set the attribute, evaluation option, and attribute value.
     3. Set the logical relationship between the filters. For **Logical operator** , select `AND` or `OR`.
  7. Click **Apply**. The query editor is updated and the query results are filtered accordingly.



## Inspect asset details

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

This section describes how you can learn more about the details of a particular asset.

### View the high-level details

  1. Search for the asset.
  2. In the query results, click the name of the asset. The details section for the asset opens and displays a summary of its details.



### View the full details of an asset

To view all details about an asset, including low-level metadata, follow these steps:

  1. Search for the asset.
  2. In the query results, click the name of the asset. The details section for the asset opens.
  3. Click the **Full metadata** tab. All property names and values of the asset are displayed in a tree structure.
  4. To search for a particular property name or value in the tree, enter the name or value in the filter.



### View the findings related to an asset

**Note:** If data residency is enabled in your organization, the **Findings** tab isn't available. Findings are [subject to data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#scc-resources-subject-to-drz).

  1. Search for the asset.
  2. In the query results, click the name of the asset. The details section for the asset opens.
  3. Click the **Findings** tab. All findings related to the asset are displayed.



### View the changes to an asset

You can compare snapshots of the metadata of an asset to see what has changed.

For information about how to see the changes to an asset over time, click the tab for the console that you are using.

### Standard-legacy, Standard, or Premium

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. In the list of assets, click the name of the asset. The details section for the asset opens.
  3. In the details section for the asset, click the **Change history** tab.
  4. On the **Change history** tab, select both a **Start time** and an **End time**.
  5. In the **Select a record to compare** list on the left, select a snapshot.
  6. In the **Select a record to compare** list on the right, select a snapshot to compare with the first snapshot that you selected. The changes between the two snapshots are highlighted.



### Enterprise

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets in the Enterprise tier](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. In the list of assets, click the name of the asset. The details section for the asset opens.
  3. In the details section for the asset, click the **Change history** tab.
  4. In the **Compare** list on the left, select a snapshot.
  5. In the **Compare** list on the right, select a snapshot to compare with the first snapshot that you selected. The changes between the two snapshots are highlighted.



### View the IAM policies associated with an asset

  1. Search for the asset.
  2. In the query results, click the name of the asset. The details section for the asset opens.
  3. Click the **IAM policies** tab. The IAM policies associated with the asset are displayed.



## View the high-value resource set

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

You can view the [high-value resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#high-value_resources) that Risk Engine included in the last [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_path_simulations). You can also view the [attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores) that Risk Engine calculated for each resource. For more information, click the tab for your service tier.

### Premium

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Click the **High value resource set** tab.
  3. To view the attack path simulation details for the resource, click the resource's attack exposure score. For information about how to interpret the attack paths, see [Attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_paths).



### Enterprise

To view the high-value resource set, follow these steps:

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Click the **High value resource set** tab.
  3. Click the subtab for the cloud provider that you want to view: 
     * To view high-value Google Cloud resources, click **Google Cloud resources**.
     * To view high-value Amazon Web Services (AWS) resources, click **AWS resources**. 
     * To view high-value Microsoft Azure resources, click **Azure resources**. 
  4. To view the details of a resource, click its resource display name.



## Filter assets by timestamp

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You can filter or sort the assets in the results section of the **Assets** page, by their **Created** and **Last updated** timestamps. 

To filter based on the **Created** timestamp, **Last updated** timestamp, or both, click the tab for your service tier. 

### Standard-legacy, Standard, or Premium

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. At the top of the results section on the **Assets** page, place your cursor in the **Filter** field. A menu of filters opens.
  3. Go to the **Create time** or **Update time** section and select one of the time-based filter options. For example, `Update time after`. A filter is added to the **Filter** field. 
  4. In the filter field, type a date in the format `MM/DD/YYYY` and press `Enter` on your keyboard.



The assets in the results section update to show only the assets that match your filter.

### Enterprise

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets in the Enterprise tier](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Click one of the following tabs to filter resources: 
     * **Google Cloud resources**
     * **AWS resources**
     * **Azure resources**
     * **AI resources**
**Note:** You can only filter by resource value on the **High value resource set** tab. 
  3. Click filter_alt **Add filter**. The **Filters** dialog appears. In this dialog, you can choose supported resource attributes and values.
  4. In the **Filter** field, select **Create time** or **Update time**.
  5. Select **Before** or **After**. 
  6. In the **Value** field, type a date in the format `MM/DD/YYYY HH:MM:SS`.
  7. Click **Apply**.



The assets in the results section update to show only the assets that match your filter.

## Customize the asset query results page

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To control screen space, you can customize some of the elements that appear in the query results.

### Hide or display columns

For information about how to hide or display columns in the query results, click the tab for your service tier.

### Standard-legacy, Standard, or Premium

  1. At the top of the results section, click view_column **Columns**.
  2. Select the columns that you want to display.
  3. Clear the selections for columns that you want to hide.
  4. Click **OK** to apply the changes to the query results.



### Enterprise

  1. At the top of the results section, click view_column **Open column selector**. The **Manage columns** menu opens.
  2. Select the columns that you want to display.
  3. Clear the selections for columns that you want to hide.
  4. Close the menu.



### Hide or resize the quick filters section

To increase the screen space for query results, you can hide or resize sections. For more information, click the tab for your service tier.

### Standard-legacy, Standard, or Premium

  * To hide the **Quick filters** side section, click the left arrow first_page.
  * To display the **Quick filters** side section, click the right arrow last_page.
  * To resize the display columns, drag the dividing line left or right.



### Enterprise

  * To hide the **Filters** side section, click chevron_left **Close sidebar**. 
  * To display the **Filters** side section, click chevron_right **Open sidebar**. 



## What's next

  * Annotate assets with [security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets).
  * Learn more about [assets and resources](https://docs.cloud.google.com/security-command-center/docs/assets-resources-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
