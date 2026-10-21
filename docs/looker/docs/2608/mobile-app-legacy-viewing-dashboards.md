---
url: https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-viewing-dashboards/
title: Viewing dashboards in the Looker Mobile (Legacy) app \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:43.505664+00:00
---

# Viewing dashboards in the Looker Mobile (Legacy) app  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-viewing-dashboards/

You are viewing documentation for Looker 26.8. Click this link to see the [most recent documentation](https://docs.cloud.google.com/looker/docs/intro). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Viewing dashboards in the Looker Mobile (Legacy) app Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** The Looker Mobile (Legacy) application will be deprecated on August 31, 2026. Use the [Looker application](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) instead.

You can view [user-defined dashboards](https://docs.cloud.google.com/looker/docs/2608/viewing-dashboards) and [LookML dashboards](https://docs.cloud.google.com/looker/docs/2608/building-lookml-dashboards) on your mobile device in the Looker Mobile (Legacy) app. You can also [view Looks](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-viewing-looks) in the app.

## Opening a dashboard

You can navigate to dashboards from the [**Recently Viewed** and **Favorites** screens](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content), while [viewing a board](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#navigating_to_content_from_boards) that you follow, or while [browsing content in folders](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#browsing_content_in_folders) in the Looker Mobile (Legacy) app.

To open a dashboard in the app, select the [content card](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#content_cards) for the dashboard:

![Content card for the Business Overview dashboard shows a visual preview of the dashboard, the dashboard title, and the name of the dashboard creator.](https://docs.cloud.google.com/static/looker/docs/images/mobile-select-dashboard-716.png)

You can also [search for a specific dashboard](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#searching_your_most_recently_viewed_or_favorite_content) on the **Recently Viewed** and **Favorites** screens.

To open a LookML dashboard in the app, navigate to the **LookML Dashboards** [folder](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#browsing_content_in_folders) and select the dashboard. If a LookML dashboard has been [pinned to a board](https://docs.cloud.google.com/looker/docs/2608/presenting-content#adding_content_to_a_board) that you have [added to your list of boards](https://docs.cloud.google.com/looker/docs/2608/presenting-content#adding_a_board_to_your_list), you can open the LookML dashboard while [viewing that board in the app](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#navigating_to_content_from_boards).

## Viewing a dashboard

Dashboards include the following elements:

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-new-dashboard-2104.png)

  1. **Back button** : Returns you to the previous screen.
  2. **Dashboard title** : Displays the title of the dashboard.
  3. **Three-dot menu**: Provides the options to add or remove the dashboard from your favorites, share the dashboard, copy the link to the dashboard, or view information about the dashboard.
  4. **Dashboard last updated indicator** : Shows how recently the data on the dashboard has been queried from (or "refreshed" from) the database.
  5. **Reload data icon** : [Updates the data](https://docs.cloud.google.com/looker/docs/2608/viewing-dashboards#updating_data_on_dashboards_\(beta\)) on the dashboard. This is often useful after filters have been changed.
  6. **Dashboard filters** : Shows any dashboard filters that have been [added to a dashboard](https://docs.cloud.google.com/looker/docs/2608/filters-user-defined-dashboards#adding_dashboard_filters). You can temporarily change dashboard filter values while in the app to see how the data changes.
  7. **Folder icon** : Opens the **Folder Content** sidebar, which lets you [browse the folders that you can access](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#browsing_content_in_folders) while viewing the dashboard.
  8. **Dashboards tiles** : Displays one or more dashboard tiles in a single vertical column.



## Switching between portrait mode and landscape mode

When you view a dashboard or [a Look](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-viewing-looks) in the Looker Mobile (Legacy) app, you can rotate the screen of your mobile device to switch between portrait mode and landscape mode.

Content displays in portrait mode by default. Portrait mode can be useful for viewing multiple dashboard tiles on the screen at once.

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-dashboard-portrait-716.png)

In landscape mode, dashboard tiles expand horizontally to fill the width of the screen. Landscape mode can be useful for viewing the details of one tile at a time.

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-dashboard-landscape-716.png)

## Temporarily changing filter values

Looker [dashboards](https://docs.cloud.google.com/looker/docs/2608/viewing-dashboards) can have one or more [filters](https://docs.cloud.google.com/looker/docs/2608/filtering-and-limiting) that affect one or more dashboard tiles.

You can temporarily change the values of dashboard filters to see how the data changes. You will not affect anyone else's dashboard results by changing the filter values temporarily in the app.

Dashboards display a filter icon and the number of filters that have been added at the top of the dashboard in the mobile app. To view the filters that have been added to a dashboard, select the filter icon or the text indicating the number of filters that have been added.

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-new-dash-filter-section-2104.png)

You can temporarily change the value for a dashboard filter. For example, a dashboard has an [advanced control](https://docs.cloud.google.com/looker/docs/2608/filters-user-defined-dashboards#using_advanced_controls) filter on a field called **State**. To change the filter, select **is any value**.

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-new-dash-filters-expanded-2104.png)

Next, begin typing the new filter value that you want to apply to the dashboard. If the value that is entered is **California** , the filter `State is any value` will change to `State is California`.

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-new-dash-filters-enter-value-2104.png)

Then, select the reload data icon to see how the filter value changes affect your data.

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-new-dash-filters-update-2104.png)

For more information on making temporary changes to filter values on dashboards, see the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/2608/viewing-dashboards#temporarily_changing_filter_values_on_dashboards) documentation page.

## Using the dashboard three-dot menu

The Looker Mobile (Legacy) app displays a three-dot menu at the top of a dashboard. Select the three-dot menu for a user-defined dashboard to use the following options:

  * **Add to Favorites** or **Remove from Favorites**: Add a dashboard to your favorites, or remove a dashboard from your favorites.
  * **Share**: Share a link to a dashboard from your mobile device.
  * **Copy link**: Copy the link to a dashboard.
  * **Get info**: View information about a dashboard, including its title, information about views and favorites, the date the dashboard was created, and the name of the user who created the dashboard.



The three-dot menu for a [LookML dashboard](https://docs.cloud.google.com/looker/docs/2608/building-lookml-dashboards) includes the options to share the dashboard or copy the link to the dashboard.

You can also access the three-dot menu for a dashboard from the [**Recently Viewed** and **Favorites** screens](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content), a [board](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#navigating_to_content_from_boards), or a [folder](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#browsing_content_in_folders) that contains the dashboard.

### Adding or removing a dashboard from your favorites

The [**Favorites** screen](https://docs.cloud.google.com/looker/docs/2608/mobile-app-legacy-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content) in the Looker Mobile (Legacy) app lists the user-defined dashboards that have you added to your favorites.

To add a dashboard to your favorites while viewing the dashboard, or from the **Recently Viewed** screen, a board, or a folder:

  1. Select the three-dot menu for the dashboard.
  2. Choose **Add to Favorites**.



To remove a dashboard from your favorites while viewing the dashboard, or from the **Recently Viewed** screen, the **Favorites** screen, a board, or a folder:

  1. Select the three-dot menu for a dashboard that you added to your favorites.
  2. Choose **Remove from Favorites**.



### Sharing a dashboard

You can share dashboards with other users using the sharing options available on your mobile device, or with a third-party service that is [integrated with Looker](https://docs.cloud.google.com/looker/docs/2608/admin-panel-platform-actions#list_of_integrated_services), such as [Slack](https://slack.com/).

### Copying the link to a dashboard

You can copy the link to a dashboard to your mobile device's clipboard:

  1. Select the three-dot menu for the dashboard.
  2. Select **Copy link**.



After you copy a link, the app displays the message **Link copied to clipboard**.

### Viewing information about a dashboard

Select **Get info** from the three-dot menu for a user-defined dashboard to view the following information:

  * **Title** : Shows the title of the dashboard, the number of views, and the number of favorites
  * **Created** : Displays the date the dashboard was created and the name of the user who created it



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
