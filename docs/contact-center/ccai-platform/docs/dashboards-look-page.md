---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-look-page/
title: Looks: Viewing looks, the explore look action gear menu \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:38.739286+00:00
---

# Looks: Viewing looks, the explore look action gear menu  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-look-page/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)



Send feedback 

#  Looks: Viewing looks, the explore look action gear menu Stay organized with collections  Save and categorize content based on your preferences. 

You can view and interact with Looks as much as you want without impacting other users. The only way to impact anyone else is if you select the **Edit** button and make changes.

## Finding and viewing Looks

Looks and dashboards can be organized in several ways:

  * In **folders** (for example, you can have folders named Marketing, Q4 Sales Review, and so on).

    * You can navigate your folders by expanding the list of folders in the **Folders section** of the **left navigation panel**.
  * On your **homepage.**




You can open a Look by selecting the Look's name or thumbnail icon, depending on whether content is organized in **grid view** or **list view**.

## The Look page

**Note:** For Looks that have the **Run on Load** option disabled, the data will not load automatically. Select the **Run** button to load the data. You can learn more on the **Saving and editing Looks** documentation page.

A Look's page consists of the following elements:

![A numbered diagram of the Look Page elements.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/the-look-page.png)

  1. The title of the Look and the **name of the folder** in which it is saved.

     * You can select the heart icon next to the Look's title to add the Look to your **Favorites** folder.
  2. Information about how many rows are in the Look, how long the report took to run, and how old the data is.

  3. How long ago the data was queried (to display the date and time, hover over the relative time information).

  4. The time zone of the data you're viewing, if your admin has enabled **user-specific time zones.**

  5. The **Explore actions gear menu.**

  6. The **Details panel** that displays information about the Look.

  7. The **Filters** section displays a list of **filters** that have been applied to the Look, if any. If the Look was created with adjustable filters, you can temporarily change them to limit the Look to only display the information that you're interested in. Just remember to rerun the query using **Run** button in the upper right after making any changes.

     * Unless you select **Edit** and make the change in **edit mode** , changes to the filters are temporary and do not impact other users.
  8. The **Visualization** section that displays the Look's data.

  9. The **tooltip** that displays additional details about each data point, which you can reveal by hovering over a point on the visualization.

  10. The **Data** table that displays the underlying data of the Look. In the **Data table** , you can adjust the following Look elements:

     * Field **sort order**. Select a column heading (or several using the Shift key) to sort the values in the column. Advanced Reporting will adjust the results and automatically rerun the query if necessary.

     * **Row and column limits**. After making changes to the limits, be sure to select the **Run** button in the upper right to run the query with the new limits.

Unless you select **Edit** and make the change in **edit mode** , changes to the sorting or limits are temporary and do not affect anyone else.

  11. If a field has a description defined, hovering over the table column header in the **Data** table will display the description.

  12. Depending on your permissions, next to each dimension or measure label you may access a gear icon that provides more information.




If you make any changes while viewing a Look, such as changing filters, sorting a column, or changing row limits, you can return to the Look's original settings by selecting **Reset Look**.

As you gain familiarity, you can also select the **Explore from Here** option to use the Look as a starting point for further data exploration. You can start with one set of data and then begin exploring the answers to related questions by changing the filters, changing the visualization, sorting the data differently, or by making other changes.

## The Look Explore actions gear menu

The **Explore actions** gear menu is located in the top navigation menu.

Depending on user **permissions** , the options may include:

  * **Edit** — Edit the query in the Explore view.

  * **Save** — Select this option to:

    * As a new dashboard

    * To an existing dashboard

    * **Save As** \- save the Look in another folder.

  * **Download** — Select this option to **download the contents** of a Look in one of several format options.

  * **Send** — Select this option to **send a Look** as a one-off delivery.

  * **Add to a board** — Select this option to **add a Look** to an existing board.

  * **Schedule** — Select this option to **set a recurring delivery** for a Look.

  * **Edit settings** — Select this option to enable or disable the **Run on Load** or **Public Access** options. Only the **Run on Load** option is enabled by default.

  * **Clear cache and refresh** — Select this option to override any data caching policies and **force new results** to be generated from the database.

  * **Move to trash** — Select this option to **delete** a Look.




## Choosing time zones

**Select the current time zone** displayed in the upper right of the Look page to choose a new time zone.

The time zone setting affects the data returned when filtering for "today", "yesterday", and so on. You can learn more on the **Using time zone settings** documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
