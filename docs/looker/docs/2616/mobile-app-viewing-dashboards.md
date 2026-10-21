---
url: https://docs.cloud.google.com/looker/docs/2616/mobile-app-viewing-dashboards/
title: Viewing dashboards in the Looker mobile application \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:32.616515+00:00
---

# Viewing dashboards in the Looker mobile application  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2616/mobile-app-viewing-dashboards/

You are viewing documentation for Looker 26.16. Click this link to see the [most recent documentation](https://docs.cloud.google.com/looker/docs/intro). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/2616/intro)



Send feedback 

#  Viewing dashboards in the Looker mobile application Stay organized with collections  Save and categorize content based on your preferences. 

You can view [user-defined dashboards](https://docs.cloud.google.com/looker/docs/2616/viewing-dashboards) and [LookML dashboards](https://docs.cloud.google.com/looker/docs/2616/building-lookml-dashboards) on your mobile device in the Looker mobile application. You can also [view Looks](https://docs.cloud.google.com/looker/docs/2616/mobile-app-viewing-looks) in the app.

## Opening a dashboard

You can navigate to dashboards from the [**Recently Viewed** and **Favorites** screens](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content), while [viewing a board](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#navigating_to_content_from_boards) that you follow, or while [browsing content in folders](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#browsing_content_in_folders) in the Looker mobile app.

To open a dashboard in the app, select the [content card](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#content_cards) for the dashboard.

You can also [search for a specific dashboard](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#searching_your_most_recently_viewed_or_favorite_content) on the **Recently Viewed** and **Favorites** screens.

To open a LookML dashboard in the app, navigate to the **LookML Dashboards** [folder](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#browsing_content_in_folders) and select the dashboard. If a LookML dashboard has been [pinned to a board](https://docs.cloud.google.com/looker/docs/2616/presenting-content#adding_content_to_a_board) that you have [added to your list of boards](https://docs.cloud.google.com/looker/docs/2616/presenting-content#adding_a_board_to_your_list), you can open the LookML dashboard while [viewing that board in the app](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#navigating_to_content_from_boards).

## Viewing a dashboard

Dashboards include the following elements:

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-dashboard-view-2610.png)

  1. **Back button** : Returns you to the previous screen.
  2. **Dashboard title** : Displays the title of the dashboard.
  3. crop_2_3 **Switch to Mobile View** button: Revert to viewing the dashboard tiles in a single column. When you're in **Mobile View** , the button is replaced with the desktop_mac **Switch to Desktop View** button for switching the view to desktop layout.

**Important:** The **Switch to Mobile View** and **Switch to Desktop View** options appear only when your dashboard editor has enabled the [**Preserve desktop layout** setting](https://docs.cloud.google.com/looker/docs/2616/editing-user-defined-dashboards#preserve-desktop-layout).
  4. more_vert **Three-dot menu**: Provides the options to add or remove the dashboard from your favorites, share the dashboard, copy the link to the dashboard, or view information about the dashboard.

  5. **Zoom %** slider: Lets users enlarge tiles when they're viewing dashboards in desktop view.

**Important:** The zoom slider appears only if your dashboard editor has enabled the [**Preserve desktop layout** setting](https://docs.cloud.google.com/looker/docs/2616/editing-user-defined-dashboards#preserve-desktop-layout).
  6. filter_list **Dashboard filters** : Shows any dashboard filters that have been [added to a dashboard](https://docs.cloud.google.com/looker/docs/2616/filters-user-defined-dashboards#adding_dashboard_filters). You can temporarily change dashboard filter values while in the app to see how the data changes.

  7. **Dashboard last updated indicator** : Shows how recently the data on the dashboard has been queried from (or refreshed from) the database.

  8. refresh **Reload data** : [Updates the data](https://docs.cloud.google.com/looker/docs/2616/viewing-dashboards#updating_data_on_dashboards_\(beta\)) on the dashboard. This element is often useful after filters have been changed.

  9. **Dashboard tiles** : Displays one or more dashboard tiles.




## Interacting with data and drilling on dashboards

If your Looker developer has configured interactive elements like [drilling](https://docs.cloud.google.com/looker/docs/2616/drilling-data), [links](https://docs.cloud.google.com/looker/docs/2616/reference/param-field-link), [data actions](https://docs.cloud.google.com/looker/docs/2616/reference/param-field-action), or [custom tooltips](https://docs.cloud.google.com/looker/docs/2616/custom-tooltips), you can interact with dashboard tiles on your mobile device.

Tapping on a data point on a supported dashboard tile displays a tooltip with details or opens a bottom sheet with a menu of options. Depending on how the data and visualization have been configured by your Looker developer, you can do one or more of the following:

  * **Drill into data** : [Drill down into the data](https://docs.cloud.google.com/looker/docs/2616/drilling-data#drilling_down) to view more granular information about the selected data point.
  * **Take configured actions** : [Perform data actions](https://docs.cloud.google.com/looker/docs/2616/reference/param-field-action) directly from the app, such as sending emails, posting messages to Slack, or setting values in other fields.
  * **Open links** : [Open links](https://docs.cloud.google.com/looker/docs/2616/reference/param-field-link) embedded in the visualization to navigate to other Looks or dashboards, or open external websites.
  * **View all underlying data** : Open the drill window and select **Explore all** to view the raw, row-level data that comprises the selected metric.
  * **View custom tooltips** : View [custom tooltips](https://docs.cloud.google.com/looker/docs/2616/custom-tooltips) configured by your developer using Liquid templating or UI settings.



For more information about drilling and configuring links in the mobile app, see the [Drilling in the mobile application](https://docs.cloud.google.com/looker/docs/2616/mobile-app-drilling) documentation page.

### Visualization types that support drilling

The following [visualization types](https://docs.cloud.google.com/looker/docs/2616/visualization-types) and elements support link actions like drilling:

  * **Cartesian charts** : [Column](https://docs.cloud.google.com/looker/docs/2616/column-options), [Bar](https://docs.cloud.google.com/looker/docs/2616/bar-options), [Scatterplot](https://docs.cloud.google.com/looker/docs/2616/scatter-options), [Line](https://docs.cloud.google.com/looker/docs/2616/line-options), [Area](https://docs.cloud.google.com/looker/docs/2616/area-options), [Boxplot](https://docs.cloud.google.com/looker/docs/2616/boxplot-options), and [Waterfall](https://docs.cloud.google.com/looker/docs/2616/waterfall-options) charts.
  * **Pie and donut charts** : [Pie](https://docs.cloud.google.com/looker/docs/2616/pie-options) charts and [Donut Multiples](https://docs.cloud.google.com/looker/docs/2616/donut-multiples-options) charts.
  * **Progression charts** : [Funnel](https://docs.cloud.google.com/looker/docs/2616/funnel-options) charts and [Timeline](https://docs.cloud.google.com/looker/docs/2616/timeline-options) charts.
  * **Maps** : [Google Maps](https://docs.cloud.google.com/looker/docs/2616/google-map-options), [Map](https://docs.cloud.google.com/looker/docs/2616/map-options), [Static Map (Regions)](https://docs.cloud.google.com/looker/docs/2616/map-regions-options), and [Static Map (Points)](https://docs.cloud.google.com/looker/docs/2616/map-points-options) charts.
  * **Text and tables** : [Table](https://docs.cloud.google.com/looker/docs/2616/table-options), [Table (Legacy)](https://docs.cloud.google.com/looker/docs/2616/legacy-table-options), and [Word Cloud](https://docs.cloud.google.com/looker/docs/2616/word-cloud-options) charts. Text tiles are also supported.
  * **Buttons** : Dashboard [buttons](https://docs.cloud.google.com/looker/docs/2616/editing-user-defined-dashboards#adding_buttons) are supported.



While tiles that use other visualization types (including Single Value charts, Single Record charts, and custom or community visualizations) can be viewed in the app, they do not support link actions or drilling.

## Switching between portrait mode and landscape mode

When you view a dashboard or [a Look](https://docs.cloud.google.com/looker/docs/2616/mobile-app-viewing-looks) in the Looker mobile app, you can rotate the screen of your mobile device to switch between portrait mode and landscape mode.

Content is displayed in portrait mode by default. Portrait mode can be useful for viewing multiple dashboard tiles on the screen at once (especially when you're viewing the dashboard in mobile view when your dashboard editor has enabled the [**Preserve desktop layout** setting](https://docs.cloud.google.com/looker/docs/2616/editing-user-defined-dashboards#preserve-desktop-layout)).

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-dashboard-portrait-26-8.png)

In landscape mode, dashboard tiles expand horizontally to fill the width of the screen. Landscape mode can be useful for viewing the details of one tile at a time (or for viewing multiple dashboard tiles on the screen at once when you're viewing the dashboard in desktop view when your dashboard editor has enabled the [**Preserve desktop layout** setting](https://docs.cloud.google.com/looker/docs/2616/editing-user-defined-dashboards#preserve-desktop-layout)).

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-dashboard-landscape-26-8.png)

## Temporarily changing filter values

Looker [dashboards](https://docs.cloud.google.com/looker/docs/2616/viewing-dashboards) can have one or more [filters](https://docs.cloud.google.com/looker/docs/2616/filtering-and-limiting) that affect one or more dashboard tiles.

You can temporarily change the values of dashboard filters to see how the data changes. You won't affect anyone else's dashboard results by changing the filter values temporarily in the app.

Dashboards display a filter icon and the number of filters that have been added at the top of the dashboard in the mobile app. To view the filters that have been added to a dashboard, select the filter icon or the text indicating the number of filters that have been added.

You can temporarily change the value for a dashboard filter. Select a filter value, change its value, and reload the data to see how the filter value changes affect your data.

For more information on making temporary changes to filter values on dashboards, see the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/2616/viewing-dashboards#temporarily_changing_filter_values_on_dashboards) documentation page.

## Using the dashboard three-dot menu

The Looker mobile app displays a more_vert three-dot menu on the dashboard. Select the three-dot menu for a user-defined dashboard to use the following options:

  * **Add to Favorites** or **Remove from Favorites**: Add a dashboard to your favorites, or remove a dashboard from your favorites.
  * **Share**: Share a link to a dashboard from your mobile device.
  * **Copy link**: Copy the link to a dashboard.
  * **Get info**: View information about a dashboard, including its title, information about views and favorites, the date the dashboard was created, and the name of the user who created the dashboard.



The three-dot menu for a [LookML dashboard](https://docs.cloud.google.com/looker/docs/2616/building-lookml-dashboards) includes the options to share the dashboard or copy the link to the dashboard.

You can also access the three-dot menu for a dashboard from the [**Recently Viewed** and **Favorites** screens](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content), a [board](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#navigating_to_content_from_boards), or a [folder](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#browsing_content_in_folders) that contains the dashboard.

### Adding or removing a dashboard from your favorites

The [**Favorites** screen](https://docs.cloud.google.com/looker/docs/2616/mobile-app-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content) in the Looker mobile app lists the user-defined dashboards that you have added to your favorites.

To add a dashboard to your favorites while viewing the dashboard, or from the **Recently Viewed** screen, a board, or a folder:

  1. Select the more_vert three-dot menu for the dashboard.
  2. Choose **Add to Favorites**.



To remove a dashboard from your favorites while viewing the dashboard, or from the **Recently Viewed** screen, the **Favorites** screen, a board, or a folder:

  1. Select the more_vert three-dot menu for a dashboard that you added to your favorites.
  2. Choose **Remove from Favorites**.



### Sharing a dashboard

You can share dashboards with other users with the sharing options that are available on your mobile device, or with a third-party service that's [integrated with Looker](https://docs.cloud.google.com/looker/docs/2616/actions-overview#list_of_integrated_services), such as [Slack](https://slack.com/).

### Copying the link to a dashboard

You can copy the link to a dashboard to your mobile device's clipboard:

  1. Select the more_vert three-dot menu for the dashboard.
  2. Select **Copy link**.



After you copy a link, the app displays the message **Link copied to clipboard**.

### Viewing information about a dashboard

Select **Get info** from the more_vert three-dot menu for a user-defined dashboard to view the following information:

  * **Title** : Shows the title of the dashboard, the number of views, and the number of favorites
  * **Created** : Displays the date the dashboard was created and the name of the user who created it



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
