---
url: https://docs.cloud.google.com/looker/docs/merge-queries-new-explore/
title: Joining data from multiple queries in the new Explore experience \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:30.319603+00:00
---

# Joining data from multiple queries in the new Explore experience  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/merge-queries-new-explore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Joining data from multiple queries in the new Explore experience Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The new Explore experience includes the **Join data** page, which lets you join two or more queries and display the query results as if they were one query.

**Note:** For a more detailed description of how Looker joins or merges queries, see the classic Explore [Merging results from different Explores](https://docs.cloud.google.com/looker/docs/merged-results) documentation page.

## Required roles

To join queries, you must have the **User** [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) or another role that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission.

## Accessing the new Explore experience

To access the new Explore experience, the [**New Looker Explore and Merge Query Experience**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#new-looker-explore-and-merge-query-experience) preview feature must be enabled for your instance. The preview feature is enabled by default. If it is disabled, and you aren't a Looker admin, ask an admin to enable the feature.

From an [Explore page](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores), click **Try the new Explore** to navigate to the new Explore experience for all Explores that you interact with.

From the [Merge Results page](https://docs.cloud.google.com/looker/docs/merged-results), click **Try the new Merge Results** to navigate to the new Explore experience **Join data** page.

## Joining queries

To join the results from multiple queries, follow these steps:

  1. [Create the first source query](https://docs.cloud.google.com/looker/docs/creating-primary-query), which is called the _primary query_.
  2. Add the next source query.
  3. Optionally, you can configure join rules for the joined query.
  4. Optionally, visualize the merged query.
  5. After you've created the joined query, you can save or share the joined query.
  6. Optionally, you can modify the joined query.



### Creating the primary query

To join the results from multiple queries, start by preparing the _primary_ query by selecting an Explore from the **Explore** menu and then selecting the dimensions and measures of interest from the field picker. Alternatively, select a Look or dashboard, and click **Explore from here** on the Look, or from a dashboard tile.

This is all you need to start merging results. However, you can also further refine your query in the following optional ways:

  * Add [filters](https://docs.cloud.google.com/filtering-and-limiting-new-explore-experience) for the data.
  * Include [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to create ad hoc metrics.
  * Click **Run** to see the results of your primary query and to test your filters and table calculations.



### Adding the next source query

Once you've created your primary Explore query, add another source query by following these steps:

  1. In your Explore **Configure** panel, click **Merge queries (join data)**. This opens the **Join data** page.
  2. In the **Add join** window, choose the method that you'll use to add another source query:

     * **Build a new query from an Explore** : Looker displays a list of Explores. Choose the Explore that you want to use as a source query, and click **Add query**. Looker will display the **Configure joined fields** page. Select the dimensions and measures for your new query and add any filters, pivots, or custom fields. When you're finished configuring your new source query, click **Save and continue**.
     * **Paste prebuilt query URL** : In the **Add prebuilt query URL** field, enter the URL of the query, Look, or dashboard tile that you want to use as a source query and click **Add query**.
     * **Select Look** : Looker displays a list of Looks. Choose the Look that you want to use as a source query, and click **Add query**.
     * **Select Dashboard tile** : Looker displays a list of dashboards. Choose a dashboard, and then Looker shows a list of tiles on that dashboard. Select a tile and click **Add query**.



### Configuring join rules

In order to join two or more queries, the queries need to have a field in common. For example, if you wanted to add customer data to an Explore of orders, if the orders Explore and the customer query both had a Customer ID field, you would use that field to join the queries.

Once you've selected and configured your primary and additional source queries, Looker will automatically select one or more join fields and create join rules in the **Configure joins** window on the **Join data** page. The primary query and each join rule appear as separate entries under **Source queries and join rules**.

In the **Source queries and join rules** section, you can modify the join rules in the following ways:

  * Change the join field of either the primary query or a source query.
  * Add new join fields.
  * Delete join fields.
  * Make a source query the primary query.
  * Add a new source query by clicking **Add join**.



### Configuring chart style

To visualize your merged queries, click **Select chart** to choose a visualization type. Alternatively, use the **Auto-visualize** option to let Gemini select an appropriate visualization. Then select the **Chart style** to configure the chart options for that chart type.

For a complete guide to all available visualization settings and supported chart types, see [Configuring and editing visualizations in the new Explore experience](https://docs.cloud.google.com/looker/docs/editing-visualizations-new-explore-experience).

### Saving or sharing the joined query

After you've created your joined query, you can click **Save or share** to perform the following actions:

  * **Save to new dashboard** : Looker displays the **Save as a new dashboard** window. Give the new dashboard a title and select a folder where you want the new dashboard to be saved.
  * **Save to existing dashboard** : Looker displays the **Add to a Dashboard in this folder** window. Enter a title for the new dashboard tile, and select the dashboard that you want to save the query to.
  * **Copy URL** : Looker displays the **Share URLs** window, displaying the query's [short URL](https://docs.cloud.google.com/looker/docs/sharing-urls#short_url) and [expanded URL](https://docs.cloud.google.com/looker/docs/sharing-urls#expanded_url).



### Modifying the joined query

After you've created your joined query, you can modify it in the following ways on the **Join data** page:

  * In the **Configure joins** window, select **Edit query** next to the _Primary query_ to open the query's data table and make changes by using the field picker. You can also select **Options** next to the _Primary query_ to rename or delete the primary query.
  * In the **Configure joins** window, select **Edit query** next to the query that you want to modify in the join rule. For each additional source query, you can also select **Options** and rename or delete the query, or make that source query the primary query for the merged queries.
  * In the **Joined fields** tab of the **Joined fields and chart style** window, pivot one or more of the joined query fields and add table calculations.
  * In the **Chart style** tab of the **Joined fields and chart style** window, change the settings of the join query visualization.
  * Use the **Totals** toggle to add or remove totals from the joined query.
  * Click **Change chart** to select a different visualization for your joined query.



After you make any changes, you can view the results of the new joined query by clicking **Run to update**.

## Editing a merge query tile on a dashboard

To edit a merge query tile on a dashboard, follow these steps:

  1. Put the dashboard into [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select **Edit Merged Query** on the tile.
  3. Looker opens the **Join data** page directly within the dashboard edit canvas.
  4. Make your changes to the primary query, additional source queries, join rules, or visualization.
  5. Select **Save** to update the merged queries settings and then select **Save** to update the tile on the dashboard.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
