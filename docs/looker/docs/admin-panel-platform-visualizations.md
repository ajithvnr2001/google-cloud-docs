---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations/
title: Admin settings - Visualizations \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:23:16.684572+00:00
---

# Admin settings - Visualizations  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Visualizations Stay organized with collections  Save and categorize content based on your preferences. 

Looker includes a robust list of built-in [visualization types](https://docs.cloud.google.com/looker/docs/visualization-types), letting you chart your data in a variety of ways. If you need a type of chart that is not included in Looker's built-in visualization types, Looker provides several ways to add custom JavaScript visualizations to your Looker instance:

  1. Add a `visualization` parameter to your LookML project's manifest file to add custom visualizations directly to your LookML project. See the [`visualization`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization) parameter documentation page for more information.
  2. Install a visualization from the Looker Marketplace. With the [**Marketplace**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace) feature enabled, you can install Looker Marketplace visualization packages.
  3. Use the **Visualizations** page in the **Platform** section of Looker's **Admin** menu to install and administer custom JavaScript visualizations from Looker's custom visualizations repository.



This page describes how to add custom JavaScript visualizations using the **Visualizations** page in the Looker **Admin** panel.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Viewing a list of custom visualizations

To obtain full functionality of downloaded visualizations, admins for customer-hosted deployments should make sure to install the appropriate version of the [Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium).

The **Visualizations** page in the **Platform** section of Looker's **Admin** menu lists all the custom visualizations that have been added to your Looker instance.

The list includes the following columns:

  * **ID** : The unique ID assigned to the custom visualization. This value is assigned either in the JavaScript code, or when you add or edit a visualization using the **Admin** page, or in the visualization's [`id`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#id) parameter when you [add a visualization using the LookML project manifest file](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization).
  * **Label** : The name given to the visualization type in the Looker visualization menu. This value is assigned when you add or edit a visualization using the Admin page, or in the visualization's [`label`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#label) parameter when you [add a visualization using the LookML project manifest file](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization).
  * **Main** : The URI of the visualization's main JavaScript code. This value is assigned when you add or edit a visualization using the Admin page, or in the visualization's [`url`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#url) parameter when you [add a visualization using the LookML project manifest file](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization).
  * **Actions** : Buttons to edit or delete the visualization configuration. These buttons are not shown for visualizations added using the [LookML project's manifest file](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization). To edit these visualizations, go to the LookML project's manifest file and edit the [`visualization`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization) parameter directly.



## Sourcing a custom visualization

You can obtain visualizations to customize and add to your Looker instance from a variety of sources, including the following:

  * Looker maintains a library of custom visualizations for public use on this [Looker GitHub page](https://github.com/looker-open-source/custom_visualizations_v2). You can find instructions for using Looker's Visualization API to create your own visualization types on this [Looker GitHub page](https://github.com/looker-open-source/custom_visualizations_v2/blob/master/docs/getting_started.md).
  * The standalone Looker Marketplace, where you can browse for visualizations — called "plug-ins" — and access their source code.
  * The Looker Marketplace that is accessible from your Looker instance. From this Marketplace, you can browse and install visualizations directly into your Looker instance. See the [Using the Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) documentation page for more information about installing visualizations from the Looker Marketplace.



## Adding a new custom visualization

Once you know which visualization you'd like to add to your instance, you can use the The **Visualizations** page in the **Platform** section of Looker's **Admin** menu to add a custom visualization by selecting the **Add Visualization** button.

Looker displays the **New Visualization:** page. To add a new visualization, perform the following steps:

  1. In the **ID** field, enter the unique ID of the visualization defined in the visualization JavaScript.

  2. In the **Label** field, enter the name of the visualization. Looker displays this name in the Looker visualization menu on an Explore.

  3. In the **Main** field, enter the URI of the visualization's main JavaScript file to point Looker to your JavaScript code repository.

  4. If the site that hosts your custom visualization code uses a [subresource integrity (SRI) hash](https://en.wikipedia.org/wiki/Subresource_Integrity) for verification purposes, enter the SRI hash in the **SRI Hash** field. This field can be found under **Advanced options**. Looker's custom visualization hosts don't use an SRI hash.

  5. In the **Dependencies** field, enter the URIs of any other files that the visualization JavaScript is dependent upon, and click **Add**. You can enter multiple URIs separated by commas, or you can add multiple URIs one at a time. The **Dependencies** field can be found under **Advanced options**.

  6. Select **Save**.




Once the visualization has been added, you will see it as you've labeled it in the visualization menu in an Explore. You can use the new visualization type like any of Looker's existing visualization types.

To view custom visualizations from the visualization menu:

  1. Select the **`...`** three-dot icon from the [visualization menu bar](https://docs.cloud.google.com/looker/docs/creating-visualizations#quick_guide) to access the custom visualization.

  2. Once the visualization is selected, the name of the visualization appears on the visualization menu bar.




## Editing a custom visualization

To edit an existing visualization, select the **Edit** button to the right of the visualization. Looker displays the same page that you use to add a visualization (described in Adding a new custom visualization), but with the relevant information already filled in. Make any preferred changes, and then click **Save**.

## Deleting a custom visualization

To delete a visualization, select the **Delete** button to the right of the visualization on the **Visualizations** page in the **Platform** section of Looker's **Admin** menu, and then click **OK** in the confirmation box.

Deleting a visualization removes it from Looker but won't affect anything in the visualization's external code repository.

Deleting a visualization disables any Looks or dashboards that use that visualization type. You can correct that by adding back the deleted visualization with the same visualization ID.

## Troubleshooting

Custom visualizations are a community-supported effort. Looker's support team does not troubleshoot issues relating to custom visualizations or your custom visualization code. For tracking and closing out bugs, use GitHub issues in the custom visualization's repository, or visit the [Looker Community](https://discuss.google.dev/c/looker/19) for how-to posts, conversations, and tips regarding custom visualizations.

### Blank custom visualizations in PDF or PNG exports

Custom visualizations in PDF or PNG downloads render as blank on Looker (Google Cloud core) private connections instances that lack outbound internet access. This issue occurs because the Chromium renderer cannot fetch external JavaScript dependencies (such as D3 or jQuery) that are hosted on public content delivery networks (CDNs) when outbound access is restricted.

To resolve this issue, use one of the following workarounds:

  * **Bundle dependencies in your LookML project:**
    1. Download the required external dependency `.js` file.
    2. Copy and paste the raw dependency code at the top of your custom visualization `.js` file.
    3. Save the bundled `.js` file in your LookML project.
    4. Update the `manifest.lkml` file to point to the local file by using the [`file`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#file) parameter instead of external URLs in `dependencies` or `url`.
    5. Deploy the changes to production so that Looker serves the dependencies locally.
  * **Configure outbound connections for Private Service Connect:** For instances that use Private Service Connect, [configure outbound (southbound) connections](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound) to let the instance reach external services and public CDNs.



For more information about troubleshooting renderer issues, see [Troubleshooting the Chromium renderer](https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-chromium-renderer).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
