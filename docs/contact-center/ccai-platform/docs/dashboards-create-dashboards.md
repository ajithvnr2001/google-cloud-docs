---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-create-dashboards/
title: Creating a Dashboard from a Look or an Explore \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:25.852242+00:00
---

# Creating a Dashboard from a Look or an Explore  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-create-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)



Send feedback 

#  Creating a Dashboard from a Look or an Explore Stay organized with collections  Save and categorize content based on your preferences. 

To create a dashboard from a **Look** or an **Explore** :

  1. Open a Look or an Explore.

  2. Click on the gear in the dashboard content navigation bar. A menu will open.

![A menu with options to save a dashboard.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboard-content-navigation-bar.png)

  3. Select **Save** from the menu.

  4. Select **As new dashboard** from the submenu.

This opens a **Save as a new Dashboard** window.

![The settings for saving a new dashboard.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/save-as-a-new-dashboard.png)

  5. On the **Settings** tab in the **Title** field, enter a name for your new dashboard.

The name that you enter applies to both the tile and the dashboard. You can modify title names at any time. To change the tile name for a query tile, see the **Editing a query tile** title subsection on the **Editing user-defined dashboards** documentation page. To change the dashboard name, enter **edit mode on the dashboard**.

  6. Select the folder where you want to save your dashboard. You must have the **Manage Access, Edit** access level for the folder.

  7. On the **Filters** tab, select whether to use the Look's or Explore's filters as the dashboard filters. Custom filters can't become dashboard filters, but they do remain as tile filters.

  8. Click **Save**.

The Look or Explore will be saved as a query tile on the dashboard.




## Adding tiles and text to a dashboard

Once you've created a dashboard, the next step is to add tiles and text to the dashboard.

The first tile you add to a dashboard takes up the entire width of the dashboard. Additional tiles you add are sized to one-third of the dashboard's width and are added horizontally under the first tile. Additional rows of tiles are added as necessary. You can **move and resize** tiles however you like. You can also **edit tiles** once you've created them to adjust the names of the tiles, the visualizations, or the underlying queries or Looks.

For any new tiles that are added to a dashboard, if they were created from the same Explore as a dashboard filter, the dashboard filter is automatically applied to that tile.

**Note:** Think about the number and complexity of tiles and other elements that you add to a dashboard. More elements require more browser resources, which increases dashboard rendering time.

### Types of dashboard tiles

There are two types of tiles you can add to a dashboard:

  * **Look-linked tiles**

  * **Text tiles**




#### Look-linked tiles

Look-linked tiles are added to a dashboard **from a Look**.

A Look-linked tile links the tile's underlying query to a Look. That Look is used when creating the tile and every time the dashboard is refreshed. The Look and the dashboard must be in the same **folder**. If you want to add Looks from a different folder, first **copy** the Look into the same folder as the dashboard.

A Look-linked tile is a good choice if you want to create, change, and test a query in one place but use it in multiple dashboards. If the Look changes, any tiles linked to that Look change. If the Look is deleted, dashboards show an error for the tile.

#### Text tiles

Text tiles are **built directly within a dashboard**.

You can use text tiles to define visual sections on a dashboard and to add descriptions. Text tiles in dashboards are designed to have flexible formatting and to default to look more like headings and descriptions than tiles.

There are two types of text tiles, each of which offers a different editing experience but results in the same kind of tile:

  * **Text** : a dashboard text tile that provides a visual editing experience

  * **Markdown** : our pre-existing text tile option, which lets you use **some HTML** and a **subset** of the Markdown markup language to style the output of the tile




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
